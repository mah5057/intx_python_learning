"""Main entrypoint for the web_app module."""
from web_app import log_config


logger = log_config.get_logger(__name__)


def main() -> None:
    """Main method."""
    logger.info("Webapp template operational.")


if __name__ == "__main__":
    main()
