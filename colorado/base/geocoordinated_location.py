import enum
from typing import Any

from colorado.airports import Airports
from colorado.counties import Counties
from colorado.internal import BaseModel


class GeocoordinatedLocation(BaseModel):
    """
    A location with a latitude/longitude pair, as well as a list of containing counties and the nearest Colorado airport.
    """
    latitude: float
    """
    The latitude of the location.
    """

    longitude: float
    """
    The longitude of the location.
    """

    counties: list[Counties]
    """
    A list of counties containing this location.
    """

    nearest_airport: Airports
    """
    The nearest airport to this location.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class GeocoordinatedLocationEnum(enum.Enum):
    """
    An enumeration of GeocoordinatedLocation objects
    """

    def __init__(self, location: GeocoordinatedLocation):
        self._location = location

    @property
    def latitude(self) -> float:
        """
        The latitude of the location.
        :return: The latitude of the location.
        :rtype: float
        """
        return self._location.latitude

    @property
    def longitude(self) -> float:
        """
        The longitude of the location.
        :return: The longitude of the location.
        :rtype: float
        """
        return self._location.longitude

    @property
    def counties(self) -> list[Counties]:
        """
        A list of counties containing this location.
        :return: A list of counties containing this location.
        :rtype: list[Counties]
        """
        return self._location.counties

    @property
    def nearest_airport(self) -> Airports:
        """
        The nearest airport to this location.
        :return: The nearest airport to this location.
        :rtype: Airports
        """
        return self._location.nearest_airport
