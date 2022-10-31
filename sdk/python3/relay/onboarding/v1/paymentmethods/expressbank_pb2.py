"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4relay/onboarding/v1/paymentmethods/expressbank.proto\x12.relay.onboarding.v1.paymentmethods.expressbank"\x90\x01\n\x15InitializeRequestData\x12\x12\n\npartner_id\x18\x01 \x01(\x03\x12\x18\n\x10product_group_id\x18\x02 \x01(\x03\x12\x1d\n\x15event_record_pass_key\x18\x03 \x01(\t\x12\x18\n\x10finance_pass_key\x18\x04 \x01(\t\x12\x10\n\x08currency\x18\x05 \x01(\t"\x8c\x01\n\x11UpdateRequestData\x12\x12\n\npartner_id\x18\x01 \x01(\x03\x12\x18\n\x10product_group_id\x18\x02 \x01(\x03\x12\x1d\n\x15event_record_pass_key\x18\x03 \x01(\t\x12\x18\n\x10finance_pass_key\x18\x04 \x01(\t\x12\x10\n\x08currency\x18\x05 \x01(\tB{ZHgithub.com/Nedved75/grpcsimple/sdk/go/relay/onboarding/v1/paymentmethods\xaa\x02.Relay.Onboarding.V1.PaymentMethods.ExpressBankb\x06proto3')
_INITIALIZEREQUESTDATA = DESCRIPTOR.message_types_by_name['InitializeRequestData']
_UPDATEREQUESTDATA = DESCRIPTOR.message_types_by_name['UpdateRequestData']
InitializeRequestData = _reflection.GeneratedProtocolMessageType('InitializeRequestData', (_message.Message,), {'DESCRIPTOR': _INITIALIZEREQUESTDATA, '__module__': 'relay.onboarding.v1.paymentmethods.expressbank_pb2'})
_sym_db.RegisterMessage(InitializeRequestData)
UpdateRequestData = _reflection.GeneratedProtocolMessageType('UpdateRequestData', (_message.Message,), {'DESCRIPTOR': _UPDATEREQUESTDATA, '__module__': 'relay.onboarding.v1.paymentmethods.expressbank_pb2'})
_sym_db.RegisterMessage(UpdateRequestData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZHgithub.com/Nedved75/grpcsimple/sdk/go/relay/onboarding/v1/paymentmethods\xaa\x02.Relay.Onboarding.V1.PaymentMethods.ExpressBank'
    _INITIALIZEREQUESTDATA._serialized_start = 105
    _INITIALIZEREQUESTDATA._serialized_end = 249
    _UPDATEREQUESTDATA._serialized_start = 252
    _UPDATEREQUESTDATA._serialized_end = 392