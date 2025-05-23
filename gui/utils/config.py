"""Utility functions for GUI application."""

from typing import Any
from core.config import Config
from gui.config_manager import ConfigManager
from gui.settings_manager import SettingsManager

def config_list_from_manager(manager: ConfigManager) -> list[dict[str, Any]]:
    """
    Get a list of config dictionaries from the ConfigManager.
    
    Args:
        manager (ConfigManager): The ConfigManager instance.
    
    Returns:
        list[dict[str, Any]]: A list of dictionaries representing the configs.
    """
    return [cfg.to_dict() for cfg in manager.configs]

def configs_from_config_dicts(dicts: list[dict[str, Any]]) -> list[Config]:
    """
    Converts a list of configuration dictionaries into a list of Config objects.
    This function iterates through each dictionary in the input list and converts
    it to a Config object using the Config.from_dict method.
    Args:
        dicts (list[dict[str, Any]]): A list of dictionaries, where each dictionary
                                     contains configuration parameters.
    Returns:
        list[Config]: A list of Config objects created from the input dictionaries.
    """
    return [Config.from_dict(config) for config in dicts]

def save_config_manager_to_settings(config: ConfigManager, settings: SettingsManager):
    """
    Save the config manager to the settings manager.
    
    Args:
        config (ConfigManager): The ConfigManager instance.
        settings (SettingsManager): The SettingsManager instance.
    """
    settings.set("gameconfigs", config_list_from_manager(config), True)

def load_config_manager_from_settings(settings: SettingsManager, config: ConfigManager):
    """
    Load the config manager from the settings manager.
    
    Args:
        settings (SettingsManager): The SettingsManager instance.
    
    Returns:
        ConfigManager: The loaded ConfigManager instance.
    """
    config.clear()
    config_dicts = settings.get("gameconfigs", [])
    config.add_configs(configs_from_config_dicts(config_dicts))
