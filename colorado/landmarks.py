from typing import Any

from colorado.airports import Airports
from colorado.base.geocoordinated_location import GeocoordinatedLocation, GeocoordinatedLocationEnum
from colorado.base.named_location import NamedLocation, NamedLocationEnum, NamedLocationAbbreviations
from colorado.counties import Counties


class Landmark(GeocoordinatedLocation, NamedLocation):
    """
    Represents a landmark in the state of Colorado.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Landmarks(GeocoordinatedLocationEnum, NamedLocationEnum):
    """
    An enumeration of notable landmarks in the state of Colorado.
    """
    PIKES_PEAK = Landmark(
        name="Pikes Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="PPK",
            five_letter="PIKES",
            seven_letter="PIKESPK",
            fourteen_letter="PIKES PEAK"
        ),
        latitude=38.840806,
        longitude=-105.042806,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS,
    )
