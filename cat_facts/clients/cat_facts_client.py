import typing
import requests

from cat_facts import log_config

logger = log_config.get_logger(__name__)

class CatFactsClient:
    """
    General purpose client for the cat facts api
    """

    def __init__(self, base_url: str,) -> None:
        """
        Constructor
        :param: base_url - The base url for all API requests
        """
        self.base_url = base_url

    def get_cat_facts(self) -> typing.List[str]:
        """
        Method to retrieve random cat facts from the /facts endpoint
        """
        url = self.base_url + "/facts"
        json_response = self._make_request("GET", url)
        
        cat_facts = [fact["text"] for fact in json_response]
        return cat_facts
    
    def _make_request(self, verb: str, url: str, **kwargs) -> typing.List[typing.Dict]:
        """
        Make an actual request, include some error handling
        """
        response = requests.request(verb, url, timeout=10)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            msg = f"Failed to make {verb} requests against {url}"
            logger.exception(msg)
            return []
        return response.json()

