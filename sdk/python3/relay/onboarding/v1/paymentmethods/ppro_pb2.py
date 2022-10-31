"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-relay/onboarding/v1/paymentmethods/ppro.proto\x12\'relay.onboarding.v1.paymentmethods.ppro\x1a\x1fgoogle/protobuf/timestamp.proto"\x9e\x02\n\x15InitializeRequestData\x12R\n\x10business_details\x18\x01 \x01(\x0b28.relay.onboarding.v1.paymentmethods.ppro.BusinessDetails\x12e\n\x1apayment_method_information\x18\x02 \x01(\x0b2A.relay.onboarding.v1.paymentmethods.ppro.PaymentMethodInformation\x12J\n\x0clegal_entity\x18\x03 \x01(\x0b24.relay.onboarding.v1.paymentmethods.ppro.LegalEntity"\xb3\x01\n\x11UpdateRequestData\x12R\n\x10business_details\x18\x01 \x01(\x0b28.relay.onboarding.v1.paymentmethods.ppro.BusinessDetails\x12J\n\x0clegal_entity\x18\x03 \x01(\x0b24.relay.onboarding.v1.paymentmethods.ppro.LegalEntity"\xb4\x02\n\x0fBusinessDetails\x12\x1e\n\x16merchant_category_code\x18\x01 \x01(\t\x12\x1a\n\x12payment_descriptor\x18\x02 \x01(\t\x12\x12\n\ntrade_name\x18\x03 \x01(\t\x12\x10\n\x08websites\x18\x04 \x03(\t\x12Z\n\x14monthly_transactions\x18\x05 \x01(\x0b2<.relay.onboarding.v1.paymentmethods.ppro.MonthlyTransactions\x12\x14\n\x0cphone_number\x18\x06 \x01(\t\x12\x15\n\remail_address\x18\x07 \x01(\t\x126\n\x12incorporation_date\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp"M\n\x13MonthlyTransactions\x12\r\n\x05count\x18\x01 \x01(\t\x12\x15\n\raverage_value\x18\x02 \x01(\t\x12\x10\n\x08currency\x18\x03 \x01(\t"\x96\x01\n\x18PaymentMethodInformation\x12N\n\x12creditor_residence\x18\x01 \x01(\x0b22.relay.onboarding.v1.paymentmethods.ppro.Residence\x12\x13\n\x0bcreditor_id\x18\x02 \x01(\t\x12\x15\n\rcreditor_name\x18\x03 \x01(\t"\xcf\x02\n\x0bLegalEntity\x12I\n\x0bpartnership\x18\x01 \x01(\x0b24.relay.onboarding.v1.paymentmethods.ppro.Partnership\x12G\n\nindividual\x18\x02 \x01(\x0b23.relay.onboarding.v1.paymentmethods.ppro.Individual\x12K\n\x0corganization\x18\x03 \x01(\x0b25.relay.onboarding.v1.paymentmethods.ppro.Organization\x12_\n\x17non_profit_organization\x18\x04 \x01(\x0b2>.relay.onboarding.v1.paymentmethods.ppro.NonprofitOrganization"\xc2\x01\n\x0bPartnership\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x13registration_number\x18\x02 \x01(\t\x12E\n\tresidence\x18\x03 \x01(\x0b22.relay.onboarding.v1.paymentmethods.ppro.Residence\x12A\n\x08partners\x18\x04 \x03(\x0b2/.relay.onboarding.v1.paymentmethods.ppro.Person"Q\n\x04Name\x12\r\n\x05title\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x13\n\x0bmiddle_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t"\xa2\x01\n\nIndividual\x12\x0c\n\x04name\x18\x01 \x01(\t\x12E\n\tresidence\x18\x02 \x01(\x0b22.relay.onboarding.v1.paymentmethods.ppro.Residence\x12?\n\x06person\x18\x03 \x01(\x0b2/.relay.onboarding.v1.paymentmethods.ppro.Person"\x99\x02\n\x0cOrganization\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x13registration_number\x18\x02 \x01(\t\x12E\n\tresidence\x18\x03 \x01(\x0b22.relay.onboarding.v1.paymentmethods.ppro.Residence\x12B\n\tdirectors\x18\x04 \x03(\x0b2/.relay.onboarding.v1.paymentmethods.ppro.Person\x12S\n\x1aultimate_beneficial_owners\x18\x05 \x03(\x0b2/.relay.onboarding.v1.paymentmethods.ppro.Person"\xa2\x02\n\x15NonprofitOrganization\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x13registration_number\x18\x02 \x01(\t\x12E\n\tresidence\x18\x03 \x01(\x0b22.relay.onboarding.v1.paymentmethods.ppro.Residence\x12B\n\tdirectors\x18\x04 \x03(\x0b2/.relay.onboarding.v1.paymentmethods.ppro.Person\x12S\n\x1aultimate_beneficial_owners\x18\x05 \x03(\x0b2/.relay.onboarding.v1.paymentmethods.ppro.Person"\xbf\x01\n\x06Person\x12;\n\x04name\x18\x01 \x01(\x0b2-.relay.onboarding.v1.paymentmethods.ppro.Name\x121\n\rdate_of_birth\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12E\n\tresidence\x18\x03 \x01(\x0b22.relay.onboarding.v1.paymentmethods.ppro.Residence"\\\n\tResidence\x12\x0f\n\x07address\x18\x01 \x03(\t\x12\x10\n\x08zip_code\x18\x02 \x01(\t\x12\x0c\n\x04city\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\x0f\n\x07country\x18\x05 \x01(\tBtZHgithub.com/Nedved75/grpcsimple/sdk/go/relay/onboarding/v1/paymentmethods\xaa\x02\'Relay.Onboarding.V1.PaymentMethods.Pprob\x06proto3')
_INITIALIZEREQUESTDATA = DESCRIPTOR.message_types_by_name['InitializeRequestData']
_UPDATEREQUESTDATA = DESCRIPTOR.message_types_by_name['UpdateRequestData']
_BUSINESSDETAILS = DESCRIPTOR.message_types_by_name['BusinessDetails']
_MONTHLYTRANSACTIONS = DESCRIPTOR.message_types_by_name['MonthlyTransactions']
_PAYMENTMETHODINFORMATION = DESCRIPTOR.message_types_by_name['PaymentMethodInformation']
_LEGALENTITY = DESCRIPTOR.message_types_by_name['LegalEntity']
_PARTNERSHIP = DESCRIPTOR.message_types_by_name['Partnership']
_NAME = DESCRIPTOR.message_types_by_name['Name']
_INDIVIDUAL = DESCRIPTOR.message_types_by_name['Individual']
_ORGANIZATION = DESCRIPTOR.message_types_by_name['Organization']
_NONPROFITORGANIZATION = DESCRIPTOR.message_types_by_name['NonprofitOrganization']
_PERSON = DESCRIPTOR.message_types_by_name['Person']
_RESIDENCE = DESCRIPTOR.message_types_by_name['Residence']
InitializeRequestData = _reflection.GeneratedProtocolMessageType('InitializeRequestData', (_message.Message,), {'DESCRIPTOR': _INITIALIZEREQUESTDATA, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(InitializeRequestData)
UpdateRequestData = _reflection.GeneratedProtocolMessageType('UpdateRequestData', (_message.Message,), {'DESCRIPTOR': _UPDATEREQUESTDATA, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(UpdateRequestData)
BusinessDetails = _reflection.GeneratedProtocolMessageType('BusinessDetails', (_message.Message,), {'DESCRIPTOR': _BUSINESSDETAILS, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(BusinessDetails)
MonthlyTransactions = _reflection.GeneratedProtocolMessageType('MonthlyTransactions', (_message.Message,), {'DESCRIPTOR': _MONTHLYTRANSACTIONS, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(MonthlyTransactions)
PaymentMethodInformation = _reflection.GeneratedProtocolMessageType('PaymentMethodInformation', (_message.Message,), {'DESCRIPTOR': _PAYMENTMETHODINFORMATION, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(PaymentMethodInformation)
LegalEntity = _reflection.GeneratedProtocolMessageType('LegalEntity', (_message.Message,), {'DESCRIPTOR': _LEGALENTITY, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(LegalEntity)
Partnership = _reflection.GeneratedProtocolMessageType('Partnership', (_message.Message,), {'DESCRIPTOR': _PARTNERSHIP, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(Partnership)
Name = _reflection.GeneratedProtocolMessageType('Name', (_message.Message,), {'DESCRIPTOR': _NAME, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(Name)
Individual = _reflection.GeneratedProtocolMessageType('Individual', (_message.Message,), {'DESCRIPTOR': _INDIVIDUAL, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(Individual)
Organization = _reflection.GeneratedProtocolMessageType('Organization', (_message.Message,), {'DESCRIPTOR': _ORGANIZATION, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(Organization)
NonprofitOrganization = _reflection.GeneratedProtocolMessageType('NonprofitOrganization', (_message.Message,), {'DESCRIPTOR': _NONPROFITORGANIZATION, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(NonprofitOrganization)
Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {'DESCRIPTOR': _PERSON, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(Person)
Residence = _reflection.GeneratedProtocolMessageType('Residence', (_message.Message,), {'DESCRIPTOR': _RESIDENCE, '__module__': 'relay.onboarding.v1.paymentmethods.ppro_pb2'})
_sym_db.RegisterMessage(Residence)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"ZHgithub.com/Nedved75/grpcsimple/sdk/go/relay/onboarding/v1/paymentmethods\xaa\x02'Relay.Onboarding.V1.PaymentMethods.Ppro"
    _INITIALIZEREQUESTDATA._serialized_start = 124
    _INITIALIZEREQUESTDATA._serialized_end = 410
    _UPDATEREQUESTDATA._serialized_start = 413
    _UPDATEREQUESTDATA._serialized_end = 592
    _BUSINESSDETAILS._serialized_start = 595
    _BUSINESSDETAILS._serialized_end = 903
    _MONTHLYTRANSACTIONS._serialized_start = 905
    _MONTHLYTRANSACTIONS._serialized_end = 982
    _PAYMENTMETHODINFORMATION._serialized_start = 985
    _PAYMENTMETHODINFORMATION._serialized_end = 1135
    _LEGALENTITY._serialized_start = 1138
    _LEGALENTITY._serialized_end = 1473
    _PARTNERSHIP._serialized_start = 1476
    _PARTNERSHIP._serialized_end = 1670
    _NAME._serialized_start = 1672
    _NAME._serialized_end = 1753
    _INDIVIDUAL._serialized_start = 1756
    _INDIVIDUAL._serialized_end = 1918
    _ORGANIZATION._serialized_start = 1921
    _ORGANIZATION._serialized_end = 2202
    _NONPROFITORGANIZATION._serialized_start = 2205
    _NONPROFITORGANIZATION._serialized_end = 2495
    _PERSON._serialized_start = 2498
    _PERSON._serialized_end = 2689
    _RESIDENCE._serialized_start = 2691
    _RESIDENCE._serialized_end = 2783