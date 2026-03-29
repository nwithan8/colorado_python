import json
from pathlib import Path
from typing import Any, TypeAlias, Tuple

from colorado.base.with_abbreviations import WithAbbreviations, WithAbbreviationsEnum, Abbreviations
from colorado.base.with_borders import WithBorders, WithBordersEnum
from colorado.base.with_coordinates import WithCoordinatesEnum, WithCoordinates
from colorado.base.with_name import WithName, WithNameEnum
from colorado.internal.geojson import to_polygon_rings, point_in_polygon, PolygonRings

AirportRegionPolygonIndex: TypeAlias = dict[str, list[PolygonRings]]  # geojson_id -> polygons
AIRPORT_REGION_POLYGON_INDEX: AirportRegionPolygonIndex = {}

def _get_airport_region_polygon_index() -> AirportRegionPolygonIndex:
    global AIRPORT_REGION_POLYGON_INDEX
    if not AIRPORT_REGION_POLYGON_INDEX:
        geojson_path = Path(__file__).resolve().parent / "COLORADO_AIRPORT_REGION_BORDERS.geojson"
        with geojson_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        features: list[dict] = data.get("features", [])
        for feature in features:
            props: dict = feature.get("properties", {})
            geometry: dict = feature.get("geometry", {})
            geojson_id: int = feature.get("id")

            geom_type: str = geometry.get("type")
            coords: list[Tuple[float, float]] = geometry.get("coordinates")

            polygons: list[PolygonRings] = []
            if geom_type == "Polygon":
                polygon = to_polygon_rings(coords)
                if polygon:
                    polygons.append(polygon)
            elif geom_type == "MultiPolygon":
                for raw_polygon in coords or []:
                    polygon = to_polygon_rings(raw_polygon)
                    if polygon:
                        polygons.append(polygon)
            else:
                continue

            if polygons:
                AIRPORT_REGION_POLYGON_INDEX.setdefault(geojson_id, []).extend(polygons)

    return AIRPORT_REGION_POLYGON_INDEX


class Airport(WithName, WithAbbreviations, WithCoordinates):
    """
    Represents a major or regional airport in the state of Colorado.
    """

    iata_code: str
    """
    The IATA code used to identify this airport nationally.
    """

    geojson_id: int
    """
    The ID of the airport in the GeoJSON data containing airport region borders.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)

    def coordinates_within_borders(self, latitude: float, longitude: float) -> bool:
        airport_region_polygon_index = _get_airport_region_polygon_index()
        airport_region_polygons = airport_region_polygon_index.get(int(self.geojson_id), [])
        return any(point_in_polygon(latitude, longitude, polygon) for polygon in airport_region_polygons)


class Airports(WithNameEnum, WithAbbreviationsEnum, WithBordersEnum, WithCoordinatesEnum):
    """
    An enumeration of all major and regional airports in the state of Colorado.
    """
    ASPEN_PITKIN = Airport(
        name="Aspen-Pitkin County/Sardy Field",
        iata_code="ASE",
        geojson_id=1,
        abbreviations=Abbreviations(
            three_letter="ASE",
            five_letter="ASE",
            seven_letter="ASE",
            fourteen_letter="ASE"
        ),
        latitude=39.221878,
        longitude=-106.868233,
    )
    COLORADO_SPRINGS = Airport(
        name="City Of Colorado Springs Municipal Airport",
        iata_code="COS",
        geojson_id=3,
        abbreviations=Abbreviations(
            three_letter="COS",
            five_letter="COS",
            seven_letter="COS",
            fourteen_letter="COS"
        ),
        latitude=38.805817,
        longitude=-104.700776,
    )
    CORTEZ = Airport(
        name="Cortez Municipal Airport",
        iata_code="CEZ",
        geojson_id=2,
        abbreviations=Abbreviations(
            three_letter="CEZ",
            five_letter="CEZ",
            seven_letter="CEZ",
            fourteen_letter="CEZ"
        ),
        latitude=37.303002,
        longitude=-108.628044,
    )
    DENVER = Airport(
        name="Denver International Airport",
        iata_code="DEN",
        geojson_id=4,
        abbreviations=Abbreviations(
            three_letter="DEN",
            five_letter="DEN",
            seven_letter="DEN",
            fourteen_letter="DEN"
        ),
        latitude=39.861667,
        longitude=-104.673167,
    )
    DURANGO_LA_PLATA = Airport(
        name="Durango-La Plata County Airport",
        iata_code="DRO",
        geojson_id=5,
        abbreviations=Abbreviations(
            three_letter="DRO",
            five_letter="DRO",
            seven_letter="DRO",
            fourteen_letter="DRO"
        ),
        latitude=37.151528,
        longitude=-107.753778,
    )
    EAGLE = Airport(
        name="Eagle County Regional Airport",
        iata_code="EGE",
        geojson_id=6,
        abbreviations=Abbreviations(
            three_letter="EGE",
            five_letter="EGE",
            seven_letter="EGE",
            fourteen_letter="EGE"
        ),
        latitude=39.64275,
        longitude=-106.915944,
    )
    GRAND_JUNCTION = Airport(
        name="Grand Junction Regional Airport",
        iata_code="GJT",
        geojson_id=8,
        abbreviations=Abbreviations(
            three_letter="GJT",
            five_letter="GJT",
            seven_letter="GJT",
            fourteen_letter="GJT"
        ),
        latitude=39.121499,
        longitude=-108.525486,
    )
    GUNNISON_CRESTED_BUTTE = Airport(
        name="Gunnison-Crested Butte Regional Airport",
        iata_code="GUC",
        geojson_id=9,
        abbreviations=Abbreviations(
            three_letter="GUC",
            five_letter="GUC",
            seven_letter="GUC",
            fourteen_letter="GUC"
        ),
        latitude=38.534333,
        longitude=-106.93175,
    )
    MONTROSE = Airport(
        name="Montrose Regional Airport",
        iata_code="MTJ",
        geojson_id=12,
        abbreviations=Abbreviations(
            three_letter="MTJ",
            five_letter="MTJ",
            seven_letter="MTJ",
            fourteen_letter="MTJ"
        ),
        latitude=38.509806,
        longitude=-107.89425,
    )
    NORTHERN_COLORADO = Airport(
        name="Northern Colorado Regional Airport",
        iata_code="FNL",
        geojson_id=7,
        abbreviations=Abbreviations(
            three_letter="FNL",
            five_letter="FNL",
            seven_letter="FNL",
            fourteen_letter="FNL"
        ),
        latitude=40.451816,
        longitude=-105.011326,
    )
    PUEBLO = Airport(
        name="Pueblo Memorial Airport",
        iata_code="PUB",
        geojson_id=13,
        abbreviations=Abbreviations(
            three_letter="PUB",
            five_letter="PUB",
            seven_letter="PUB",
            fourteen_letter="PUB"
        ),
        latitude=38.289947,
        longitude=-104.498028,
    )
    SAN_LUIS_VALLEY = Airport(
        name="San Luis Valley Regional/Bergman Field",
        iata_code="ALS",
        geojson_id=0,
        abbreviations=Abbreviations(
            three_letter="ALS",
            five_letter="ALS",
            seven_letter="ALS",
            fourteen_letter="ALS"
        ),
        latitude=37.435125,
        longitude=-105.867875,
    )
    SOUTHEAST_COLORADO = Airport(
        name="Southeast Colorado Regional Airport",
        iata_code="LAA",
        geojson_id=11,
        abbreviations=Abbreviations(
            three_letter="LAA",
            five_letter="LAA",
            seven_letter="LAA",
            fourteen_letter="LAA"
        ),
        latitude=38.069704,
        longitude=-102.688494,
    )
    STERLING = Airport(
        name="Sterling Municipal Airport",
        iata_code="STK",
        geojson_id=14,
        abbreviations=Abbreviations(
            three_letter="STK",
            five_letter="STK",
            seven_letter="STK",
            fourteen_letter="STK"
        ),
        latitude=40.614298,
        longitude=-103.264261,
    )
    TELLURIDE = Airport(
        name="Telluride Regional Airport",
        iata_code="TEX",
        geojson_id=15,
        abbreviations=Abbreviations(
            three_letter="TEX",
            five_letter="TEX",
            seven_letter="TEX",
            fourteen_letter="TEX"
        ),
        latitude=37.953806,
        longitude=-107.90875,
    )
    YAMPA_VALLEY = Airport(
        name="Yampa Valley Airport",
        iata_code="HDN",
        geojson_id=10,
        abbreviations=Abbreviations(
            three_letter="HDN",
            five_letter="HDN",
            seven_letter="HDN",
            fourteen_letter="HDN"
        ),
        latitude=40.481194,
        longitude=-107.217667,
    )

    @property
    def iata_code(self) -> str:
        """
        Get the IATA code for this airport.
        :return: The IATA code for this airport.
        :rtype: str
        """
        return self._location.iata_code  # type: ignore
