"""Tests for the cat_facts_client module."""
from unittest.mock import patch, Mock
from cat_facts.clients.cat_facts_client import CatFactsClient

import pytest
import requests


@pytest.fixture(name="mock_json")
def get_mock_json():
    return [
            {
                "text": "Cat Fact 1",
            },
            {
                "text": "Cat Fact 2",
            },
            {
                "text": "Cat Fact 3",
            }
        ]


class MockResponse:
    """Mock response class."""
    def __init__(self, raise_exc: bool, mock_json):
        """Constructor of mock response"""
        self.raise_exc = raise_exc
        self.mock_json = mock_json

    def raise_for_status(self):
        """Mock raise_for_status method."""
        if self.raise_exc:
            raise requests.exceptions.HTTPError
        
    def json(self):
        """Mock json() method."""
        return self.mock_json


def test_get_cat_facts_success(mock_json):
    """
    Test that success case of get_cat_facts works,
    and that it calls the correct methods.
    """
    test_client = CatFactsClient("some_base_url")
    test_client._make_request = Mock()

    mock_return_value = mock_json

    test_client._make_request.return_value = mock_return_value
    cat_facts = test_client.get_cat_facts()
    expected_cat_facts = [fact["text"] for fact in mock_return_value]
    assert cat_facts == expected_cat_facts
    test_client._make_request.assert_called_once_with("GET", "some_base_url/facts")


@patch("cat_facts.clients.cat_facts_client.logger.exception")
@patch("cat_facts.clients.cat_facts_client.requests.request")
def test__make_request_success(mock_request_method, mock_logger_exception, mock_json):
    """
    Test that _make_request performs correctly
    in the success case, and that it calls the correct
    methods.
    """
    mock_request_method.return_value = MockResponse(False, mock_json)
    test_client = CatFactsClient("some_base_url")

    _make_request_response = test_client._make_request("GET", "some_base_url/facts")
    assert _make_request_response == mock_json
    mock_request_method.assert_called_once_with("GET", "some_base_url/facts", timeout=10)
    mock_logger_exception.assert_not_called()


@patch("cat_facts.clients.cat_facts_client.logger.exception")
@patch("cat_facts.clients.cat_facts_client.requests.request")
def test__make_request_exception(mock_request_method, mock_logger_exception, mock_json):
    """
    Test that _make_request performs correctly
    in the exception case, and that it calls the correct
    methods.
    """
    mock_request_method.return_value = MockResponse(True, mock_json)
    test_client = CatFactsClient("some_base_url")

    _make_request_response = test_client._make_request("GET", "some_base_url/facts")
    assert _make_request_response == []
    mock_request_method.assert_called_once_with("GET", "some_base_url/facts", timeout=10)
    mock_logger_exception.assert_called_once_with("Failed to make GET requests against some_base_url/facts")