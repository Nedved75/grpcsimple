"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/relay/onboarding/v1/paymentmethods/klarna.proto\x12)relay.onboarding.v1.paymentmethods.klarna\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x9a\x02\n\x15InitializeRequestData\x12T\n\x10business_details\x18\x01 \x01(\x0b2:.relay.onboarding.v1.paymentmethods.klarna.BusinessDetails\x12N\n\rstore_details\x18\x02 \x01(\x0b27.relay.onboarding.v1.paymentmethods.klarna.StoreDetails\x12[\n\x14stakeholders_details\x18\x03 \x03(\x0b2=.relay.onboarding.v1.paymentmethods.klarna.StakeholderDetails"\x96\x02\n\x11UpdateRequestData\x12T\n\x10business_details\x18\x01 \x01(\x0b2:.relay.onboarding.v1.paymentmethods.klarna.BusinessDetails\x12N\n\rstore_details\x18\x02 \x01(\x0b27.relay.onboarding.v1.paymentmethods.klarna.StoreDetails\x12[\n\x14stakeholders_details\x18\x03 \x03(\x0b2=.relay.onboarding.v1.paymentmethods.klarna.StakeholderDetails"\xa1\x02\n\x0fBusinessDetails\x12*\n\x04name\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12N\n\x12registered_address\x18\x02 \x01(\x0b22.relay.onboarding.v1.paymentmethods.klarna.Address\x12\x15\n\ris_registered\x18\x03 \x01(\x08\x125\n\x0fregistration_id\x18\x04 \x01(\x0b2\x1c.google.protobuf.StringValue\x12\x16\n\x0esubject_to_vat\x18\x05 \x01(\x08\x12,\n\x06vat_id\x18\x06 \x01(\x0b2\x1c.google.protobuf.StringValue"\x98\x03\n\x12StakeholderDetails\x121\n\x0bresource_id\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x120\n\ngiven_name\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x121\n\x0bfamily_name\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValue\x121\n\rdate_of_birth\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12C\n\x07address\x18\x05 \x01(\x0b22.relay.onboarding.v1.paymentmethods.klarna.Address\x121\n\x0bpersonal_id\x18\x06 \x01(\x0b2\x1c.google.protobuf.StringValue\x12?\n\x05roles\x18\x07 \x03(\x0e20.relay.onboarding.v1.paymentmethods.klarna.Roles"\xa7\x02\n\x07Address\x12,\n\x06street\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12-\n\x07street2\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x121\n\x0bpostal_code\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValue\x12*\n\x04city\x18\x04 \x01(\x0b2\x1c.google.protobuf.StringValue\x122\n\x0ccountry_code\x18\x05 \x01(\x0b2\x1c.google.protobuf.StringValue\x12,\n\x06region\x18\x06 \x01(\x0b2\x1c.google.protobuf.StringValue"\xe2\x05\n\x0cStoreDetails\x12*\n\x04name\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12)\n\x03url\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x12E\n\x08category\x18\x03 \x01(\x0e23.relay.onboarding.v1.paymentmethods.klarna.Category\x122\n\x0ccountry_code\x18\x04 \x01(\x0b2\x1c.google.protobuf.StringValue\x12.\n\x08logo_url\x18\x05 \x01(\x0b2\x1c.google.protobuf.StringValue\x12.\n\x08icon_url\x18\x06 \x01(\x0b2\x1c.google.protobuf.StringValue\x127\n\x11feature_image_url\x18\x07 \x01(\x0b2\x1c.google.protobuf.StringValue\x122\n\x0cfacebook_url\x18\x08 \x01(\x0b2\x1c.google.protobuf.StringValue\x123\n\rinstagram_url\x18\t \x01(\x0b2\x1c.google.protobuf.StringValue\x129\n\x13admin_email_address\x18\n \x01(\x0b2\x1c.google.protobuf.StringValue\x128\n\x12risk_email_address\x18\x0b \x01(\x0b2\x1c.google.protobuf.StringValue\x12D\n\x1ecustomer_support_email_address\x18\x0c \x01(\x0b2\x1c.google.protobuf.StringValue\x12C\n\x1dcustomer_support_phone_number\x18\r \x01(\x0b2\x1c.google.protobuf.StringValue*\x8c\r\n\x08Category\x12\x1c\n\x18ADULT_SHOES_AND_CLOTHING\x10\x00\x12$\n AUTOMOTIVE_PARTS_AND_ACCESSORIES\x10\x01\x12\x14\n\x10BAGS_AND_WALLETS\x10\x02\x12\x16\n\x12BODY_AND_HAIR_CARE\x10\x03\x12\x16\n\x12BOOK_AND_MAGAZINES\x10\x04\x12\t\n\x05CANDY\x10\x05\x12\x13\n\x0fCAR_ELECTRONICS\x10\x06\x12+\n\'CHILDREN_CLOTHES_AND_NURTURING_PRODUCTS\x10\x07\x12\x11\n\rCHILDREN_TOYS\x10\x08\x12\x19\n\x15CLEANING_AND_SANITARY\x10\t\x12\x10\n\x0cCOLLECTIBLES\x10\n\x12$\n CONCEPT_STORES_AND_MISCELLANEOUS\x10\x0b\x12\r\n\tCOSMETICS\x10\x0c\x12\x1f\n\x1bCOSTUMES_AND_PARTY_SUPPLIES\x10\r\x12\x13\n\x0fDATING_SERVICES\x10\x0e\x12\x16\n\x12DECORATION_AND_ART\x10\x0f\x12\x17\n\x13DIETARY_SUPPLEMENTS\x10\x10\x12\x14\n\x10DIGITAL_SERVICES\x10\x11\x12!\n\x1dDIVERSIFIED_CHILDREN_PRODUCTS\x10\x12\x12\x1b\n\x17DIVERSIFIED_ELECTRONICS\x10\x13\x12\x1d\n\x19DIVERSIFIED_ENTERTAINMENT\x10\x14\x12\x1f\n\x1bDIVERSIFIED_EROTIC_MATERIAL\x10\x15\x12(\n$DIVERSIFIED_HOME_AND_GARDEN_PRODUCTS\x10\x16\x12\'\n#DIVERSIFIED_JEWELRY_AND_ACCESSORIES\x10\x17\x12*\n&DIVERSIFIED_HEALTH_AND_BEAUTY_PRODUCTS\x10\x18\x12*\n&DIVERSIFIES_HEALTH_AND_BEAUTY_PRODUCTS\x10\x19\x12\r\n\tEDUCATION\x10\x1a\x120\n,ELECTRONIC_EQUIPMENT_AND_RELATED_ACCESSORIES\x10\x1b\x12#\n\x1fEROTIC_CLOTHING_AND_ACCESSORIES\x10\x1c\x12\x11\n\rEVENT_TICKETS\x10\x1d\x12\x15\n\x11FOOD_AND_BEVERAGE\x10\x1e\x12\x0e\n\nFRAGRANCES\x10\x1f\x12\r\n\tFURNITURE\x10 \x12\x1e\n\x1aGENERAL_SHOES_AND_CLOTHING\x10!\x12\x12\n\x0eHOBBY_ARTICLES\x10"\x12\x19\n\x15HOUSEHOLD_ELECTRONICS\x10#\x12\x17\n\x13JEWELRY_AND_WATCHES\x10$\x12\x0f\n\x0bKITCHENWARE\x10%\x12\x10\n\x0cMARKETPLACES\x10&\x12\x14\n\x10MUSIC_AND_MOVIES\x10\'\x12%\n!MUSICAL_INSTRUMENTS_AND_EQUIPMENT\x10(\x12*\n&NON_PRESCRIPTION_SUNGLASSES_AND_LENSES\x10)\x12+\n\'OFFICE_MACHINES_AND_RELATED_ACCESSORIES\x10*\x12\x12\n\x0eOTHER_SERVICES\x10+\x12&\n"PERSONAL_CARE_AND_BODY_IMPROVEMENT\x10,\x12\x10\n\x0cPET_SUPPLIES\x10-\x12\x1b\n\x17PHARMACEUTICAL_PRODUCTS\x10.\x12\x16\n\x12PLANTS_AND_FLOWERS\x10/\x12\x17\n\x13PRESCRIPTION_OPTICS\x100\x12\x15\n\x11PRINTS_AND_PHOTOS\x101\x12\x13\n\x0fSAFETY_PRODUCTS\x102\x12\x0c\n\x08SEX_TOYS\x103\x12\x1b\n\x17SPORTS_GEAR_AND_OUTDOOR\x104\x12\x0b\n\x07TOBACCO\x105\x12\x1e\n\x1aTOOLS_AND_HOME_IMPROVEMENT\x106\x12\x13\n\x0fTRAVEL_SERVICES\x107\x12\r\n\tUNDERWEAR\x108\x12\'\n#VIDEO_GAMES_AND_RELATED_ACCESSORIES\x109\x12\x14\n\x10WHEELS_AND_TIRES\x10:\x12\x18\n\x14WINE_BEER_AND_LIQUOR\x10;\x12\x1f\n\x1bYOUTHFUL_SHOES_AND_CLOTHING\x10<*\xdf\x01\n\x05Roles\x12\r\n\tAPPLICANT\x10\x00\x12\x1b\n\x17CONTROL_OVER_MANAGEMENT\x10\x01\x12\t\n\x05OWNER\x10\x02\x12\x0b\n\x07PARTNER\x10\x03\x12\x0f\n\x0bSOLE_TRADER\x10\x04\x12\x1d\n\x19ULTIMATE_BENEFICIAL_OWNER\x10\x05\x12\x15\n\x11MANAGING_DIRECTOR\x10\x06\x12\x1e\n\x1aPOLITICALLY_EXPOSED_PERSON\x10\x07\x12\x17\n\x13MATERIAL_INFLUENCER\x10\x08\x12\x12\n\x0eNOT_APPLICABLE\x10\tBvZHgithub.com/Nedved75/grpcsimple/sdk/go/relay/onboarding/v1/paymentmethods\xaa\x02)Relay.Onboarding.V1.PaymentMethods.Klarnab\x06proto3')
_CATEGORY = DESCRIPTOR.enum_types_by_name['Category']
Category = enum_type_wrapper.EnumTypeWrapper(_CATEGORY)
_ROLES = DESCRIPTOR.enum_types_by_name['Roles']
Roles = enum_type_wrapper.EnumTypeWrapper(_ROLES)
ADULT_SHOES_AND_CLOTHING = 0
AUTOMOTIVE_PARTS_AND_ACCESSORIES = 1
BAGS_AND_WALLETS = 2
BODY_AND_HAIR_CARE = 3
BOOK_AND_MAGAZINES = 4
CANDY = 5
CAR_ELECTRONICS = 6
CHILDREN_CLOTHES_AND_NURTURING_PRODUCTS = 7
CHILDREN_TOYS = 8
CLEANING_AND_SANITARY = 9
COLLECTIBLES = 10
CONCEPT_STORES_AND_MISCELLANEOUS = 11
COSMETICS = 12
COSTUMES_AND_PARTY_SUPPLIES = 13
DATING_SERVICES = 14
DECORATION_AND_ART = 15
DIETARY_SUPPLEMENTS = 16
DIGITAL_SERVICES = 17
DIVERSIFIED_CHILDREN_PRODUCTS = 18
DIVERSIFIED_ELECTRONICS = 19
DIVERSIFIED_ENTERTAINMENT = 20
DIVERSIFIED_EROTIC_MATERIAL = 21
DIVERSIFIED_HOME_AND_GARDEN_PRODUCTS = 22
DIVERSIFIED_JEWELRY_AND_ACCESSORIES = 23
DIVERSIFIED_HEALTH_AND_BEAUTY_PRODUCTS = 24
DIVERSIFIES_HEALTH_AND_BEAUTY_PRODUCTS = 25
EDUCATION = 26
ELECTRONIC_EQUIPMENT_AND_RELATED_ACCESSORIES = 27
EROTIC_CLOTHING_AND_ACCESSORIES = 28
EVENT_TICKETS = 29
FOOD_AND_BEVERAGE = 30
FRAGRANCES = 31
FURNITURE = 32
GENERAL_SHOES_AND_CLOTHING = 33
HOBBY_ARTICLES = 34
HOUSEHOLD_ELECTRONICS = 35
JEWELRY_AND_WATCHES = 36
KITCHENWARE = 37
MARKETPLACES = 38
MUSIC_AND_MOVIES = 39
MUSICAL_INSTRUMENTS_AND_EQUIPMENT = 40
NON_PRESCRIPTION_SUNGLASSES_AND_LENSES = 41
OFFICE_MACHINES_AND_RELATED_ACCESSORIES = 42
OTHER_SERVICES = 43
PERSONAL_CARE_AND_BODY_IMPROVEMENT = 44
PET_SUPPLIES = 45
PHARMACEUTICAL_PRODUCTS = 46
PLANTS_AND_FLOWERS = 47
PRESCRIPTION_OPTICS = 48
PRINTS_AND_PHOTOS = 49
SAFETY_PRODUCTS = 50
SEX_TOYS = 51
SPORTS_GEAR_AND_OUTDOOR = 52
TOBACCO = 53
TOOLS_AND_HOME_IMPROVEMENT = 54
TRAVEL_SERVICES = 55
UNDERWEAR = 56
VIDEO_GAMES_AND_RELATED_ACCESSORIES = 57
WHEELS_AND_TIRES = 58
WINE_BEER_AND_LIQUOR = 59
YOUTHFUL_SHOES_AND_CLOTHING = 60
APPLICANT = 0
CONTROL_OVER_MANAGEMENT = 1
OWNER = 2
PARTNER = 3
SOLE_TRADER = 4
ULTIMATE_BENEFICIAL_OWNER = 5
MANAGING_DIRECTOR = 6
POLITICALLY_EXPOSED_PERSON = 7
MATERIAL_INFLUENCER = 8
NOT_APPLICABLE = 9
_INITIALIZEREQUESTDATA = DESCRIPTOR.message_types_by_name['InitializeRequestData']
_UPDATEREQUESTDATA = DESCRIPTOR.message_types_by_name['UpdateRequestData']
_BUSINESSDETAILS = DESCRIPTOR.message_types_by_name['BusinessDetails']
_STAKEHOLDERDETAILS = DESCRIPTOR.message_types_by_name['StakeholderDetails']
_ADDRESS = DESCRIPTOR.message_types_by_name['Address']
_STOREDETAILS = DESCRIPTOR.message_types_by_name['StoreDetails']
InitializeRequestData = _reflection.GeneratedProtocolMessageType('InitializeRequestData', (_message.Message,), {'DESCRIPTOR': _INITIALIZEREQUESTDATA, '__module__': 'relay.onboarding.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(InitializeRequestData)
UpdateRequestData = _reflection.GeneratedProtocolMessageType('UpdateRequestData', (_message.Message,), {'DESCRIPTOR': _UPDATEREQUESTDATA, '__module__': 'relay.onboarding.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(UpdateRequestData)
BusinessDetails = _reflection.GeneratedProtocolMessageType('BusinessDetails', (_message.Message,), {'DESCRIPTOR': _BUSINESSDETAILS, '__module__': 'relay.onboarding.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(BusinessDetails)
StakeholderDetails = _reflection.GeneratedProtocolMessageType('StakeholderDetails', (_message.Message,), {'DESCRIPTOR': _STAKEHOLDERDETAILS, '__module__': 'relay.onboarding.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(StakeholderDetails)
Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {'DESCRIPTOR': _ADDRESS, '__module__': 'relay.onboarding.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(Address)
StoreDetails = _reflection.GeneratedProtocolMessageType('StoreDetails', (_message.Message,), {'DESCRIPTOR': _STOREDETAILS, '__module__': 'relay.onboarding.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(StoreDetails)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZHgithub.com/Nedved75/grpcsimple/sdk/go/relay/onboarding/v1/paymentmethods\xaa\x02)Relay.Onboarding.V1.PaymentMethods.Klarna'
    _CATEGORY._serialized_start = 2468
    _CATEGORY._serialized_end = 4144
    _ROLES._serialized_start = 4147
    _ROLES._serialized_end = 4370
    _INITIALIZEREQUESTDATA._serialized_start = 160
    _INITIALIZEREQUESTDATA._serialized_end = 442
    _UPDATEREQUESTDATA._serialized_start = 445
    _UPDATEREQUESTDATA._serialized_end = 723
    _BUSINESSDETAILS._serialized_start = 726
    _BUSINESSDETAILS._serialized_end = 1015
    _STAKEHOLDERDETAILS._serialized_start = 1018
    _STAKEHOLDERDETAILS._serialized_end = 1426
    _ADDRESS._serialized_start = 1429
    _ADDRESS._serialized_end = 1724
    _STOREDETAILS._serialized_start = 1727
    _STOREDETAILS._serialized_end = 2465