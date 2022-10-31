"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12relay/models.proto\x12\x05relay\x1a\x19google/protobuf/any.proto"N\n\x06Status\x12\x0c\n\x04code\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12%\n\x07details\x18\x03 \x03(\x0b2\x14.google.protobuf.Any"&\n\x05Error\x12\x0c\n\x04code\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t"H\n\x0fValidationError\x12\x0c\n\x04code\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x16\n\x0eparameter_name\x18\x03 \x01(\t*\xa6\x01\n\rPaymentMethod\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x10\n\x0cPPRO_TRUSTLY\x10\x01\x12\x0f\n\x0bPPRO_SOFORT\x10\x02\x12\x0e\n\nPPRO_IDEAL\x10\x03\x12\x13\n\x0fPPRO_BANCONTACT\x10\x04\x12\x10\n\x0cEXPRESS_BANK\x10\x05\x12\x0c\n\x08PPRO_EPS\x10\x06\x12\x10\n\x0cPPRO_GIROPAY\x10\x07\x12\n\n\x06KLARNA\x10\x08B5Z+github.com/Nedved75/grpcsimple/sdk/go/relay\xaa\x02\x05Relayb\x06proto3')
_PAYMENTMETHOD = DESCRIPTOR.enum_types_by_name['PaymentMethod']
PaymentMethod = enum_type_wrapper.EnumTypeWrapper(_PAYMENTMETHOD)
UNSPECIFIED = 0
PPRO_TRUSTLY = 1
PPRO_SOFORT = 2
PPRO_IDEAL = 3
PPRO_BANCONTACT = 4
EXPRESS_BANK = 5
PPRO_EPS = 6
PPRO_GIROPAY = 7
KLARNA = 8
_STATUS = DESCRIPTOR.message_types_by_name['Status']
_ERROR = DESCRIPTOR.message_types_by_name['Error']
_VALIDATIONERROR = DESCRIPTOR.message_types_by_name['ValidationError']
Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {'DESCRIPTOR': _STATUS, '__module__': 'relay.models_pb2'})
_sym_db.RegisterMessage(Status)
Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {'DESCRIPTOR': _ERROR, '__module__': 'relay.models_pb2'})
_sym_db.RegisterMessage(Error)
ValidationError = _reflection.GeneratedProtocolMessageType('ValidationError', (_message.Message,), {'DESCRIPTOR': _VALIDATIONERROR, '__module__': 'relay.models_pb2'})
_sym_db.RegisterMessage(ValidationError)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z+github.com/Nedved75/grpcsimple/sdk/go/relay\xaa\x02\x05Relay'
    _PAYMENTMETHOD._serialized_start = 251
    _PAYMENTMETHOD._serialized_end = 417
    _STATUS._serialized_start = 56
    _STATUS._serialized_end = 134
    _ERROR._serialized_start = 136
    _ERROR._serialized_end = 174
    _VALIDATIONERROR._serialized_start = 176
    _VALIDATIONERROR._serialized_end = 248