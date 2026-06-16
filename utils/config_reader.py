import configparser
import os
class ConfigReader:
    @staticmethod
    def get_config(env, key):
        """
        Reads a specific key from the config.ini file for a given environment.
        """
        # Get the absolute path to the config file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, 'config.ini')
        # Initialize parser
        config = configparser.ConfigParser()
        config.read(config_path)
        # Ensure environment section exists!
        env = env.upper()
        if not config.has_section(env):
            raise ValueError(f"Environment '{env}' not found in config.ini")
        return config.get(env, key)