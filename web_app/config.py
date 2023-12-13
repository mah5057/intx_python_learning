"""Class to standardize setting and accessing the environment"""

import typing

import envparse  # type: ignore


class Config:
    """Config class, to be instatiated with a schema document"""

    def __init__(self, schema: typing.Dict):  # pylint: disable=redefined-outer-name
        self.schema = schema
        self.env = Config.get_coerced_env(self.schema)

    @staticmethod
    def get_coerced_env(
        schema: typing.Dict,
    ) -> typing.Dict:  # pylint: disable=redefined-outer-name
        """Given a schema document, parse with envparse, and construct
        an environment document and return it
        """
        coerced_env = envparse.Env(**schema)
        return {var_name: coerced_env(var_name) for var_name in schema}

    def get_env_value(self, env_var: str) -> typing.Any:
        """Get a config value contained in an env var.

        :param env_var: The env var containing the config value.
        :returns: The value if it exists in the env, else None.
        """
        if env_var in self.env:
            return self.env[env_var]
        return None


# Config from environment variables
schema = {
    "ENV": {
        # Intended for internal usage
        "cast": str,
        "default": "devel",
    },
    "LOG_LEVEL": {"cast": str, "default": "DEBUG"},
}

config = Config(schema)

# Static config
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
