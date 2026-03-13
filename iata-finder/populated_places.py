from typing import Any
    
from colorado.base._base import Place, PlaceEnum, PlaceAbbreviations
from colorado.counties import Counties
from colorado.airports import Airports
    
    
class PopulatedPlace(Place):
    """
    Represents a populated place in the state of Colorado.
    """
        
    latitude: float
    """
    The latitude coordinate of this populated place.
    """
        
    longitude: float
    """
    The longitude coordinate of this populated place.
    """
        
    counties: list[Counties]
    """
    The counties that this populated place is located in.
    """
    
    nearest_airport: Airports
    """
    The nearest airport within Colorado to this populated area.
    """
        
    def __init__(self, /, **data: Any):
            super().__init__(**data)
    
class PopulatedPlaces(PlaceEnum):
    """
    An enumeration of all populated places in the state of Colorado.
    """
    ABARR = PopulatedPlace(
        name="Abarr",
        abbreviations=PlaceAbbreviations(
            three_letter="ABA",
            five_letter="ABARR",
            seven_letter="ABARR",
            fourteen_letter="ABARR"
        ),
        latitude=39.85055049121354,
        longitude=-102.70716268305858,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    ABBEYVILLE = PopulatedPlace(
        name="Abbeyville",
        abbreviations=PlaceAbbreviations(
            three_letter="ABB",
            five_letter="ABBEY",
            seven_letter="ABBEYVI",
            fourteen_letter="ABBEYVILLE"
        ),
        latitude=38.777500784292954,
        longitude=-106.49226014081182,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    ABEYTA = PopulatedPlace(
        name="Abeyta",
        abbreviations=PlaceAbbreviations(
            three_letter="ABE",
            five_letter="ABEYT",
            seven_letter="ABEYTA",
            fourteen_letter="ABEYTA"
        ),
        latitude=37.07974948792338,
        longitude=-104.18637504404398,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    ABLE = PopulatedPlace(
        name="Able",
        abbreviations=PlaceAbbreviations(
            three_letter="ABL",
            five_letter="ABLE",
            seven_letter="ABLE",
            fourteen_letter="ABLE"
        ),
        latitude=38.06056961638046,
        longitude=-102.869653230501,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    ACEQUIA = PopulatedPlace(
        name="Acequia",
        abbreviations=PlaceAbbreviations(
            three_letter="ACE",
            five_letter="ACEQU",
            seven_letter="ACEQUIA",
            fourteen_letter="ACEQUIA"
        ),
        latitude=39.52360578674484,
        longitude=-105.02804989120972,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    ACRES_GREEN = PopulatedPlace(
        name="Acres Green",
        abbreviations=PlaceAbbreviations(
            three_letter="ACR",
            five_letter="ACRES",
            seven_letter="ACRES G",
            fourteen_letter="ACRES GREEN"
        ),
        latitude=39.556661500356654,
        longitude=-104.89610036561157,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    ADAMS_CITY = PopulatedPlace(
        name="Adams City",
        abbreviations=PlaceAbbreviations(
            three_letter="ADA",
            five_letter="ADAMS",
            seven_letter="ADAMS C",
            fourteen_letter="ADAMS CITY"
        ),
        latitude=39.826659235406055,
        longitude=-104.92887730497768,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    ADELAIDE = PopulatedPlace(
        name="Adelaide",
        abbreviations=PlaceAbbreviations(
            three_letter="ADE",
            five_letter="ADELA",
            seven_letter="ADELAID",
            fourteen_letter="ADELAIDE"
        ),
        latitude=38.560001747163824,
        longitude=-105.09082670010639,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ADENA = PopulatedPlace(
        name="Adena",
        abbreviations=PlaceAbbreviations(
            three_letter="ADE",
            five_letter="ADENA",
            seven_letter="ADENA",
            fourteen_letter="ADENA"
        ),
        latitude=40.008324632759525,
        longitude=-103.88662608218448,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    ADNA = PopulatedPlace(
        name="Adna",
        abbreviations=PlaceAbbreviations(
            three_letter="ADN",
            five_letter="ADNA",
            seven_letter="ADNA",
            fourteen_letter="ADNA"
        ),
        latitude=40.339433112467304,
        longitude=-104.82831464231879,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    AGATE = PopulatedPlace(
        name="Agate",
        abbreviations=PlaceAbbreviations(
            three_letter="AGA",
            five_letter="AGATE",
            seven_letter="AGATE",
            fourteen_letter="AGATE"
        ),
        latitude=39.461657452027566,
        longitude=-103.9421905323623,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.DENVER
    )
    AGUILAR = PopulatedPlace(
        name="Aguilar",
        abbreviations=PlaceAbbreviations(
            three_letter="AGU",
            five_letter="AGUIL",
            seven_letter="AGUILAR",
            fourteen_letter="AGUILAR"
        ),
        latitude=37.40279920713442,
        longitude=-104.65332858227504,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    AKIN = PopulatedPlace(
        name="Akin",
        abbreviations=PlaceAbbreviations(
            three_letter="AKI",
            five_letter="AKIN",
            seven_letter="AKIN",
            fourteen_letter="AKIN"
        ),
        latitude=39.25470782436963,
        longitude=-108.26314978552,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    AKRON = PopulatedPlace(
        name="Akron",
        abbreviations=PlaceAbbreviations(
            three_letter="AKR",
            five_letter="AKRON",
            seven_letter="AKRON",
            fourteen_letter="AKRON"
        ),
        latitude=40.16054390057366,
        longitude=-103.21439404027768,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    ALAMO = PopulatedPlace(
        name="Alamo",
        abbreviations=PlaceAbbreviations(
            three_letter="ALA",
            five_letter="ALAMO",
            seven_letter="ALAMO",
            fourteen_letter="ALAMO"
        ),
        latitude=37.65557252521444,
        longitude=-104.95861407682617,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    ALAMO_PLACITA = PopulatedPlace(
        name="Alamo Placita",
        abbreviations=PlaceAbbreviations(
            three_letter="ALA",
            five_letter="ALAMO",
            seven_letter="ALAMO P",
            fourteen_letter="ALAMO PLACITA"
        ),
        latitude=39.720826817291595,
        longitude=-104.97582440348447,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    ALAMOSA = PopulatedPlace(
        name="Alamosa",
        abbreviations=PlaceAbbreviations(
            three_letter="ALA",
            five_letter="ALAMO",
            seven_letter="ALAMOSA",
            fourteen_letter="ALAMOSA"
        ),
        latitude=37.46945514128652,
        longitude=-105.87003156514731,
        counties=[Counties.ALAMOSA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    ALDEN = PopulatedPlace(
        name="Alden",
        abbreviations=PlaceAbbreviations(
            three_letter="ALD",
            five_letter="ALDEN",
            seven_letter="ALDEN",
            fourteen_letter="ALDEN"
        ),
        latitude=40.45748734624118,
        longitude=-104.58191389879642,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ALDER = PopulatedPlace(
        name="Alder",
        abbreviations=PlaceAbbreviations(
            three_letter="ALD",
            five_letter="ALDER",
            seven_letter="ALDER",
            fourteen_letter="ALDER"
        ),
        latitude=38.36944905782468,
        longitude=-106.03947029564802,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    ALGONQUIN_ACRES = PopulatedPlace(
        name="Algonquin Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="ALG",
            five_letter="ALGON",
            seven_letter="ALGONQU",
            fourteen_letter="ALGONQUIN ACRE"
        ),
        latitude=39.59833971103029,
        longitude=-104.82639895443276,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    ALICE = PopulatedPlace(
        name="Alice",
        abbreviations=PlaceAbbreviations(
            three_letter="ALI",
            five_letter="ALICE",
            seven_letter="ALICE",
            fourteen_letter="ALICE"
        ),
        latitude=39.818327084539874,
        longitude=-105.64279006754668,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ALKIRE_ESTATES = PopulatedPlace(
        name="Alkire Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="ALK",
            five_letter="ALKIR",
            seven_letter="ALKIRE ",
            fourteen_letter="ALKIRE ESTATES"
        ),
        latitude=39.8430620224259,
        longitude=-105.14501015672312,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ALLENSPARK = PopulatedPlace(
        name="Allenspark",
        abbreviations=PlaceAbbreviations(
            three_letter="ALL",
            five_letter="ALLEN",
            seven_letter="ALLENSP",
            fourteen_letter="ALLENSPARK"
        ),
        latitude=40.19443584305941,
        longitude=-105.52556518619838,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ALLISON = PopulatedPlace(
        name="Allison",
        abbreviations=PlaceAbbreviations(
            three_letter="ALL",
            five_letter="ALLIS",
            seven_letter="ALLISON",
            fourteen_letter="ALLISON"
        ),
        latitude=37.02445517662784,
        longitude=-107.48811627894196,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    ALMA = PopulatedPlace(
        name="Alma",
        abbreviations=PlaceAbbreviations(
            three_letter="ALM",
            five_letter="ALMA",
            seven_letter="ALMA",
            fourteen_letter="ALMA"
        ),
        latitude=39.283884582644646,
        longitude=-106.06280700139007,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    ALMA_JUNCTION = PopulatedPlace(
        name="Alma Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="ALM",
            five_letter="ALMA ",
            seven_letter="ALMA JU",
            fourteen_letter="ALMA JUNCTION"
        ),
        latitude=39.26749598249586,
        longitude=-106.0453065952517,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    ALMONT = PopulatedPlace(
        name="Almont",
        abbreviations=PlaceAbbreviations(
            three_letter="ALM",
            five_letter="ALMON",
            seven_letter="ALMONT",
            fourteen_letter="ALMONT"
        ),
        latitude=38.66472104455505,
        longitude=-106.8461610077602,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    """
    ALTA_VISTA = PopulatedPlace(
        name="Alta Vista",
        abbreviations=PlaceAbbreviations(
            three_letter="ALT",
            five_letter="ALTA ",
            seven_letter="ALTA VI",
            fourteen_letter="ALTA VISTA"
        ),
        latitude=39.807228621327965,
        longitude=-105.09362124037767,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ALTA_VISTA = PopulatedPlace(
        name="Alta Vista",
        abbreviations=PlaceAbbreviations(
            three_letter="ALT",
            five_letter="ALTA ",
            seven_letter="ALTA VI",
            fourteen_letter="ALTA VISTA"
        ),
        latitude=39.0269408785727,
        longitude=-104.11246932419766,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.DENVER
    )
    """
    """
    ALTURA = PopulatedPlace(
        name="Altura",
        abbreviations=PlaceAbbreviations(
            three_letter="ALT",
            five_letter="ALTUR",
            seven_letter="ALTURA",
            fourteen_letter="ALTURA"
        ),
        latitude=37.183343617530625,
        longitude=-107.19116472926783,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    ALTURA = PopulatedPlace(
        name="Altura",
        abbreviations=PlaceAbbreviations(
            three_letter="ALT",
            five_letter="ALTUR",
            seven_letter="ALTURA",
            fourteen_letter="ALTURA"
        ),
        latitude=39.740271731748464,
        longitude=-104.8044283652523,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    """
    ALVIN = PopulatedPlace(
        name="Alvin",
        abbreviations=PlaceAbbreviations(
            three_letter="ALV",
            five_letter="ALVIN",
            seven_letter="ALVIN",
            fourteen_letter="ALVIN"
        ),
        latitude=40.30777689954556,
        longitude=-102.07575268289492,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    AMERICUS = PopulatedPlace(
        name="Americus",
        abbreviations=PlaceAbbreviations(
            three_letter="AME",
            five_letter="AMERI",
            seven_letter="AMERICU",
            fourteen_letter="AMERICUS"
        ),
        latitude=38.90250132302276,
        longitude=-106.16558468136753,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.ASPEN
    )
    AMES = PopulatedPlace(
        name="Ames",
        abbreviations=PlaceAbbreviations(
            three_letter="AME",
            five_letter="AMES",
            seven_letter="AMES",
            fourteen_letter="AMES"
        ),
        latitude=37.86472256733225,
        longitude=-107.88229854915636,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    ANDERSONVILLE = PopulatedPlace(
        name="Andersonville",
        abbreviations=PlaceAbbreviations(
            three_letter="AND",
            five_letter="ANDER",
            seven_letter="ANDERSO",
            fourteen_letter="ANDERSONVILLE"
        ),
        latitude=40.59387782946453,
        longitude=-105.05720992667938,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ANDRIX = PopulatedPlace(
        name="Andrix",
        abbreviations=PlaceAbbreviations(
            three_letter="AND",
            five_letter="ANDRI",
            seven_letter="ANDRIX",
            fourteen_letter="ANDRIX"
        ),
        latitude=37.27946857791551,
        longitude=-103.19272083118545,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    ANGORA = PopulatedPlace(
        name="Angora",
        abbreviations=PlaceAbbreviations(
            three_letter="ANG",
            five_letter="ANGOR",
            seven_letter="ANGORA",
            fourteen_letter="ANGORA"
        ),
        latitude=40.176644220020705,
        longitude=-108.57566656449643,
        counties=[Counties.RIO_BLANCO],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    ANSEL = PopulatedPlace(
        name="Ansel",
        abbreviations=PlaceAbbreviations(
            three_letter="ANS",
            five_letter="ANSEL",
            seven_letter="ANSEL",
            fourteen_letter="ANSEL"
        ),
        latitude=37.70306285974277,
        longitude=-106.10253694058116,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    ANTERO_JUNCTION = PopulatedPlace(
        name="Antero Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="ANT",
            five_letter="ANTER",
            seven_letter="ANTERO ",
            fourteen_letter="ANTERO JUNCTIO"
        ),
        latitude=38.92333433982225,
        longitude=-105.96530083851911,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    ANTLERS = PopulatedPlace(
        name="Antlers",
        abbreviations=PlaceAbbreviations(
            three_letter="ANT",
            five_letter="ANTLE",
            seven_letter="ANTLERS",
            fourteen_letter="ANTLERS"
        ),
        latitude=39.54332000089806,
        longitude=-107.72785060318137,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    ANTON = PopulatedPlace(
        name="Anton",
        abbreviations=PlaceAbbreviations(
            three_letter="ANT",
            five_letter="ANTON",
            seven_letter="ANTON",
            fourteen_letter="ANTON"
        ),
        latitude=39.741656741143686,
        longitude=-103.21717129247122,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    ANTONITO = PopulatedPlace(
        name="Antonito",
        abbreviations=PlaceAbbreviations(
            three_letter="ANT",
            five_letter="ANTON",
            seven_letter="ANTONIT",
            fourteen_letter="ANTONITO"
        ),
        latitude=37.07918497659148,
        longitude=-106.00864295826494,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    ANVIL_POINTS = PopulatedPlace(
        name="Anvil Points",
        abbreviations=PlaceAbbreviations(
            three_letter="ANV",
            five_letter="ANVIL",
            seven_letter="ANVIL P",
            fourteen_letter="ANVIL POINTS"
        ),
        latitude=39.51609598323529,
        longitude=-107.92285844183846,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    APACHE_CITY = PopulatedPlace(
        name="Apache City",
        abbreviations=PlaceAbbreviations(
            three_letter="APA",
            five_letter="APACH",
            seven_letter="APACHE ",
            fourteen_letter="APACHE CITY"
        ),
        latitude=37.85834886339728,
        longitude=-104.83110696824298,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    APACHE_MESA = PopulatedPlace(
        name="Apache Mesa",
        abbreviations=PlaceAbbreviations(
            three_letter="APA",
            five_letter="APACH",
            seven_letter="APACHE ",
            fourteen_letter="APACHE MESA"
        ),
        latitude=39.73195083112199,
        longitude=-104.79584336281295,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    APPLE_MEADOWS = PopulatedPlace(
        name="Apple Meadows",
        abbreviations=PlaceAbbreviations(
            three_letter="APP",
            five_letter="APPLE",
            seven_letter="APPLE M",
            fourteen_letter="APPLE MEADOWS"
        ),
        latitude=39.80472861238661,
        longitude=-105.21195456732812,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    APPLETON = PopulatedPlace(
        name="Appleton",
        abbreviations=PlaceAbbreviations(
            three_letter="APP",
            five_letter="APPLE",
            seven_letter="APPLETO",
            fourteen_letter="APPLETON"
        ),
        latitude=39.1208203839966,
        longitude=-108.60816164396743,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    APPLEWOOD = PopulatedPlace(
        name="Applewood",
        abbreviations=PlaceAbbreviations(
            three_letter="APP",
            five_letter="APPLE",
            seven_letter="APPLEWO",
            fourteen_letter="APPLEWOOD"
        ),
        latitude=39.75778420926429,
        longitude=-105.16251015053479,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    APPLEWOOD_GLEN = PopulatedPlace(
        name="Applewood Glen",
        abbreviations=PlaceAbbreviations(
            three_letter="APP",
            five_letter="APPLE",
            seven_letter="APPLEWO",
            fourteen_letter="APPLEWOOD GLEN"
        ),
        latitude=39.74528420952748,
        longitude=-105.13445454250291,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    APPLEWOOD_GROVE = PopulatedPlace(
        name="Applewood Grove",
        abbreviations=PlaceAbbreviations(
            three_letter="APP",
            five_letter="APPLE",
            seven_letter="APPLEWO",
            fourteen_letter="APPLEWOOD GROV"
        ),
        latitude=39.74361750906962,
        longitude=-105.14584344476043,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    APPLEWOOD_VILLAGE = PopulatedPlace(
        name="Applewood Village",
        abbreviations=PlaceAbbreviations(
            three_letter="APP",
            five_letter="APPLE",
            seven_letter="APPLEWO",
            fourteen_letter="APPLEWOOD VILL"
        ),
        latitude=39.765562012536975,
        longitude=-105.13306574437877,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ARA = PopulatedPlace(
        name="Ara",
        abbreviations=PlaceAbbreviations(
            three_letter="ARA",
            five_letter="ARA",
            seven_letter="ARA",
            fourteen_letter="ARA"
        ),
        latitude=40.02499203961651,
        longitude=-105.2502773019147,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ARAPAHOE = PopulatedPlace(
        name="Arapahoe",
        abbreviations=PlaceAbbreviations(
            three_letter="ARA",
            five_letter="ARAPA",
            seven_letter="ARAPAHO",
            fourteen_letter="ARAPAHOE"
        ),
        latitude=38.85001367854085,
        longitude=-102.18213704753413,
        counties=[Counties.CHEYENNE],
        nearest_airport=Airports.PUEBLO
    )
    ARBOLES = PopulatedPlace(
        name="Arboles",
        abbreviations=PlaceAbbreviations(
            three_letter="ARB",
            five_letter="ARBOL",
            seven_letter="ARBOLES",
            fourteen_letter="ARBOLES"
        ),
        latitude=37.028066581218525,
        longitude=-107.41922526403204,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    ARCHER = PopulatedPlace(
        name="Archer",
        abbreviations=PlaceAbbreviations(
            three_letter="ARC",
            five_letter="ARCHE",
            seven_letter="ARCHER",
            fourteen_letter="ARCHER"
        ),
        latitude=39.53332798446087,
        longitude=-105.07694030439092,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ARGO_MILL = PopulatedPlace(
        name="Argo Mill",
        abbreviations=PlaceAbbreviations(
            three_letter="ARG",
            five_letter="ARGO ",
            seven_letter="ARGO MI",
            fourteen_letter="ARGO MILL"
        ),
        latitude=39.74277228346136,
        longitude=-105.50667362745145,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.DENVER
    )
    ARICKAREE = PopulatedPlace(
        name="Arickaree",
        abbreviations=PlaceAbbreviations(
            three_letter="ARI",
            five_letter="ARICK",
            seven_letter="ARICKAR",
            fourteen_letter="ARICKAREE"
        ),
        latitude=39.69915904503779,
        longitude=-103.06605915226896,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    ARISTOCRAT_RANCHETTES = PopulatedPlace(
        name="Aristocrat Ranchettes",
        abbreviations=PlaceAbbreviations(
            three_letter="ARI",
            five_letter="ARIST",
            seven_letter="ARISTOC",
            fourteen_letter="ARISTOCRAT RAN"
        ),
        latitude=40.10915618587029,
        longitude=-104.76247979931179,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    ARLINGTON = PopulatedPlace(
        name="Arlington",
        abbreviations=PlaceAbbreviations(
            three_letter="ARL",
            five_letter="ARLIN",
            seven_letter="ARLINGT",
            fourteen_letter="ARLINGTON"
        ),
        latitude=38.33612112797198,
        longitude=-103.34327607070878,
        counties=[Counties.KIOWA],
        nearest_airport=Airports.PUEBLO
    )
    ARMEL = PopulatedPlace(
        name="Armel",
        abbreviations=PlaceAbbreviations(
            three_letter="ARM",
            five_letter="ARMEL",
            seven_letter="ARMEL",
            fourteen_letter="ARMEL"
        ),
        latitude=39.79722122384214,
        longitude=-102.10825263303144,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    AROYA = PopulatedPlace(
        name="Aroya",
        abbreviations=PlaceAbbreviations(
            three_letter="ARO",
            five_letter="AROYA",
            seven_letter="AROYA",
            fourteen_letter="AROYA"
        ),
        latitude=38.85417051838721,
        longitude=-103.12549897321003,
        counties=[Counties.CHEYENNE],
        nearest_airport=Airports.PUEBLO
    )
    ARRIBA = PopulatedPlace(
        name="Arriba",
        abbreviations=PlaceAbbreviations(
            three_letter="ARR",
            five_letter="ARRIB",
            seven_letter="ARRIBA",
            fourteen_letter="ARRIBA"
        ),
        latitude=39.286106171651454,
        longitude=-103.2755051561436,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ARRIOLA = PopulatedPlace(
        name="Arriola",
        abbreviations=PlaceAbbreviations(
            three_letter="ARR",
            five_letter="ARRIO",
            seven_letter="ARRIOLA",
            fourteen_letter="ARRIOLA"
        ),
        latitude=37.44249816031305,
        longitude=-108.64621766964461,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    ARROWHEAD = PopulatedPlace(
        name="Arrowhead",
        abbreviations=PlaceAbbreviations(
            three_letter="ARR",
            five_letter="ARROW",
            seven_letter="ARROWHE",
            fourteen_letter="ARROWHEAD"
        ),
        latitude=40.579155630598166,
        longitude=-105.02443101730785,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ARROWHEAD_VILLAGE = PopulatedPlace(
        name="Arrowhead Village",
        abbreviations=PlaceAbbreviations(
            three_letter="ARR",
            five_letter="ARROW",
            seven_letter="ARROWHE",
            fourteen_letter="ARROWHEAD VILL"
        ),
        latitude=39.63438829477394,
        longitude=-106.56704945524967,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    ARROWOOD = PopulatedPlace(
        name="Arrowood",
        abbreviations=PlaceAbbreviations(
            three_letter="ARR",
            five_letter="ARROW",
            seven_letter="ARROWOO",
            fourteen_letter="ARROWOOD"
        ),
        latitude=40.18721374320347,
        longitude=-105.51084238169824,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ARVADA = PopulatedPlace(
        name="Arvada",
        abbreviations=PlaceAbbreviations(
            three_letter="ARV",
            five_letter="ARVAD",
            seven_letter="ARVADA",
            fourteen_letter="ARVADA"
        ),
        latitude=39.802770821209435,
        longitude=-105.08749433847447,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ASHCROFT = PopulatedPlace(
        name="Ashcroft",
        abbreviations=PlaceAbbreviations(
            three_letter="ASH",
            five_letter="ASHCR",
            seven_letter="ASHCROF",
            fourteen_letter="ASHCROFT"
        ),
        latitude=39.053607500517614,
        longitude=-106.7997708404751,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    ASPEN = PopulatedPlace(
        name="Aspen",
        abbreviations=PlaceAbbreviations(
            three_letter="ASP",
            five_letter="ASPEN",
            seven_letter="ASPEN",
            fourteen_letter="ASPEN"
        ),
        latitude=39.19110451823167,
        longitude=-106.81754916020952,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    ASPEN_CREEK = PopulatedPlace(
        name="Aspen Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="ASP",
            five_letter="ASPEN",
            seven_letter="ASPEN C",
            fourteen_letter="ASPEN CREEK"
        ),
        latitude=39.945284242385355,
        longitude=-105.05473234797302,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    ASPEN_MEADOWS = PopulatedPlace(
        name="Aspen Meadows",
        abbreviations=PlaceAbbreviations(
            three_letter="ASP",
            five_letter="ASPEN",
            seven_letter="ASPEN M",
            fourteen_letter="ASPEN MEADOWS"
        ),
        latitude=39.97638182147119,
        longitude=-105.41333833435982,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ASPEN_PARK = PopulatedPlace(
        name="Aspen Park",
        abbreviations=PlaceAbbreviations(
            three_letter="ASP",
            five_letter="ASPEN",
            seven_letter="ASPEN P",
            fourteen_letter="ASPEN PARK"
        ),
        latitude=39.53916137069251,
        longitude=-105.29472495582291,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ATCHEE = PopulatedPlace(
        name="Atchee",
        abbreviations=PlaceAbbreviations(
            three_letter="ATC",
            five_letter="ATCHE",
            seven_letter="ATCHEE",
            fourteen_letter="ATCHEE"
        ),
        latitude=39.563036918449484,
        longitude=-108.9128933612817,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    ATLANTA = PopulatedPlace(
        name="Atlanta",
        abbreviations=PlaceAbbreviations(
            three_letter="ATL",
            five_letter="ATLAN",
            seven_letter="ATLANTA",
            fourteen_letter="ATLANTA"
        ),
        latitude=37.50363082422757,
        longitude=-102.9960476058231,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    ATWOOD = PopulatedPlace(
        name="Atwood",
        abbreviations=PlaceAbbreviations(
            three_letter="ATW",
            five_letter="ATWOO",
            seven_letter="ATWOOD",
            fourteen_letter="ATWOOD"
        ),
        latitude=40.54776855150061,
        longitude=-103.26966729975942,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    AUBURN = PopulatedPlace(
        name="Auburn",
        abbreviations=PlaceAbbreviations(
            three_letter="AUB",
            five_letter="AUBUR",
            seven_letter="AUBURN",
            fourteen_letter="AUBURN"
        ),
        latitude=40.36804322987882,
        longitude=-104.6366393009393,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    AULT = PopulatedPlace(
        name="Ault",
        abbreviations=PlaceAbbreviations(
            three_letter="AUL",
            five_letter="AULT",
            seven_letter="AULT",
            fourteen_letter="AULT"
        ),
        latitude=40.58248695250995,
        longitude=-104.73192134925284,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    AURORA = PopulatedPlace(
        name="Aurora",
        abbreviations=PlaceAbbreviations(
            three_letter="AUR",
            five_letter="AUROR",
            seven_letter="AURORA",
            fourteen_letter="AURORA"
        ),
        latitude=39.72943832854605,
        longitude=-104.83192957081997,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    AURORA_HEIGHTS = PopulatedPlace(
        name="Aurora Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="AUR",
            five_letter="AUROR",
            seven_letter="AURORA ",
            fourteen_letter="AURORA HEIGHTS"
        ),
        latitude=39.73639532759739,
        longitude=-104.85751007769898,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    AURORA_HIGHLANDS = PopulatedPlace(
        name="Aurora Highlands",
        abbreviations=PlaceAbbreviations(
            three_letter="AUR",
            five_letter="AUROR",
            seven_letter="AURORA ",
            fourteen_letter="AURORA HIGHLAN"
        ),
        latitude=39.68972862644688,
        longitude=-104.77973225426211,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    AURORA_HILLS = PopulatedPlace(
        name="Aurora Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="AUR",
            five_letter="AUROR",
            seven_letter="AURORA ",
            fourteen_letter="AURORA HILLS"
        ),
        latitude=39.70695082419394,
        longitude=-104.84723227197196,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    AURORA_KNOLLS = PopulatedPlace(
        name="Aurora Knolls",
        abbreviations=PlaceAbbreviations(
            three_letter="AUR",
            five_letter="AUROR",
            seven_letter="AURORA ",
            fourteen_letter="AURORA KNOLLS"
        ),
        latitude=39.68056202539981,
        longitude=-104.77778785262626,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    AUSTIN = PopulatedPlace(
        name="Austin",
        abbreviations=PlaceAbbreviations(
            three_letter="AUS",
            five_letter="AUSTI",
            seven_letter="AUSTIN",
            fourteen_letter="AUSTIN"
        ),
        latitude=38.78110068535818,
        longitude=-107.95090916303513,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    AVALO = PopulatedPlace(
        name="Avalo",
        abbreviations=PlaceAbbreviations(
            three_letter="AVA",
            five_letter="AVALO",
            seven_letter="AVALO",
            fourteen_letter="AVALO"
        ),
        latitude=40.80332505942738,
        longitude=-103.65022992179541,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    AVON = PopulatedPlace(
        name="Avon",
        abbreviations=PlaceAbbreviations(
            three_letter="AVO",
            five_letter="AVON",
            seven_letter="AVON",
            fourteen_letter="AVON"
        ),
        latitude=39.63138119770201,
        longitude=-106.5222645450379,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    AVONDALE = PopulatedPlace(
        name="Avondale",
        abbreviations=PlaceAbbreviations(
            three_letter="AVO",
            five_letter="AVOND",
            seven_letter="AVONDAL",
            fourteen_letter="AVONDALE"
        ),
        latitude=38.237508749206995,
        longitude=-104.35108899637459,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    AXIAL = PopulatedPlace(
        name="Axial",
        abbreviations=PlaceAbbreviations(
            three_letter="AXI",
            five_letter="AXIAL",
            seven_letter="AXIAL",
            fourteen_letter="AXIAL"
        ),
        latitude=40.28525709105179,
        longitude=-107.79202650669185,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    AYER = PopulatedPlace(
        name="Ayer",
        abbreviations=PlaceAbbreviations(
            three_letter="AYE",
            five_letter="AYER",
            seven_letter="AYER",
            fourteen_letter="AYER"
        ),
        latitude=37.758073510475015,
        longitude=-103.84635303055586,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    BACHELOR_GULCH_VILLAGE = PopulatedPlace(
        name="Bachelor Gulch Village",
        abbreviations=PlaceAbbreviations(
            three_letter="BAC",
            five_letter="BACHE",
            seven_letter="BACHELO",
            fourteen_letter="BACHELOR GULCH"
        ),
        latitude=39.62222429474025,
        longitude=-106.54374644890714,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    BADITO = PopulatedPlace(
        name="Badito",
        abbreviations=PlaceAbbreviations(
            three_letter="BAD",
            five_letter="BADIT",
            seven_letter="BADITO",
            fourteen_letter="BADITO"
        ),
        latitude=37.72723783214019,
        longitude=-105.01417069638956,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    BAILEY = PopulatedPlace(
        name="Bailey",
        abbreviations=PlaceAbbreviations(
            three_letter="BAI",
            five_letter="BAILE",
            seven_letter="BAILEY",
            fourteen_letter="BAILEY"
        ),
        latitude=39.40555123973951,
        longitude=-105.47334298091721,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    BAKERVILLE = PopulatedPlace(
        name="Bakerville",
        abbreviations=PlaceAbbreviations(
            three_letter="BAK",
            five_letter="BAKER",
            seven_letter="BAKERVI",
            fourteen_letter="BAKERVILLE"
        ),
        latitude=39.69138225580622,
        longitude=-105.8050186896084,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BALARAT = PopulatedPlace(
        name="Balarat",
        abbreviations=PlaceAbbreviations(
            three_letter="BAL",
            five_letter="BALAR",
            seven_letter="BALARAT",
            fourteen_letter="BALARAT"
        ),
        latitude=40.15915854758026,
        longitude=-105.39639335207005,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BALDWIN = PopulatedPlace(
        name="Baldwin",
        abbreviations=PlaceAbbreviations(
            three_letter="BAL",
            five_letter="BALDW",
            seven_letter="BALDWIN",
            fourteen_letter="BALDWIN"
        ),
        latitude=38.76388904429433,
        longitude=-107.04783576246876,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    BALFOUR = PopulatedPlace(
        name="Balfour",
        abbreviations=PlaceAbbreviations(
            three_letter="BAL",
            five_letter="BALFO",
            seven_letter="BALFOUR",
            fourteen_letter="BALFOUR"
        ),
        latitude=38.90722185396612,
        longitude=-105.72445888344959,
        counties=[Counties.PARK],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BALLTOWN = PopulatedPlace(
        name="Balltown",
        abbreviations=PlaceAbbreviations(
            three_letter="BAL",
            five_letter="BALLT",
            seven_letter="BALLTOW",
            fourteen_letter="BALLTOWN"
        ),
        latitude=39.07777673973226,
        longitude=-106.28114412750165,
        counties=[Counties.LAKE],
        nearest_airport=Airports.ASPEN
    )
    BALZAC = PopulatedPlace(
        name="Balzac",
        abbreviations=PlaceAbbreviations(
            three_letter="BAL",
            five_letter="BALZA",
            seven_letter="BALZAC",
            fourteen_letter="BALZAC"
        ),
        latitude=40.40693131730285,
        longitude=-103.47134133132408,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    BARELA = PopulatedPlace(
        name="Barela",
        abbreviations=PlaceAbbreviations(
            three_letter="BAR",
            five_letter="BAREL",
            seven_letter="BARELA",
            fourteen_letter="BARELA"
        ),
        latitude=37.11558178846258,
        longitude=-104.26165556446563,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    BARK_RANCH = PopulatedPlace(
        name="Bark Ranch",
        abbreviations=PlaceAbbreviations(
            three_letter="BAR",
            five_letter="BARK ",
            seven_letter="BARK RA",
            fourteen_letter="BARK RANCH"
        ),
        latitude=40.11749203919982,
        longitude=-105.43945055675044,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BARNESVILLE = PopulatedPlace(
        name="Barnesville",
        abbreviations=PlaceAbbreviations(
            three_letter="BAR",
            five_letter="BARNE",
            seven_letter="BARNESV",
            fourteen_letter="BARNESVILLE"
        ),
        latitude=40.47915425654071,
        longitude=-104.47968727775356,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BARR_LAKE = PopulatedPlace(
        name="Barr Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="BAR",
            five_letter="BARR ",
            seven_letter="BARR LA",
            fourteen_letter="BARR LAKE"
        ),
        latitude=39.944435262185436,
        longitude=-104.77525898281198,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    BARTLETT = PopulatedPlace(
        name="Bartlett",
        abbreviations=PlaceAbbreviations(
            three_letter="BAR",
            five_letter="BARTL",
            seven_letter="BARTLET",
            fourteen_letter="BARTLETT"
        ),
        latitude=37.43335596524611,
        longitude=-102.1440777969051,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    BASALT = PopulatedPlace(
        name="Basalt",
        abbreviations=PlaceAbbreviations(
            three_letter="BAS",
            five_letter="BASAL",
            seven_letter="BASALT",
            fourteen_letter="BASALT"
        ),
        latitude=39.36887932690354,
        longitude=-107.0328347281656,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.ASPEN
    )
    BASIN = PopulatedPlace(
        name="Basin",
        abbreviations=PlaceAbbreviations(
            three_letter="BAS",
            five_letter="BASIN",
            seven_letter="BASIN",
            fourteen_letter="BASIN"
        ),
        latitude=38.06583095126183,
        longitude=-108.5367687113968,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    BATTLE_CREEK = PopulatedPlace(
        name="Battle Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="BAT",
            five_letter="BATTL",
            seven_letter="BATTLE ",
            fourteen_letter="BATTLE CREEK"
        ),
        latitude=41.00136092264904,
        longitude=-107.24506837684328,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    BATTLEMENT_MESA = PopulatedPlace(
        name="Battlement Mesa",
        abbreviations=PlaceAbbreviations(
            three_letter="BAT",
            five_letter="BATTL",
            seven_letter="BATTLEM",
            fourteen_letter="BATTLEMENT MES"
        ),
        latitude=39.44137316629843,
        longitude=-108.02508455533308,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    BAXTER = PopulatedPlace(
        name="Baxter",
        abbreviations=PlaceAbbreviations(
            three_letter="BAX",
            five_letter="BAXTE",
            seven_letter="BAXTER",
            fourteen_letter="BAXTER"
        ),
        latitude=38.27584184549494,
        longitude=-104.49164713213764,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    BAXTERVILLE = PopulatedPlace(
        name="Baxterville",
        abbreviations=PlaceAbbreviations(
            three_letter="BAX",
            five_letter="BAXTE",
            seven_letter="BAXTERV",
            fourteen_letter="BAXTERVILLE"
        ),
        latitude=37.674176820241826,
        longitude=-106.65782976090856,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    BAYFIELD = PopulatedPlace(
        name="Bayfield",
        abbreviations=PlaceAbbreviations(
            three_letter="BAY",
            five_letter="BAYFI",
            seven_letter="BAYFIEL",
            fourteen_letter="BAYFIELD"
        ),
        latitude=37.22556519746513,
        longitude=-107.59812272267197,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    BAYOU_HILLS = PopulatedPlace(
        name="Bayou Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="BAY",
            five_letter="BAYOU",
            seven_letter="BAYOU H",
            fourteen_letter="BAYOU HILLS"
        ),
        latitude=39.42630639549486,
        longitude=-104.70381000614742,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    BEACON_HILL = PopulatedPlace(
        name="Beacon Hill",
        abbreviations=PlaceAbbreviations(
            three_letter="BEA",
            five_letter="BEACO",
            seven_letter="BEACON ",
            fourteen_letter="BEACON HILL"
        ),
        latitude=38.72249566537391,
        longitude=-105.16499143479177,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BEAR_VALLEY = PopulatedPlace(
        name="Bear Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="BEA",
            five_letter="BEAR ",
            seven_letter="BEAR VA",
            fourteen_letter="BEAR VALLEY"
        ),
        latitude=39.662784203711055,
        longitude=-105.060843416171,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    BEAR_VALLEY_HEIGHTS = PopulatedPlace(
        name="Bear Valley Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="BEA",
            five_letter="BEAR ",
            seven_letter="BEAR VA",
            fourteen_letter="BEAR VALLEY HE"
        ),
        latitude=39.647506401834846,
        longitude=-105.05889901363679,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    BEARDS_CORNER = PopulatedPlace(
        name="Beards Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="BEA",
            five_letter="BEARD",
            seven_letter="BEARDS ",
            fourteen_letter="BEARDS CORNER"
        ),
        latitude=38.06583104603277,
        longitude=-108.612049127614,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    BEAVER_CREEK_VILLAGE = PopulatedPlace(
        name="Beaver Creek Village",
        abbreviations=PlaceAbbreviations(
            three_letter="BEA",
            five_letter="BEAVE",
            seven_letter="BEAVER ",
            fourteen_letter="BEAVER CREEK V"
        ),
        latitude=39.60490129406065,
        longitude=-106.51531544030803,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    BEAVER_POINT = PopulatedPlace(
        name="Beaver Point",
        abbreviations=PlaceAbbreviations(
            three_letter="BEA",
            five_letter="BEAVE",
            seven_letter="BEAVER ",
            fourteen_letter="BEAVER POINT"
        ),
        latitude=40.364434764832254,
        longitude=-105.5444543105109,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BECK_SAND_DRAW_CROSSING = PopulatedPlace(
        name="Beck Sand Draw Crossing",
        abbreviations=PlaceAbbreviations(
            three_letter="BEC",
            five_letter="BECK ",
            seven_letter="BECK SA",
            fourteen_letter="BECK SAND DRAW"
        ),
        latitude=39.02694088206198,
        longitude=-104.05330131010544,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BEDROCK = PopulatedPlace(
        name="Bedrock",
        abbreviations=PlaceAbbreviations(
            three_letter="BED",
            five_letter="BEDRO",
            seven_letter="BEDROCK",
            fourteen_letter="BEDROCK"
        ),
        latitude=38.314995659988654,
        longitude=-108.8909471137506,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    BEECHER_ISLAND = PopulatedPlace(
        name="Beecher Island",
        abbreviations=PlaceAbbreviations(
            three_letter="BEE",
            five_letter="BEECH",
            seven_letter="BEECHER",
            fourteen_letter="BEECHER ISLAND"
        ),
        latitude=39.87222012960723,
        longitude=-102.18436735956874,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    BELDEN = PopulatedPlace(
        name="Belden",
        abbreviations=PlaceAbbreviations(
            three_letter="BEL",
            five_letter="BELDE",
            seven_letter="BELDEN",
            fourteen_letter="BELDEN"
        ),
        latitude=39.525547992886686,
        longitude=-106.3861501027958,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    BELLEVIEW = PopulatedPlace(
        name="Belleview",
        abbreviations=PlaceAbbreviations(
            three_letter="BEL",
            five_letter="BELLE",
            seven_letter="BELLEVI",
            fourteen_letter="BELLEVIEW"
        ),
        latitude=38.569169885568726,
        longitude=-106.03724711623681,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    BELLEVUE_ACRES = PopulatedPlace(
        name="Bellevue Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="BEL",
            five_letter="BELLE",
            seven_letter="BELLEVU",
            fourteen_letter="BELLEVUE ACRES"
        ),
        latitude=39.62167309250793,
        longitude=-105.14223232960768,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    BELLVUE = PopulatedPlace(
        name="Bellvue",
        abbreviations=PlaceAbbreviations(
            three_letter="BEL",
            five_letter="BELLV",
            seven_letter="BELLVUE",
            fourteen_letter="BELLVUE"
        ),
        latitude=40.62637752626176,
        longitude=-105.1716581577054,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BENNETT = PopulatedPlace(
        name="Bennett",
        abbreviations=PlaceAbbreviations(
            three_letter="BEN",
            five_letter="BENNE",
            seven_letter="BENNETT",
            fourteen_letter="BENNETT"
        ),
        latitude=39.758880060492515,
        longitude=-104.42747097979384,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    BENTON = PopulatedPlace(
        name="Benton",
        abbreviations=PlaceAbbreviations(
            three_letter="BEN",
            five_letter="BENTO",
            seven_letter="BENTON",
            fourteen_letter="BENTON"
        ),
        latitude=37.905016343015234,
        longitude=-103.65717960054877,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    BERGEN_PARK = PopulatedPlace(
        name="Bergen Park",
        abbreviations=PlaceAbbreviations(
            three_letter="BER",
            five_letter="BERGE",
            seven_letter="BERGEN ",
            fourteen_letter="BERGEN PARK"
        ),
        latitude=39.691383286459484,
        longitude=-105.36166998896033,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    BERKELEY_GARDENS = PopulatedPlace(
        name="Berkeley Gardens",
        abbreviations=PlaceAbbreviations(
            three_letter="BER",
            five_letter="BERKE",
            seven_letter="BERKELE",
            fourteen_letter="BERKELEY GARDE"
        ),
        latitude=39.79472862354373,
        longitude=-105.03473232475926,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    BERKLEY = PopulatedPlace(
        name="Berkley",
        abbreviations=PlaceAbbreviations(
            three_letter="BER",
            five_letter="BERKL",
            seven_letter="BERKLEY",
            fourteen_letter="BERKLEY"
        ),
        latitude=39.80443712513289,
        longitude=-105.02610352405998,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    BERTHOUD = PopulatedPlace(
        name="Berthoud",
        abbreviations=PlaceAbbreviations(
            three_letter="BER",
            five_letter="BERTH",
            seven_letter="BERTHOU",
            fourteen_letter="BERTHOUD"
        ),
        latitude=40.308323890381644,
        longitude=-105.08110259705586,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BERTHOUD_FALLS = PopulatedPlace(
        name="Berthoud Falls",
        abbreviations=PlaceAbbreviations(
            three_letter="BER",
            five_letter="BERTH",
            seven_letter="BERTHOU",
            fourteen_letter="BERTHOUD FALLS"
        ),
        latitude=39.770826666498124,
        longitude=-105.80862980026956,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BERTS_CORNER = PopulatedPlace(
        name="Berts Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="BER",
            five_letter="BERTS",
            seven_letter="BERTS C",
            fourteen_letter="BERTS CORNER"
        ),
        latitude=40.307768488651675,
        longitude=-105.10277000213301,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BESHOAR = PopulatedPlace(
        name="Beshoar",
        abbreviations=PlaceAbbreviations(
            three_letter="BES",
            five_letter="BESHO",
            seven_letter="BESHOAR",
            fourteen_letter="BESHOAR"
        ),
        latitude=37.218079095157634,
        longitude=-104.4066581079104,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    """
    BETA = PopulatedPlace(
        name="Beta",
        abbreviations=PlaceAbbreviations(
            three_letter="BET",
            five_letter="BETA",
            seven_letter="BETA",
            fourteen_letter="BETA"
        ),
        latitude=38.08612573127925,
        longitude=-102.69048269120128,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    BETA = PopulatedPlace(
        name="Beta",
        abbreviations=PlaceAbbreviations(
            three_letter="BET",
            five_letter="BETA",
            seven_letter="BETA",
            fourteen_letter="BETA"
        ),
        latitude=40.46609963187359,
        longitude=-103.3788385159894,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.PUEBLO
    )
    """
    BETHUNE = PopulatedPlace(
        name="Bethune",
        abbreviations=PlaceAbbreviations(
            three_letter="BET",
            five_letter="BETHU",
            seven_letter="BETHUNE",
            fourteen_letter="BETHUNE"
        ),
        latitude=39.30416893007231,
        longitude=-102.42464895454725,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.PUEBLO
    )
    BEULAH = PopulatedPlace(
        name="Beulah",
        abbreviations=PlaceAbbreviations(
            three_letter="BEU",
            five_letter="BEULA",
            seven_letter="BEULAH",
            fourteen_letter="BEULAH"
        ),
        latitude=38.07501258487508,
        longitude=-104.98666492558357,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    BEULAH_VALLEY = PopulatedPlace(
        name="Beulah Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="BEU",
            five_letter="BEULA",
            seven_letter="BEULAH ",
            fourteen_letter="BEULAH VALLEY"
        ),
        latitude=38.072234785233036,
        longitude=-104.96638642103858,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    """
    BEVERLY_HILLS = PopulatedPlace(
        name="Beverly Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="BEV",
            five_letter="BEVER",
            seven_letter="BEVERLY",
            fourteen_letter="BEVERLY HILLS"
        ),
        latitude=39.474706390343215,
        longitude=-104.87741005194619,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    BEVERLY_HILLS = PopulatedPlace(
        name="Beverly Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="BEV",
            five_letter="BEVER",
            seven_letter="BEVERLY",
            fourteen_letter="BEVERLY HILLS"
        ),
        latitude=39.474995490128265,
        longitude=-104.87971155277211,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    """
    BIG_BEND = PopulatedPlace(
        name="Big Bend",
        abbreviations=PlaceAbbreviations(
            three_letter="BIG",
            five_letter="BIG B",
            seven_letter="BIG BEN",
            fourteen_letter="BIG BEND"
        ),
        latitude=38.20140314530818,
        longitude=-102.75076131673381,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    BIG_ELK_MEADOWS = PopulatedPlace(
        name="Big Elk Meadows",
        abbreviations=PlaceAbbreviations(
            three_letter="BIG",
            five_letter="BIG E",
            seven_letter="BIG ELK",
            fourteen_letter="BIG ELK MEADOW"
        ),
        latitude=40.261935458949665,
        longitude=-105.4302835717711,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BIGHORN = PopulatedPlace(
        name="Bighorn",
        abbreviations=PlaceAbbreviations(
            three_letter="BIG",
            five_letter="BIGHO",
            seven_letter="BIGHORN",
            fourteen_letter="BIGHORN"
        ),
        latitude=39.636658913909855,
        longitude=-106.29725989471552,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    BIGLOW = PopulatedPlace(
        name="Biglow",
        abbreviations=PlaceAbbreviations(
            three_letter="BIG",
            five_letter="BIGLO",
            seven_letter="BIGLOW",
            fourteen_letter="BIGLOW"
        ),
        latitude=39.34360364872413,
        longitude=-106.66726694385392,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    BIJOU = PopulatedPlace(
        name="Bijou",
        abbreviations=PlaceAbbreviations(
            three_letter="BIJ",
            five_letter="BIJOU",
            seven_letter="BIJOU",
            fourteen_letter="BIJOU"
        ),
        latitude=39.42249132922427,
        longitude=-104.19830438804775,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.DENVER
    )
    BIRDSEYE = PopulatedPlace(
        name="Birdseye",
        abbreviations=PlaceAbbreviations(
            three_letter="BIR",
            five_letter="BIRDS",
            seven_letter="BIRDSEY",
            fourteen_letter="BIRDSEYE"
        ),
        latitude=39.31110637458346,
        longitude=-106.22753314116426,
        counties=[Counties.LAKE],
        nearest_airport=Airports.ASPEN
    )
    BLACK_EAGLE_MILL = PopulatedPlace(
        name="Black Eagle Mill",
        abbreviations=PlaceAbbreviations(
            three_letter="BLA",
            five_letter="BLACK",
            seven_letter="BLACK E",
            fourteen_letter="BLACK EAGLE MI"
        ),
        latitude=39.72638327850416,
        longitude=-105.54750863547747,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.DENVER
    )
    BLACK_FOREST = PopulatedPlace(
        name="Black Forest",
        abbreviations=PlaceAbbreviations(
            three_letter="BLA",
            five_letter="BLACK",
            seven_letter="BLACK F",
            fourteen_letter="BLACK FOREST"
        ),
        latitude=39.013054737060145,
        longitude=-104.70081825962012,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BLACK_HAWK = PopulatedPlace(
        name="Black Hawk",
        abbreviations=PlaceAbbreviations(
            three_letter="BLA",
            five_letter="BLACK",
            seven_letter="BLACK H",
            fourteen_letter="BLACK HAWK"
        ),
        latitude=39.796938591671164,
        longitude=-105.49389553091271,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BLACK_HOLLOW_JUNCTION = PopulatedPlace(
        name="Black Hollow Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="BLA",
            five_letter="BLACK",
            seven_letter="BLACK H",
            fourteen_letter="BLACK HOLLOW J"
        ),
        latitude=40.59610003153898,
        longitude=-105.02943101951797,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BLAKELAND = PopulatedPlace(
        name="Blakeland",
        abbreviations=PlaceAbbreviations(
            three_letter="BLA",
            five_letter="BLAKE",
            seven_letter="BLAKELA",
            fourteen_letter="BLAKELAND"
        ),
        latitude=39.55971669063149,
        longitude=-105.03666099779281,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    BLANCA = PopulatedPlace(
        name="Blanca",
        abbreviations=PlaceAbbreviations(
            three_letter="BLA",
            five_letter="BLANC",
            seven_letter="BLANCA",
            fourteen_letter="BLANCA"
        ),
        latitude=37.43806935871913,
        longitude=-105.51585598170686,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    BLOOM = PopulatedPlace(
        name="Bloom",
        abbreviations=PlaceAbbreviations(
            three_letter="BLO",
            five_letter="BLOOM",
            seven_letter="BLOOM",
            fourteen_letter="BLOOM"
        ),
        latitude=37.687518593228845,
        longitude=-103.9566354493175,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    BLUE_MOUNTAIN = PopulatedPlace(
        name="Blue Mountain",
        abbreviations=PlaceAbbreviations(
            three_letter="BLU",
            five_letter="BLUE ",
            seven_letter="BLUE MO",
            fourteen_letter="BLUE MOUNTAIN"
        ),
        latitude=40.24830880745537,
        longitude=-108.8617891354229,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    BLUE_RIVER = PopulatedPlace(
        name="Blue River",
        abbreviations=PlaceAbbreviations(
            three_letter="BLU",
            five_letter="BLUE ",
            seven_letter="BLUE RI",
            fourteen_letter="BLUE RIVER"
        ),
        latitude=39.42971610358546,
        longitude=-106.04391771358416,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.ASPEN
    )
    BLUE_VALLEY = PopulatedPlace(
        name="Blue Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="BLU",
            five_letter="BLUE ",
            seven_letter="BLUE VA",
            fourteen_letter="BLUE VALLEY"
        ),
        latitude=39.699716779031576,
        longitude=-105.48917351865538,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.DENVER
    )
    BOCKMAN_LUMBER_CAMP = PopulatedPlace(
        name="Bockman Lumber Camp",
        abbreviations=PlaceAbbreviations(
            three_letter="BOC",
            five_letter="BOCKM",
            seven_letter="BOCKMAN",
            fourteen_letter="BOCKMAN LUMBER"
        ),
        latitude=40.558321260063565,
        longitude=-105.96585903187378,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BOGGSVILLE = PopulatedPlace(
        name="Boggsville",
        abbreviations=PlaceAbbreviations(
            three_letter="BOG",
            five_letter="BOGGS",
            seven_letter="BOGGSVI",
            fourteen_letter="BOGGSVILLE"
        ),
        latitude=38.04168009229409,
        longitude=-103.21271741025834,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    BONANZA = PopulatedPlace(
        name="Bonanza",
        abbreviations=PlaceAbbreviations(
            three_letter="BON",
            five_letter="BONAN",
            seven_letter="BONANZA",
            fourteen_letter="BONANZA"
        ),
        latitude=38.294727740533574,
        longitude=-106.14225271064538,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    BONANZA_MOUNTAIN_ESTATES = PopulatedPlace(
        name="Bonanza Mountain Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="BON",
            five_letter="BONAN",
            seven_letter="BONANZA",
            fourteen_letter="BONANZA MOUNTA"
        ),
        latitude=39.97665991702257,
        longitude=-105.48028494943048,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BONCARBO = PopulatedPlace(
        name="Boncarbo",
        abbreviations=PlaceAbbreviations(
            three_letter="BON",
            five_letter="BONCA",
            seven_letter="BONCARB",
            fourteen_letter="BONCARBO"
        ),
        latitude=37.21669087713565,
        longitude=-104.69499907382095,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    BOND = PopulatedPlace(
        name="Bond",
        abbreviations=PlaceAbbreviations(
            three_letter="BON",
            five_letter="BOND",
            seven_letter="BOND",
            fourteen_letter="BOND"
        ),
        latitude=39.8744377181435,
        longitude=-106.6872696108095,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    BONDAD = PopulatedPlace(
        name="Bondad",
        abbreviations=PlaceAbbreviations(
            three_letter="BON",
            five_letter="BONDA",
            seven_letter="BONDAD",
            fourteen_letter="BONDAD"
        ),
        latitude=37.0458413549361,
        longitude=-107.87618716475134,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    BONITA = PopulatedPlace(
        name="Bonita",
        abbreviations=PlaceAbbreviations(
            three_letter="BON",
            five_letter="BONIT",
            seven_letter="BONITA",
            fourteen_letter="BONITA"
        ),
        latitude=38.23278402740408,
        longitude=-106.21503402003026,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    BOONE = PopulatedPlace(
        name="Boone",
        abbreviations=PlaceAbbreviations(
            three_letter="BOO",
            five_letter="BOONE",
            seven_letter="BOONE",
            fourteen_letter="BOONE"
        ),
        latitude=38.24861925662066,
        longitude=-104.25692017539552,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    BORDENVILLE = PopulatedPlace(
        name="Bordenville",
        abbreviations=PlaceAbbreviations(
            three_letter="BOR",
            five_letter="BORDE",
            seven_letter="BORDENV",
            fourteen_letter="BORDENVILLE"
        ),
        latitude=39.27610620723044,
        longitude=-105.6836295141486,
        counties=[Counties.PARK],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BOSTON_HEIGHTS = PopulatedPlace(
        name="Boston Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="BOS",
            five_letter="BOSTO",
            seven_letter="BOSTON ",
            fourteen_letter="BOSTON HEIGHTS"
        ),
        latitude=39.74361752910073,
        longitude=-104.8516767766717,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    BOULDER = PopulatedPlace(
        name="Boulder",
        abbreviations=PlaceAbbreviations(
            three_letter="BOU",
            five_letter="BOULD",
            seven_letter="BOULDER",
            fourteen_letter="BOULDER"
        ),
        latitude=40.014992037079196,
        longitude=-105.27055580556157,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BOULDER_JUNCTION = PopulatedPlace(
        name="Boulder Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="BOU",
            five_letter="BOULD",
            seven_letter="BOULDER",
            fourteen_letter="BOULDER JUNCTI"
        ),
        latitude=40.0166585412984,
        longitude=-105.20888689159972,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BOUNTIFUL = PopulatedPlace(
        name="Bountiful",
        abbreviations=PlaceAbbreviations(
            three_letter="BOU",
            five_letter="BOUNT",
            seven_letter="BOUNTIF",
            fourteen_letter="BOUNTIFUL"
        ),
        latitude=37.229181999870434,
        longitude=-105.97697776491123,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    BOVINA = PopulatedPlace(
        name="Bovina",
        abbreviations=PlaceAbbreviations(
            three_letter="BOV",
            five_letter="BOVIN",
            seven_letter="BOVINA",
            fourteen_letter="BOVINA"
        ),
        latitude=39.28027236334623,
        longitude=-103.38523048108846,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BOW_MAR = PopulatedPlace(
        name="Bow Mar",
        abbreviations=PlaceAbbreviations(
            three_letter="BOW",
            five_letter="BOW M",
            seven_letter="BOW MAR",
            fourteen_letter="BOW MAR"
        ),
        latitude=39.628327399445595,
        longitude=-105.0499942109563,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    BOWIE = PopulatedPlace(
        name="Bowie",
        abbreviations=PlaceAbbreviations(
            three_letter="BOW",
            five_letter="BOWIE",
            seven_letter="BOWIE",
            fourteen_letter="BOWIE"
        ),
        latitude=38.92138283198159,
        longitude=-107.5400668893767,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    BOX_PRAIRIE = PopulatedPlace(
        name="Box Prairie",
        abbreviations=PlaceAbbreviations(
            three_letter="BOX",
            five_letter="BOX P",
            seven_letter="BOX PRA",
            fourteen_letter="BOX PRAIRIE"
        ),
        latitude=40.581377598717495,
        longitude=-105.4688931204617,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BOYERO = PopulatedPlace(
        name="Boyero",
        abbreviations=PlaceAbbreviations(
            three_letter="BOY",
            five_letter="BOYER",
            seven_letter="BOYERO",
            fourteen_letter="BOYERO"
        ),
        latitude=38.942778421543665,
        longitude=-103.27911511965607,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.PUEBLO
    )
    BRACEWELL = PopulatedPlace(
        name="Bracewell",
        abbreviations=PlaceAbbreviations(
            three_letter="BRA",
            five_letter="BRACE",
            seven_letter="BRACEWE",
            fourteen_letter="BRACEWELL"
        ),
        latitude=40.45943212968001,
        longitude=-104.81720225408219,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BRADFORD = PopulatedPlace(
        name="Bradford",
        abbreviations=PlaceAbbreviations(
            three_letter="BRA",
            five_letter="BRADF",
            seven_letter="BRADFOR",
            fourteen_letter="BRADFORD"
        ),
        latitude=37.88139813449493,
        longitude=-105.33306828518585,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    BRAGDON = PopulatedPlace(
        name="Bragdon",
        abbreviations=PlaceAbbreviations(
            three_letter="BRA",
            five_letter="BRAGD",
            seven_letter="BRAGDON",
            fourteen_letter="BRAGDON"
        ),
        latitude=38.40195135578705,
        longitude=-104.61164957380186,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    BRANDYWINE = PopulatedPlace(
        name="Brandywine",
        abbreviations=PlaceAbbreviations(
            three_letter="BRA",
            five_letter="BRAND",
            seven_letter="BRANDYW",
            fourteen_letter="BRANDYWINE"
        ),
        latitude=39.92361754023307,
        longitude=-105.03639904007287,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    BRANSON = PopulatedPlace(
        name="Branson",
        abbreviations=PlaceAbbreviations(
            three_letter="BRA",
            five_letter="BRANS",
            seven_letter="BRANSON",
            fourteen_letter="BRANSON"
        ),
        latitude=37.017528796882175,
        longitude=-103.8844178678076,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    BRECKENRIDGE = PopulatedPlace(
        name="Breckenridge",
        abbreviations=PlaceAbbreviations(
            three_letter="BRE",
            five_letter="BRECK",
            seven_letter="BRECKEN",
            fourteen_letter="BRECKENRIDGE"
        ),
        latitude=39.481660010867984,
        longitude=-106.03836211864223,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.ASPEN
    )
    BREEN = PopulatedPlace(
        name="Breen",
        abbreviations=PlaceAbbreviations(
            three_letter="BRE",
            five_letter="BREEN",
            seven_letter="BREEN",
            fourteen_letter="BREEN"
        ),
        latitude=37.19250626272196,
        longitude=-108.07786122326536,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    BRIDGEPORT = PopulatedPlace(
        name="Bridgeport",
        abbreviations=PlaceAbbreviations(
            three_letter="BRI",
            five_letter="BRIDG",
            seven_letter="BRIDGEP",
            fourteen_letter="BRIDGEPORT"
        ),
        latitude=38.83665646267997,
        longitude=-108.3806507622744,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    BRIDGES_SWITCH = PopulatedPlace(
        name="Bridges Switch",
        abbreviations=PlaceAbbreviations(
            three_letter="BRI",
            five_letter="BRIDG",
            seven_letter="BRIDGES",
            fourteen_letter="BRIDGES SWITCH"
        ),
        latitude=39.09859839524631,
        longitude=-108.40398749855916,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    BRIDLE_DALE = PopulatedPlace(
        name="Bridle Dale",
        abbreviations=PlaceAbbreviations(
            three_letter="BRI",
            five_letter="BRIDL",
            seven_letter="BRIDLE ",
            fourteen_letter="BRIDLE DALE"
        ),
        latitude=39.84361752472694,
        longitude=-105.1155657496688,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    BRIGGSDALE = PopulatedPlace(
        name="Briggsdale",
        abbreviations=PlaceAbbreviations(
            three_letter="BRI",
            five_letter="BRIGG",
            seven_letter="BRIGGSD",
            fourteen_letter="BRIGGSDALE"
        ),
        latitude=40.634711588425546,
        longitude=-104.32690536077934,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BRIGHTON = PopulatedPlace(
        name="Brighton",
        abbreviations=PlaceAbbreviations(
            three_letter="BRI",
            five_letter="BRIGH",
            seven_letter="BRIGHTO",
            fourteen_letter="BRIGHTON"
        ),
        latitude=39.98526816452795,
        longitude=-104.82053839851977,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    BRIMSTONE_CORNER = PopulatedPlace(
        name="Brimstone Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="BRI",
            five_letter="BRIMS",
            seven_letter="BRIMSTO",
            fourteen_letter="BRIMSTONE CORN"
        ),
        latitude=38.93804300406117,
        longitude=-107.97535548668077,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    BRISTOL = PopulatedPlace(
        name="Bristol",
        abbreviations=PlaceAbbreviations(
            three_letter="BRI",
            five_letter="BRIST",
            seven_letter="BRISTOL",
            fourteen_letter="BRISTOL"
        ),
        latitude=38.12223796098772,
        longitude=-102.3115879037797,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    BROADLANDS = PopulatedPlace(
        name="Broadlands",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROAD",
            seven_letter="BROADLA",
            fourteen_letter="BROADLANDS"
        ),
        latitude=39.95056204484564,
        longitude=-105.03889904342367,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    BROADLANDS_WEST = PopulatedPlace(
        name="Broadlands West",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROAD",
            seven_letter="BROADLA",
            fourteen_letter="BROADLANDS WES"
        ),
        latitude=39.94556204295901,
        longitude=-105.04723234690357,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    BROADMOOR = PopulatedPlace(
        name="Broadmoor",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROAD",
            seven_letter="BROADMO",
            fourteen_letter="BROADMOOR"
        ),
        latitude=38.795553997255524,
        longitude=-104.84137256856013,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BROADWAY_ESTATES = PopulatedPlace(
        name="Broadway Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROAD",
            seven_letter="BROADWA",
            fourteen_letter="BROADWAY ESTAT"
        ),
        latitude=39.59000639863319,
        longitude=-104.98362118995755,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    BROKEN_ARROW_ACRES = PopulatedPlace(
        name="Broken Arrow Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROKE",
            seven_letter="BROKEN ",
            fourteen_letter="BROKEN ARROW A"
        ),
        latitude=39.502772663298174,
        longitude=-105.32667065890377,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    BRONQUIST = PopulatedPlace(
        name="Bronquist",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BRONQ",
            seven_letter="BRONQUI",
            fourteen_letter="BRONQUIST"
        ),
        latitude=38.2019548091904,
        longitude=-104.89166021684264,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    BROOK_FOREST = PopulatedPlace(
        name="Brook Forest",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROOK",
            seven_letter="BROOK F",
            fourteen_letter="BROOK FOREST"
        ),
        latitude=39.579439170047124,
        longitude=-105.38194938014254,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    BROOKSIDE = PopulatedPlace(
        name="Brookside",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROOK",
            seven_letter="BROOKSI",
            fourteen_letter="BROOKSIDE"
        ),
        latitude=38.41528271983117,
        longitude=-105.19194360802419,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    """
    BROOKVALE = PopulatedPlace(
        name="Brookvale",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROOK",
            seven_letter="BROOKVA",
            fourteen_letter="BROOKVALE"
        ),
        latitude=39.62971687415546,
        longitude=-105.41917219413915,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.DENVER
    )
    BROOKVALE = PopulatedPlace(
        name="Brookvale",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROOK",
            seven_letter="BROOKVA",
            fourteen_letter="BROOKVALE"
        ),
        latitude=39.69167312545437,
        longitude=-104.80001005901948,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    """
    BROOMFIELD = PopulatedPlace(
        name="Broomfield",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROOM",
            seven_letter="BROOMFI",
            fourteen_letter="BROOMFIELD"
        ),
        latitude=39.92054753645141,
        longitude=-105.08666055187217,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    BROOMFIELD_HEIGHTS = PopulatedPlace(
        name="Broomfield Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROOM",
            seven_letter="BROOMFI",
            fourteen_letter="BROOMFIELD HEI"
        ),
        latitude=39.93806204128168,
        longitude=-105.07528795134215,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    BROUGHTON = PopulatedPlace(
        name="Broughton",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROUG",
            seven_letter="BROUGHT",
            fourteen_letter="BROUGHTON"
        ),
        latitude=38.813323263246616,
        longitude=-108.3270368483274,
        counties=[Counties.DELTA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    BROWNLEE = PopulatedPlace(
        name="Brownlee",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROWN",
            seven_letter="BROWNLE",
            fourteen_letter="BROWNLEE"
        ),
        latitude=40.78470456577003,
        longitude=-106.28670303273549,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    BROWNS_CANON = PopulatedPlace(
        name="Browns Canon",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROWN",
            seven_letter="BROWNS ",
            fourteen_letter="BROWNS CANON"
        ),
        latitude=38.611947390022294,
        longitude=-106.06002552621635,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    BROWNS_CORNER = PopulatedPlace(
        name="Browns Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="BRO",
            five_letter="BROWN",
            seven_letter="BROWNS ",
            fourteen_letter="BROWNS CORNER"
        ),
        latitude=40.40748980514354,
        longitude=-105.0588785042005,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BRUCE = PopulatedPlace(
        name="Bruce",
        abbreviations=PlaceAbbreviations(
            three_letter="BRU",
            five_letter="BRUCE",
            seven_letter="BRUCE",
            fourteen_letter="BRUCE"
        ),
        latitude=40.49582123084451,
        longitude=-104.86442596991611,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BRUSH = PopulatedPlace(
        name="Brush",
        abbreviations=PlaceAbbreviations(
            three_letter="BRU",
            five_letter="BRUSH",
            seven_letter="BRUSH",
            fourteen_letter="BRUSH"
        ),
        latitude=40.25887518606942,
        longitude=-103.6238465492246,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    BUCHANAN = PopulatedPlace(
        name="Buchanan",
        abbreviations=PlaceAbbreviations(
            three_letter="BUC",
            five_letter="BUCHA",
            seven_letter="BUCHANA",
            fourteen_letter="BUCHANAN"
        ),
        latitude=40.831938098079036,
        longitude=-103.16854681025865,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    BUCKEYE = PopulatedPlace(
        name="Buckeye",
        abbreviations=PlaceAbbreviations(
            three_letter="BUC",
            five_letter="BUCKE",
            seven_letter="BUCKEYE",
            fourteen_letter="BUCKEYE"
        ),
        latitude=40.82721155911224,
        longitude=-105.09498656462517,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BUCKEYE_CROSSROADS = PopulatedPlace(
        name="Buckeye Crossroads",
        abbreviations=PlaceAbbreviations(
            three_letter="BUC",
            five_letter="BUCKE",
            seven_letter="BUCKEYE",
            fourteen_letter="BUCKEYE CROSSR"
        ),
        latitude=37.557520785189695,
        longitude=-102.12880110557387,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    """
    BUCKINGHAM = PopulatedPlace(
        name="Buckingham",
        abbreviations=PlaceAbbreviations(
            three_letter="BUC",
            five_letter="BUCKI",
            seven_letter="BUCKING",
            fourteen_letter="BUCKINGHAM"
        ),
        latitude=40.621382911105286,
        longitude=-103.97773757692573,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    BUCKINGHAM = PopulatedPlace(
        name="Buckingham",
        abbreviations=PlaceAbbreviations(
            three_letter="BUC",
            five_letter="BUCKI",
            seven_letter="BUCKING",
            fourteen_letter="BUCKINGHAM"
        ),
        latitude=40.59054452839433,
        longitude=-105.06609912831834,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.DENVER
    )
    """
    BUCKSKIN_JOE = PopulatedPlace(
        name="Buckskin Joe",
        abbreviations=PlaceAbbreviations(
            three_letter="BUC",
            five_letter="BUCKS",
            seven_letter="BUCKSKI",
            fourteen_letter="BUCKSKIN JOE"
        ),
        latitude=38.47639211963775,
        longitude=-105.32694624496503,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BUDA = PopulatedPlace(
        name="Buda",
        abbreviations=PlaceAbbreviations(
            three_letter="BUD",
            five_letter="BUDA",
            seven_letter="BUDA",
            fourteen_letter="BUDA"
        ),
        latitude=40.32860100050965,
        longitude=-104.97776507531535,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BUENA_VISTA = PopulatedPlace(
        name="Buena Vista",
        abbreviations=PlaceAbbreviations(
            three_letter="BUE",
            five_letter="BUENA",
            seven_letter="BUENA V",
            fourteen_letter="BUENA VISTA"
        ),
        latitude=38.842224017267654,
        longitude=-106.13113906746224,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.ASPEN
    )
    BUFFALO_CREEK = PopulatedPlace(
        name="Buffalo Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="BUF",
            five_letter="BUFFA",
            seven_letter="BUFFALO",
            fourteen_letter="BUFFALO CREEK"
        ),
        latitude=39.386662250783274,
        longitude=-105.27028153283732,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    BUFORD = PopulatedPlace(
        name="Buford",
        abbreviations=PlaceAbbreviations(
            three_letter="BUF",
            five_letter="BUFOR",
            seven_letter="BUFORD",
            fourteen_letter="BUFORD"
        ),
        latitude=39.98720566597757,
        longitude=-107.61674063122717,
        counties=[Counties.RIO_BLANCO],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    BULGER = PopulatedPlace(
        name="Bulger",
        abbreviations=PlaceAbbreviations(
            three_letter="BUL",
            five_letter="BULGE",
            seven_letter="BULGER",
            fourteen_letter="BULGER"
        ),
        latitude=40.7936003627313,
        longitude=-104.98248293466094,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BUNYAN = PopulatedPlace(
        name="Bunyan",
        abbreviations=PlaceAbbreviations(
            three_letter="BUN",
            five_letter="BUNYA",
            seven_letter="BUNYAN",
            fourteen_letter="BUNYAN"
        ),
        latitude=40.29026749978823,
        longitude=-104.91526285624815,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    BURDETT = PopulatedPlace(
        name="Burdett",
        abbreviations=PlaceAbbreviations(
            three_letter="BUR",
            five_letter="BURDE",
            seven_letter="BURDETT",
            fourteen_letter="BURDETT"
        ),
        latitude=40.36554744775685,
        longitude=-102.9510543017368,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    BURLINGTON = PopulatedPlace(
        name="Burlington",
        abbreviations=PlaceAbbreviations(
            three_letter="BUR",
            five_letter="BURLI",
            seven_letter="BURLING",
            fourteen_letter="BURLINGTON"
        ),
        latitude=39.306114740695364,
        longitude=-102.2693657172918,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.PUEBLO
    )
    BURNING_TREE_RANCH = PopulatedPlace(
        name="Burning Tree Ranch",
        abbreviations=PlaceAbbreviations(
            three_letter="BUR",
            five_letter="BURNI",
            seven_letter="BURNING",
            fourteen_letter="BURNING TREE R"
        ),
        latitude=39.39740638916686,
        longitude=-104.73161000934493,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    BURNS = PopulatedPlace(
        name="Burns",
        abbreviations=PlaceAbbreviations(
            three_letter="BUR",
            five_letter="BURNS",
            seven_letter="BURNS",
            fourteen_letter="BURNS"
        ),
        latitude=39.87388180342623,
        longitude=-106.88560925504123,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    BURNT_MILL = PopulatedPlace(
        name="Burnt Mill",
        abbreviations=PlaceAbbreviations(
            three_letter="BUR",
            five_letter="BURNT",
            seven_letter="BURNT M",
            fourteen_letter="BURNT MILL"
        ),
        latitude=38.051679593132064,
        longitude=-104.79638117968204,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    BUTTES = PopulatedPlace(
        name="Buttes",
        abbreviations=PlaceAbbreviations(
            three_letter="BUT",
            five_letter="BUTTE",
            seven_letter="BUTTES",
            fourteen_letter="BUTTES"
        ),
        latitude=38.58722667798719,
        longitude=-104.6672048054682,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    BYERS = PopulatedPlace(
        name="Byers",
        abbreviations=PlaceAbbreviations(
            three_letter="BYE",
            five_letter="BYERS",
            seven_letter="BYERS",
            fourteen_letter="BYERS"
        ),
        latitude=39.71137726766915,
        longitude=-104.22774572825375,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CABIN_CREEK = PopulatedPlace(
        name="Cabin Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="CAB",
            five_letter="CABIN",
            seven_letter="CABIN C",
            fourteen_letter="CABIN CREEK"
        ),
        latitude=39.740542585076525,
        longitude=-104.03052258481722,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    CADDOA = PopulatedPlace(
        name="Caddoa",
        abbreviations=PlaceAbbreviations(
            three_letter="CAD",
            five_letter="CADDO",
            seven_letter="CADDOA",
            fourteen_letter="CADDOA"
        ),
        latitude=38.04779160839115,
        longitude=-102.96604415201466,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    CAHONE = PopulatedPlace(
        name="Cahone",
        abbreviations=PlaceAbbreviations(
            three_letter="CAH",
            five_letter="CAHON",
            seven_letter="CAHONE",
            fourteen_letter="CAHONE"
        ),
        latitude=37.658883678638915,
        longitude=-108.80789112657249,
        counties=[Counties.DOLORES],
        nearest_airport=Airports.CORTEZ
    )
    CALHAN = PopulatedPlace(
        name="Calhan",
        abbreviations=PlaceAbbreviations(
            three_letter="CAL",
            five_letter="CALHA",
            seven_letter="CALHAN",
            fourteen_letter="CALHAN"
        ),
        latitude=39.03555226719334,
        longitude=-104.29719586807113,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    CALHOUN = PopulatedPlace(
        name="Calhoun",
        abbreviations=PlaceAbbreviations(
            three_letter="CAL",
            five_letter="CALHO",
            seven_letter="CALHOUN",
            fourteen_letter="CALHOUN"
        ),
        latitude=40.14249082050952,
        longitude=-102.89050086089765,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    CAMBRIDGE_PARK = PopulatedPlace(
        name="Cambridge Park",
        abbreviations=PlaceAbbreviations(
            three_letter="CAM",
            five_letter="CAMBR",
            seven_letter="CAMBRID",
            fourteen_letter="CAMBRIDGE PARK"
        ),
        latitude=39.771117514598245,
        longitude=-105.1127879405197,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    CAMDEN = PopulatedPlace(
        name="Camden",
        abbreviations=PlaceAbbreviations(
            three_letter="CAM",
            five_letter="CAMDE",
            seven_letter="CAMDEN",
            fourteen_letter="CAMDEN"
        ),
        latitude=40.304152997861536,
        longitude=-103.54912203745465,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    CAMEO = PopulatedPlace(
        name="Cameo",
        abbreviations=PlaceAbbreviations(
            three_letter="CAM",
            five_letter="CAMEO",
            seven_letter="CAMEO",
            fourteen_letter="CAMEO"
        ),
        latitude=39.148597807333715,
        longitude=-108.3209291856428,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    CAMEO_ESTATES = PopulatedPlace(
        name="Cameo Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="CAM",
            five_letter="CAMEO",
            seven_letter="CAMEO E",
            fourteen_letter="CAMEO ESTATES"
        ),
        latitude=39.838617521485276,
        longitude=-105.15306575771098,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    CAMP_BIRD = PopulatedPlace(
        name="Camp Bird",
        abbreviations=PlaceAbbreviations(
            three_letter="CAM",
            five_letter="CAMP ",
            seven_letter="CAMP BI",
            fourteen_letter="CAMP BIRD"
        ),
        latitude=37.972777792034776,
        longitude=-107.72646002729118,
        counties=[Counties.OURAY],
        nearest_airport=Airports.TELLURIDE
    )
    CAMPION = PopulatedPlace(
        name="Campion",
        abbreviations=PlaceAbbreviations(
            three_letter="CAM",
            five_letter="CAMPI",
            seven_letter="CAMPION",
            fourteen_letter="CAMPION"
        ),
        latitude=40.34943469634197,
        longitude=-105.07776870110143,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CAMPO = PopulatedPlace(
        name="Campo",
        abbreviations=PlaceAbbreviations(
            three_letter="CAM",
            five_letter="CAMPO",
            seven_letter="CAMPO",
            fourteen_letter="CAMPO"
        ),
        latitude=37.105025187708804,
        longitude=-102.57964697041172,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    CANDLELIGHT = PopulatedPlace(
        name="Candlelight",
        abbreviations=PlaceAbbreviations(
            three_letter="CAN",
            five_letter="CANDL",
            seven_letter="CANDLEL",
            fourteen_letter="CANDLELIGHT"
        ),
        latitude=39.80361751673786,
        longitude=-105.15362125342483,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    CANFIELD = PopulatedPlace(
        name="Canfield",
        abbreviations=PlaceAbbreviations(
            three_letter="CAN",
            five_letter="CANFI",
            seven_letter="CANFIEL",
            fourteen_letter="CANFIELD"
        ),
        latitude=40.0536021559775,
        longitude=-105.07471506514275,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CANTON = PopulatedPlace(
        name="Canton",
        abbreviations=PlaceAbbreviations(
            three_letter="CAN",
            five_letter="CANTO",
            seven_letter="CANTON",
            fourteen_letter="CANTON"
        ),
        latitude=40.31582094341866,
        longitude=-104.34607402643525,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    CARBON_JUNCTION = PopulatedPlace(
        name="Carbon Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARBO",
            seven_letter="CARBON ",
            fourteen_letter="CARBON JUNCTIO"
        ),
        latitude=37.23750858130313,
        longitude=-107.86674318155934,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    CARBONDALE = PopulatedPlace(
        name="Carbondale",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARBO",
            seven_letter="CARBOND",
            fourteen_letter="CARBONDALE"
        ),
        latitude=39.402211618604326,
        longitude=-107.21117337181659,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    CARBONERA = PopulatedPlace(
        name="Carbonera",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARBO",
            seven_letter="CARBONE",
            fourteen_letter="CARBONERA"
        ),
        latitude=39.458871101807006,
        longitude=-108.95900625906302,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    CARDIFF = PopulatedPlace(
        name="Cardiff",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARDI",
            seven_letter="CARDIFF",
            fourteen_letter="CARDIFF"
        ),
        latitude=39.50609942551267,
        longitude=-107.31089770599107,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    CARIBOU_CITY = PopulatedPlace(
        name="Caribou City",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARIB",
            seven_letter="CARIBOU",
            fourteen_letter="CARIBOU CITY"
        ),
        latitude=39.98999321628156,
        longitude=-105.51278605839366,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CARLTON = PopulatedPlace(
        name="Carlton",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARLT",
            seven_letter="CARLTON",
            fourteen_letter="CARLTON"
        ),
        latitude=38.08473764822634,
        longitude=-102.41964452633772,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    CARMODY_ESTATES = PopulatedPlace(
        name="Carmody Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARMO",
            seven_letter="CARMODY",
            fourteen_letter="CARMODY ESTATE"
        ),
        latitude=39.678339702282415,
        longitude=-105.1136212303536,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    CARR = PopulatedPlace(
        name="Carr",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARR",
            seven_letter="CARR",
            fourteen_letter="CARR"
        ),
        latitude=40.896100483763405,
        longitude=-104.87498012167907,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CARRACAS = PopulatedPlace(
        name="Carracas",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARRA",
            seven_letter="CARRACA",
            fourteen_letter="CARRACAS"
        ),
        latitude=37.005011788068714,
        longitude=-107.25866462660349,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    CARRIAGE_CLUB = PopulatedPlace(
        name="Carriage Club",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARRI",
            seven_letter="CARRIAG",
            fourteen_letter="CARRIAGE CLUB"
        ),
        latitude=39.53249499659091,
        longitude=-104.90110076397877,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CARRIZO_SPRINGS = PopulatedPlace(
        name="Carrizo Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARRI",
            seven_letter="CARRIZO",
            fourteen_letter="CARRIZO SPRING"
        ),
        latitude=37.163635369613075,
        longitude=-103.0349398839781,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    CARTERVILLE = PopulatedPlace(
        name="Carterville",
        abbreviations=PlaceAbbreviations(
            three_letter="CAR",
            five_letter="CARTE",
            seven_letter="CARTERV",
            fourteen_letter="CARTERVILLE"
        ),
        latitude=39.630825488325854,
        longitude=-106.64615597233171,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    CASA = PopulatedPlace(
        name="Casa",
        abbreviations=PlaceAbbreviations(
            three_letter="CAS",
            five_letter="CASA",
            seven_letter="CASA",
            fourteen_letter="CASA"
        ),
        latitude=38.009181570831004,
        longitude=-103.47217216785901,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    """
    CASCADE = PopulatedPlace(
        name="Cascade",
        abbreviations=PlaceAbbreviations(
            three_letter="CAS",
            five_letter="CASCA",
            seven_letter="CASCADE",
            fourteen_letter="CASCADE"
        ),
        latitude=38.89666290241621,
        longitude=-104.97221130934315,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    CASCADE = PopulatedPlace(
        name="Cascade",
        abbreviations=PlaceAbbreviations(
            three_letter="CAS",
            five_letter="CASCA",
            seven_letter="CASCADE",
            fourteen_letter="CASCADE"
        ),
        latitude=37.603337839087885,
        longitude=-107.76257459601004,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    """
    CASTIEL = PopulatedPlace(
        name="Castiel",
        abbreviations=PlaceAbbreviations(
            three_letter="CAS",
            five_letter="CASTI",
            seven_letter="CASTIEL",
            fourteen_letter="CASTIEL"
        ),
        latitude=38.10723548635747,
        longitude=-103.46300397554398,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    CASTLE_OAKS = PopulatedPlace(
        name="Castle Oaks",
        abbreviations=PlaceAbbreviations(
            three_letter="CAS",
            five_letter="CASTL",
            seven_letter="CASTLE ",
            fourteen_letter="CASTLE OAKS"
        ),
        latitude=39.3920063830775,
        longitude=-104.81071002711593,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CASTLE_PINES = PopulatedPlace(
        name="Castle Pines",
        abbreviations=PlaceAbbreviations(
            three_letter="CAS",
            five_letter="CASTL",
            seven_letter="CASTLE ",
            fourteen_letter="CASTLE PINES"
        ),
        latitude=39.458051186501905,
        longitude=-104.89610115433231,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CASTLE_PINES_NORTH = PopulatedPlace(
        name="Castle Pines North",
        abbreviations=PlaceAbbreviations(
            three_letter="CAS",
            five_letter="CASTL",
            seven_letter="CASTLE ",
            fourteen_letter="CASTLE PINES N"
        ),
        latitude=39.47171838854382,
        longitude=-104.89482505614882,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CASTLE_PINES_VILLAGE = PopulatedPlace(
        name="Castle Pines Village",
        abbreviations=PlaceAbbreviations(
            three_letter="CAS",
            five_letter="CASTL",
            seven_letter="CASTLE ",
            fourteen_letter="CASTLE PINES V"
        ),
        latitude=39.431903382859446,
        longitude=-104.89190105067883,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CASTLE_ROCK = PopulatedPlace(
        name="Castle Rock",
        abbreviations=PlaceAbbreviations(
            three_letter="CAS",
            five_letter="CASTL",
            seven_letter="CASTLE ",
            fourteen_letter="CASTLE ROCK"
        ),
        latitude=39.37221847758906,
        longitude=-104.8561002356409,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CASTLEWOOD = PopulatedPlace(
        name="Castlewood",
        abbreviations=PlaceAbbreviations(
            three_letter="CAS",
            five_letter="CASTL",
            seven_letter="CASTLEW",
            fourteen_letter="CASTLEWOOD"
        ),
        latitude=39.584716803729066,
        longitude=-104.9011003705167,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CASTLEWOOD_NORTH = PopulatedPlace(
        name="Castlewood North",
        abbreviations=PlaceAbbreviations(
            three_letter="CAS",
            five_letter="CASTL",
            seven_letter="CASTLEW",
            fourteen_letter="CASTLEWOOD NOR"
        ),
        latitude=39.3843063841386,
        longitude=-104.776710018914,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CANON = PopulatedPlace(
        name="Cañon",
        abbreviations=PlaceAbbreviations(
            three_letter="CAÑ",
            five_letter="CAÑON",
            seven_letter="CAÑON",
            fourteen_letter="CAÑON"
        ),
        latitude=37.04335116265406,
        longitude=-106.14586888510973,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CANON_CITY = PopulatedPlace(
        name="Cañon City",
        abbreviations=PlaceAbbreviations(
            three_letter="CAÑ",
            five_letter="CAÑON",
            seven_letter="CAÑON C",
            fourteen_letter="CAÑON CITY"
        ),
        latitude=38.44099122033896,
        longitude=-105.24245702270053,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    CEDAR_COVE = PopulatedPlace(
        name="Cedar Cove",
        abbreviations=PlaceAbbreviations(
            three_letter="CED",
            five_letter="CEDAR",
            seven_letter="CEDAR C",
            fourteen_letter="CEDAR COVE"
        ),
        latitude=40.415823591237825,
        longitude=-105.26555295299698,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CEDAR_CREEK = PopulatedPlace(
        name="Cedar Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="CED",
            five_letter="CEDAR",
            seven_letter="CEDAR C",
            fourteen_letter="CEDAR CREEK"
        ),
        latitude=38.47888146100382,
        longitude=-107.71451327753044,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    CEDAR_CREST = PopulatedPlace(
        name="Cedar Crest",
        abbreviations=PlaceAbbreviations(
            three_letter="CED",
            five_letter="CEDAR",
            seven_letter="CEDAR C",
            fourteen_letter="CEDAR CREST"
        ),
        latitude=37.80696098939785,
        longitude=-104.29859094002927,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    CEDAR_GROVE = PopulatedPlace(
        name="Cedar Grove",
        abbreviations=PlaceAbbreviations(
            three_letter="CED",
            five_letter="CEDAR",
            seven_letter="CEDAR G",
            fourteen_letter="CEDAR GROVE"
        ),
        latitude=38.07501248799451,
        longitude=-104.93888551460986,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    CEDAR_POINT = PopulatedPlace(
        name="Cedar Point",
        abbreviations=PlaceAbbreviations(
            three_letter="CED",
            five_letter="CEDAR",
            seven_letter="CEDAR P",
            fourteen_letter="CEDAR POINT"
        ),
        latitude=39.345270340298214,
        longitude=-103.87052120255186,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.DENVER
    )
    CEDAREDGE = PopulatedPlace(
        name="Cedaredge",
        abbreviations=PlaceAbbreviations(
            three_letter="CED",
            five_letter="CEDAR",
            seven_letter="CEDARED",
            fourteen_letter="CEDAREDGE"
        ),
        latitude=38.90165480315932,
        longitude=-107.9264646710543,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    CEDARWOOD = PopulatedPlace(
        name="Cedarwood",
        abbreviations=PlaceAbbreviations(
            three_letter="CED",
            five_letter="CEDAR",
            seven_letter="CEDARWO",
            fourteen_letter="CEDARWOOD"
        ),
        latitude=37.94168128878181,
        longitude=-104.61748782724129,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    CENTENNIAL = PopulatedPlace(
        name="Centennial",
        abbreviations=PlaceAbbreviations(
            three_letter="CEN",
            five_letter="CENTE",
            seven_letter="CENTENN",
            fourteen_letter="CENTENNIAL"
        ),
        latitude=39.57916140479068,
        longitude=-104.87693276356094,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CENTER = PopulatedPlace(
        name="Center",
        abbreviations=PlaceAbbreviations(
            three_letter="CEN",
            five_letter="CENTE",
            seven_letter="CENTER",
            fourteen_letter="CENTER"
        ),
        latitude=37.75306236660913,
        longitude=-106.10864804650834,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CENTERVILLE = PopulatedPlace(
        name="Centerville",
        abbreviations=PlaceAbbreviations(
            three_letter="CEN",
            five_letter="CENTE",
            seven_letter="CENTERV",
            fourteen_letter="CENTERVILLE"
        ),
        latitude=38.708891501569724,
        longitude=-106.09169314322457,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    CENTRAL_CITY = PopulatedPlace(
        name="Central City",
        abbreviations=PlaceAbbreviations(
            three_letter="CEN",
            five_letter="CENTR",
            seven_letter="CENTRAL",
            fourteen_letter="CENTRAL CITY"
        ),
        latitude=39.801938590971986,
        longitude=-105.51417413606902,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CENTREPOINT = PopulatedPlace(
        name="Centrepoint",
        abbreviations=PlaceAbbreviations(
            three_letter="CEN",
            five_letter="CENTR",
            seven_letter="CENTREP",
            fourteen_letter="CENTREPOINT"
        ),
        latitude=39.70639532632009,
        longitude=-104.81528786426156,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CENTRO = PopulatedPlace(
        name="Centro",
        abbreviations=PlaceAbbreviations(
            three_letter="CEN",
            five_letter="CENTR",
            seven_letter="CENTRO",
            fourteen_letter="CENTRO"
        ),
        latitude=37.28390189728367,
        longitude=-106.1475387085942,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CHADSFORD = PopulatedPlace(
        name="Chadsford",
        abbreviations=PlaceAbbreviations(
            three_letter="CHA",
            five_letter="CHADS",
            seven_letter="CHADSFO",
            fourteen_letter="CHADSFORD"
        ),
        latitude=39.67250642177828,
        longitude=-104.81612116038389,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    """
    CHAMA = PopulatedPlace(
        name="Chama",
        abbreviations=PlaceAbbreviations(
            three_letter="CHA",
            five_letter="CHAMA",
            seven_letter="CHAMA",
            fourteen_letter="CHAMA"
        ),
        latitude=37.16196712703163,
        longitude=-105.37835452359809,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CHAMA = PopulatedPlace(
        name="Chama",
        abbreviations=PlaceAbbreviations(
            three_letter="CHA",
            five_letter="CHAMA",
            seven_letter="CHAMA",
            fourteen_letter="CHAMA"
        ),
        latitude=37.718899813047244,
        longitude=-105.29890316034641,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    """
    CHAMBERS_HEIGHTS = PopulatedPlace(
        name="Chambers Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="CHA",
            five_letter="CHAMB",
            seven_letter="CHAMBER",
            fourteen_letter="CHAMBERS HEIGH"
        ),
        latitude=39.73222862970101,
        longitude=-104.81612116757043,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CHANCE = PopulatedPlace(
        name="Chance",
        abbreviations=PlaceAbbreviations(
            three_letter="CHA",
            five_letter="CHANC",
            seven_letter="CHANCE",
            fourteen_letter="CHANCE"
        ),
        latitude=38.43722011379265,
        longitude=-106.84977308321209,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    CHANNING = PopulatedPlace(
        name="Channing",
        abbreviations=PlaceAbbreviations(
            three_letter="CHA",
            five_letter="CHANN",
            seven_letter="CHANNIN",
            fourteen_letter="CHANNING"
        ),
        latitude=38.143626249186184,
        longitude=-102.54936826291862,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    CHAPPARAL = PopulatedPlace(
        name="Chapparal",
        abbreviations=PlaceAbbreviations(
            three_letter="CHA",
            five_letter="CHAPP",
            seven_letter="CHAPPAR",
            fourteen_letter="CHAPPARAL"
        ),
        latitude=39.58695081364141,
        longitude=-104.76584333877224,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CHERAW = PopulatedPlace(
        name="Cheraw",
        abbreviations=PlaceAbbreviations(
            three_letter="CHE",
            five_letter="CHERA",
            seven_letter="CHERAW",
            fourteen_letter="CHERAW"
        ),
        latitude=38.10695778309707,
        longitude=-103.51022798692372,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    CHERRY_CREEK = PopulatedPlace(
        name="Cherry Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="CHE",
            five_letter="CHERR",
            seven_letter="CHERRY ",
            fourteen_letter="CHERRY CREEK"
        ),
        latitude=39.63455341195396,
        longitude=-104.88287107135676,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CHERRY_CREEK_EAST = PopulatedPlace(
        name="Cherry Creek East",
        abbreviations=PlaceAbbreviations(
            three_letter="CHE",
            five_letter="CHERR",
            seven_letter="CHERRY ",
            fourteen_letter="CHERRY CREEK E"
        ),
        latitude=39.599173112693734,
        longitude=-104.80139894877186,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CHERRY_CREEK_HIGHLANDS = PopulatedPlace(
        name="Cherry Creek Highlands",
        abbreviations=PlaceAbbreviations(
            three_letter="CHE",
            five_letter="CHERR",
            seven_letter="CHERRY ",
            fourteen_letter="CHERRY CREEK H"
        ),
        latitude=39.50120640010687,
        longitude=-104.78651003409755,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CHERRY_HILLS_VILLAGE = PopulatedPlace(
        name="Cherry Hills Village",
        abbreviations=PlaceAbbreviations(
            three_letter="CHE",
            five_letter="CHERR",
            seven_letter="CHERRY ",
            fourteen_letter="CHERRY HILLS V"
        ),
        latitude=39.64166080743007,
        longitude=-104.95943539032072,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CHERRY_KNOLLS = PopulatedPlace(
        name="Cherry Knolls",
        abbreviations=PlaceAbbreviations(
            three_letter="CHE",
            five_letter="CHERR",
            seven_letter="CHERRY ",
            fourteen_letter="CHERRY KNOLLS"
        ),
        latitude=39.59167310102083,
        longitude=-104.95084338281879,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CHERRY_RIDGE = PopulatedPlace(
        name="Cherry Ridge",
        abbreviations=PlaceAbbreviations(
            three_letter="CHE",
            five_letter="CHERR",
            seven_letter="CHERRY ",
            fourteen_letter="CHERRY RIDGE"
        ),
        latitude=39.626660906679376,
        longitude=-104.93887918328363,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CHESTER = PopulatedPlace(
        name="Chester",
        abbreviations=PlaceAbbreviations(
            three_letter="CHE",
            five_letter="CHEST",
            seven_letter="CHESTER",
            fourteen_letter="CHESTER"
        ),
        latitude=38.37361544102947,
        longitude=-106.3017021545254,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    CHEYENNE_WELLS = PopulatedPlace(
        name="Cheyenne Wells",
        abbreviations=PlaceAbbreviations(
            three_letter="CHE",
            five_letter="CHEYE",
            seven_letter="CHEYENN",
            fourteen_letter="CHEYENNE WELLS"
        ),
        latitude=38.82140156342473,
        longitude=-102.35325288416135,
        counties=[Counties.CHEYENNE],
        nearest_airport=Airports.PUEBLO
    )
    CHIMNEY_ROCK = PopulatedPlace(
        name="Chimney Rock",
        abbreviations=PlaceAbbreviations(
            three_letter="CHI",
            five_letter="CHIMN",
            seven_letter="CHIMNEY",
            fourteen_letter="CHIMNEY ROCK"
        ),
        latitude=37.194453911831886,
        longitude=-107.30116795523247,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    CHIPETA = PopulatedPlace(
        name="Chipeta",
        abbreviations=PlaceAbbreviations(
            three_letter="CHI",
            five_letter="CHIPE",
            seven_letter="CHIPETA",
            fourteen_letter="CHIPETA"
        ),
        latitude=38.6811016680349,
        longitude=-108.00896646507579,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    CHIPITA_PARK = PopulatedPlace(
        name="Chipita Park",
        abbreviations=PlaceAbbreviations(
            three_letter="CHI",
            five_letter="CHIPI",
            seven_letter="CHIPITA",
            fourteen_letter="CHIPITA PARK"
        ),
        latitude=38.92444090443553,
        longitude=-105.00665772005419,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    CHIVINGTON = PopulatedPlace(
        name="Chivington",
        abbreviations=PlaceAbbreviations(
            three_letter="CHI",
            five_letter="CHIVI",
            seven_letter="CHIVING",
            fourteen_letter="CHIVINGTON"
        ),
        latitude=38.43640439343653,
        longitude=-102.54353359106227,
        counties=[Counties.KIOWA],
        nearest_airport=Airports.PUEBLO
    )
    CHROMO = PopulatedPlace(
        name="Chromo",
        abbreviations=PlaceAbbreviations(
            three_letter="CHR",
            five_letter="CHROM",
            seven_letter="CHROMO",
            fourteen_letter="CHROMO"
        ),
        latitude=37.03640541876803,
        longitude=-106.84337993862505,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    CHURCHHILL_DOWNS = PopulatedPlace(
        name="Churchhill Downs",
        abbreviations=PlaceAbbreviations(
            three_letter="CHU",
            five_letter="CHURC",
            seven_letter="CHURCHH",
            fourteen_letter="CHURCHHILL DOW"
        ),
        latitude=39.84389532385177,
        longitude=-105.12167685110444,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    """
    CIMARRON = PopulatedPlace(
        name="Cimarron",
        abbreviations=PlaceAbbreviations(
            three_letter="CIM",
            five_letter="CIMAR",
            seven_letter="CIMARRO",
            fourteen_letter="CIMARRON"
        ),
        latitude=38.4424941670776,
        longitude=-107.5567357394296,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    CIMARRON = PopulatedPlace(
        name="Cimarron",
        abbreviations=PlaceAbbreviations(
            three_letter="CIM",
            five_letter="CIMAR",
            seven_letter="CIMARRO",
            fourteen_letter="CIMARRON"
        ),
        latitude=39.37361749269411,
        longitude=-104.62778778272826,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.MONTROSE
    )
    """
    CIMARRON_HILLS = PopulatedPlace(
        name="Cimarron Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="CIM",
            five_letter="CIMAR",
            seven_letter="CIMARRO",
            fourteen_letter="CIMARRON HILLS"
        ),
        latitude=38.85861201574784,
        longitude=-104.69887164184053,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    """
    CLARK = PopulatedPlace(
        name="Clark",
        abbreviations=PlaceAbbreviations(
            three_letter="CLA",
            five_letter="CLARK",
            seven_letter="CLARK",
            fourteen_letter="CLARK"
        ),
        latitude=40.706090209300214,
        longitude=-106.91922736605966,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    CLARK = PopulatedPlace(
        name="Clark",
        abbreviations=PlaceAbbreviations(
            three_letter="CLA",
            five_letter="CLARK",
            seven_letter="CLARK",
            fourteen_letter="CLARK"
        ),
        latitude=40.327767304019176,
        longitude=-104.92554076348483,
        counties=[Counties.WELD],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    """
    CLARKE_FARMS = PopulatedPlace(
        name="Clarke Farms",
        abbreviations=PlaceAbbreviations(
            three_letter="CLA",
            five_letter="CLARK",
            seven_letter="CLARKE ",
            fourteen_letter="CLARKE FARMS"
        ),
        latitude=39.5272064037531,
        longitude=-104.78811003782323,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CLARKVILLE = PopulatedPlace(
        name="Clarkville",
        abbreviations=PlaceAbbreviations(
            three_letter="CLA",
            five_letter="CLARK",
            seven_letter="CLARKVI",
            fourteen_letter="CLARKVILLE"
        ),
        latitude=40.39499407420914,
        longitude=-102.62604252669024,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    CLEORA = PopulatedPlace(
        name="Cleora",
        abbreviations=PlaceAbbreviations(
            three_letter="CLE",
            five_letter="CLEOR",
            seven_letter="CLEORA",
            fourteen_letter="CLEORA"
        ),
        latitude=38.513336682622594,
        longitude=-105.9700223953306,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    CLIFFDALE = PopulatedPlace(
        name="Cliffdale",
        abbreviations=PlaceAbbreviations(
            three_letter="CLI",
            five_letter="CLIFF",
            seven_letter="CLIFFDA",
            fourteen_letter="CLIFFDALE"
        ),
        latitude=39.408606646721694,
        longitude=-105.3763954596601,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    CLIFFORD = PopulatedPlace(
        name="Clifford",
        abbreviations=PlaceAbbreviations(
            three_letter="CLI",
            five_letter="CLIFF",
            seven_letter="CLIFFOR",
            fourteen_letter="CLIFFORD"
        ),
        latitude=39.043886931364796,
        longitude=-103.351339847264,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    CLIFTON = PopulatedPlace(
        name="Clifton",
        abbreviations=PlaceAbbreviations(
            three_letter="CLI",
            five_letter="CLIFT",
            seven_letter="CLIFTON",
            fourteen_letter="CLIFTON"
        ),
        latitude=39.09193169098921,
        longitude=-108.44898920638502,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    CLOVERLY = PopulatedPlace(
        name="Cloverly",
        abbreviations=PlaceAbbreviations(
            three_letter="CLO",
            five_letter="CLOVE",
            seven_letter="CLOVERL",
            fourteen_letter="CLOVERLY"
        ),
        latitude=40.45665394247135,
        longitude=-104.62636040914913,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CLUB_CREST = PopulatedPlace(
        name="Club Crest",
        abbreviations=PlaceAbbreviations(
            three_letter="CLU",
            five_letter="CLUB ",
            seven_letter="CLUB CR",
            fourteen_letter="CLUB CREST"
        ),
        latitude=39.832506424092685,
        longitude=-105.10251014557247,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    """
    COAL_CREEK = PopulatedPlace(
        name="Coal Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="COA",
            five_letter="COAL ",
            seven_letter="COAL CR",
            fourteen_letter="COAL CREEK"
        ),
        latitude=38.361117415151966,
        longitude=-105.14833219222083,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    COAL_CREEK = PopulatedPlace(
        name="Coal Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="COA",
            five_letter="COAL ",
            seven_letter="COAL CR",
            fourteen_letter="COAL CREEK"
        ),
        latitude=39.90638211473009,
        longitude=-105.37750361780144,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    """
    COALMONT = PopulatedPlace(
        name="Coalmont",
        abbreviations=PlaceAbbreviations(
            three_letter="COA",
            five_letter="COALM",
            seven_letter="COALMON",
            fourteen_letter="COALMONT"
        ),
        latitude=40.562486025638975,
        longitude=-106.4444872408273,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    COBURN = PopulatedPlace(
        name="Coburn",
        abbreviations=PlaceAbbreviations(
            three_letter="COB",
            five_letter="COBUR",
            seven_letter="COBURN",
            fourteen_letter="COBURN"
        ),
        latitude=38.84665901590108,
        longitude=-107.63590180223855,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    CODO = PopulatedPlace(
        name="Codo",
        abbreviations=PlaceAbbreviations(
            three_letter="COD",
            five_letter="CODO",
            seven_letter="CODO",
            fourteen_letter="CODO"
        ),
        latitude=37.502238091345475,
        longitude=-105.1472338050549,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CODY_PARK = PopulatedPlace(
        name="Cody Park",
        abbreviations=PlaceAbbreviations(
            three_letter="COD",
            five_letter="CODY ",
            seven_letter="CODY PA",
            fourteen_letter="CODY PARK"
        ),
        latitude=39.71582739602866,
        longitude=-105.27027827015621,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    COKEDALE = PopulatedPlace(
        name="Cokedale",
        abbreviations=PlaceAbbreviations(
            three_letter="COK",
            five_letter="COKED",
            seven_letter="COKEDAL",
            fourteen_letter="COKEDALE"
        ),
        latitude=37.14530357142036,
        longitude=-104.62110914995054,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    COLBY = PopulatedPlace(
        name="Colby",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLBY",
            seven_letter="COLBY",
            fourteen_letter="COLBY"
        ),
        latitude=38.93165420320594,
        longitude=-107.97535538517116,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    COLD_SPRING = PopulatedPlace(
        name="Cold Spring",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLD ",
            seven_letter="COLD SP",
            fourteen_letter="COLD SPRING"
        ),
        latitude=38.14945277856992,
        longitude=-105.24250499183836,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.PUEBLO
    )
    COLFAX_VILLAGE = PopulatedPlace(
        name="Colfax Village",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLFA",
            seven_letter="COLFAX ",
            fourteen_letter="COLFAX VILLAGE"
        ),
        latitude=39.72917312574003,
        longitude=-104.8705656799986,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    COLLBRAN = PopulatedPlace(
        name="Collbran",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLLB",
            seven_letter="COLLBRA",
            fourteen_letter="COLLBRAN"
        ),
        latitude=39.24054044452362,
        longitude=-107.96119151783063,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    COLLEGE_HILLS = PopulatedPlace(
        name="College Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLLE",
            seven_letter="COLLEGE",
            fourteen_letter="COLLEGE HILLS"
        ),
        latitude=39.90389533850373,
        longitude=-105.03056573635058,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    COLLEGE_VIEW = PopulatedPlace(
        name="College View",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLLE",
            seven_letter="COLLEGE",
            fourteen_letter="COLLEGE VIEW"
        ),
        latitude=39.66304940654692,
        longitude=-105.02165970657148,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    COLLEGE_WEST_ESTATES = PopulatedPlace(
        name="College West Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLLE",
            seven_letter="COLLEGE",
            fourteen_letter="COLLEGE WEST E"
        ),
        latitude=39.7186175058975,
        longitude=-105.14223234128588,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    COLORADO_CITY = PopulatedPlace(
        name="Colorado City",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLOR",
            seven_letter="COLORAD",
            fourteen_letter="COLORADO CITY"
        ),
        latitude=37.945292275728775,
        longitude=-104.83527267809922,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    COLORADO_SPRINGS = PopulatedPlace(
        name="Colorado Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLOR",
            seven_letter="COLORAD",
            fourteen_letter="COLORADO SPRIN"
        ),
        latitude=38.83388790377501,
        longitude=-104.8213733682033,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    """
    COLUMBINE = PopulatedPlace(
        name="Columbine",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLUM",
            seven_letter="COLUMBI",
            fourteen_letter="COLUMBINE"
        ),
        latitude=40.854142924838754,
        longitude=-106.965894595338,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    COLUMBINE = PopulatedPlace(
        name="Columbine",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLUM",
            seven_letter="COLUMBI",
            fourteen_letter="COLUMBINE"
        ),
        latitude=39.58777209263394,
        longitude=-105.06943960892369,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    """
    COLUMBINE_ACRES = PopulatedPlace(
        name="Columbine Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLUM",
            seven_letter="COLUMBI",
            fourteen_letter="COLUMBINE ACRE"
        ),
        latitude=39.79500642089596,
        longitude=-105.07223233369984,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    COLUMBINE_HEIGHTS = PopulatedPlace(
        name="Columbine Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLUM",
            seven_letter="COLUMBI",
            fourteen_letter="COLUMBINE HEIG"
        ),
        latitude=39.59639529496252,
        longitude=-105.04945450672693,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    COLUMBINE_HILLS = PopulatedPlace(
        name="Columbine Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLUM",
            seven_letter="COLUMBI",
            fourteen_letter="COLUMBINE HILL"
        ),
        latitude=39.57389529099726,
        longitude=-105.06501010698753,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    COLUMBINE_KNOLLS = PopulatedPlace(
        name="Columbine Knolls",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLUM",
            seven_letter="COLUMBI",
            fourteen_letter="COLUMBINE KNOL"
        ),
        latitude=39.57750639084594,
        longitude=-105.0772323098588,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    COLUMBINE_LAKES = PopulatedPlace(
        name="Columbine Lakes",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLUM",
            seven_letter="COLUMBI",
            fourteen_letter="COLUMBINE LAKE"
        ),
        latitude=39.604728596659186,
        longitude=-105.0444545063134,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    COLUMBINE_MANOR = PopulatedPlace(
        name="Columbine Manor",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLUM",
            seven_letter="COLUMBI",
            fourteen_letter="COLUMBINE MANO"
        ),
        latitude=39.58528419357759,
        longitude=-105.05195450558614,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    COLUMBINE_VALLEY = PopulatedPlace(
        name="Columbine Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLUM",
            seven_letter="COLUMBI",
            fourteen_letter="COLUMBINE VALL"
        ),
        latitude=39.601105297271715,
        longitude=-105.03221610142771,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    COLUMBUS = PopulatedPlace(
        name="Columbus",
        abbreviations=PlaceAbbreviations(
            three_letter="COL",
            five_letter="COLUM",
            seven_letter="COLUMBU",
            fourteen_letter="COLUMBUS"
        ),
        latitude=37.32778650996039,
        longitude=-107.63006923962638,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    COMANCHE = PopulatedPlace(
        name="Comanche",
        abbreviations=PlaceAbbreviations(
            three_letter="COM",
            five_letter="COMAN",
            seven_letter="COMANCH",
            fourteen_letter="COMANCHE"
        ),
        latitude=39.9855456010078,
        longitude=-104.30051897705556,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    COMER = PopulatedPlace(
        name="Comer",
        abbreviations=PlaceAbbreviations(
            three_letter="COM",
            five_letter="COMER",
            seven_letter="COMER",
            fourteen_letter="COMER"
        ),
        latitude=40.46776582772617,
        longitude=-104.85442576427317,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    COMMERCE_CITY = PopulatedPlace(
        name="Commerce City",
        abbreviations=PlaceAbbreviations(
            three_letter="COM",
            five_letter="COMME",
            seven_letter="COMMERC",
            fourteen_letter="COMMERCE CITY"
        ),
        latitude=39.80832603235723,
        longitude=-104.93387760363186,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    COMO = PopulatedPlace(
        name="Como",
        abbreviations=PlaceAbbreviations(
            three_letter="COM",
            five_letter="COMO",
            seven_letter="COMO",
            fourteen_letter="COMO"
        ),
        latitude=39.31610609866084,
        longitude=-105.89280226668336,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    CONCRETE = PopulatedPlace(
        name="Concrete",
        abbreviations=PlaceAbbreviations(
            three_letter="CON",
            five_letter="CONCR",
            seven_letter="CONCRET",
            fourteen_letter="CONCRETE"
        ),
        latitude=38.38334062816938,
        longitude=-104.99777225989834,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.PUEBLO
    )
    CONIFER = PopulatedPlace(
        name="Conifer",
        abbreviations=PlaceAbbreviations(
            three_letter="CON",
            five_letter="CONIF",
            seven_letter="CONIFER",
            fourteen_letter="CONIFER"
        ),
        latitude=39.521105867387234,
        longitude=-105.30528095631865,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    COOPER = PopulatedPlace(
        name="Cooper",
        abbreviations=PlaceAbbreviations(
            three_letter="COO",
            five_letter="COOPE",
            seven_letter="COOPER",
            fourteen_letter="COOPER"
        ),
        latitude=40.36054220713902,
        longitude=-103.52912113928187,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    COPE = PopulatedPlace(
        name="Cope",
        abbreviations=PlaceAbbreviations(
            three_letter="COP",
            five_letter="COPE",
            seven_letter="COPE",
            fourteen_letter="COPE"
        ),
        latitude=39.663883654139,
        longitude=-102.8510543967725,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    COPPER_SPUR = PopulatedPlace(
        name="Copper Spur",
        abbreviations=PlaceAbbreviations(
            three_letter="COP",
            five_letter="COPPE",
            seven_letter="COPPER ",
            fourteen_letter="COPPER SPUR"
        ),
        latitude=39.91054902237164,
        longitude=-106.68838121578642,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    COPPERDALE = PopulatedPlace(
        name="Copperdale",
        abbreviations=PlaceAbbreviations(
            three_letter="COP",
            five_letter="COPPE",
            seven_letter="COPPERD",
            fourteen_letter="COPPERDALE"
        ),
        latitude=39.9141597177408,
        longitude=-105.34944721206563,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CORDOVA_PLAZA = PopulatedPlace(
        name="Cordova Plaza",
        abbreviations=PlaceAbbreviations(
            three_letter="COR",
            five_letter="CORDO",
            seven_letter="CORDOVA",
            fourteen_letter="CORDOVA PLAZA"
        ),
        latitude=37.13335965673997,
        longitude=-104.82972609685282,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CORNELIA = PopulatedPlace(
        name="Cornelia",
        abbreviations=PlaceAbbreviations(
            three_letter="COR",
            five_letter="CORNE",
            seven_letter="CORNELI",
            fourteen_letter="CORNELIA"
        ),
        latitude=38.09279059510345,
        longitude=-103.28827513281044,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    CORNISH = PopulatedPlace(
        name="Cornish",
        abbreviations=PlaceAbbreviations(
            three_letter="COR",
            five_letter="CORNI",
            seven_letter="CORNISH",
            fourteen_letter="CORNISH"
        ),
        latitude=40.523043867232104,
        longitude=-104.41329676745454,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CORTEZ = PopulatedPlace(
        name="Cortez",
        abbreviations=PlaceAbbreviations(
            three_letter="COR",
            five_letter="CORTE",
            seven_letter="CORTEZ",
            fourteen_letter="CORTEZ"
        ),
        latitude=37.34888855197022,
        longitude=-108.5859371477685,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    CORY = PopulatedPlace(
        name="Cory",
        abbreviations=PlaceAbbreviations(
            three_letter="COR",
            five_letter="CORY",
            seven_letter="CORY",
            fourteen_letter="CORY"
        ),
        latitude=38.78804498350058,
        longitude=-107.98729927200094,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    COTTON_CREEK = PopulatedPlace(
        name="Cotton Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="COT",
            five_letter="COTTO",
            seven_letter="COTTON ",
            fourteen_letter="COTTON CREEK"
        ),
        latitude=39.89472863678003,
        longitude=-105.0436212398356,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    COTTONWOOD = PopulatedPlace(
        name="Cottonwood",
        abbreviations=PlaceAbbreviations(
            three_letter="COT",
            five_letter="COTTO",
            seven_letter="COTTONW",
            fourteen_letter="COTTONWOOD"
        ),
        latitude=37.93445022230628,
        longitude=-105.64418776078884,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    """
    COTTONWOOD = PopulatedPlace(
        name="Cottonwood",
        abbreviations=PlaceAbbreviations(
            three_letter="COT",
            five_letter="COTTO",
            seven_letter="COTTONW",
            fourteen_letter="COTTONWOOD"
        ),
        latitude=39.5624951075348,
        longitude=-104.80193014505721,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    COTTONWOOD = PopulatedPlace(
        name="Cottonwood",
        abbreviations=PlaceAbbreviations(
            three_letter="COT",
            five_letter="COTTO",
            seven_letter="COTTONW",
            fourteen_letter="COTTONWOOD"
        ),
        latitude=39.76332749228192,
        longitude=-105.42472681171421,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    """
    COUNTRY_ACRES = PopulatedPlace(
        name="Country Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="COU",
            five_letter="COUNT",
            seven_letter="COUNTRY",
            fourteen_letter="COUNTRY ACRES"
        ),
        latitude=39.388061990770325,
        longitude=-104.68889889859412,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    """
    COUNTRY_ESTATES = PopulatedPlace(
        name="Country Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="COU",
            five_letter="COUNT",
            seven_letter="COUNTRY",
            fourteen_letter="COUNTRY ESTATE"
        ),
        latitude=39.94583974185525,
        longitude=-105.0694545515002,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    COUNTRY_ESTATES = PopulatedPlace(
        name="Country Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="COU",
            five_letter="COUNT",
            seven_letter="COUNTRY",
            fourteen_letter="COUNTRY ESTATE"
        ),
        latitude=39.94472864129733,
        longitude=-105.07028795092862,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    """
    COUNTRY_VIEW_ESTATES = PopulatedPlace(
        name="Country View Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="COU",
            five_letter="COUNT",
            seven_letter="COUNTRY",
            fourteen_letter="COUNTRY VIEW E"
        ),
        latitude=39.839728623163865,
        longitude=-105.13028795229752,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    COUNTRY_WEST = PopulatedPlace(
        name="Country West",
        abbreviations=PlaceAbbreviations(
            three_letter="COU",
            five_letter="COUNT",
            seven_letter="COUNTRY",
            fourteen_letter="COUNTRY WEST"
        ),
        latitude=39.61889529232786,
        longitude=-105.13362122751619,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    COUNTRYSIDE = PopulatedPlace(
        name="Countryside",
        abbreviations=PlaceAbbreviations(
            three_letter="COU",
            five_letter="COUNT",
            seven_letter="COUNTRY",
            fourteen_letter="COUNTRYSIDE"
        ),
        latitude=39.88583972992325,
        longitude=-105.11945455563546,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    """
    COVENTRY = PopulatedPlace(
        name="Coventry",
        abbreviations=PlaceAbbreviations(
            three_letter="COV",
            five_letter="COVEN",
            seven_letter="COVENTR",
            fourteen_letter="COVENTRY"
        ),
        latitude=38.159996474230525,
        longitude=-108.37481768672416,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.TELLURIDE
    )
    COVENTRY = PopulatedPlace(
        name="Coventry",
        abbreviations=PlaceAbbreviations(
            three_letter="COV",
            five_letter="COVEN",
            seven_letter="COVENTR",
            fourteen_letter="COVENTRY"
        ),
        latitude=39.60472859596712,
        longitude=-105.05084340815739,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.TELLURIDE
    )
    """
    COWDREY = PopulatedPlace(
        name="Cowdrey",
        abbreviations=PlaceAbbreviations(
            three_letter="COW",
            five_letter="COWDR",
            seven_letter="COWDREY",
            fourteen_letter="COWDREY"
        ),
        latitude=40.85970347377793,
        longitude=-106.31309224884723,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    COZY_CORNER = PopulatedPlace(
        name="Cozy Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="COZ",
            five_letter="COZY ",
            seven_letter="COZY CO",
            fourteen_letter="COZY CORNER"
        ),
        latitude=39.91388064041848,
        longitude=-105.02582503733873,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    CRAIG = PopulatedPlace(
        name="Craig",
        abbreviations=PlaceAbbreviations(
            three_letter="CRA",
            five_letter="CRAIG",
            seven_letter="CRAIG",
            fourteen_letter="CRAIG"
        ),
        latitude=40.515255438601514,
        longitude=-107.5464648812731,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    CRAIG_PLACE = PopulatedPlace(
        name="Craig Place",
        abbreviations=PlaceAbbreviations(
            three_letter="CRA",
            five_letter="CRAIG",
            seven_letter="CRAIG P",
            fourteen_letter="CRAIG PLACE"
        ),
        latitude=40.72024615846385,
        longitude=-108.95429591592125,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    CRAIG_SOUTH_HIGHLANDS = PopulatedPlace(
        name="Craig South Highlands",
        abbreviations=PlaceAbbreviations(
            three_letter="CRA",
            five_letter="CRAIG",
            seven_letter="CRAIG S",
            fourteen_letter="CRAIG SOUTH HI"
        ),
        latitude=40.48497793349969,
        longitude=-107.56313188169486,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    CRAWFORD = PopulatedPlace(
        name="Crawford",
        abbreviations=PlaceAbbreviations(
            three_letter="CRA",
            five_letter="CRAWF",
            seven_letter="CRAWFOR",
            fourteen_letter="CRAWFORD"
        ),
        latitude=38.703882798126415,
        longitude=-107.60895718024449,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    CREEDE = PopulatedPlace(
        name="Creede",
        abbreviations=PlaceAbbreviations(
            three_letter="CRE",
            five_letter="CREED",
            seven_letter="CREEDE",
            fourteen_letter="CREEDE"
        ),
        latitude=37.84917222718855,
        longitude=-106.92644483888739,
        counties=[Counties.MINERAL],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    CRESCENT = PopulatedPlace(
        name="Crescent",
        abbreviations=PlaceAbbreviations(
            three_letter="CRE",
            five_letter="CRESC",
            seven_letter="CRESCEN",
            fourteen_letter="CRESCENT"
        ),
        latitude=39.92832621892643,
        longitude=-105.34278031218395,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CRESCENT_VILLAGE = PopulatedPlace(
        name="Crescent Village",
        abbreviations=PlaceAbbreviations(
            three_letter="CRE",
            five_letter="CRESC",
            seven_letter="CRESCEN",
            fourteen_letter="CRESCENT VILLA"
        ),
        latitude=39.919715217025214,
        longitude=-105.36111431538001,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    CRESTED_BUTTE = PopulatedPlace(
        name="Crested Butte",
        abbreviations=PlaceAbbreviations(
            three_letter="CRE",
            five_letter="CREST",
            seven_letter="CRESTED",
            fourteen_letter="CRESTED BUTTE"
        ),
        latitude=38.869720762929205,
        longitude=-106.98783366173689,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    CRESTMONT_HEIGHTS = PopulatedPlace(
        name="Crestmont Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="CRE",
            five_letter="CREST",
            seven_letter="CRESTMO",
            fourteen_letter="CRESTMONT HEIG"
        ),
        latitude=39.805562017919954,
        longitude=-105.1327879493603,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    CRESTONE = PopulatedPlace(
        name="Crestone",
        abbreviations=PlaceAbbreviations(
            three_letter="CRE",
            five_letter="CREST",
            seven_letter="CRESTON",
            fourteen_letter="CRESTONE"
        ),
        latitude=37.99639422771361,
        longitude=-105.6997432790177,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CRESTVIEW = PopulatedPlace(
        name="Crestview",
        abbreviations=PlaceAbbreviations(
            three_letter="CRE",
            five_letter="CREST",
            seven_letter="CRESTVI",
            fourteen_letter="CRESTVIEW"
        ),
        latitude=39.486406402946955,
        longitude=-104.71381001595762,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    CRESTVIEW_VILLA = PopulatedPlace(
        name="Crestview Villa",
        abbreviations=PlaceAbbreviations(
            three_letter="CRE",
            five_letter="CREST",
            seven_letter="CRESTVI",
            fourteen_letter="CRESTVIEW VILL"
        ),
        latitude=39.73778420523303,
        longitude=-105.1811212525551,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    CRIPPLE_CREEK = PopulatedPlace(
        name="Cripple Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="CRI",
            five_letter="CRIPP",
            seven_letter="CRIPPLE",
            fourteen_letter="CRIPPLE CREEK"
        ),
        latitude=38.74666176812747,
        longitude=-105.17832494080608,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    CROFTON_PARK = PopulatedPlace(
        name="Crofton Park",
        abbreviations=PlaceAbbreviations(
            three_letter="CRO",
            five_letter="CROFT",
            seven_letter="CROFTON",
            fourteen_letter="CROFTON PARK"
        ),
        latitude=39.92306204017734,
        longitude=-105.03112123835257,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    CROOK = PopulatedPlace(
        name="Crook",
        abbreviations=PlaceAbbreviations(
            three_letter="CRO",
            five_letter="CROOK",
            seven_letter="CROOK",
            fourteen_letter="CROOK"
        ),
        latitude=40.85888662779365,
        longitude=-102.80103612539585,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    CROSS_CREEK = PopulatedPlace(
        name="Cross Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="CRO",
            five_letter="CROSS",
            seven_letter="CROSS C",
            fourteen_letter="CROSS CREEK"
        ),
        latitude=39.7219508360518,
        longitude=-104.70862114116244,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    CROSSONS = PopulatedPlace(
        name="Crossons",
        abbreviations=PlaceAbbreviations(
            three_letter="CRO",
            five_letter="CROSS",
            seven_letter="CROSSON",
            fourteen_letter="CROSSONS"
        ),
        latitude=39.399162244888316,
        longitude=-105.3863958602376,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    CROWLEY = PopulatedPlace(
        name="Crowley",
        abbreviations=PlaceAbbreviations(
            three_letter="CRO",
            five_letter="CROWL",
            seven_letter="CROWLEY",
            fourteen_letter="CROWLEY"
        ),
        latitude=38.19306697390681,
        longitude=-103.85607427606533,
        counties=[Counties.CROWLEY],
        nearest_airport=Airports.PUEBLO
    )
    CRYSTAL = PopulatedPlace(
        name="Crystal",
        abbreviations=PlaceAbbreviations(
            three_letter="CRY",
            five_letter="CRYST",
            seven_letter="CRYSTAL",
            fourteen_letter="CRYSTAL"
        ),
        latitude=39.05916188050503,
        longitude=-107.10116900768656,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.ASPEN
    )
    CRYSTOLA = PopulatedPlace(
        name="Crystola",
        abbreviations=PlaceAbbreviations(
            three_letter="CRY",
            five_letter="CRYST",
            seven_letter="CRYSTOL",
            fourteen_letter="CRYSTOLA"
        ),
        latitude=38.955830607722476,
        longitude=-105.027215328463,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    CUCHARA = PopulatedPlace(
        name="Cuchara",
        abbreviations=PlaceAbbreviations(
            three_letter="CUC",
            five_letter="CUCHA",
            seven_letter="CUCHARA",
            fourteen_letter="CUCHARA"
        ),
        latitude=37.379185676286056,
        longitude=-105.1002908819176,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    CUCHARA_JUNCTION = PopulatedPlace(
        name="Cuchara Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="CUC",
            five_letter="CUCHA",
            seven_letter="CUCHARA",
            fourteen_letter="CUCHARA JUNCTI"
        ),
        latitude=37.66696294434303,
        longitude=-104.68610411577777,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    CUERNA_VERDE_PARK = PopulatedPlace(
        name="Cuerna Verde Park",
        abbreviations=PlaceAbbreviations(
            three_letter="CUE",
            five_letter="CUERN",
            seven_letter="CUERNA ",
            fourteen_letter="CUERNA VERDE P"
        ),
        latitude=37.921958864771284,
        longitude=-104.97138860615485,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    CULP = PopulatedPlace(
        name="Culp",
        abbreviations=PlaceAbbreviations(
            three_letter="CUL",
            five_letter="CULP",
            seven_letter="CULP",
            fourteen_letter="CULP"
        ),
        latitude=38.13584824406996,
        longitude=-102.60936967643943,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    CUMBRES = PopulatedPlace(
        name="Cumbres",
        abbreviations=PlaceAbbreviations(
            three_letter="CUM",
            five_letter="CUMBR",
            seven_letter="CUMBRES",
            fourteen_letter="CUMBRES"
        ),
        latitude=37.01973874073923,
        longitude=-106.44782074960767,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    DACONO = PopulatedPlace(
        name="Dacono",
        abbreviations=PlaceAbbreviations(
            three_letter="DAC",
            five_letter="DACON",
            seven_letter="DACONO",
            fourteen_letter="DACONO"
        ),
        latitude=40.08471266990625,
        longitude=-104.93943173791331,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    DAILEY = PopulatedPlace(
        name="Dailey",
        abbreviations=PlaceAbbreviations(
            three_letter="DAI",
            five_letter="DAILE",
            seven_letter="DAILEY",
            fourteen_letter="DAILEY"
        ),
        latitude=40.65666490482192,
        longitude=-102.72381388211454,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    DALLAS = PopulatedPlace(
        name="Dallas",
        abbreviations=PlaceAbbreviations(
            three_letter="DAL",
            five_letter="DALLA",
            seven_letter="DALLAS",
            fourteen_letter="DALLAS"
        ),
        latitude=38.18332961954934,
        longitude=-107.74479185297105,
        counties=[Counties.OURAY],
        nearest_airport=Airports.TELLURIDE
    )
    DANIELS_GARDEN = PopulatedPlace(
        name="Daniels Garden",
        abbreviations=PlaceAbbreviations(
            three_letter="DAN",
            five_letter="DANIE",
            seven_letter="DANIELS",
            fourteen_letter="DANIELS GARDEN"
        ),
        latitude=39.73528420823925,
        longitude=-105.13278794127547,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    DE_BEQUE = PopulatedPlace(
        name="De Beque",
        abbreviations=PlaceAbbreviations(
            three_letter="DE ",
            five_letter="DE BE",
            seven_letter="DE BEQU",
            fourteen_letter="DE BEQUE"
        ),
        latitude=39.33442943909051,
        longitude=-108.21509238369515,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    DEARFIELD = PopulatedPlace(
        name="Dearfield",
        abbreviations=PlaceAbbreviations(
            three_letter="DEA",
            five_letter="DEARF",
            seven_letter="DEARFIE",
            fourteen_letter="DEARFIELD"
        ),
        latitude=40.290542946185326,
        longitude=-104.25940530354359,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    DECKERS = PopulatedPlace(
        name="Deckers",
        abbreviations=PlaceAbbreviations(
            three_letter="DEC",
            five_letter="DECKE",
            seven_letter="DECKERS",
            fourteen_letter="DECKERS"
        ),
        latitude=39.2547188343579,
        longitude=-105.2269483073112,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    DEER_TRAIL = PopulatedPlace(
        name="Deer Trail",
        abbreviations=PlaceAbbreviations(
            three_letter="DEE",
            five_letter="DEER ",
            seven_letter="DEER TR",
            fourteen_letter="DEER TRAIL"
        ),
        latitude=39.61498856692867,
        longitude=-104.0444131738684,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    DEERMONT = PopulatedPlace(
        name="Deermont",
        abbreviations=PlaceAbbreviations(
            three_letter="DEE",
            five_letter="DEERM",
            seven_letter="DEERMON",
            fourteen_letter="DEERMONT"
        ),
        latitude=39.5074947734866,
        longitude=-105.18444392675497,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    DEL_MAR = PopulatedPlace(
        name="Del Mar",
        abbreviations=PlaceAbbreviations(
            three_letter="DEL",
            five_letter="DEL M",
            seven_letter="DEL MAR",
            fourteen_letter="DEL MAR"
        ),
        latitude=39.728895326592806,
        longitude=-104.85751007680062,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    DEL_NORTE = PopulatedPlace(
        name="Del Norte",
        abbreviations=PlaceAbbreviations(
            three_letter="DEL",
            five_letter="DEL N",
            seven_letter="DEL NOR",
            fourteen_letter="DEL NORTE"
        ),
        latitude=37.678897940199704,
        longitude=-106.3533785937455,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    DELCARBON = PopulatedPlace(
        name="Delcarbon",
        abbreviations=PlaceAbbreviations(
            three_letter="DEL",
            five_letter="DELCA",
            seven_letter="DELCARB",
            fourteen_letter="DELCARBON"
        ),
        latitude=37.71251703906165,
        longitude=-104.87694376343165,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    DELHI = PopulatedPlace(
        name="Delhi",
        abbreviations=PlaceAbbreviations(
            three_letter="DEL",
            five_letter="DELHI",
            seven_letter="DELHI",
            fourteen_letter="DELHI"
        ),
        latitude=37.64224128265511,
        longitude=-104.01802705874098,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    DELL = PopulatedPlace(
        name="Dell",
        abbreviations=PlaceAbbreviations(
            three_letter="DEL",
            five_letter="DELL",
            seven_letter="DELL",
            fourteen_letter="DELL"
        ),
        latitude=39.885548707449175,
        longitude=-106.85644165036695,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    DELTA = PopulatedPlace(
        name="Delta",
        abbreviations=PlaceAbbreviations(
            three_letter="DEL",
            five_letter="DELTA",
            seven_letter="DELTA",
            fourteen_letter="DELTA"
        ),
        latitude=38.74221227221676,
        longitude=-108.06896888470965,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    DENT = PopulatedPlace(
        name="Dent",
        abbreviations=PlaceAbbreviations(
            three_letter="DEN",
            five_letter="DENT",
            seven_letter="DENT",
            fourteen_letter="DENT"
        ),
        latitude=40.30971110812658,
        longitude=-104.83387053999314,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    DENVER = PopulatedPlace(
        name="Denver",
        abbreviations=PlaceAbbreviations(
            three_letter="DEN",
            five_letter="DENVE",
            seven_letter="DENVER",
            fourteen_letter="DENVER"
        ),
        latitude=39.73916001934174,
        longitude=-104.98471350720706,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    DEORA = PopulatedPlace(
        name="Deora",
        abbreviations=PlaceAbbreviations(
            three_letter="DEO",
            five_letter="DEORA",
            seven_letter="DEORA",
            fourteen_letter="DEORA"
        ),
        latitude=37.58029613771009,
        longitude=-102.96660180638008,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    DERBY = PopulatedPlace(
        name="Derby",
        abbreviations=PlaceAbbreviations(
            three_letter="DER",
            five_letter="DERBY",
            seven_letter="DERBY",
            fourteen_letter="DERBY"
        ),
        latitude=39.839436837374706,
        longitude=-104.91859900338068,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    DERBY_JUNCTION = PopulatedPlace(
        name="Derby Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="DER",
            five_letter="DERBY",
            seven_letter="DERBY J",
            fourteen_letter="DERBY JUNCTION"
        ),
        latitude=39.868881701795374,
        longitude=-106.90560995917792,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    DEVINE = PopulatedPlace(
        name="Devine",
        abbreviations=PlaceAbbreviations(
            three_letter="DEV",
            five_letter="DEVIN",
            seven_letter="DEVINE",
            fourteen_letter="DEVINE"
        ),
        latitude=38.27500844739029,
        longitude=-104.45747972467922,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    DEVONSIRE_HEIGHTS = PopulatedPlace(
        name="Devonsire Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="DEV",
            five_letter="DEVON",
            seven_letter="DEVONSI",
            fourteen_letter="DEVONSIRE HEIG"
        ),
        latitude=39.648895309392174,
        longitude=-104.94862118885948,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    DICK = PopulatedPlace(
        name="Dick",
        abbreviations=PlaceAbbreviations(
            three_letter="DIC",
            five_letter="DICK",
            seven_letter="DICK",
            fourteen_letter="DICK"
        ),
        latitude=40.03137936274396,
        longitude=-104.93720973080354,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    DILLON = PopulatedPlace(
        name="Dillon",
        abbreviations=PlaceAbbreviations(
            three_letter="DIL",
            five_letter="DILLO",
            seven_letter="DILLON",
            fourteen_letter="DILLON"
        ),
        latitude=39.630270631010035,
        longitude=-106.04336213702209,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    DINOSAUR = PopulatedPlace(
        name="Dinosaur",
        abbreviations=PlaceAbbreviations(
            three_letter="DIN",
            five_letter="DINOS",
            seven_letter="DINOSAU",
            fourteen_letter="DINOSAUR"
        ),
        latitude=40.24358419608177,
        longitude=-109.01457236753077,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    DODD = PopulatedPlace(
        name="Dodd",
        abbreviations=PlaceAbbreviations(
            three_letter="DOD",
            five_letter="DODD",
            seven_letter="DODD",
            fourteen_letter="DODD"
        ),
        latitude=40.287209483962954,
        longitude=-103.70746007398708,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    DOENZ_PLACE = PopulatedPlace(
        name="Doenz Place",
        abbreviations=PlaceAbbreviations(
            three_letter="DOE",
            five_letter="DOENZ",
            seven_letter="DOENZ P",
            fourteen_letter="DOENZ PLACE"
        ),
        latitude=39.904992341971706,
        longitude=-106.4017075499927,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    DOLORES = PopulatedPlace(
        name="Dolores",
        abbreviations=PlaceAbbreviations(
            three_letter="DOL",
            five_letter="DOLOR",
            seven_letter="DOLORES",
            fourteen_letter="DOLORES"
        ),
        latitude=37.47388767410109,
        longitude=-108.50454624276676,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    DOME_ROCK = PopulatedPlace(
        name="Dome Rock",
        abbreviations=PlaceAbbreviations(
            three_letter="DOM",
            five_letter="DOME ",
            seven_letter="DOME RO",
            fourteen_letter="DOME ROCK"
        ),
        latitude=39.421662060766494,
        longitude=-105.19750081993368,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    DOMINGUEZ = PopulatedPlace(
        name="Dominguez",
        abbreviations=PlaceAbbreviations(
            three_letter="DOM",
            five_letter="DOMIN",
            seven_letter="DOMINGU",
            fourteen_letter="DOMINGUEZ"
        ),
        latitude=38.797212262134735,
        longitude=-108.3223141452657,
        counties=[Counties.DELTA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    DOMINION = PopulatedPlace(
        name="Dominion",
        abbreviations=PlaceAbbreviations(
            three_letter="DOM",
            five_letter="DOMIN",
            seven_letter="DOMINIO",
            fourteen_letter="DOMINION"
        ),
        latitude=40.14304686484246,
        longitude=-105.12693878767828,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    DOUBLEHEADER_RANCH = PopulatedPlace(
        name="Doubleheader Ranch",
        abbreviations=PlaceAbbreviations(
            three_letter="DOU",
            five_letter="DOUBL",
            seven_letter="DOUBLEH",
            fourteen_letter="DOUBLEHEADER R"
        ),
        latitude=39.55889527658377,
        longitude=-105.24612124625287,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    DOVE_CREEK = PopulatedPlace(
        name="Dove Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="DOV",
            five_letter="DOVE ",
            seven_letter="DOVE CR",
            fourteen_letter="DOVE CREEK"
        ),
        latitude=37.76610588633355,
        longitude=-108.90595005877037,
        counties=[Counties.DOLORES],
        nearest_airport=Airports.CORTEZ
    )
    DOVE_HILL = PopulatedPlace(
        name="Dove Hill",
        abbreviations=PlaceAbbreviations(
            three_letter="DOV",
            five_letter="DOVE ",
            seven_letter="DOVE HI",
            fourteen_letter="DOVE HILL"
        ),
        latitude=39.62056202193514,
        longitude=-104.7119544307539,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    DOVE_VALLEY = PopulatedPlace(
        name="Dove Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="DOV",
            five_letter="DOVE ",
            seven_letter="DOVE VA",
            fourteen_letter="DOVE VALLEY"
        ),
        latitude=39.577716407905484,
        longitude=-104.82941005246789,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    DOVER = PopulatedPlace(
        name="Dover",
        abbreviations=PlaceAbbreviations(
            three_letter="DOV",
            five_letter="DOVER",
            seven_letter="DOVER",
            fourteen_letter="DOVER"
        ),
        latitude=40.779432172711665,
        longitude=-104.81247989327863,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    DOWDS_JUNCTION = PopulatedPlace(
        name="Dowds Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="DOW",
            five_letter="DOWDS",
            seven_letter="DOWDS J",
            fourteen_letter="DOWDS JUNCTION"
        ),
        latitude=39.608325599810144,
        longitude=-106.44781832595316,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    DOWNIEVILLE = PopulatedPlace(
        name="Downieville",
        abbreviations=PlaceAbbreviations(
            three_letter="DOW",
            five_letter="DOWNI",
            seven_letter="DOWNIEV",
            fourteen_letter="DOWNIEVILLE"
        ),
        latitude=39.76666067943563,
        longitude=-105.61445545536401,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    DOYLEVILLE = PopulatedPlace(
        name="Doyleville",
        abbreviations=PlaceAbbreviations(
            three_letter="DOY",
            five_letter="DOYLE",
            seven_letter="DOYLEVI",
            fourteen_letter="DOYLEVILLE"
        ),
        latitude=38.45166643190527,
        longitude=-106.609487631766,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    DRAKE = PopulatedPlace(
        name="Drake",
        abbreviations=PlaceAbbreviations(
            three_letter="DRA",
            five_letter="DRAKE",
            seven_letter="DRAKE",
            fourteen_letter="DRAKE"
        ),
        latitude=40.4319344884218,
        longitude=-105.3402782723523,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    DRAKES = PopulatedPlace(
        name="Drakes",
        abbreviations=PlaceAbbreviations(
            three_letter="DRA",
            five_letter="DRAKE",
            seven_letter="DRAKES",
            fourteen_letter="DRAKES"
        ),
        latitude=40.554155723481415,
        longitude=-105.07998892685208,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    DUFFIELD = PopulatedPlace(
        name="Duffield",
        abbreviations=PlaceAbbreviations(
            three_letter="DUF",
            five_letter="DUFFI",
            seven_letter="DUFFIEL",
            fourteen_letter="DUFFIELD"
        ),
        latitude=38.74221788519242,
        longitude=-104.91248287856604,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    DUMONT = PopulatedPlace(
        name="Dumont",
        abbreviations=PlaceAbbreviations(
            three_letter="DUM",
            five_letter="DUMON",
            seven_letter="DUMONT",
            fourteen_letter="DUMONT"
        ),
        latitude=39.76471628002753,
        longitude=-105.60028825168058,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    DUNCAN = PopulatedPlace(
        name="Duncan",
        abbreviations=PlaceAbbreviations(
            three_letter="DUN",
            five_letter="DUNCA",
            seven_letter="DUNCAN",
            fourteen_letter="DUNCAN"
        ),
        latitude=37.87417281541303,
        longitude=-105.61446614801088,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    DUNCKLEY = PopulatedPlace(
        name="Dunckley",
        abbreviations=PlaceAbbreviations(
            three_letter="DUN",
            five_letter="DUNCK",
            seven_letter="DUNCKLE",
            fourteen_letter="DUNCKLEY"
        ),
        latitude=40.300818037269266,
        longitude=-107.1942320762127,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    DUNTON = PopulatedPlace(
        name="Dunton",
        abbreviations=PlaceAbbreviations(
            three_letter="DUN",
            five_letter="DUNTO",
            seven_letter="DUNTON",
            fourteen_letter="DUNTON"
        ),
        latitude=37.772777740780214,
        longitude=-108.09397378529047,
        counties=[Counties.DOLORES],
        nearest_airport=Airports.TELLURIDE
    )
    DUNUL = PopulatedPlace(
        name="Dunul",
        abbreviations=PlaceAbbreviations(
            three_letter="DUN",
            five_letter="DUNUL",
            seven_letter="DUNUL",
            fourteen_letter="DUNUL"
        ),
        latitude=37.66222995432639,
        longitude=-106.10253713641396,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    DUPONT = PopulatedPlace(
        name="Dupont",
        abbreviations=PlaceAbbreviations(
            three_letter="DUP",
            five_letter="DUPON",
            seven_letter="DUPONT",
            fourteen_letter="DUPONT"
        ),
        latitude=39.838048038306056,
        longitude=-104.9119321017024,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    DURANGO = PopulatedPlace(
        name="Durango",
        abbreviations=PlaceAbbreviations(
            three_letter="DUR",
            five_letter="DURAN",
            seven_letter="DURANGO",
            fourteen_letter="DURANGO"
        ),
        latitude=37.275285887032624,
        longitude=-107.88007718883347,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    DURHAM = PopulatedPlace(
        name="Durham",
        abbreviations=PlaceAbbreviations(
            three_letter="DUR",
            five_letter="DURHA",
            seven_letter="DURHAM",
            fourteen_letter="DURHAM"
        ),
        latitude=39.08776528057575,
        longitude=-108.59899453861397,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    DYKE = PopulatedPlace(
        name="Dyke",
        abbreviations=PlaceAbbreviations(
            three_letter="DYK",
            five_letter="DYKE",
            seven_letter="DYKE",
            fourteen_letter="DYKE"
        ),
        latitude=37.22639852303365,
        longitude=-107.195331835106,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    EADS = PopulatedPlace(
        name="Eads",
        abbreviations=PlaceAbbreviations(
            three_letter="EAD",
            five_letter="EADS",
            seven_letter="EADS",
            fourteen_letter="EADS"
        ),
        latitude=38.4805678851622,
        longitude=-102.78187235286333,
        counties=[Counties.KIOWA],
        nearest_airport=Airports.PUEBLO
    )
    EAGLE = PopulatedPlace(
        name="Eagle",
        abbreviations=PlaceAbbreviations(
            three_letter="EAG",
            five_letter="EAGLE",
            seven_letter="EAGLE",
            fourteen_letter="EAGLE"
        ),
        latitude=39.655269779267655,
        longitude=-106.82866121606952,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    EAGLES_NEST = PopulatedPlace(
        name="Eagles Nest",
        abbreviations=PlaceAbbreviations(
            three_letter="EAG",
            five_letter="EAGLE",
            seven_letter="EAGLES ",
            fourteen_letter="EAGLES NEST"
        ),
        latitude=39.61832560500028,
        longitude=-106.3861505142242,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    EARL = PopulatedPlace(
        name="Earl",
        abbreviations=PlaceAbbreviations(
            three_letter="EAR",
            five_letter="EARL",
            seven_letter="EARL",
            fourteen_letter="EARL"
        ),
        latitude=37.33335491999071,
        longitude=-104.27831918901848,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    EAST_CANON = PopulatedPlace(
        name="East Canon",
        abbreviations=PlaceAbbreviations(
            three_letter="EAS",
            five_letter="EAST ",
            seven_letter="EAST CA",
            fourteen_letter="EAST CANON"
        ),
        latitude=38.452781923705004,
        longitude=-105.21305461727559,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    EAST_LA_SALLE = PopulatedPlace(
        name="East La Salle",
        abbreviations=PlaceAbbreviations(
            three_letter="EAS",
            five_letter="EAST ",
            seven_letter="EAST LA",
            fourteen_letter="EAST LA SALLE"
        ),
        latitude=40.354710024793235,
        longitude=-104.6824749103518,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    EAST_PORTAL = PopulatedPlace(
        name="East Portal",
        abbreviations=PlaceAbbreviations(
            three_letter="EAS",
            five_letter="EAST ",
            seven_letter="EAST PO",
            fourteen_letter="EAST PORTAL"
        ),
        latitude=39.90332679532111,
        longitude=-105.64445717811896,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    EAST_QUINCY_HIGHLANDS = PopulatedPlace(
        name="East Quincy Highlands",
        abbreviations=PlaceAbbreviations(
            three_letter="EAS",
            five_letter="EAST ",
            seven_letter="EAST QU",
            fourteen_letter="EAST QUINCY HI"
        ),
        latitude=39.64472862406865,
        longitude=-104.73112113808253,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    EAST_VANCORUM = PopulatedPlace(
        name="East Vancorum",
        abbreviations=PlaceAbbreviations(
            three_letter="EAS",
            five_letter="EAST ",
            seven_letter="EAST VA",
            fourteen_letter="EAST VANCORUM"
        ),
        latitude=38.22777436824475,
        longitude=-108.59510374108226,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.TELLURIDE
    )
    EASTDALE = PopulatedPlace(
        name="Eastdale",
        abbreviations=PlaceAbbreviations(
            three_letter="EAS",
            five_letter="EASTD",
            seven_letter="EASTDAL",
            fourteen_letter="EASTDALE"
        ),
        latitude=37.02863599103097,
        longitude=-105.65085627314642,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    EASTLAKE = PopulatedPlace(
        name="Eastlake",
        abbreviations=PlaceAbbreviations(
            three_letter="EAS",
            five_letter="EASTL",
            seven_letter="EASTLAK",
            fourteen_letter="EASTLAKE"
        ),
        latitude=39.92388034564112,
        longitude=-104.96137802317378,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    EASTONVILLE = PopulatedPlace(
        name="Eastonville",
        abbreviations=PlaceAbbreviations(
            three_letter="EAS",
            five_letter="EASTO",
            seven_letter="EASTONV",
            fourteen_letter="EASTONVILLE"
        ),
        latitude=39.06110925344137,
        longitude=-104.56220263274264,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    EASTRIDGE = PopulatedPlace(
        name="Eastridge",
        abbreviations=PlaceAbbreviations(
            three_letter="EAS",
            five_letter="EASTR",
            seven_letter="EASTRID",
            fourteen_letter="EASTRIDGE"
        ),
        latitude=39.67111751846255,
        longitude=-104.85667676989863,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    EATON = PopulatedPlace(
        name="Eaton",
        abbreviations=PlaceAbbreviations(
            three_letter="EAT",
            five_letter="EATON",
            seven_letter="EATON",
            fourteen_letter="EATON"
        ),
        latitude=40.53026474664489,
        longitude=-104.71136433822358,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ECHO = PopulatedPlace(
        name="Echo",
        abbreviations=PlaceAbbreviations(
            three_letter="ECH",
            five_letter="ECHO",
            seven_letter="ECHO",
            fourteen_letter="ECHO"
        ),
        latitude=38.442780901154265,
        longitude=-105.5388972899425,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ECHO_HILLS = PopulatedPlace(
        name="Echo Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="ECH",
            five_letter="ECHO ",
            seven_letter="ECHO HI",
            fourteen_letter="ECHO HILLS"
        ),
        latitude=39.67240888045944,
        longitude=-105.4155086991205,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.DENVER
    )
    ECKERT = PopulatedPlace(
        name="Eckert",
        abbreviations=PlaceAbbreviations(
            three_letter="ECK",
            five_letter="ECKER",
            seven_letter="ECKERT",
            fourteen_letter="ECKERT"
        ),
        latitude=38.842766492346186,
        longitude=-107.96285437308342,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    ECKLEY = PopulatedPlace(
        name="Eckley",
        abbreviations=PlaceAbbreviations(
            three_letter="ECK",
            five_letter="ECKLE",
            seven_letter="ECKLEY",
            fourteen_letter="ECKLEY"
        ),
        latitude=40.113883843500105,
        longitude=-102.4907671612292,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    EDEN = PopulatedPlace(
        name="Eden",
        abbreviations=PlaceAbbreviations(
            three_letter="EDE",
            five_letter="EDEN",
            seven_letter="EDEN",
            fourteen_letter="EDEN"
        ),
        latitude=38.31639714341895,
        longitude=-104.61637266583415,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    EDGEMONT = PopulatedPlace(
        name="Edgemont",
        abbreviations=PlaceAbbreviations(
            three_letter="EDG",
            five_letter="EDGEM",
            seven_letter="EDGEMON",
            fourteen_letter="EDGEMONT"
        ),
        latitude=39.73110480818872,
        longitude=-105.13082933996992,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    EDGEWATER = PopulatedPlace(
        name="Edgewater",
        abbreviations=PlaceAbbreviations(
            three_letter="EDG",
            five_letter="EDGEW",
            seven_letter="EDGEWAT",
            fourteen_letter="EDGEWATER"
        ),
        latitude=39.7530489155871,
        longitude=-105.06416042739124,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    EDITH = PopulatedPlace(
        name="Edith",
        abbreviations=PlaceAbbreviations(
            three_letter="EDI",
            five_letter="EDITH",
            seven_letter="EDITH",
            fourteen_letter="EDITH"
        ),
        latitude=37.00557200965517,
        longitude=-106.91032465106395,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    EDLER = PopulatedPlace(
        name="Edler",
        abbreviations=PlaceAbbreviations(
            three_letter="EDL",
            five_letter="EDLER",
            seven_letter="EDLER",
            fourteen_letter="EDLER"
        ),
        latitude=37.176413186964794,
        longitude=-102.77826492349823,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    EDWARDS = PopulatedPlace(
        name="Edwards",
        abbreviations=PlaceAbbreviations(
            three_letter="EDW",
            five_letter="EDWAR",
            seven_letter="EDWARDS",
            fourteen_letter="EDWARDS"
        ),
        latitude=39.6449922941743,
        longitude=-106.59421046253107,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    EGGERS = PopulatedPlace(
        name="Eggers",
        abbreviations=PlaceAbbreviations(
            three_letter="EGG",
            five_letter="EGGER",
            seven_letter="EGGERS",
            fourteen_letter="EGGERS"
        ),
        latitude=40.69082111192603,
        longitude=-105.48750323792854,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    EGNAR = PopulatedPlace(
        name="Egnar",
        abbreviations=PlaceAbbreviations(
            three_letter="EGN",
            five_letter="EGNAR",
            seven_letter="EGNAR",
            fourteen_letter="EGNAR"
        ),
        latitude=37.916386202934405,
        longitude=-108.9401169820369,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.CORTEZ
    )
    EL_JEBEL = PopulatedPlace(
        name="El Jebel",
        abbreviations=PlaceAbbreviations(
            three_letter="EL ",
            five_letter="EL JE",
            seven_letter="EL JEBE",
            fourteen_letter="EL JEBEL"
        ),
        latitude=39.394990026132405,
        longitude=-107.09033644466092,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.ASPEN
    )
    EL_RANCHO = PopulatedPlace(
        name="El Rancho",
        abbreviations=PlaceAbbreviations(
            three_letter="EL ",
            five_letter="EL RA",
            seven_letter="EL RANC",
            fourteen_letter="EL RANCHO"
        ),
        latitude=39.69860538932153,
        longitude=-105.3336135832244,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    EL_VADO = PopulatedPlace(
        name="El Vado",
        abbreviations=PlaceAbbreviations(
            three_letter="EL ",
            five_letter="EL VA",
            seven_letter="EL VADO",
            fourteen_letter="EL VADO"
        ),
        latitude=40.00582573049644,
        longitude=-105.34639172198405,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ELBA = PopulatedPlace(
        name="Elba",
        abbreviations=PlaceAbbreviations(
            three_letter="ELB",
            five_letter="ELBA",
            seven_letter="ELBA",
            fourteen_letter="ELBA"
        ),
        latitude=39.94832407011671,
        longitude=-103.21828311663711,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    ELDER = PopulatedPlace(
        name="Elder",
        abbreviations=PlaceAbbreviations(
            three_letter="ELD",
            five_letter="ELDER",
            seven_letter="ELDER",
            fourteen_letter="ELDER"
        ),
        latitude=38.12334535662211,
        longitude=-103.96719019486682,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    ELDORA = PopulatedPlace(
        name="Eldora",
        abbreviations=PlaceAbbreviations(
            three_letter="ELD",
            five_letter="ELDOR",
            seven_letter="ELDORA",
            fourteen_letter="ELDORA"
        ),
        latitude=39.94860450764929,
        longitude=-105.56389886496015,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ELDORADO_ESTATES = PopulatedPlace(
        name="Eldorado Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="ELD",
            five_letter="ELDOR",
            seven_letter="ELDORAD",
            fourteen_letter="ELDORADO ESTAT"
        ),
        latitude=39.83861751872621,
        longitude=-105.18667686546348,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ELDORADO_SPRINGS = PopulatedPlace(
        name="Eldorado Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="ELD",
            five_letter="ELDOR",
            seven_letter="ELDORAD",
            fourteen_letter="ELDORADO SPRIN"
        ),
        latitude=39.93249262637323,
        longitude=-105.27694499756137,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ELDREDGE = PopulatedPlace(
        name="Eldredge",
        abbreviations=PlaceAbbreviations(
            three_letter="ELD",
            five_letter="ELDRE",
            seven_letter="ELDREDG",
            fourteen_letter="ELDREDGE"
        ),
        latitude=38.28777233228419,
        longitude=-107.76729186875588,
        counties=[Counties.OURAY],
        nearest_airport=Airports.MONTROSE
    )
    ELEPHANT_PARK = PopulatedPlace(
        name="Elephant Park",
        abbreviations=PlaceAbbreviations(
            three_letter="ELE",
            five_letter="ELEPH",
            seven_letter="ELEPHAN",
            fourteen_letter="ELEPHANT PARK"
        ),
        latitude=39.628883478284024,
        longitude=-105.36278168197225,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ELIZABETH = PopulatedPlace(
        name="Elizabeth",
        abbreviations=PlaceAbbreviations(
            three_letter="ELI",
            five_letter="ELIZA",
            seven_letter="ELIZABE",
            fourteen_letter="ELIZABETH"
        ),
        latitude=39.36027259311544,
        longitude=-104.5969249744677,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.DENVER
    )
    ELK_SPRINGS = PopulatedPlace(
        name="Elk Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="ELK",
            five_letter="ELK S",
            seven_letter="ELK SPR",
            fourteen_letter="ELK SPRINGS"
        ),
        latitude=40.35553025181639,
        longitude=-108.4484414595388,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    ELKDALE = PopulatedPlace(
        name="Elkdale",
        abbreviations=PlaceAbbreviations(
            three_letter="ELK",
            five_letter="ELKDA",
            seven_letter="ELKDALE",
            fourteen_letter="ELKDALE"
        ),
        latitude=40.04027039736184,
        longitude=-105.88113394884664,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ELKHEAD = PopulatedPlace(
        name="Elkhead",
        abbreviations=PlaceAbbreviations(
            three_letter="ELK",
            five_letter="ELKHE",
            seven_letter="ELKHEAD",
            fourteen_letter="ELKHEAD"
        ),
        latitude=40.64858968066824,
        longitude=-107.20756802294966,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    """
    ELKTON = PopulatedPlace(
        name="Elkton",
        abbreviations=PlaceAbbreviations(
            three_letter="ELK",
            five_letter="ELKTO",
            seven_letter="ELKTON",
            fourteen_letter="ELKTON"
        ),
        latitude=38.722217666285985,
        longitude=-105.15054643159834,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ELKTON = PopulatedPlace(
        name="Elkton",
        abbreviations=PlaceAbbreviations(
            three_letter="ELK",
            five_letter="ELKTO",
            seven_letter="ELKTON",
            fourteen_letter="ELKTON"
        ),
        latitude=38.96360847273354,
        longitude=-107.03339018255679,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    """
    ELM = PopulatedPlace(
        name="Elm",
        abbreviations=PlaceAbbreviations(
            three_letter="ELM",
            five_letter="ELM",
            seven_letter="ELM",
            fourteen_letter="ELM"
        ),
        latitude=40.35359931734149,
        longitude=-104.7838682334758,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ELSMERE = PopulatedPlace(
        name="Elsmere",
        abbreviations=PlaceAbbreviations(
            three_letter="ELS",
            five_letter="ELSME",
            seven_letter="ELSMERE",
            fourteen_letter="ELSMERE"
        ),
        latitude=38.864723015759466,
        longitude=-104.71053874605332,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ELWELL = PopulatedPlace(
        name="Elwell",
        abbreviations=PlaceAbbreviations(
            three_letter="ELW",
            five_letter="ELWEL",
            seven_letter="ELWELL",
            fourteen_letter="ELWELL"
        ),
        latitude=40.33610070358634,
        longitude=-104.94193026802708,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    EMMA = PopulatedPlace(
        name="Emma",
        abbreviations=PlaceAbbreviations(
            three_letter="EMM",
            five_letter="EMMA",
            seven_letter="EMMA",
            fourteen_letter="EMMA"
        ),
        latitude=39.36499032432471,
        longitude=-107.06172433570043,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    EMPIRE = PopulatedPlace(
        name="Empire",
        abbreviations=PlaceAbbreviations(
            three_letter="EMP",
            five_letter="EMPIR",
            seven_letter="EMPIRE",
            fourteen_letter="EMPIRE"
        ),
        latitude=39.761382673497906,
        longitude=-105.68445817047234,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ENGLEVILLE = PopulatedPlace(
        name="Engleville",
        abbreviations=PlaceAbbreviations(
            three_letter="ENG",
            five_letter="ENGLE",
            seven_letter="ENGLEVI",
            fourteen_letter="ENGLEVILLE"
        ),
        latitude=37.14946978043923,
        longitude=-104.475272316847,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    ENGLEWOOD = PopulatedPlace(
        name="Englewood",
        abbreviations=PlaceAbbreviations(
            three_letter="ENG",
            five_letter="ENGLE",
            seven_letter="ENGLEWO",
            fourteen_letter="ENGLEWOOD"
        ),
        latitude=39.647771706177764,
        longitude=-104.98776979768752,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    ENO = PopulatedPlace(
        name="Eno",
        abbreviations=PlaceAbbreviations(
            three_letter="ENO",
            five_letter="ENO",
            seven_letter="ENO",
            fourteen_letter="ENO"
        ),
        latitude=39.88721404928765,
        longitude=-104.84415119248115,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    ERIE = PopulatedPlace(
        name="Erie",
        abbreviations=PlaceAbbreviations(
            three_letter="ERI",
            five_letter="ERIE",
            seven_letter="ERIE",
            fourteen_letter="ERIE"
        ),
        latitude=40.050268757471486,
        longitude=-105.04999186006529,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ESCALANTE = PopulatedPlace(
        name="Escalante",
        abbreviations=PlaceAbbreviations(
            three_letter="ESC",
            five_letter="ESCAL",
            seven_letter="ESCALAN",
            fourteen_letter="ESCALANTE"
        ),
        latitude=38.7577681607537,
        longitude=-108.26175492825928,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    ESPINOSA = PopulatedPlace(
        name="Espinosa",
        abbreviations=PlaceAbbreviations(
            three_letter="ESP",
            five_letter="ESPIN",
            seven_letter="ESPINOS",
            fourteen_letter="ESPINOSA"
        ),
        latitude=37.13057358781384,
        longitude=-105.94614224926585,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    ESTABROOK = PopulatedPlace(
        name="Estabrook",
        abbreviations=PlaceAbbreviations(
            three_letter="EST",
            five_letter="ESTAB",
            seven_letter="ESTABRO",
            fourteen_letter="ESTABROOK"
        ),
        latitude=39.38305133962831,
        longitude=-105.4294529687981,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    ESTES_PARK = PopulatedPlace(
        name="Estes Park",
        abbreviations=PlaceAbbreviations(
            three_letter="EST",
            five_letter="ESTES",
            seven_letter="ESTES P",
            fourteen_letter="ESTES PARK"
        ),
        latitude=40.37721236799962,
        longitude=-105.52167540735627,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ESTRELLA = PopulatedPlace(
        name="Estrella",
        abbreviations=PlaceAbbreviations(
            three_letter="EST",
            five_letter="ESTRE",
            seven_letter="ESTRELL",
            fourteen_letter="ESTRELLA"
        ),
        latitude=37.366123822949305,
        longitude=-105.92447716723194,
        counties=[Counties.ALAMOSA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    EUREKA = PopulatedPlace(
        name="Eureka",
        abbreviations=PlaceAbbreviations(
            three_letter="EUR",
            five_letter="EUREK",
            seven_letter="EUREKA",
            fourteen_letter="EUREKA"
        ),
        latitude=37.87972469001113,
        longitude=-107.56506988193593,
        counties=[Counties.SAN_JUAN],
        nearest_airport=Airports.TELLURIDE
    )
    EVANS = PopulatedPlace(
        name="Evans",
        abbreviations=PlaceAbbreviations(
            three_letter="EVA",
            five_letter="EVANS",
            seven_letter="EVANS",
            fourteen_letter="EVANS"
        ),
        latitude=40.37637662729253,
        longitude=-104.69219751501237,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    EVANSTON = PopulatedPlace(
        name="Evanston",
        abbreviations=PlaceAbbreviations(
            three_letter="EVA",
            five_letter="EVANS",
            seven_letter="EVANSTO",
            fourteen_letter="EVANSTON"
        ),
        latitude=40.10693477328397,
        longitude=-104.93859834028143,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    EVANSVILLE = PopulatedPlace(
        name="Evansville",
        abbreviations=PlaceAbbreviations(
            three_letter="EVA",
            five_letter="EVANS",
            seven_letter="EVANSVI",
            fourteen_letter="EVANSVILLE"
        ),
        latitude=37.67112014127764,
        longitude=-106.31893288551703,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    EVERETT = PopulatedPlace(
        name="Everett",
        abbreviations=PlaceAbbreviations(
            three_letter="EVE",
            five_letter="EVERE",
            seven_letter="EVERETT",
            fourteen_letter="EVERETT"
        ),
        latitude=39.06777552289708,
        longitude=-106.50198327547838,
        counties=[Counties.LAKE],
        nearest_airport=Airports.ASPEN
    )
    EVERGREEN = PopulatedPlace(
        name="Evergreen",
        abbreviations=PlaceAbbreviations(
            three_letter="EVE",
            five_letter="EVERG",
            seven_letter="EVERGRE",
            fourteen_letter="EVERGREEN"
        ),
        latitude=39.63332768157636,
        longitude=-105.31722477128335,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    FAIRPLAY = PopulatedPlace(
        name="Fairplay",
        abbreviations=PlaceAbbreviations(
            three_letter="FAI",
            five_letter="FAIRP",
            seven_letter="FAIRPLA",
            fourteen_letter="FAIRPLAY"
        ),
        latitude=39.22471887862463,
        longitude=-106.00197208064321,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    """
    FAIRVIEW = PopulatedPlace(
        name="Fairview",
        abbreviations=PlaceAbbreviations(
            three_letter="FAI",
            five_letter="FAIRV",
            seven_letter="FAIRVIE",
            fourteen_letter="FAIRVIEW"
        ),
        latitude=38.74388366876997,
        longitude=-105.15832403544681,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FAIRVIEW = PopulatedPlace(
        name="Fairview",
        abbreviations=PlaceAbbreviations(
            three_letter="FAI",
            five_letter="FAIRV",
            seven_letter="FAIRVIE",
            fourteen_letter="FAIRVIEW"
        ),
        latitude=38.4888811563506,
        longitude=-107.80312619903862,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FAIRVIEW = PopulatedPlace(
        name="Fairview",
        abbreviations=PlaceAbbreviations(
            three_letter="FAI",
            five_letter="FAIRV",
            seven_letter="FAIRVIE",
            fourteen_letter="FAIRVIEW"
        ),
        latitude=39.838339730668224,
        longitude=-105.0183434265798,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FAIRVIEW = PopulatedPlace(
        name="Fairview",
        abbreviations=PlaceAbbreviations(
            three_letter="FAI",
            five_letter="FAIRV",
            seven_letter="FAIRVIE",
            fourteen_letter="FAIRVIEW"
        ),
        latitude=38.0677890761728,
        longitude=-105.0991685510561,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    """
    FALCON = PopulatedPlace(
        name="Falcon",
        abbreviations=PlaceAbbreviations(
            three_letter="FAL",
            five_letter="FALCO",
            seven_letter="FALCON",
            fourteen_letter="FALCON"
        ),
        latitude=38.93305573226104,
        longitude=-104.60859252963485,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FALFA = PopulatedPlace(
        name="Falfa",
        abbreviations=PlaceAbbreviations(
            three_letter="FAL",
            five_letter="FALFA",
            seven_letter="FALFA",
            fourteen_letter="FALFA"
        ),
        latitude=37.21306468401406,
        longitude=-107.7909075633774,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    FAR_HORIZON = PopulatedPlace(
        name="Far Horizon",
        abbreviations=PlaceAbbreviations(
            three_letter="FAR",
            five_letter="FAR H",
            seven_letter="FAR HOR",
            fourteen_letter="FAR HORIZON"
        ),
        latitude=39.849728629287824,
        longitude=-105.05723233695079,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    FARISITA = PopulatedPlace(
        name="Farisita",
        abbreviations=PlaceAbbreviations(
            three_letter="FAR",
            five_letter="FARIS",
            seven_letter="FARISIT",
            fourteen_letter="FARISITA"
        ),
        latitude=37.7447366313296,
        longitude=-105.07139471129125,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    FARMERS = PopulatedPlace(
        name="Farmers",
        abbreviations=PlaceAbbreviations(
            three_letter="FAR",
            five_letter="FARME",
            seven_letter="FARMERS",
            fourteen_letter="FARMERS"
        ),
        latitude=40.451931830834724,
        longitude=-104.77914524474977,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    FAYETTE = PopulatedPlace(
        name="Fayette",
        abbreviations=PlaceAbbreviations(
            three_letter="FAY",
            five_letter="FAYET",
            seven_letter="FAYETTE",
            fourteen_letter="FAYETTE"
        ),
        latitude=38.07279166174061,
        longitude=-103.76940544357927,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    FEARNOWVILLE = PopulatedPlace(
        name="Fearnowville",
        abbreviations=PlaceAbbreviations(
            three_letter="FEA",
            five_letter="FEARN",
            seven_letter="FEARNOW",
            fourteen_letter="FEARNOWVILLE"
        ),
        latitude=38.27917534155711,
        longitude=-104.5602602487229,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    FEDERAL_HEIGHTS = PopulatedPlace(
        name="Federal Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="FED",
            five_letter="FEDER",
            seven_letter="FEDERAL",
            fourteen_letter="FEDERAL HEIGHT"
        ),
        latitude=39.85138113351388,
        longitude=-104.99860232388221,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    FENDERS = PopulatedPlace(
        name="Fenders",
        abbreviations=PlaceAbbreviations(
            three_letter="FEN",
            five_letter="FENDE",
            seven_letter="FENDERS",
            fourteen_letter="FENDERS"
        ),
        latitude=39.573883380599966,
        longitude=-105.21694444193167,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    FERNCLIFF = PopulatedPlace(
        name="Ferncliff",
        abbreviations=PlaceAbbreviations(
            three_letter="FER",
            five_letter="FERNC",
            seven_letter="FERNCLI",
            fourteen_letter="FERNCLIFF"
        ),
        latitude=40.19082474344003,
        longitude=-105.51306468255711,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    FERNDALE = PopulatedPlace(
        name="Ferndale",
        abbreviations=PlaceAbbreviations(
            three_letter="FER",
            five_letter="FERND",
            seven_letter="FERNDAL",
            fourteen_letter="FERNDALE"
        ),
        latitude=39.40610655473955,
        longitude=-105.25555863131916,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    FINK = PopulatedPlace(
        name="Fink",
        abbreviations=PlaceAbbreviations(
            three_letter="FIN",
            five_letter="FINK",
            seven_letter="FINK",
            fourteen_letter="FINK"
        ),
        latitude=38.488891818021784,
        longitude=-105.38111435925498,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FIR = PopulatedPlace(
        name="Fir",
        abbreviations=PlaceAbbreviations(
            three_letter="FIR",
            five_letter="FIR",
            seven_letter="FIR",
            fourteen_letter="FIR"
        ),
        latitude=37.485293586775015,
        longitude=-105.17945761037817,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    FIRESTONE = PopulatedPlace(
        name="Firestone",
        abbreviations=PlaceAbbreviations(
            three_letter="FIR",
            five_letter="FIRES",
            seven_letter="FIRESTO",
            fourteen_letter="FIRESTONE"
        ),
        latitude=40.1124903740415,
        longitude=-104.93665374011795,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    FIRSTVIEW = PopulatedPlace(
        name="Firstview",
        abbreviations=PlaceAbbreviations(
            three_letter="FIR",
            five_letter="FIRST",
            seven_letter="FIRSTVI",
            fourteen_letter="FIRSTVIEW"
        ),
        latitude=38.815843850565386,
        longitude=-102.53964672994823,
        counties=[Counties.CHEYENNE],
        nearest_airport=Airports.PUEBLO
    )
    FIVE_POINTS = PopulatedPlace(
        name="Five Points",
        abbreviations=PlaceAbbreviations(
            three_letter="FIV",
            five_letter="FIVE ",
            seven_letter="FIVE PO",
            fourteen_letter="FIVE POINTS"
        ),
        latitude=39.75472862214781,
        longitude=-104.97806570730495,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    FLAGLER = PopulatedPlace(
        name="Flagler",
        abbreviations=PlaceAbbreviations(
            three_letter="FLA",
            five_letter="FLAGL",
            seven_letter="FLAGLER",
            fourteen_letter="FLAGLER"
        ),
        latitude=39.29305278608126,
        longitude=-103.06716780717863,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.DENVER
    )
    FLEMING = PopulatedPlace(
        name="Fleming",
        abbreviations=PlaceAbbreviations(
            three_letter="FLE",
            five_letter="FLEMI",
            seven_letter="FLEMING",
            fourteen_letter="FLEMING"
        ),
        latitude=40.679998099875206,
        longitude=-102.83937241286526,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    FLORENCE = PopulatedPlace(
        name="Florence",
        abbreviations=PlaceAbbreviations(
            three_letter="FLO",
            five_letter="FLORE",
            seven_letter="FLORENC",
            fourteen_letter="FLORENCE"
        ),
        latitude=38.39028392110623,
        longitude=-105.11860878820221,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FLORESTA = PopulatedPlace(
        name="Floresta",
        abbreviations=PlaceAbbreviations(
            three_letter="FLO",
            five_letter="FLORE",
            seven_letter="FLOREST",
            fourteen_letter="FLORESTA"
        ),
        latitude=38.8419436501664,
        longitude=-107.122837388334,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    FLORIDA = PopulatedPlace(
        name="Florida",
        abbreviations=PlaceAbbreviations(
            three_letter="FLO",
            five_letter="FLORI",
            seven_letter="FLORIDA",
            fourteen_letter="FLORIDA"
        ),
        latitude=37.21500948624089,
        longitude=-107.75257305547063,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    FONDIS = PopulatedPlace(
        name="Fondis",
        abbreviations=PlaceAbbreviations(
            three_letter="FON",
            five_letter="FONDI",
            seven_letter="FONDIS",
            fourteen_letter="FONDIS"
        ),
        latitude=39.21582779000818,
        longitude=-104.34719669955479,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FORD = PopulatedPlace(
        name="Ford",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORD",
            seven_letter="FORD",
            fourteen_letter="FORD"
        ),
        latitude=40.716661384272584,
        longitude=-103.13521368796751,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    FORDER = PopulatedPlace(
        name="Forder",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORDE",
            seven_letter="FORDER",
            fourteen_letter="FORDER"
        ),
        latitude=38.680837054933704,
        longitude=-103.70579019301056,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.PUEBLO
    )
    FORDS_MOUNTAINDALE_RANCH = PopulatedPlace(
        name="Fords Mountaindale Ranch",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORDS",
            seven_letter="FORDS M",
            fourteen_letter="FORDS MOUNTAIN"
        ),
        latitude=38.60222286260358,
        longitude=-104.94804357213178,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FORT_BIG_SPRING = PopulatedPlace(
        name="Fort Big Spring",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORT ",
            seven_letter="FORT BI",
            fourteen_letter="FORT BIG SPRIN"
        ),
        latitude=38.933338649022005,
        longitude=-102.829658111333,
        counties=[Counties.CHEYENNE],
        nearest_airport=Airports.PUEBLO
    )
    FORT_BOETTCHER = PopulatedPlace(
        name="Fort Boettcher",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORT ",
            seven_letter="FORT BO",
            fourteen_letter="FORT BOETTCHER"
        ),
        latitude=40.80442464982298,
        longitude=-106.54393459385682,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    FORT_CARSON = PopulatedPlace(
        name="Fort Carson",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORT ",
            seven_letter="FORT CA",
            fourteen_letter="FORT CARSON"
        ),
        latitude=38.73750059218338,
        longitude=-104.788871449858,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FORT_COLLINS = PopulatedPlace(
        name="Fort Collins",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORT ",
            seven_letter="FORT CO",
            fourteen_letter="FORT COLLINS"
        ),
        latitude=40.58526672731159,
        longitude=-105.08443323212572,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    FORT_GARLAND = PopulatedPlace(
        name="Fort Garland",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORT ",
            seven_letter="FORT GA",
            fourteen_letter="FORT GARLAND"
        ),
        latitude=37.42890346269331,
        longitude=-105.43390986216394,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    FORT_LUPTON = PopulatedPlace(
        name="Fort Lupton",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORT ",
            seven_letter="FORT LU",
            fourteen_letter="FORT LUPTON"
        ),
        latitude=40.084711978487576,
        longitude=-104.81303760783112,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    FORT_LYON = PopulatedPlace(
        name="Fort Lyon",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORT ",
            seven_letter="FORT LY",
            fourteen_letter="FORT LYON"
        ),
        latitude=38.092235103882274,
        longitude=-103.15215990094907,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    FORT_MORGAN = PopulatedPlace(
        name="Fort Morgan",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORT ",
            seven_letter="FORT MO",
            fourteen_letter="FORT MORGAN"
        ),
        latitude=40.25026477242511,
        longitude=-103.79996089057028,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    FORT_REYNOLDS = PopulatedPlace(
        name="Fort Reynolds",
        abbreviations=PlaceAbbreviations(
            three_letter="FOR",
            five_letter="FORT ",
            seven_letter="FORT RE",
            fourteen_letter="FORT REYNOLDS"
        ),
        latitude=38.23056425105699,
        longitude=-104.30331028429015,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    FOSSTON = PopulatedPlace(
        name="Fosston",
        abbreviations=PlaceAbbreviations(
            three_letter="FOS",
            five_letter="FOSST",
            seven_letter="FOSSTON",
            fourteen_letter="FOSSTON"
        ),
        latitude=40.5685999769787,
        longitude=-104.35996196006647,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    FOUNDERS_VILLAGE = PopulatedPlace(
        name="Founders Village",
        abbreviations=PlaceAbbreviations(
            three_letter="FOU",
            five_letter="FOUND",
            seven_letter="FOUNDER",
            fourteen_letter="FOUNDERS VILLA"
        ),
        latitude=39.375806381247685,
        longitude=-104.8086100246964,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    FOUNTAIN = PopulatedPlace(
        name="Fountain",
        abbreviations=PlaceAbbreviations(
            three_letter="FOU",
            five_letter="FOUNT",
            seven_letter="FOUNTAI",
            fourteen_letter="FOUNTAIN"
        ),
        latitude=38.68222529017055,
        longitude=-104.70081552335176,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    FOUNTAIN_SIDE = PopulatedPlace(
        name="Fountain Side",
        abbreviations=PlaceAbbreviations(
            three_letter="FOU",
            five_letter="FOUNT",
            seven_letter="FOUNTAI",
            fourteen_letter="FOUNTAIN SIDE"
        ),
        latitude=39.687506420664306,
        longitude=-104.85945447214829,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    FOUR_CORNERS_CROSSING = PopulatedPlace(
        name="Four Corners Crossing",
        abbreviations=PlaceAbbreviations(
            three_letter="FOU",
            five_letter="FOUR ",
            seven_letter="FOUR CO",
            fourteen_letter="FOUR CORNERS C"
        ),
        latitude=38.026681116905934,
        longitude=-102.7779847057235,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    FOWLER = PopulatedPlace(
        name="Fowler",
        abbreviations=PlaceAbbreviations(
            three_letter="FOW",
            five_letter="FOWLE",
            seven_letter="FOWLER",
            fourteen_letter="FOWLER"
        ),
        latitude=38.12917835433535,
        longitude=-104.0233031087464,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    FOX_CREEK = PopulatedPlace(
        name="Fox Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="FOX",
            five_letter="FOX C",
            seven_letter="FOX CRE",
            fourteen_letter="FOX CREEK"
        ),
        latitude=37.06557246216471,
        longitude=-106.2014265000065,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    FOXFIELD = PopulatedPlace(
        name="Foxfield",
        abbreviations=PlaceAbbreviations(
            three_letter="FOX",
            five_letter="FOXFI",
            seven_letter="FOXFIEL",
            fourteen_letter="FOXFIELD"
        ),
        latitude=39.591661612488224,
        longitude=-104.79248494554628,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    FOXTON = PopulatedPlace(
        name="Foxton",
        abbreviations=PlaceAbbreviations(
            three_letter="FOX",
            five_letter="FOXTO",
            seven_letter="FOXTON",
            fourteen_letter="FOXTON"
        ),
        latitude=39.424439658417725,
        longitude=-105.2361133285732,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    FRANKTOWN = PopulatedPlace(
        name="Franktown",
        abbreviations=PlaceAbbreviations(
            three_letter="FRA",
            five_letter="FRANK",
            seven_letter="FRANKTO",
            fourteen_letter="FRANKTOWN"
        ),
        latitude=39.39138518732699,
        longitude=-104.75276301393751,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    FRASER = PopulatedPlace(
        name="Fraser",
        abbreviations=PlaceAbbreviations(
            three_letter="FRA",
            five_letter="FRASE",
            seven_letter="FRASER",
            fourteen_letter="FRASER"
        ),
        latitude=39.94499318934146,
        longitude=-105.8172419228473,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    FREDERICK = PopulatedPlace(
        name="Frederick",
        abbreviations=PlaceAbbreviations(
            three_letter="FRE",
            five_letter="FREDE",
            seven_letter="FREDERI",
            fourteen_letter="FREDERICK"
        ),
        latitude=40.09915707212315,
        longitude=-104.93720943885103,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    FREELAND = PopulatedPlace(
        name="Freeland",
        abbreviations=PlaceAbbreviations(
            three_letter="FRE",
            five_letter="FREEL",
            seven_letter="FREELAN",
            fourteen_letter="FREELAND"
        ),
        latitude=39.74416077770911,
        longitude=-105.59556584865612,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    FRICK = PopulatedPlace(
        name="Frick",
        abbreviations=PlaceAbbreviations(
            three_letter="FRI",
            five_letter="FRICK",
            seven_letter="FRICK",
            fourteen_letter="FRICK"
        ),
        latitude=37.585296038989384,
        longitude=-102.95549040449367,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    FRIENDLY_VILLAGE = PopulatedPlace(
        name="Friendly Village",
        abbreviations=PlaceAbbreviations(
            three_letter="FRI",
            five_letter="FRIEN",
            seven_letter="FRIENDL",
            fourteen_letter="FRIENDLY VILLA"
        ),
        latitude=39.743895333844364,
        longitude=-104.78862116215186,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    FRISCO = PopulatedPlace(
        name="Frisco",
        abbreviations=PlaceAbbreviations(
            three_letter="FRI",
            five_letter="FRISC",
            seven_letter="FRISCO",
            fourteen_letter="FRISCO"
        ),
        latitude=39.57443721917679,
        longitude=-106.09753074269054,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    FROST = PopulatedPlace(
        name="Frost",
        abbreviations=PlaceAbbreviations(
            three_letter="FRO",
            five_letter="FROST",
            seven_letter="FROST",
            fourteen_letter="FROST"
        ),
        latitude=38.56721405589133,
        longitude=-107.97007644348878,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    FRUITA = PopulatedPlace(
        name="Fruita",
        abbreviations=PlaceAbbreviations(
            three_letter="FRU",
            five_letter="FRUIT",
            seven_letter="FRUITA",
            fourteen_letter="FRUITA"
        ),
        latitude=39.15887568050579,
        longitude=-108.72899907417974,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    FRUITVALE = PopulatedPlace(
        name="Fruitvale",
        abbreviations=PlaceAbbreviations(
            three_letter="FRU",
            five_letter="FRUIT",
            seven_letter="FRUITVA",
            fourteen_letter="FRUITVALE"
        ),
        latitude=39.081654086935885,
        longitude=-108.49676871527515,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    FUNSTON = PopulatedPlace(
        name="Funston",
        abbreviations=PlaceAbbreviations(
            three_letter="FUN",
            five_letter="FUNST",
            seven_letter="FUNSTON",
            fourteen_letter="FUNSTON"
        ),
        latitude=39.560543629874815,
        longitude=-107.34923132097248,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    FUTURITY = PopulatedPlace(
        name="Futurity",
        abbreviations=PlaceAbbreviations(
            three_letter="FUT",
            five_letter="FUTUR",
            seven_letter="FUTURIT",
            fourteen_letter="FUTURITY"
        ),
        latitude=38.73639091451133,
        longitude=-105.95391021598789,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    GALATEA = PopulatedPlace(
        name="Galatea",
        abbreviations=PlaceAbbreviations(
            three_letter="GAL",
            five_letter="GALAT",
            seven_letter="GALATEA",
            fourteen_letter="GALATEA"
        ),
        latitude=38.504454472941404,
        longitude=-103.0246574115032,
        counties=[Counties.KIOWA],
        nearest_airport=Airports.PUEBLO
    )
    GALENA = PopulatedPlace(
        name="Galena",
        abbreviations=PlaceAbbreviations(
            three_letter="GAL",
            five_letter="GALEN",
            seven_letter="GALENA",
            fourteen_letter="GALENA"
        ),
        latitude=38.261951192390256,
        longitude=-105.2777818114862,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.PUEBLO
    )
    GALETON = PopulatedPlace(
        name="Galeton",
        abbreviations=PlaceAbbreviations(
            three_letter="GAL",
            five_letter="GALET",
            seven_letter="GALETON",
            fourteen_letter="GALETON"
        ),
        latitude=40.520820454294096,
        longitude=-104.58580280806933,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GALIEN = PopulatedPlace(
        name="Galien",
        abbreviations=PlaceAbbreviations(
            three_letter="GAL",
            five_letter="GALIE",
            seven_letter="GALIEN",
            fourteen_letter="GALIEN"
        ),
        latitude=40.68777458943913,
        longitude=-103.0082668541354,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    GARCIA = PopulatedPlace(
        name="Garcia",
        abbreviations=PlaceAbbreviations(
            three_letter="GAR",
            five_letter="GARCI",
            seven_letter="GARCIA",
            fourteen_letter="GARCIA"
        ),
        latitude=37.00419379419503,
        longitude=-105.53724224464281,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    GARDEN_CITY = PopulatedPlace(
        name="Garden City",
        abbreviations=PlaceAbbreviations(
            three_letter="GAR",
            five_letter="GARDE",
            seven_letter="GARDEN ",
            fourteen_letter="GARDEN CITY"
        ),
        latitude=40.393876529410534,
        longitude=-104.68941941660574,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GARDNER = PopulatedPlace(
        name="Gardner",
        abbreviations=PlaceAbbreviations(
            three_letter="GAR",
            five_letter="GARDN",
            seven_letter="GARDNER",
            fourteen_letter="GARDNER"
        ),
        latitude=37.78334583099257,
        longitude=-105.16556413683657,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    GARO = PopulatedPlace(
        name="Garo",
        abbreviations=PlaceAbbreviations(
            three_letter="GAR",
            five_letter="GARO",
            seven_letter="GARO",
            fourteen_letter="GARO"
        ),
        latitude=39.1077759701144,
        longitude=-105.8903006427717,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    GARY = PopulatedPlace(
        name="Gary",
        abbreviations=PlaceAbbreviations(
            three_letter="GAR",
            five_letter="GARY",
            seven_letter="GARY",
            fourteen_letter="GARY"
        ),
        latitude=40.0738785626171,
        longitude=-103.58495531850525,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    GASKIL = PopulatedPlace(
        name="Gaskil",
        abbreviations=PlaceAbbreviations(
            three_letter="GAS",
            five_letter="GASKI",
            seven_letter="GASKIL",
            fourteen_letter="GASKIL"
        ),
        latitude=40.3305465371522,
        longitude=-105.8622452799799,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GATES = PopulatedPlace(
        name="Gates",
        abbreviations=PlaceAbbreviations(
            three_letter="GAT",
            five_letter="GATES",
            seven_letter="GATES",
            fourteen_letter="GATES"
        ),
        latitude=40.53137584345944,
        longitude=-104.75525534837084,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GATEVIEW = PopulatedPlace(
        name="Gateview",
        abbreviations=PlaceAbbreviations(
            three_letter="GAT",
            five_letter="GATEV",
            seven_letter="GATEVIE",
            fourteen_letter="GATEVIEW"
        ),
        latitude=38.29361166935939,
        longitude=-107.2186768493662,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    """
    GATEWAY = PopulatedPlace(
        name="Gateway",
        abbreviations=PlaceAbbreviations(
            three_letter="GAT",
            five_letter="GATEW",
            seven_letter="GATEWAY",
            fourteen_letter="GATEWAY"
        ),
        latitude=38.682490501910024,
        longitude=-108.97511957297786,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    GATEWAY = PopulatedPlace(
        name="Gateway",
        abbreviations=PlaceAbbreviations(
            three_letter="GAT",
            five_letter="GATEW",
            seven_letter="GATEWAY",
            fourteen_letter="GATEWAY"
        ),
        latitude=39.549161598534056,
        longitude=-104.90610086680016,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    """
    GATEWAY_PARK = PopulatedPlace(
        name="Gateway Park",
        abbreviations=PlaceAbbreviations(
            three_letter="GAT",
            five_letter="GATEW",
            seven_letter="GATEWAY",
            fourteen_letter="GATEWAY PARK"
        ),
        latitude=39.743617528410084,
        longitude=-104.86112117937694,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    GATO = PopulatedPlace(
        name="Gato",
        abbreviations=PlaceAbbreviations(
            three_letter="GAT",
            five_letter="GATO",
            seven_letter="GATO",
            fourteen_letter="GATO"
        ),
        latitude=37.04501209770223,
        longitude=-107.19727461707942,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    GEM_VILLAGE = PopulatedPlace(
        name="Gem Village",
        abbreviations=PlaceAbbreviations(
            three_letter="GEM",
            five_letter="GEM V",
            seven_letter="GEM VIL",
            fourteen_letter="GEM VILLAGE"
        ),
        latitude=37.219176294680494,
        longitude=-107.63729083033144,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    GEMS_PARK_ESTATES = PopulatedPlace(
        name="Gems Park Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="GEM",
            five_letter="GEMS ",
            seven_letter="GEMS PA",
            fourteen_letter="GEMS PARK ESTA"
        ),
        latitude=39.59556198239619,
        longitude=-105.23667684893746,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GENESEE = PopulatedPlace(
        name="Genesee",
        abbreviations=PlaceAbbreviations(
            three_letter="GEN",
            five_letter="GENES",
            seven_letter="GENESEE",
            fourteen_letter="GENESEE"
        ),
        latitude=39.68582749210066,
        longitude=-105.27277856725618,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GENESEE_RIDGE = PopulatedPlace(
        name="Genesee Ridge",
        abbreviations=PlaceAbbreviations(
            three_letter="GEN",
            five_letter="GENES",
            seven_letter="GENESEE",
            fourteen_letter="GENESEE RIDGE"
        ),
        latitude=39.681395291368176,
        longitude=-105.27223236641055,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GENOA = PopulatedPlace(
        name="Genoa",
        abbreviations=PlaceAbbreviations(
            three_letter="GEN",
            five_letter="GENOA",
            seven_letter="GENOA",
            fourteen_letter="GENOA"
        ),
        latitude=39.27832725508563,
        longitude=-103.50023360775361,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GEORGETOWN = PopulatedPlace(
        name="Georgetown",
        abbreviations=PlaceAbbreviations(
            three_letter="GEO",
            five_letter="GEORG",
            seven_letter="GEORGET",
            fourteen_letter="GEORGETOWN"
        ),
        latitude=39.706104765436294,
        longitude=-105.69751436745668,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GIDDINGS = PopulatedPlace(
        name="Giddings",
        abbreviations=PlaceAbbreviations(
            three_letter="GID",
            five_letter="GIDDI",
            seven_letter="GIDDING",
            fourteen_letter="GIDDINGS"
        ),
        latitude=40.62137783748307,
        longitude=-105.0105412196724,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GILCREST = PopulatedPlace(
        name="Gilcrest",
        abbreviations=PlaceAbbreviations(
            three_letter="GIL",
            five_letter="GILCR",
            seven_letter="GILCRES",
            fourteen_letter="GILCREST"
        ),
        latitude=40.28193310830176,
        longitude=-104.77775732338125,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GILL = PopulatedPlace(
        name="Gill",
        abbreviations=PlaceAbbreviations(
            three_letter="GIL",
            five_letter="GILL",
            seven_letter="GILL",
            fourteen_letter="GILL"
        ),
        latitude=40.45415404850684,
        longitude=-104.54218988938447,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GILMAN = PopulatedPlace(
        name="Gilman",
        abbreviations=PlaceAbbreviations(
            three_letter="GIL",
            five_letter="GILMA",
            seven_letter="GILMAN",
            fourteen_letter="GILMAN"
        ),
        latitude=39.532770193369345,
        longitude=-106.39392800578327,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    """
    GILPIN = PopulatedPlace(
        name="Gilpin",
        abbreviations=PlaceAbbreviations(
            three_letter="GIL",
            five_letter="GILPI",
            seven_letter="GILPIN",
            fourteen_letter="GILPIN"
        ),
        latitude=37.94612537941725,
        longitude=-103.18466179414162,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    GILPIN = PopulatedPlace(
        name="Gilpin",
        abbreviations=PlaceAbbreviations(
            three_letter="GIL",
            five_letter="GILPI",
            seven_letter="GILPIN",
            fourteen_letter="GILPIN"
        ),
        latitude=39.890827003470235,
        longitude=-105.5080632457375,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.PUEBLO
    )
    """
    GILSON_GULCH = PopulatedPlace(
        name="Gilson Gulch",
        abbreviations=PlaceAbbreviations(
            three_letter="GIL",
            five_letter="GILSO",
            seven_letter="GILSON ",
            fourteen_letter="GILSON GULCH"
        ),
        latitude=39.76166108610232,
        longitude=-105.50806253067844,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.DENVER
    )
    GILSONITE = PopulatedPlace(
        name="Gilsonite",
        abbreviations=PlaceAbbreviations(
            three_letter="GIL",
            five_letter="GILSO",
            seven_letter="GILSONI",
            fourteen_letter="GILSONITE"
        ),
        latitude=39.17693117894919,
        longitude=-108.77872318682654,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    GLADE_PARK = PopulatedPlace(
        name="Glade Park",
        abbreviations=PlaceAbbreviations(
            three_letter="GLA",
            five_letter="GLADE",
            seven_letter="GLADE P",
            fourteen_letter="GLADE PARK"
        ),
        latitude=38.9935999584477,
        longitude=-108.74094375781533,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    GLEN_COMFORT = PopulatedPlace(
        name="Glen Comfort",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLEN ",
            seven_letter="GLEN CO",
            fourteen_letter="GLEN COMFORT"
        ),
        latitude=40.39360127609956,
        longitude=-105.44028289077687,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GLEN_ECHO = PopulatedPlace(
        name="Glen Echo",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLEN ",
            seven_letter="GLEN EC",
            fourteen_letter="GLEN ECHO"
        ),
        latitude=40.69859860588315,
        longitude=-105.58528546206941,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GLEN_EDEN = PopulatedPlace(
        name="Glen Eden",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLEN ",
            seven_letter="GLEN ED",
            fourteen_letter="GLEN EDEN"
        ),
        latitude=40.71720121110809,
        longitude=-106.91506046683389,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    GLEN_EYRIE = PopulatedPlace(
        name="Glen Eyrie",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLEN ",
            seven_letter="GLEN EY",
            fourteen_letter="GLEN EYRIE"
        ),
        latitude=38.891664507673,
        longitude=-104.88443158873571,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GLEN_HAVEN = PopulatedPlace(
        name="Glen Haven",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLEN ",
            seven_letter="GLEN HA",
            fourteen_letter="GLEN HAVEN"
        ),
        latitude=40.453878683562095,
        longitude=-105.449171699852,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GLEN_PARK = PopulatedPlace(
        name="Glen Park",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLEN ",
            seven_letter="GLEN PA",
            fourteen_letter="GLEN PARK"
        ),
        latitude=39.11444243706438,
        longitude=-104.92026962187407,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GLENDALE = PopulatedPlace(
        name="Glendale",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLEND",
            seven_letter="GLENDAL",
            fourteen_letter="GLENDALE"
        ),
        latitude=39.70499371841959,
        longitude=-104.9336005919443,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    GLENDEVEY = PopulatedPlace(
        name="Glendevey",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLEND",
            seven_letter="GLENDEV",
            fourteen_letter="GLENDEVEY"
        ),
        latitude=40.81026239504871,
        longitude=-105.9350206559925,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GLENEAGLE = PopulatedPlace(
        name="Gleneagle",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLENE",
            seven_letter="GLENEAG",
            fourteen_letter="GLENEAGLE"
        ),
        latitude=39.04527653391324,
        longitude=-104.82443319175775,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GLENELK = PopulatedPlace(
        name="Glenelk",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLENE",
            seven_letter="GLENELK",
            fourteen_letter="GLENELK"
        ),
        latitude=39.46306195539398,
        longitude=-105.3563990611487,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GLENISLE = PopulatedPlace(
        name="Glenisle",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLENI",
            seven_letter="GLENISL",
            fourteen_letter="GLENISLE"
        ),
        latitude=39.40888443767,
        longitude=-105.50973288955879,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    GLENTIVAR = PopulatedPlace(
        name="Glentivar",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLENT",
            seven_letter="GLENTIV",
            fourteen_letter="GLENTIVAR"
        ),
        latitude=39.04777578112487,
        longitude=-105.60417987027239,
        counties=[Counties.PARK],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GLENWOOD_SPRINGS = PopulatedPlace(
        name="Glenwood Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="GLE",
            five_letter="GLENW",
            seven_letter="GLENWOO",
            fourteen_letter="GLENWOOD SPRIN"
        ),
        latitude=39.55054383038498,
        longitude=-107.32478681461873,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    GOLCONDA = PopulatedPlace(
        name="Golconda",
        abbreviations=PlaceAbbreviations(
            three_letter="GOL",
            five_letter="GOLCO",
            seven_letter="GOLCOND",
            fourteen_letter="GOLCONDA"
        ),
        latitude=37.457502194611436,
        longitude=-108.1523105657925,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    """
    GOLD_HILL = PopulatedPlace(
        name="Gold Hill",
        abbreviations=PlaceAbbreviations(
            three_letter="GOL",
            five_letter="GOLD ",
            seven_letter="GOLD HI",
            fourteen_letter="GOLD HILL"
        ),
        latitude=40.063343433545754,
        longitude=-105.4096172438567,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GOLD_HILL = PopulatedPlace(
        name="Gold Hill",
        abbreviations=PlaceAbbreviations(
            three_letter="GOL",
            five_letter="GOLD ",
            seven_letter="GOLD HI",
            fourteen_letter="GOLD HILL"
        ),
        latitude=39.54527081874613,
        longitude=-106.04836242848972,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    GOLD_RUN = PopulatedPlace(
        name="Gold Run",
        abbreviations=PlaceAbbreviations(
            three_letter="GOL",
            five_letter="GOLD ",
            seven_letter="GOLD RU",
            fourteen_letter="GOLD RUN"
        ),
        latitude=40.05415913274885,
        longitude=-105.41139384289232,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GOLDEN = PopulatedPlace(
        name="Golden",
        abbreviations=PlaceAbbreviations(
            three_letter="GOL",
            five_letter="GOLDE",
            seven_letter="GOLDEN",
            fourteen_letter="GOLDEN"
        ),
        latitude=39.75554940484966,
        longitude=-105.22110986342881,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GOLDEN_HEIGHTS = PopulatedPlace(
        name="Golden Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="GOL",
            five_letter="GOLDE",
            seven_letter="GOLDEN ",
            fourteen_letter="GOLDEN HEIGHTS"
        ),
        latitude=39.720006403138086,
        longitude=-105.17945454981793,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GOLDEN_MEADOWS = PopulatedPlace(
        name="Golden Meadows",
        abbreviations=PlaceAbbreviations(
            three_letter="GOL",
            five_letter="GOLDE",
            seven_letter="GOLDEN ",
            fourteen_letter="GOLDEN MEADOWS"
        ),
        latitude=39.57778418004466,
        longitude=-105.2266768445171,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GOLDENWEST_PARK = PopulatedPlace(
        name="Goldenwest Park",
        abbreviations=PlaceAbbreviations(
            three_letter="GOL",
            five_letter="GOLDE",
            seven_letter="GOLDENW",
            fourteen_letter="GOLDENWEST PAR"
        ),
        latitude=39.58583969605286,
        longitude=-105.01945449795755,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    GOODALE = PopulatedPlace(
        name="Goodale",
        abbreviations=PlaceAbbreviations(
            three_letter="GOO",
            five_letter="GOODA",
            seven_letter="GOODALE",
            fourteen_letter="GOODALE"
        ),
        latitude=38.11807105214501,
        longitude=-102.43520013288656,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    GOODELL_CORNER = PopulatedPlace(
        name="Goodell Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="GOO",
            five_letter="GOODE",
            seven_letter="GOODELL",
            fourteen_letter="GOODELL CORNER"
        ),
        latitude=40.73526491109868,
        longitude=-105.58111816578827,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GOODING = PopulatedPlace(
        name="Gooding",
        abbreviations=PlaceAbbreviations(
            three_letter="GOO",
            five_letter="GOODI",
            seven_letter="GOODING",
            fourteen_letter="GOODING"
        ),
        latitude=40.07360225851818,
        longitude=-105.08304856984518,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GOODNIGHT = PopulatedPlace(
        name="Goodnight",
        abbreviations=PlaceAbbreviations(
            three_letter="GOO",
            five_letter="GOODN",
            seven_letter="GOODNIG",
            fourteen_letter="GOODNIGHT"
        ),
        latitude=38.26112013183655,
        longitude=-104.66998597251978,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    GOODPASTURE = PopulatedPlace(
        name="Goodpasture",
        abbreviations=PlaceAbbreviations(
            three_letter="GOO",
            five_letter="GOODP",
            seven_letter="GOODPAS",
            fourteen_letter="GOODPASTURE"
        ),
        latitude=38.08334569019996,
        longitude=-104.91999591149528,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    GOODRICH = PopulatedPlace(
        name="Goodrich",
        abbreviations=PlaceAbbreviations(
            three_letter="GOO",
            five_letter="GOODR",
            seven_letter="GOODRIC",
            fourteen_letter="GOODRICH"
        ),
        latitude=40.35110046812224,
        longitude=-104.06162696443062,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    GOTHIC = PopulatedPlace(
        name="Gothic",
        abbreviations=PlaceAbbreviations(
            three_letter="GOT",
            five_letter="GOTHI",
            seven_letter="GOTHIC",
            fourteen_letter="GOTHIC"
        ),
        latitude=38.95916417519044,
        longitude=-106.98977807235588,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.ASPEN
    )
    GOULD = PopulatedPlace(
        name="Gould",
        abbreviations=PlaceAbbreviations(
            three_letter="GOU",
            five_letter="GOULD",
            seven_letter="GOULD",
            fourteen_letter="GOULD"
        ),
        latitude=40.52637695149775,
        longitude=-106.02669514109186,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GOWANDA = PopulatedPlace(
        name="Gowanda",
        abbreviations=PlaceAbbreviations(
            three_letter="GOW",
            five_letter="GOWAN",
            seven_letter="GOWANDA",
            fourteen_letter="GOWANDA"
        ),
        latitude=40.20471218863406,
        longitude=-104.90054064283959,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GRAFT = PopulatedPlace(
        name="Graft",
        abbreviations=PlaceAbbreviations(
            three_letter="GRA",
            five_letter="GRAFT",
            seven_letter="GRAFT",
            fourteen_letter="GRAFT"
        ),
        latitude=37.44779842187319,
        longitude=-102.8924338763872,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    GRANADA = PopulatedPlace(
        name="Granada",
        abbreviations=PlaceAbbreviations(
            three_letter="GRA",
            five_letter="GRANA",
            seven_letter="GRANADA",
            fourteen_letter="GRANADA"
        ),
        latitude=38.06390455206366,
        longitude=-102.31047669765462,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    GRANBY = PopulatedPlace(
        name="Granby",
        abbreviations=PlaceAbbreviations(
            three_letter="GRA",
            five_letter="GRANB",
            seven_letter="GRANBY",
            fourteen_letter="GRANBY"
        ),
        latitude=40.086103399087506,
        longitude=-105.93947006729013,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GRAND_JUNCTION = PopulatedPlace(
        name="Grand Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="GRA",
            five_letter="GRAND",
            seven_letter="GRAND J",
            fourteen_letter="GRAND JUNCTION"
        ),
        latitude=39.06387658040359,
        longitude=-108.55065942531371,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    GRAND_LAKE = PopulatedPlace(
        name="Grand Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="GRA",
            five_letter="GRAND",
            seven_letter="GRAND L",
            fourteen_letter="GRAND LAKE"
        ),
        latitude=40.25221372956071,
        longitude=-105.82307746067949,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GRAND_MESA = PopulatedPlace(
        name="Grand Mesa",
        abbreviations=PlaceAbbreviations(
            three_letter="GRA",
            five_letter="GRAND",
            seven_letter="GRAND M",
            fourteen_letter="GRAND MESA"
        ),
        latitude=39.040264219516644,
        longitude=-107.9497999924925,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    GRAND_VIEW_ESTATES = PopulatedPlace(
        name="Grand View Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="GRA",
            five_letter="GRAND",
            seven_letter="GRAND V",
            fourteen_letter="GRAND VIEW EST"
        ),
        latitude=39.54360620375962,
        longitude=-104.82109774710784,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    GRANDVIEW = PopulatedPlace(
        name="Grandview",
        abbreviations=PlaceAbbreviations(
            three_letter="GRA",
            five_letter="GRAND",
            seven_letter="GRANDVI",
            fourteen_letter="GRANDVIEW"
        ),
        latitude=37.22750888346462,
        longitude=-107.82701977222206,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    GRANITE = PopulatedPlace(
        name="Granite",
        abbreviations=PlaceAbbreviations(
            three_letter="GRA",
            five_letter="GRANI",
            seven_letter="GRANITE",
            fourteen_letter="GRANITE"
        ),
        latitude=39.04361073603616,
        longitude=-106.26336561912098,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.ASPEN
    )
    GRANT = PopulatedPlace(
        name="Grant",
        abbreviations=PlaceAbbreviations(
            three_letter="GRA",
            five_letter="GRANT",
            seven_letter="GRANT",
            fourteen_letter="GRANT"
        ),
        latitude=39.459716334325606,
        longitude=-105.66168173049812,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    GRAYMONT = PopulatedPlace(
        name="Graymont",
        abbreviations=PlaceAbbreviations(
            three_letter="GRA",
            five_letter="GRAYM",
            seven_letter="GRAYMON",
            fourteen_letter="GRAYMONT"
        ),
        latitude=39.69443775646454,
        longitude=-105.80057408878895,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GREELEY = PopulatedPlace(
        name="Greeley",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEL",
            seven_letter="GREELEY",
            fourteen_letter="GREELEY"
        ),
        latitude=40.423320732340756,
        longitude=-104.70914232482562,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GREELEY_JUNCTION = PopulatedPlace(
        name="Greeley Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEL",
            seven_letter="GREELEY",
            fourteen_letter="GREELEY JUNCTI"
        ),
        latitude=40.4555428380213,
        longitude=-104.69441922567813,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GREEN_GABLES = PopulatedPlace(
        name="Green Gables",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEN",
            seven_letter="GREEN G",
            fourteen_letter="GREEN GABLES"
        ),
        latitude=39.67833970297397,
        longitude=-105.09723232588595,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GREEN_MOUNTAIN = PopulatedPlace(
        name="Green Mountain",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEN",
            seven_letter="GREEN M",
            fourteen_letter="GREEN MOUNTAIN"
        ),
        latitude=39.68833940236573,
        longitude=-105.12973213498685,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GREEN_MOUNTAIN_FALLS = PopulatedPlace(
        name="Green Mountain Falls",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEN",
            seven_letter="GREEN M",
            fourteen_letter="GREEN MOUNTAIN"
        ),
        latitude=38.934996805106266,
        longitude=-105.01693632348514,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GREEN_MOUNTAIN_VILLAGE = PopulatedPlace(
        name="Green Mountain Village",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEN",
            seven_letter="GREEN M",
            fourteen_letter="GREEN MOUNTAIN"
        ),
        latitude=39.69804940333324,
        longitude=-105.13249633645609,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GREEN_SETTLEMENT = PopulatedPlace(
        name="Green Settlement",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEN",
            seven_letter="GREEN S",
            fourteen_letter="GREEN SETTLEME"
        ),
        latitude=38.77555209068288,
        longitude=-104.89248347788481,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GREEN_VALLEY = PopulatedPlace(
        name="Green Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEN",
            seven_letter="GREEN V",
            fourteen_letter="GREEN VALLEY"
        ),
        latitude=39.78139531765038,
        longitude=-105.09417683760108,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GREEN_VALLEY_ACRES = PopulatedPlace(
        name="Green Valley Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEN",
            seven_letter="GREEN V",
            fourteen_letter="GREEN VALLEY A"
        ),
        latitude=39.50221706386611,
        longitude=-105.31194805562632,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    GREENHORN = PopulatedPlace(
        name="Greenhorn",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEN",
            seven_letter="GREENHO",
            fourteen_letter="GREENHORN"
        ),
        latitude=37.90695926800322,
        longitude=-104.85332937765543,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    GREENLAND = PopulatedPlace(
        name="Greenland",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEN",
            seven_letter="GREENLA",
            fourteen_letter="GREENLAND"
        ),
        latitude=39.18249765097545,
        longitude=-104.85526751444053,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    GREENWOOD = PopulatedPlace(
        name="Greenwood",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEN",
            seven_letter="GREENWO",
            fourteen_letter="GREENWOOD"
        ),
        latitude=38.20500939641761,
        longitude=-105.09694426402217,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.PUEBLO
    )
    GREENWOOD_VILLAGE = PopulatedPlace(
        name="Greenwood Village",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREEN",
            seven_letter="GREENWO",
            fourteen_letter="GREENWOOD VILL"
        ),
        latitude=39.617216504763064,
        longitude=-104.95082418492291,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    GREYSTONE = PopulatedPlace(
        name="Greystone",
        abbreviations=PlaceAbbreviations(
            three_letter="GRE",
            five_letter="GREYS",
            seven_letter="GREYSTO",
            fourteen_letter="GREYSTONE"
        ),
        latitude=40.609415967395535,
        longitude=-108.6740077410683,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    GRIFF = PopulatedPlace(
        name="Griff",
        abbreviations=PlaceAbbreviations(
            three_letter="GRI",
            five_letter="GRIFF",
            seven_letter="GRIFF",
            fourteen_letter="GRIFF"
        ),
        latitude=40.78221890255412,
        longitude=-103.00715296564101,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    GROTE = PopulatedPlace(
        name="Grote",
        abbreviations=PlaceAbbreviations(
            three_letter="GRO",
            five_letter="GROTE",
            seven_letter="GROTE",
            fourteen_letter="GROTE"
        ),
        latitude=38.08723764868097,
        longitude=-102.41575562514964,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    GROVER = PopulatedPlace(
        name="Grover",
        abbreviations=PlaceAbbreviations(
            three_letter="GRO",
            five_letter="GROVE",
            seven_letter="GROVER",
            fourteen_letter="GROVER"
        ),
        latitude=40.87137952792369,
        longitude=-104.22523756640345,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GUADALUPE = PopulatedPlace(
        name="Guadalupe",
        abbreviations=PlaceAbbreviations(
            three_letter="GUA",
            five_letter="GUADA",
            seven_letter="GUADALU",
            fourteen_letter="GUADALUPE"
        ),
        latitude=37.0952955777646,
        longitude=-106.02558816333686,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    GULNARE = PopulatedPlace(
        name="Gulnare",
        abbreviations=PlaceAbbreviations(
            three_letter="GUL",
            five_letter="GULNA",
            seven_letter="GULNARE",
            fourteen_letter="GULNARE"
        ),
        latitude=37.31724478871587,
        longitude=-104.75194389682389,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    GUN_CLUB_ESTATES = PopulatedPlace(
        name="Gun Club Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="GUN",
            five_letter="GUN C",
            seven_letter="GUN CLU",
            fourteen_letter="GUN CLUB ESTAT"
        ),
        latitude=39.70000643305286,
        longitude=-104.71167673994012,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    GUNBARREL = PopulatedPlace(
        name="Gunbarrel",
        abbreviations=PlaceAbbreviations(
            three_letter="GUN",
            five_letter="GUNBA",
            seven_letter="GUNBARR",
            fourteen_letter="GUNBARREL"
        ),
        latitude=40.06548844946491,
        longitude=-105.18753319259287,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    GUNNISON = PopulatedPlace(
        name="Gunnison",
        abbreviations=PlaceAbbreviations(
            three_letter="GUN",
            five_letter="GUNNI",
            seven_letter="GUNNISO",
            fourteen_letter="GUNNISON"
        ),
        latitude=38.54583072305218,
        longitude=-106.92533111208968,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    GYPSUM = PopulatedPlace(
        name="Gypsum",
        abbreviations=PlaceAbbreviations(
            three_letter="GYP",
            five_letter="GYPSU",
            seven_letter="GYPSUM",
            fourteen_letter="GYPSUM"
        ),
        latitude=39.64693576935315,
        longitude=-106.9517214430108,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    HACKBERRY_HILLS = PopulatedPlace(
        name="Hackberry Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="HAC",
            five_letter="HACKB",
            seven_letter="HACKBER",
            fourteen_letter="HACKBERRY HILL"
        ),
        latitude=39.82889532502509,
        longitude=-105.07806573893168,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    HADLEY = PopulatedPlace(
        name="Hadley",
        abbreviations=PlaceAbbreviations(
            three_letter="HAD",
            five_letter="HADLE",
            seven_letter="HADLEY",
            fourteen_letter="HADLEY"
        ),
        latitude=38.03834738007106,
        longitude=-103.40328015492082,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    HALE = PopulatedPlace(
        name="Hale",
        abbreviations=PlaceAbbreviations(
            three_letter="HAL",
            five_letter="HALE",
            seven_letter="HALE",
            fourteen_letter="HALE"
        ),
        latitude=39.62972239663554,
        longitude=-102.14269742228339,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    HALLCRAFTS_VILLAGE_EAST = PopulatedPlace(
        name="Hallcrafts Village East",
        abbreviations=PlaceAbbreviations(
            three_letter="HAL",
            five_letter="HALLC",
            seven_letter="HALLCRA",
            fourteen_letter="HALLCRAFTS VIL"
        ),
        latitude=39.693062023240316,
        longitude=-104.83889896849217,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    HAMBERT = PopulatedPlace(
        name="Hambert",
        abbreviations=PlaceAbbreviations(
            three_letter="HAM",
            five_letter="HAMBE",
            seven_letter="HAMBERT",
            fourteen_letter="HAMBERT"
        ),
        latitude=40.31498821516732,
        longitude=-104.73803331846102,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HAMILTON = PopulatedPlace(
        name="Hamilton",
        abbreviations=PlaceAbbreviations(
            three_letter="HAM",
            five_letter="HAMIL",
            seven_letter="HAMILTO",
            fourteen_letter="HAMILTON"
        ),
        latitude=40.36720181510202,
        longitude=-107.6131323772085,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    HAMLET = PopulatedPlace(
        name="Hamlet",
        abbreviations=PlaceAbbreviations(
            three_letter="HAM",
            five_letter="HAMLE",
            seven_letter="HAMLET",
            fourteen_letter="HAMLET"
        ),
        latitude=38.154733053406346,
        longitude=-104.09386052815267,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    HANNA = PopulatedPlace(
        name="Hanna",
        abbreviations=PlaceAbbreviations(
            three_letter="HAN",
            five_letter="HANNA",
            seven_letter="HANNA",
            fourteen_letter="HANNA"
        ),
        latitude=37.67945363405846,
        longitude=-106.45893781716876,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    HAPPY_CANYON = PopulatedPlace(
        name="Happy Canyon",
        abbreviations=PlaceAbbreviations(
            three_letter="HAP",
            five_letter="HAPPY",
            seven_letter="HAPPY C",
            fourteen_letter="HAPPY CANYON"
        ),
        latitude=39.4349957847906,
        longitude=-104.87054474565917,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    HAPPY_CANYON_RANCHES = PopulatedPlace(
        name="Happy Canyon Ranches",
        abbreviations=PlaceAbbreviations(
            three_letter="HAP",
            five_letter="HAPPY",
            seven_letter="HAPPY C",
            fourteen_letter="HAPPY CANYON R"
        ),
        latitude=39.44160638612658,
        longitude=-104.86391004499058,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    HAPPY_VALLEY_GARDENS = PopulatedPlace(
        name="Happy Valley Gardens",
        abbreviations=PlaceAbbreviations(
            three_letter="HAP",
            five_letter="HAPPY",
            seven_letter="HAPPY V",
            fourteen_letter="HAPPY VALLEY G"
        ),
        latitude=39.77667311583468,
        longitude=-105.10445453912348,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    HARBOR_POINTE = PopulatedPlace(
        name="Harbor Pointe",
        abbreviations=PlaceAbbreviations(
            three_letter="HAR",
            five_letter="HARBO",
            seven_letter="HARBOR ",
            fourteen_letter="HARBOR POINTE"
        ),
        latitude=39.63667311650738,
        longitude=-104.8250100583922,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    HARDIN = PopulatedPlace(
        name="Hardin",
        abbreviations=PlaceAbbreviations(
            three_letter="HAR",
            five_letter="HARDI",
            seven_letter="HARDIN",
            fourteen_letter="HARDIN"
        ),
        latitude=40.351098742250144,
        longitude=-104.42552024952681,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    HARDMAN = PopulatedPlace(
        name="Hardman",
        abbreviations=PlaceAbbreviations(
            three_letter="HAR",
            five_letter="HARDM",
            seven_letter="HARDMAN",
            fourteen_letter="HARDMAN"
        ),
        latitude=40.36582250976119,
        longitude=-104.91526226605504,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HARMONY = PopulatedPlace(
        name="Harmony",
        abbreviations=PlaceAbbreviations(
            three_letter="HAR",
            five_letter="HARMO",
            seven_letter="HARMONY",
            fourteen_letter="HARMONY"
        ),
        latitude=40.52332242217494,
        longitude=-105.04359911612681,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HARNEY = PopulatedPlace(
        name="Harney",
        abbreviations=PlaceAbbreviations(
            three_letter="HAR",
            five_letter="HARNE",
            seven_letter="HARNEY",
            fourteen_letter="HARNEY"
        ),
        latitude=40.15137917888171,
        longitude=-104.9408203455946,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    HARRIS_PARK = PopulatedPlace(
        name="Harris Park",
        abbreviations=PlaceAbbreviations(
            three_letter="HAR",
            five_letter="HARRI",
            seven_letter="HARRIS ",
            fourteen_letter="HARRIS PARK"
        ),
        latitude=39.831950828460606,
        longitude=-105.03834342913228,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    HARRIS_PARK = PopulatedPlace(
        name="Harris Park",
        abbreviations=PlaceAbbreviations(
            three_letter="HAR",
            five_letter="HARRI",
            seven_letter="HARRIS ",
            fourteen_letter="HARRIS PARK"
        ),
        latitude=39.5116618531988,
        longitude=-105.49112009780748,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    """
    HARRY_PARKER_PLACE = PopulatedPlace(
        name="Harry Parker Place",
        abbreviations=PlaceAbbreviations(
            three_letter="HAR",
            five_letter="HARRY",
            seven_letter="HARRY P",
            fourteen_letter="HARRY PARKER P"
        ),
        latitude=39.0522152539981,
        longitude=-107.4692316884267,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.ASPEN
    )
    HARTMAN = PopulatedPlace(
        name="Hartman",
        abbreviations=PlaceAbbreviations(
            three_letter="HAR",
            five_letter="HARTM",
            seven_letter="HARTMAN",
            fourteen_letter="HARTMAN"
        ),
        latitude=38.12029426615311,
        longitude=-102.21991968173444,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    HARTNER = PopulatedPlace(
        name="Hartner",
        abbreviations=PlaceAbbreviations(
            three_letter="HAR",
            five_letter="HARTN",
            seven_letter="HARTNER",
            fourteen_letter="HARTNER"
        ),
        latitude=37.39251222802284,
        longitude=-105.91003236615944,
        counties=[Counties.ALAMOSA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    HARTSEL = PopulatedPlace(
        name="Hartsel",
        abbreviations=PlaceAbbreviations(
            three_letter="HAR",
            five_letter="HARTS",
            seven_letter="HARTSEL",
            fourteen_letter="HARTSEL"
        ),
        latitude=39.02166566491837,
        longitude=-105.79585211156592,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    HASWELL = PopulatedPlace(
        name="Haswell",
        abbreviations=PlaceAbbreviations(
            three_letter="HAS",
            five_letter="HASWE",
            seven_letter="HASWELL",
            fourteen_letter="HASWELL"
        ),
        latitude=38.452231856848755,
        longitude=-103.16299354015649,
        counties=[Counties.KIOWA],
        nearest_airport=Airports.PUEBLO
    )
    HAVANA_VILLAGE = PopulatedPlace(
        name="Havana Village",
        abbreviations=PlaceAbbreviations(
            three_letter="HAV",
            five_letter="HAVAN",
            seven_letter="HAVANA ",
            fourteen_letter="HAVANA VILLAGE"
        ),
        latitude=39.700006422685306,
        longitude=-104.85973227345494,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    HAVER = PopulatedPlace(
        name="Haver",
        abbreviations=PlaceAbbreviations(
            three_letter="HAV",
            five_letter="HAVER",
            seven_letter="HAVER",
            fourteen_letter="HAVER"
        ),
        latitude=38.965000547801765,
        longitude=-105.92752213444828,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    HAWKINS = PopulatedPlace(
        name="Hawkins",
        abbreviations=PlaceAbbreviations(
            three_letter="HAW",
            five_letter="HAWKI",
            seven_letter="HAWKINS",
            fourteen_letter="HAWKINS"
        ),
        latitude=38.49389977718204,
        longitude=-102.93243238939039,
        counties=[Counties.KIOWA],
        nearest_airport=Airports.PUEBLO
    )
    HAWLEY = PopulatedPlace(
        name="Hawley",
        abbreviations=PlaceAbbreviations(
            three_letter="HAW",
            five_letter="HAWLE",
            seven_letter="HAWLEY",
            fourteen_letter="HAWLEY"
        ),
        latitude=37.98279315182265,
        longitude=-103.71107062230288,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    HAXTUN = PopulatedPlace(
        name="Haxtun",
        abbreviations=PlaceAbbreviations(
            three_letter="HAX",
            five_letter="HAXTU",
            seven_letter="HAXTUN",
            fourteen_letter="HAXTUN"
        ),
        latitude=40.641108909376555,
        longitude=-102.62686805687667,
        counties=[Counties.PHILLIPS],
        nearest_airport=Airports.DENVER
    )
    HAYBRO = PopulatedPlace(
        name="Haybro",
        abbreviations=PlaceAbbreviations(
            three_letter="HAY",
            five_letter="HAYBR",
            seven_letter="HAYBRO",
            fourteen_letter="HAYBRO"
        ),
        latitude=40.33220785789291,
        longitude=-106.95950522816668,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    HAYDEN = PopulatedPlace(
        name="Hayden",
        abbreviations=PlaceAbbreviations(
            three_letter="HAY",
            five_letter="HAYDE",
            seven_letter="HAYDEN",
            fourteen_letter="HAYDEN"
        ),
        latitude=40.49529335752396,
        longitude=-107.25729871485771,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    HAYS = PopulatedPlace(
        name="Hays",
        abbreviations=PlaceAbbreviations(
            three_letter="HAY",
            five_letter="HAYS",
            seven_letter="HAYS",
            fourteen_letter="HAYS"
        ),
        latitude=38.07306957120477,
        longitude=-103.61912170907078,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    HAZELTINE = PopulatedPlace(
        name="Hazeltine",
        abbreviations=PlaceAbbreviations(
            three_letter="HAZ",
            five_letter="HAZEL",
            seven_letter="HAZELTI",
            fourteen_letter="HAZELTINE"
        ),
        latitude=39.896658447729465,
        longitude=-104.88304160214045,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    HAZELTINE_HEIGHTS = PopulatedPlace(
        name="Hazeltine Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="HAZ",
            five_letter="HAZEL",
            seven_letter="HAZELTI",
            fourteen_letter="HAZELTINE HEIG"
        ),
        latitude=39.88554744602749,
        longitude=-104.88970870234641,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    HEARTSTRONG = PopulatedPlace(
        name="Heartstrong",
        abbreviations=PlaceAbbreviations(
            three_letter="HEA",
            five_letter="HEART",
            seven_letter="HEARTST",
            fourteen_letter="HEARTSTRONG"
        ),
        latitude=39.947495513897366,
        longitude=-102.57688126336609,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    HEATHER_RIDGE = PopulatedPlace(
        name="Heather Ridge",
        abbreviations=PlaceAbbreviations(
            three_letter="HEA",
            five_letter="HEATH",
            seven_letter="HEATHER",
            fourteen_letter="HEATHER RIDGE"
        ),
        latitude=39.67722862038198,
        longitude=-104.84084336653473,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    HEBRON = PopulatedPlace(
        name="Hebron",
        abbreviations=PlaceAbbreviations(
            three_letter="HEB",
            five_letter="HEBRO",
            seven_letter="HEBRON",
            fourteen_letter="HEBRON"
        ),
        latitude=40.5960963318023,
        longitude=-106.40698583680319,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    HEIBERGER = PopulatedPlace(
        name="Heiberger",
        abbreviations=PlaceAbbreviations(
            three_letter="HEI",
            five_letter="HEIBE",
            seven_letter="HEIBERG",
            fourteen_letter="HEIBERGER"
        ),
        latitude=39.268874660803874,
        longitude=-107.80229578650858,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    HENDERSON = PopulatedPlace(
        name="Henderson",
        abbreviations=PlaceAbbreviations(
            three_letter="HEN",
            five_letter="HENDE",
            seven_letter="HENDERS",
            fourteen_letter="HENDERSON"
        ),
        latitude=39.92054695153314,
        longitude=-104.86581850143858,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    HENKEL = PopulatedPlace(
        name="Henkel",
        abbreviations=PlaceAbbreviations(
            three_letter="HEN",
            five_letter="HENKE",
            seven_letter="HENKEL",
            fourteen_letter="HENKEL"
        ),
        latitude=38.52000537170551,
        longitude=-104.62637108921956,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.PUEBLO
    )
    HENRY = PopulatedPlace(
        name="Henry",
        abbreviations=PlaceAbbreviations(
            three_letter="HEN",
            five_letter="HENRY",
            seven_letter="HENRY",
            fourteen_letter="HENRY"
        ),
        latitude=37.398345428551124,
        longitude=-105.90697676648341,
        counties=[Counties.ALAMOSA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    HENSON = PopulatedPlace(
        name="Henson",
        abbreviations=PlaceAbbreviations(
            three_letter="HEN",
            five_letter="HENSO",
            seven_letter="HENSON",
            fourteen_letter="HENSON"
        ),
        latitude=38.020835721532194,
        longitude=-107.37701165555694,
        counties=[Counties.HINSDALE],
        nearest_airport=Airports.TELLURIDE
    )
    HEREFORD = PopulatedPlace(
        name="Hereford",
        abbreviations=PlaceAbbreviations(
            three_letter="HER",
            five_letter="HEREF",
            seven_letter="HEREFOR",
            fourteen_letter="HEREFORD"
        ),
        latitude=40.97499013597155,
        longitude=-104.305796998863,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HERITAGE_DELLS = PopulatedPlace(
        name="Heritage Dells",
        abbreviations=PlaceAbbreviations(
            three_letter="HER",
            five_letter="HERIT",
            seven_letter="HERITAG",
            fourteen_letter="HERITAGE DELLS"
        ),
        latitude=39.71945080102694,
        longitude=-105.21251015736505,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    HERITAGE_HILLS = PopulatedPlace(
        name="Heritage Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="HER",
            five_letter="HERIT",
            seven_letter="HERITAG",
            fourteen_letter="HERITAGE HILLS"
        ),
        latitude=39.54332829980217,
        longitude=-104.87887756045558,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    HERMOSA = PopulatedPlace(
        name="Hermosa",
        abbreviations=PlaceAbbreviations(
            three_letter="HER",
            five_letter="HERMO",
            seven_letter="HERMOSA",
            fourteen_letter="HERMOSA"
        ),
        latitude=37.41528410919716,
        longitude=-107.8353546926694,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    HERZMAN_MESA = PopulatedPlace(
        name="Herzman Mesa",
        abbreviations=PlaceAbbreviations(
            three_letter="HER",
            five_letter="HERZM",
            seven_letter="HERZMAN",
            fourteen_letter="HERZMAN MESA"
        ),
        latitude=39.61055007933163,
        longitude=-105.3102802677243,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    HESPERUS = PopulatedPlace(
        name="Hesperus",
        abbreviations=PlaceAbbreviations(
            three_letter="HES",
            five_letter="HESPE",
            seven_letter="HESPERU",
            fourteen_letter="HESPERUS"
        ),
        latitude=37.286117277964706,
        longitude=-108.03952702437903,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    HI_LAND_ACRES = PopulatedPlace(
        name="Hi-Land Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="HI-",
            five_letter="HI-LA",
            seven_letter="HI-LAND",
            fourteen_letter="HI-LAND ACRES"
        ),
        latitude=39.988323860684886,
        longitude=-104.877485211291,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    HIAWATHA = PopulatedPlace(
        name="Hiawatha",
        abbreviations=PlaceAbbreviations(
            three_letter="HIA",
            five_letter="HIAWA",
            seven_letter="HIAWATH",
            fourteen_letter="HIAWATHA"
        ),
        latitude=40.98830181620127,
        longitude=-108.62039677898548,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    HIDDEN_CREEK_PARK = PopulatedPlace(
        name="Hidden Creek Park",
        abbreviations=PlaceAbbreviations(
            three_letter="HID",
            five_letter="HIDDE",
            seven_letter="HIDDEN ",
            fourteen_letter="HIDDEN CREEK P"
        ),
        latitude=39.83806202908863,
        longitude=-105.04278793293372,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    """
    HIDDEN_LAKE = PopulatedPlace(
        name="Hidden Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="HID",
            five_letter="HIDDE",
            seven_letter="HIDDEN ",
            fourteen_letter="HIDDEN LAKE"
        ),
        latitude=40.10999213552731,
        longitude=-105.47861866530832,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HIDDEN_LAKE = PopulatedPlace(
        name="Hidden Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="HID",
            five_letter="HIDDE",
            seven_letter="HIDDEN ",
            fourteen_letter="HIDDEN LAKE"
        ),
        latitude=39.81639532708937,
        longitude=-105.0300101256525,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    HIDDEN_VALLEY = PopulatedPlace(
        name="Hidden Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="HID",
            five_letter="HIDDE",
            seven_letter="HIDDEN ",
            fourteen_letter="HIDDEN VALLEY"
        ),
        latitude=39.69471648861429,
        longitude=-105.33916928416778,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    HIDDEN_VILAGE = PopulatedPlace(
        name="Hidden Vilage",
        abbreviations=PlaceAbbreviations(
            three_letter="HID",
            five_letter="HIDDE",
            seven_letter="HIDDEN ",
            fourteen_letter="HIDDEN VILAGE"
        ),
        latitude=39.46340639987653,
        longitude=-104.70741001183512,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    HIDEAWAY_PARK = PopulatedPlace(
        name="Hideaway Park",
        abbreviations=PlaceAbbreviations(
            three_letter="HID",
            five_letter="HIDEA",
            seven_letter="HIDEAWA",
            fourteen_letter="HIDEAWAY PARK"
        ),
        latitude=39.918048886705265,
        longitude=-105.78557371205255,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HIGBEE = PopulatedPlace(
        name="Higbee",
        abbreviations=PlaceAbbreviations(
            three_letter="HIG",
            five_letter="HIGBE",
            seven_letter="HIGBEE",
            fourteen_letter="HIGBEE"
        ),
        latitude=37.77640673699307,
        longitude=-103.45939474146348,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    HIGHLAND = PopulatedPlace(
        name="Highland",
        abbreviations=PlaceAbbreviations(
            three_letter="HIG",
            five_letter="HIGHL",
            seven_letter="HIGHLAN",
            fourteen_letter="HIGHLAND"
        ),
        latitude=40.23887998063526,
        longitude=-105.0833254890062,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HIGHLAND_GARDENS = PopulatedPlace(
        name="Highland Gardens",
        abbreviations=PlaceAbbreviations(
            three_letter="HIG",
            five_letter="HIGHL",
            seven_letter="HIGHLAN",
            fourteen_letter="HIGHLAND GARDE"
        ),
        latitude=39.76750641775266,
        longitude=-105.06278792829954,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    HIGHLAND_LAKE = PopulatedPlace(
        name="Highland Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="HIG",
            five_letter="HIGHL",
            seven_letter="HIGHLAN",
            fourteen_letter="HIGHLAND LAKE"
        ),
        latitude=40.24776848696871,
        longitude=-105.01443397463294,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    HIGHLAND_PARK = PopulatedPlace(
        name="Highland Park",
        abbreviations=PlaceAbbreviations(
            three_letter="HIG",
            five_letter="HIGHL",
            seven_letter="HIGHLAN",
            fourteen_letter="HIGHLAND PARK"
        ),
        latitude=39.76083972020899,
        longitude=-105.01806571779969,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    HIGHLAND_PARK = PopulatedPlace(
        name="Highland Park",
        abbreviations=PlaceAbbreviations(
            three_letter="HIG",
            five_letter="HIGHL",
            seven_letter="HIGHLAN",
            fourteen_letter="HIGHLAND PARK"
        ),
        latitude=39.091931688897546,
        longitude=-108.48149041326457,
        counties=[Counties.MESA],
        nearest_airport=Airports.DENVER
    )
    HIGHLAND_PARK = PopulatedPlace(
        name="Highland Park",
        abbreviations=PlaceAbbreviations(
            three_letter="HIG",
            five_letter="HIGHL",
            seven_letter="HIGHLAN",
            fourteen_letter="HIGHLAND PARK"
        ),
        latitude=39.498883948640184,
        longitude=-105.52917690501891,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    HIGHLAND_PARK = PopulatedPlace(
        name="Highland Park",
        abbreviations=PlaceAbbreviations(
            three_letter="HIG",
            five_letter="HIGHL",
            seven_letter="HIGHLAN",
            fourteen_letter="HIGHLAND PARK"
        ),
        latitude=39.72139532561056,
        longitude=-104.86001007655824,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    """
    HIGHLANDS_RANCH = PopulatedPlace(
        name="Highlands Ranch",
        abbreviations=PlaceAbbreviations(
            three_letter="HIG",
            five_letter="HIGHL",
            seven_letter="HIGHLAN",
            fourteen_letter="HIGHLANDS RANC"
        ),
        latitude=39.55388349459594,
        longitude=-104.96943648260083,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    HIGHPOINT = PopulatedPlace(
        name="Highpoint",
        abbreviations=PlaceAbbreviations(
            three_letter="HIG",
            five_letter="HIGHP",
            seven_letter="HIGHPOI",
            fourteen_letter="HIGHPOINT"
        ),
        latitude=39.64583972158965,
        longitude=-104.76473224583503,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    """
    HILLCREST = PopulatedPlace(
        name="Hillcrest",
        abbreviations=PlaceAbbreviations(
            three_letter="HIL",
            five_letter="HILLC",
            seven_letter="HILLCRE",
            fourteen_letter="HILLCREST"
        ),
        latitude=39.7419508311545,
        longitude=-104.81584336895867,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    HILLCREST = PopulatedPlace(
        name="Hillcrest",
        abbreviations=PlaceAbbreviations(
            three_letter="HIL",
            five_letter="HILLC",
            seven_letter="HILLCRE",
            fourteen_letter="HILLCREST"
        ),
        latitude=39.881395337483525,
        longitude=-105.0022323279104,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    """
    HILLCREST_HEIGHTS = PopulatedPlace(
        name="Hillcrest Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="HIL",
            five_letter="HILLC",
            seven_letter="HILLCRE",
            fourteen_letter="HILLCREST HEIG"
        ),
        latitude=39.77889531748531,
        longitude=-105.08612123571493,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    HILLCREST_VILLAGE = PopulatedPlace(
        name="Hillcrest Village",
        abbreviations=PlaceAbbreviations(
            three_letter="HIL",
            five_letter="HILLC",
            seven_letter="HILLCRE",
            fourteen_letter="HILLCREST VILL"
        ),
        latitude=39.74611753186019,
        longitude=-104.82112117067891,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    HILLROSE = PopulatedPlace(
        name="Hillrose",
        abbreviations=PlaceAbbreviations(
            three_letter="HIL",
            five_letter="HILLR",
            seven_letter="HILLROS",
            fourteen_letter="HILLROSE"
        ),
        latitude=40.325819502574404,
        longitude=-103.52189883351787,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    HILLSBORO = PopulatedPlace(
        name="Hillsboro",
        abbreviations=PlaceAbbreviations(
            three_letter="HIL",
            five_letter="HILLS",
            seven_letter="HILLSBO",
            fourteen_letter="HILLSBORO"
        ),
        latitude=40.33276680916896,
        longitude=-104.86442715030239,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    HILLSIDE = PopulatedPlace(
        name="Hillside",
        abbreviations=PlaceAbbreviations(
            three_letter="HIL",
            five_letter="HILLS",
            seven_letter="HILLSID",
            fourteen_letter="HILLSIDE"
        ),
        latitude=38.2652825711192,
        longitude=-105.61167998812283,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    HILLSIDE = PopulatedPlace(
        name="Hillside",
        abbreviations=PlaceAbbreviations(
            three_letter="HIL",
            five_letter="HILLS",
            seven_letter="HILLSID",
            fourteen_letter="HILLSIDE"
        ),
        latitude=39.733617527049944,
        longitude=-104.86695447950592,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    """
    HILLSIDE_MANOR = PopulatedPlace(
        name="Hillside Manor",
        abbreviations=PlaceAbbreviations(
            three_letter="HIL",
            five_letter="HILLS",
            seven_letter="HILLSID",
            fourteen_letter="HILLSIDE MANOR"
        ),
        latitude=39.62056199910046,
        longitude=-105.03973230540993,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    HILLTOP = PopulatedPlace(
        name="Hilltop",
        abbreviations=PlaceAbbreviations(
            three_letter="HIL",
            five_letter="HILLT",
            seven_letter="HILLTOP",
            fourteen_letter="HILLTOP"
        ),
        latitude=39.45166179994641,
        longitude=-104.68137140368708,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    HILTON = PopulatedPlace(
        name="Hilton",
        abbreviations=PlaceAbbreviations(
            three_letter="HIL",
            five_letter="HILTO",
            seven_letter="HILTON",
            fourteen_letter="HILTON"
        ),
        latitude=38.07029120626396,
        longitude=-103.06104647752517,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    HIWAN_HILLS = PopulatedPlace(
        name="Hiwan Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="HIW",
            five_letter="HIWAN",
            seven_letter="HIWAN H",
            fourteen_letter="HIWAN HILLS"
        ),
        latitude=39.64027228167538,
        longitude=-105.33000277529555,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    HOBSON = PopulatedPlace(
        name="Hobson",
        abbreviations=PlaceAbbreviations(
            three_letter="HOB",
            five_letter="HOBSO",
            seven_letter="HOBSON",
            fourteen_letter="HOBSON"
        ),
        latitude=38.34084132646893,
        longitude=-104.93443764122782,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    HOLIDAY_HILLS_VILLAGE = PopulatedPlace(
        name="Holiday Hills Village",
        abbreviations=PlaceAbbreviations(
            three_letter="HOL",
            five_letter="HOLID",
            seven_letter="HOLIDAY",
            fourteen_letter="HOLIDAY HILLS "
        ),
        latitude=39.86611753509396,
        longitude=-105.00862122795775,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    HOLLY = PopulatedPlace(
        name="Holly",
        abbreviations=PlaceAbbreviations(
            three_letter="HOL",
            five_letter="HOLLY",
            seven_letter="HOLLY",
            fourteen_letter="HOLLY"
        ),
        latitude=38.05224006183107,
        longitude=-102.12269425137288,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    HOLLY_HILLS = PopulatedPlace(
        name="Holly Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="HOL",
            five_letter="HOLLY",
            seven_letter="HOLLY H",
            fourteen_letter="HOLLY HILLS"
        ),
        latitude=39.66757641416103,
        longitude=-104.91798008391288,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    HOLLYWOOD = PopulatedPlace(
        name="Hollywood",
        abbreviations=PlaceAbbreviations(
            three_letter="HOL",
            five_letter="HOLLY",
            seven_letter="HOLLYWO",
            fourteen_letter="HOLLYWOOD"
        ),
        latitude=38.70944016563766,
        longitude=-105.13332382586827,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    HOLYOKE = PopulatedPlace(
        name="Holyoke",
        abbreviations=PlaceAbbreviations(
            three_letter="HOL",
            five_letter="HOLYO",
            seven_letter="HOLYOKE",
            fourteen_letter="HOLYOKE"
        ),
        latitude=40.584443624000585,
        longitude=-102.30241987136469,
        counties=[Counties.PHILLIPS],
        nearest_airport=Airports.DENVER
    )
    HOMELAKE = PopulatedPlace(
        name="Homelake",
        abbreviations=PlaceAbbreviations(
            three_letter="HOM",
            five_letter="HOMEL",
            seven_letter="HOMELAK",
            fourteen_letter="HOMELAKE"
        ),
        latitude=37.57556434192588,
        longitude=-106.09698182623788,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    HOMESTEAD = PopulatedPlace(
        name="Homestead",
        abbreviations=PlaceAbbreviations(
            three_letter="HOM",
            five_letter="HOMES",
            seven_letter="HOMESTE",
            fourteen_letter="HOMESTEAD"
        ),
        latitude=39.56389527811535,
        longitude=-105.22889904296807,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    HOMESTEAD_HEIGHTS = PopulatedPlace(
        name="Homestead Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="HOM",
            five_letter="HOMES",
            seven_letter="HOMESTE",
            fourteen_letter="HOMESTEAD HEIG"
        ),
        latitude=39.861117534315554,
        longitude=-105.01389902788134,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    HOMESTEAD_HILLS = PopulatedPlace(
        name="Homestead Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="HOM",
            five_letter="HOMES",
            seven_letter="HOMESTE",
            fourteen_letter="HOMESTEAD HILL"
        ),
        latitude=39.531395307819025,
        longitude=-104.72973222407563,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    HOMEWOOD_PARK = PopulatedPlace(
        name="Homewood Park",
        abbreviations=PlaceAbbreviations(
            three_letter="HOM",
            five_letter="HOMEW",
            seven_letter="HOMEWOO",
            fourteen_letter="HOMEWOOD PARK"
        ),
        latitude=39.54277237771089,
        longitude=-105.19777743366757,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    HOOKS = PopulatedPlace(
        name="Hooks",
        abbreviations=PlaceAbbreviations(
            three_letter="HOO",
            five_letter="HOOKS",
            seven_letter="HOOKS",
            fourteen_letter="HOOKS"
        ),
        latitude=39.3741568236793,
        longitude=-107.08866964131244,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.ASPEN
    )
    HOOPER = PopulatedPlace(
        name="Hooper",
        abbreviations=PlaceAbbreviations(
            three_letter="HOO",
            five_letter="HOOPE",
            seven_letter="HOOPER",
            fourteen_letter="HOOPER"
        ),
        latitude=37.74278368036585,
        longitude=-105.8753087937423,
        counties=[Counties.ALAMOSA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    HOOVERS_CORNER = PopulatedPlace(
        name="Hoovers Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="HOO",
            five_letter="HOOVE",
            seven_letter="HOOVERS",
            fourteen_letter="HOOVERS CORNER"
        ),
        latitude=38.60693595500527,
        longitude=-108.05896886771285,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    HORSETOOTH_HEIGHTS = PopulatedPlace(
        name="Horsetooth Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="HOR",
            five_letter="HORSE",
            seven_letter="HORSETO",
            fourteen_letter="HORSETOOTH HEI"
        ),
        latitude=40.50443371141483,
        longitude=-105.15415893824144,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HOT_SULPHUR_SPRINGS = PopulatedPlace(
        name="Hot Sulphur Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="HOT",
            five_letter="HOT S",
            seven_letter="HOT SUL",
            fourteen_letter="HOT SULPHUR SP"
        ),
        latitude=40.07304748573205,
        longitude=-106.10280950291315,
        counties=[Counties.GRAND],
        nearest_airport=Airports.EAGLE
    )
    HOTCHKISS = PopulatedPlace(
        name="Hotchkiss",
        abbreviations=PlaceAbbreviations(
            three_letter="HOT",
            five_letter="HOTCH",
            seven_letter="HOTCHKI",
            fourteen_letter="HOTCHKISS"
        ),
        latitude=38.79971310347622,
        longitude=-107.71951381423827,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    HOUGHTON = PopulatedPlace(
        name="Houghton",
        abbreviations=PlaceAbbreviations(
            three_letter="HOU",
            five_letter="HOUGH",
            seven_letter="HOUGHTO",
            fourteen_letter="HOUGHTON"
        ),
        latitude=37.58946397275122,
        longitude=-104.0433063596069,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    HOUSER_COW_CAMP = PopulatedPlace(
        name="Houser Cow Camp",
        abbreviations=PlaceAbbreviations(
            three_letter="HOU",
            five_letter="HOUSE",
            seven_letter="HOUSER ",
            fourteen_letter="HOUSER COW CAM"
        ),
        latitude=38.32943910105655,
        longitude=-108.30564778983432,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    HOUSTON = PopulatedPlace(
        name="Houston",
        abbreviations=PlaceAbbreviations(
            three_letter="HOU",
            five_letter="HOUST",
            seven_letter="HOUSTON",
            fourteen_letter="HOUSTON"
        ),
        latitude=40.25471130242636,
        longitude=-104.80692542751876,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HOWARDSVILLE = PopulatedPlace(
        name="Howardsville",
        abbreviations=PlaceAbbreviations(
            three_letter="HOW",
            five_letter="HOWAR",
            seven_letter="HOWARDS",
            fourteen_letter="HOWARDSVILLE"
        ),
        latitude=37.835558381836336,
        longitude=-107.59423718387796,
        counties=[Counties.SAN_JUAN],
        nearest_airport=Airports.TELLURIDE
    )
    HOYT = PopulatedPlace(
        name="Hoyt",
        abbreviations=PlaceAbbreviations(
            three_letter="HOY",
            five_letter="HOYT",
            seven_letter="HOYT",
            fourteen_letter="HOYT"
        ),
        latitude=40.01554632067365,
        longitude=-104.07496022789974,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    HUDSON = PopulatedPlace(
        name="Hudson",
        abbreviations=PlaceAbbreviations(
            three_letter="HUD",
            five_letter="HUDSO",
            seven_letter="HUDSON",
            fourteen_letter="HUDSON"
        ),
        latitude=40.07360058949382,
        longitude=-104.64302996707443,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    HUFF = PopulatedPlace(
        name="Huff",
        abbreviations=PlaceAbbreviations(
            three_letter="HUF",
            five_letter="HUFF",
            seven_letter="HUFF",
            fourteen_letter="HUFF"
        ),
        latitude=38.75693476120341,
        longitude=-108.25619912670464,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    HUGO = PopulatedPlace(
        name="Hugo",
        abbreviations=PlaceAbbreviations(
            three_letter="HUG",
            five_letter="HUGO",
            seven_letter="HUGO",
            fourteen_letter="HUGO"
        ),
        latitude=39.136106837064915,
        longitude=-103.46995438552602,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    HUNTINGTON_HEIGHTS = PopulatedPlace(
        name="Huntington Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="HUN",
            five_letter="HUNTI",
            seven_letter="HUNTING",
            fourteen_letter="HUNTINGTON HEI"
        ),
        latitude=39.82445082347857,
        longitude=-105.09306574196887,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    HURLEY = PopulatedPlace(
        name="Hurley",
        abbreviations=PlaceAbbreviations(
            three_letter="HUR",
            five_letter="HURLE",
            seven_letter="HURLEY",
            fourteen_letter="HURLEY"
        ),
        latitude=40.27415407845024,
        longitude=-103.76162788374836,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    HURRICH = PopulatedPlace(
        name="Hurrich",
        abbreviations=PlaceAbbreviations(
            three_letter="HUR",
            five_letter="HURRI",
            seven_letter="HURRICH",
            fourteen_letter="HURRICH"
        ),
        latitude=40.53109834067624,
        longitude=-104.79386775729739,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    HUTCHINSON_HEIGHTS = PopulatedPlace(
        name="Hutchinson Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="HUT",
            five_letter="HUTCH",
            seven_letter="HUTCHIN",
            fourteen_letter="HUTCHINSON HEI"
        ),
        latitude=39.66278422238253,
        longitude=-104.78417675177525,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    HYDE = PopulatedPlace(
        name="Hyde",
        abbreviations=PlaceAbbreviations(
            three_letter="HYD",
            five_letter="HYDE",
            seven_letter="HYDE",
            fourteen_letter="HYDE"
        ),
        latitude=40.13582482330588,
        longitude=-102.8327218461522,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    HYGIENE = PopulatedPlace(
        name="Hygiene",
        abbreviations=PlaceAbbreviations(
            three_letter="HYG",
            five_letter="HYGIE",
            seven_letter="HYGIENE",
            fourteen_letter="HYGIENE"
        ),
        latitude=40.1886026671516,
        longitude=-105.18082940608889,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    IDAHO_CREEK = PopulatedPlace(
        name="Idaho Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="IDA",
            five_letter="IDAHO",
            seven_letter="IDAHO C",
            fourteen_letter="IDAHO CREEK"
        ),
        latitude=40.12221296946717,
        longitude=-105.01304565890416,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    IDAHO_SPRINGS = PopulatedPlace(
        name="Idaho Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="IDA",
            five_letter="IDAHO",
            seven_letter="IDAHO S",
            fourteen_letter="IDAHO SPRINGS"
        ),
        latitude=39.74249448316948,
        longitude=-105.5136184292511,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.DENVER
    )
    IDYLWILDE = PopulatedPlace(
        name="Idylwilde",
        abbreviations=PlaceAbbreviations(
            three_letter="IDY",
            five_letter="IDYLW",
            seven_letter="IDYLWIL",
            fourteen_letter="IDYLWILDE"
        ),
        latitude=40.700820501447595,
        longitude=-105.65473327794524,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    IGNACIO = PopulatedPlace(
        name="Ignacio",
        abbreviations=PlaceAbbreviations(
            three_letter="IGN",
            five_letter="IGNAC",
            seven_letter="IGNACIO",
            fourteen_letter="IGNACIO"
        ),
        latitude=37.115009580496064,
        longitude=-107.63312341906595,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    ILES_GROVE = PopulatedPlace(
        name="Iles Grove",
        abbreviations=PlaceAbbreviations(
            three_letter="ILE",
            five_letter="ILES ",
            seven_letter="ILES GR",
            fourteen_letter="ILES GROVE"
        ),
        latitude=40.33525730495046,
        longitude=-107.68730119024531,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    ILIFF = PopulatedPlace(
        name="Iliff",
        abbreviations=PlaceAbbreviations(
            three_letter="ILI",
            five_letter="ILIFF",
            seven_letter="ILIFF",
            fourteen_letter="ILIFF"
        ),
        latitude=40.75916269480257,
        longitude=-103.06659917719702,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    ILIUM = PopulatedPlace(
        name="Ilium",
        abbreviations=PlaceAbbreviations(
            three_letter="ILI",
            five_letter="ILIUM",
            seven_letter="ILIUM",
            fourteen_letter="ILIUM"
        ),
        latitude=37.92972177619674,
        longitude=-107.89785365893687,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    INDIAN_HILLS = PopulatedPlace(
        name="Indian Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="IND",
            five_letter="INDIA",
            seven_letter="INDIAN ",
            fourteen_letter="INDIAN HILLS"
        ),
        latitude=39.6166609847196,
        longitude=-105.23722255121805,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    INDIAN_MEADOWS = PopulatedPlace(
        name="Indian Meadows",
        abbreviations=PlaceAbbreviations(
            three_letter="IND",
            five_letter="INDIA",
            seven_letter="INDIAN ",
            fourteen_letter="INDIAN MEADOWS"
        ),
        latitude=40.70054310907415,
        longitude=-105.5519505539275,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    INDIAN_SPRINGS_VILLAGE = PopulatedPlace(
        name="Indian Springs Village",
        abbreviations=PlaceAbbreviations(
            three_letter="IND",
            five_letter="INDIA",
            seven_letter="INDIAN ",
            fourteen_letter="INDIAN SPRINGS"
        ),
        latitude=39.43193975398367,
        longitude=-105.32056024917091,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    INDIANS_HILLS = PopulatedPlace(
        name="Indians Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="IND",
            five_letter="INDIA",
            seven_letter="INDIANS",
            fourteen_letter="INDIANS HILLS"
        ),
        latitude=39.632772085384545,
        longitude=-105.25972315809423,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    INSMONT = PopulatedPlace(
        name="Insmont",
        abbreviations=PlaceAbbreviations(
            three_letter="INS",
            five_letter="INSMO",
            seven_letter="INSMONT",
            fourteen_letter="INSMONT"
        ),
        latitude=39.3919400388931,
        longitude=-105.4530646748999,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    """
    INVERNESS = PopulatedPlace(
        name="Inverness",
        abbreviations=PlaceAbbreviations(
            three_letter="INV",
            five_letter="INVER",
            seven_letter="INVERNE",
            fourteen_letter="INVERNESS"
        ),
        latitude=39.57738640534245,
        longitude=-104.86136006027567,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    INVERNESS = PopulatedPlace(
        name="Inverness",
        abbreviations=PlaceAbbreviations(
            three_letter="INV",
            five_letter="INVER",
            seven_letter="INVERNE",
            fourteen_letter="INVERNESS"
        ),
        latitude=39.56230940308899,
        longitude=-104.86289105901437,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    """
    IRIS = PopulatedPlace(
        name="Iris",
        abbreviations=PlaceAbbreviations(
            three_letter="IRI",
            five_letter="IRIS",
            seven_letter="IRIS",
            fourteen_letter="IRIS"
        ),
        latitude=38.416109311800255,
        longitude=-106.82893897695209,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    IRONDALE = PopulatedPlace(
        name="Irondale",
        abbreviations=PlaceAbbreviations(
            three_letter="IRO",
            five_letter="IROND",
            seven_letter="IRONDAL",
            fourteen_letter="IRONDALE"
        ),
        latitude=39.84943674047389,
        longitude=-104.89720920018425,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    IRONTON = PopulatedPlace(
        name="Ironton",
        abbreviations=PlaceAbbreviations(
            three_letter="IRO",
            five_letter="IRONT",
            seven_letter="IRONTON",
            fourteen_letter="IRONTON"
        ),
        latitude=37.932778689657425,
        longitude=-107.6803488120546,
        counties=[Counties.OURAY],
        nearest_airport=Airports.TELLURIDE
    )
    IRWIN = PopulatedPlace(
        name="Irwin",
        abbreviations=PlaceAbbreviations(
            three_letter="IRW",
            five_letter="IRWIN",
            seven_letter="IRWIN",
            fourteen_letter="IRWIN"
        ),
        latitude=38.873609755974485,
        longitude=-107.09700318643911,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    IVYWILD = PopulatedPlace(
        name="Ivywild",
        abbreviations=PlaceAbbreviations(
            three_letter="IVY",
            five_letter="IVYWI",
            seven_letter="IVYWILD",
            fourteen_letter="IVYWILD"
        ),
        latitude=38.81055419939298,
        longitude=-104.83526186867147,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    JACK_SPRINGS = PopulatedPlace(
        name="Jack Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="JAC",
            five_letter="JACK ",
            seven_letter="JACK SP",
            fourteen_letter="JACK SPRINGS"
        ),
        latitude=40.351086131950865,
        longitude=-108.70317321404048,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    JACKSON_FIELD = PopulatedPlace(
        name="Jackson Field",
        abbreviations=PlaceAbbreviations(
            three_letter="JAC",
            five_letter="JACKS",
            seven_letter="JACKSON",
            fourteen_letter="JACKSON FIELD"
        ),
        latitude=40.40693193156278,
        longitude=-104.68636361750373,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    JAMESTOWN = PopulatedPlace(
        name="Jamestown",
        abbreviations=PlaceAbbreviations(
            three_letter="JAM",
            five_letter="JAMES",
            seven_letter="JAMESTO",
            fourteen_letter="JAMESTOWN"
        ),
        latitude=40.11554764251014,
        longitude=-105.38861534487802,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    JANSEN = PopulatedPlace(
        name="Jansen",
        abbreviations=PlaceAbbreviations(
            three_letter="JAN",
            five_letter="JANSE",
            seven_letter="JANSEN",
            fourteen_letter="JANSEN"
        ),
        latitude=37.15716607788352,
        longitude=-104.53815973171129,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    JAROSO = PopulatedPlace(
        name="Jaroso",
        abbreviations=PlaceAbbreviations(
            three_letter="JAR",
            five_letter="JAROS",
            seven_letter="JAROSO",
            fourteen_letter="JAROSO"
        ),
        latitude=37.00280388882504,
        longitude=-105.62418856402519,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    JASPER = PopulatedPlace(
        name="Jasper",
        abbreviations=PlaceAbbreviations(
            three_letter="JAS",
            five_letter="JASPE",
            seven_letter="JASPER",
            fourteen_letter="JASPER"
        ),
        latitude=37.41778919645907,
        longitude=-106.46254709167346,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    JEFFERSON = PopulatedPlace(
        name="Jefferson",
        abbreviations=PlaceAbbreviations(
            three_letter="JEF",
            five_letter="JEFFE",
            seven_letter="JEFFERS",
            fourteen_letter="JEFFERSON"
        ),
        latitude=39.377216413094345,
        longitude=-105.8005764522564,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    JESSICA = PopulatedPlace(
        name="Jessica",
        abbreviations=PlaceAbbreviations(
            three_letter="JES",
            five_letter="JESSI",
            seven_letter="JESSICA",
            fourteen_letter="JESSICA"
        ),
        latitude=40.76054978739376,
        longitude=-103.17188020225814,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    JESSUM = PopulatedPlace(
        name="Jessum",
        abbreviations=PlaceAbbreviations(
            three_letter="JES",
            five_letter="JESSU",
            seven_letter="JESSUM",
            fourteen_letter="JESSUM"
        ),
        latitude=40.138879671106736,
        longitude=-105.02499046381229,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    JOHN_HELD_CORNER = PopulatedPlace(
        name="John Held Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="JOH",
            five_letter="JOHN ",
            seven_letter="JOHN HE",
            fourteen_letter="JOHN HELD CORN"
        ),
        latitude=39.13665291873514,
        longitude=-108.1361986442663,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    JOHNSON = PopulatedPlace(
        name="Johnson",
        abbreviations=PlaceAbbreviations(
            three_letter="JOH",
            five_letter="JOHNS",
            seven_letter="JOHNSON",
            fourteen_letter="JOHNSON"
        ),
        latitude=40.08748910480159,
        longitude=-104.44274402216837,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    JOHNSONS_CORNER = PopulatedPlace(
        name="Johnsons Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="JOH",
            five_letter="JOHNS",
            seven_letter="JOHNSON",
            fourteen_letter="JOHNSONS CORNE"
        ),
        latitude=39.09193168820036,
        longitude=-108.49676881678471,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    JOHNSTOWN = PopulatedPlace(
        name="Johnstown",
        abbreviations=PlaceAbbreviations(
            three_letter="JOH",
            five_letter="JOHNS",
            seven_letter="JOHNSTO",
            fourteen_letter="JOHNSTOWN"
        ),
        latitude=40.336933706200284,
        longitude=-104.91220686131345,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    JUANITA = PopulatedPlace(
        name="Juanita",
        abbreviations=PlaceAbbreviations(
            three_letter="JUA",
            five_letter="JUANI",
            seven_letter="JUANITA",
            fourteen_letter="JUANITA"
        ),
        latitude=37.02723519779062,
        longitude=-107.15060660536847,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    JUANITA_JUNCTION = PopulatedPlace(
        name="Juanita Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="JUA",
            five_letter="JUANI",
            seven_letter="JUANITA",
            fourteen_letter="JUANITA JUNCTI"
        ),
        latitude=38.92471643361989,
        longitude=-107.52812228658951,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    JULESBURG = PopulatedPlace(
        name="Julesburg",
        abbreviations=PlaceAbbreviations(
            three_letter="JUL",
            five_letter="JULES",
            seven_letter="JULESBU",
            fourteen_letter="JULESBURG"
        ),
        latitude=40.98833258373469,
        longitude=-102.26436151096613,
        counties=[Counties.SEDGWICK],
        nearest_airport=Airports.DENVER
    )
    JUNIPER_HOT_SPRINGS = PopulatedPlace(
        name="Juniper Hot Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="JUN",
            five_letter="JUNIP",
            seven_letter="JUNIPER",
            fourteen_letter="JUNIPER HOT SP"
        ),
        latitude=40.46719820211172,
        longitude=-107.95370056549098,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    KAHLER = PopulatedPlace(
        name="Kahler",
        abbreviations=PlaceAbbreviations(
            three_letter="KAH",
            five_letter="KAHLE",
            seven_letter="KAHLER",
            fourteen_letter="KAHLER"
        ),
        latitude=40.32832339867002,
        longitude=-104.99859928039007,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    KANNAH = PopulatedPlace(
        name="Kannah",
        abbreviations=PlaceAbbreviations(
            three_letter="KAN",
            five_letter="KANNA",
            seven_letter="KANNAH",
            fourteen_letter="KANNAH"
        ),
        latitude=38.93915557182851,
        longitude=-108.44704378875457,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    KARL = PopulatedPlace(
        name="Karl",
        abbreviations=PlaceAbbreviations(
            three_letter="KAR",
            five_letter="KARL",
            seven_letter="KARL",
            fourteen_letter="KARL"
        ),
        latitude=38.13751524979324,
        longitude=-102.51992315517845,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    KARVAL = PopulatedPlace(
        name="Karval",
        abbreviations=PlaceAbbreviations(
            three_letter="KAR",
            five_letter="KARVA",
            seven_letter="KARVAL",
            fourteen_letter="KARVAL"
        ),
        latitude=38.733336573883435,
        longitude=-103.53717465797496,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.PUEBLO
    )
    KASSLER = PopulatedPlace(
        name="Kassler",
        abbreviations=PlaceAbbreviations(
            three_letter="KAS",
            five_letter="KASSL",
            seven_letter="KASSLER",
            fourteen_letter="KASSLER"
        ),
        latitude=39.49055047757338,
        longitude=-105.09471900411268,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    KEARNS = PopulatedPlace(
        name="Kearns",
        abbreviations=PlaceAbbreviations(
            three_letter="KEA",
            five_letter="KEARN",
            seven_letter="KEARNS",
            fourteen_letter="KEARNS"
        ),
        latitude=37.13112251234509,
        longitude=-107.16033001761457,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    KEENESBURG = PopulatedPlace(
        name="Keenesburg",
        abbreviations=PlaceAbbreviations(
            three_letter="KEE",
            five_letter="KEENE",
            seven_letter="KEENESB",
            fourteen_letter="KEENESBURG"
        ),
        latitude=40.108322302224224,
        longitude=-104.51996854267901,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    KEESEE = PopulatedPlace(
        name="Keesee",
        abbreviations=PlaceAbbreviations(
            three_letter="KEE",
            five_letter="KEESE",
            seven_letter="KEESEE",
            fourteen_letter="KEESEE"
        ),
        latitude=38.13640303343567,
        longitude=-102.77881771707973,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    KELIM = PopulatedPlace(
        name="Kelim",
        abbreviations=PlaceAbbreviations(
            three_letter="KEL",
            five_letter="KELIM",
            seven_letter="KELIM",
            fourteen_letter="KELIM"
        ),
        latitude=40.40665591283687,
        longitude=-104.95081887857447,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    KELKER = PopulatedPlace(
        name="Kelker",
        abbreviations=PlaceAbbreviations(
            three_letter="KEL",
            five_letter="KELKE",
            seven_letter="KELKER",
            fourteen_letter="KELKER"
        ),
        latitude=38.79583370129217,
        longitude=-104.7813720542531,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    KELLER = PopulatedPlace(
        name="Keller",
        abbreviations=PlaceAbbreviations(
            three_letter="KEL",
            five_letter="KELLE",
            seven_letter="KELLER",
            fourteen_letter="KELLER"
        ),
        latitude=38.06279109942511,
        longitude=-103.1463264966157,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    KELLYTOWN = PopulatedPlace(
        name="Kellytown",
        abbreviations=PlaceAbbreviations(
            three_letter="KEL",
            five_letter="KELLY",
            seven_letter="KELLYTO",
            fourteen_letter="KELLYTOWN"
        ),
        latitude=39.481383982733405,
        longitude=-104.99360458003667,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    KEN_CARYL = PopulatedPlace(
        name="Ken Caryl",
        abbreviations=PlaceAbbreviations(
            three_letter="KEN",
            five_letter="KEN C",
            seven_letter="KEN CAR",
            fourteen_letter="KEN CARYL"
        ),
        latitude=39.57582768828337,
        longitude=-105.11221891797425,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    KEN_CARYL_RANCH_NORTH = PopulatedPlace(
        name="Ken Caryl Ranch North",
        abbreviations=PlaceAbbreviations(
            three_letter="KEN",
            five_letter="KEN C",
            seven_letter="KEN CAR",
            fourteen_letter="KEN CARYL RANC"
        ),
        latitude=39.59528418623944,
        longitude=-105.17251013429387,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    KENYON_CORNER = PopulatedPlace(
        name="Kenyon Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="KEN",
            five_letter="KENYO",
            seven_letter="KENYON ",
            fourteen_letter="KENYON CORNER"
        ),
        latitude=40.63943323557987,
        longitude=-105.07276543621026,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    KEOTA = PopulatedPlace(
        name="Keota",
        abbreviations=PlaceAbbreviations(
            three_letter="KEO",
            five_letter="KEOTA",
            seven_letter="KEOTA",
            fourteen_letter="KEOTA"
        ),
        latitude=40.70277081557964,
        longitude=-104.07523630983098,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    KERNS = PopulatedPlace(
        name="Kerns",
        abbreviations=PlaceAbbreviations(
            three_letter="KER",
            five_letter="KERNS",
            seven_letter="KERNS",
            fourteen_letter="KERNS"
        ),
        latitude=40.50748852694636,
        longitude=-104.94442888976909,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    KERPER_CITY = PopulatedPlace(
        name="Kerper City",
        abbreviations=PlaceAbbreviations(
            three_letter="KER",
            five_letter="KERPE",
            seven_letter="KERPER ",
            fourteen_letter="KERPER CITY"
        ),
        latitude=38.282783438761896,
        longitude=-106.14225280946005,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    KERSEY = PopulatedPlace(
        name="Kersey",
        abbreviations=PlaceAbbreviations(
            three_letter="KER",
            five_letter="KERSE",
            seven_letter="KERSEY",
            fourteen_letter="KERSEY"
        ),
        latitude=40.38748753767152,
        longitude=-104.56163568620377,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    KEYHOLE = PopulatedPlace(
        name="Keyhole",
        abbreviations=PlaceAbbreviations(
            three_letter="KEY",
            five_letter="KEYHO",
            seven_letter="KEYHOLE",
            fourteen_letter="KEYHOLE"
        ),
        latitude=38.69304674876321,
        longitude=-108.30897963134174,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    """
    KEYSTONE = PopulatedPlace(
        name="Keystone",
        abbreviations=PlaceAbbreviations(
            three_letter="KEY",
            five_letter="KEYST",
            seven_letter="KEYSTON",
            fourteen_letter="KEYSTONE"
        ),
        latitude=37.949721678872606,
        longitude=-107.87757505737369,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    KEYSTONE = PopulatedPlace(
        name="Keystone",
        abbreviations=PlaceAbbreviations(
            three_letter="KEY",
            five_letter="KEYST",
            seven_letter="KEYSTON",
            fourteen_letter="KEYSTONE"
        ),
        latitude=40.301097454009835,
        longitude=-106.96311602441756,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.TELLURIDE
    )
    KEYSTONE = PopulatedPlace(
        name="Keystone",
        abbreviations=PlaceAbbreviations(
            three_letter="KEY",
            five_letter="KEYST",
            seven_letter="KEYSTON",
            fourteen_letter="KEYSTONE"
        ),
        latitude=39.59943743055959,
        longitude=-105.98724892041025,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.TELLURIDE
    )
    """
    KIGGIN = PopulatedPlace(
        name="Kiggin",
        abbreviations=PlaceAbbreviations(
            three_letter="KIG",
            five_letter="KIGGI",
            seven_letter="KIGGIN",
            fourteen_letter="KIGGIN"
        ),
        latitude=39.42637812007115,
        longitude=-107.23950778097998,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    KIM = PopulatedPlace(
        name="Kim",
        abbreviations=PlaceAbbreviations(
            three_letter="KIM",
            five_letter="KIM",
            seven_letter="KIM",
            fourteen_letter="KIM"
        ),
        latitude=37.246691664210175,
        longitude=-103.35217056522134,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    KIMBERLY_HILLS = PopulatedPlace(
        name="Kimberly Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="KIM",
            five_letter="KIMBE",
            seven_letter="KIMBERL",
            fourteen_letter="KIMBERLY HILLS"
        ),
        latitude=39.86750643445981,
        longitude=-105.0186212305814,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    KING_CENTER = PopulatedPlace(
        name="King Center",
        abbreviations=PlaceAbbreviations(
            three_letter="KIN",
            five_letter="KING ",
            seven_letter="KING CE",
            fourteen_letter="KING CENTER"
        ),
        latitude=38.176955768464325,
        longitude=-103.90746518667083,
        counties=[Counties.CROWLEY],
        nearest_airport=Airports.PUEBLO
    )
    KINGS_CANYON = PopulatedPlace(
        name="Kings Canyon",
        abbreviations=PlaceAbbreviations(
            three_letter="KIN",
            five_letter="KINGS",
            seven_letter="KINGS C",
            fourteen_letter="KINGS CANYON"
        ),
        latitude=40.92692578853769,
        longitude=-106.22697693757789,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    KINGS_CORNER = PopulatedPlace(
        name="Kings Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="KIN",
            five_letter="KINGS",
            seven_letter="KINGS C",
            fourteen_letter="KINGS CORNER"
        ),
        latitude=40.37832340016257,
        longitude=-105.07332380383804,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    KINGSBOROUGH = PopulatedPlace(
        name="Kingsborough",
        abbreviations=PlaceAbbreviations(
            three_letter="KIN",
            five_letter="KINGS",
            seven_letter="KINGSBO",
            fourteen_letter="KINGSBOROUGH"
        ),
        latitude=39.670839722693756,
        longitude=-104.79917675660914,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    KINIKINIK = PopulatedPlace(
        name="Kinikinik",
        abbreviations=PlaceAbbreviations(
            three_letter="KIN",
            five_letter="KINIK",
            seven_letter="KINIKIN",
            fourteen_letter="KINIKINIK"
        ),
        latitude=40.712486796800476,
        longitude=-105.73807049889263,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    KIOWA = PopulatedPlace(
        name="Kiowa",
        abbreviations=PlaceAbbreviations(
            three_letter="KIO",
            five_letter="KIOWA",
            seven_letter="KIOWA",
            fourteen_letter="KIOWA"
        ),
        latitude=39.34721590041636,
        longitude=-104.46442114162693,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.DENVER
    )
    KIRKGAARD_ACRES = PopulatedPlace(
        name="Kirkgaard Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="KIR",
            five_letter="KIRKG",
            seven_letter="KIRKGAA",
            fourteen_letter="KIRKGAARD ACRE"
        ),
        latitude=39.73472863251732,
        longitude=-104.78667676051606,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    KIRKLAND = PopulatedPlace(
        name="Kirkland",
        abbreviations=PlaceAbbreviations(
            three_letter="KIR",
            five_letter="KIRKL",
            seven_letter="KIRKLAN",
            fourteen_letter="KIRKLAND"
        ),
        latitude=40.18776857861042,
        longitude=-105.01582326772899,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    KIRKWELL = PopulatedPlace(
        name="Kirkwell",
        abbreviations=PlaceAbbreviations(
            three_letter="KIR",
            five_letter="KIRKW",
            seven_letter="KIRKWEL",
            fourteen_letter="KIRKWELL"
        ),
        latitude=37.148635372839465,
        longitude=-102.94104825973943,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    KISTLER_PARK = PopulatedPlace(
        name="Kistler Park",
        abbreviations=PlaceAbbreviations(
            three_letter="KIS",
            five_letter="KISTL",
            seven_letter="KISTLER",
            fourteen_letter="KISTLER PARK"
        ),
        latitude=39.541706392441256,
        longitude=-104.98051008338018,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    KIT_CARSON = PopulatedPlace(
        name="Kit Carson",
        abbreviations=PlaceAbbreviations(
            three_letter="KIT",
            five_letter="KIT C",
            seven_letter="KIT CAR",
            fourteen_letter="KIT CARSON"
        ),
        latitude=38.76111932616783,
        longitude=-102.78937618345088,
        counties=[Counties.CHEYENNE],
        nearest_airport=Airports.PUEBLO
    )
    KITTREDGE = PopulatedPlace(
        name="Kittredge",
        abbreviations=PlaceAbbreviations(
            three_letter="KIT",
            five_letter="KITTR",
            seven_letter="KITTRED",
            fourteen_letter="KITTREDGE"
        ),
        latitude=39.654716486066036,
        longitude=-105.29972407049758,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    KLINE = PopulatedPlace(
        name="Kline",
        abbreviations=PlaceAbbreviations(
            three_letter="KLI",
            five_letter="KLINE",
            seven_letter="KLINE",
            fourteen_letter="KLINE"
        ),
        latitude=37.144172653675696,
        longitude=-108.11952942680233,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    KNOB_HILL = PopulatedPlace(
        name="Knob Hill",
        abbreviations=PlaceAbbreviations(
            three_letter="KNO",
            five_letter="KNOB ",
            seven_letter="KNOB HI",
            fourteen_letter="KNOB HILL"
        ),
        latitude=38.840000107204276,
        longitude=-104.78276195999996,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    KOBE = PopulatedPlace(
        name="Kobe",
        abbreviations=PlaceAbbreviations(
            three_letter="KOB",
            five_letter="KOBE",
            seven_letter="KOBE",
            fourteen_letter="KOBE"
        ),
        latitude=39.12944224440622,
        longitude=-106.31475634018176,
        counties=[Counties.LAKE],
        nearest_airport=Airports.ASPEN
    )
    KOEN = PopulatedPlace(
        name="Koen",
        abbreviations=PlaceAbbreviations(
            three_letter="KOE",
            five_letter="KOEN",
            seven_letter="KOEN",
            fourteen_letter="KOEN"
        ),
        latitude=38.0714044507032,
        longitude=-102.34686600622166,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    KOLDEWAY = PopulatedPlace(
        name="Koldeway",
        abbreviations=PlaceAbbreviations(
            three_letter="KOL",
            five_letter="KOLDE",
            seven_letter="KOLDEWA",
            fourteen_letter="KOLDEWAY"
        ),
        latitude=39.80778422019853,
        longitude=-105.10306574279593,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    KORNMAN = PopulatedPlace(
        name="Kornman",
        abbreviations=PlaceAbbreviations(
            three_letter="KOR",
            five_letter="KORNM",
            seven_letter="KORNMAN",
            fourteen_letter="KORNMAN"
        ),
        latitude=38.15029274649186,
        longitude=-102.61214737868897,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    KRAUSS = PopulatedPlace(
        name="Krauss",
        abbreviations=PlaceAbbreviations(
            three_letter="KRA",
            five_letter="KRAUS",
            seven_letter="KRAUSS",
            fourteen_letter="KRAUSS"
        ),
        latitude=40.10693330776235,
        longitude=-104.44274402486332,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    KREMMLING = PopulatedPlace(
        name="Kremmling",
        abbreviations=PlaceAbbreviations(
            three_letter="KRE",
            five_letter="KREMM",
            seven_letter="KREMMLI",
            fourteen_letter="KREMMLING"
        ),
        latitude=40.05888076379165,
        longitude=-106.38893036704059,
        counties=[Counties.GRAND],
        nearest_airport=Airports.EAGLE
    )
    KREYBILL = PopulatedPlace(
        name="Kreybill",
        abbreviations=PlaceAbbreviations(
            three_letter="KRE",
            five_letter="KREYB",
            seven_letter="KREYBIL",
            fourteen_letter="KREYBILL"
        ),
        latitude=38.11390171025516,
        longitude=-103.10049179090834,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    KUNER = PopulatedPlace(
        name="Kuner",
        abbreviations=PlaceAbbreviations(
            three_letter="KUN",
            five_letter="KUNER",
            seven_letter="KUNER",
            fourteen_letter="KUNER"
        ),
        latitude=40.37609854113083,
        longitude=-104.49052156823956,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    KUTCH = PopulatedPlace(
        name="Kutch",
        abbreviations=PlaceAbbreviations(
            three_letter="KUT",
            five_letter="KUTCH",
            seven_letter="KUTCH",
            fourteen_letter="KUTCH"
        ),
        latitude=38.91055437753755,
        longitude=-103.86940715505563,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    LA_BOCA = PopulatedPlace(
        name="La Boca",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA BO",
            seven_letter="LA BOCA",
            fourteen_letter="LA BOCA"
        ),
        latitude=37.01112086789294,
        longitude=-107.60201020272513,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    LA_FORET = PopulatedPlace(
        name="La Foret",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA FO",
            seven_letter="LA FORE",
            fourteen_letter="LA FORET"
        ),
        latitude=39.00944363602969,
        longitude=-104.71442976277388,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    LA_FRUTO = PopulatedPlace(
        name="La Fruto",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA FR",
            seven_letter="LA FRUT",
            fourteen_letter="LA FRUTO"
        ),
        latitude=37.41473403195846,
        longitude=-105.89864336598566,
        counties=[Counties.ALAMOSA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LA_GARITA = PopulatedPlace(
        name="La Garita",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA GA",
            seven_letter="LA GARI",
            fourteen_letter="LA GARITA"
        ),
        latitude=37.840840870237,
        longitude=-106.24670678708003,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LA_ISLA = PopulatedPlace(
        name="La Isla",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA IS",
            seven_letter="LA ISLA",
            fourteen_letter="LA ISLA"
        ),
        latitude=37.10536498528984,
        longitude=-105.92716804191946,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LA_JARA = PopulatedPlace(
        name="La Jara",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA JA",
            seven_letter="LA JARA",
            fourteen_letter="LA JARA"
        ),
        latitude=37.27501440763774,
        longitude=-105.96031106632341,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LA_JUNTA = PopulatedPlace(
        name="La Junta",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA JU",
            seven_letter="LA JUNT",
            fourteen_letter="LA JUNTA"
        ),
        latitude=37.9850153627396,
        longitude=-103.54384168182412,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    LA_JUNTA_VILLAGE = PopulatedPlace(
        name="La Junta Village",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA JU",
            seven_letter="LA JUNT",
            fourteen_letter="LA JUNTA VILLA"
        ),
        latitude=38.0375144719373,
        longitude=-103.5310630849238,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    LA_PLATA = PopulatedPlace(
        name="La Plata",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA PL",
            seven_letter="LA PLAT",
            fourteen_letter="LA PLATA"
        ),
        latitude=37.39722629195546,
        longitude=-108.06314004022443,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    LA_POSTA = PopulatedPlace(
        name="La Posta",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA PO",
            seven_letter="LA POST",
            fourteen_letter="LA POSTA"
        ),
        latitude=37.12528596524379,
        longitude=-107.89507677684912,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    LA_SALLE = PopulatedPlace(
        name="La Salle",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA SA",
            seven_letter="LA SALL",
            fourteen_letter="LA SALLE"
        ),
        latitude=40.34887682244681,
        longitude=-104.70192031370902,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LA_VALLEY = PopulatedPlace(
        name="La Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA VA",
            seven_letter="LA VALL",
            fourteen_letter="LA VALLEY"
        ),
        latitude=37.10196952015144,
        longitude=-105.3477970113803,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LA_VETA = PopulatedPlace(
        name="La Veta",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA VE",
            seven_letter="LA VETA",
            fourteen_letter="LA VETA"
        ),
        latitude=37.50501790061219,
        longitude=-105.00778457303471,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LA_VETA_PASS = PopulatedPlace(
        name="La Veta Pass",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA VE",
            seven_letter="LA VETA",
            fourteen_letter="LA VETA PASS"
        ),
        latitude=37.59306960071632,
        longitude=-105.20334572629616,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LA_VISTA = PopulatedPlace(
        name="La Vista",
        abbreviations=PlaceAbbreviations(
            three_letter="LA ",
            five_letter="LA VI",
            seven_letter="LA VIST",
            fourteen_letter="LA VISTA"
        ),
        latitude=39.730006430798426,
        longitude=-104.80528786433291,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    LAFAYETTE = PopulatedPlace(
        name="Lafayette",
        abbreviations=PlaceAbbreviations(
            three_letter="LAF",
            five_letter="LAFAY",
            seven_letter="LAFAYET",
            fourteen_letter="LAFAYETTE"
        ),
        latitude=39.99360234663493,
        longitude=-105.08971596110536,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    LAKE_ARBOR = PopulatedPlace(
        name="Lake Arbor",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKE ",
            seven_letter="LAKE AR",
            fourteen_letter="LAKE ARBOR"
        ),
        latitude=39.84778422806289,
        longitude=-105.0769545408915,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LAKE_CITY = PopulatedPlace(
        name="Lake City",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKE ",
            seven_letter="LAKE CI",
            fourteen_letter="LAKE CITY"
        ),
        latitude=38.03000272716531,
        longitude=-107.31534394264264,
        counties=[Counties.HINSDALE],
        nearest_airport=Airports.TELLURIDE
    )
    LAKE_GEORGE = PopulatedPlace(
        name="Lake George",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKE ",
            seven_letter="LAKE GE",
            fourteen_letter="LAKE GEORGE"
        ),
        latitude=38.97972038852174,
        longitude=-105.35750450727602,
        counties=[Counties.PARK],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    LAKE_SHORE_PARK = PopulatedPlace(
        name="Lake Shore Park",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKE ",
            seven_letter="LAKE SH",
            fourteen_letter="LAKE SHORE PAR"
        ),
        latitude=39.95888172242667,
        longitude=-105.36694792093624,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LAKECREST = PopulatedPlace(
        name="Lakecrest",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKEC",
            seven_letter="LAKECRE",
            fourteen_letter="LAKECREST"
        ),
        latitude=39.850284225236805,
        longitude=-105.12001015196057,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    """
    LAKESIDE = PopulatedPlace(
        name="Lakeside",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKES",
            seven_letter="LAKESID",
            fourteen_letter="LAKESIDE"
        ),
        latitude=39.77721531946281,
        longitude=-105.05582672775438,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LAKESIDE = PopulatedPlace(
        name="Lakeside",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKES",
            seven_letter="LAKESID",
            fourteen_letter="LAKESIDE"
        ),
        latitude=39.7783264198132,
        longitude=-105.05943802885832,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    """
    LAKEVIEW = PopulatedPlace(
        name="Lakeview",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKEV",
            seven_letter="LAKEVIE",
            fourteen_letter="LAKEVIEW"
        ),
        latitude=39.78111751848951,
        longitude=-105.07556573288588,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LAKEVIEW_ESTATES = PopulatedPlace(
        name="Lakeview Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKEV",
            seven_letter="LAKEVIE",
            fourteen_letter="LAKEVIEW ESTAT"
        ),
        latitude=39.82472862700382,
        longitude=-105.04806573285725,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    LAKEVIEW_MEADOWS = PopulatedPlace(
        name="Lakeview Meadows",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKEV",
            seven_letter="LAKEVIE",
            fourteen_letter="LAKEVIEW MEADO"
        ),
        latitude=39.823617524830695,
        longitude=-105.07639903799122,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LAKEWOOD = PopulatedPlace(
        name="Lakewood",
        abbreviations=PlaceAbbreviations(
            three_letter="LAK",
            five_letter="LAKEW",
            seven_letter="LAKEWOO",
            fourteen_letter="LAKEWOOD"
        ),
        latitude=39.70471590756529,
        longitude=-105.08138352539805,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LAMAR = PopulatedPlace(
        name="Lamar",
        abbreviations=PlaceAbbreviations(
            three_letter="LAM",
            five_letter="LAMAR",
            seven_letter="LAMAR",
            fourteen_letter="LAMAR"
        ),
        latitude=38.08723703638498,
        longitude=-102.62075897395562,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    """
    LAMAR_HEIGHTS = PopulatedPlace(
        name="Lamar Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="LAM",
            five_letter="LAMAR",
            seven_letter="LAMAR H",
            fourteen_letter="LAMAR HEIGHTS"
        ),
        latitude=39.82556202532078,
        longitude=-105.06751013638961,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LAMAR_HEIGHTS = PopulatedPlace(
        name="Lamar Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="LAM",
            five_letter="LAMAR",
            seven_letter="LAMAR H",
            fourteen_letter="LAMAR HEIGHTS"
        ),
        latitude=39.814450824572475,
        longitude=-105.06223233377102,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    """
    LAMARTINE = PopulatedPlace(
        name="Lamartine",
        abbreviations=PlaceAbbreviations(
            three_letter="LAM",
            five_letter="LAMAR",
            seven_letter="LAMARTI",
            fourteen_letter="LAMARTINE"
        ),
        latitude=39.72943847431941,
        longitude=-105.61667785144425,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LAMB = PopulatedPlace(
        name="Lamb",
        abbreviations=PlaceAbbreviations(
            three_letter="LAM",
            five_letter="LAMB",
            seven_letter="LAMB",
            fourteen_letter="LAMB"
        ),
        latitude=40.24498696832609,
        longitude=-103.84773830099584,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    LAMPLIGHTER = PopulatedPlace(
        name="Lamplighter",
        abbreviations=PlaceAbbreviations(
            three_letter="LAM",
            five_letter="LAMPL",
            seven_letter="LAMPLIG",
            fourteen_letter="LAMPLIGHTER"
        ),
        latitude=39.830006421870564,
        longitude=-105.12473235016904,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LAPORTE = PopulatedPlace(
        name="Laporte",
        abbreviations=PlaceAbbreviations(
            three_letter="LAP",
            five_letter="LAPOR",
            seven_letter="LAPORTE",
            fourteen_letter="LAPORTE"
        ),
        latitude=40.62637762921281,
        longitude=-105.13776804939533,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LARAND = PopulatedPlace(
        name="Larand",
        abbreviations=PlaceAbbreviations(
            three_letter="LAR",
            five_letter="LARAN",
            seven_letter="LARAND",
            fourteen_letter="LARAND"
        ),
        latitude=40.62248474462501,
        longitude=-106.29281521394597,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    LARKSPUR = PopulatedPlace(
        name="Larkspur",
        abbreviations=PlaceAbbreviations(
            three_letter="LAR",
            five_letter="LARKS",
            seven_letter="LARKSPU",
            fourteen_letter="LARKSPUR"
        ),
        latitude=39.228608454987125,
        longitude=-104.88721312679161,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    LAS_ANIMAS = PopulatedPlace(
        name="Las Animas",
        abbreviations=PlaceAbbreviations(
            three_letter="LAS",
            five_letter="LAS A",
            seven_letter="LAS ANI",
            fourteen_letter="LAS ANIMAS"
        ),
        latitude=38.066679795239736,
        longitude=-103.2227175152899,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    LAS_ANIMAS_JUNCTION = PopulatedPlace(
        name="Las Animas Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="LAS",
            five_letter="LAS A",
            seven_letter="LAS ANI",
            fourteen_letter="LAS ANIMAS JUN"
        ),
        latitude=38.06251319759235,
        longitude=-103.17410510284145,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    LAS_MESITAS = PopulatedPlace(
        name="Las Mesitas",
        abbreviations=PlaceAbbreviations(
            three_letter="LAS",
            five_letter="LAS M",
            seven_letter="LAS MES",
            fourteen_letter="LAS MESITAS"
        ),
        latitude=37.06446206791918,
        longitude=-106.11059027961113,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LASAUSES = PopulatedPlace(
        name="Lasauses",
        abbreviations=PlaceAbbreviations(
            three_letter="LAS",
            five_letter="LASAU",
            seven_letter="LASAUSE",
            fourteen_letter="LASAUSES"
        ),
        latitude=37.26668331940283,
        longitude=-105.74641701748862,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LASCAR = PopulatedPlace(
        name="Lascar",
        abbreviations=PlaceAbbreviations(
            three_letter="LAS",
            five_letter="LASCA",
            seven_letter="LASCAR",
            fourteen_letter="LASCAR"
        ),
        latitude=37.82501646361408,
        longitude=-104.74860454540078,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    LAST_CHANCE = PopulatedPlace(
        name="Last Chance",
        abbreviations=PlaceAbbreviations(
            three_letter="LAS",
            five_letter="LAST ",
            seven_letter="LAST CH",
            fourteen_letter="LAST CHANCE"
        ),
        latitude=39.74082601528687,
        longitude=-103.59162338170523,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    LAWSON = PopulatedPlace(
        name="Lawson",
        abbreviations=PlaceAbbreviations(
            three_letter="LAW",
            five_letter="LAWSO",
            seven_letter="LAWSON",
            fourteen_letter="LAWSON"
        ),
        latitude=39.765827278317545,
        longitude=-105.62751145831237,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LAY = PopulatedPlace(
        name="Lay",
        abbreviations=PlaceAbbreviations(
            three_letter="LAY",
            five_letter="LAY",
            seven_letter="LAY",
            fourteen_letter="LAY"
        ),
        latitude=40.52664261473814,
        longitude=-107.88203175670344,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    LAZEAR = PopulatedPlace(
        name="Lazear",
        abbreviations=PlaceAbbreviations(
            three_letter="LAZ",
            five_letter="LAZEA",
            seven_letter="LAZEAR",
            fourteen_letter="LAZEAR"
        ),
        latitude=38.77999029674936,
        longitude=-107.7817373264968,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    LAZY_ACRES = PopulatedPlace(
        name="Lazy Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="LAZ",
            five_letter="LAZY ",
            seven_letter="LAZY AC",
            fourteen_letter="LAZY ACRES"
        ),
        latitude=40.093325343098456,
        longitude=-105.3327799295729,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LEADER = PopulatedPlace(
        name="Leader",
        abbreviations=PlaceAbbreviations(
            three_letter="LEA",
            five_letter="LEADE",
            seven_letter="LEADER",
            fourteen_letter="LEADER"
        ),
        latitude=39.899433805664216,
        longitude=-104.05635170943424,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    LEADVILLE = PopulatedPlace(
        name="Leadville",
        abbreviations=PlaceAbbreviations(
            three_letter="LEA",
            five_letter="LEADV",
            seven_letter="LEADVIL",
            fourteen_letter="LEADVILLE"
        ),
        latitude=39.250829161129275,
        longitude=-106.29253414905992,
        counties=[Counties.LAKE],
        nearest_airport=Airports.ASPEN
    )
    LEADVILLE_JUNCTION = PopulatedPlace(
        name="Leadville Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="LEA",
            five_letter="LEADV",
            seven_letter="LEADVIL",
            fourteen_letter="LEADVILLE JUNC"
        ),
        latitude=39.25860655916722,
        longitude=-106.33975776068934,
        counties=[Counties.LAKE],
        nearest_airport=Airports.ASPEN
    )
    LEAL = PopulatedPlace(
        name="Leal",
        abbreviations=PlaceAbbreviations(
            three_letter="LEA",
            five_letter="LEAL",
            seven_letter="LEAL",
            fourteen_letter="LEAL"
        ),
        latitude=39.81027035483089,
        longitude=-106.04447325870535,
        counties=[Counties.GRAND],
        nearest_airport=Airports.EAGLE
    )
    LEAWOOD = PopulatedPlace(
        name="Leawood",
        abbreviations=PlaceAbbreviations(
            three_letter="LEA",
            five_letter="LEAWO",
            seven_letter="LEAWOOD",
            fourteen_letter="LEAWOOD"
        ),
        latitude=39.60361749496002,
        longitude=-105.06362121004872,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LEBANON = PopulatedPlace(
        name="Lebanon",
        abbreviations=PlaceAbbreviations(
            three_letter="LEB",
            five_letter="LEBAN",
            seven_letter="LEBANON",
            fourteen_letter="LEBANON"
        ),
        latitude=37.45722056613215,
        longitude=-108.59149355927906,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    LENADO = PopulatedPlace(
        name="Lenado",
        abbreviations=PlaceAbbreviations(
            three_letter="LEN",
            five_letter="LENAD",
            seven_letter="LENADO",
            fourteen_letter="LENADO"
        ),
        latitude=39.24249262858888,
        longitude=-106.76254725392732,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    LEON = PopulatedPlace(
        name="Leon",
        abbreviations=PlaceAbbreviations(
            three_letter="LEO",
            five_letter="LEON",
            seven_letter="LEON",
            fourteen_letter="LEON"
        ),
        latitude=39.38471222438267,
        longitude=-107.09922554479016,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.ASPEN
    )
    LEROY = PopulatedPlace(
        name="Leroy",
        abbreviations=PlaceAbbreviations(
            three_letter="LER",
            five_letter="LEROY",
            seven_letter="LEROY",
            fourteen_letter="LEROY"
        ),
        latitude=40.526106872783544,
        longitude=-102.91410351198112,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    LEYDEN = PopulatedPlace(
        name="Leyden",
        abbreviations=PlaceAbbreviations(
            three_letter="LEY",
            five_letter="LEYDE",
            seven_letter="LEYDEN",
            fourteen_letter="LEYDEN"
        ),
        latitude=39.84471512026386,
        longitude=-105.18416406561136,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LEYDEN_JUNCTION = PopulatedPlace(
        name="Leyden Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="LEY",
            five_letter="LEYDE",
            seven_letter="LEYDEN ",
            fourteen_letter="LEYDEN JUNCTIO"
        ),
        latitude=39.84610392243525,
        longitude=-105.14832955746209,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    """
    LIBERTY = PopulatedPlace(
        name="Liberty",
        abbreviations=PlaceAbbreviations(
            three_letter="LIB",
            five_letter="LIBER",
            seven_letter="LIBERTY",
            fourteen_letter="LIBERTY"
        ),
        latitude=37.308078410669566,
        longitude=-102.72381862342252,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    LIBERTY = PopulatedPlace(
        name="Liberty",
        abbreviations=PlaceAbbreviations(
            three_letter="LIB",
            five_letter="LIBER",
            seven_letter="LIBERTY",
            fourteen_letter="LIBERTY"
        ),
        latitude=37.860284114869955,
        longitude=-105.59585484207298,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.PUEBLO
    )
    LIBERTY = PopulatedPlace(
        name="Liberty",
        abbreviations=PlaceAbbreviations(
            three_letter="LIB",
            five_letter="LIBER",
            seven_letter="LIBERTY",
            fourteen_letter="LIBERTY"
        ),
        latitude=40.20610178125389,
        longitude=-105.00915616842121,
        counties=[Counties.WELD],
        nearest_airport=Airports.PUEBLO
    )
    """
    LIBERTY_BELL = PopulatedPlace(
        name="Liberty Bell",
        abbreviations=PlaceAbbreviations(
            three_letter="LIB",
            five_letter="LIBER",
            seven_letter="LIBERTY",
            fourteen_letter="LIBERTY BELL"
        ),
        latitude=37.93527788217227,
        longitude=-107.79562863779358,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    LIGGETT = PopulatedPlace(
        name="Liggett",
        abbreviations=PlaceAbbreviations(
            three_letter="LIG",
            five_letter="LIGGE",
            seven_letter="LIGGETT",
            fourteen_letter="LIGGETT"
        ),
        latitude=40.04499145079291,
        longitude=-105.13388397755028,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LIME = PopulatedPlace(
        name="Lime",
        abbreviations=PlaceAbbreviations(
            three_letter="LIM",
            five_letter="LIME",
            seven_letter="LIME",
            fourteen_letter="LIME"
        ),
        latitude=37.9549990760658,
        longitude=-107.93090986925347,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    LIMON = PopulatedPlace(
        name="Limon",
        abbreviations=PlaceAbbreviations(
            three_letter="LIM",
            five_letter="LIMON",
            seven_letter="LIMON",
            fourteen_letter="LIMON"
        ),
        latitude=39.26388264136767,
        longitude=-103.69218345092781,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    LINCOLN = PopulatedPlace(
        name="Lincoln",
        abbreviations=PlaceAbbreviations(
            three_letter="LIN",
            five_letter="LINCO",
            seven_letter="LINCOLN",
            fourteen_letter="LINCOLN"
        ),
        latitude=39.48749331539341,
        longitude=-105.9855825069306,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.ASPEN
    )
    LINCOLN_HILLS = PopulatedPlace(
        name="Lincoln Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="LIN",
            five_letter="LINCO",
            seven_letter="LINCOLN",
            fourteen_letter="LINCOLN HILLS"
        ),
        latitude=39.922493410123366,
        longitude=-105.45833953823075,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LINCOLN_PARK = PopulatedPlace(
        name="Lincoln Park",
        abbreviations=PlaceAbbreviations(
            three_letter="LIN",
            five_letter="LINCO",
            seven_letter="LINCOLN",
            fourteen_letter="LINCOLN PARK"
        ),
        latitude=38.429171120320234,
        longitude=-105.21999961580627,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    LINDON = PopulatedPlace(
        name="Lindon",
        abbreviations=PlaceAbbreviations(
            three_letter="LIN",
            five_letter="LINDO",
            seven_letter="LINDON",
            fourteen_letter="LINDON"
        ),
        latitude=39.73943632720079,
        longitude=-103.4138410395567,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    LITTLE_DAM = PopulatedPlace(
        name="Little Dam",
        abbreviations=PlaceAbbreviations(
            three_letter="LIT",
            five_letter="LITTL",
            seven_letter="LITTLE ",
            fourteen_letter="LITTLE DAM"
        ),
        latitude=40.422212395691304,
        longitude=-105.22277344362197,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LITTLETON = PopulatedPlace(
        name="Littleton",
        abbreviations=PlaceAbbreviations(
            three_letter="LIT",
            five_letter="LITTL",
            seven_letter="LITTLET",
            fourteen_letter="LITTLETON"
        ),
        latitude=39.6133273999032,
        longitude=-105.01665990019404,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    LIVERMORE = PopulatedPlace(
        name="Livermore",
        abbreviations=PlaceAbbreviations(
            three_letter="LIV",
            five_letter="LIVER",
            seven_letter="LIVERMO",
            fourteen_letter="LIVERMORE"
        ),
        latitude=40.79443274579154,
        longitude=-105.21721368858198,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LIVING_SPRINGS = PopulatedPlace(
        name="Living Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="LIV",
            five_letter="LIVIN",
            seven_letter="LIVING ",
            fourteen_letter="LIVING SPRINGS"
        ),
        latitude=39.89137848752671,
        longitude=-104.30052096592561,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    LOBATOS = PopulatedPlace(
        name="Lobatos",
        abbreviations=PlaceAbbreviations(
            three_letter="LOB",
            five_letter="LOBAT",
            seven_letter="LOBATOS",
            fourteen_letter="LOBATOS"
        ),
        latitude=37.07946357988516,
        longitude=-105.94891924454129,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LOCHBUIE = PopulatedPlace(
        name="Lochbuie",
        abbreviations=PlaceAbbreviations(
            three_letter="LOC",
            five_letter="LOCHB",
            seven_letter="LOCHBUI",
            fourteen_letter="LOCHBUIE"
        ),
        latitude=40.007212074714175,
        longitude=-104.71608927629381,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    LODI = PopulatedPlace(
        name="Lodi",
        abbreviations=PlaceAbbreviations(
            three_letter="LOD",
            five_letter="LODI",
            seven_letter="LODI",
            fourteen_letter="LODI"
        ),
        latitude=40.25109777932164,
        longitude=-103.70384876839154,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    LOG_LANE_VILLAGE = PopulatedPlace(
        name="Log Lane Village",
        abbreviations=PlaceAbbreviations(
            three_letter="LOG",
            five_letter="LOG L",
            seven_letter="LOG LAN",
            fourteen_letter="LOG LANE VILLA"
        ),
        latitude=40.27054297349616,
        longitude=-103.8296830998296,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    LOGAN = PopulatedPlace(
        name="Logan",
        abbreviations=PlaceAbbreviations(
            three_letter="LOG",
            five_letter="LOGAN",
            seven_letter="LOGAN",
            fourteen_letter="LOGAN"
        ),
        latitude=40.57860114943776,
        longitude=-103.35827992482365,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    LOGHILL_VILLAGE = PopulatedPlace(
        name="Loghill Village",
        abbreviations=PlaceAbbreviations(
            three_letter="LOG",
            five_letter="LOGHI",
            seven_letter="LOGHILL",
            fourteen_letter="LOGHILL VILLAG"
        ),
        latitude=38.19527371861767,
        longitude=-107.7795148621446,
        counties=[Counties.OURAY],
        nearest_airport=Airports.TELLURIDE
    )
    LOMA_LINDA = PopulatedPlace(
        name="Loma Linda",
        abbreviations=PlaceAbbreviations(
            three_letter="LOM",
            five_letter="LOMA ",
            seven_letter="LOMA LI",
            fourteen_letter="LOMA LINDA"
        ),
        latitude=37.22417588474639,
        longitude=-107.79590776501362,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    LOMBARD_VILLAGE = PopulatedPlace(
        name="Lombard Village",
        abbreviations=PlaceAbbreviations(
            three_letter="LOM",
            five_letter="LOMBA",
            seven_letter="LOMBARD",
            fourteen_letter="LOMBARD VILLAG"
        ),
        latitude=38.22500953468085,
        longitude=-104.54498253960048,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    LONE_PINE_ESTATES = PopulatedPlace(
        name="Lone Pine Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="LON",
            five_letter="LONE ",
            seven_letter="LONE PI",
            fourteen_letter="LONE PINE ESTA"
        ),
        latitude=39.59499438113596,
        longitude=-105.24527855105782,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LONE_STAR = PopulatedPlace(
        name="Lone Star",
        abbreviations=PlaceAbbreviations(
            three_letter="LON",
            five_letter="LONE ",
            seven_letter="LONE ST",
            fourteen_letter="LONE STAR"
        ),
        latitude=40.351936352489304,
        longitude=-102.8513293764708,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    LONE_TREE = PopulatedPlace(
        name="Lone Tree",
        abbreviations=PlaceAbbreviations(
            three_letter="LON",
            five_letter="LONE ",
            seven_letter="LONE TR",
            fourteen_letter="LONE TREE"
        ),
        latitude=39.5313873989478,
        longitude=-104.86197205463094,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    LONETREE = PopulatedPlace(
        name="Lonetree",
        abbreviations=PlaceAbbreviations(
            three_letter="LON",
            five_letter="LONET",
            seven_letter="LONETRE",
            fourteen_letter="LONETREE"
        ),
        latitude=37.16806631660404,
        longitude=-107.172830724275,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    LONGMONT = PopulatedPlace(
        name="Longmont",
        abbreviations=PlaceAbbreviations(
            three_letter="LON",
            five_letter="LONGM",
            seven_letter="LONGMON",
            fourteen_letter="LONGMONT"
        ),
        latitude=40.167213369566355,
        longitude=-105.10193768517456,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LONGVIEW = PopulatedPlace(
        name="Longview",
        abbreviations=PlaceAbbreviations(
            three_letter="LON",
            five_letter="LONGV",
            seven_letter="LONGVIE",
            fourteen_letter="LONGVIEW"
        ),
        latitude=39.41749536027373,
        longitude=-105.1938896185427,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LOS_CERRITOS = PopulatedPlace(
        name="Los Cerritos",
        abbreviations=PlaceAbbreviations(
            three_letter="LOS",
            five_letter="LOS C",
            seven_letter="LOS CER",
            fourteen_letter="LOS CERRITOS"
        ),
        latitude=37.14835129216442,
        longitude=-105.91086394290619,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LOS_FUERTES = PopulatedPlace(
        name="Los Fuertes",
        abbreviations=PlaceAbbreviations(
            three_letter="LOS",
            five_letter="LOS F",
            seven_letter="LOS FUE",
            fourteen_letter="LOS FUERTES"
        ),
        latitude=37.134468122811256,
        longitude=-105.37974272164769,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LOUISVILLE = PopulatedPlace(
        name="Louisville",
        abbreviations=PlaceAbbreviations(
            three_letter="LOU",
            five_letter="LOUIS",
            seven_letter="LOUISVI",
            fourteen_letter="LOUISVILLE"
        ),
        latitude=39.977769441487794,
        longitude=-105.13193976905217,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    LOUVIERS = PopulatedPlace(
        name="Louviers",
        abbreviations=PlaceAbbreviations(
            three_letter="LOU",
            five_letter="LOUVI",
            seven_letter="LOUVIER",
            fourteen_letter="LOUVIERS"
        ),
        latitude=39.47777288178747,
        longitude=-105.0072161820051,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    LOVELAND = PopulatedPlace(
        name="Loveland",
        abbreviations=PlaceAbbreviations(
            three_letter="LOV",
            five_letter="LOVEL",
            seven_letter="LOVELAN",
            fourteen_letter="LOVELAND"
        ),
        latitude=40.39776770281662,
        longitude=-105.07499030714911,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LOVELAND_HEIGHTS = PopulatedPlace(
        name="Loveland Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="LOV",
            five_letter="LOVEL",
            seven_letter="LOVELAN",
            fourteen_letter="LOVELAND HEIGH"
        ),
        latitude=40.38971237363677,
        longitude=-105.46417289585185,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LOWE = PopulatedPlace(
        name="Lowe",
        abbreviations=PlaceAbbreviations(
            three_letter="LOW",
            five_letter="LOWE",
            seven_letter="LOWE",
            fourteen_letter="LOWE"
        ),
        latitude=40.492487149472254,
        longitude=-104.59552540644171,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LOYD = PopulatedPlace(
        name="Loyd",
        abbreviations=PlaceAbbreviations(
            three_letter="LOY",
            five_letter="LOYD",
            seven_letter="LOYD",
            fourteen_letter="LOYD"
        ),
        latitude=40.30359100013726,
        longitude=-107.70480138977126,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    LUBERS = PopulatedPlace(
        name="Lubers",
        abbreviations=PlaceAbbreviations(
            three_letter="LUB",
            five_letter="LUBER",
            seven_letter="LUBERS",
            fourteen_letter="LUBERS"
        ),
        latitude=38.128902323732916,
        longitude=-102.92437645063598,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    LUCERNE = PopulatedPlace(
        name="Lucerne",
        abbreviations=PlaceAbbreviations(
            three_letter="LUC",
            five_letter="LUCER",
            seven_letter="LUCERNE",
            fourteen_letter="LUCERNE"
        ),
        latitude=40.48193144070086,
        longitude=-104.69969712980617,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    LUCKY_SEVEN_SUMMER_HOMES = PopulatedPlace(
        name="Lucky Seven Summer Homes",
        abbreviations=PlaceAbbreviations(
            three_letter="LUC",
            five_letter="LUCKY",
            seven_letter="LUCKY S",
            fourteen_letter="LUCKY SEVEN SU"
        ),
        latitude=37.58390150216752,
        longitude=-106.73977477013369,
        counties=[Counties.MINERAL],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    LUDLOW = PopulatedPlace(
        name="Ludlow",
        abbreviations=PlaceAbbreviations(
            three_letter="LUD",
            five_letter="LUDLO",
            seven_letter="LUDLOW",
            fourteen_letter="LUDLOW"
        ),
        latitude=37.33335540140797,
        longitude=-104.58332775901874,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    LUJANE = PopulatedPlace(
        name="Lujane",
        abbreviations=PlaceAbbreviations(
            three_letter="LUJ",
            five_letter="LUJAN",
            seven_letter="LUJANE",
            fourteen_letter="LUJANE"
        ),
        latitude=38.4872144610199,
        longitude=-107.73367998396077,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    LYCAN = PopulatedPlace(
        name="Lycan",
        abbreviations=PlaceAbbreviations(
            three_letter="LYC",
            five_letter="LYCAN",
            seven_letter="LYCAN",
            fourteen_letter="LYCAN"
        ),
        latitude=37.61529719001186,
        longitude=-102.20074842803223,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    LYNDALE_PARK = PopulatedPlace(
        name="Lyndale Park",
        abbreviations=PlaceAbbreviations(
            three_letter="LYN",
            five_letter="LYNDA",
            seven_letter="LYNDALE",
            fourteen_letter="LYNDALE PARK"
        ),
        latitude=39.81639532363948,
        longitude=-105.07389903733514,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    LYONS = PopulatedPlace(
        name="Lyons",
        abbreviations=PlaceAbbreviations(
            three_letter="LYO",
            five_letter="LYONS",
            seven_letter="LYONS",
            fourteen_letter="LYONS"
        ),
        latitude=40.2247139651152,
        longitude=-105.27138823121618,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MACK = PopulatedPlace(
        name="Mack",
        abbreviations=PlaceAbbreviations(
            three_letter="MAC",
            five_letter="MACK",
            seven_letter="MACK",
            fourteen_letter="MACK"
        ),
        latitude=39.223875378684,
        longitude=-108.86511541096871,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    MAD_CREEK = PopulatedPlace(
        name="Mad Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="MAD",
            five_letter="MAD C",
            seven_letter="MAD CRE",
            fourteen_letter="MAD CREEK"
        ),
        latitude=40.56609259325688,
        longitude=-106.88839404140504,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    """
    MAGNOLIA = PopulatedPlace(
        name="Magnolia",
        abbreviations=PlaceAbbreviations(
            three_letter="MAG",
            five_letter="MAGNO",
            seven_letter="MAGNOLI",
            fourteen_letter="MAGNOLIA"
        ),
        latitude=39.99388152760429,
        longitude=-105.36528122538567,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MAGNOLIA = PopulatedPlace(
        name="Magnolia",
        abbreviations=PlaceAbbreviations(
            three_letter="MAG",
            five_letter="MAGNO",
            seven_letter="MAGNOLI",
            fourteen_letter="MAGNOLIA"
        ),
        latitude=39.76667313389851,
        longitude=-104.83167677501751,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    MAHER = PopulatedPlace(
        name="Maher",
        abbreviations=PlaceAbbreviations(
            three_letter="MAH",
            five_letter="MAHER",
            seven_letter="MAHER",
            fourteen_letter="MAHER"
        ),
        latitude=38.64499399197001,
        longitude=-107.58479056862217,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    MAITLAND = PopulatedPlace(
        name="Maitland",
        abbreviations=PlaceAbbreviations(
            three_letter="MAI",
            five_letter="MAITL",
            seven_letter="MAITLAN",
            fourteen_letter="MAITLAND"
        ),
        latitude=37.656684633613736,
        longitude=-104.83388714804613,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    MALACHITE = PopulatedPlace(
        name="Malachite",
        abbreviations=PlaceAbbreviations(
            three_letter="MAL",
            five_letter="MALAC",
            seven_letter="MALACHI",
            fourteen_letter="MALACHITE"
        ),
        latitude=37.754455521101136,
        longitude=-105.26084585546835,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MALOY = PopulatedPlace(
        name="Maloy",
        abbreviations=PlaceAbbreviations(
            three_letter="MAL",
            five_letter="MALOY",
            seven_letter="MALOY",
            fourteen_letter="MALOY"
        ),
        latitude=40.244434789233594,
        longitude=-104.96998766370638,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MALTA = PopulatedPlace(
        name="Malta",
        abbreviations=PlaceAbbreviations(
            three_letter="MAL",
            five_letter="MALTA",
            seven_letter="MALTA",
            fourteen_letter="MALTA"
        ),
        latitude=39.22944025504103,
        longitude=-106.35086896045482,
        counties=[Counties.LAKE],
        nearest_airport=Airports.ASPEN
    )
    MANASSA = PopulatedPlace(
        name="Manassa",
        abbreviations=PlaceAbbreviations(
            three_letter="MAN",
            five_letter="MANAS",
            seven_letter="MANASSA",
            fourteen_letter="MANASSA"
        ),
        latitude=37.1741837945965,
        longitude=-105.93753155141616,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MANCOS = PopulatedPlace(
        name="Mancos",
        abbreviations=PlaceAbbreviations(
            three_letter="MAN",
            five_letter="MANCO",
            seven_letter="MANCOS",
            fourteen_letter="MANCOS"
        ),
        latitude=37.34500187012043,
        longitude=-108.2892592833204,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    MANILA = PopulatedPlace(
        name="Manila",
        abbreviations=PlaceAbbreviations(
            three_letter="MAN",
            five_letter="MANIL",
            seven_letter="MANILA",
            fourteen_letter="MANILA"
        ),
        latitude=39.75638135372532,
        longitude=-104.5224734023223,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    MANITOU_SPRINGS = PopulatedPlace(
        name="Manitou Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="MAN",
            five_letter="MANIT",
            seven_letter="MANITOU",
            fourteen_letter="MANITOU SPRING"
        ),
        latitude=38.859719000843654,
        longitude=-104.91720889281783,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    MANZANOLA = PopulatedPlace(
        name="Manzanola",
        abbreviations=PlaceAbbreviations(
            three_letter="MAN",
            five_letter="MANZA",
            seven_letter="MANZANO",
            fourteen_letter="MANZANOLA"
        ),
        latitude=38.1094571613765,
        longitude=-103.8660754698551,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    MAPLE_GROVE = PopulatedPlace(
        name="Maple Grove",
        abbreviations=PlaceAbbreviations(
            three_letter="MAP",
            five_letter="MAPLE",
            seven_letter="MAPLE G",
            fourteen_letter="MAPLE GROVE"
        ),
        latitude=39.96361754254406,
        longitude=-105.09556575969282,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    MAPLEWOOD_ACRES = PopulatedPlace(
        name="Maplewood Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="MAP",
            five_letter="MAPLE",
            seven_letter="MAPLEWO",
            fourteen_letter="MAPLEWOOD ACRE"
        ),
        latitude=39.824728621484496,
        longitude=-105.12251014902319,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MARBLE = PopulatedPlace(
        name="Marble",
        abbreviations=PlaceAbbreviations(
            three_letter="MAR",
            five_letter="MARBL",
            seven_letter="MARBLE",
            fourteen_letter="MARBLE"
        ),
        latitude=39.07221677633197,
        longitude=-107.18894822883067,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.ASPEN
    )
    MARCOTT = PopulatedPlace(
        name="Marcott",
        abbreviations=PlaceAbbreviations(
            three_letter="MAR",
            five_letter="MARCO",
            seven_letter="MARCOTT",
            fourteen_letter="MARCOTT"
        ),
        latitude=40.87860903575927,
        longitude=-102.72409000896153,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    MARIANO = PopulatedPlace(
        name="Mariano",
        abbreviations=PlaceAbbreviations(
            three_letter="MAR",
            five_letter="MARIA",
            seven_letter="MARIANO",
            fourteen_letter="MARIANO"
        ),
        latitude=37.1794445102276,
        longitude=-108.87344689176689,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    MARIGOLD = PopulatedPlace(
        name="Marigold",
        abbreviations=PlaceAbbreviations(
            three_letter="MAR",
            five_letter="MARIG",
            seven_letter="MARIGOL",
            fourteen_letter="MARIGOLD"
        ),
        latitude=38.661109453236236,
        longitude=-105.2213841406446,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    MARLMAN = PopulatedPlace(
        name="Marlman",
        abbreviations=PlaceAbbreviations(
            three_letter="MAR",
            five_letter="MARLM",
            seven_letter="MARLMAN",
            fourteen_letter="MARLMAN"
        ),
        latitude=38.09362419129428,
        longitude=-103.34911074705673,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    MARNETT = PopulatedPlace(
        name="Marnett",
        abbreviations=PlaceAbbreviations(
            three_letter="MAR",
            five_letter="MARNE",
            seven_letter="MARNETT",
            fourteen_letter="MARNETT"
        ),
        latitude=40.16832466722434,
        longitude=-105.13388329213564,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MARSHALL = PopulatedPlace(
        name="Marshall",
        abbreviations=PlaceAbbreviations(
            three_letter="MAR",
            five_letter="MARSH",
            seven_letter="MARSHAL",
            fourteen_letter="MARSHALL"
        ),
        latitude=39.95554783151897,
        longitude=-105.22972118920092,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MARSHDALE = PopulatedPlace(
        name="Marshdale",
        abbreviations=PlaceAbbreviations(
            three_letter="MAR",
            five_letter="MARSH",
            seven_letter="MARSHDA",
            fourteen_letter="MARSHDALE"
        ),
        latitude=39.5924945767058,
        longitude=-105.31222506551723,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MARVEL = PopulatedPlace(
        name="Marvel",
        abbreviations=PlaceAbbreviations(
            three_letter="MAR",
            five_letter="MARVE",
            seven_letter="MARVEL",
            fourteen_letter="MARVEL"
        ),
        latitude=37.11250594849798,
        longitude=-108.12675182599111,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    MARYVALE = PopulatedPlace(
        name="Maryvale",
        abbreviations=PlaceAbbreviations(
            three_letter="MAR",
            five_letter="MARYV",
            seven_letter="MARYVAL",
            fourteen_letter="MARYVALE"
        ),
        latitude=39.93304889027394,
        longitude=-105.7872406142157,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MASON_CORNER = PopulatedPlace(
        name="Mason Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="MAS",
            five_letter="MASON",
            seven_letter="MASON C",
            fourteen_letter="MASON CORNER"
        ),
        latitude=40.46693153863856,
        longitude=-104.70191952858147,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MASONTOWN = PopulatedPlace(
        name="Masontown",
        abbreviations=PlaceAbbreviations(
            three_letter="MAS",
            five_letter="MASON",
            seven_letter="MASONTO",
            fourteen_letter="MASONTOWN"
        ),
        latitude=39.566381717866875,
        longitude=-106.10030864256953,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    MASONVILLE = PopulatedPlace(
        name="Masonville",
        abbreviations=PlaceAbbreviations(
            three_letter="MAS",
            five_letter="MASON",
            seven_letter="MASONVI",
            fourteen_letter="MASONVILLE"
        ),
        latitude=40.48748960528934,
        longitude=-105.21082794880778,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MASSADONA = PopulatedPlace(
        name="Massadona",
        abbreviations=PlaceAbbreviations(
            three_letter="MAS",
            five_letter="MASSA",
            seven_letter="MASSADO",
            fourteen_letter="MASSADONA"
        ),
        latitude=40.25275432444937,
        longitude=-108.64039198812759,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    MASTERS = PopulatedPlace(
        name="Masters",
        abbreviations=PlaceAbbreviations(
            three_letter="MAS",
            five_letter="MASTE",
            seven_letter="MASTERS",
            fourteen_letter="MASTERS"
        ),
        latitude=40.30943204965956,
        longitude=-104.24496050247109,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    MATHESON = PopulatedPlace(
        name="Matheson",
        abbreviations=PlaceAbbreviations(
            three_letter="MAT",
            five_letter="MATHE",
            seven_letter="MATHESO",
            fourteen_letter="MATHESON"
        ),
        latitude=39.17166110830743,
        longitude=-103.9755223080789,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    MATTHEWS = PopulatedPlace(
        name="Matthews",
        abbreviations=PlaceAbbreviations(
            three_letter="MAT",
            five_letter="MATTH",
            seven_letter="MATTHEW",
            fourteen_letter="MATTHEWS"
        ),
        latitude=40.47970955497317,
        longitude=-104.49774318230078,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MAXEYVILLE = PopulatedPlace(
        name="Maxeyville",
        abbreviations=PlaceAbbreviations(
            three_letter="MAX",
            five_letter="MAXEY",
            seven_letter="MAXEYVI",
            fourteen_letter="MAXEYVILLE"
        ),
        latitude=37.618064144725054,
        longitude=-106.14948324228237,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MAY_VALLEY = PopulatedPlace(
        name="May Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="MAY",
            five_letter="MAY V",
            seven_letter="MAY VAL",
            fourteen_letter="MAY VALLEY"
        ),
        latitude=38.20168165395597,
        longitude=-102.61381378408362,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    MAYDAY = PopulatedPlace(
        name="Mayday",
        abbreviations=PlaceAbbreviations(
            three_letter="MAY",
            five_letter="MAYDA",
            seven_letter="MAYDAY",
            fourteen_letter="MAYDAY"
        ),
        latitude=37.350560184766096,
        longitude=-108.07675123884923,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    MCARTHUR_RANCH = PopulatedPlace(
        name="McArthur Ranch",
        abbreviations=PlaceAbbreviations(
            three_letter="MCA",
            five_letter="MCART",
            seven_letter="MCARTHU",
            fourteen_letter="MCARTHUR RANCH"
        ),
        latitude=39.51730639424562,
        longitude=-104.90581006327818,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    MCCLAVE = PopulatedPlace(
        name="McClave",
        abbreviations=PlaceAbbreviations(
            three_letter="MCC",
            five_letter="MCCLA",
            seven_letter="MCCLAVE",
            fourteen_letter="MCCLAVE"
        ),
        latitude=38.13751372929204,
        longitude=-102.85048593387762,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    MCCLELLANDS = PopulatedPlace(
        name="McClellands",
        abbreviations=PlaceAbbreviations(
            three_letter="MCC",
            five_letter="MCCLE",
            seven_letter="MCCLELL",
            fourteen_letter="MCCLELLANDS"
        ),
        latitude=40.52804471957427,
        longitude=-105.08082262362291,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MCCOY = PopulatedPlace(
        name="McCoy",
        abbreviations=PlaceAbbreviations(
            three_letter="MCC",
            five_letter="MCCOY",
            seven_letter="MCCOY",
            fourteen_letter="MCCOY"
        ),
        latitude=39.91610462093024,
        longitude=-106.72560422471753,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    MCGREGOR = PopulatedPlace(
        name="McGregor",
        abbreviations=PlaceAbbreviations(
            three_letter="MCG",
            five_letter="MCGRE",
            seven_letter="MCGREGO",
            fourteen_letter="MCGREGOR"
        ),
        latitude=40.47942617178853,
        longitude=-107.03506396312008,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    MCKAY_LANDING = PopulatedPlace(
        name="McKay Landing",
        abbreviations=PlaceAbbreviations(
            three_letter="MCK",
            five_letter="MCKAY",
            seven_letter="MCKAY L",
            fourteen_letter="MCKAY LANDING"
        ),
        latitude=39.95333974624981,
        longitude=-105.02056574091336,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    MCKENZIE_JUNCTION = PopulatedPlace(
        name="McKenzie Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="MCK",
            five_letter="MCKEN",
            seven_letter="MCKENZI",
            fourteen_letter="MCKENZIE JUNCT"
        ),
        latitude=38.16417548408634,
        longitude=-105.19083658176021,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.PUEBLO
    )
    MEAD = PopulatedPlace(
        name="Mead",
        abbreviations=PlaceAbbreviations(
            three_letter="MEA",
            five_letter="MEAD",
            seven_letter="MEAD",
            fourteen_letter="MEAD"
        ),
        latitude=40.23332388577927,
        longitude=-104.99860016882377,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MEADOW_HILLS = PopulatedPlace(
        name="Meadow Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="MEA",
            five_letter="MEADO",
            seven_letter="MEADOW ",
            fourteen_letter="MEADOW HILLS"
        ),
        latitude=39.64111751735368,
        longitude=-104.8172322569144,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    MEADOW_LAKE = PopulatedPlace(
        name="Meadow Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="MEA",
            five_letter="MEADO",
            seven_letter="MEADOW ",
            fourteen_letter="MEADOW LAKE"
        ),
        latitude=39.806950817448694,
        longitude=-105.14223235116731,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MEADOW_WOOD_FARMS = PopulatedPlace(
        name="Meadow Wood Farms",
        abbreviations=PlaceAbbreviations(
            three_letter="MEA",
            five_letter="MEADO",
            seven_letter="MEADOW ",
            fourteen_letter="MEADOW WOOD FA"
        ),
        latitude=39.838062019431845,
        longitude=-105.17973236370102,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MEADOWBROOK_HEIGHTS = PopulatedPlace(
        name="Meadowbrook Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="MEA",
            five_letter="MEADO",
            seven_letter="MEADOWB",
            fourteen_letter="MEADOWBROOK HE"
        ),
        latitude=39.56222858773833,
        longitude=-105.08834341080967,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MEADOWOOD = PopulatedPlace(
        name="Meadowood",
        abbreviations=PlaceAbbreviations(
            three_letter="MEA",
            five_letter="MEADO",
            seven_letter="MEADOWO",
            fourteen_letter="MEADOWOOD"
        ),
        latitude=39.65889532072106,
        longitude=-104.80389895571597,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    MEDINA_PLAZA = PopulatedPlace(
        name="Medina Plaza",
        abbreviations=PlaceAbbreviations(
            three_letter="MED",
            five_letter="MEDIN",
            seven_letter="MEDINA ",
            fourteen_letter="MEDINA PLAZA"
        ),
        latitude=37.12780425819773,
        longitude=-104.79222468743882,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MEEKER = PopulatedPlace(
        name="Meeker",
        abbreviations=PlaceAbbreviations(
            three_letter="MEE",
            five_letter="MEEKE",
            seven_letter="MEEKER",
            fourteen_letter="MEEKER"
        ),
        latitude=40.03747955105064,
        longitude=-107.91314070245346,
        counties=[Counties.RIO_BLANCO],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    MEEKER_PARK = PopulatedPlace(
        name="Meeker Park",
        abbreviations=PlaceAbbreviations(
            three_letter="MEE",
            five_letter="MEEKE",
            seven_letter="MEEKER ",
            fourteen_letter="MEEKER PARK"
        ),
        latitude=40.233880048018875,
        longitude=-105.53084339216048,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MELINA = PopulatedPlace(
        name="Melina",
        abbreviations=PlaceAbbreviations(
            three_letter="MEL",
            five_letter="MELIN",
            seven_letter="MELINA",
            fourteen_letter="MELINA"
        ),
        latitude=38.099457202460655,
        longitude=-103.18660520942728,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    MELROSE = PopulatedPlace(
        name="Melrose",
        abbreviations=PlaceAbbreviations(
            three_letter="MEL",
            five_letter="MELRO",
            seven_letter="MELROSE",
            fourteen_letter="MELROSE"
        ),
        latitude=39.77306201630188,
        longitude=-105.09084343572005,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MEREDITH = PopulatedPlace(
        name="Meredith",
        abbreviations=PlaceAbbreviations(
            three_letter="MER",
            five_letter="MERED",
            seven_letter="MEREDIT",
            fourteen_letter="MEREDITH"
        ),
        latitude=39.36304754689439,
        longitude=-106.73004636055981,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.ASPEN
    )
    MERIDIAN = PopulatedPlace(
        name="Meridian",
        abbreviations=PlaceAbbreviations(
            three_letter="MER",
            five_letter="MERID",
            seven_letter="MERIDIA",
            fourteen_letter="MERIDIAN"
        ),
        latitude=39.55166170184157,
        longitude=-104.85887675660592,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    MERIDIAN_VILLAGE = PopulatedPlace(
        name="Meridian Village",
        abbreviations=PlaceAbbreviations(
            three_letter="MER",
            five_letter="MERID",
            seven_letter="MERIDIA",
            fourteen_letter="MERIDIAN VILLA"
        ),
        latitude=39.5310169017888,
        longitude=-104.82613314653344,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    MERINO = PopulatedPlace(
        name="Merino",
        abbreviations=PlaceAbbreviations(
            three_letter="MER",
            five_letter="MERIN",
            seven_letter="MERINO",
            fourteen_letter="MERINO"
        ),
        latitude=40.48248903652103,
        longitude=-103.3513377110703,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    MESA = PopulatedPlace(
        name="Mesa",
        abbreviations=PlaceAbbreviations(
            three_letter="MES",
            five_letter="MESA",
            seven_letter="MESA",
            fourteen_letter="MESA"
        ),
        latitude=39.16637482289997,
        longitude=-108.13897674806282,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    MESA_HEIGHTS = PopulatedPlace(
        name="Mesa Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="MES",
            five_letter="MESA ",
            seven_letter="MESA HE",
            fourteen_letter="MESA HEIGHTS"
        ),
        latitude=39.83917312320028,
        longitude=-105.1269545522133,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MESA_LAKES = PopulatedPlace(
        name="Mesa Lakes",
        abbreviations=PlaceAbbreviations(
            three_letter="MES",
            five_letter="MESA ",
            seven_letter="MESA LA",
            fourteen_letter="MESA LAKES"
        ),
        latitude=39.04998671104704,
        longitude=-108.09230672412548,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    MESA_LAKES_RESORT = PopulatedPlace(
        name="Mesa Lakes Resort",
        abbreviations=PlaceAbbreviations(
            three_letter="MES",
            five_letter="MESA ",
            seven_letter="MESA LA",
            fourteen_letter="MESA LAKES RES"
        ),
        latitude=39.049153411070506,
        longitude=-108.0914732240858,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    MESITA = PopulatedPlace(
        name="Mesita",
        abbreviations=PlaceAbbreviations(
            three_letter="MES",
            five_letter="MESIT",
            seven_letter="MESITA",
            fourteen_letter="MESITA"
        ),
        latitude=37.09835650420655,
        longitude=-105.60196736823667,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MESSEX = PopulatedPlace(
        name="Messex",
        abbreviations=PlaceAbbreviations(
            three_letter="MES",
            five_letter="MESSE",
            seven_letter="MESSEX",
            fourteen_letter="MESSEX"
        ),
        latitude=40.429431823223354,
        longitude=-103.43661812541961,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    MEYERS_CORNER = PopulatedPlace(
        name="Meyers Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="MEY",
            five_letter="MEYER",
            seven_letter="MEYERS ",
            fourteen_letter="MEYERS CORNER"
        ),
        latitude=40.6680444428568,
        longitude=-105.01942992723787,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MID_VAIL = PopulatedPlace(
        name="Mid Vail",
        abbreviations=PlaceAbbreviations(
            three_letter="MID",
            five_letter="MID V",
            seven_letter="MID VAI",
            fourteen_letter="MID VAIL"
        ),
        latitude=39.61499230588038,
        longitude=-106.36781670865741,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    MIDDLETON = PopulatedPlace(
        name="Middleton",
        abbreviations=PlaceAbbreviations(
            three_letter="MID",
            five_letter="MIDDL",
            seven_letter="MIDDLET",
            fourteen_letter="MIDDLETON"
        ),
        latitude=37.8550027858729,
        longitude=-107.57229238083772,
        counties=[Counties.SAN_JUAN],
        nearest_airport=Airports.TELLURIDE
    )
    """
    MIDWAY = PopulatedPlace(
        name="Midway",
        abbreviations=PlaceAbbreviations(
            three_letter="MID",
            five_letter="MIDWA",
            seven_letter="MIDWAY",
            fourteen_letter="MIDWAY"
        ),
        latitude=40.226375397247125,
        longitude=-103.39773009180436,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    MIDWAY = PopulatedPlace(
        name="Midway",
        abbreviations=PlaceAbbreviations(
            three_letter="MID",
            five_letter="MIDWA",
            seven_letter="MIDWAY",
            fourteen_letter="MIDWAY"
        ),
        latitude=38.7399946695254,
        longitude=-105.1427678315182,
        counties=[Counties.TELLER],
        nearest_airport=Airports.DENVER
    )
    MIDWAY = PopulatedPlace(
        name="Midway",
        abbreviations=PlaceAbbreviations(
            three_letter="MID",
            five_letter="MIDWA",
            seven_letter="MIDWAY",
            fourteen_letter="MIDWAY"
        ),
        latitude=40.4302678894677,
        longitude=-105.32277746826014,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.DENVER
    )
    MIDWAY = PopulatedPlace(
        name="Midway",
        abbreviations=PlaceAbbreviations(
            three_letter="MID",
            five_letter="MIDWA",
            seven_letter="MIDWAY",
            fourteen_letter="MIDWAY"
        ),
        latitude=37.149192918195354,
        longitude=-102.18602068010307,
        counties=[Counties.BACA],
        nearest_airport=Airports.DENVER
    )
    MIDWAY = PopulatedPlace(
        name="Midway",
        abbreviations=PlaceAbbreviations(
            three_letter="MID",
            five_letter="MIDWA",
            seven_letter="MIDWAY",
            fourteen_letter="MIDWAY"
        ),
        latitude=38.842494995045456,
        longitude=-104.97387560369697,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.DENVER
    )
    """
    MILLIKEN = PopulatedPlace(
        name="Milliken",
        abbreviations=PlaceAbbreviations(
            three_letter="MIL",
            five_letter="MILLI",
            seven_letter="MILLIKE",
            fourteen_letter="MILLIKEN"
        ),
        latitude=40.329433308848195,
        longitude=-104.85526014735689,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MILLWOOD = PopulatedPlace(
        name="Millwood",
        abbreviations=PlaceAbbreviations(
            three_letter="MIL",
            five_letter="MILLW",
            seven_letter="MILLWOO",
            fourteen_letter="MILLWOOD"
        ),
        latitude=37.42166747802656,
        longitude=-108.33370600118394,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    MILNER = PopulatedPlace(
        name="Milner",
        abbreviations=PlaceAbbreviations(
            three_letter="MIL",
            five_letter="MILNE",
            seven_letter="MILNER",
            fourteen_letter="MILNER"
        ),
        latitude=40.48470397325531,
        longitude=-107.0195081607385,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    MINDEMAN = PopulatedPlace(
        name="Mindeman",
        abbreviations=PlaceAbbreviations(
            three_letter="MIN",
            five_letter="MINDE",
            seven_letter="MINDEMA",
            fourteen_letter="MINDEMAN"
        ),
        latitude=37.70696289806085,
        longitude=-103.91663374190517,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    MINERAL_HOT_SPRINGS = PopulatedPlace(
        name="Mineral Hot Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="MIN",
            five_letter="MINER",
            seven_letter="MINERAL",
            fourteen_letter="MINERAL HOT SP"
        ),
        latitude=38.16889423724808,
        longitude=-105.92585704867867,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MINNEHAHA = PopulatedPlace(
        name="Minnehaha",
        abbreviations=PlaceAbbreviations(
            three_letter="MIN",
            five_letter="MINNE",
            seven_letter="MINNEHA",
            fourteen_letter="MINNEHAHA"
        ),
        latitude=38.849439896822844,
        longitude=-104.95943130118945,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    MINTURN = PopulatedPlace(
        name="Minturn",
        abbreviations=PlaceAbbreviations(
            three_letter="MIN",
            five_letter="MINTU",
            seven_letter="MINTURN",
            fourteen_letter="MINTURN"
        ),
        latitude=39.586381197849164,
        longitude=-106.4308735188348,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    MIRAMONTE = PopulatedPlace(
        name="Miramonte",
        abbreviations=PlaceAbbreviations(
            three_letter="MIR",
            five_letter="MIRAM",
            seven_letter="MIRAMON",
            fourteen_letter="MIRAMONTE"
        ),
        latitude=39.930548619180854,
        longitude=-105.37278131898154,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MISHAWAKA = PopulatedPlace(
        name="Mishawaka",
        abbreviations=PlaceAbbreviations(
            three_letter="MIS",
            five_letter="MISHA",
            seven_letter="MISHAWA",
            fourteen_letter="MISHAWAKA"
        ),
        latitude=40.68721012030829,
        longitude=-105.36583170939855,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MISSION_VIEJO = PopulatedPlace(
        name="Mission Viejo",
        abbreviations=PlaceAbbreviations(
            three_letter="MIS",
            five_letter="MISSI",
            seven_letter="MISSION",
            fourteen_letter="MISSION VIEJO"
        ),
        latitude=39.64639531933682,
        longitude=-104.80001005362959,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    MITCHELL = PopulatedPlace(
        name="Mitchell",
        abbreviations=PlaceAbbreviations(
            three_letter="MIT",
            five_letter="MITCH",
            seven_letter="MITCHEL",
            fourteen_letter="MITCHELL"
        ),
        latitude=39.391660579534346,
        longitude=-106.31920297119387,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.ASPEN
    )
    MODEL = PopulatedPlace(
        name="Model",
        abbreviations=PlaceAbbreviations(
            three_letter="MOD",
            five_letter="MODEL",
            seven_letter="MODEL",
            fourteen_letter="MODEL"
        ),
        latitude=37.37224332804823,
        longitude=-104.24498398533092,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    MOFFAT = PopulatedPlace(
        name="Moffat",
        abbreviations=PlaceAbbreviations(
            three_letter="MOF",
            five_letter="MOFFA",
            seven_letter="MOFFAT",
            fourteen_letter="MOFFAT"
        ),
        latitude=37.998894314008396,
        longitude=-105.91002572760954,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MOGOTE = PopulatedPlace(
        name="Mogote",
        abbreviations=PlaceAbbreviations(
            three_letter="MOG",
            five_letter="MOGOT",
            seven_letter="MOGOTE",
            fourteen_letter="MOGOTE"
        ),
        latitude=37.05946236858199,
        longitude=-106.09225637433138,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MOLINA = PopulatedPlace(
        name="Molina",
        abbreviations=PlaceAbbreviations(
            three_letter="MOL",
            five_letter="MOLIN",
            seven_letter="MOLINA",
            fourteen_letter="MOLINA"
        ),
        latitude=39.18915203135657,
        longitude=-108.06036203344593,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    MONSON = PopulatedPlace(
        name="Monson",
        abbreviations=PlaceAbbreviations(
            three_letter="MON",
            five_letter="MONSO",
            seven_letter="MONSON",
            fourteen_letter="MONSON"
        ),
        latitude=37.51613122110285,
        longitude=-104.70416170466603,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    MONTBELLO = PopulatedPlace(
        name="Montbello",
        abbreviations=PlaceAbbreviations(
            three_letter="MON",
            five_letter="MONTB",
            seven_letter="MONTBEL",
            fourteen_letter="MONTBELLO"
        ),
        latitude=39.79360423754787,
        longitude=-104.83359587829835,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    MONTE_VISTA = PopulatedPlace(
        name="Monte Vista",
        abbreviations=PlaceAbbreviations(
            three_letter="MON",
            five_letter="MONTE",
            seven_letter="MONTE V",
            fourteen_letter="MONTE VISTA"
        ),
        latitude=37.57917563945995,
        longitude=-106.14809443786993,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MONTE_VISTA_ESTATES = PopulatedPlace(
        name="Monte Vista Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="MON",
            five_letter="MONTE",
            seven_letter="MONTE V",
            fourteen_letter="MONTE VISTA ES"
        ),
        latitude=39.36527407208155,
        longitude=-104.92138024948406,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    MONTEZUMA = PopulatedPlace(
        name="Montezuma",
        abbreviations=PlaceAbbreviations(
            three_letter="MON",
            five_letter="MONTE",
            seven_letter="MONTEZU",
            fourteen_letter="MONTEZUMA"
        ),
        latitude=39.58110433619612,
        longitude=-105.86724409102396,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    MONTROSE = PopulatedPlace(
        name="Montrose",
        abbreviations=PlaceAbbreviations(
            three_letter="MON",
            five_letter="MONTR",
            seven_letter="MONTROS",
            fourteen_letter="MONTROSE"
        ),
        latitude=38.478325850516626,
        longitude=-107.87618441321172,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    MONUMENT = PopulatedPlace(
        name="Monument",
        abbreviations=PlaceAbbreviations(
            three_letter="MON",
            five_letter="MONUM",
            seven_letter="MONUMEN",
            fourteen_letter="MONUMENT"
        ),
        latitude=39.091664937058795,
        longitude=-104.87276800771542,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    MONUMENT_PARK = PopulatedPlace(
        name="Monument Park",
        abbreviations=PlaceAbbreviations(
            three_letter="MON",
            five_letter="MONUM",
            seven_letter="MONUMEN",
            fourteen_letter="MONUMENT PARK"
        ),
        latitude=37.206967854224615,
        longitude=-105.04640205384936,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MOONRIDGE = PopulatedPlace(
        name="Moonridge",
        abbreviations=PlaceAbbreviations(
            three_letter="MOO",
            five_letter="MOONR",
            seven_letter="MOONRID",
            fourteen_letter="MOONRIDGE"
        ),
        latitude=39.365273758165756,
        longitude=-105.11749849476547,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    MOREY = PopulatedPlace(
        name="Morey",
        abbreviations=PlaceAbbreviations(
            three_letter="MOR",
            five_letter="MOREY",
            seven_letter="MOREY",
            fourteen_letter="MOREY"
        ),
        latitude=40.21749107710946,
        longitude=-105.09277038937813,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MORGAN = PopulatedPlace(
        name="Morgan",
        abbreviations=PlaceAbbreviations(
            three_letter="MOR",
            five_letter="MORGA",
            seven_letter="MORGAN",
            fourteen_letter="MORGAN"
        ),
        latitude=37.32779071160178,
        longitude=-106.020034984863,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MORRISON = PopulatedPlace(
        name="Morrison",
        abbreviations=PlaceAbbreviations(
            three_letter="MOR",
            five_letter="MORRI",
            seven_letter="MORRISO",
            fourteen_letter="MORRISON"
        ),
        latitude=39.65360519299031,
        longitude=-105.19110974506509,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MOSCA = PopulatedPlace(
        name="Mosca",
        abbreviations=PlaceAbbreviations(
            three_letter="MOS",
            five_letter="MOSCA",
            seven_letter="MOSCA",
            fourteen_letter="MOSCA"
        ),
        latitude=37.64834076657752,
        longitude=-105.87392018336601,
        counties=[Counties.ALAMOSA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MOSELEY = PopulatedPlace(
        name="Moseley",
        abbreviations=PlaceAbbreviations(
            three_letter="MOS",
            five_letter="MOSEL",
            seven_letter="MOSELEY",
            fourteen_letter="MOSELEY"
        ),
        latitude=40.24887587573198,
        longitude=-103.7541277793726,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    MOUNT_CRESTED_BUTTE = PopulatedPlace(
        name="Mount Crested Butte",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNT C",
            fourteen_letter="MOUNT CRESTED "
        ),
        latitude=38.90862516936443,
        longitude=-106.96947846189317,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.ASPEN
    )
    MOUNT_HARRIS = PopulatedPlace(
        name="Mount Harris",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNT H",
            fourteen_letter="MOUNT HARRIS"
        ),
        latitude=40.48359206400835,
        longitude=-107.14478868799046,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    MOUNT_LINCOLN = PopulatedPlace(
        name="Mount Lincoln",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNT L",
            fourteen_letter="MOUNT LINCOLN"
        ),
        latitude=39.10609829806225,
        longitude=-108.38343129331872,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    MOUNT_MASSIVE_LAKES = PopulatedPlace(
        name="Mount Massive Lakes",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNT M",
            fourteen_letter="MOUNT MASSIVE "
        ),
        latitude=39.152219748346226,
        longitude=-106.30058944012904,
        counties=[Counties.LAKE],
        nearest_airport=Airports.ASPEN
    )
    MOUNT_OLIVET = PopulatedPlace(
        name="Mount Olivet",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNT O",
            fourteen_letter="MOUNT OLIVET"
        ),
        latitude=39.787493315022175,
        longitude=-105.14221844883986,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MOUNT_PEARL = PopulatedPlace(
        name="Mount Pearl",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNT P",
            fourteen_letter="MOUNT PEARL"
        ),
        latitude=38.96250525597452,
        longitude=-102.78937950452257,
        counties=[Counties.CHEYENNE],
        nearest_airport=Airports.PUEBLO
    )
    MOUNT_VERNON_CLUB_PLACE = PopulatedPlace(
        name="Mount Vernon Club Place",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNT V",
            fourteen_letter="MOUNT VERNON C"
        ),
        latitude=39.722771895898575,
        longitude=-105.29388997625784,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MOUNTAIN_MEADOW_HEIGHTS = PopulatedPlace(
        name="Mountain Meadow Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNTAI",
            fourteen_letter="MOUNTAIN MEADO"
        ),
        latitude=39.66083968583689,
        longitude=-105.30917687334903,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MOUNTAIN_MEADOWS = PopulatedPlace(
        name="Mountain Meadows",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNTAI",
            fourteen_letter="MOUNTAIN MEADO"
        ),
        latitude=40.023881430386666,
        longitude=-105.38055953188774,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    MOUNTAIN_VIEW = PopulatedPlace(
        name="Mountain View",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNTAI",
            fourteen_letter="MOUNTAIN VIEW"
        ),
        latitude=38.30527368639787,
        longitude=-108.48398852566169,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    MOUNTAIN_VIEW = PopulatedPlace(
        name="Mountain View",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNTAI",
            fourteen_letter="MOUNTAIN VIEW"
        ),
        latitude=40.592488924359145,
        longitude=-105.12915694281224,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.MONTROSE
    )
    MOUNTAIN_VIEW = PopulatedPlace(
        name="Mountain View",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNTAI",
            fourteen_letter="MOUNTAIN VIEW"
        ),
        latitude=39.77443751945077,
        longitude=-105.05554902795734,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.MONTROSE
    )
    """
    """
    MOUNTAIN_VIEW_ESTATES = PopulatedPlace(
        name="Mountain View Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNTAI",
            fourteen_letter="MOUNTAIN VIEW "
        ),
        latitude=39.72750640664486,
        longitude=-105.14389904222634,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    MOUNTAIN_VIEW_ESTATES = PopulatedPlace(
        name="Mountain View Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNTAI",
            fourteen_letter="MOUNTAIN VIEW "
        ),
        latitude=39.96945084768856,
        longitude=-105.03001014361877,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    """
    MOUNTAIN_VILLAGE = PopulatedPlace(
        name="Mountain Village",
        abbreviations=PlaceAbbreviations(
            three_letter="MOU",
            five_letter="MOUNT",
            seven_letter="MOUNTAI",
            fourteen_letter="MOUNTAIN VILLA"
        ),
        latitude=37.93138867787246,
        longitude=-107.85646365016862,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    MULESHOE = PopulatedPlace(
        name="Muleshoe",
        abbreviations=PlaceAbbreviations(
            three_letter="MUL",
            five_letter="MULES",
            seven_letter="MULESHO",
            fourteen_letter="MULESHOE"
        ),
        latitude=37.589736601868026,
        longitude=-105.18251172154572,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    MULFORD = PopulatedPlace(
        name="Mulford",
        abbreviations=PlaceAbbreviations(
            three_letter="MUL",
            five_letter="MULFO",
            seven_letter="MULFORD",
            fourteen_letter="MULFORD"
        ),
        latitude=39.408702222552336,
        longitude=-107.16851556350139,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    MUMPER_CORNER = PopulatedPlace(
        name="Mumper Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="MUM",
            five_letter="MUMPE",
            seven_letter="MUMPER ",
            fourteen_letter="MUMPER CORNER"
        ),
        latitude=40.451931636699726,
        longitude=-104.69719722527009,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    MURRAY_PLACE = PopulatedPlace(
        name="Murray Place",
        abbreviations=PlaceAbbreviations(
            three_letter="MUR",
            five_letter="MURRA",
            seven_letter="MURRAY ",
            fourteen_letter="MURRAY PLACE"
        ),
        latitude=37.516130526388736,
        longitude=-102.99715860803059,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    MYSTIC = PopulatedPlace(
        name="Mystic",
        abbreviations=PlaceAbbreviations(
            three_letter="MYS",
            five_letter="MYSTI",
            seven_letter="MYSTIC",
            fourteen_letter="MYSTIC"
        ),
        latitude=40.56998048620102,
        longitude=-106.99589666574093,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    NANTUCKET = PopulatedPlace(
        name="Nantucket",
        abbreviations=PlaceAbbreviations(
            three_letter="NAN",
            five_letter="NANTU",
            seven_letter="NANTUCK",
            fourteen_letter="NANTUCKET"
        ),
        latitude=39.71667312479974,
        longitude=-104.85862117512772,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    NAST = PopulatedPlace(
        name="Nast",
        abbreviations=PlaceAbbreviations(
            three_letter="NAS",
            five_letter="NAST",
            seven_letter="NAST",
            fourteen_letter="NAST"
        ),
        latitude=39.29166014629271,
        longitude=-106.60143152323008,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    NATURITA = PopulatedPlace(
        name="Naturita",
        abbreviations=PlaceAbbreviations(
            three_letter="NAT",
            five_letter="NATUR",
            seven_letter="NATURIT",
            fourteen_letter="NATURITA"
        ),
        latitude=38.21832986920998,
        longitude=-108.56871403449037,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.TELLURIDE
    )
    NEDERLAND = PopulatedPlace(
        name="Nederland",
        abbreviations=PlaceAbbreviations(
            three_letter="NED",
            five_letter="NEDER",
            seven_letter="NEDERLA",
            fourteen_letter="NEDERLAND"
        ),
        latitude=39.96138231263194,
        longitude=-105.51084145463687,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    NEEDLETON = PopulatedPlace(
        name="Needleton",
        abbreviations=PlaceAbbreviations(
            three_letter="NEE",
            five_letter="NEEDL",
            seven_letter="NEEDLET",
            fourteen_letter="NEEDLETON"
        ),
        latitude=37.64056014889263,
        longitude=-107.6914615847702,
        counties=[Counties.SAN_JUAN],
        nearest_airport=Airports.TELLURIDE
    )
    NELSON = PopulatedPlace(
        name="Nelson",
        abbreviations=PlaceAbbreviations(
            three_letter="NEL",
            five_letter="NELSO",
            seven_letter="NELSON",
            fourteen_letter="NELSON"
        ),
        latitude=40.252764282723035,
        longitude=-103.66079205778459,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    NEPESTA = PopulatedPlace(
        name="Nepesta",
        abbreviations=PlaceAbbreviations(
            three_letter="NEP",
            five_letter="NEPES",
            seven_letter="NEPESTA",
            fourteen_letter="NEPESTA"
        ),
        latitude=38.16889925232016,
        longitude=-104.14302864113091,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    NEVADAVILLE = PopulatedPlace(
        name="Nevadaville",
        abbreviations=PlaceAbbreviations(
            three_letter="NEV",
            five_letter="NEVAD",
            seven_letter="NEVADAV",
            fourteen_letter="NEVADAVILLE"
        ),
        latitude=39.79527198870727,
        longitude=-105.53250803955223,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    NEW_CASTLE = PopulatedPlace(
        name="New Castle",
        abbreviations=PlaceAbbreviations(
            three_letter="NEW",
            five_letter="NEW C",
            seven_letter="NEW CAS",
            fourteen_letter="NEW CASTLE"
        ),
        latitude=39.57276471783331,
        longitude=-107.53645496394358,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    NEW_HAVEN = PopulatedPlace(
        name="New Haven",
        abbreviations=PlaceAbbreviations(
            three_letter="NEW",
            five_letter="NEW H",
            seven_letter="NEW HAV",
            fourteen_letter="NEW HAVEN"
        ),
        latitude=40.483050272201524,
        longitude=-102.83632398803348,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    NEW_RAYMER = PopulatedPlace(
        name="New Raymer",
        abbreviations=PlaceAbbreviations(
            three_letter="NEW",
            five_letter="NEW R",
            seven_letter="NEW RAY",
            fourteen_letter="NEW RAYMER"
        ),
        latitude=40.60665961988332,
        longitude=-103.84384894346363,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    NEWETT = PopulatedPlace(
        name="Newett",
        abbreviations=PlaceAbbreviations(
            three_letter="NEW",
            five_letter="NEWET",
            seven_letter="NEWETT",
            fourteen_letter="NEWETT"
        ),
        latitude=38.8666682305917,
        longitude=-105.98891243772135,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.ASPEN
    )
    NIGHTHAWK = PopulatedPlace(
        name="Nighthawk",
        abbreviations=PlaceAbbreviations(
            three_letter="NIG",
            five_letter="NIGHT",
            seven_letter="NIGHTHA",
            fourteen_letter="NIGHTHAWK"
        ),
        latitude=39.35471815314207,
        longitude=-105.16944500528939,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    NINAVIEW = PopulatedPlace(
        name="Ninaview",
        abbreviations=PlaceAbbreviations(
            three_letter="NIN",
            five_letter="NINAV",
            seven_letter="NINAVIE",
            fourteen_letter="NINAVIEW"
        ),
        latitude=37.64390663077961,
        longitude=-103.240776177665,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    """
    NINEMILE_CORNER = PopulatedPlace(
        name="Ninemile Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="NIN",
            five_letter="NINEM",
            seven_letter="NINEMIL",
            fourteen_letter="NINEMILE CORNE"
        ),
        latitude=40.146377072895575,
        longitude=-103.58440032674628,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    NINEMILE_CORNER = PopulatedPlace(
        name="Ninemile Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="NIN",
            five_letter="NINEM",
            seven_letter="NINEMIL",
            fourteen_letter="NINEMILE CORNE"
        ),
        latitude=40.01526904872003,
        longitude=-105.10360526736235,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    NINEMILE_CORNER = PopulatedPlace(
        name="Ninemile Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="NIN",
            five_letter="NINEM",
            seven_letter="NINEMIL",
            fourteen_letter="NINEMILE CORNE"
        ),
        latitude=40.11610045454859,
        longitude=-103.79273777272931,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    """
    NIWOT = PopulatedPlace(
        name="Niwot",
        abbreviations=PlaceAbbreviations(
            three_letter="NIW",
            five_letter="NIWOT",
            seven_letter="NIWOT",
            fourteen_letter="NIWOT"
        ),
        latitude=40.10388045627434,
        longitude=-105.17082949329682,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    NO_NAME = PopulatedPlace(
        name="No Name",
        abbreviations=PlaceAbbreviations(
            three_letter="NO ",
            five_letter="NO NA",
            seven_letter="NO NAME",
            fourteen_letter="NO NAME"
        ),
        latitude=39.56110623399451,
        longitude=-107.29311060881798,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    NOEL = PopulatedPlace(
        name="Noel",
        abbreviations=PlaceAbbreviations(
            three_letter="NOE",
            five_letter="NOEL",
            seven_letter="NOEL",
            fourteen_letter="NOEL"
        ),
        latitude=38.099719396871706,
        longitude=-107.91285278072672,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    NOLAND = PopulatedPlace(
        name="Noland",
        abbreviations=PlaceAbbreviations(
            three_letter="NOL",
            five_letter="NOLAN",
            seven_letter="NOLAND",
            fourteen_letter="NOLAND"
        ),
        latitude=40.25915847121695,
        longitude=-105.25444293092283,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    NORFOLK = PopulatedPlace(
        name="Norfolk",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORFO",
            seven_letter="NORFOLK",
            fourteen_letter="NORFOLK"
        ),
        latitude=40.91082377939426,
        longitude=-104.96970364605795,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    NORFOLK_GLEN = PopulatedPlace(
        name="Norfolk Glen",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORFO",
            seven_letter="NORFOLK",
            fourteen_letter="NORFOLK GLEN"
        ),
        latitude=39.74361753255431,
        longitude=-104.80001006530773,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    NORMANDY_ESTATES = PopulatedPlace(
        name="Normandy Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORMA",
            seven_letter="NORMAND",
            fourteen_letter="NORMANDY ESTAT"
        ),
        latitude=39.58750639344578,
        longitude=-105.06056570739065,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    NORTH_AVONDALE = PopulatedPlace(
        name="North Avondale",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORTH",
            seven_letter="NORTH A",
            fourteen_letter="NORTH AVONDALE"
        ),
        latitude=38.261952652456785,
        longitude=-104.3460886977204,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    NORTH_CREEDE = PopulatedPlace(
        name="North Creede",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORTH",
            seven_letter="NORTH C",
            fourteen_letter="NORTH CREEDE"
        ),
        latitude=37.86417192921442,
        longitude=-106.92588923986727,
        counties=[Counties.MINERAL],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    NORTH_DELTA = PopulatedPlace(
        name="North Delta",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORTH",
            seven_letter="NORTH D",
            fourteen_letter="NORTH DELTA"
        ),
        latitude=38.75860097406269,
        longitude=-108.06924678662756,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    NORTH_GREEN_VALLEY = PopulatedPlace(
        name="North Green Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORTH",
            seven_letter="NORTH G",
            fourteen_letter="NORTH GREEN VA"
        ),
        latitude=39.78083971682639,
        longitude=-105.10195453936592,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    NORTH_WASHINGTON = PopulatedPlace(
        name="North Washington",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORTH",
            seven_letter="NORTH W",
            fourteen_letter="NORTH WASHINGT"
        ),
        latitude=39.80721492928507,
        longitude=-104.97887941386568,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    NORTHBOROUGH_HEIGHTS = PopulatedPlace(
        name="Northborough Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORTH",
            seven_letter="NORTHBO",
            fourteen_letter="NORTHBOROUGH H"
        ),
        latitude=39.8791731359475,
        longitude=-105.02001013201186,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    NORTHDALE = PopulatedPlace(
        name="Northdale",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORTH",
            seven_letter="NORTHDA",
            fourteen_letter="NORTHDALE"
        ),
        latitude=37.809440885087895,
        longitude=-109.01678648653404,
        counties=[Counties.DOLORES],
        nearest_airport=Airports.CORTEZ
    )
    NORTHGATE = PopulatedPlace(
        name="Northgate",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORTH",
            seven_letter="NORTHGA",
            fourteen_letter="NORTHGATE"
        ),
        latitude=40.88581447860287,
        longitude=-106.29420234749205,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    NORTHGLENN = PopulatedPlace(
        name="Northglenn",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORTH",
            seven_letter="NORTHGL",
            fourteen_letter="NORTHGLENN"
        ),
        latitude=39.885547439134484,
        longitude=-104.98721272543037,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    NORTHMOOR = PopulatedPlace(
        name="Northmoor",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORTH",
            seven_letter="NORTHMO",
            fourteen_letter="NORTHMOOR"
        ),
        latitude=39.93972864283836,
        longitude=-105.05612124760682,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    NORTHWOOD_ACRES = PopulatedPlace(
        name="Northwood Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORTH",
            seven_letter="NORTHWO",
            fourteen_letter="NORTHWOOD ACRE"
        ),
        latitude=39.836117519574884,
        longitude=-105.1694545615673,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    NORWOOD = PopulatedPlace(
        name="Norwood",
        abbreviations=PlaceAbbreviations(
            three_letter="NOR",
            five_letter="NORWO",
            seven_letter="NORWOOD",
            fourteen_letter="NORWOOD"
        ),
        latitude=38.130552075579885,
        longitude=-108.29231436556671,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    NUCLA = PopulatedPlace(
        name="Nucla",
        abbreviations=PlaceAbbreviations(
            three_letter="NUC",
            five_letter="NUCLA",
            seven_letter="NUCLA",
            fourteen_letter="NUCLA"
        ),
        latitude=38.26944067707865,
        longitude=-108.54787983570384,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    NUGGET = PopulatedPlace(
        name="Nugget",
        abbreviations=PlaceAbbreviations(
            three_letter="NUG",
            five_letter="NUGGE",
            seven_letter="NUGGET",
            fourteen_letter="NUGGET"
        ),
        latitude=39.86360479444323,
        longitude=-105.58834386089586,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    NUNN = PopulatedPlace(
        name="Nunn",
        abbreviations=PlaceAbbreviations(
            three_letter="NUN",
            five_letter="NUNN",
            seven_letter="NUNN",
            fourteen_letter="NUNN"
        ),
        latitude=40.703598265179835,
        longitude=-104.78081257630754,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    NUTRIA = PopulatedPlace(
        name="Nutria",
        abbreviations=PlaceAbbreviations(
            three_letter="NUT",
            five_letter="NUTRI",
            seven_letter="NUTRIA",
            fourteen_letter="NUTRIA"
        ),
        latitude=37.230843728255365,
        longitude=-107.1256078196198,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    NYBERG = PopulatedPlace(
        name="Nyberg",
        abbreviations=PlaceAbbreviations(
            three_letter="NYB",
            five_letter="NYBER",
            seven_letter="NYBERG",
            fourteen_letter="NYBERG"
        ),
        latitude=38.26834165029885,
        longitude=-104.39803411050298,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    OAK_CREEK = PopulatedPlace(
        name="Oak Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="OAK",
            five_letter="OAK C",
            seven_letter="OAK CRE",
            fourteen_letter="OAK CREEK"
        ),
        latitude=40.27498695093249,
        longitude=-106.95839352078178,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    OAK_GROVE = PopulatedPlace(
        name="Oak Grove",
        abbreviations=PlaceAbbreviations(
            three_letter="OAK",
            five_letter="OAK G",
            seven_letter="OAK GRO",
            fourteen_letter="OAK GROVE"
        ),
        latitude=38.459992844098224,
        longitude=-107.92813062279993,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    OAK_PARK = PopulatedPlace(
        name="Oak Park",
        abbreviations=PlaceAbbreviations(
            three_letter="OAK",
            five_letter="OAK P",
            seven_letter="OAK PAR",
            fourteen_letter="OAK PARK"
        ),
        latitude=39.8358397227845,
        longitude=-105.12112125028773,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    OBERON_ACRES = PopulatedPlace(
        name="Oberon Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="OBE",
            five_letter="OBERO",
            seven_letter="OBERON ",
            fourteen_letter="OBERON ACRES"
        ),
        latitude=39.83917312389008,
        longitude=-105.1155657487705,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    OCCIDENTAL = PopulatedPlace(
        name="Occidental",
        abbreviations=PlaceAbbreviations(
            three_letter="OCC",
            five_letter="OCCID",
            seven_letter="OCCIDEN",
            fourteen_letter="OCCIDENTAL"
        ),
        latitude=37.51501639590822,
        longitude=-105.10695449666025,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    OEHLMANN_PARK = PopulatedPlace(
        name="Oehlmann Park",
        abbreviations=PlaceAbbreviations(
            three_letter="OEH",
            five_letter="OEHLM",
            seven_letter="OEHLMAN",
            fourteen_letter="OEHLMANN PARK"
        ),
        latitude=39.51888356992691,
        longitude=-105.2591684448131,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    OFFIELD_PLACE = PopulatedPlace(
        name="Offield Place",
        abbreviations=PlaceAbbreviations(
            three_letter="OFF",
            five_letter="OFFIE",
            seven_letter="OFFIELD",
            fourteen_letter="OFFIELD PLACE"
        ),
        latitude=40.985801612853095,
        longitude=-108.66317598742478,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    OHIO = PopulatedPlace(
        name="Ohio",
        abbreviations=PlaceAbbreviations(
            three_letter="OHI",
            five_letter="OHIO",
            seven_letter="OHIO",
            fourteen_letter="OHIO"
        ),
        latitude=38.56666634734381,
        longitude=-106.61170914480243,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    OLATHE = PopulatedPlace(
        name="Olathe",
        abbreviations=PlaceAbbreviations(
            three_letter="OLA",
            five_letter="OLATH",
            seven_letter="OLATHE",
            fourteen_letter="OLATHE"
        ),
        latitude=38.60499145983238,
        longitude=-107.98229905060197,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    OLD_FORT_LYONS = PopulatedPlace(
        name="Old Fort Lyons",
        abbreviations=PlaceAbbreviations(
            three_letter="OLD",
            five_letter="OLD F",
            seven_letter="OLD FOR",
            fourteen_letter="OLD FORT LYONS"
        ),
        latitude=38.095847627663204,
        longitude=-102.77270661115256,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    OLD_HOMESTEAD = PopulatedPlace(
        name="Old Homestead",
        abbreviations=PlaceAbbreviations(
            three_letter="OLD",
            five_letter="OLD H",
            seven_letter="OLD HOM",
            fourteen_letter="OLD HOMESTEAD"
        ),
        latitude=40.440266131403575,
        longitude=-106.14364435732728,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    OLD_ROACH = PopulatedPlace(
        name="Old Roach",
        abbreviations=PlaceAbbreviations(
            three_letter="OLD",
            five_letter="OLD R",
            seven_letter="OLD ROA",
            fourteen_letter="OLD ROACH"
        ),
        latitude=40.924426696632736,
        longitude=-106.11724911262161,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    OLD_TOWNE = PopulatedPlace(
        name="Old Towne",
        abbreviations=PlaceAbbreviations(
            three_letter="OLD",
            five_letter="OLD T",
            seven_letter="OLD TOW",
            fourteen_letter="OLD TOWNE"
        ),
        latitude=39.71278422511,
        longitude=-104.85112117315998,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    OLD_WELLS = PopulatedPlace(
        name="Old Wells",
        abbreviations=PlaceAbbreviations(
            three_letter="OLD",
            five_letter="OLD W",
            seven_letter="OLD WEL",
            fourteen_letter="OLD WELLS"
        ),
        latitude=38.90001127683075,
        longitude=-102.32630828731999,
        counties=[Counties.CHEYENNE],
        nearest_airport=Airports.PUEBLO
    )
    OLINGER_GARDENS = PopulatedPlace(
        name="Olinger Gardens",
        abbreviations=PlaceAbbreviations(
            three_letter="OLI",
            five_letter="OLING",
            seven_letter="OLINGER",
            fourteen_letter="OLINGER GARDEN"
        ),
        latitude=39.756950816730466,
        longitude=-105.0569545257627,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    OLNEY_SPRINGS = PopulatedPlace(
        name="Olney Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="OLN",
            five_letter="OLNEY",
            seven_letter="OLNEY S",
            fourteen_letter="OLNEY SPRINGS"
        ),
        latitude=38.1661224647267,
        longitude=-103.94468889449121,
        counties=[Counties.CROWLEY],
        nearest_airport=Airports.PUEBLO
    )
    OLYMPUS_HEIGHTS = PopulatedPlace(
        name="Olympus Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="OLY",
            five_letter="OLYMP",
            seven_letter="OLYMPUS",
            fourteen_letter="OLYMPUS HEIGHT"
        ),
        latitude=40.3777679708856,
        longitude=-105.48389599900611,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    OMEGA = PopulatedPlace(
        name="Omega",
        abbreviations=PlaceAbbreviations(
            three_letter="OME",
            five_letter="OMEGA",
            seven_letter="OMEGA",
            fourteen_letter="OMEGA"
        ),
        latitude=40.53971132160257,
        longitude=-105.08054462558516,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    OPHIR = PopulatedPlace(
        name="Ophir",
        abbreviations=PlaceAbbreviations(
            three_letter="OPH",
            five_letter="OPHIR",
            seven_letter="OPHIR",
            fourteen_letter="OPHIR"
        ),
        latitude=37.85694516957318,
        longitude=-107.83257493776938,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    OPHIR_LOOP = PopulatedPlace(
        name="Ophir Loop",
        abbreviations=PlaceAbbreviations(
            three_letter="OPH",
            five_letter="OPHIR",
            seven_letter="OPHIR L",
            fourteen_letter="OPHIR LOOP"
        ),
        latitude=37.85972276749055,
        longitude=-107.86840934530727,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    ORCHARD_CITY = PopulatedPlace(
        name="Orchard City",
        abbreviations=PlaceAbbreviations(
            three_letter="ORC",
            five_letter="ORCHA",
            seven_letter="ORCHARD",
            fourteen_letter="ORCHARD CITY"
        ),
        latitude=38.82832219044815,
        longitude=-107.97091017259896,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    ORCHARD_MESA = PopulatedPlace(
        name="Orchard Mesa",
        abbreviations=PlaceAbbreviations(
            three_letter="ORC",
            five_letter="ORCHA",
            seven_letter="ORCHARD",
            fourteen_letter="ORCHARD MESA"
        ),
        latitude=39.04304357747287,
        longitude=-108.55232612355934,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    ORCHARD_PARK = PopulatedPlace(
        name="Orchard Park",
        abbreviations=PlaceAbbreviations(
            three_letter="ORC",
            five_letter="ORCHA",
            seven_letter="ORCHARD",
            fourteen_letter="ORCHARD PARK"
        ),
        latitude=38.47222582550154,
        longitude=-105.2283325222308,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ORDWAY = PopulatedPlace(
        name="Ordway",
        abbreviations=PlaceAbbreviations(
            three_letter="ORD",
            five_letter="ORDWA",
            seven_letter="ORDWAY",
            fourteen_letter="ORDWAY"
        ),
        latitude=38.21806708393126,
        longitude=-103.7560702559187,
        counties=[Counties.CROWLEY],
        nearest_airport=Airports.PUEBLO
    )
    ORMEGA = PopulatedPlace(
        name="Ormega",
        abbreviations=PlaceAbbreviations(
            three_letter="ORM",
            five_letter="ORMEG",
            seven_letter="ORMEGA",
            fourteen_letter="ORMEGA"
        ),
        latitude=37.96084895675892,
        longitude=-103.5863433898923,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    ORODELL = PopulatedPlace(
        name="Orodell",
        abbreviations=PlaceAbbreviations(
            three_letter="ORO",
            five_letter="ORODE",
            seven_letter="ORODELL",
            fourteen_letter="ORODELL"
        ),
        latitude=40.01499233291844,
        longitude=-105.3252799186219,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ORR = PopulatedPlace(
        name="Orr",
        abbreviations=PlaceAbbreviations(
            three_letter="ORR",
            five_letter="ORR",
            seven_letter="ORR",
            fourteen_letter="ORR"
        ),
        latitude=38.10751338153028,
        longitude=-103.53522899240949,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    ORSA = PopulatedPlace(
        name="Orsa",
        abbreviations=PlaceAbbreviations(
            three_letter="ORS",
            five_letter="ORSA",
            seven_letter="ORSA",
            fourteen_letter="ORSA"
        ),
        latitude=39.422217980255425,
        longitude=-104.91387965462815,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    ORTIZ = PopulatedPlace(
        name="Ortiz",
        abbreviations=PlaceAbbreviations(
            three_letter="ORT",
            five_letter="ORTIZ",
            seven_letter="ORTIZ",
            fourteen_letter="ORTIZ"
        ),
        latitude=37.004186363500935,
        longitude=-106.04419845866994,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    OSIER = PopulatedPlace(
        name="Osier",
        abbreviations=PlaceAbbreviations(
            three_letter="OSI",
            five_letter="OSIER",
            seven_letter="OSIER",
            fourteen_letter="OSIER"
        ),
        latitude=37.013350446278196,
        longitude=-106.33642922498228,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    OTIS = PopulatedPlace(
        name="Otis",
        abbreviations=PlaceAbbreviations(
            three_letter="OTI",
            five_letter="OTIS",
            seven_letter="OTIS",
            fourteen_letter="OTIS"
        ),
        latitude=40.148878816009756,
        longitude=-102.96300237920752,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    OURAY = PopulatedPlace(
        name="Ouray",
        abbreviations=PlaceAbbreviations(
            three_letter="OUR",
            five_letter="OURAY",
            seven_letter="OURAY",
            fourteen_letter="OURAY"
        ),
        latitude=38.02277760272227,
        longitude=-107.67145921964857,
        counties=[Counties.OURAY],
        nearest_airport=Airports.TELLURIDE
    )
    OVID = PopulatedPlace(
        name="Ovid",
        abbreviations=PlaceAbbreviations(
            three_letter="OVI",
            five_letter="OVID",
            seven_letter="OVID",
            fourteen_letter="OVID"
        ),
        latitude=40.9605541713928,
        longitude=-102.38797433745265,
        counties=[Counties.SEDGWICK],
        nearest_airport=Airports.DENVER
    )
    OWL_CANYON = PopulatedPlace(
        name="Owl Canyon",
        abbreviations=PlaceAbbreviations(
            three_letter="OWL",
            five_letter="OWL C",
            seven_letter="OWL CAN",
            fourteen_letter="OWL CANYON"
        ),
        latitude=40.76248814417107,
        longitude=-105.17554567548791,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    OXFORD = PopulatedPlace(
        name="Oxford",
        abbreviations=PlaceAbbreviations(
            three_letter="OXF",
            five_letter="OXFOR",
            seven_letter="OXFORD",
            fourteen_letter="OXFORD"
        ),
        latitude=37.1688981826004,
        longitude=-107.71423814152524,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    OXYOKE = PopulatedPlace(
        name="Oxyoke",
        abbreviations=PlaceAbbreviations(
            three_letter="OXY",
            five_letter="OXYOK",
            seven_letter="OXYOKE",
            fourteen_letter="OXYOKE"
        ),
        latitude=39.30305194437426,
        longitude=-105.19833550664794,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PACTOLUS = PopulatedPlace(
        name="Pactolus",
        abbreviations=PlaceAbbreviations(
            three_letter="PAC",
            five_letter="PACTO",
            seven_letter="PACTOLU",
            fourteen_letter="PACTOLUS"
        ),
        latitude=39.917771209386444,
        longitude=-105.46445083909236,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PADRONI = PopulatedPlace(
        name="Padroni",
        abbreviations=PlaceAbbreviations(
            three_letter="PAD",
            five_letter="PADRO",
            seven_letter="PADRONI",
            fourteen_letter="PADRONI"
        ),
        latitude=40.77777188996856,
        longitude=-103.17271360438144,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    PAGODA = PopulatedPlace(
        name="Pagoda",
        abbreviations=PlaceAbbreviations(
            three_letter="PAG",
            five_letter="PAGOD",
            seven_letter="PAGODA",
            fourteen_letter="PAGODA"
        ),
        latitude=40.33692622539405,
        longitude=-107.41590432986891,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    PAGOSA_JUNCTION = PopulatedPlace(
        name="Pagosa Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="PAG",
            five_letter="PAGOS",
            seven_letter="PAGOSA ",
            fourteen_letter="PAGOSA JUNCTIO"
        ),
        latitude=37.03806769682154,
        longitude=-107.19921891720566,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    PAGOSA_SPRINGS = PopulatedPlace(
        name="Pagosa Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="PAG",
            five_letter="PAGOS",
            seven_letter="PAGOSA ",
            fourteen_letter="PAGOSA SPRINGS"
        ),
        latitude=37.269455940850605,
        longitude=-107.00977199870368,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    PAISAJE = PopulatedPlace(
        name="Paisaje",
        abbreviations=PlaceAbbreviations(
            three_letter="PAI",
            five_letter="PAISA",
            seven_letter="PAISAJE",
            fourteen_letter="PAISAJE"
        ),
        latitude=37.06779587120451,
        longitude=-106.06058876810283,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    PALISADE = PopulatedPlace(
        name="Palisade",
        abbreviations=PlaceAbbreviations(
            three_letter="PAL",
            five_letter="PALIS",
            seven_letter="PALISAD",
            fourteen_letter="PALISADE"
        ),
        latitude=39.11026490084913,
        longitude=-108.35093008733753,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    PALMER_LAKE = PopulatedPlace(
        name="Palmer Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="PAL",
            five_letter="PALME",
            seven_letter="PALMER ",
            fourteen_letter="PALMER LAKE"
        ),
        latitude=39.12222013829518,
        longitude=-104.9172140212998,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PALOS_VERDES = PopulatedPlace(
        name="Palos Verdes",
        abbreviations=PlaceAbbreviations(
            three_letter="PAL",
            five_letter="PALOS",
            seven_letter="PALOS V",
            fourteen_letter="PALOS VERDES"
        ),
        latitude=39.605839705446215,
        longitude=-104.91834337608844,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    PANDO = PopulatedPlace(
        name="Pando",
        abbreviations=PlaceAbbreviations(
            three_letter="PAN",
            five_letter="PANDO",
            seven_letter="PANDO",
            fourteen_letter="PANDO"
        ),
        latitude=39.4572152875005,
        longitude=-106.33364848193543,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.ASPEN
    )
    PANDORA = PopulatedPlace(
        name="Pandora",
        abbreviations=PlaceAbbreviations(
            three_letter="PAN",
            five_letter="PANDO",
            seven_letter="PANDORA",
            fourteen_letter="PANDORA"
        ),
        latitude=37.933333382617604,
        longitude=-107.78562833513251,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    PANORAMA_HEIGHTS = PopulatedPlace(
        name="Panorama Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="PAN",
            five_letter="PANOR",
            seven_letter="PANORAM",
            fourteen_letter="PANORAMA HEIGH"
        ),
        latitude=39.72222859892207,
        longitude=-105.24028796409021,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    PAOLI = PopulatedPlace(
        name="Paoli",
        abbreviations=PlaceAbbreviations(
            three_letter="PAO",
            five_letter="PAOLI",
            seven_letter="PAOLI",
            fourteen_letter="PAOLI"
        ),
        latitude=40.612220016848596,
        longitude=-102.47269891562667,
        counties=[Counties.PHILLIPS],
        nearest_airport=Airports.DENVER
    )
    PAONIA = PopulatedPlace(
        name="Paonia",
        abbreviations=PlaceAbbreviations(
            three_letter="PAO",
            five_letter="PAONI",
            seven_letter="PAONIA",
            fourteen_letter="PAONIA"
        ),
        latitude=38.86832652169471,
        longitude=-107.59201229497279,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    PAPETON = PopulatedPlace(
        name="Papeton",
        abbreviations=PlaceAbbreviations(
            three_letter="PAP",
            five_letter="PAPET",
            seven_letter="PAPETON",
            fourteen_letter="PAPETON"
        ),
        latitude=38.87638841099397,
        longitude=-104.80192966805186,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PARACHUTE = PopulatedPlace(
        name="Parachute",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARAC",
            seven_letter="PARACHU",
            fourteen_letter="PARACHUTE"
        ),
        latitude=39.45192866577594,
        longitude=-108.05286366281877,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    PARADISE_ACRES = PopulatedPlace(
        name="Paradise Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARAD",
            seven_letter="PARADIS",
            fourteen_letter="PARADISE ACRES"
        ),
        latitude=39.82889532364521,
        longitude=-105.10056574483491,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    PARADISE_HILLS = PopulatedPlace(
        name="Paradise Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARAD",
            seven_letter="PARADIS",
            fourteen_letter="PARADISE HILLS"
        ),
        latitude=39.712493997262584,
        longitude=-105.25166666597761,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    PARADOX = PopulatedPlace(
        name="Paradox",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARAD",
            seven_letter="PARADOX",
            fourteen_letter="PARADOX"
        ),
        latitude=38.3683284622137,
        longitude=-108.96233863506791,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    PARAMOUNT_HEIGHTS = PopulatedPlace(
        name="Paramount Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARAM",
            seven_letter="PARAMOU",
            fourteen_letter="PARAMOUNT HEIG"
        ),
        latitude=39.75778421271713,
        longitude=-105.1141768392551,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    PARK_CENTER = PopulatedPlace(
        name="Park Center",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARK ",
            seven_letter="PARK CE",
            fourteen_letter="PARK CENTER"
        ),
        latitude=38.47778152776385,
        longitude=-105.20610961784655,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PARK_EAST = PopulatedPlace(
        name="Park East",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARK ",
            seven_letter="PARK EA",
            fourteen_letter="PARK EAST"
        ),
        latitude=39.72167312595667,
        longitude=-104.85306567450891,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    PARK_MEADOWS = PopulatedPlace(
        name="Park Meadows",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARK ",
            seven_letter="PARK ME",
            fourteen_letter="PARK MEADOWS"
        ),
        latitude=39.56288940251295,
        longitude=-104.87634006232298,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    PARK_SLOPE = PopulatedPlace(
        name="Park Slope",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARK ",
            seven_letter="PARK SL",
            fourteen_letter="PARK SLOPE"
        ),
        latitude=39.79333971934568,
        longitude=-105.09084343841505,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    PARK_VIEW = PopulatedPlace(
        name="Park View",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARK ",
            seven_letter="PARK VI",
            fourteen_letter="PARK VIEW"
        ),
        latitude=39.61278421810107,
        longitude=-104.74973223830625,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    PARK_VIEW_ESTATES = PopulatedPlace(
        name="Park View Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARK ",
            seven_letter="PARK VI",
            fourteen_letter="PARK VIEW ESTA"
        ),
        latitude=39.72167312733853,
        longitude=-104.83334336995682,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    PARKBOROUGH = PopulatedPlace(
        name="Parkborough",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARKB",
            seven_letter="PARKBOR",
            fourteen_letter="PARKBOROUGH"
        ),
        latitude=39.61139531828354,
        longitude=-104.73973223568248,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    PARKER = PopulatedPlace(
        name="Parker",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARKE",
            seven_letter="PARKER",
            fourteen_letter="PARKER"
        ),
        latitude=39.51860660437933,
        longitude=-104.76137343061458,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    PARKER_HIGHLANDS = PopulatedPlace(
        name="Parker Highlands",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARKE",
            seven_letter="PARKER ",
            fourteen_letter="PARKER HIGHLAN"
        ),
        latitude=39.47139530524436,
        longitude=-104.65056559892139,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.DENVER
    )
    PARKVILLE = PopulatedPlace(
        name="Parkville",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARKV",
            seven_letter="PARKVIL",
            fourteen_letter="PARKVILLE"
        ),
        latitude=38.22722803390519,
        longitude=-106.10058489428224,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    PARKWAY_ESTATES = PopulatedPlace(
        name="Parkway Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARKW",
            seven_letter="PARKWAY",
            fourteen_letter="PARKWAY ESTATE"
        ),
        latitude=39.83695082663809,
        longitude=-105.07612123937946,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    PARLIN = PopulatedPlace(
        name="Parlin",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARLI",
            seven_letter="PARLIN",
            fourteen_letter="PARLIN"
        ),
        latitude=38.50277563076469,
        longitude=-106.72837956349957,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    PARMA = PopulatedPlace(
        name="Parma",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARMA",
            seven_letter="PARMA",
            fourteen_letter="PARMA"
        ),
        latitude=37.53723104047083,
        longitude=-106.03864690974012,
        counties=[Counties.ALAMOSA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    PARRAS_PLAZA = PopulatedPlace(
        name="Parras Plaza",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARRA",
            seven_letter="PARRAS ",
            fourteen_letter="PARRAS PLAZA"
        ),
        latitude=37.17724715556369,
        longitude=-104.95639792942688,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    PARRISH = PopulatedPlace(
        name="Parrish",
        abbreviations=PlaceAbbreviations(
            three_letter="PAR",
            five_letter="PARRI",
            seven_letter="PARRISH",
            fourteen_letter="PARRISH"
        ),
        latitude=38.121682256187455,
        longitude=-102.38464412099768,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    PATTERSON_CROSSING = PopulatedPlace(
        name="Patterson Crossing",
        abbreviations=PlaceAbbreviations(
            three_letter="PAT",
            five_letter="PATTE",
            seven_letter="PATTERS",
            fourteen_letter="PATTERSON CROS"
        ),
        latitude=37.21752360684803,
        longitude=-104.20831856159504,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    PATTERSON_PLACE = PopulatedPlace(
        name="Patterson Place",
        abbreviations=PlaceAbbreviations(
            three_letter="PAT",
            five_letter="PATTE",
            seven_letter="PATTERS",
            fourteen_letter="PATTERSON PLAC"
        ),
        latitude=39.11388076630186,
        longitude=-107.41756388381305,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.ASPEN
    )
    PAWNEE_HILLS = PopulatedPlace(
        name="Pawnee Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="PAW",
            five_letter="PAWNE",
            seven_letter="PAWNEE ",
            fourteen_letter="PAWNEE HILLS"
        ),
        latitude=39.393061995094115,
        longitude=-104.63834328735396,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.DENVER
    )
    PAYNE = PopulatedPlace(
        name="Payne",
        abbreviations=PlaceAbbreviations(
            three_letter="PAY",
            five_letter="PAYNE",
            seven_letter="PAYNE",
            fourteen_letter="PAYNE"
        ),
        latitude=38.8016561914485,
        longitude=-107.90201895466981,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    PEA_GREEN_CORNER = PopulatedPlace(
        name="Pea Green Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="PEA",
            five_letter="PEA G",
            seven_letter="PEA GRE",
            fourteen_letter="PEA GREEN CORN"
        ),
        latitude=38.64999115828596,
        longitude=-108.09508138018805,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    PEABODYS = PopulatedPlace(
        name="Peabodys",
        abbreviations=PlaceAbbreviations(
            three_letter="PEA",
            five_letter="PEABO",
            seven_letter="PEABODY",
            fourteen_letter="PEABODYS"
        ),
        latitude=39.34805040050975,
        longitude=-105.9272475778564,
        counties=[Counties.PARK],
        nearest_airport=Airports.ASPEN
    )
    PEACEFUL_VALLEY = PopulatedPlace(
        name="Peaceful Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="PEA",
            five_letter="PEACE",
            seven_letter="PEACEFU",
            fourteen_letter="PEACEFUL VALLE"
        ),
        latitude=40.13138083686073,
        longitude=-105.4977860715261,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PEAK_SEVEN_WEST = PopulatedPlace(
        name="Peak Seven West",
        abbreviations=PlaceAbbreviations(
            three_letter="PEA",
            five_letter="PEAK ",
            seven_letter="PEAK SE",
            fourteen_letter="PEAK SEVEN WES"
        ),
        latitude=39.49995731156207,
        longitude=-106.06381632598544,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.ASPEN
    )
    PEAR_PARK = PopulatedPlace(
        name="Pear Park",
        abbreviations=PlaceAbbreviations(
            three_letter="PEA",
            five_letter="PEAR ",
            seven_letter="PEAR PA",
            fourteen_letter="PEAR PARK"
        ),
        latitude=39.070265387145014,
        longitude=-108.4720456090123,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    PEARL = PopulatedPlace(
        name="Pearl",
        abbreviations=PlaceAbbreviations(
            three_letter="PEA",
            five_letter="PEARL",
            seven_letter="PEARL",
            fourteen_letter="PEARL"
        ),
        latitude=40.98525487234514,
        longitude=-106.54698931767552,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    PECKHAM = PopulatedPlace(
        name="Peckham",
        abbreviations=PlaceAbbreviations(
            three_letter="PEC",
            five_letter="PECKH",
            seven_letter="PECKHAM",
            fourteen_letter="PECKHAM"
        ),
        latitude=40.303877213022304,
        longitude=-104.75108951993695,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PECONIC = PopulatedPlace(
        name="Peconic",
        abbreviations=PlaceAbbreviations(
            three_letter="PEC",
            five_letter="PECON",
            seven_letter="PECONIC",
            fourteen_letter="PECONIC"
        ),
        latitude=39.320837750727094,
        longitude=-102.1488060892845,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.PUEBLO
    )
    PEEPLES = PopulatedPlace(
        name="Peeples",
        abbreviations=PlaceAbbreviations(
            three_letter="PEE",
            five_letter="PEEPL",
            seven_letter="PEEPLES",
            fourteen_letter="PEEPLES"
        ),
        latitude=38.82193426388284,
        longitude=-108.34175985225346,
        counties=[Counties.DELTA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    PEETZ = PopulatedPlace(
        name="Peetz",
        abbreviations=PlaceAbbreviations(
            three_letter="PEE",
            five_letter="PEETZ",
            seven_letter="PEETZ",
            fourteen_letter="PEETZ"
        ),
        latitude=40.96277091990271,
        longitude=-103.11243391254868,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    PENROSE = PopulatedPlace(
        name="Penrose",
        abbreviations=PlaceAbbreviations(
            three_letter="PEN",
            five_letter="PENRO",
            seven_letter="PENROSE",
            fourteen_letter="PENROSE"
        ),
        latitude=38.425006332565886,
        longitude=-105.02277237066221,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PEORIA_PARK = PopulatedPlace(
        name="Peoria Park",
        abbreviations=PlaceAbbreviations(
            three_letter="PEO",
            five_letter="PEORI",
            seven_letter="PEORIA ",
            fourteen_letter="PEORIA PARK"
        ),
        latitude=39.678895320186314,
        longitude=-104.85195446928213,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    PERRY_PARK = PopulatedPlace(
        name="Perry Park",
        abbreviations=PlaceAbbreviations(
            three_letter="PER",
            five_letter="PERRY",
            seven_letter="PERRY P",
            fourteen_letter="PERRY PARK"
        ),
        latitude=39.256663850901816,
        longitude=-104.99249445368656,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PHEASANT_RUN = PopulatedPlace(
        name="Pheasant Run",
        abbreviations=PlaceAbbreviations(
            three_letter="PHE",
            five_letter="PHEAS",
            seven_letter="PHEASAN",
            fourteen_letter="PHEASANT RUN"
        ),
        latitude=39.63611751674614,
        longitude=-104.81278785552092,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    PHILLIPSBURG = PopulatedPlace(
        name="Phillipsburg",
        abbreviations=PlaceAbbreviations(
            three_letter="PHI",
            five_letter="PHILL",
            seven_letter="PHILLIP",
            fourteen_letter="PHILLIPSBURG"
        ),
        latitude=39.53832787781232,
        longitude=-105.1869438303928,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    PICTOU = PopulatedPlace(
        name="Pictou",
        abbreviations=PlaceAbbreviations(
            three_letter="PIC",
            five_letter="PICTO",
            seven_letter="PICTOU",
            fourteen_letter="PICTOU"
        ),
        latitude=37.63862943232908,
        longitude=-104.81360884202877,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    PIEDRA = PopulatedPlace(
        name="Piedra",
        abbreviations=PlaceAbbreviations(
            three_letter="PIE",
            five_letter="PIEDR",
            seven_letter="PIEDRA",
            fourteen_letter="PIEDRA"
        ),
        latitude=37.22362041343831,
        longitude=-107.34089166640359,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    PIEPLANT_MILL = PopulatedPlace(
        name="Pieplant Mill",
        abbreviations=PlaceAbbreviations(
            three_letter="PIE",
            five_letter="PIEPL",
            seven_letter="PIEPLAN",
            fourteen_letter="PIEPLANT MILL"
        ),
        latitude=38.938054701549504,
        longitude=-106.55948477368321,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.ASPEN
    )
    PIERCE = PopulatedPlace(
        name="Pierce",
        abbreviations=PlaceAbbreviations(
            three_letter="PIE",
            five_letter="PIERC",
            seven_letter="PIERCE",
            fourteen_letter="PIERCE"
        ),
        latitude=40.635542557952135,
        longitude=-104.75525596192023,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PIKE_SAN_ISABEL_VILLAGE = PopulatedPlace(
        name="Pike-San Isabel Village",
        abbreviations=PlaceAbbreviations(
            three_letter="PIK",
            five_letter="PIKE-",
            seven_letter="PIKE-SA",
            fourteen_letter="PIKE-SAN ISABE"
        ),
        latitude=39.051942473940926,
        longitude=-105.7205724984426,
        counties=[Counties.PARK],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PIKEVIEW = PopulatedPlace(
        name="Pikeview",
        abbreviations=PlaceAbbreviations(
            three_letter="PIK",
            five_letter="PIKEV",
            seven_letter="PIKEVIE",
            fourteen_letter="PIKEVIEW"
        ),
        latitude=38.91527681515379,
        longitude=-104.82220877716298,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PINE_BROOK_HILL = PopulatedPlace(
        name="Pine Brook Hill",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINE ",
            seven_letter="PINE BR",
            fourteen_letter="PINE BROOK HIL"
        ),
        latitude=40.04999213893808,
        longitude=-105.31472391992276,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PINE_CREST = PopulatedPlace(
        name="Pine Crest",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINE ",
            seven_letter="PINE CR",
            fourteen_letter="PINE CREST"
        ),
        latitude=39.11249803739469,
        longitude=-104.90832481876248,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PINE_GROVE = PopulatedPlace(
        name="Pine Grove",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINE ",
            seven_letter="PINE GR",
            fourteen_letter="PINE GROVE"
        ),
        latitude=39.40999545089062,
        longitude=-105.32389394749595,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    PINE_JUNCTION = PopulatedPlace(
        name="Pine Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINE ",
            seven_letter="PINE JU",
            fourteen_letter="PINE JUNCTION"
        ),
        latitude=39.46610635335702,
        longitude=-105.39583987037906,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    PINE_NOOK = PopulatedPlace(
        name="Pine Nook",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINE ",
            seven_letter="PINE NO",
            fourteen_letter="PINE NOOK"
        ),
        latitude=39.38416256437273,
        longitude=-105.0713855862046,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    """
    PINE_VALLEY = PopulatedPlace(
        name="Pine Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINE ",
            seven_letter="PINE VA",
            fourteen_letter="PINE VALLEY"
        ),
        latitude=39.6928526830518,
        longitude=-105.41067709958514,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.DENVER
    )
    PINE_VALLEY = PopulatedPlace(
        name="Pine Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINE ",
            seven_letter="PINE VA",
            fourteen_letter="PINE VALLEY"
        ),
        latitude=39.525562006242524,
        longitude=-104.74167672625151,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    PINE_VALLEY = PopulatedPlace(
        name="Pine Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINE ",
            seven_letter="PINE VA",
            fourteen_letter="PINE VALLEY"
        ),
        latitude=40.19165814592645,
        longitude=-105.48306347543513,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    """
    PINECLIFFE = PopulatedPlace(
        name="Pinecliffe",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINEC",
            seven_letter="PINECLI",
            fourteen_letter="PINECLIFFE"
        ),
        latitude=39.931937615764014,
        longitude=-105.42833863204442,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PINEWOOD_SPRINGS = PopulatedPlace(
        name="Pinewood Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINEW",
            seven_letter="PINEWOO",
            fourteen_letter="PINEWOOD SPRIN"
        ),
        latitude=40.27332456575789,
        longitude=-105.35666925641988,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PINEY_CREEK = PopulatedPlace(
        name="Piney Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINEY",
            seven_letter="PINEY C",
            fourteen_letter="PINEY CREEK"
        ),
        latitude=39.61750641616783,
        longitude=-104.79167674835315,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    PINEY_CREEK_RANCHES = PopulatedPlace(
        name="Piney Creek Ranches",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINEY",
            seven_letter="PINEY C",
            fourteen_letter="PINEY CREEK RA"
        ),
        latitude=39.59833971518344,
        longitude=-104.76473224044503,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    PINNEO = PopulatedPlace(
        name="Pinneo",
        abbreviations=PlaceAbbreviations(
            three_letter="PIN",
            five_letter="PINNE",
            seven_letter="PINNEO",
            fourteen_letter="PINNEO"
        ),
        latitude=40.20943109229921,
        longitude=-103.43856419971848,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    PITKIN = PopulatedPlace(
        name="Pitkin",
        abbreviations=PlaceAbbreviations(
            three_letter="PIT",
            five_letter="PITKI",
            seven_letter="PITKIN",
            fourteen_letter="PITKIN"
        ),
        latitude=38.60916735946631,
        longitude=-106.51670612848756,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    PITTSBURG = PopulatedPlace(
        name="Pittsburg",
        abbreviations=PlaceAbbreviations(
            three_letter="PIT",
            five_letter="PITTS",
            seven_letter="PITTSBU",
            fourteen_letter="PITTSBURG"
        ),
        latitude=38.952219668884936,
        longitude=-107.06255738837916,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.ASPEN
    )
    """
    PINON = PopulatedPlace(
        name="Piñon",
        abbreviations=PlaceAbbreviations(
            three_letter="PIÑ",
            five_letter="PIÑON",
            seven_letter="PIÑON",
            fourteen_letter="PIÑON"
        ),
        latitude=38.433339760489446,
        longitude=-104.6074824760484,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    PINON = PopulatedPlace(
        name="Piñon",
        abbreviations=PlaceAbbreviations(
            three_letter="PIÑ",
            five_letter="PIÑON",
            seven_letter="PIÑON",
            fourteen_letter="PIÑON"
        ),
        latitude=38.26666238674733,
        longitude=-108.40065200450192,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.PUEBLO
    )
    """
    PINON_ACRES = PopulatedPlace(
        name="Piñon Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="PIÑ",
            five_letter="PIÑON",
            seven_letter="PIÑON A",
            fourteen_letter="PIÑON ACRES"
        ),
        latitude=37.22778678412783,
        longitude=-107.81729726996946,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    PLACERVILLE = PopulatedPlace(
        name="Placerville",
        abbreviations=PlaceAbbreviations(
            three_letter="PLA",
            five_letter="PLACE",
            seven_letter="PLACERV",
            fourteen_letter="PLACERVILLE"
        ),
        latitude=38.016664676468906,
        longitude=-108.05341370216547,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    PLACITA = PopulatedPlace(
        name="Placita",
        abbreviations=PlaceAbbreviations(
            three_letter="PLA",
            five_letter="PLACI",
            seven_letter="PLACITA",
            fourteen_letter="PLACITA"
        ),
        latitude=39.132214979503374,
        longitude=-107.2628388524887,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    PLAINVIEW = PopulatedPlace(
        name="Plainview",
        abbreviations=PlaceAbbreviations(
            three_letter="PLA",
            five_letter="PLAIN",
            seven_letter="PLAINVI",
            fourteen_letter="PLAINVIEW"
        ),
        latitude=39.89360402010254,
        longitude=-105.2763892925401,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    PLATEAU_CITY = PopulatedPlace(
        name="Plateau City",
        abbreviations=PlaceAbbreviations(
            three_letter="PLA",
            five_letter="PLATE",
            seven_letter="PLATEAU",
            fourteen_letter="PLATEAU CITY"
        ),
        latitude=39.23720694297293,
        longitude=-107.98174792159864,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    PLATNER = PopulatedPlace(
        name="Platner",
        abbreviations=PlaceAbbreviations(
            three_letter="PLA",
            five_letter="PLATN",
            seven_letter="PLATNER",
            fourteen_letter="PLATNER"
        ),
        latitude=40.1552669097336,
        longitude=-103.0674481049034,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    PLATORO = PopulatedPlace(
        name="Platoro",
        abbreviations=PlaceAbbreviations(
            three_letter="PLA",
            five_letter="PLATO",
            seven_letter="PLATORO",
            fourteen_letter="PLATORO"
        ),
        latitude=37.35195618273133,
        longitude=-106.53282470114016,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    PLATTE_SPRINGS = PopulatedPlace(
        name="Platte Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="PLA",
            five_letter="PLATT",
            seven_letter="PLATTE ",
            fourteen_letter="PLATTE SPRINGS"
        ),
        latitude=39.06360890013349,
        longitude=-105.35861691624524,
        counties=[Counties.PARK],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PLATTEVILLE = PopulatedPlace(
        name="Platteville",
        abbreviations=PlaceAbbreviations(
            three_letter="PLA",
            five_letter="PLATT",
            seven_letter="PLATTEV",
            fourteen_letter="PLATTEVILLE"
        ),
        latitude=40.21498939606772,
        longitude=-104.8227595261788,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    PLEASANT_VIEW = PopulatedPlace(
        name="Pleasant View",
        abbreviations=PlaceAbbreviations(
            three_letter="PLE",
            five_letter="PLEAS",
            seven_letter="PLEASAN",
            fourteen_letter="PLEASANT VIEW"
        ),
        latitude=39.73416040545544,
        longitude=-105.17166395004233,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    PLEASANT_VIEW = PopulatedPlace(
        name="Pleasant View",
        abbreviations=PlaceAbbreviations(
            three_letter="PLE",
            five_letter="PLEAS",
            seven_letter="PLEASAN",
            fourteen_letter="PLEASANT VIEW"
        ),
        latitude=37.589439872431626,
        longitude=-108.7651116100111,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.DENVER
    )
    """
    PLEASANT_VIEW_RIDGE = PopulatedPlace(
        name="Pleasant View Ridge",
        abbreviations=PlaceAbbreviations(
            three_letter="PLE",
            five_letter="PLEAS",
            seven_letter="PLEASAN",
            fourteen_letter="PLEASANT VIEW "
        ),
        latitude=40.1166576662726,
        longitude=-105.05554726815768,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PLEASANTON = PopulatedPlace(
        name="Pleasanton",
        abbreviations=PlaceAbbreviations(
            three_letter="PLE",
            five_letter="PLEAS",
            seven_letter="PLEASAN",
            fourteen_letter="PLEASANTON"
        ),
        latitude=38.36500387618412,
        longitude=-105.74779342874336,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    PLUMBS = PopulatedPlace(
        name="Plumbs",
        abbreviations=PlaceAbbreviations(
            three_letter="PLU",
            five_letter="PLUMB",
            seven_letter="PLUMBS",
            fourteen_letter="PLUMBS"
        ),
        latitude=40.087768762756866,
        longitude=-105.04388036337087,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PONCHA_SPRINGS = PopulatedPlace(
        name="Poncha Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="PON",
            five_letter="PONCH",
            seven_letter="PONCHA ",
            fourteen_letter="PONCHA SPRINGS"
        ),
        latitude=38.51278137505858,
        longitude=-106.07724861883315,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    PONDEROSA_EAST = PopulatedPlace(
        name="Ponderosa East",
        abbreviations=PlaceAbbreviations(
            three_letter="PON",
            five_letter="PONDE",
            seven_letter="PONDERO",
            fourteen_letter="PONDEROSA EAST"
        ),
        latitude=39.546105513903,
        longitude=-104.67053691197856,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    PONDEROSA_HILLS = PopulatedPlace(
        name="Ponderosa Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="PON",
            five_letter="PONDE",
            seven_letter="PONDERO",
            fourteen_letter="PONDEROSA HILL"
        ),
        latitude=39.54471730970573,
        longitude=-104.73192782610602,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    PONDEROSA_PARK = PopulatedPlace(
        name="Ponderosa Park",
        abbreviations=PlaceAbbreviations(
            three_letter="PON",
            five_letter="PONDE",
            seven_letter="PONDERO",
            fourteen_letter="PONDEROSA PARK"
        ),
        latitude=39.40832839657702,
        longitude=-104.65109309235112,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.DENVER
    )
    """
    PONY_ESTATES = PopulatedPlace(
        name="Pony Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="PON",
            five_letter="PONY ",
            seven_letter="PONY ES",
            fourteen_letter="PONY ESTATES"
        ),
        latitude=39.960839744924044,
        longitude=-105.05695455001717,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    PONY_ESTATES = PopulatedPlace(
        name="Pony Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="PON",
            five_letter="PONY ",
            seven_letter="PONY ES",
            fourteen_letter="PONY ESTATES"
        ),
        latitude=39.96056204495471,
        longitude=-105.05695455001717,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    """
    PORTLAND = PopulatedPlace(
        name="Portland",
        abbreviations=PlaceAbbreviations(
            three_letter="POR",
            five_letter="PORTL",
            seven_letter="PORTLAN",
            fourteen_letter="PORTLAND"
        ),
        latitude=38.39111802719623,
        longitude=-105.02499516739113,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    POUDRE_PARK = PopulatedPlace(
        name="Poudre Park",
        abbreviations=PlaceAbbreviations(
            three_letter="POU",
            five_letter="POUDR",
            seven_letter="POUDRE ",
            fourteen_letter="POUDRE PARK"
        ),
        latitude=40.686099125125,
        longitude=-105.30471809531781,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    POWARS = PopulatedPlace(
        name="Powars",
        abbreviations=PlaceAbbreviations(
            three_letter="POW",
            five_letter="POWAR",
            seven_letter="POWARS",
            fourteen_letter="POWARS"
        ),
        latitude=40.04082327342894,
        longitude=-104.8080376020277,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    POWDER_WASH = PopulatedPlace(
        name="Powder Wash",
        abbreviations=PlaceAbbreviations(
            three_letter="POW",
            five_letter="POWDE",
            seven_letter="POWDER ",
            fourteen_letter="POWDER WASH"
        ),
        latitude=40.94580403495678,
        longitude=-108.311495705553,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    POWDERHORN = PopulatedPlace(
        name="Powderhorn",
        abbreviations=PlaceAbbreviations(
            three_letter="POW",
            five_letter="POWDE",
            seven_letter="POWDERH",
            fourteen_letter="POWDERHORN"
        ),
        latitude=38.27694467545865,
        longitude=-107.09589452074971,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    PRAIRIE_TRAIL_RANCHES = PopulatedPlace(
        name="Prairie Trail Ranches",
        abbreviations=PlaceAbbreviations(
            three_letter="PRA",
            five_letter="PRAIR",
            seven_letter="PRAIRIE",
            fourteen_letter="PRAIRIE TRAIL "
        ),
        latitude=39.46972860609924,
        longitude=-104.6322321949014,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.DENVER
    )
    PRICHETT = PopulatedPlace(
        name="Prichett",
        abbreviations=PlaceAbbreviations(
            three_letter="PRI",
            five_letter="PRICH",
            seven_letter="PRICHET",
            fourteen_letter="PRICHETT"
        ),
        latitude=37.37168841227782,
        longitude=-102.86048896112885,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    PRINCETON = PopulatedPlace(
        name="Princeton",
        abbreviations=PlaceAbbreviations(
            three_letter="PRI",
            five_letter="PRINC",
            seven_letter="PRINCET",
            fourteen_letter="PRINCETON"
        ),
        latitude=38.993333832076246,
        longitude=-106.22003080357666,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.ASPEN
    )
    PRITCHETT = PopulatedPlace(
        name="Pritchett",
        abbreviations=PlaceAbbreviations(
            three_letter="PRI",
            five_letter="PRITC",
            seven_letter="PRITCHE",
            fourteen_letter="PRITCHETT"
        ),
        latitude=37.370299612091685,
        longitude=-102.8596556614134,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    PROCTOR = PopulatedPlace(
        name="Proctor",
        abbreviations=PlaceAbbreviations(
            three_letter="PRO",
            five_letter="PROCT",
            seven_letter="PROCTOR",
            fourteen_letter="PROCTOR"
        ),
        latitude=40.80694140950794,
        longitude=-102.9515957549861,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    PROSPECT_HEIGHTS = PopulatedPlace(
        name="Prospect Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="PRO",
            five_letter="PROSP",
            seven_letter="PROSPEC",
            fourteen_letter="PROSPECT HEIGH"
        ),
        latitude=38.42639321880074,
        longitude=-105.23750011986107,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    PROSPECT_VALLEY = PopulatedPlace(
        name="Prospect Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="PRO",
            five_letter="PROSP",
            seven_letter="PROSPEC",
            fourteen_letter="PROSPECT VALLE"
        ),
        latitude=40.073600304907245,
        longitude=-104.41496561447013,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    PROWERS = PopulatedPlace(
        name="Prowers",
        abbreviations=PlaceAbbreviations(
            three_letter="PRO",
            five_letter="PROWE",
            seven_letter="PROWERS",
            fourteen_letter="PROWERS"
        ),
        latitude=38.08195872601431,
        longitude=-102.767706508331,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    PRYOR = PopulatedPlace(
        name="Pryor",
        abbreviations=PlaceAbbreviations(
            three_letter="PRY",
            five_letter="PRYOR",
            seven_letter="PRYOR",
            fourteen_letter="PRYOR"
        ),
        latitude=37.508075819032854,
        longitude=-104.71416210614171,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    PUEBLO = PopulatedPlace(
        name="Pueblo",
        abbreviations=PlaceAbbreviations(
            three_letter="PUE",
            five_letter="PUEBL",
            seven_letter="PUEBLO",
            fourteen_letter="PUEBLO"
        ),
        latitude=38.25445343479271,
        longitude=-104.60915085773684,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    PUEBLO_WEST = PopulatedPlace(
        name="Pueblo West",
        abbreviations=PlaceAbbreviations(
            three_letter="PUE",
            five_letter="PUEBL",
            seven_letter="PUEBLO ",
            fourteen_letter="PUEBLO WEST"
        ),
        latitude=38.35000784091312,
        longitude=-104.72276449367666,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    PULLIAM = PopulatedPlace(
        name="Pulliam",
        abbreviations=PlaceAbbreviations(
            three_letter="PUL",
            five_letter="PULLI",
            seven_letter="PULLIAM",
            fourteen_letter="PULLIAM"
        ),
        latitude=40.32054530157012,
        longitude=-104.94387486729221,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PULTNEY = PopulatedPlace(
        name="Pultney",
        abbreviations=PlaceAbbreviations(
            three_letter="PUL",
            five_letter="PULTN",
            seven_letter="PULTNEY",
            fourteen_letter="PULTNEY"
        ),
        latitude=38.16223315761374,
        longitude=-104.04774801754542,
        counties=[Counties.CROWLEY],
        nearest_airport=Airports.PUEBLO
    )
    PUNKIN_CENTER = PopulatedPlace(
        name="Punkin Center",
        abbreviations=PlaceAbbreviations(
            three_letter="PUN",
            five_letter="PUNKI",
            seven_letter="PUNKIN ",
            fourteen_letter="PUNKIN CENTER"
        ),
        latitude=38.85194468012878,
        longitude=-103.70051340997986,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.PUEBLO
    )
    PURCELL = PopulatedPlace(
        name="Purcell",
        abbreviations=PlaceAbbreviations(
            three_letter="PUR",
            five_letter="PURCE",
            seven_letter="PURCELL",
            fourteen_letter="PURCELL"
        ),
        latitude=40.63832066924249,
        longitude=-104.60163762627985,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    PURITAN = PopulatedPlace(
        name="Puritan",
        abbreviations=PlaceAbbreviations(
            three_letter="PUR",
            five_letter="PURIT",
            seven_letter="PURITAN",
            fourteen_letter="PURITAN"
        ),
        latitude=40.08499066571147,
        longitude=-104.99915645146177,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    QUAIL_HILL = PopulatedPlace(
        name="Quail Hill",
        abbreviations=PlaceAbbreviations(
            three_letter="QUA",
            five_letter="QUAIL",
            seven_letter="QUAIL H",
            fourteen_letter="QUAIL HILL"
        ),
        latitude=39.96306204905778,
        longitude=-105.00223233779195,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    QUAKER_ACRES = PopulatedPlace(
        name="Quaker Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="QUA",
            five_letter="QUAKE",
            seven_letter="QUAKER ",
            fourteen_letter="QUAKER ACRES"
        ),
        latitude=39.830562018052774,
        longitude=-105.18723236477047,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    QUEENSBOROUGH = PopulatedPlace(
        name="Queensborough",
        abbreviations=PlaceAbbreviations(
            three_letter="QUE",
            five_letter="QUEEN",
            seven_letter="QUEENSB",
            fourteen_letter="QUEENSBOROUGH"
        ),
        latitude=39.70000642337652,
        longitude=-104.8516767721801,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    QUERIDA = PopulatedPlace(
        name="Querida",
        abbreviations=PlaceAbbreviations(
            three_letter="QUE",
            five_letter="QUERI",
            seven_letter="QUERIDA",
            fourteen_letter="QUERIDA"
        ),
        latitude=38.12611866939869,
        longitude=-105.33445271031115,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.PUEBLO
    )
    QUIMBY = PopulatedPlace(
        name="Quimby",
        abbreviations=PlaceAbbreviations(
            three_letter="QUI",
            five_letter="QUIMB",
            seven_letter="QUIMBY",
            fourteen_letter="QUIMBY"
        ),
        latitude=39.87332534093662,
        longitude=-104.94387761344211,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    RAGO = PopulatedPlace(
        name="Rago",
        abbreviations=PlaceAbbreviations(
            three_letter="RAG",
            five_letter="RAGO",
            seven_letter="RAGO",
            fourteen_letter="RAGO"
        ),
        latitude=40.00193536461188,
        longitude=-103.41550737039142,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    RAINBOW_HILLS = PopulatedPlace(
        name="Rainbow Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="RAI",
            five_letter="RAINB",
            seven_letter="RAINBOW",
            fourteen_letter="RAINBOW HILLS"
        ),
        latitude=39.713339690891985,
        longitude=-105.3386212857933,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    RAINBOW_RIDGE = PopulatedPlace(
        name="Rainbow Ridge",
        abbreviations=PlaceAbbreviations(
            three_letter="RAI",
            five_letter="RAINB",
            seven_letter="RAINBOW",
            fourteen_letter="RAINBOW RIDGE"
        ),
        latitude=39.793895316554654,
        longitude=-105.13417684809588,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    RALSTON_ESTATES = PopulatedPlace(
        name="Ralston Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="RAL",
            five_letter="RALST",
            seven_letter="RALSTON",
            fourteen_letter="RALSTON ESTATE"
        ),
        latitude=39.816395318809384,
        longitude=-105.14667685407028,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    RALSTON_VALLEY = PopulatedPlace(
        name="Ralston Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="RAL",
            five_letter="RALST",
            seven_letter="RALSTON",
            fourteen_letter="RALSTON VALLEY"
        ),
        latitude=39.82695081953017,
        longitude=-105.15195455607761,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    RAMAH = PopulatedPlace(
        name="Ramah",
        abbreviations=PlaceAbbreviations(
            three_letter="RAM",
            five_letter="RAMAH",
            seven_letter="RAMAH",
            fourteen_letter="RAMAH"
        ),
        latitude=39.12166178833019,
        longitude=-104.16580384681976,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    RAND = PopulatedPlace(
        name="Rand",
        abbreviations=PlaceAbbreviations(
            three_letter="RAN",
            five_letter="RAND",
            seven_letter="RAND",
            fourteen_letter="RAND"
        ),
        latitude=40.453876730649085,
        longitude=-106.18142326711234,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    RANDALL = PopulatedPlace(
        name="Randall",
        abbreviations=PlaceAbbreviations(
            three_letter="RAN",
            five_letter="RANDA",
            seven_letter="RANDALL",
            fourteen_letter="RANDALL"
        ),
        latitude=38.09556917698768,
        longitude=-103.57967540215088,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    RANGELY = PopulatedPlace(
        name="Rangely",
        abbreviations=PlaceAbbreviations(
            three_letter="RAN",
            five_letter="RANGE",
            seven_letter="RANGELY",
            fourteen_letter="RANGELY"
        ),
        latitude=40.08748209192953,
        longitude=-108.80484020262759,
        counties=[Counties.RIO_BLANCO],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    RAYMER = PopulatedPlace(
        name="Raymer",
        abbreviations=PlaceAbbreviations(
            three_letter="RAY",
            five_letter="RAYME",
            seven_letter="RAYMER",
            fourteen_letter="RAYMER"
        ),
        latitude=40.60804842018672,
        longitude=-103.84246004382982,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    RAYMOND = PopulatedPlace(
        name="Raymond",
        abbreviations=PlaceAbbreviations(
            three_letter="RAY",
            five_letter="RAYMO",
            seven_letter="RAYMOND",
            fourteen_letter="RAYMOND"
        ),
        latitude=40.154991742163475,
        longitude=-105.46445156672775,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    READ = PopulatedPlace(
        name="Read",
        abbreviations=PlaceAbbreviations(
            three_letter="REA",
            five_letter="READ",
            seven_letter="READ",
            fourteen_letter="READ"
        ),
        latitude=38.7661007818931,
        longitude=-107.9761876670953,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    RED_CLIFF = PopulatedPlace(
        name="Red Cliff",
        abbreviations=PlaceAbbreviations(
            three_letter="RED",
            five_letter="RED C",
            seven_letter="RED CLI",
            fourteen_letter="RED CLIFF"
        ),
        latitude=39.51221459248302,
        longitude=-106.36809409673907,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    RED_FEATHER_LAKES = PopulatedPlace(
        name="Red Feather Lakes",
        abbreviations=PlaceAbbreviations(
            three_letter="RED",
            five_letter="RED F",
            seven_letter="RED FEA",
            fourteen_letter="RED FEATHER LA"
        ),
        latitude=40.802487519265696,
        longitude=-105.5916732760536,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    RED_LION = PopulatedPlace(
        name="Red Lion",
        abbreviations=PlaceAbbreviations(
            three_letter="RED",
            five_letter="RED L",
            seven_letter="RED LIO",
            fourteen_letter="RED LION"
        ),
        latitude=40.891664541205955,
        longitude=-102.6768671986294,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    RED_WING = PopulatedPlace(
        name="Red Wing",
        abbreviations=PlaceAbbreviations(
            three_letter="RED",
            five_letter="RED W",
            seven_letter="RED WIN",
            fourteen_letter="RED WING"
        ),
        latitude=37.73612191660828,
        longitude=-105.29001376017993,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    REDLANDS = PopulatedPlace(
        name="Redlands",
        abbreviations=PlaceAbbreviations(
            three_letter="RED",
            five_letter="REDLA",
            seven_letter="REDLAND",
            fourteen_letter="REDLANDS"
        ),
        latitude=39.07887657633677,
        longitude=-108.63566244529324,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    REDMESA = PopulatedPlace(
        name="Redmesa",
        abbreviations=PlaceAbbreviations(
            three_letter="RED",
            five_letter="REDME",
            seven_letter="REDMESA",
            fourteen_letter="REDMESA"
        ),
        latitude=37.0944499437266,
        longitude=-108.17036473299783,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    REDMOND = PopulatedPlace(
        name="Redmond",
        abbreviations=PlaceAbbreviations(
            three_letter="RED",
            five_letter="REDMO",
            seven_letter="REDMOND",
            fourteen_letter="REDMOND"
        ),
        latitude=40.47887811603505,
        longitude=-105.04082160791336,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    REDS_PLACE = PopulatedPlace(
        name="Reds Place",
        abbreviations=PlaceAbbreviations(
            three_letter="RED",
            five_letter="REDS ",
            seven_letter="REDS PL",
            fourteen_letter="REDS PLACE"
        ),
        latitude=40.730541389578605,
        longitude=-105.87168663110828,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    REILLY_CANYON = PopulatedPlace(
        name="Reilly Canyon",
        abbreviations=PlaceAbbreviations(
            three_letter="REI",
            five_letter="REILL",
            seven_letter="REILLY ",
            fourteen_letter="REILLY CANYON"
        ),
        latitude=37.25446768282569,
        longitude=-104.70999918106276,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    RESURRECTION_MILL = PopulatedPlace(
        name="Resurrection Mill",
        abbreviations=PlaceAbbreviations(
            three_letter="RES",
            five_letter="RESUR",
            seven_letter="RESURRE",
            fourteen_letter="RESURRECTION M"
        ),
        latitude=39.23527396117572,
        longitude=-106.27697814365905,
        counties=[Counties.LAKE],
        nearest_airport=Airports.ASPEN
    )
    REX = PopulatedPlace(
        name="Rex",
        abbreviations=PlaceAbbreviations(
            three_letter="REX",
            five_letter="REX",
            seven_letter="REX",
            fourteen_letter="REX"
        ),
        latitude=40.788877347849166,
        longitude=-105.17832337953416,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    RHONE = PopulatedPlace(
        name="Rhone",
        abbreviations=PlaceAbbreviations(
            three_letter="RHO",
            five_letter="RHONE",
            seven_letter="RHONE",
            fourteen_letter="RHONE"
        ),
        latitude=39.126653879440596,
        longitude=-108.6784417597338,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    RICHFIELD = PopulatedPlace(
        name="Richfield",
        abbreviations=PlaceAbbreviations(
            three_letter="RIC",
            five_letter="RICHF",
            seven_letter="RICHFIE",
            fourteen_letter="RICHFIELD"
        ),
        latitude=37.27779230914973,
        longitude=-105.94503296284063,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    RICHLAWN_HILLS = PopulatedPlace(
        name="Richlawn Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="RIC",
            five_letter="RICHL",
            seven_letter="RICHLAW",
            fourteen_letter="RICHLAWN HILLS"
        ),
        latitude=39.4657063954719,
        longitude=-104.78261002883426,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    RICO = PopulatedPlace(
        name="Rico",
        abbreviations=PlaceAbbreviations(
            three_letter="RIC",
            five_letter="RICO",
            seven_letter="RICO",
            fourteen_letter="RICO"
        ),
        latitude=37.69277883455203,
        longitude=-108.03036076344199,
        counties=[Counties.DOLORES],
        nearest_airport=Airports.TELLURIDE
    )
    RIDGEWOOD = PopulatedPlace(
        name="Ridgewood",
        abbreviations=PlaceAbbreviations(
            three_letter="RID",
            five_letter="RIDGE",
            seven_letter="RIDGEWO",
            fourteen_letter="RIDGEWOOD"
        ),
        latitude=39.965826319751045,
        longitude=-105.42361643473424,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    RIDGEWOOD_PARK = PopulatedPlace(
        name="Ridgewood Park",
        abbreviations=PlaceAbbreviations(
            three_letter="RID",
            five_letter="RIDGE",
            seven_letter="RIDGEWO",
            fourteen_letter="RIDGEWOOD PARK"
        ),
        latitude=39.59028419657125,
        longitude=-105.0186211982421,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    RIDGWAY = PopulatedPlace(
        name="Ridgway",
        abbreviations=PlaceAbbreviations(
            three_letter="RID",
            five_letter="RIDGW",
            seven_letter="RIDGWAY",
            fourteen_letter="RIDGWAY"
        ),
        latitude=38.152774514179725,
        longitude=-107.76173685322726,
        counties=[Counties.OURAY],
        nearest_airport=Airports.TELLURIDE
    )
    RIFLE = PopulatedPlace(
        name="Rifle",
        abbreviations=PlaceAbbreviations(
            three_letter="RIF",
            five_letter="RIFLE",
            seven_letter="RIFLE",
            fourteen_letter="RIFLE"
        ),
        latitude=39.53470849550695,
        longitude=-107.7831305137895,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    RINN = PopulatedPlace(
        name="Rinn",
        abbreviations=PlaceAbbreviations(
            three_letter="RIN",
            five_letter="RINN",
            seven_letter="RINN",
            fourteen_letter="RINN"
        ),
        latitude=40.13887957290177,
        longitude=-104.99887835820266,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    RIO_BLANCO = PopulatedPlace(
        name="Rio Blanco",
        abbreviations=PlaceAbbreviations(
            three_letter="RIO",
            five_letter="RIO B",
            seven_letter="RIO BLA",
            fourteen_letter="RIO BLANCO"
        ),
        latitude=39.737760610091755,
        longitude=-107.94536157298057,
        counties=[Counties.RIO_BLANCO],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    RIVA_CHASE = PopulatedPlace(
        name="Riva Chase",
        abbreviations=PlaceAbbreviations(
            three_letter="RIV",
            five_letter="RIVA ",
            seven_letter="RIVA CH",
            fourteen_letter="RIVA CHASE"
        ),
        latitude=39.69611749447546,
        longitude=-105.2572323651699,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    RIVERDALE = PopulatedPlace(
        name="Riverdale",
        abbreviations=PlaceAbbreviations(
            three_letter="RIV",
            five_letter="RIVER",
            seven_letter="RIVERDA",
            fourteen_letter="RIVERDALE"
        ),
        latitude=38.058624488278895,
        longitude=-103.31660983662124,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    """
    RIVERSIDE = PopulatedPlace(
        name="Riverside",
        abbreviations=PlaceAbbreviations(
            three_letter="RIV",
            five_letter="RIVER",
            seven_letter="RIVERSI",
            fourteen_letter="RIVERSIDE"
        ),
        latitude=40.175547246684914,
        longitude=-105.43722836368937,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    RIVERSIDE = PopulatedPlace(
        name="Riverside",
        abbreviations=PlaceAbbreviations(
            three_letter="RIV",
            five_letter="RIVER",
            seven_letter="RIVERSI",
            fourteen_letter="RIVERSIDE"
        ),
        latitude=38.938334426832455,
        longitude=-106.18391858934223,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    RIVERVIEW = PopulatedPlace(
        name="Riverview",
        abbreviations=PlaceAbbreviations(
            three_letter="RIV",
            five_letter="RIVER",
            seven_letter="RIVERVI",
            fourteen_letter="RIVERVIEW"
        ),
        latitude=39.39749545294171,
        longitude=-105.26805913316377,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ROBB = PopulatedPlace(
        name="Robb",
        abbreviations=PlaceAbbreviations(
            three_letter="ROB",
            five_letter="ROBB",
            seven_letter="ROBB",
            fourteen_letter="ROBB"
        ),
        latitude=40.10249564978278,
        longitude=-102.37187483154207,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    ROBERTA = PopulatedPlace(
        name="Roberta",
        abbreviations=PlaceAbbreviations(
            three_letter="ROB",
            five_letter="ROBER",
            seven_letter="ROBERTA",
            fourteen_letter="ROBERTA"
        ),
        latitude=37.9964040564314,
        longitude=-103.67579141403479,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    ROBINSON_PLACE = PopulatedPlace(
        name="Robinson Place",
        abbreviations=PlaceAbbreviations(
            three_letter="ROB",
            five_letter="ROBIN",
            seven_letter="ROBINSO",
            fourteen_letter="ROBINSON PLACE"
        ),
        latitude=40.405804818160334,
        longitude=-108.98596168150175,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    ROCK_CREEK = PopulatedPlace(
        name="Rock Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="ROC",
            five_letter="ROCK ",
            seven_letter="ROCK CR",
            fourteen_letter="ROCK CREEK"
        ),
        latitude=39.93611753516967,
        longitude=-105.15639906976048,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    ROCK_CREEK_PARK = PopulatedPlace(
        name="Rock Creek Park",
        abbreviations=PlaceAbbreviations(
            three_letter="ROC",
            five_letter="ROCK ",
            seven_letter="ROCK CR",
            fourteen_letter="ROCK CREEK PAR"
        ),
        latitude=38.70249968434416,
        longitude=-104.83915025781982,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ROCK_CROSSING = PopulatedPlace(
        name="Rock Crossing",
        abbreviations=PlaceAbbreviations(
            three_letter="ROC",
            five_letter="ROCK ",
            seven_letter="ROCK CR",
            fourteen_letter="ROCK CROSSING"
        ),
        latitude=37.77001729489268,
        longitude=-104.12414079601939,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    ROCKDALE = PopulatedPlace(
        name="Rockdale",
        abbreviations=PlaceAbbreviations(
            three_letter="ROC",
            five_letter="ROCKD",
            seven_letter="ROCKDAL",
            fourteen_letter="ROCKDALE"
        ),
        latitude=38.99138841865903,
        longitude=-106.41170274662954,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.ASPEN
    )
    ROCKLAND = PopulatedPlace(
        name="Rockland",
        abbreviations=PlaceAbbreviations(
            three_letter="ROC",
            five_letter="ROCKL",
            seven_letter="ROCKLAN",
            fourteen_letter="ROCKLAND"
        ),
        latitude=40.51055048455777,
        longitude=-102.71992946351975,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    ROCKPORT = PopulatedPlace(
        name="Rockport",
        abbreviations=PlaceAbbreviations(
            three_letter="ROC",
            five_letter="ROCKP",
            seven_letter="ROCKPOR",
            fourteen_letter="ROCKPORT"
        ),
        latitude=40.89859979031854,
        longitude=-104.7966456041757,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ROCKVALE = PopulatedPlace(
        name="Rockvale",
        abbreviations=PlaceAbbreviations(
            three_letter="ROC",
            five_letter="ROCKV",
            seven_letter="ROCKVAL",
            fourteen_letter="ROCKVALE"
        ),
        latitude=38.369728415553936,
        longitude=-105.16389889655676,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ROCKWOOD = PopulatedPlace(
        name="Rockwood",
        abbreviations=PlaceAbbreviations(
            three_letter="ROC",
            five_letter="ROCKW",
            seven_letter="ROCKWOO",
            fourteen_letter="ROCKWOOD"
        ),
        latitude=37.490838821427076,
        longitude=-107.80202079333554,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    ROCKY_FORD = PopulatedPlace(
        name="Rocky Ford",
        abbreviations=PlaceAbbreviations(
            three_letter="ROC",
            five_letter="ROCKY",
            seven_letter="ROCKY F",
            fourteen_letter="ROCKY FORD"
        ),
        latitude=38.05251426207832,
        longitude=-103.72023703056374,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    ROE = PopulatedPlace(
        name="Roe",
        abbreviations=PlaceAbbreviations(
            three_letter="ROE",
            five_letter="ROE",
            seven_letter="ROE",
            fourteen_letter="ROE"
        ),
        latitude=38.5377699534036,
        longitude=-107.94479793493696,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    ROGERS_MESA = PopulatedPlace(
        name="Rogers Mesa",
        abbreviations=PlaceAbbreviations(
            three_letter="ROG",
            five_letter="ROGER",
            seven_letter="ROGERS ",
            fourteen_letter="ROGERS MESA"
        ),
        latitude=38.779156995685696,
        longitude=-107.79312652879173,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    ROGGEN = PopulatedPlace(
        name="Roggen",
        abbreviations=PlaceAbbreviations(
            three_letter="ROG",
            five_letter="ROGGE",
            seven_letter="ROGGEN",
            fourteen_letter="ROGGEN"
        ),
        latitude=40.16748812103879,
        longitude=-104.3721865165237,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    ROLLA = PopulatedPlace(
        name="Rolla",
        abbreviations=PlaceAbbreviations(
            three_letter="ROL",
            five_letter="ROLLA",
            seven_letter="ROLLA",
            fourteen_letter="ROLLA"
        ),
        latitude=39.86915874368418,
        longitude=-104.89137540059198,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    ROLLING_HILLS = PopulatedPlace(
        name="Rolling Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="ROL",
            five_letter="ROLLI",
            seven_letter="ROLLING",
            fourteen_letter="ROLLING HILLS"
        ),
        latitude=39.76556201391793,
        longitude=-105.11528794027731,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ROMEO = PopulatedPlace(
        name="Romeo",
        abbreviations=PlaceAbbreviations(
            three_letter="ROM",
            five_letter="ROMEO",
            seven_letter="ROMEO",
            fourteen_letter="ROMEO"
        ),
        latitude=37.172238691342045,
        longitude=-105.98531046202828,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    """
    ROSEDALE = PopulatedPlace(
        name="Rosedale",
        abbreviations=PlaceAbbreviations(
            three_letter="ROS",
            five_letter="ROSED",
            seven_letter="ROSEDAL",
            fourteen_letter="ROSEDALE"
        ),
        latitude=39.6399945777448,
        longitude=-105.38305998709126,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    ROSEDALE = PopulatedPlace(
        name="Rosedale",
        abbreviations=PlaceAbbreviations(
            three_letter="ROS",
            five_letter="ROSED",
            seven_letter="ROSEDAL",
            fourteen_letter="ROSEDALE"
        ),
        latitude=40.38526542816709,
        longitude=-104.69858661807899,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    """
    ROSEMONT = PopulatedPlace(
        name="Rosemont",
        abbreviations=PlaceAbbreviations(
            three_letter="ROS",
            five_letter="ROSEM",
            seven_letter="ROSEMON",
            fourteen_letter="ROSEMONT"
        ),
        latitude=38.74221618189165,
        longitude=-104.9569275886949,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ROSEVALE = PopulatedPlace(
        name="Rosevale",
        abbreviations=PlaceAbbreviations(
            three_letter="ROS",
            five_letter="ROSEV",
            seven_letter="ROSEVAL",
            fourteen_letter="ROSEVALE"
        ),
        latitude=39.05998777808418,
        longitude=-108.58038263080482,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    ROSITA = PopulatedPlace(
        name="Rosita",
        abbreviations=PlaceAbbreviations(
            three_letter="ROS",
            five_letter="ROSIT",
            seven_letter="ROSITA",
            fourteen_letter="ROSITA"
        ),
        latitude=38.09722996510328,
        longitude=-105.33612000773297,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    ROSWELL = PopulatedPlace(
        name="Roswell",
        abbreviations=PlaceAbbreviations(
            three_letter="ROS",
            five_letter="ROSWE",
            seven_letter="ROSWELL",
            fourteen_letter="ROSWELL"
        ),
        latitude=38.87361020986401,
        longitude=-104.81942997178226,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    ROUNDUP_JUNCTION = PopulatedPlace(
        name="Roundup Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="ROU",
            five_letter="ROUND",
            seven_letter="ROUNDUP",
            fourteen_letter="ROUNDUP JUNCTI"
        ),
        latitude=37.48277949692721,
        longitude=-108.16231107057445,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    ROUSE = PopulatedPlace(
        name="Rouse",
        abbreviations=PlaceAbbreviations(
            three_letter="ROU",
            five_letter="ROUSE",
            seven_letter="ROUSE",
            fourteen_letter="ROUSE"
        ),
        latitude=37.49085361708154,
        longitude=-104.71166220430047,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    ROWENA = PopulatedPlace(
        name="Rowena",
        abbreviations=PlaceAbbreviations(
            three_letter="ROW",
            five_letter="ROWEN",
            seven_letter="ROWENA",
            fourteen_letter="ROWENA"
        ),
        latitude=40.076936636821586,
        longitude=-105.38944874071314,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    ROXBOROUGH = PopulatedPlace(
        name="Roxborough",
        abbreviations=PlaceAbbreviations(
            three_letter="ROX",
            five_letter="ROXBO",
            seven_letter="ROXBORO",
            fourteen_letter="ROXBOROUGH"
        ),
        latitude=39.46927017498837,
        longitude=-105.08556899908899,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    ROXBOROUGH_PARK = PopulatedPlace(
        name="Roxborough Park",
        abbreviations=PlaceAbbreviations(
            three_letter="ROX",
            five_letter="ROXBO",
            seven_letter="ROXBORO",
            fourteen_letter="ROXBOROUGH PAR"
        ),
        latitude=39.47388397596933,
        longitude=-105.08527429957343,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    ROY = PopulatedPlace(
        name="Roy",
        abbreviations=PlaceAbbreviations(
            three_letter="ROY",
            five_letter="ROY",
            seven_letter="ROY",
            fourteen_letter="ROY"
        ),
        latitude=40.109711299239734,
        longitude=-104.56552625376679,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    RUBY = PopulatedPlace(
        name="Ruby",
        abbreviations=PlaceAbbreviations(
            three_letter="RUB",
            five_letter="RUBY",
            seven_letter="RUBY",
            fourteen_letter="RUBY"
        ),
        latitude=38.8661098548377,
        longitude=-107.09561428500865,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    RUBY_HILL = PopulatedPlace(
        name="Ruby Hill",
        abbreviations=PlaceAbbreviations(
            three_letter="RUB",
            five_letter="RUBY ",
            seven_letter="RUBY HI",
            fourteen_letter="RUBY HILL"
        ),
        latitude=39.686117509963196,
        longitude=-105.01139900746244,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    RUGBY = PopulatedPlace(
        name="Rugby",
        abbreviations=PlaceAbbreviations(
            three_letter="RUG",
            five_letter="RUGBY",
            seven_letter="RUGBY",
            fourteen_letter="RUGBY"
        ),
        latitude=37.470020616464524,
        longitude=-104.6649943911172,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    RULISON = PopulatedPlace(
        name="Rulison",
        abbreviations=PlaceAbbreviations(
            three_letter="RUL",
            five_letter="RULIS",
            seven_letter="RULISON",
            fourteen_letter="RULISON"
        ),
        latitude=39.49720697933452,
        longitude=-107.94063684331957,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    RUSH = PopulatedPlace(
        name="Rush",
        abbreviations=PlaceAbbreviations(
            three_letter="RUS",
            five_letter="RUSH",
            seven_letter="RUSH",
            fourteen_letter="RUSH"
        ),
        latitude=38.839999753156974,
        longitude=-104.09218969945346,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    RUSSELL = PopulatedPlace(
        name="Russell",
        abbreviations=PlaceAbbreviations(
            three_letter="RUS",
            five_letter="RUSSE",
            seven_letter="RUSSELL",
            fourteen_letter="RUSSELL"
        ),
        latitude=37.55529119024993,
        longitude=-105.28779334218984,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    RUSSELL_GULCH = PopulatedPlace(
        name="Russell Gulch",
        abbreviations=PlaceAbbreviations(
            three_letter="RUS",
            five_letter="RUSSE",
            seven_letter="RUSSELL",
            fourteen_letter="RUSSELL GULCH"
        ),
        latitude=39.778605286515926,
        longitude=-105.53695263857497,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    RUSTIC = PopulatedPlace(
        name="Rustic",
        abbreviations=PlaceAbbreviations(
            three_letter="RUS",
            five_letter="RUSTI",
            seven_letter="RUSTIC",
            fourteen_letter="RUSTIC"
        ),
        latitude=40.699290206465264,
        longitude=-105.58130586068205,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    RUXTON = PopulatedPlace(
        name="Ruxton",
        abbreviations=PlaceAbbreviations(
            three_letter="RUX",
            five_letter="RUXTO",
            seven_letter="RUXTON",
            fourteen_letter="RUXTON"
        ),
        latitude=37.74807115194477,
        longitude=-103.14660636494574,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    RYE = PopulatedPlace(
        name="Rye",
        abbreviations=PlaceAbbreviations(
            three_letter="RYE",
            five_letter="RYE",
            seven_letter="RYE",
            fourteen_letter="RYE"
        ),
        latitude=37.923625567579904,
        longitude=-104.93027609685947,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    SABLE = PopulatedPlace(
        name="Sable",
        abbreviations=PlaceAbbreviations(
            three_letter="SAB",
            five_letter="SABLE",
            seven_letter="SABLE",
            fourteen_letter="SABLE"
        ),
        latitude=39.7663824334316,
        longitude=-104.83109597466046,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    SABLERIDGE = PopulatedPlace(
        name="Sableridge",
        abbreviations=PlaceAbbreviations(
            three_letter="SAB",
            five_letter="SABLE",
            seven_letter="SABLERI",
            fourteen_letter="SABLERIDGE"
        ),
        latitude=39.69195082360653,
        longitude=-104.82362116414822,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SADDLEBROOK = PopulatedPlace(
        name="Saddlebrook",
        abbreviations=PlaceAbbreviations(
            three_letter="SAD",
            five_letter="SADDL",
            seven_letter="SADDLEB",
            fourteen_letter="SADDLEBROOK"
        ),
        latitude=39.516673105646646,
        longitude=-104.73389892387547,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    SAGUACHE = PopulatedPlace(
        name="Saguache",
        abbreviations=PlaceAbbreviations(
            three_letter="SAG",
            five_letter="SAGUA",
            seven_letter="SAGUACH",
            fourteen_letter="SAGUACHE"
        ),
        latitude=38.08750611168176,
        longitude=-106.14197728897585,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SAINT_ANN_HIGHLANDS = PopulatedPlace(
        name="Saint Ann Highlands",
        abbreviations=PlaceAbbreviations(
            three_letter="SAI",
            five_letter="SAINT",
            seven_letter="SAINT A",
            fourteen_letter="SAINT ANN HIGH"
        ),
        latitude=39.98693741997437,
        longitude=-105.45611754459571,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SAINT_CHARLES = PopulatedPlace(
        name="Saint Charles",
        abbreviations=PlaceAbbreviations(
            three_letter="SAI",
            five_letter="SAINT",
            seven_letter="SAINT C",
            fourteen_letter="SAINT CHARLES"
        ),
        latitude=38.13890001701395,
        longitude=-104.62137474854245,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    SAINT_MARYS = PopulatedPlace(
        name="Saint Marys",
        abbreviations=PlaceAbbreviations(
            three_letter="SAI",
            five_letter="SAINT",
            seven_letter="SAINT M",
            fourteen_letter="SAINT MARYS"
        ),
        latitude=39.816660483860744,
        longitude=-105.64751246877444,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SAINT_PETERSBURG = PopulatedPlace(
        name="Saint Petersburg",
        abbreviations=PlaceAbbreviations(
            three_letter="SAI",
            five_letter="SAINT",
            seven_letter="SAINT P",
            fourteen_letter="SAINT PETERSBU"
        ),
        latitude=40.555551584253806,
        longitude=-102.81715389225968,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    SAINT_VRAINS = PopulatedPlace(
        name="Saint Vrains",
        abbreviations=PlaceAbbreviations(
            three_letter="SAI",
            five_letter="SAINT",
            seven_letter="SAINT V",
            fourteen_letter="SAINT VRAINS"
        ),
        latitude=40.03693496240908,
        longitude=-104.95471043518256,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    SALIDA = PopulatedPlace(
        name="Salida",
        abbreviations=PlaceAbbreviations(
            three_letter="SAL",
            five_letter="SALID",
            seven_letter="SALIDA",
            fourteen_letter="SALIDA"
        ),
        latitude=38.53472548350504,
        longitude=-105.99891240351411,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SALINA = PopulatedPlace(
        name="Salina",
        abbreviations=PlaceAbbreviations(
            three_letter="SAL",
            five_letter="SALIN",
            seven_letter="SALINA",
            fourteen_letter="SALINA"
        ),
        latitude=40.05054793496521,
        longitude=-105.37250363355747,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SALT_CREEK = PopulatedPlace(
        name="Salt Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="SAL",
            five_letter="SALT ",
            seven_letter="SALT CR",
            fourteen_letter="SALT CREEK"
        ),
        latitude=38.23839123398329,
        longitude=-104.5871438508546,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    SAMPLE = PopulatedPlace(
        name="Sample",
        abbreviations=PlaceAbbreviations(
            three_letter="SAM",
            five_letter="SAMPL",
            seven_letter="SAMPLE",
            fourteen_letter="SAMPLE"
        ),
        latitude=38.47222531771911,
        longitude=-105.3555582515175,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    SAN_ANTONIO = PopulatedPlace(
        name="San Antonio",
        abbreviations=PlaceAbbreviations(
            three_letter="SAN",
            five_letter="SAN A",
            seven_letter="SAN ANT",
            fourteen_letter="SAN ANTONIO"
        ),
        latitude=37.02085266684577,
        longitude=-106.02808705637011,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SAN_ISABEL = PopulatedPlace(
        name="San Isabel",
        abbreviations=PlaceAbbreviations(
            three_letter="SAN",
            five_letter="SAN I",
            seven_letter="SAN ISA",
            fourteen_letter="SAN ISABEL"
        ),
        latitude=37.98751296733013,
        longitude=-105.05444603243399,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.PUEBLO
    )
    SAN_LUIS = PopulatedPlace(
        name="San Luis",
        abbreviations=PlaceAbbreviations(
            three_letter="SAN",
            five_letter="SAN L",
            seven_letter="SAN LUI",
            fourteen_letter="SAN LUIS"
        ),
        latitude=37.20085433015964,
        longitude=-105.42391113784294,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    """
    SAN_MIGUEL = PopulatedPlace(
        name="San Miguel",
        abbreviations=PlaceAbbreviations(
            three_letter="SAN",
            five_letter="SAN M",
            seven_letter="SAN MIG",
            fourteen_letter="SAN MIGUEL"
        ),
        latitude=37.946944081221716,
        longitude=-107.83590734791028,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    SAN_MIGUEL = PopulatedPlace(
        name="San Miguel",
        abbreviations=PlaceAbbreviations(
            three_letter="SAN",
            five_letter="SAN M",
            seven_letter="SAN MIG",
            fourteen_letter="SAN MIGUEL"
        ),
        latitude=37.099471077893895,
        longitude=-104.39554859338438,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.TELLURIDE
    )
    """
    SAN_PABLO = PopulatedPlace(
        name="San Pablo",
        abbreviations=PlaceAbbreviations(
            three_letter="SAN",
            five_letter="SAN P",
            seven_letter="SAN PAB",
            fourteen_letter="SAN PABLO"
        ),
        latitude=37.14918972404638,
        longitude=-105.39696542709072,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SAN_PEDRO = PopulatedPlace(
        name="San Pedro",
        abbreviations=PlaceAbbreviations(
            three_letter="SAN",
            five_letter="SAN P",
            seven_letter="SAN PED",
            fourteen_letter="SAN PEDRO"
        ),
        latitude=37.15974482557556,
        longitude=-105.40252112893222,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SANDOWN = PopulatedPlace(
        name="Sandown",
        abbreviations=PlaceAbbreviations(
            three_letter="SAN",
            five_letter="SANDO",
            seven_letter="SANDOWN",
            fourteen_letter="SANDOWN"
        ),
        latitude=39.77249322990326,
        longitude=-104.90137649197379,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    SANFORD = PopulatedPlace(
        name="Sanford",
        abbreviations=PlaceAbbreviations(
            three_letter="SAN",
            five_letter="SANFO",
            seven_letter="SANFORD",
            fourteen_letter="SANFORD"
        ),
        latitude=37.258348609583265,
        longitude=-105.90475425182558,
        counties=[Counties.CONEJOS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SANTA_MARIA = PopulatedPlace(
        name="Santa Maria",
        abbreviations=PlaceAbbreviations(
            three_letter="SAN",
            five_letter="SANTA",
            seven_letter="SANTA M",
            fourteen_letter="SANTA MARIA"
        ),
        latitude=39.44971663483284,
        longitude=-105.63334762316873,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    SAPINERO = PopulatedPlace(
        name="Sapinero",
        abbreviations=PlaceAbbreviations(
            three_letter="SAP",
            five_letter="SAPIN",
            seven_letter="SAPINER",
            fourteen_letter="SAPINERO"
        ),
        latitude=38.45944258602111,
        longitude=-107.30228838615704,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SARCILLO = PopulatedPlace(
        name="Sarcillo",
        abbreviations=PlaceAbbreviations(
            three_letter="SAR",
            five_letter="SARCI",
            seven_letter="SARCILL",
            fourteen_letter="SARCILLO"
        ),
        latitude=37.125582159638896,
        longitude=-104.75944568015086,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SARGENTS = PopulatedPlace(
        name="Sargents",
        abbreviations=PlaceAbbreviations(
            three_letter="SAR",
            five_letter="SARGE",
            seven_letter="SARGENT",
            fourteen_letter="SARGENTS"
        ),
        latitude=38.40416913789892,
        longitude=-106.41503828290774,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SATANK = PopulatedPlace(
        name="Satank",
        abbreviations=PlaceAbbreviations(
            three_letter="SAT",
            five_letter="SATAN",
            seven_letter="SATANK",
            fourteen_letter="SATANK"
        ),
        latitude=39.413878219191304,
        longitude=-107.22839617697258,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    SAUNDERS = PopulatedPlace(
        name="Saunders",
        abbreviations=PlaceAbbreviations(
            three_letter="SAU",
            five_letter="SAUND",
            seven_letter="SAUNDER",
            fourteen_letter="SAUNDERS"
        ),
        latitude=38.76026747864893,
        longitude=-108.01007757418273,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    SAWPIT = PopulatedPlace(
        name="Sawpit",
        abbreviations=PlaceAbbreviations(
            three_letter="SAW",
            five_letter="SAWPI",
            seven_letter="SAWPIT",
            fourteen_letter="SAWPIT"
        ),
        latitude=37.995276176994764,
        longitude=-108.00174448899344,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    SAXTON = PopulatedPlace(
        name="Saxton",
        abbreviations=PlaceAbbreviations(
            three_letter="SAX",
            five_letter="SAXTO",
            seven_letter="SAXTON",
            fourteen_letter="SAXTON"
        ),
        latitude=38.76832298218119,
        longitude=-107.97146526586755,
        counties=[Counties.DELTA],
        nearest_airport=Airports.MONTROSE
    )
    SCENIC_HEIGHTS = PopulatedPlace(
        name="Scenic Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="SCE",
            five_letter="SCENI",
            seven_letter="SCENIC ",
            fourteen_letter="SCENIC HEIGHTS"
        ),
        latitude=39.81278422236102,
        longitude=-105.08501013918442,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SCHRAMM = PopulatedPlace(
        name="Schramm",
        abbreviations=PlaceAbbreviations(
            three_letter="SCH",
            five_letter="SCHRA",
            seven_letter="SCHRAMM",
            fourteen_letter="SCHRAMM"
        ),
        latitude=40.11388283567055,
        longitude=-102.60604868927567,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    SECURITY = PopulatedPlace(
        name="Security",
        abbreviations=PlaceAbbreviations(
            three_letter="SEC",
            five_letter="SECUR",
            seven_letter="SECURIT",
            fourteen_letter="SECURITY"
        ),
        latitude=38.75833509825043,
        longitude=-104.74303774128055,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    SEDALIA = PopulatedPlace(
        name="Sedalia",
        abbreviations=PlaceAbbreviations(
            three_letter="SED",
            five_letter="SEDAL",
            seven_letter="SEDALIA",
            fourteen_letter="SEDALIA"
        ),
        latitude=39.436939979056774,
        longitude=-104.959714666661,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    SEDGWICK = PopulatedPlace(
        name="Sedgwick",
        abbreviations=PlaceAbbreviations(
            three_letter="SED",
            five_letter="SEDGW",
            seven_letter="SEDGWIC",
            fourteen_letter="SEDGWICK"
        ),
        latitude=40.936386657985054,
        longitude=-102.52547616746403,
        counties=[Counties.SEDGWICK],
        nearest_airport=Airports.DENVER
    )
    SEIBERT = PopulatedPlace(
        name="Seibert",
        abbreviations=PlaceAbbreviations(
            three_letter="SEI",
            five_letter="SEIBE",
            seven_letter="SEIBERT",
            fourteen_letter="SEIBERT"
        ),
        latitude=39.299165600236734,
        longitude=-102.86910726052236,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.DENVER
    )
    SELMA = PopulatedPlace(
        name="Selma",
        abbreviations=PlaceAbbreviations(
            three_letter="SEL",
            five_letter="SELMA",
            seven_letter="SELMA",
            fourteen_letter="SELMA"
        ),
        latitude=40.77138539941899,
        longitude=-103.03104257096572,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    SEMPER = PopulatedPlace(
        name="Semper",
        abbreviations=PlaceAbbreviations(
            three_letter="SEM",
            five_letter="SEMPE",
            seven_letter="SEMPER",
            fourteen_letter="SEMPER"
        ),
        latitude=39.85610352963619,
        longitude=-105.06471563923742,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SEQUNDO = PopulatedPlace(
        name="Sequndo",
        abbreviations=PlaceAbbreviations(
            three_letter="SEQ",
            five_letter="SEQUN",
            seven_letter="SEQUNDO",
            fourteen_letter="SEQUNDO"
        ),
        latitude=37.12085996138313,
        longitude=-104.72222257060838,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SETTLERS_VILLAGE = PopulatedPlace(
        name="Settlers Village",
        abbreviations=PlaceAbbreviations(
            three_letter="SET",
            five_letter="SETTL",
            seven_letter="SETTLER",
            fourteen_letter="SETTLERS VILLA"
        ),
        latitude=39.700284225544635,
        longitude=-104.81473226344491,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    """
    SEVEN_HILLS = PopulatedPlace(
        name="Seven Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="SEV",
            five_letter="SEVEN",
            seven_letter="SEVEN H",
            fourteen_letter="SEVEN HILLS"
        ),
        latitude=39.658339723840186,
        longitude=-104.76139894636196,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SEVEN_HILLS = PopulatedPlace(
        name="Seven Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="SEV",
            five_letter="SEVEN",
            seven_letter="SEVEN H",
            fourteen_letter="SEVEN HILLS"
        ),
        latitude=40.02638113541167,
        longitude=-105.31194611616365,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    """
    SEVENMILE_PLAZA = PopulatedPlace(
        name="Sevenmile Plaza",
        abbreviations=PlaceAbbreviations(
            three_letter="SEV",
            five_letter="SEVEN",
            seven_letter="SEVENMI",
            fourteen_letter="SEVENMILE PLAZ"
        ),
        latitude=37.64806454344176,
        longitude=-106.2375412654564,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SEVERANCE = PopulatedPlace(
        name="Severance",
        abbreviations=PlaceAbbreviations(
            three_letter="SEV",
            five_letter="SEVER",
            seven_letter="SEVERAN",
            fourteen_letter="SEVERANCE"
        ),
        latitude=40.52415443575012,
        longitude=-104.85109207043973,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SHAFFERS_CROSSING = PopulatedPlace(
        name="Shaffers Crossing",
        abbreviations=PlaceAbbreviations(
            three_letter="SHA",
            five_letter="SHAFF",
            seven_letter="SHAFFER",
            fourteen_letter="SHAFFERS CROSS"
        ),
        latitude=39.47860615698386,
        longitude=-105.36833896574694,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SHAMBALLAH_ASHRAMA = PopulatedPlace(
        name="Shamballah-Ashrama",
        abbreviations=PlaceAbbreviations(
            three_letter="SHA",
            five_letter="SHAMB",
            seven_letter="SHAMBAL",
            fourteen_letter="SHAMBALLAH-ASH"
        ),
        latitude=39.343051860894434,
        longitude=-105.03332887241788,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    SHAMROCK = PopulatedPlace(
        name="Shamrock",
        abbreviations=PlaceAbbreviations(
            three_letter="SHA",
            five_letter="SHAMR",
            seven_letter="SHAMROC",
            fourteen_letter="SHAMROCK"
        ),
        latitude=39.88526882014122,
        longitude=-103.8163498516318,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    SHAW = PopulatedPlace(
        name="Shaw",
        abbreviations=PlaceAbbreviations(
            three_letter="SHA",
            five_letter="SHAW",
            seven_letter="SHAW",
            fourteen_letter="SHAW"
        ),
        latitude=39.55054870392513,
        longitude=-103.36078500545244,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.DENVER
    )
    SHAW_HEIGHTS = PopulatedPlace(
        name="Shaw Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="SHA",
            five_letter="SHAW ",
            seven_letter="SHAW HE",
            fourteen_letter="SHAW HEIGHTS"
        ),
        latitude=39.85250643096589,
        longitude=-105.04306573513861,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    SHAWNEE = PopulatedPlace(
        name="Shawnee",
        abbreviations=PlaceAbbreviations(
            three_letter="SHA",
            five_letter="SHAWN",
            seven_letter="SHAWNEE",
            fourteen_letter="SHAWNEE"
        ),
        latitude=39.421106336006744,
        longitude=-105.55417870102224,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    SHEEPHORN = PopulatedPlace(
        name="Sheephorn",
        abbreviations=PlaceAbbreviations(
            three_letter="SHE",
            five_letter="SHEEP",
            seven_letter="SHEEPHO",
            fourteen_letter="SHEEPHORN"
        ),
        latitude=39.89221473598741,
        longitude=-106.46698706347416,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    SHELTON = PopulatedPlace(
        name="Shelton",
        abbreviations=PlaceAbbreviations(
            three_letter="SHE",
            five_letter="SHELT",
            seven_letter="SHELTON",
            fourteen_letter="SHELTON"
        ),
        latitude=38.083347073949426,
        longitude=-103.6063433071048,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    SHENANDOAH = PopulatedPlace(
        name="Shenandoah",
        abbreviations=PlaceAbbreviations(
            three_letter="SHE",
            five_letter="SHENA",
            seven_letter="SHENAND",
            fourteen_letter="SHENANDOAH"
        ),
        latitude=39.62695081588464,
        longitude=-104.80751005290233,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SHERIDAN = PopulatedPlace(
        name="Sheridan",
        abbreviations=PlaceAbbreviations(
            three_letter="SHE",
            five_letter="SHERI",
            seven_letter="SHERIDA",
            fourteen_letter="SHERIDAN"
        ),
        latitude=39.646938303721754,
        longitude=-105.02527110559186,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SHERIDAN_GREEN = PopulatedPlace(
        name="Sheridan Green",
        abbreviations=PlaceAbbreviations(
            three_letter="SHE",
            five_letter="SHERI",
            seven_letter="SHERIDA",
            fourteen_letter="SHERIDAN GREEN"
        ),
        latitude=39.8966731350514,
        longitude=-105.06501014471684,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SHERIDAN_LAKE = PopulatedPlace(
        name="Sheridan Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="SHE",
            five_letter="SHERI",
            seven_letter="SHERIDA",
            fourteen_letter="SHERIDAN LAKE"
        ),
        latitude=38.46668741401601,
        longitude=-102.29214023397287,
        counties=[Counties.KIOWA],
        nearest_airport=Airports.PUEBLO
    )
    SHERRELWOOD = PopulatedPlace(
        name="Sherrelwood",
        abbreviations=PlaceAbbreviations(
            three_letter="SHE",
            five_letter="SHERR",
            seven_letter="SHERREL",
            fourteen_letter="SHERRELWOOD"
        ),
        latitude=39.837770132061394,
        longitude=-105.00138022286285,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    SHERRELWOOD_ESTATES = PopulatedPlace(
        name="Sherrelwood Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="SHE",
            five_letter="SHERR",
            seven_letter="SHERREL",
            fourteen_letter="SHERRELWOOD ES"
        ),
        latitude=39.84472863240762,
        longitude=-105.0094545249782,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    SHERWOOD_FARMS = PopulatedPlace(
        name="Sherwood Farms",
        abbreviations=PlaceAbbreviations(
            three_letter="SHE",
            five_letter="SHERW",
            seven_letter="SHERWOO",
            fourteen_letter="SHERWOOD FARMS"
        ),
        latitude=39.83222861890533,
        longitude=-105.1747323623892,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SHIRLEY = PopulatedPlace(
        name="Shirley",
        abbreviations=PlaceAbbreviations(
            three_letter="SHI",
            five_letter="SHIRL",
            seven_letter="SHIRLEY",
            fourteen_letter="SHIRLEY"
        ),
        latitude=38.90111162452371,
        longitude=-104.65331553604216,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    SIDE_CREEK = PopulatedPlace(
        name="Side Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="SID",
            five_letter="SIDE ",
            seven_letter="SIDE CR",
            fourteen_letter="SIDE CREEK"
        ),
        latitude=39.68833972726742,
        longitude=-104.76612115085862,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SIERRA_ESTATES = PopulatedPlace(
        name="Sierra Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="SIE",
            five_letter="SIERR",
            seven_letter="SIERRA ",
            fourteen_letter="SIERRA ESTATES"
        ),
        latitude=39.83583972416403,
        longitude=-105.10473234671832,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SIERRA_RIDGE = PopulatedPlace(
        name="Sierra Ridge",
        abbreviations=PlaceAbbreviations(
            three_letter="SIE",
            five_letter="SIERR",
            seven_letter="SIERRA ",
            fourteen_letter="SIERRA RIDGE"
        ),
        latitude=39.531373801784014,
        longitude=-104.81812864441383,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    SIERRA_VISTA = PopulatedPlace(
        name="Sierra Vista",
        abbreviations=PlaceAbbreviations(
            three_letter="SIE",
            five_letter="SIERR",
            seven_letter="SIERRA ",
            fourteen_letter="SIERRA VISTA"
        ),
        latitude=39.835839723474294,
        longitude=-105.11334344791157,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SIKES = PopulatedPlace(
        name="Sikes",
        abbreviations=PlaceAbbreviations(
            three_letter="SIK",
            five_letter="SIKES",
            seven_letter="SIKES",
            fourteen_letter="SIKES"
        ),
        latitude=38.258342105195084,
        longitude=-105.07472066434184,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.PUEBLO
    )
    SILLSVILLE = PopulatedPlace(
        name="Sillsville",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILLS",
            seven_letter="SILLSVI",
            fourteen_letter="SILLSVILLE"
        ),
        latitude=38.44666472063983,
        longitude=-106.76115856449923,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SILOAM = PopulatedPlace(
        name="Siloam",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILOA",
            seven_letter="SILOAM",
            fourteen_letter="SILOAM"
        ),
        latitude=38.25139861086484,
        longitude=-104.97582894177333,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    SILT = PopulatedPlace(
        name="Silt",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILT",
            seven_letter="SILT",
            fourteen_letter="SILT"
        ),
        latitude=39.548597906311045,
        longitude=-107.65618138745685,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.EAGLE
    )
    SILVER_CLIFF = PopulatedPlace(
        name="Silver Cliff",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILVE",
            seven_letter="SILVER ",
            fourteen_letter="SILVER CLIFF"
        ),
        latitude=38.13528406364776,
        longitude=-105.44640023640204,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SILVER_HEIGHTS = PopulatedPlace(
        name="Silver Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILVE",
            seven_letter="SILVER ",
            fourteen_letter="SILVER HEIGHTS"
        ),
        latitude=39.41805148301967,
        longitude=-104.86582244324615,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    SILVER_PLUME = PopulatedPlace(
        name="Silver Plume",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILVE",
            seven_letter="SILVER ",
            fourteen_letter="SILVER PLUME"
        ),
        latitude=39.69610466161322,
        longitude=-105.7258488727399,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    SILVER_SPRINGS = PopulatedPlace(
        name="Silver Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILVE",
            seven_letter="SILVER ",
            fourteen_letter="SILVER SPRINGS"
        ),
        latitude=40.01554842386736,
        longitude=-105.45445084814685,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SILVER_SPRINGS = PopulatedPlace(
        name="Silver Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILVE",
            seven_letter="SILVER ",
            fourteen_letter="SILVER SPRINGS"
        ),
        latitude=39.45916195206678,
        longitude=-105.39611776960209,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    SILVER_SPRUCE = PopulatedPlace(
        name="Silver Spruce",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILVE",
            seven_letter="SILVER ",
            fourteen_letter="SILVER SPRUCE"
        ),
        latitude=40.00471463041106,
        longitude=-105.34778062251621,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SILVERTHORNE = PopulatedPlace(
        name="Silverthorne",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILVE",
            seven_letter="SILVERT",
            fourteen_letter="SILVERTHORNE"
        ),
        latitude=39.632145328770605,
        longitude=-106.07429134425666,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    SILVERTON = PopulatedPlace(
        name="Silverton",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILVE",
            seven_letter="SILVERT",
            fourteen_letter="SILVERTON"
        ),
        latitude=37.81194697461086,
        longitude=-107.66451619651315,
        counties=[Counties.SAN_JUAN],
        nearest_airport=Airports.TELLURIDE
    )
    SIMLA = PopulatedPlace(
        name="Simla",
        abbreviations=PlaceAbbreviations(
            three_letter="SIM",
            five_letter="SIMLA",
            seven_letter="SIMLA",
            fourteen_letter="SIMLA"
        ),
        latitude=39.141661497053235,
        longitude=-104.0838577299719,
        counties=[Counties.ELBERT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    SIMPSON = PopulatedPlace(
        name="Simpson",
        abbreviations=PlaceAbbreviations(
            three_letter="SIM",
            five_letter="SIMPS",
            seven_letter="SIMPSON",
            fourteen_letter="SIMPSON"
        ),
        latitude=37.49779795169326,
        longitude=-104.16720087890178,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    SINGLETON = PopulatedPlace(
        name="Singleton",
        abbreviations=PlaceAbbreviations(
            three_letter="SIN",
            five_letter="SINGL",
            seven_letter="SINGLET",
            fourteen_letter="SINGLETON"
        ),
        latitude=39.44305033576984,
        longitude=-105.60195781465359,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    SINNARD = PopulatedPlace(
        name="Sinnard",
        abbreviations=PlaceAbbreviations(
            three_letter="SIN",
            five_letter="SINNA",
            seven_letter="SINNARD",
            fourteen_letter="SINNARD"
        ),
        latitude=40.58832223241137,
        longitude=-105.00331911333438,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SKINNERS = PopulatedPlace(
        name="Skinners",
        abbreviations=PlaceAbbreviations(
            three_letter="SKI",
            five_letter="SKINN",
            seven_letter="SKINNER",
            fourteen_letter="SKINNERS"
        ),
        latitude=38.76889009847201,
        longitude=-104.76137144713437,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    SKY_VILLAGE = PopulatedPlace(
        name="Sky Village",
        abbreviations=PlaceAbbreviations(
            three_letter="SKY",
            five_letter="SKY V",
            seven_letter="SKY VIL",
            fourteen_letter="SKY VILLAGE"
        ),
        latitude=39.550550175130354,
        longitude=-105.24722344586871,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SKYLINE_ESTATES = PopulatedPlace(
        name="Skyline Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="SKY",
            five_letter="SKYLI",
            seven_letter="SKYLINE",
            fourteen_letter="SKYLINE ESTATE"
        ),
        latitude=39.79611751764139,
        longitude=-105.11806574493471,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SKYLINE_VISTA = PopulatedPlace(
        name="Skyline Vista",
        abbreviations=PlaceAbbreviations(
            three_letter="SKY",
            five_letter="SKYLI",
            seven_letter="SKYLINE",
            fourteen_letter="SKYLINE VISTA"
        ),
        latitude=39.83056202978031,
        longitude=-105.02001012572367,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    SLATE_CREEK = PopulatedPlace(
        name="Slate Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="SLA",
            five_letter="SLATE",
            seven_letter="SLATE C",
            fourteen_letter="SLATE CREEK"
        ),
        latitude=39.784158843368004,
        longitude=-106.16336688196651,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.EAGLE
    )
    SLATER = PopulatedPlace(
        name="Slater",
        abbreviations=PlaceAbbreviations(
            three_letter="SLA",
            five_letter="SLATE",
            seven_letter="SLATER",
            fourteen_letter="SLATER"
        ),
        latitude=40.94775029694301,
        longitude=-107.4978530266784,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    SLAVONIA = PopulatedPlace(
        name="Slavonia",
        abbreviations=PlaceAbbreviations(
            three_letter="SLA",
            five_letter="SLAVO",
            seven_letter="SLAVONI",
            fourteen_letter="SLAVONIA"
        ),
        latitude=40.78442393507055,
        longitude=-106.70421892747049,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    SLOAN = PopulatedPlace(
        name="Sloan",
        abbreviations=PlaceAbbreviations(
            three_letter="SLO",
            five_letter="SLOAN",
            seven_letter="SLOAN",
            fourteen_letter="SLOAN"
        ),
        latitude=40.05165619699119,
        longitude=-104.48802312885556,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    SMITH_HILL = PopulatedPlace(
        name="Smith Hill",
        abbreviations=PlaceAbbreviations(
            three_letter="SMI",
            five_letter="SMITH",
            seven_letter="SMITH H",
            fourteen_letter="SMITH HILL"
        ),
        latitude=39.778327491970856,
        longitude=-105.45861672059823,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.DENVER
    )
    SMITH_PLACE = PopulatedPlace(
        name="Smith Place",
        abbreviations=PlaceAbbreviations(
            three_letter="SMI",
            five_letter="SMITH",
            seven_letter="SMITH P",
            fourteen_letter="SMITH PLACE"
        ),
        latitude=38.201667567102504,
        longitude=-107.05978210619094,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SNOW_WATER_SPRINGS = PopulatedPlace(
        name="Snow Water Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="SNO",
            five_letter="SNOW ",
            seven_letter="SNOW WA",
            fourteen_letter="SNOW WATER SPR"
        ),
        latitude=39.264718738685815,
        longitude=-105.21694780612245,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    SNOWMASS = PopulatedPlace(
        name="Snowmass",
        abbreviations=PlaceAbbreviations(
            three_letter="SNO",
            five_letter="SNOWM",
            seven_letter="SNOWMAS",
            fourteen_letter="SNOWMASS"
        ),
        latitude=39.33165752466277,
        longitude=-106.98616651343536,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    SNOWMASS_VILLAGE = PopulatedPlace(
        name="Snowmass Village",
        abbreviations=PlaceAbbreviations(
            three_letter="SNO",
            five_letter="SNOWM",
            seven_letter="SNOWMAS",
            fourteen_letter="SNOWMASS VILLA"
        ),
        latitude=39.21304801267007,
        longitude=-106.93783118903116,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    SOMERSET = PopulatedPlace(
        name="Somerset",
        abbreviations=PlaceAbbreviations(
            three_letter="SOM",
            five_letter="SOMER",
            seven_letter="SOMERSE",
            fourteen_letter="SOMERSET"
        ),
        latitude=38.92638413766548,
        longitude=-107.4703434748634,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.MONTROSE
    )
    SOMERSET_VILLAGE = PopulatedPlace(
        name="Somerset Village",
        abbreviations=PlaceAbbreviations(
            three_letter="SOM",
            five_letter="SOMER",
            seven_letter="SOMERSE",
            fourteen_letter="SOMERSET VILLA"
        ),
        latitude=39.69500642697329,
        longitude=-104.78834335635361,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SOUTH_FORK = PopulatedPlace(
        name="South Fork",
        abbreviations=PlaceAbbreviations(
            three_letter="SOU",
            five_letter="SOUTH",
            seven_letter="SOUTH F",
            fourteen_letter="SOUTH FORK"
        ),
        latitude=37.67001012062855,
        longitude=-106.63977405668572,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SOUTH_PLATTE = PopulatedPlace(
        name="South Platte",
        abbreviations=PlaceAbbreviations(
            three_letter="SOU",
            five_letter="SOUTH",
            seven_letter="SOUTH P",
            fourteen_letter="SOUTH PLATTE"
        ),
        latitude=39.407495560705115,
        longitude=-105.1713889119535,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SOUTH_ROGGEN = PopulatedPlace(
        name="South Roggen",
        abbreviations=PlaceAbbreviations(
            three_letter="SOU",
            five_letter="SOUTH",
            seven_letter="SOUTH R",
            fourteen_letter="SOUTH ROGGEN"
        ),
        latitude=40.10221111470821,
        longitude=-104.33857479971351,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    SOUTHFIELD_PARK = PopulatedPlace(
        name="Southfield Park",
        abbreviations=PlaceAbbreviations(
            three_letter="SOU",
            five_letter="SOUTH",
            seven_letter="SOUTHFI",
            fourteen_letter="SOUTHFIELD PAR"
        ),
        latitude=39.60056200989152,
        longitude=-104.84334335820745,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SOUTHGLENN = PopulatedPlace(
        name="Southglenn",
        abbreviations=PlaceAbbreviations(
            three_letter="SOU",
            five_letter="SOUTH",
            seven_letter="SOUTHGL",
            fourteen_letter="SOUTHGLENN"
        ),
        latitude=39.587216700494196,
        longitude=-104.95276888210452,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SOUTHPARK = PopulatedPlace(
        name="Southpark",
        abbreviations=PlaceAbbreviations(
            three_letter="SOU",
            five_letter="SOUTH",
            seven_letter="SOUTHPA",
            fourteen_letter="SOUTHPARK"
        ),
        latitude=39.575006394444756,
        longitude=-105.02028789648767,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SPANISH_VILLAGE = PopulatedPlace(
        name="Spanish Village",
        abbreviations=PlaceAbbreviations(
            three_letter="SPA",
            five_letter="SPANI",
            seven_letter="SPANISH",
            fourteen_letter="SPANISH VILLAG"
        ),
        latitude=40.384431838768194,
        longitude=-104.54635718207231,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SPAR_CITY = PopulatedPlace(
        name="Spar City",
        abbreviations=PlaceAbbreviations(
            three_letter="SPA",
            five_letter="SPAR ",
            seven_letter="SPAR CI",
            fourteen_letter="SPAR CITY"
        ),
        latitude=37.70723060530196,
        longitude=-106.96838983312625,
        counties=[Counties.MINERAL],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SPENCER_HEIGHTS = PopulatedPlace(
        name="Spencer Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="SPE",
            five_letter="SPENC",
            seven_letter="SPENCER",
            fourteen_letter="SPENCER HEIGHT"
        ),
        latitude=40.67415388820535,
        longitude=-105.7844617046303,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SPHINX_PARK = PopulatedPlace(
        name="Sphinx Park",
        abbreviations=PlaceAbbreviations(
            three_letter="SPH",
            five_letter="SPHIN",
            seven_letter="SPHINX ",
            fourteen_letter="SPHINX PARK"
        ),
        latitude=39.42443975348408,
        longitude=-105.31500454732941,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SPIVAK = PopulatedPlace(
        name="Spivak",
        abbreviations=PlaceAbbreviations(
            three_letter="SPI",
            five_letter="SPIVA",
            seven_letter="SPIVAK",
            fourteen_letter="SPIVAK"
        ),
        latitude=39.74471561431125,
        longitude=-105.06804952710701,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SPOOK_CITY = PopulatedPlace(
        name="Spook City",
        abbreviations=PlaceAbbreviations(
            three_letter="SPO",
            five_letter="SPOOK",
            seven_letter="SPOOK C",
            fourteen_letter="SPOOK CITY"
        ),
        latitude=38.23000622801442,
        longitude=-106.19725561585415,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    SPRING_CREEK_MEADOWS = PopulatedPlace(
        name="Spring Creek Meadows",
        abbreviations=PlaceAbbreviations(
            three_letter="SPR",
            five_letter="SPRIN",
            seven_letter="SPRING ",
            fourteen_letter="SPRING CREEK M"
        ),
        latitude=39.640562022469624,
        longitude=-104.74667674103807,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SPRING_HILL = PopulatedPlace(
        name="Spring Hill",
        abbreviations=PlaceAbbreviations(
            three_letter="SPR",
            five_letter="SPRIN",
            seven_letter="SPRING ",
            fourteen_letter="SPRING HILL"
        ),
        latitude=39.635284193829364,
        longitude=-105.15028793329054,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SPRING_MESA = PopulatedPlace(
        name="Spring Mesa",
        abbreviations=PlaceAbbreviations(
            three_letter="SPR",
            five_letter="SPRIN",
            seven_letter="SPRING ",
            fourteen_letter="SPRING MESA"
        ),
        latitude=39.83778421809046,
        longitude=-105.19862126792628,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SPRING_RANCH = PopulatedPlace(
        name="Spring Ranch",
        abbreviations=PlaceAbbreviations(
            three_letter="SPR",
            five_letter="SPRIN",
            seven_letter="SPRING ",
            fourteen_letter="SPRING RANCH"
        ),
        latitude=39.69972859106116,
        longitude=-105.31556577878627,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SPRINGDALE = PopulatedPlace(
        name="Springdale",
        abbreviations=PlaceAbbreviations(
            three_letter="SPR",
            five_letter="SPRIN",
            seven_letter="SPRINGD",
            fourteen_letter="SPRINGDALE"
        ),
        latitude=40.10971424390402,
        longitude=-105.35833643706064,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SPRINGFIELD = PopulatedPlace(
        name="Springfield",
        abbreviations=PlaceAbbreviations(
            three_letter="SPR",
            five_letter="SPRIN",
            seven_letter="SPRINGF",
            fourteen_letter="SPRINGFIELD"
        ),
        latitude=37.408354833005376,
        longitude=-102.61437090664646,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    SPRUCE = PopulatedPlace(
        name="Spruce",
        abbreviations=PlaceAbbreviations(
            three_letter="SPR",
            five_letter="SPRUC",
            seven_letter="SPRUCE",
            fourteen_letter="SPRUCE"
        ),
        latitude=39.15666454581748,
        longitude=-104.8783239161695,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    SPRUCEDALE = PopulatedPlace(
        name="Sprucedale",
        abbreviations=PlaceAbbreviations(
            three_letter="SPR",
            five_letter="SPRUC",
            seven_letter="SPRUCED",
            fourteen_letter="SPRUCEDALE"
        ),
        latitude=39.58888357313998,
        longitude=-105.35222627436457,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SPRUCEWOOD = PopulatedPlace(
        name="Sprucewood",
        abbreviations=PlaceAbbreviations(
            three_letter="SPR",
            five_letter="SPRUC",
            seven_letter="SPRUCEW",
            fourteen_letter="SPRUCEWOOD"
        ),
        latitude=39.348884955936626,
        longitude=-105.12083209427584,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    STAGE = PopulatedPlace(
        name="Stage",
        abbreviations=PlaceAbbreviations(
            three_letter="STA",
            five_letter="STAGE",
            seven_letter="STAGE",
            fourteen_letter="STAGE"
        ),
        latitude=40.61165365619212,
        longitude=-104.742755355871,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    STANLEY_PARK = PopulatedPlace(
        name="Stanley Park",
        abbreviations=PlaceAbbreviations(
            three_letter="STA",
            five_letter="STANL",
            seven_letter="STANLEY",
            fourteen_letter="STANLEY PARK"
        ),
        latitude=39.6183276816343,
        longitude=-105.29277976456791,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    STAPLETON = PopulatedPlace(
        name="Stapleton",
        abbreviations=PlaceAbbreviations(
            three_letter="STA",
            five_letter="STAPL",
            seven_letter="STAPLET",
            fourteen_letter="STAPLETON"
        ),
        latitude=37.498888283689496,
        longitude=-108.40482032486244,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    STARKVILLE = PopulatedPlace(
        name="Starkville",
        abbreviations=PlaceAbbreviations(
            three_letter="STA",
            five_letter="STARK",
            seven_letter="STARKVI",
            fourteen_letter="STARKVILLE"
        ),
        latitude=37.11530407296931,
        longitude=-104.52416302467543,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    STATE_BRIDGE = PopulatedPlace(
        name="State Bridge",
        abbreviations=PlaceAbbreviations(
            three_letter="STA",
            five_letter="STATE",
            seven_letter="STATE B",
            fourteen_letter="STATE BRIDGE"
        ),
        latitude=39.85777091807813,
        longitude=-106.64976860024734,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    STEAMBOAT_II = PopulatedPlace(
        name="Steamboat II",
        abbreviations=PlaceAbbreviations(
            three_letter="STE",
            five_letter="STEAM",
            seven_letter="STEAMBO",
            fourteen_letter="STEAMBOAT II"
        ),
        latitude=40.50803778473994,
        longitude=-106.9067281380261,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    STEAMBOAT_SPRINGS = PopulatedPlace(
        name="Steamboat Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="STE",
            five_letter="STEAM",
            seven_letter="STEAMBO",
            fourteen_letter="STEAMBOAT SPRI"
        ),
        latitude=40.484983287346495,
        longitude=-106.83172641783767,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    STELBARS_LINDLAND = PopulatedPlace(
        name="Stelbars Lindland",
        abbreviations=PlaceAbbreviations(
            three_letter="STE",
            five_letter="STELB",
            seven_letter="STELBAR",
            fourteen_letter="STELBARS LINDL"
        ),
        latitude=40.57443135489757,
        longitude=-106.06475155573952,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    STEM_BEACH = PopulatedPlace(
        name="Stem Beach",
        abbreviations=PlaceAbbreviations(
            three_letter="STE",
            five_letter="STEM ",
            seven_letter="STEM BE",
            fourteen_letter="STEM BEACH"
        ),
        latitude=38.16389961977825,
        longitude=-104.64359745619555,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    STEPPING_STONE = PopulatedPlace(
        name="Stepping Stone",
        abbreviations=PlaceAbbreviations(
            three_letter="STE",
            five_letter="STEPP",
            seven_letter="STEPPIN",
            fourteen_letter="STEPPING STONE"
        ),
        latitude=39.51376249882941,
        longitude=-104.82614294445824,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    STERLING = PopulatedPlace(
        name="Sterling",
        abbreviations=PlaceAbbreviations(
            three_letter="STE",
            five_letter="STERL",
            seven_letter="STERLIN",
            fourteen_letter="STERLING"
        ),
        latitude=40.625548166277156,
        longitude=-103.20771879414866,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    STERLING_RANCH = PopulatedPlace(
        name="Sterling Ranch",
        abbreviations=PlaceAbbreviations(
            three_letter="STE",
            five_letter="STERL",
            seven_letter="STERLIN",
            fourteen_letter="STERLING RANCH"
        ),
        latitude=39.50433618317675,
        longitude=-105.03678449099158,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    STOLLSTEIMER = PopulatedPlace(
        name="Stollsteimer",
        abbreviations=PlaceAbbreviations(
            three_letter="STO",
            five_letter="STOLL",
            seven_letter="STOLLST",
            fourteen_letter="STOLLSTEIMER"
        ),
        latitude=37.141676801270194,
        longitude=-107.35478016148187,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    STONE_CITY = PopulatedPlace(
        name="Stone City",
        abbreviations=PlaceAbbreviations(
            three_letter="STO",
            five_letter="STONE",
            seven_letter="STONE C",
            fourteen_letter="STONE CITY"
        ),
        latitude=38.44861744617202,
        longitude=-104.86110083612908,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    STONE_RIDGE_PARK = PopulatedPlace(
        name="Stone Ridge Park",
        abbreviations=PlaceAbbreviations(
            three_letter="STO",
            five_letter="STONE",
            seven_letter="STONE R",
            fourteen_letter="STONE RIDGE PA"
        ),
        latitude=39.68417312478732,
        longitude=-104.79556565672772,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    STONEGATE = PopulatedPlace(
        name="Stonegate",
        abbreviations=PlaceAbbreviations(
            three_letter="STO",
            five_letter="STONE",
            seven_letter="STONEGA",
            fourteen_letter="STONEGATE"
        ),
        latitude=39.530828602868326,
        longitude=-104.80387494105338,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    STONEHAM = PopulatedPlace(
        name="Stoneham",
        abbreviations=PlaceAbbreviations(
            three_letter="STO",
            five_letter="STONE",
            seven_letter="STONEHA",
            fourteen_letter="STONEHAM"
        ),
        latitude=40.60554653206873,
        longitude=-103.66662330166986,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    STONER = PopulatedPlace(
        name="Stoner",
        abbreviations=PlaceAbbreviations(
            three_letter="STO",
            five_letter="STONE",
            seven_letter="STONER",
            fourteen_letter="STONER"
        ),
        latitude=37.58944400102757,
        longitude=-108.3200947154225,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    STONEWALL = PopulatedPlace(
        name="Stonewall",
        abbreviations=PlaceAbbreviations(
            three_letter="STO",
            five_letter="STONE",
            seven_letter="STONEWA",
            fourteen_letter="STONEWALL"
        ),
        latitude=37.15224764780572,
        longitude=-105.01723344126538,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    STONINGTON = PopulatedPlace(
        name="Stonington",
        abbreviations=PlaceAbbreviations(
            three_letter="STO",
            five_letter="STONI",
            seven_letter="STONING",
            fourteen_letter="STONINGTON"
        ),
        latitude=37.29363574069106,
        longitude=-102.18741089397219,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    STOVE_PRAIRIE_LANDING = PopulatedPlace(
        name="Stove Prairie Landing",
        abbreviations=PlaceAbbreviations(
            three_letter="STO",
            five_letter="STOVE",
            seven_letter="STOVE P",
            fourteen_letter="STOVE PRAIRIE "
        ),
        latitude=40.68248791851141,
        longitude=-105.38916601484215,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    STRASBURG = PopulatedPlace(
        name="Strasburg",
        abbreviations=PlaceAbbreviations(
            three_letter="STR",
            five_letter="STRAS",
            seven_letter="STRASBU",
            fourteen_letter="STRASBURG"
        ),
        latitude=39.73832276453544,
        longitude=-104.32330245353336,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    STRATMOOR = PopulatedPlace(
        name="Stratmoor",
        abbreviations=PlaceAbbreviations(
            three_letter="STR",
            five_letter="STRAT",
            seven_letter="STRATMO",
            fourteen_letter="STRATMOOR"
        ),
        latitude=38.77388939789927,
        longitude=-104.77970505147863,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    STRATMOOR_HILLS = PopulatedPlace(
        name="Stratmoor Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="STR",
            five_letter="STRAT",
            seven_letter="STRATMO",
            fourteen_letter="STRATMOOR HILL"
        ),
        latitude=38.78305559830278,
        longitude=-104.79442755594147,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    """
    STRATTON = PopulatedPlace(
        name="Stratton",
        abbreviations=PlaceAbbreviations(
            three_letter="STR",
            five_letter="STRAT",
            seven_letter="STRATTO",
            fourteen_letter="STRATTON"
        ),
        latitude=38.74777237004082,
        longitude=-105.14999013368902,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    STRATTON = PopulatedPlace(
        name="Stratton",
        abbreviations=PlaceAbbreviations(
            three_letter="STR",
            five_letter="STRAT",
            seven_letter="STRATTO",
            fourteen_letter="STRATTON"
        ),
        latitude=39.30333411822744,
        longitude=-102.60465489741682,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    """
    STRATTON_MEADOWS = PopulatedPlace(
        name="Stratton Meadows",
        abbreviations=PlaceAbbreviations(
            three_letter="STR",
            five_letter="STRAT",
            seven_letter="STRATTO",
            fourteen_letter="STRATTON MEADO"
        ),
        latitude=38.80333259986878,
        longitude=-104.81165036199576,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    STRINGTOWN = PopulatedPlace(
        name="Stringtown",
        abbreviations=PlaceAbbreviations(
            three_letter="STR",
            five_letter="STRIN",
            seven_letter="STRINGT",
            fourteen_letter="STRINGTOWN"
        ),
        latitude=39.233607057765425,
        longitude=-106.31920145304105,
        counties=[Counties.LAKE],
        nearest_airport=Airports.ASPEN
    )
    STRONG = PopulatedPlace(
        name="Strong",
        abbreviations=PlaceAbbreviations(
            three_letter="STR",
            five_letter="STRON",
            seven_letter="STRONG",
            fourteen_letter="STRONG"
        ),
        latitude=37.7125168372375,
        longitude=-104.90222246961275,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    STUART = PopulatedPlace(
        name="Stuart",
        abbreviations=PlaceAbbreviations(
            three_letter="STU",
            five_letter="STUAR",
            seven_letter="STUART",
            fourteen_letter="STUART"
        ),
        latitude=38.47141082083493,
        longitude=-102.19463801111283,
        counties=[Counties.KIOWA],
        nearest_airport=Airports.PUEBLO
    )
    SUGAR = PopulatedPlace(
        name="Sugar",
        abbreviations=PlaceAbbreviations(
            three_letter="SUG",
            five_letter="SUGAR",
            seven_letter="SUGAR",
            fourteen_letter="SUGAR"
        ),
        latitude=38.150292442727334,
        longitude=-102.66853759171698,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    SUGAR_CITY = PopulatedPlace(
        name="Sugar City",
        abbreviations=PlaceAbbreviations(
            three_letter="SUG",
            five_letter="SUGAR",
            seven_letter="SUGAR C",
            fourteen_letter="SUGAR CITY"
        ),
        latitude=38.23195569224055,
        longitude=-103.66301073483965,
        counties=[Counties.CROWLEY],
        nearest_airport=Airports.PUEBLO
    )
    SUGAR_JUNCTION = PopulatedPlace(
        name="Sugar Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="SUG",
            five_letter="SUGAR",
            seven_letter="SUGAR J",
            fourteen_letter="SUGAR JUNCTION"
        ),
        latitude=37.56778673988509,
        longitude=-106.11253782894369,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    SULLIVAN = PopulatedPlace(
        name="Sullivan",
        abbreviations=PlaceAbbreviations(
            three_letter="SUL",
            five_letter="SULLI",
            seven_letter="SULLIVA",
            fourteen_letter="SULLIVAN"
        ),
        latitude=39.67138291611025,
        longitude=-104.89804387971196,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SUMMER_LAKE = PopulatedPlace(
        name="Summer Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="SUM",
            five_letter="SUMME",
            seven_letter="SUMMER ",
            fourteen_letter="SUMMER LAKE"
        ),
        latitude=39.636395319951816,
        longitude=-104.76723224469424,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SUMMER_VALLEY = PopulatedPlace(
        name="Summer Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="SUM",
            five_letter="SUMME",
            seven_letter="SUMMER ",
            fourteen_letter="SUMMER VALLEY"
        ),
        latitude=39.642506419737344,
        longitude=-104.78112114940438,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SUMMERVILLE = PopulatedPlace(
        name="Summerville",
        abbreviations=PlaceAbbreviations(
            three_letter="SUM",
            five_letter="SUMME",
            seven_letter="SUMMERV",
            fourteen_letter="SUMMERVILLE"
        ),
        latitude=40.05693673428732,
        longitude=-105.3944488390431,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SUNBEAM = PopulatedPlace(
        name="Sunbeam",
        abbreviations=PlaceAbbreviations(
            three_letter="SUN",
            five_letter="SUNBE",
            seven_letter="SUNBEAM",
            fourteen_letter="SUNBEAM"
        ),
        latitude=40.55080739506974,
        longitude=-108.1959330290772,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    SUNDOWN = PopulatedPlace(
        name="Sundown",
        abbreviations=PlaceAbbreviations(
            three_letter="SUN",
            five_letter="SUNDO",
            seven_letter="SUNDOWN",
            fourteen_letter="SUNDOWN"
        ),
        latitude=39.630006415629964,
        longitude=-104.82223225732793,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SUNLAND = PopulatedPlace(
        name="Sunland",
        abbreviations=PlaceAbbreviations(
            three_letter="SUN",
            five_letter="SUNLA",
            seven_letter="SUNLAND",
            fourteen_letter="SUNLAND"
        ),
        latitude=39.832784226087085,
        longitude=-105.07473233884735,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    """
    SUNNYSIDE = PopulatedPlace(
        name="Sunnyside",
        abbreviations=PlaceAbbreviations(
            three_letter="SUN",
            five_letter="SUNNY",
            seven_letter="SUNNYSI",
            fourteen_letter="SUNNYSIDE"
        ),
        latitude=40.00360372762157,
        longitude=-105.38167063021478,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SUNNYSIDE = PopulatedPlace(
        name="Sunnyside",
        abbreviations=PlaceAbbreviations(
            three_letter="SUN",
            five_letter="SUNNY",
            seven_letter="SUNNYSI",
            fourteen_letter="SUNNYSIDE"
        ),
        latitude=37.84611662513004,
        longitude=-106.96033444593746,
        counties=[Counties.MINERAL],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    """
    SUNNYSLOPE_ESTATES = PopulatedPlace(
        name="Sunnyslope Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="SUN",
            five_letter="SUNNY",
            seven_letter="SUNNYSL",
            fourteen_letter="SUNNYSLOPE EST"
        ),
        latitude=39.94250644458913,
        longitude=-105.04001014264918,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    SUNNYVALE = PopulatedPlace(
        name="Sunnyvale",
        abbreviations=PlaceAbbreviations(
            three_letter="SUN",
            five_letter="SUNNY",
            seven_letter="SUNNYVA",
            fourteen_letter="SUNNYVALE"
        ),
        latitude=39.723339724890025,
        longitude=-104.87251007983787,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    SUNSET = PopulatedPlace(
        name="Sunset",
        abbreviations=PlaceAbbreviations(
            three_letter="SUN",
            five_letter="SUNSE",
            seven_letter="SUNSET",
            fourteen_letter="SUNSET"
        ),
        latitude=40.03582602568105,
        longitude=-105.46889585403517,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    SUNSET_CITY = PopulatedPlace(
        name="Sunset City",
        abbreviations=PlaceAbbreviations(
            three_letter="SUN",
            five_letter="SUNSE",
            seven_letter="SUNSET ",
            fourteen_letter="SUNSET CITY"
        ),
        latitude=38.41250370485875,
        longitude=-105.4172277592657,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    SUNSET_RIDGE = PopulatedPlace(
        name="Sunset Ridge",
        abbreviations=PlaceAbbreviations(
            three_letter="SUN",
            five_letter="SUNSE",
            seven_letter="SUNSET ",
            fourteen_letter="SUNSET RIDGE"
        ),
        latitude=39.866117533025545,
        longitude=-105.0344545324358,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    SUNSTREAM = PopulatedPlace(
        name="Sunstream",
        abbreviations=PlaceAbbreviations(
            three_letter="SUN",
            five_letter="SUNST",
            seven_letter="SUNSTRE",
            fourteen_letter="SUNSTREAM"
        ),
        latitude=39.86778422860942,
        longitude=-105.10139904904196,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SUPERIOR = PopulatedPlace(
        name="Superior",
        abbreviations=PlaceAbbreviations(
            three_letter="SUP",
            five_letter="SUPER",
            seven_letter="SUPERIO",
            fourteen_letter="SUPERIOR"
        ),
        latitude=39.95276983553691,
        longitude=-105.16860787515753,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.DENVER
    )
    SUPREME_ESTATES = PopulatedPlace(
        name="Supreme Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="SUP",
            five_letter="SUPRE",
            seven_letter="SUPREME",
            fourteen_letter="SUPREME ESTATE"
        ),
        latitude=39.828339718812344,
        longitude=-105.17139906111953,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    SURREY_RIDGE = PopulatedPlace(
        name="Surrey Ridge",
        abbreviations=PlaceAbbreviations(
            three_letter="SUR",
            five_letter="SURRE",
            seven_letter="SURREY ",
            fourteen_letter="SURREY RIDGE"
        ),
        latitude=39.497806392708924,
        longitude=-104.88261005596951,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    SWALLOWS = PopulatedPlace(
        name="Swallows",
        abbreviations=PlaceAbbreviations(
            three_letter="SWA",
            five_letter="SWALL",
            seven_letter="SWALLOW",
            fourteen_letter="SWALLOWS"
        ),
        latitude=38.30223082565584,
        longitude=-104.86026912014347,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    SWINK = PopulatedPlace(
        name="Swink",
        abbreviations=PlaceAbbreviations(
            three_letter="SWI",
            five_letter="SWINK",
            seven_letter="SWINK",
            fourteen_letter="SWINK"
        ),
        latitude=38.01445926225392,
        longitude=-103.62828940461742,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    SWITZERLAND_PARK = PopulatedPlace(
        name="Switzerland Park",
        abbreviations=PlaceAbbreviations(
            three_letter="SWI",
            five_letter="SWITZ",
            seven_letter="SWITZER",
            fourteen_letter="SWITZERLAND PA"
        ),
        latitude=40.00138172399426,
        longitude=-105.43472804143653,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    TABERNASH = PopulatedPlace(
        name="Tabernash",
        abbreviations=PlaceAbbreviations(
            three_letter="TAB",
            five_letter="TABER",
            seven_letter="TABERNA",
            fourteen_letter="TABERNASH"
        ),
        latitude=39.993604094009925,
        longitude=-105.84307643466104,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    TABOR = PopulatedPlace(
        name="Tabor",
        abbreviations=PlaceAbbreviations(
            three_letter="TAB",
            five_letter="TABOR",
            seven_letter="TABOR",
            fourteen_letter="TABOR"
        ),
        latitude=40.051379956096866,
        longitude=-105.07415946432604,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    TACOMA = PopulatedPlace(
        name="Tacoma",
        abbreviations=PlaceAbbreviations(
            three_letter="TAC",
            five_letter="TACOM",
            seven_letter="TACOMA",
            fourteen_letter="TACOMA"
        ),
        latitude=37.52361642735963,
        longitude=-107.78202009279204,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    TALL_TIMBER = PopulatedPlace(
        name="Tall Timber",
        abbreviations=PlaceAbbreviations(
            three_letter="TAL",
            five_letter="TALL ",
            seven_letter="TALL TI",
            fourteen_letter="TALL TIMBER"
        ),
        latitude=40.01443683118583,
        longitude=-105.35166962431549,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    TAMPA = PopulatedPlace(
        name="Tampa",
        abbreviations=PlaceAbbreviations(
            three_letter="TAM",
            five_letter="TAMPA",
            seven_letter="TAMPA",
            fourteen_letter="TAMPA"
        ),
        latitude=40.14998851248862,
        longitude=-104.45552203246882,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    TANGLEWOOD_ACRES = PopulatedPlace(
        name="Tanglewood Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="TAN",
            five_letter="TANGL",
            seven_letter="TANGLEW",
            fourteen_letter="TANGLEWOOD ACR"
        ),
        latitude=38.093894450593325,
        longitude=-105.56168215880888,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    TARRYALL = PopulatedPlace(
        name="Tarryall",
        abbreviations=PlaceAbbreviations(
            three_letter="TAR",
            five_letter="TARRY",
            seven_letter="TARRYAL",
            fourteen_letter="TARRYALL"
        ),
        latitude=39.12194170015903,
        longitude=-105.47556554947403,
        counties=[Counties.PARK],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    TELLURIDE = PopulatedPlace(
        name="Telluride",
        abbreviations=PlaceAbbreviations(
            three_letter="TEL",
            five_letter="TELLU",
            seven_letter="TELLURI",
            fourteen_letter="TELLURIDE"
        ),
        latitude=37.937499881928375,
        longitude=-107.81229574152144,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    TENNYSON_PARK = PopulatedPlace(
        name="Tennyson Park",
        abbreviations=PlaceAbbreviations(
            three_letter="TEN",
            five_letter="TENNY",
            seven_letter="TENNYSO",
            fourteen_letter="TENNYSON PARK"
        ),
        latitude=39.811117524536485,
        longitude=-105.04862123126594,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    TERCIO = PopulatedPlace(
        name="Tercio",
        abbreviations=PlaceAbbreviations(
            three_letter="TER",
            five_letter="TERCI",
            seven_letter="TERCIO",
            fourteen_letter="TERCIO"
        ),
        latitude=37.051973134337686,
        longitude=-104.99667602689254,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    TEXAS_CREEK = PopulatedPlace(
        name="Texas Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="TEX",
            five_letter="TEXAS",
            seven_letter="TEXAS C",
            fourteen_letter="TEXAS CREEK"
        ),
        latitude=38.41305899455011,
        longitude=-105.5805656964987,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    THE_BLUFFS = PopulatedPlace(
        name="The Bluffs",
        abbreviations=PlaceAbbreviations(
            three_letter="THE",
            five_letter="THE B",
            seven_letter="THE BLU",
            fourteen_letter="THE BLUFFS"
        ),
        latitude=39.58639528130465,
        longitude=-105.22612124549698,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    THE_BROADLANDS = PopulatedPlace(
        name="The Broadlands",
        abbreviations=PlaceAbbreviations(
            three_letter="THE",
            five_letter="THE B",
            seven_letter="THE BRO",
            fourteen_letter="THE BROADLANDS"
        ),
        latitude=39.9511175455325,
        longitude=-105.02889904169831,
        counties=[Counties.BROOMFIELD],
        nearest_airport=Airports.DENVER
    )
    THE_HIGHLANDS = PopulatedPlace(
        name="The Highlands",
        abbreviations=PlaceAbbreviations(
            three_letter="THE",
            five_letter="THE H",
            seven_letter="THE HIG",
            fourteen_letter="THE HIGHLANDS"
        ),
        latitude=39.832784226087085,
        longitude=-105.06834343790166,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    THE_PINERY = PopulatedPlace(
        name="The Pinery",
        abbreviations=PlaceAbbreviations(
            three_letter="THE",
            five_letter="THE P",
            seven_letter="THE PIN",
            fourteen_letter="THE PINERY"
        ),
        latitude=39.455273497273254,
        longitude=-104.7344287169924,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    THE_POND = PopulatedPlace(
        name="The Pond",
        abbreviations=PlaceAbbreviations(
            three_letter="THE",
            five_letter="THE P",
            seven_letter="THE PON",
            fourteen_letter="THE POND"
        ),
        latitude=39.85417312683967,
        longitude=-105.10556574884174,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    THE_RIDGE_AT_STONY_CREEK = PopulatedPlace(
        name="The Ridge At Stony Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="THE",
            five_letter="THE R",
            seven_letter="THE RID",
            fourteen_letter="THE RIDGE AT S"
        ),
        latitude=39.58556199037184,
        longitude=-105.09417681514321,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    THE_VALLEY = PopulatedPlace(
        name="The Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="THE",
            five_letter="THE V",
            seven_letter="THE VAL",
            fourteen_letter="THE VALLEY"
        ),
        latitude=39.57528418466097,
        longitude=-105.16278792938357,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    THISTLEDOWN = PopulatedPlace(
        name="Thistledown",
        abbreviations=PlaceAbbreviations(
            three_letter="THI",
            five_letter="THIST",
            seven_letter="THISTLE",
            fourteen_letter="THISTLEDOWN"
        ),
        latitude=37.993611096572806,
        longitude=-107.69979302334747,
        counties=[Counties.OURAY],
        nearest_airport=Airports.TELLURIDE
    )
    THOMASVILLE = PopulatedPlace(
        name="Thomasville",
        abbreviations=PlaceAbbreviations(
            three_letter="THO",
            five_letter="THOMA",
            seven_letter="THOMASV",
            fourteen_letter="THOMASVILLE"
        ),
        latitude=39.36026994825551,
        longitude=-106.70254565355702,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    THORNBURGH = PopulatedPlace(
        name="Thornburgh",
        abbreviations=PlaceAbbreviations(
            three_letter="THO",
            five_letter="THORN",
            seven_letter="THORNBU",
            fourteen_letter="THORNBURGH"
        ),
        latitude=40.20692528824253,
        longitude=-107.6959114757683,
        counties=[Counties.RIO_BLANCO],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    THORNTON = PopulatedPlace(
        name="Thornton",
        abbreviations=PlaceAbbreviations(
            three_letter="THO",
            five_letter="THORN",
            seven_letter="THORNTO",
            fourteen_letter="THORNTON"
        ),
        latitude=39.8680476377578,
        longitude=-104.97193441982654,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    THUNDERBIRD_ESTATES = PopulatedPlace(
        name="Thunderbird Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="THU",
            five_letter="THUND",
            seven_letter="THUNDER",
            fourteen_letter="THUNDERBIRD ES"
        ),
        latitude=39.714450835000264,
        longitude=-104.70806564005858,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    THURMAN = PopulatedPlace(
        name="Thurman",
        abbreviations=PlaceAbbreviations(
            three_letter="THU",
            five_letter="THURM",
            seven_letter="THURMAN",
            fourteen_letter="THURMAN"
        ),
        latitude=39.59610341997592,
        longitude=-103.21744867606134,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    TIFFANY = PopulatedPlace(
        name="Tiffany",
        abbreviations=PlaceAbbreviations(
            three_letter="TIF",
            five_letter="TIFFA",
            seven_letter="TIFFANY",
            fourteen_letter="TIFFANY"
        ),
        latitude=37.03278817462507,
        longitude=-107.53811849023788,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    TIJERAS = PopulatedPlace(
        name="Tijeras",
        abbreviations=PlaceAbbreviations(
            three_letter="TIJ",
            five_letter="TIJER",
            seven_letter="TIJERAS",
            fourteen_letter="TIJERAS"
        ),
        latitude=37.125859665532516,
        longitude=-104.66305455741457,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    TIMNATH = PopulatedPlace(
        name="Timnath",
        abbreviations=PlaceAbbreviations(
            three_letter="TIM",
            five_letter="TIMNA",
            seven_letter="TIMNATH",
            fourteen_letter="TIMNATH"
        ),
        latitude=40.52915562719477,
        longitude=-104.98526350163803,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    TIMPAS = PopulatedPlace(
        name="Timpas",
        abbreviations=PlaceAbbreviations(
            three_letter="TIM",
            five_letter="TIMPA",
            seven_letter="TIMPAS",
            fourteen_letter="TIMPAS"
        ),
        latitude=37.818072923946204,
        longitude=-103.77412831911761,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    TINCUP = PopulatedPlace(
        name="Tincup",
        abbreviations=PlaceAbbreviations(
            three_letter="TIN",
            five_letter="TINCU",
            seven_letter="TINCUP",
            fourteen_letter="TINCUP"
        ),
        latitude=38.75444548160198,
        longitude=-106.47837083545318,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    TIOGA = PopulatedPlace(
        name="Tioga",
        abbreviations=PlaceAbbreviations(
            three_letter="TIO",
            five_letter="TIOGA",
            seven_letter="TIOGA",
            fourteen_letter="TIOGA"
        ),
        latitude=37.698905633913796,
        longitude=-104.92750117399731,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    TOBE = PopulatedPlace(
        name="Tobe",
        abbreviations=PlaceAbbreviations(
            three_letter="TOB",
            five_letter="TOBE",
            seven_letter="TOBE",
            fourteen_letter="TOBE"
        ),
        latitude=37.21919204389451,
        longitude=-103.61162542343328,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    TOBIN = PopulatedPlace(
        name="Tobin",
        abbreviations=PlaceAbbreviations(
            three_letter="TOB",
            five_letter="TOBIN",
            seven_letter="TOBIN",
            fourteen_letter="TOBIN"
        ),
        latitude=40.834164118936485,
        longitude=-102.87270463953621,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    TODD_CREEK = PopulatedPlace(
        name="Todd Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="TOD",
            five_letter="TODD ",
            seven_letter="TODD CR",
            fourteen_letter="TODD CREEK"
        ),
        latitude=39.97804625997202,
        longitude=-104.87331850969463,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    TOLLAND = PopulatedPlace(
        name="Tolland",
        abbreviations=PlaceAbbreviations(
            three_letter="TOL",
            five_letter="TOLLA",
            seven_letter="TOLLAND",
            fourteen_letter="TOLLAND"
        ),
        latitude=39.904993599590114,
        longitude=-105.58917736542713,
        counties=[Counties.GILPIN],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    TOLLGATE = PopulatedPlace(
        name="Tollgate",
        abbreviations=PlaceAbbreviations(
            three_letter="TOL",
            five_letter="TOLLG",
            seven_letter="TOLLGAT",
            fourteen_letter="TOLLGATE"
        ),
        latitude=39.70028422761817,
        longitude=-104.79112115831629,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    TOMAH = PopulatedPlace(
        name="Tomah",
        abbreviations=PlaceAbbreviations(
            three_letter="TOM",
            five_letter="TOMAH",
            seven_letter="TOMAH",
            fourteen_letter="TOMAH"
        ),
        latitude=39.30194116507374,
        longitude=-104.88999063500506,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    TONVILLE = PopulatedPlace(
        name="Tonville",
        abbreviations=PlaceAbbreviations(
            three_letter="TON",
            five_letter="TONVI",
            seven_letter="TONVILL",
            fourteen_letter="TONVILLE"
        ),
        latitude=40.00915657597727,
        longitude=-104.70386637363492,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    TOONERVILLE = PopulatedPlace(
        name="Toonerville",
        abbreviations=PlaceAbbreviations(
            three_letter="TOO",
            five_letter="TOONE",
            seven_letter="TOONERV",
            fourteen_letter="TOONERVILLE"
        ),
        latitude=37.77501535496663,
        longitude=-103.16410677198252,
        counties=[Counties.BENT],
        nearest_airport=Airports.PUEBLO
    )
    TOPONAS = PopulatedPlace(
        name="Toponas",
        abbreviations=PlaceAbbreviations(
            three_letter="TOP",
            five_letter="TOPON",
            seven_letter="TOPONAS",
            fourteen_letter="TOPONAS"
        ),
        latitude=40.060270233626284,
        longitude=-106.80810896072143,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.EAGLE
    )
    TORDAL_ESTATES = PopulatedPlace(
        name="Tordal Estates",
        abbreviations=PlaceAbbreviations(
            three_letter="TOR",
            five_letter="TORDA",
            seven_letter="TORDAL ",
            fourteen_letter="TORDAL ESTATES"
        ),
        latitude=39.38450629714083,
        longitude=-106.05041030975809,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.ASPEN
    )
    """
    TORRES = PopulatedPlace(
        name="Torres",
        abbreviations=PlaceAbbreviations(
            three_letter="TOR",
            five_letter="TORRE",
            seven_letter="TORRES",
            fourteen_letter="TORRES"
        ),
        latitude=37.069472333375586,
        longitude=-105.05612244236613,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    TORRES = PopulatedPlace(
        name="Torres",
        abbreviations=PlaceAbbreviations(
            three_letter="TOR",
            five_letter="TORRE",
            seven_letter="TORRES",
            fourteen_letter="TORRES"
        ),
        latitude=37.606675739843524,
        longitude=-106.20448495363019,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    """
    TOWAOC = PopulatedPlace(
        name="Towaoc",
        abbreviations=PlaceAbbreviations(
            three_letter="TOW",
            five_letter="TOWAO",
            seven_letter="TOWAOC",
            fourteen_letter="TOWAOC"
        ),
        latitude=37.204444522639506,
        longitude=-108.72955216330683,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    TRAPPER = PopulatedPlace(
        name="Trapper",
        abbreviations=PlaceAbbreviations(
            three_letter="TRA",
            five_letter="TRAPP",
            seven_letter="TRAPPER",
            fourteen_letter="TRAPPER"
        ),
        latitude=40.103880034394194,
        longitude=-106.87977848187319,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.EAGLE
    )
    TRAVOIS = PopulatedPlace(
        name="Travois",
        abbreviations=PlaceAbbreviations(
            three_letter="TRA",
            five_letter="TRAVO",
            seven_letter="TRAVOIS",
            fourteen_letter="TRAVOIS"
        ),
        latitude=39.56583971217583,
        longitude=-104.73945443078253,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    TREASURE = PopulatedPlace(
        name="Treasure",
        abbreviations=PlaceAbbreviations(
            three_letter="TRE",
            five_letter="TREAS",
            seven_letter="TREASUR",
            fourteen_letter="TREASURE"
        ),
        latitude=37.31251204976297,
        longitude=-106.9656054932251,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    TRILBY_CORNER = PopulatedPlace(
        name="Trilby Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="TRI",
            five_letter="TRILB",
            seven_letter="TRILBY ",
            fourteen_letter="TRILBY CORNER"
        ),
        latitude=40.49471141583609,
        longitude=-105.07748941937126,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    TRIMBLE = PopulatedPlace(
        name="Trimble",
        abbreviations=PlaceAbbreviations(
            three_letter="TRI",
            five_letter="TRIMB",
            seven_letter="TRIMBLE",
            fourteen_letter="TRIMBLE"
        ),
        latitude=37.390284404882664,
        longitude=-107.84646589243494,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    TRINCHERA = PopulatedPlace(
        name="Trinchera",
        abbreviations=PlaceAbbreviations(
            three_letter="TRI",
            five_letter="TRINC",
            seven_letter="TRINCHE",
            fourteen_letter="TRINCHERA"
        ),
        latitude=37.04225059058075,
        longitude=-104.04748030791256,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    TRINIDAD = PopulatedPlace(
        name="Trinidad",
        abbreviations=PlaceAbbreviations(
            three_letter="TRI",
            five_letter="TRINI",
            seven_letter="TRINIDA",
            fourteen_letter="TRINIDAD"
        ),
        latitude=37.16946928227463,
        longitude=-104.5005504247502,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    TROUBLESOME = PopulatedPlace(
        name="Troublesome",
        abbreviations=PlaceAbbreviations(
            three_letter="TRO",
            five_letter="TROUB",
            seven_letter="TROUBLE",
            fourteen_letter="TROUBLESOME"
        ),
        latitude=40.06082497090944,
        longitude=-106.29170504447688,
        counties=[Counties.GRAND],
        nearest_airport=Airports.EAGLE
    )
    TROUTDALE = PopulatedPlace(
        name="Troutdale",
        abbreviations=PlaceAbbreviations(
            three_letter="TRO",
            five_letter="TROUT",
            seven_letter="TROUTDA",
            fourteen_letter="TROUTDALE"
        ),
        latitude=39.63693888025813,
        longitude=-105.34805897898173,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    TRUCKTON = PopulatedPlace(
        name="Truckton",
        abbreviations=PlaceAbbreviations(
            three_letter="TRU",
            five_letter="TRUCK",
            seven_letter="TRUCKTO",
            fourteen_letter="TRUCKTON"
        ),
        latitude=38.73805703230869,
        longitude=-104.18219100945419,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    TRUJILLO = PopulatedPlace(
        name="Trujillo",
        abbreviations=PlaceAbbreviations(
            three_letter="TRU",
            five_letter="TRUJI",
            seven_letter="TRUJILL",
            fourteen_letter="TRUJILLO"
        ),
        latitude=37.100569015081646,
        longitude=-107.04699358919493,
        counties=[Counties.ARCHULETA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    TRUMBULL = PopulatedPlace(
        name="Trumbull",
        abbreviations=PlaceAbbreviations(
            three_letter="TRU",
            five_letter="TRUMB",
            seven_letter="TRUMBUL",
            fourteen_letter="TRUMBULL"
        ),
        latitude=39.26305213857046,
        longitude=-105.21944790649133,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    TURRET = PopulatedPlace(
        name="Turret",
        abbreviations=PlaceAbbreviations(
            three_letter="TUR",
            five_letter="TURRE",
            seven_letter="TURRET",
            fourteen_letter="TURRET"
        ),
        latitude=38.64028049888316,
        longitude=-105.98891181339224,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    TWELVEMILE_CORNER = PopulatedPlace(
        name="Twelvemile Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="TWE",
            five_letter="TWELV",
            seven_letter="TWELVEM",
            fourteen_letter="TWELVEMILE COR"
        ),
        latitude=40.07332344837681,
        longitude=-103.79273746730212,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    TWIN_CEDARS = PopulatedPlace(
        name="Twin Cedars",
        abbreviations=PlaceAbbreviations(
            three_letter="TWI",
            five_letter="TWIN ",
            seven_letter="TWIN CE",
            fourteen_letter="TWIN CEDARS"
        ),
        latitude=39.35971815450171,
        longitude=-105.16722270622711,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    TWIN_FORKS = PopulatedPlace(
        name="Twin Forks",
        abbreviations=PlaceAbbreviations(
            three_letter="TWI",
            five_letter="TWIN ",
            seven_letter="TWIN FO",
            fourteen_letter="TWIN FORKS"
        ),
        latitude=39.59277218260888,
        longitude=-105.21972224479265,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    TWIN_LAKES = PopulatedPlace(
        name="Twin Lakes",
        abbreviations=PlaceAbbreviations(
            three_letter="TWI",
            five_letter="TWIN ",
            seven_letter="TWIN LA",
            fourteen_letter="TWIN LAKES"
        ),
        latitude=39.82499252979164,
        longitude=-105.0047137217619,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    TWIN_MILLS = PopulatedPlace(
        name="Twin Mills",
        abbreviations=PlaceAbbreviations(
            three_letter="TWI",
            five_letter="TWIN ",
            seven_letter="TWIN MI",
            fourteen_letter="TWIN MILLS"
        ),
        latitude=40.573604864885624,
        longitude=-103.1263299687468,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    TWIN_SPRUCE = PopulatedPlace(
        name="Twin Spruce",
        abbreviations=PlaceAbbreviations(
            three_letter="TWI",
            five_letter="TWIN ",
            seven_letter="TWIN SP",
            fourteen_letter="TWIN SPRUCE"
        ),
        latitude=39.88915991388512,
        longitude=-105.35861411080657,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    TWO_BUTTES = PopulatedPlace(
        name="Two Buttes",
        abbreviations=PlaceAbbreviations(
            three_letter="TWO",
            five_letter="TWO B",
            seven_letter="TWO BUT",
            fourteen_letter="TWO BUTTES"
        ),
        latitude=37.56113066965287,
        longitude=-102.39769796978601,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    TYRONE = PopulatedPlace(
        name="Tyrone",
        abbreviations=PlaceAbbreviations(
            three_letter="TYR",
            five_letter="TYRON",
            seven_letter="TYRONE",
            fourteen_letter="TYRONE"
        ),
        latitude=37.454187242768796,
        longitude=-104.20831438442895,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    UNA = PopulatedPlace(
        name="Una",
        abbreviations=PlaceAbbreviations(
            three_letter="UNA",
            five_letter="UNA",
            seven_letter="UNA",
            fourteen_letter="UNA"
        ),
        latitude=39.399706654812064,
        longitude=-108.10869916885378,
        counties=[Counties.GARFIELD],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    UNCOMPAHGRE = PopulatedPlace(
        name="Uncompahgre",
        abbreviations=PlaceAbbreviations(
            three_letter="UNC",
            five_letter="UNCOM",
            seven_letter="UNCOMPA",
            fourteen_letter="UNCOMPAHGRE"
        ),
        latitude=38.37804914032074,
        longitude=-107.81868239039073,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    UNION = PopulatedPlace(
        name="Union",
        abbreviations=PlaceAbbreviations(
            three_letter="UNI",
            five_letter="UNION",
            seven_letter="UNION",
            fourteen_letter="UNION"
        ),
        latitude=40.37665311095395,
        longitude=-103.50106453412008,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    UNIVERSITY_HILLS = PopulatedPlace(
        name="University Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="UNI",
            five_letter="UNIVE",
            seven_letter="UNIVERS",
            fourteen_letter="UNIVERSITY HIL"
        ),
        latitude=39.66528421169693,
        longitude=-104.94723229012396,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    UNIVERSITY_PARK = PopulatedPlace(
        name="University Park",
        abbreviations=PlaceAbbreviations(
            three_letter="UNI",
            five_letter="UNIVE",
            seven_letter="UNIVERS",
            fourteen_letter="UNIVERSITY PAR"
        ),
        latitude=39.67861751213883,
        longitude=-104.96945449651724,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    UPPER_WITTER_GULCH = PopulatedPlace(
        name="Upper Witter Gulch",
        abbreviations=PlaceAbbreviations(
            three_letter="UPP",
            five_letter="UPPER",
            seven_letter="UPPER W",
            fourteen_letter="UPPER WITTER G"
        ),
        latitude=39.66018657782422,
        longitude=-105.42802910044531,
        counties=[Counties.CLEAR_CREEK],
        nearest_airport=Airports.DENVER
    )
    URAVAN = PopulatedPlace(
        name="Uravan",
        abbreviations=PlaceAbbreviations(
            three_letter="URA",
            five_letter="URAVA",
            seven_letter="URAVAN",
            fourteen_letter="URAVAN"
        ),
        latitude=38.368328477708474,
        longitude=-108.73649788677807,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    UTAH_JUNCTION = PopulatedPlace(
        name="Utah Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="UTA",
            five_letter="UTAH ",
            seven_letter="UTAH JU",
            fourteen_letter="UTAH JUNCTION"
        ),
        latitude=39.800548327145066,
        longitude=-104.9980470177129,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    UTALINE = PopulatedPlace(
        name="Utaline",
        abbreviations=PlaceAbbreviations(
            three_letter="UTA",
            five_letter="UTALI",
            seven_letter="UTALINE",
            fourteen_letter="UTALINE"
        ),
        latitude=39.12693335400928,
        longitude=-109.04234383753993,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    UTE = PopulatedPlace(
        name="Ute",
        abbreviations=PlaceAbbreviations(
            three_letter="UTE",
            five_letter="UTE",
            seven_letter="UTE",
            fourteen_letter="UTE"
        ),
        latitude=38.25555069372797,
        longitude=-108.27120237445672,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    UTLEYVILLE = PopulatedPlace(
        name="Utleyville",
        abbreviations=PlaceAbbreviations(
            three_letter="UTL",
            five_letter="UTLEY",
            seven_letter="UTLEYVI",
            fourteen_letter="UTLEYVILLE"
        ),
        latitude=37.271134386849496,
        longitude=-103.03132779325495,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    VAIL = PopulatedPlace(
        name="Vail",
        abbreviations=PlaceAbbreviations(
            three_letter="VAI",
            five_letter="VAIL",
            seven_letter="VAIL",
            fourteen_letter="VAIL"
        ),
        latitude=39.640270108853656,
        longitude=-106.374205911437,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    VALLECITO = PopulatedPlace(
        name="Vallecito",
        abbreviations=PlaceAbbreviations(
            three_letter="VAL",
            five_letter="VALLE",
            seven_letter="VALLECI",
            fourteen_letter="VALLECITO"
        ),
        latitude=37.37528601966545,
        longitude=-107.58395703444643,
        counties=[Counties.LA_PLATA],
        nearest_airport=Airports.DURANGO_LA_PLATA
    )
    VALLEY_VIEW = PopulatedPlace(
        name="Valley View",
        abbreviations=PlaceAbbreviations(
            three_letter="VAL",
            five_letter="VALLE",
            seven_letter="VALLEY ",
            fourteen_letter="VALLEY VIEW"
        ),
        latitude=38.06834598440395,
        longitude=-104.97694242243261,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    VALLIE = PopulatedPlace(
        name="Vallie",
        abbreviations=PlaceAbbreviations(
            three_letter="VAL",
            five_letter="VALLI",
            seven_letter="VALLIE",
            fourteen_letter="VALLIE"
        ),
        latitude=38.394170478676074,
        longitude=-105.77251603733953,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    VALLORSO = PopulatedPlace(
        name="Vallorso",
        abbreviations=PlaceAbbreviations(
            three_letter="VAL",
            five_letter="VALLO",
            seven_letter="VALLORS",
            fourteen_letter="VALLORSO"
        ),
        latitude=37.282800590214265,
        longitude=-104.64499686881322,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    VANADIUM = PopulatedPlace(
        name="Vanadium",
        abbreviations=PlaceAbbreviations(
            three_letter="VAN",
            five_letter="VANAD",
            seven_letter="VANADIU",
            fourteen_letter="VANADIUM"
        ),
        latitude=37.96694317507166,
        longitude=-107.9717440795755,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    VANCE_JUNCTION = PopulatedPlace(
        name="Vance Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="VAN",
            five_letter="VANCE",
            seven_letter="VANCE J",
            fourteen_letter="VANCE JUNCTION"
        ),
        latitude=37.935555075565844,
        longitude=-107.89868706016188,
        counties=[Counties.SAN_MIGUEL],
        nearest_airport=Airports.TELLURIDE
    )
    VANCORUM = PopulatedPlace(
        name="Vancorum",
        abbreviations=PlaceAbbreviations(
            three_letter="VAN",
            five_letter="VANCO",
            seven_letter="VANCORU",
            fourteen_letter="VANCORUM"
        ),
        latitude=38.231663168998125,
        longitude=-108.59565934189891,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.TELLURIDE
    )
    VASTINE = PopulatedPlace(
        name="Vastine",
        abbreviations=PlaceAbbreviations(
            three_letter="VAS",
            five_letter="VASTI",
            seven_letter="VASTINE",
            fourteen_letter="VASTINE"
        ),
        latitude=37.63445245042669,
        longitude=-106.10337063375869,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    VELASQUEZ_PLAZA = PopulatedPlace(
        name="Velasquez Plaza",
        abbreviations=PlaceAbbreviations(
            three_letter="VEL",
            five_letter="VELAS",
            seven_letter="VELASQU",
            fourteen_letter="VELASQUEZ PLAZ"
        ),
        latitude=37.12363765814695,
        longitude=-104.78250198486182,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    VERNAL = PopulatedPlace(
        name="Vernal",
        abbreviations=PlaceAbbreviations(
            three_letter="VER",
            five_letter="VERNA",
            seven_letter="VERNAL",
            fourteen_letter="VERNAL"
        ),
        latitude=38.38971564174062,
        longitude=-107.82923829386857,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.MONTROSE
    )
    VERNON_GARDENS = PopulatedPlace(
        name="Vernon Gardens",
        abbreviations=PlaceAbbreviations(
            three_letter="VER",
            five_letter="VERNO",
            seven_letter="VERNON ",
            fourteen_letter="VERNON GARDENS"
        ),
        latitude=39.73250640436311,
        longitude=-105.18834345321613,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    VICKSBURG = PopulatedPlace(
        name="Vicksburg",
        abbreviations=PlaceAbbreviations(
            three_letter="VIC",
            five_letter="VICKS",
            seven_letter="VICKSBU",
            fourteen_letter="VICKSBURG"
        ),
        latitude=38.99916642208831,
        longitude=-106.3778129392552,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.ASPEN
    )
    VICTOR = PopulatedPlace(
        name="Victor",
        abbreviations=PlaceAbbreviations(
            three_letter="VIC",
            five_letter="VICTO",
            seven_letter="VICTOR",
            fourteen_letter="VICTOR"
        ),
        latitude=38.70999586538289,
        longitude=-105.13999072754666,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    VIEJO_SAN_ACACIO = PopulatedPlace(
        name="Viejo San Acacio",
        abbreviations=PlaceAbbreviations(
            three_letter="VIE",
            five_letter="VIEJO",
            seven_letter="VIEJO S",
            fourteen_letter="VIEJO SAN ACAC"
        ),
        latitude=37.202798225000834,
        longitude=-105.50835585756823,
        counties=[Counties.COSTILLA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    VIGIL = PopulatedPlace(
        name="Vigil",
        abbreviations=PlaceAbbreviations(
            three_letter="VIG",
            five_letter="VIGIL",
            seven_letter="VIGIL",
            fourteen_letter="VIGIL"
        ),
        latitude=37.16113655426818,
        longitude=-104.94167492460252,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    VILAS = PopulatedPlace(
        name="Vilas",
        abbreviations=PlaceAbbreviations(
            three_letter="VIL",
            five_letter="VILAS",
            seven_letter="VILAS",
            fourteen_letter="VILAS"
        ),
        latitude=37.37363343792504,
        longitude=-102.44631026365687,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    VILLA_GROVE = PopulatedPlace(
        name="Villa Grove",
        abbreviations=PlaceAbbreviations(
            three_letter="VIL",
            five_letter="VILLA",
            seven_letter="VILLA G",
            fourteen_letter="VILLA GROVE"
        ),
        latitude=38.248616347239306,
        longitude=-105.94918996263198,
        counties=[Counties.SAGUACHE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    VILLAGE_EAST = PopulatedPlace(
        name="Village East",
        abbreviations=PlaceAbbreviations(
            three_letter="VIL",
            five_letter="VILLA",
            seven_letter="VILLAGE",
            fourteen_letter="VILLAGE EAST"
        ),
        latitude=39.68333972088726,
        longitude=-104.85084337005662,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    VILLAGE_GREEN = PopulatedPlace(
        name="Village Green",
        abbreviations=PlaceAbbreviations(
            three_letter="VIL",
            five_letter="VILLA",
            seven_letter="VILLAGE",
            fourteen_letter="VILLAGE GREEN"
        ),
        latitude=39.693895324997015,
        longitude=-104.81362116242286,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    VILLAGE_PINES = PopulatedPlace(
        name="Village Pines",
        abbreviations=PlaceAbbreviations(
            three_letter="VIL",
            five_letter="VILLA",
            seven_letter="VILLAGE",
            fourteen_letter="VILLAGE PINES"
        ),
        latitude=39.3800063874815,
        longitude=-104.72389890598032,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    VILLAGE_OF_FIVE_PARKS = PopulatedPlace(
        name="Village of Five Parks",
        abbreviations=PlaceAbbreviations(
            three_letter="VIL",
            five_letter="VILLA",
            seven_letter="VILLAGE",
            fourteen_letter="VILLAGE OF FIV"
        ),
        latitude=39.848617521833205,
        longitude=-105.1597323602503,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    VILLEGREEN = PopulatedPlace(
        name="Villegreen",
        abbreviations=PlaceAbbreviations(
            three_letter="VIL",
            five_letter="VILLE",
            seven_letter="VILLEGR",
            fourteen_letter="VILLEGREEN"
        ),
        latitude=37.3058575624471,
        longitude=-103.52023171036927,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    VISTA_POINTE = PopulatedPlace(
        name="Vista Pointe",
        abbreviations=PlaceAbbreviations(
            three_letter="VIS",
            five_letter="VISTA",
            seven_letter="VISTA P",
            fourteen_letter="VISTA POINTE"
        ),
        latitude=39.53982640246295,
        longitude=-104.83423904958391,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    VOLLMAR = PopulatedPlace(
        name="Vollmar",
        abbreviations=PlaceAbbreviations(
            three_letter="VOL",
            five_letter="VOLLM",
            seven_letter="VOLLMAR",
            fourteen_letter="VOLLMAR"
        ),
        latitude=40.1349897839205,
        longitude=-104.83887171989466,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    VONA = PopulatedPlace(
        name="Vona",
        abbreviations=PlaceAbbreviations(
            three_letter="VON",
            five_letter="VONA",
            seven_letter="VONA",
            fourteen_letter="VONA"
        ),
        latitude=39.303610909350255,
        longitude=-102.74299263046106,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.DENVER
    )
    VROMAN = PopulatedPlace(
        name="Vroman",
        abbreviations=PlaceAbbreviations(
            three_letter="VRO",
            five_letter="VROMA",
            seven_letter="VROMAN",
            fourteen_letter="VROMAN"
        ),
        latitude=38.08973556208616,
        longitude=-103.81024015516135,
        counties=[Counties.OTERO],
        nearest_airport=Airports.PUEBLO
    )
    WAH_KEENEY_PARK = PopulatedPlace(
        name="Wah Keeney Park",
        abbreviations=PlaceAbbreviations(
            three_letter="WAH",
            five_letter="WAH K",
            seven_letter="WAH KEE",
            fourteen_letter="WAH KEENEY PAR"
        ),
        latitude=39.66027218414945,
        longitude=-105.34055857995855,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WALDEN = PopulatedPlace(
        name="Walden",
        abbreviations=PlaceAbbreviations(
            three_letter="WAL",
            five_letter="WALDE",
            seven_letter="WALDEN",
            fourteen_letter="WALDEN"
        ),
        latitude=40.7316497593207,
        longitude=-106.28364782562318,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    WALKER = PopulatedPlace(
        name="Walker",
        abbreviations=PlaceAbbreviations(
            three_letter="WAL",
            five_letter="WALKE",
            seven_letter="WALKER",
            fourteen_letter="WALKER"
        ),
        latitude=40.26443459369398,
        longitude=-104.95220906190087,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WALLACE_VILLAGE = PopulatedPlace(
        name="Wallace Village",
        abbreviations=PlaceAbbreviations(
            three_letter="WAL",
            five_letter="WALLA",
            seven_letter="WALLACE",
            fourteen_letter="WALLACE VILLAG"
        ),
        latitude=39.88332553139492,
        longitude=-105.09277194885351,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WALLSTREET = PopulatedPlace(
        name="Wallstreet",
        abbreviations=PlaceAbbreviations(
            three_letter="WAL",
            five_letter="WALLS",
            seven_letter="WALLSTR",
            fourteen_letter="WALLSTREET"
        ),
        latitude=40.038881332015364,
        longitude=-105.3908376358554,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WALNUT_GROVE = PopulatedPlace(
        name="Walnut Grove",
        abbreviations=PlaceAbbreviations(
            three_letter="WAL",
            five_letter="WALNU",
            seven_letter="WALNUT ",
            fourteen_letter="WALNUT GROVE"
        ),
        latitude=39.88778423153542,
        longitude=-105.10334345247446,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WALSENBURG = PopulatedPlace(
        name="Walsenburg",
        abbreviations=PlaceAbbreviations(
            three_letter="WAL",
            five_letter="WALSE",
            seven_letter="WALSENB",
            fourteen_letter="WALSENBURG"
        ),
        latitude=37.62418543204245,
        longitude=-104.78027433273883,
        counties=[Counties.HUERFANO],
        nearest_airport=Airports.PUEBLO
    )
    WALSH = PopulatedPlace(
        name="Walsh",
        abbreviations=PlaceAbbreviations(
            three_letter="WAL",
            five_letter="WALSH",
            seven_letter="WALSH",
            fourteen_letter="WALSH"
        ),
        latitude=37.38613334973962,
        longitude=-102.27824862443555,
        counties=[Counties.BACA],
        nearest_airport=Airports.PUEBLO
    )
    WALTONIA = PopulatedPlace(
        name="Waltonia",
        abbreviations=PlaceAbbreviations(
            three_letter="WAL",
            five_letter="WALTO",
            seven_letter="WALTONI",
            fourteen_letter="WALTONIA"
        ),
        latitude=40.41387908421626,
        longitude=-105.36305717550692,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WALTS_CORNER = PopulatedPlace(
        name="Walts Corner",
        abbreviations=PlaceAbbreviations(
            three_letter="WAL",
            five_letter="WALTS",
            seven_letter="WALTS C",
            fourteen_letter="WALTS CORNER"
        ),
        latitude=37.168915019629424,
        longitude=-103.87997138142441,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.PUEBLO
    )
    WANDCREST_PARK = PopulatedPlace(
        name="Wandcrest Park",
        abbreviations=PlaceAbbreviations(
            three_letter="WAN",
            five_letter="WANDC",
            seven_letter="WANDCRE",
            fourteen_letter="WANDCREST PARK"
        ),
        latitude=39.435550949207254,
        longitude=-105.39389566637249,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WANDERING_VIEW = PopulatedPlace(
        name="Wandering View",
        abbreviations=PlaceAbbreviations(
            three_letter="WAN",
            five_letter="WANDE",
            seven_letter="WANDERI",
            fourteen_letter="WANDERING VIEW"
        ),
        latitude=39.8883397364786,
        longitude=-105.03028793414552,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    WARD = PopulatedPlace(
        name="Ward",
        abbreviations=PlaceAbbreviations(
            three_letter="WAR",
            five_letter="WARD",
            seven_letter="WARD",
            fourteen_letter="WARD"
        ),
        latitude=40.072214728272456,
        longitude=-105.50834186720596,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WARELAND = PopulatedPlace(
        name="Wareland",
        abbreviations=PlaceAbbreviations(
            three_letter="WAR",
            five_letter="WAREL",
            seven_letter="WARELAN",
            fourteen_letter="WARELAND"
        ),
        latitude=39.09249854749743,
        longitude=-103.21578122053597,
        counties=[Counties.LINCOLN],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    WARREN = PopulatedPlace(
        name="Warren",
        abbreviations=PlaceAbbreviations(
            three_letter="WAR",
            five_letter="WARRE",
            seven_letter="WARREN",
            fourteen_letter="WARREN"
        ),
        latitude=40.9597124913393,
        longitude=-104.89220213452091,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WARWICK = PopulatedPlace(
        name="Warwick",
        abbreviations=PlaceAbbreviations(
            three_letter="WAR",
            five_letter="WARWI",
            seven_letter="WARWICK",
            fourteen_letter="WARWICK"
        ),
        latitude=38.12390476309787,
        longitude=-102.27408759480187,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    WATERTON = PopulatedPlace(
        name="Waterton",
        abbreviations=PlaceAbbreviations(
            three_letter="WAT",
            five_letter="WATER",
            seven_letter="WATERTO",
            fourteen_letter="WATERTON"
        ),
        latitude=39.49360597815979,
        longitude=-105.0886076026398,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WATTENBERG = PopulatedPlace(
        name="Wattenberg",
        abbreviations=PlaceAbbreviations(
            three_letter="WAT",
            five_letter="WATTE",
            seven_letter="WATTENB",
            fourteen_letter="WATTENBERG"
        ),
        latitude=40.02776796940992,
        longitude=-104.83664990682087,
        counties=[Counties.WELD],
        nearest_airport=Airports.DENVER
    )
    WAUNETA = PopulatedPlace(
        name="Wauneta",
        abbreviations=PlaceAbbreviations(
            three_letter="WAU",
            five_letter="WAUNE",
            seven_letter="WAUNETA",
            fourteen_letter="WAUNETA"
        ),
        latitude=40.29305208546049,
        longitude=-102.2546487248917,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    WAUNITA_HOT_SPRINGS = PopulatedPlace(
        name="Waunita Hot Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="WAU",
            five_letter="WAUNI",
            seven_letter="WAUNITA",
            fourteen_letter="WAUNITA HOT SP"
        ),
        latitude=38.514167447136685,
        longitude=-106.5083732157749,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    """
    WAVERLY = PopulatedPlace(
        name="Waverly",
        abbreviations=PlaceAbbreviations(
            three_letter="WAV",
            five_letter="WAVER",
            seven_letter="WAVERLY",
            fourteen_letter="WAVERLY"
        ),
        latitude=37.42973292680142,
        longitude=-106.00614599121974,
        counties=[Counties.ALAMOSA],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    WAVERLY = PopulatedPlace(
        name="Waverly",
        abbreviations=PlaceAbbreviations(
            three_letter="WAV",
            five_letter="WAVER",
            seven_letter="WAVERLY",
            fourteen_letter="WAVERLY"
        ),
        latitude=40.736377448185976,
        longitude=-105.07665344896441,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    """
    WEBER = PopulatedPlace(
        name="Weber",
        abbreviations=PlaceAbbreviations(
            three_letter="WEB",
            five_letter="WEBER",
            seven_letter="WEBER",
            fourteen_letter="WEBER"
        ),
        latitude=37.31250226585007,
        longitude=-108.28925908030112,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    WEBSTER = PopulatedPlace(
        name="Webster",
        abbreviations=PlaceAbbreviations(
            three_letter="WEB",
            five_letter="WEBST",
            seven_letter="WEBSTER",
            fourteen_letter="WEBSTER"
        ),
        latitude=39.457493729493024,
        longitude=-105.72029484445972,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    WELBY = PopulatedPlace(
        name="Welby",
        abbreviations=PlaceAbbreviations(
            three_letter="WEL",
            five_letter="WELBY",
            seven_letter="WELBY",
            fourteen_letter="WELBY"
        ),
        latitude=39.83665913458481,
        longitude=-104.959156212795,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    WELLER = PopulatedPlace(
        name="Weller",
        abbreviations=PlaceAbbreviations(
            three_letter="WEL",
            five_letter="WELLE",
            seven_letter="WELLER",
            fourteen_letter="WELLER"
        ),
        latitude=39.44749453552629,
        longitude=-105.6205695194435,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    WELLINGTON = PopulatedPlace(
        name="Wellington",
        abbreviations=PlaceAbbreviations(
            three_letter="WEL",
            five_letter="WELLI",
            seven_letter="WELLING",
            fourteen_letter="WELLINGTON"
        ),
        latitude=40.70387774845142,
        longitude=-105.00859582899142,
        counties=[Counties.LARIMER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WELLINGTON_DOWNS = PopulatedPlace(
        name="Wellington Downs",
        abbreviations=PlaceAbbreviations(
            three_letter="WEL",
            five_letter="WELLI",
            seven_letter="WELLING",
            fourteen_letter="WELLINGTON DOW"
        ),
        latitude=39.807228623398316,
        longitude=-105.05778793237761,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WELLSHIRE = PopulatedPlace(
        name="Wellshire",
        abbreviations=PlaceAbbreviations(
            three_letter="WEL",
            five_letter="WELLS",
            seven_letter="WELLSHI",
            fourteen_letter="WELLSHIRE"
        ),
        latitude=39.67167311079754,
        longitude=-104.96889899541344,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    WELLSVILLE = PopulatedPlace(
        name="Wellsville",
        abbreviations=PlaceAbbreviations(
            three_letter="WEL",
            five_letter="WELLS",
            seven_letter="WELLSVI",
            fourteen_letter="WELLSVILLE"
        ),
        latitude=38.48667008304113,
        longitude=-105.91002017871602,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    WELTY = PopulatedPlace(
        name="Welty",
        abbreviations=PlaceAbbreviations(
            three_letter="WEL",
            five_letter="WELTY",
            seven_letter="WELTY",
            fourteen_letter="WELTY"
        ),
        latitude=40.327767997072044,
        longitude=-105.01776658509829,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WEST_BURLINGTON = PopulatedPlace(
        name="West Burlington",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WEST ",
            seven_letter="WEST BU",
            fourteen_letter="WEST BURLINGTO"
        ),
        latitude=39.30333663803509,
        longitude=-102.3096449268719,
        counties=[Counties.KIT_CARSON],
        nearest_airport=Airports.PUEBLO
    )
    WEST_FARM = PopulatedPlace(
        name="West Farm",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WEST ",
            seven_letter="WEST FA",
            fourteen_letter="WEST FARM"
        ),
        latitude=38.09279284048938,
        longitude=-102.55853545990038,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    WEST_MEADOWS = PopulatedPlace(
        name="West Meadows",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WEST ",
            seven_letter="WEST ME",
            fourteen_letter="WEST MEADOWS"
        ),
        latitude=39.60778419064502,
        longitude=-105.13917682784813,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WEST_VAIL = PopulatedPlace(
        name="West Vail",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WEST ",
            seven_letter="WEST VA",
            fourteen_letter="WEST VAIL"
        ),
        latitude=39.63027010450372,
        longitude=-106.41476232045238,
        counties=[Counties.EAGLE],
        nearest_airport=Airports.EAGLE
    )
    WEST_VANCORUM = PopulatedPlace(
        name="West Vancorum",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WEST ",
            seven_letter="WEST VA",
            fourteen_letter="WEST VANCORUM"
        ),
        latitude=38.22777436824475,
        longitude=-108.60065954263683,
        counties=[Counties.MONTROSE],
        nearest_airport=Airports.TELLURIDE
    )
    WESTCLIFFE = PopulatedPlace(
        name="Westcliffe",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WESTC",
            seven_letter="WESTCLI",
            fourteen_letter="WESTCLIFFE"
        ),
        latitude=38.13472816209804,
        longitude=-105.46584534062032,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    WESTCREEK = PopulatedPlace(
        name="Westcreek",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WESTC",
            seven_letter="WESTCRE",
            fourteen_letter="WESTCREEK"
        ),
        latitude=39.15249742588554,
        longitude=-105.16361158119275,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    WESTERN_HILLS = PopulatedPlace(
        name="Western Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WESTE",
            seven_letter="WESTERN",
            fourteen_letter="WESTERN HILLS"
        ),
        latitude=39.83221463107344,
        longitude=-104.9972134206551,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    WESTGATE = PopulatedPlace(
        name="Westgate",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WESTG",
            seven_letter="WESTGAT",
            fourteen_letter="WESTGATE"
        ),
        latitude=39.671117502559014,
        longitude=-105.0930657240026,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WESTHAVEN = PopulatedPlace(
        name="Westhaven",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WESTH",
            seven_letter="WESTHAV",
            fourteen_letter="WESTHAVEN"
        ),
        latitude=39.767506414990635,
        longitude=-105.1050101381436,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WESTMINSTER = PopulatedPlace(
        name="Westminster",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WESTM",
            seven_letter="WESTMIN",
            fourteen_letter="WESTMINSTER"
        ),
        latitude=39.83665922908642,
        longitude=-105.0372147301137,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    WESTMINSTER_HILLS = PopulatedPlace(
        name="Westminster Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WESTM",
            seven_letter="WESTMIN",
            fourteen_letter="WESTMINSTER HI"
        ),
        latitude=39.845006429795774,
        longitude=-105.04584343469327,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    WESTPLAINS = PopulatedPlace(
        name="Westplains",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WESTP",
            seven_letter="WESTPLA",
            fourteen_letter="WESTPLAINS"
        ),
        latitude=40.86471297894042,
        longitude=-103.49772349296592,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    WESTSIDE_NEIGHBORHOOD = PopulatedPlace(
        name="Westside Neighborhood",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WESTS",
            seven_letter="WESTSID",
            fourteen_letter="WESTSIDE NEIGH"
        ),
        latitude=39.73778421766718,
        longitude=-105.00112121071868,
        counties=[Counties.DENVER],
        nearest_airport=Airports.DENVER
    )
    WESTVIEW = PopulatedPlace(
        name="Westview",
        abbreviations=PlaceAbbreviations(
            three_letter="WES",
            five_letter="WESTV",
            seven_letter="WESTVIE",
            fourteen_letter="WESTVIEW"
        ),
        latitude=39.89083973871226,
        longitude=-105.00139902909336,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )
    WETMORE = PopulatedPlace(
        name="Wetmore",
        abbreviations=PlaceAbbreviations(
            three_letter="WET",
            five_letter="WETMO",
            seven_letter="WETMORE",
            fourteen_letter="WETMORE"
        ),
        latitude=38.23806470166812,
        longitude=-105.08472126524356,
        counties=[Counties.CUSTER],
        nearest_airport=Airports.PUEBLO
    )
    WHEAT_RIDGE = PopulatedPlace(
        name="Wheat Ridge",
        abbreviations=PlaceAbbreviations(
            three_letter="WHE",
            five_letter="WHEAT",
            seven_letter="WHEAT R",
            fourteen_letter="WHEAT RIDGE"
        ),
        latitude=39.766104416930204,
        longitude=-105.0772164321362,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WHEELER_JUNCTION = PopulatedPlace(
        name="Wheeler Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="WHE",
            five_letter="WHEEL",
            seven_letter="WHEELER",
            fourteen_letter="WHEELER JUNCTI"
        ),
        latitude=39.506104006912324,
        longitude=-106.14225454500507,
        counties=[Counties.SUMMIT],
        nearest_airport=Airports.ASPEN
    )
    WHEELMAN = PopulatedPlace(
        name="Wheelman",
        abbreviations=PlaceAbbreviations(
            three_letter="WHE",
            five_letter="WHEEL",
            seven_letter="WHEELMA",
            fourteen_letter="WHEELMAN"
        ),
        latitude=40.00360362853337,
        longitude=-105.37389262841276,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WHISPERING_PINE = PopulatedPlace(
        name="Whispering Pine",
        abbreviations=PlaceAbbreviations(
            three_letter="WHI",
            five_letter="WHISP",
            seven_letter="WHISPER",
            fourteen_letter="WHISPERING PIN"
        ),
        latitude=39.96971541577369,
        longitude=-105.48584064947539,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WHITE_RIVER_CITY = PopulatedPlace(
        name="White River City",
        abbreviations=PlaceAbbreviations(
            three_letter="WHI",
            five_letter="WHITE",
            seven_letter="WHITE R",
            fourteen_letter="WHITE RIVER CI"
        ),
        latitude=40.0908104349499,
        longitude=-108.22426357728148,
        counties=[Counties.RIO_BLANCO],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    WHITEHORN = PopulatedPlace(
        name="Whitehorn",
        abbreviations=PlaceAbbreviations(
            three_letter="WHI",
            five_letter="WHITE",
            seven_letter="WHITEHO",
            fourteen_letter="WHITEHORN"
        ),
        latitude=38.64389120673104,
        longitude=-105.8783516885452,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    WHITEPINE = PopulatedPlace(
        name="Whitepine",
        abbreviations=PlaceAbbreviations(
            three_letter="WHI",
            five_letter="WHITE",
            seven_letter="WHITEPI",
            fourteen_letter="WHITEPINE"
        ),
        latitude=38.54166875813263,
        longitude=-106.39364769458365,
        counties=[Counties.GUNNISON],
        nearest_airport=Airports.GUNNISON_CRESTED_BUTTE
    )
    WHITEROCK = PopulatedPlace(
        name="Whiterock",
        abbreviations=PlaceAbbreviations(
            three_letter="WHI",
            five_letter="WHITE",
            seven_letter="WHITERO",
            fourteen_letter="WHITEROCK"
        ),
        latitude=37.86584910977507,
        longitude=-104.11441830364822,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    WHITEWATER = PopulatedPlace(
        name="Whitewater",
        abbreviations=PlaceAbbreviations(
            three_letter="WHI",
            five_letter="WHITE",
            seven_letter="WHITEWA",
            fourteen_letter="WHITEWATER"
        ),
        latitude=38.99109947764657,
        longitude=-108.45343339577607,
        counties=[Counties.MESA],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    WIDE_ACRES = PopulatedPlace(
        name="Wide Acres",
        abbreviations=PlaceAbbreviations(
            three_letter="WID",
            five_letter="WIDE ",
            seven_letter="WIDE AC",
            fourteen_letter="WIDE ACRES"
        ),
        latitude=39.5683396922127,
        longitude=-105.03445449829985,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    WIDEFIELD = PopulatedPlace(
        name="Widefield",
        abbreviations=PlaceAbbreviations(
            three_letter="WID",
            five_letter="WIDEF",
            seven_letter="WIDEFIE",
            fourteen_letter="WIDEFIELD"
        ),
        latitude=38.733335596343295,
        longitude=-104.71998183362496,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    WIGGINS = PopulatedPlace(
        name="Wiggins",
        abbreviations=PlaceAbbreviations(
            three_letter="WIG",
            five_letter="WIGGI",
            seven_letter="WIGGINS",
            fourteen_letter="WIGGINS"
        ),
        latitude=40.230542851072016,
        longitude=-104.0727377527677,
        counties=[Counties.MORGAN],
        nearest_airport=Airports.DENVER
    )
    WIGWAM = PopulatedPlace(
        name="Wigwam",
        abbreviations=PlaceAbbreviations(
            three_letter="WIG",
            five_letter="WIGWA",
            seven_letter="WIGWAM",
            fourteen_letter="WIGWAM"
        ),
        latitude=38.539449573845275,
        longitude=-104.63553779302606,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    WILADEL = PopulatedPlace(
        name="Wiladel",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILAD",
            seven_letter="WILADEL",
            fourteen_letter="WILADEL"
        ),
        latitude=39.743048154799965,
        longitude=-103.0099478436789,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    """
    WILD_HORSE = PopulatedPlace(
        name="Wild Horse",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILD ",
            seven_letter="WILD HO",
            fourteen_letter="WILD HORSE"
        ),
        latitude=38.32917474159029,
        longitude=-104.66859647909956,
        counties=[Counties.PUEBLO],
        nearest_airport=Airports.PUEBLO
    )
    WILD_HORSE = PopulatedPlace(
        name="Wild Horse",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILD ",
            seven_letter="WILD HO",
            fourteen_letter="WILD HORSE"
        ),
        latitude=38.82583862180252,
        longitude=-103.01160664303808,
        counties=[Counties.CHEYENNE],
        nearest_airport=Airports.PUEBLO
    )
    """
    WILDCAT = PopulatedPlace(
        name="Wildcat",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILDC",
            seven_letter="WILDCAT",
            fourteen_letter="WILDCAT"
        ),
        latitude=40.25915639748678,
        longitude=-104.88470634565186,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WILDWOOD = PopulatedPlace(
        name="Wildwood",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILDW",
            seven_letter="WILDWOO",
            fourteen_letter="WILDWOOD"
        ),
        latitude=39.77056201515302,
        longitude=-105.10251013838598,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WILEY = PopulatedPlace(
        name="Wiley",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILEY",
            seven_letter="WILEY",
            fourteen_letter="WILEY"
        ),
        latitude=38.154181139978334,
        longitude=-102.7196497047841,
        counties=[Counties.PROWERS],
        nearest_airport=Airports.PUEBLO
    )
    WILL_O_THE_WISP = PopulatedPlace(
        name="Will-O-The-Wisp",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILL-",
            seven_letter="WILL-O-",
            fourteen_letter="WILL-O-THE-WIS"
        ),
        latitude=39.461384152003916,
        longitude=-105.41028477296112,
        counties=[Counties.PARK],
        nearest_airport=Airports.DENVER
    )
    WILLARD = PopulatedPlace(
        name="Willard",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILLA",
            seven_letter="WILLARD",
            fourteen_letter="WILLARD"
        ),
        latitude=40.55443263660635,
        longitude=-103.4863395521038,
        counties=[Counties.LOGAN],
        nearest_airport=Airports.DENVER
    )
    WILLEY_LUMBER_CAMP = PopulatedPlace(
        name="Willey Lumber Camp",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILLE",
            seven_letter="WILLEY ",
            fourteen_letter="WILLEY LUMBER "
        ),
        latitude=40.502766957690255,
        longitude=-105.8991903088396,
        counties=[Counties.JACKSON],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WILLIAMSBURG = PopulatedPlace(
        name="Williamsburg",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILLI",
            seven_letter="WILLIAM",
            fourteen_letter="WILLIAMSBURG"
        ),
        latitude=38.38195031786478,
        longitude=-105.15194309537117,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    WILLOW_BROOK = PopulatedPlace(
        name="Willow Brook",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILLO",
            seven_letter="WILLOW ",
            fourteen_letter="WILLOW BROOK"
        ),
        latitude=39.607784188568644,
        longitude=-105.17056573535291,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WILLOW_CREEK = PopulatedPlace(
        name="Willow Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILLO",
            seven_letter="WILLOW ",
            fourteen_letter="WILLOW CREEK"
        ),
        latitude=39.573062002791346,
        longitude=-104.89473226736646,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    WILLOW_PARK = PopulatedPlace(
        name="Willow Park",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILLO",
            seven_letter="WILLOW ",
            fourteen_letter="WILLOW PARK"
        ),
        latitude=39.68611752378928,
        longitude=-104.81445446213831,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    WILLOW_SPRINGS = PopulatedPlace(
        name="Willow Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILLO",
            seven_letter="WILLOW ",
            fourteen_letter="WILLOW SPRINGS"
        ),
        latitude=39.61167308788089,
        longitude=-105.18112123818207,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WILSON_PLACE = PopulatedPlace(
        name="Wilson Place",
        abbreviations=PlaceAbbreviations(
            three_letter="WIL",
            five_letter="WILSO",
            seven_letter="WILSON ",
            fourteen_letter="WILSON PLACE"
        ),
        latitude=40.7619129679631,
        longitude=-108.89373850812171,
        counties=[Counties.MOFFAT],
        nearest_airport=Airports.GRAND_JUNCTION
    )
    WINDSOR = PopulatedPlace(
        name="Windsor",
        abbreviations=PlaceAbbreviations(
            three_letter="WIN",
            five_letter="WINDS",
            seven_letter="WINDSOR",
            fourteen_letter="WINDSOR"
        ),
        latitude=40.4774883261677,
        longitude=-104.90137187642983,
        counties=[Counties.WELD],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WINDY_HILLS = PopulatedPlace(
        name="Windy Hills",
        abbreviations=PlaceAbbreviations(
            three_letter="WIN",
            five_letter="WINDY",
            seven_letter="WINDY H",
            fourteen_letter="WINDY HILLS"
        ),
        latitude=39.48560640489853,
        longitude=-104.68761000929919,
        counties=[Counties.DOUGLAS],
        nearest_airport=Airports.DENVER
    )
    WINFIELD = PopulatedPlace(
        name="Winfield",
        abbreviations=PlaceAbbreviations(
            three_letter="WIN",
            five_letter="WINFI",
            seven_letter="WINFIEL",
            fourteen_letter="WINFIELD"
        ),
        latitude=38.98472161604758,
        longitude=-106.4408702524891,
        counties=[Counties.CHAFFEE],
        nearest_airport=Airports.ASPEN
    )
    WINGO = PopulatedPlace(
        name="Wingo",
        abbreviations=PlaceAbbreviations(
            three_letter="WIN",
            five_letter="WINGO",
            seven_letter="WINGO",
            fourteen_letter="WINGO"
        ),
        latitude=39.34582392516256,
        longitude=-107.01033402067804,
        counties=[Counties.PITKIN],
        nearest_airport=Airports.ASPEN
    )
    WINTER_PARK = PopulatedPlace(
        name="Winter Park",
        abbreviations=PlaceAbbreviations(
            three_letter="WIN",
            five_letter="WINTE",
            seven_letter="WINTER ",
            fourteen_letter="WINTER PARK"
        ),
        latitude=39.8916600853978,
        longitude=-105.7630727036294,
        counties=[Counties.GRAND],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WOLHURST = PopulatedPlace(
        name="Wolhurst",
        abbreviations=PlaceAbbreviations(
            three_letter="WOL",
            five_letter="WOLHU",
            seven_letter="WOLHURS",
            fourteen_letter="WOLHURST"
        ),
        latitude=39.57054999260731,
        longitude=-105.03332749799546,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    WONDERVU = PopulatedPlace(
        name="Wondervu",
        abbreviations=PlaceAbbreviations(
            three_letter="WON",
            five_letter="WONDE",
            seven_letter="WONDERV",
            fourteen_letter="WONDERVU"
        ),
        latitude=39.92554871510964,
        longitude=-105.39500422336579,
        counties=[Counties.BOULDER],
        nearest_airport=Airports.NORTHERN_COLORADO
    )
    WOOD_CREEK = PopulatedPlace(
        name="Wood Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="WOO",
            five_letter="WOOD ",
            seven_letter="WOOD CR",
            fourteen_letter="WOOD CREEK"
        ),
        latitude=39.83417312746036,
        longitude=-105.05778793507255,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WOOD_RUN = PopulatedPlace(
        name="Wood Run",
        abbreviations=PlaceAbbreviations(
            three_letter="WOO",
            five_letter="WOOD ",
            seven_letter="WOOD RU",
            fourteen_letter="WOOD RUN"
        ),
        latitude=39.84667312569138,
        longitude=-105.10417684741117,
        counties=[Counties.JEFFERSON],
        nearest_airport=Airports.DENVER
    )
    WOODGATE = PopulatedPlace(
        name="Woodgate",
        abbreviations=PlaceAbbreviations(
            three_letter="WOO",
            five_letter="WOODG",
            seven_letter="WOODGAT",
            fourteen_letter="WOODGATE"
        ),
        latitude=39.62722861577299,
        longitude=-104.81417675515479,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    WOODLAND_PARK = PopulatedPlace(
        name="Woodland Park",
        abbreviations=PlaceAbbreviations(
            three_letter="WOO",
            five_letter="WOODL",
            seven_letter="WOODLAN",
            fourteen_letter="WOODLAND PARK"
        ),
        latitude=38.993887110981234,
        longitude=-105.05694013924335,
        counties=[Counties.TELLER],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    WOODMOOR = PopulatedPlace(
        name="Woodmoor",
        abbreviations=PlaceAbbreviations(
            three_letter="WOO",
            five_letter="WOODM",
            seven_letter="WOODMOO",
            fourteen_letter="WOODMOOR"
        ),
        latitude=39.101387139975145,
        longitude=-104.84748940304388,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    WOODRIM = PopulatedPlace(
        name="Woodrim",
        abbreviations=PlaceAbbreviations(
            three_letter="WOO",
            five_letter="WOODR",
            seven_letter="WOODRIM",
            fourteen_letter="WOODRIM"
        ),
        latitude=39.67833972233251,
        longitude=-104.8166767612006,
        counties=[Counties.ARAPAHOE],
        nearest_airport=Airports.DENVER
    )
    WOODROW = PopulatedPlace(
        name="Woodrow",
        abbreviations=PlaceAbbreviations(
            three_letter="WOO",
            five_letter="WOODR",
            seven_letter="WOODROW",
            fourteen_letter="WOODROW"
        ),
        latitude=39.98832465012737,
        longitude=-103.59162181055171,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    WRAY = PopulatedPlace(
        name="Wray",
        abbreviations=PlaceAbbreviations(
            three_letter="WRA",
            five_letter="WRAY",
            seven_letter="WRAY",
            fourteen_letter="WRAY"
        ),
        latitude=40.075829756553446,
        longitude=-102.22325899183505,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    XENIA = PopulatedPlace(
        name="Xenia",
        abbreviations=PlaceAbbreviations(
            three_letter="XEN",
            five_letter="XENIA",
            seven_letter="XENIA",
            fourteen_letter="XENIA"
        ),
        latitude=40.16109899183073,
        longitude=-103.3449513721198,
        counties=[Counties.WASHINGTON],
        nearest_airport=Airports.DENVER
    )
    YAMPA = PopulatedPlace(
        name="Yampa",
        abbreviations=PlaceAbbreviations(
            three_letter="YAM",
            five_letter="YAMPA",
            seven_letter="YAMPA",
            fourteen_letter="YAMPA"
        ),
        latitude=40.152490038823714,
        longitude=-106.90866879458554,
        counties=[Counties.ROUTT],
        nearest_airport=Airports.YAMPA_VALLEY
    )
    YELLOW_JACKET = PopulatedPlace(
        name="Yellow Jacket",
        abbreviations=PlaceAbbreviations(
            three_letter="YEL",
            five_letter="YELLO",
            seven_letter="YELLOW ",
            fourteen_letter="YELLOW JACKET"
        ),
        latitude=37.53444086815631,
        longitude=-108.71733189450845,
        counties=[Counties.MONTEZUMA],
        nearest_airport=Airports.CORTEZ
    )
    YODER = PopulatedPlace(
        name="Yoder",
        abbreviations=PlaceAbbreviations(
            three_letter="YOD",
            five_letter="YODER",
            seven_letter="YODER",
            fourteen_letter="YODER"
        ),
        latitude=38.839444144542426,
        longitude=-104.22191482932152,
        counties=[Counties.EL_PASO],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    YORKVILLE = PopulatedPlace(
        name="Yorkville",
        abbreviations=PlaceAbbreviations(
            three_letter="YOR",
            five_letter="YORKV",
            seven_letter="YORKVIL",
            fourteen_letter="YORKVILLE"
        ),
        latitude=38.29222839637009,
        longitude=-105.29028161713637,
        counties=[Counties.FREMONT],
        nearest_airport=Airports.COLORADO_SPRINGS
    )
    YUMA = PopulatedPlace(
        name="Yuma",
        abbreviations=PlaceAbbreviations(
            three_letter="YUM",
            five_letter="YUMA",
            seven_letter="YUMA",
            fourteen_letter="YUMA"
        ),
        latitude=40.12221502884205,
        longitude=-102.72521921912147,
        counties=[Counties.YUMA],
        nearest_airport=Airports.DENVER
    )
    ZAMARA = PopulatedPlace(
        name="Zamara",
        abbreviations=PlaceAbbreviations(
            three_letter="ZAM",
            five_letter="ZAMAR",
            seven_letter="ZAMARA",
            fourteen_letter="ZAMARA"
        ),
        latitude=37.153914554082235,
        longitude=-104.92056301883247,
        counties=[Counties.LAS_ANIMAS],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    ZINZER = PopulatedPlace(
        name="Zinzer",
        abbreviations=PlaceAbbreviations(
            three_letter="ZIN",
            five_letter="ZINZE",
            seven_letter="ZINZER",
            fourteen_letter="ZINZER"
        ),
        latitude=37.56028663984097,
        longitude=-106.0944818246835,
        counties=[Counties.RIO_GRANDE],
        nearest_airport=Airports.SAN_LUIS_VALLEY
    )
    ZUNI = PopulatedPlace(
        name="Zuni",
        abbreviations=PlaceAbbreviations(
            three_letter="ZUN",
            five_letter="ZUNI",
            seven_letter="ZUNI",
            fourteen_letter="ZUNI"
        ),
        latitude=39.80332602546406,
        longitude=-105.02165882352762,
        counties=[Counties.ADAMS],
        nearest_airport=Airports.DENVER
    )

    @property
    def latitude(self) -> str:
        """
        Get the IATA code for this airport.
        :return: The IATA code for this airport.
        :rtype: str
        """
        return self._location.latitude


    @property
    def longitude(self) -> str:
        """
        Get the IATA code for this airport.
        :return: The IATA code for this airport.
        :rtype: str
        """
        return self._location.longitude

    @property
    def counties(self) -> str:
        """
        Get the IATA code for this airport.
        :return: The IATA code for this airport.
        :rtype: str
        """
        return self._location.counties


    @property
    def nearest_airport(self) -> str:
        """
        Get the IATA code for this airport.
        :return: The IATA code for this airport.
        :rtype: str
        """
        return self._location.nearest_airport

