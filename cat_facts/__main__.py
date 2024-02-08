"""Main entrypoint for the web_app module."""
from flask import Flask

from cat_facts import log_config
from cat_facts.config import config
from cat_facts.clients.cat_facts_client import CatFactsClient
from cat_facts.clients.dog_facts_client import DogFactsClient


app = Flask(__name__)


logger = log_config.get_logger(__name__)


@app.route("/cat")
def cat():
    """Cat endpoint."""
    client = CatFactsClient(config.get_env_value("CAT_FACTS_URL"))
    return client.get_cat_facts()


@app.route("/dog")
def dog():
    """Dog endpoint."""
    client = DogFactsClient(config.get_env_value("DOG_FACTS_URL"))
    return client.get_dog_facts()


def main() -> None:
    """Main method."""
    logger.info("Webapp template operational.")
    # base_url = "https://cat-fact.herokuapp.com"
    # response = requests.get(base_url + "/facts")
    # json_facts = response.json()
    # for fact in json_facts:
    #     logger.info("Cat fact: %s", fact["text"])
    # client = CatFactsClient(config.get_env_value("CAT_FACTS_URL"))
    # cat_facts = client.get_cat_facts()
    # for fact in cat_facts:
    #     logger.info("Cat fact: %s", fact)


if __name__ == "__main__":
    logger.info("Server starting up!")
    app.run(host=config.get_env_value("HOST"))
