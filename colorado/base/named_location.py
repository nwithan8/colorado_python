import enum
from typing import Any

from pydantic import model_validator

from colorado.internal import BaseModel, validate_attribute_lengths


class NamedLocationAbbreviations(BaseModel):
    """
    A set of abbreviations for named locations.
    """
    three_letter: str
    five_letter: str
    seven_letter: str
    fourteen_letter: str

    def __init__(self, /, **data: Any):
        super().__init__(**data)

    @model_validator(mode="after")
    def validate_model(self):
        lengths = {
            'three_letter': 3,
            'five_letter': 5,
            'seven_letter': 7,
            'fourteen_letter': 14
        }
        validate_attribute_lengths(obj=self, lengths=lengths)

        return self


class NamedLocation(BaseModel):
    """
    A location with a name and set of abbreviations.
    """
    name: str
    """
    The name of the location.
    """

    abbreviations: NamedLocationAbbreviations
    """
    The abbreviations of the location.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class NamedLocationEnum(enum.Enum):
    """
    An enumeration for named locations.
    """
    def __init__(self, location: NamedLocation):
        self._location = location

    @property
    def name(self) -> str:
        """
        The name of the location.
        :return: The name of the location.
        :rtype: str
        """
        return self._location.name

    @property
    def abbreviations(self) -> NamedLocationAbbreviations:
        """
        The abbreviations of the location.
        :return: The abbreviations of the location.
        :rtype: NamedLocationAbbreviations
        """
        return self._location.abbreviations
