from typing import Any

from colorado.base.geocoordinated_location import GeocoordinatedLocation, GeocoordinatedLocationEnum
from colorado.base.named_location import NamedLocation, NamedLocationEnum
from colorado.counties import Counties


class PopulatedPlace(GeocoordinatedLocation, NamedLocation):
    """
    A named and geo-coordinated location where people reside.
    """

    counties: list[Counties]
    """
    A list of counties containing this location.
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
    def counties(self) -> list[Counties]:
        return self._location.counties
