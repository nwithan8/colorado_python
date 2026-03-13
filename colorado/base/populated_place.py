from typing import Any

from colorado.airports import Airports
from colorado.base.geocoordinated_location import GeocoordinatedLocation, GeocoordinatedLocationEnum
from colorado.base.named_location import NamedLocation, NamedLocationEnum
from colorado.counties import Counties


class PopulatedPlace(GeocoordinatedLocation, NamedLocation):
    """
    A named and geo-coordinated location where people reside.
    """
    def __init__(self, /, **data: Any):
        super().__init__(**data)


class PopulatedPlaceEnum(GeocoordinatedLocationEnum, NamedLocationEnum):
    """
    An enumeration of PopulatedPlace.
    """
    def __init__(self, location: PopulatedPlace):
        super().__init__(location=location)

    @property
    def latitude(self) -> float:
        return self._location.latitude

    @property
    def longitude(self) -> float:
        return self._location.longitude

    @property
    def counties(self) -> list[Counties]:
        return self._location.counties

    @property
    def nearest_airport(self) -> Airports:
        return self._location.nearest_airport
