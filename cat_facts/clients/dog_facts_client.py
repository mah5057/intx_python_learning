import typing
import requests

from cat_facts import log_config

logger = log_config.get_logger(__name__)

class DogFactsClient:
    """
    General purpose client for the dog facts api
    """

    def __init__(self, base_url: str,) -> None:
        """
        Constructor
        :param: base_url - The base url for all API requests
        """
        self.base_url = base_url

    def get_dog_facts(self) -> typing.List[str]:
        """
        Method to retrieve random dog facts from the /facts endpoint
        """
        url = self.base_url + "/facts"
        json_response = self._make_request("GET", url)
        
        dog_facts = []
        for obj in json_response["data"]:
            dog_facts.append(obj["attributes"]["body"])
        return dog_facts
    
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

