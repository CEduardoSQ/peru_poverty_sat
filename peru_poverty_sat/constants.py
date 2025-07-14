ENAHO_COLS = [
    # Key
    "AÑO", "CONGLOME", "VIVIENDA", "HOGAR", "RESULT",
    # Amenities
    # Facade
    "P24A", "P24B",
    # Throughface
    "P25$1", "P25$2", "P25$3", "P25$4",
    # House
    "P101", "P102", "P103", "P103A", "P104", "P104A",
    # Services
    # Sanitation
    "T110", "P110A1", "P110A_MODIFICADA", "P110C", "P110C1", "P110C2", "P110C3", "T111A",
    # Illumination
    "P1121", "P1123", "P1124", "P1125", "P1126",
    # Combustion
    "P1131", "P1132", "P1133", "P1135", "P1136", "P1139", "P1137",
    # Assets
    "P1141", "P1142", "P1143", "P1144",
    # Sampling weight
    "FACTOR07",
    # Georeference
    "LONGITUD", "LATITUD",
]


class HouseholdsCols:
    KEY_COLS = [
        "year", "cluster", "house", "household"
    ]
    FACADE_COLS = [
        "plastered", "painted"
    ]
    THROUGHFACE_COLS = [
        "paved_road", "dirt_road", "sidewalk", "light_pole"
    ]
    HOUSE_COLS = [
        "structure", "wall", "floor", "roof", "rooms", "bedrooms"
    ]
    SANITATION_COLS = [
        "water_source", "potable", "water_treatment", "water_access", "toilet"
    ]
    ILLUMINATION_COLS = [
        "transmitted_electricity", "wax", "kerosene", "generated_electricity",
        "other_source",
    ]
    COMBUSTION_COLS = [
        "electricity",
        "petroleum",
        "methane",
        "coal",
        "wood",
        "dung",
        "other_fuel"]
    ASSETS_COLS = [
        "landline", "phone", "televisor", "internet"
    ]
    GEOREFERENCE_COLS = [
        "longitude", "latitude"
    ]
    FEATURES_COLS = (
        FACADE_COLS +
        THROUGHFACE_COLS +
        HOUSE_COLS +
        SANITATION_COLS +
        ILLUMINATION_COLS +
        COMBUSTION_COLS +
        ASSETS_COLS +
        GEOREFERENCE_COLS)
