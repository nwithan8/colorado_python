from typing import Any

from colorado.airports import Airports
from colorado.base.geocoordinated_location import GeocoordinatedLocation, GeocoordinatedLocationEnum
from colorado.base.named_location import NamedLocation, NamedLocationEnum, NamedLocationAbbreviations


class Mountain(GeocoordinatedLocation, NamedLocation):
    """
    Represents a mountain in the state of Colorado.
    """

    height: float
    """
    The height, in feet, of the mountain.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Mountains(GeocoordinatedLocationEnum, NamedLocationEnum):
    """
    An enumeration of mountains in the state of Colorado.
    """
    ANTHRACITE_RANGE_HIGH_POINT = Mountain(
        name="Anthracite Range High Point",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.8145,
        longitude=-107.1445,
        height=12394.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    ANTORA_PEAK = Mountain(
        name="Antora Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.325,
        longitude=-106.218,
        height=13275.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    BALD_MOUNTAIN = Mountain(
        name="Bald Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.4448,
        longitude=-105.9705,
        height=13690.0,
        nearest_airport=Airports.ASPEN
    )
    BARD_PEAK = Mountain(
        name="Bard Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.7204,
        longitude=-105.8044,
        height=13647.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BENNETT_PEAK = Mountain(
        name="Bennett Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.4833,
        longitude=-106.4343,
        height=13209.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    BILL_WILLIAMS_PEAK = Mountain(
        name="Bill Williams Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.1806,
        longitude=-106.6102,
        height=13389.0,
        nearest_airport=Airports.ASPEN
    )
    BISON_MOUNTAIN = Mountain(
        name="Bison Mountain (Bison Peak)",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.2384,
        longitude=-105.4978,
        height=12432.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BLACK_MOUNTAIN_MOFFAT_COUNTY = Mountain(
        name="Black Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.7835,
        longitude=-107.3691,
        height=10865.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    BLACK_MOUNTAIN_PARK_COUNTY = Mountain(
        name="Black Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.7185,
        longitude=-105.6874,
        height=11659.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BLAIR_MOUNTAIN = Mountain(
        name="Blair Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.7943,
        longitude=-107.4176,
        height=11465.0,
        nearest_airport=Airports.EAGLE
    )
    BLANCA_PEAK = Mountain(
        name="Blanca Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.5775,
        longitude=-105.4856,
        height=14351.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    BUSHNELL_PEAK = Mountain(
        name="Bushnell Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.3412,
        longitude=-105.8892,
        height=13110.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CAPITOL_PEAK = Mountain(
        name="Capitol Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.1503,
        longitude=-107.0829,
        height=14137.0,
        nearest_airport=Airports.ASPEN
    )
    CARBON_PEAK = Mountain(
        name="Carbon Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.7943,
        longitude=-107.0431,
        height=12088.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    CASTLE_PEAK = Mountain(
        name="Castle Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.0097,
        longitude=-106.8614,
        height=14279.0,
        nearest_airport=Airports.ASPEN
    )
    CASTLE_PEAK_SAWATCH_RANGE = Mountain(
        name="Castle Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.7723,
        longitude=-106.8304,
        height=11305.0,
        nearest_airport=Airports.EAGLE
    )
    CHAIR_MOUNTAIN = Mountain(
        name="Chair Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.0581,
        longitude=-107.2822,
        height=12727.0,
        nearest_airport=Airports.ASPEN
    )
    CHALK_BENCHMARK = Mountain(
        name="Chalk Benchmark",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.1418,
        longitude=-106.75,
        height=12038.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CLARK_PEAK = Mountain(
        name="Clark Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.6068,
        longitude=-105.93,
        height=12954.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    COAL_MOUNTAIN = Mountain(
        name="Coal Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.787,
        longitude=-107.4837,
        height=11710.0,
        nearest_airport=Airports.MONTROSE
    )
    COCHETOPA_DOME = Mountain(
        name="Cochetopa Dome",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.2267,
        longitude=-106.7147,
        height=11138.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    COLUMBUS_MOUNTAIN = Mountain(
        name="Columbus Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.8799,
        longitude=-107.1921,
        height=10258.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    CONEJOS_PEAK = Mountain(
        name="Conejos Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.2887,
        longitude=-106.5709,
        height=13179.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CORNWALL_MOUNTAIN = Mountain(
        name="Cornwall Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.3811,
        longitude=-106.492,
        height=12291.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CRATER_PEAK = Mountain(
        name="Crater Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.0396,
        longitude=-107.6628,
        height=11333.0,
        nearest_airport=Airports.MONTROSE
    )
    CRESTED_BUTTE = Mountain(
        name="Crested Butte",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.8835,
        longitude=-106.9436,
        height=12168.0,
        nearest_airport=Airports.ASPEN
    )
    CRESTONE_PEAK = Mountain(
        name="Crestone Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.9669,
        longitude=-105.5855,
        height=14300.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CULEBRA_PEAK = Mountain(
        name="Culebra Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.1224,
        longitude=-105.1858,
        height=14053.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    EAST_BECKWITH_MOUNTAIN = Mountain(
        name="East Beckwith Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.8464,
        longitude=-107.2233,
        height=12441.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    EAST_SPANISH_PEAK = Mountain(
        name="East Spanish Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.3934,
        longitude=-104.9201,
        height=12688.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    ELK_MOUNTAIN = Mountain(
        name="Elk Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.1619,
        longitude=-106.1285,
        height=11424.0,
        nearest_airport=Airports.EAGLE
    )
    ELLIOTT_MOUNTAIN = Mountain(
        name="Elliott Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.7344,
        longitude=-108.058,
        height=12346.0,
        nearest_airport=Airports.TELLURIDE
    )
    FLAT_TOP_MOUNTAIN = Mountain(
        name="Flat Top Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.0147,
        longitude=-107.0833,
        height=12361.0,
        nearest_airport=Airports.EAGLE
    )
    GOTHIC_MOUNTAIN = Mountain(
        name="Gothic Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.9562,
        longitude=-107.0107,
        height=12631.0,
        nearest_airport=Airports.ASPEN
    )
    GRAHAM_PEAK = Mountain(
        name="Graham Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.4972,
        longitude=-107.3761,
        height=12536.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    GRAYS_PEAK = Mountain(
        name="Grays Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.6339,
        longitude=-105.8176,
        height=14278.0,
        nearest_airport=Airports.EAGLE
    )
    GREEN_MOUNTAIN = Mountain(
        name="Green Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.3053,
        longitude=-105.3001,
        height=10427.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GREENHORN_MOUNTAIN = Mountain(
        name="Greenhorn Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.8815,
        longitude=-105.0133,
        height=12352.0,
        nearest_airport=Airports.PUEBLO
    )
    GRIZZLY_PEAK = Mountain(
        name="Grizzly Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.0425,
        longitude=-106.5976,
        height=13995.0,
        nearest_airport=Airports.ASPEN
    )
    HAGUES_PEAK = Mountain(
        name="Hagues Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.4845,
        longitude=-105.6464,
        height=13573.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HANDIES_PEAK = Mountain(
        name="Handies Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.913,
        longitude=-107.5044,
        height=14058.0,
        nearest_airport=Airports.TELLURIDE
    )
    HARDSCRABBLE_MOUNTAIN = Mountain(
        name="Hardscrabble Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.5171,
        longitude=-106.8021,
        height=11171.0,
        nearest_airport=Airports.EAGLE
    )
    HENRY_MOUNTAIN = Mountain(
        name="Henry Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.6856,
        longitude=-106.6211,
        height=13261.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    HESPERUS_MOUNTAIN = Mountain(
        name="Hesperus Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.4451,
        longitude=-108.089,
        height=13237.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    HORSE_MOUNTAIN = Mountain(
        name="Horse Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.308,
        longitude=-107.2864,
        height=9952.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    HUNTSMAN_RIDGE_PEAK_DUTCH_PEAK = Mountain(
        name="Huntsman Ridge Peak (Dutch Peak)",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.192,
        longitude=-107.3668,
        height=11858.0,
        nearest_airport=Airports.ASPEN
    )
    IRON_MOUNTAIN = Mountain(
        name="Iron Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.6375,
        longitude=-105.2538,
        height=11416.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    JACQUE_PEAK = Mountain(
        name="Jacque Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.4549,
        longitude=-106.197,
        height=13211.0,
        nearest_airport=Airports.ASPEN
    )
    KNOBBY_CREST = Mountain(
        name="Knobby Crest",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.3681,
        longitude=-105.605,
        height=12434.0,
        nearest_airport=Airports.DENVER
    )
    LA_PLATA_PEAK = Mountain(
        name="La Plata Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.0294,
        longitude=-106.4729,
        height=14343.0,
        nearest_airport=Airports.ASPEN
    )
    LARAMIE_MOUNTAINS_HP = Mountain(
        name="Laramie Mountains HP",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.7704,
        longitude=-105.7162,
        height=11025.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LITTLE_CONE = Mountain(
        name="Little Cone",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.9275,
        longitude=-108.0908,
        height=11988.0,
        nearest_airport=Airports.TELLURIDE
    )
    LONE_CONE = Mountain(
        name="Lone Cone",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.888,
        longitude=-108.2556,
        height=12618.0,
        nearest_airport=Airports.TELLURIDE
    )
    LONGS_PEAK = Mountain(
        name="Longs Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.255,
        longitude=-105.6151,
        height=14259.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MARCELLINA_MOUNTAIN = Mountain(
        name="Marcellina Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.9299,
        longitude=-107.2438,
        height=11353.0,
        nearest_airport=Airports.ASPEN
    )
    MAROON_PEAK = Mountain(
        name="Maroon Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.0708,
        longitude=-106.989,
        height=14163.0,
        nearest_airport=Airports.ASPEN
    )
    MATCHLESS_MOUNTAIN = Mountain(
        name="Matchless Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.834,
        longitude=-106.6451,
        height=12389.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MIDDLE_PEAK = Mountain(
        name="Middle Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.8536,
        longitude=-108.1082,
        height=13306.0,
        nearest_airport=Airports.TELLURIDE
    )
    MOUNT_ANTERO = Mountain(
        name="Mount Antero",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.6741,
        longitude=-106.2462,
        height=14276.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MOUNT_BLUE_SKY = Mountain(
        name="Mount Blue Sky",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.5883,
        longitude=-105.6438,
        height=14271.0,
        nearest_airport=Airports.DENVER
    )
    MOUNT_CENTENNIAL = Mountain(
        name="Mount Centennial (Peak 13010)",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.6062,
        longitude=-107.2446,
        height=13016.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    MOUNT_ELBERT = Mountain(
        name="Mount Elbert",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.1178,
        longitude=-106.4454,
        height=14440.0,
        nearest_airport=Airports.ASPEN
    )
    MOUNT_GUERO = Mountain(
        name="Mount Guero",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.7196,
        longitude=-107.3861,
        height=12058.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MOUNT_GUNNISON = Mountain(
        name="Mount Gunnison",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.8121,
        longitude=-107.3826,
        height=12725.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MOUNT_HARVARD = Mountain(
        name="Mount Harvard",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.9244,
        longitude=-106.3207,
        height=14421.0,
        nearest_airport=Airports.ASPEN
    )
    MOUNT_HERARD = Mountain(
        name="Mount Herard",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.8492,
        longitude=-105.4949,
        height=13345.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MOUNT_JACKSON = Mountain(
        name="Mount Jackson",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.4853,
        longitude=-106.5367,
        height=13676.0,
        nearest_airport=Airports.EAGLE
    )
    MOUNT_LINCOLN = Mountain(
        name="Mount Lincoln",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.3515,
        longitude=-106.1116,
        height=14293.0,
        nearest_airport=Airports.ASPEN
    )
    MOUNT_MASSIVE = Mountain(
        name="Mount Massive",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.1875,
        longitude=-106.4757,
        height=14428.0,
        nearest_airport=Airports.ASPEN
    )
    MOUNT_MESTAS = Mountain(
        name="Mount Mestas",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.583,
        longitude=-105.1474,
        height=11574.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MOUNT_OSO = Mountain(
        name="Mount Oso",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.607,
        longitude=-107.4936,
        height=13690.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    MOUNT_OURAY = Mountain(
        name="Mount Ouray",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.4227,
        longitude=-106.2247,
        height=13961.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MOUNT_POWELL = Mountain(
        name="Mount Powell",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.7601,
        longitude=-106.3407,
        height=13586.0,
        nearest_airport=Airports.EAGLE
    )
    MOUNT_PRINCETON = Mountain(
        name="Mount Princeton",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.7492,
        longitude=-106.2424,
        height=14204.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    MOUNT_RICHTHOFEN = Mountain(
        name="Mount Richthofen",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.4695,
        longitude=-105.8945,
        height=12945.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MOUNT_SILVERHEELS = Mountain(
        name="Mount Silverheels",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.3394,
        longitude=-106.0054,
        height=13829.0,
        nearest_airport=Airports.ASPEN
    )
    MOUNT_SNEFFELS = Mountain(
        name="Mount Sneffels",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.0038,
        longitude=-107.7923,
        height=14158.0,
        nearest_airport=Airports.TELLURIDE
    )
    MOUNT_WILSON = Mountain(
        name="Mount Wilson",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.8391,
        longitude=-107.9916,
        height=14252.0,
        nearest_airport=Airports.TELLURIDE
    )
    MOUNT_YALE = Mountain(
        name="Mount Yale",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.8442,
        longitude=-106.3138,
        height=14200.0,
        nearest_airport=Airports.ASPEN
    )
    MOUNT_ZIRKEL = Mountain(
        name="Mount Zirkel",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.8313,
        longitude=-106.6631,
        height=12185.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    MOUNT_ZWISCHEN = Mountain(
        name="Mount Zwischen",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.7913,
        longitude=-105.4554,
        height=12011.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MOUNT_OF_THE_HOLY_CROSS = Mountain(
        name="Mount of the Holy Cross",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.4668,
        longitude=-106.4817,
        height=14011.0,
        nearest_airport=Airports.ASPEN
    )
    NORTH_ARAPAHO_PEAK = Mountain(
        name="North Arapaho Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.0265,
        longitude=-105.6504,
        height=13508.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    NORTH_MAMM_PEAK = Mountain(
        name="North Mamm Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.3865,
        longitude=-107.866,
        height=11126.0,
        nearest_airport=Airports.GRAND_JUNCTION
    )
    PARK_CONE = Mountain(
        name="Park Cone",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.7967,
        longitude=-106.6028,
        height=12106.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    PARKVIEW_MOUNTAIN = Mountain(
        name="Parkview Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.3303,
        longitude=-106.1363,
        height=12301.0,
        nearest_airport=Airports.EAGLE
    )
    PARRY_PEAK = Mountain(
        name="Parry Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.8381,
        longitude=-105.7132,
        height=13397.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PIKES_PEAK = Mountain(
        name="Pikes Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.8405,
        longitude=-105.0442,
        height=14115.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PUMA_PEAK = Mountain(
        name="Puma Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.1572,
        longitude=-105.5815,
        height=11575.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    RED_TABLE_MOUNTAIN = Mountain(
        name="Red Table Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.4181,
        longitude=-106.7712,
        height=12043.0,
        nearest_airport=Airports.ASPEN
    )
    RIO_GRANDE_PYRAMID = Mountain(
        name="Rio Grande Pyramid",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.6797,
        longitude=-107.3924,
        height=13827.0,
        nearest_airport=Airports.TELLURIDE
    )
    SAN_LUIS_PEAK = Mountain(
        name="San Luis Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.9868,
        longitude=-106.9313,
        height=14022.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SAND_MOUNTAIN_NORTH = Mountain(
        name="Sand Mountain North",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.7636,
        longitude=-107.0575,
        height=10884.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    SAWTOOTH_MOUNTAIN = Mountain(
        name="Sawtooth Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.274,
        longitude=-106.867,
        height=12153.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SHEEP_MOUNTAIN = Mountain(
        name="Sheep Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.361,
        longitude=-106.2658,
        height=11825.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    SLEEPY_CAT_PEAK = Mountain(
        name="Sleepy Cat Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.1275,
        longitude=-107.5338,
        height=10853.0,
        nearest_airport=Airports.YAMPA_VALLEY
    )
    SOUTH_RIVER_PEAK = Mountain(
        name="South River Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.5741,
        longitude=-106.9815,
        height=13154.0,
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    SPECIMEN_MOUNTAIN = Mountain(
        name="Specimen Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.4449,
        longitude=-105.8081,
        height=12494.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SPRUCE_MOUNTAIN = Mountain(
        name="Spruce Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.1973,
        longitude=-107.522,
        height=10838.0,
        nearest_airport=Airports.ASPEN
    )
    SULTAN_MOUNTAIN = Mountain(
        name="Sultan Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.7859,
        longitude=-107.7038,
        height=13373.0,
        nearest_airport=Airports.TELLURIDE
    )
    SUMMIT_PEAK = Mountain(
        name="Summit Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.3506,
        longitude=-106.6968,
        height=13308.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    THIRTYNINE_MILE_MOUNTAIN = Mountain(
        name="Thirtynine Mile Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.8324,
        longitude=-105.5553,
        height=11553.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    TOMICHI_DOME = Mountain(
        name="Tomichi Dome",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.4849,
        longitude=-106.5291,
        height=11471.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    TOWER_MOUNTAIN = Mountain(
        name="Tower Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.8573,
        longitude=-107.623,
        height=13558.0,
        nearest_airport=Airports.TELLURIDE
    )
    TREASURE_MOUNTAIN = Mountain(
        name="Treasure Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.0244,
        longitude=-107.1228,
        height=13535.0,
        nearest_airport=Airports.ASPEN
    )
    TWILIGHT_PEAK = Mountain(
        name="Twilight Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.663,
        longitude=-107.727,
        height=13163.0,
        nearest_airport=Airports.TELLURIDE
    )
    TWIN_SISTERS_PEAKS = Mountain(
        name="Twin Sisters Peaks",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=40.2886,
        longitude=-105.5175,
        height=11433.0,
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    UNCOMPAHGRE_PEAK = Mountain(
        name="Uncompahgre Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.0717,
        longitude=-107.4621,
        height=14321.0,
        nearest_airport=Airports.TELLURIDE
    )
    UTE_PEAK = Mountain(
        name="Ute Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.2841,
        longitude=-108.7787,
        height=9984.0,
        nearest_airport=Airports.CORTEZ
    )
    VERMILION_PEAK = Mountain(
        name="Vermilion Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.7993,
        longitude=-107.8285,
        height=13900.0,
        nearest_airport=Airports.TELLURIDE
    )
    WAUGH_MOUNTAIN = Mountain(
        name="Waugh Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.6022,
        longitude=-105.6955,
        height=11716.0,
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    WEST_BUFFALO_PEAK = Mountain(
        name="West Buffalo Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.9917,
        longitude=-106.1249,
        height=13332.0,
        nearest_airport=Airports.ASPEN
    )
    WEST_ELK_PEAK = Mountain(
        name="West Elk Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.7179,
        longitude=-107.1994,
        height=13042.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    WEST_SPANISH_PEAK = Mountain(
        name="West Spanish Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.3756,
        longitude=-104.9934,
        height=13631.0,
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    WHETSTONE_MOUNTAIN = Mountain(
        name="Whetstone Mountain",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=38.8223,
        longitude=-106.9799,
        height=12527.0,
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    WILLIAMS_PEAK = Mountain(
        name="Williams Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=39.8552,
        longitude=-106.1854,
        height=11620.0,
        nearest_airport=Airports.EAGLE
    )
    WINDOM_PEAK = Mountain(
        name="Windom Peak",
        abbreviations=NamedLocationAbbreviations(
            three_letter="Three Letter Abbreviation",
            five_letter="Five Letter Abbreviation",
            seven_letter="Seven Letter Abbreviation",
            fourteen_letter="Fourteen Letter Abbreviation"
        ),
        latitude=37.6212,
        longitude=-107.5919,
        height=14093.0,
        nearest_airport=Airports.TELLURIDE
    )

    @property
    def height(self) -> str:
        """
        Get the height, in feet, of the mountain.
        :return: The height, in feet, of the mountain.
        :rtype: float
        """
        return self._location.height  # type: ignore
