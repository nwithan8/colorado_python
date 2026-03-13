from typing import Any

from colorado.airports import Airports
from colorado.base.named_location import NamedLocationAbbreviations
from colorado.base.populated_place import PopulatedPlace, PopulatedPlaceEnum
from colorado.counties import Counties


class UnincorporatedArea(PopulatedPlace):
    """
    Represents an unincorporated area in the state of Colorado.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class UnincorporatedAreas(PopulatedPlaceEnum):
    """
    An enumeration of unincorporated areas in the state of Colorado.
    """
    HENDERSON = UnincorporatedArea(
        name="Henderson",
        abbreviations=NamedLocationAbbreviations(
            three_letter="HND",
            five_letter="HENDR",
            seven_letter="HENDRSN",
            fourteen_letter="HENDERSON"
        ),
        latitude=39.92054695153314,
        longitude=-104.86581850143858,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
