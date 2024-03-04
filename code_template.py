# File: code_template.py

from typing import Dict

class CodeTemplate:
    """
    A class representing a code template with placeholders
    """
    def __init__(self, template: str):
        """
        Initialize a CodeTemplate object with the given template.

        Args:
            template (str): The template string with placeholders.
        """
        self.template = template
        self.values: Dict[str, str] = {}

    def set_value(self, key: str, value: str) -> None:
        """
        Set the value for a placeholder in the template.

        Args:
            key (str): The placeholder key.
            value (str): The value to be substituted for the placeholder.
        """
        self.values[key] = value

    def render(self) -> str:
        """
        Render the template with substituted values.

        Returns:
            str: The rendered template string.
        """
        return self.template.format(**self.values)
      
