"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n relay/processing/v1/models.proto\x12\x13relay.processing.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbb\x02\n\x10OperationSummary\x12\n\n\x02id\x18\x01 \x01(\t\x121\n\toperation\x18\x02 \x01(\x0e2\x1e.relay.processing.v1.Operation\x12\x0e\n\x06amount\x18\x03 \x01(\x03\x120\n\x0clast_updated\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x11\n\treference\x18\x05 \x01(\t\x12\x17\n\x0frecon_reference\x18\x06 \x01(\t\x12\x10\n\x08currency\x18\x07 \x01(\t\x124\n\x06status\x18d \x01(\x0e2$.relay.processing.v1.OperationStatus\x122\n\x05error\x18e \x01(\x0b2#.relay.processing.v1.OperationError"/\n\x0eOperationError\x12\x0c\n\x04code\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t"Z\n\x05Order\x12\x0e\n\x06amount\x18\x01 \x01(\x03\x12\x10\n\x08currency\x18\x02 \x01(\t\x12/\n\treference\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValue*K\n\tOperation\x12\r\n\tAUTHORIZE\x10\x00\x12\n\n\x06CANCEL\x10\x01\x12\n\n\x06CHARGE\x10\x02\x12\n\n\x06REFUND\x10\x03\x12\x0b\n\x07CAPTURE\x10\x04*9\n\x0fOperationStatus\x12\x0b\n\x07PENDING\x10\x00\x12\r\n\tCOMPLETED\x10\x01\x12\n\n\x06FAILED\x10\x02BQZ9github.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1\xaa\x02\x13Relay.Processing.V1b\x06proto3')
_OPERATION = DESCRIPTOR.enum_types_by_name['Operation']
Operation = enum_type_wrapper.EnumTypeWrapper(_OPERATION)
_OPERATIONSTATUS = DESCRIPTOR.enum_types_by_name['OperationStatus']
OperationStatus = enum_type_wrapper.EnumTypeWrapper(_OPERATIONSTATUS)
AUTHORIZE = 0
CANCEL = 1
CHARGE = 2
REFUND = 3
CAPTURE = 4
PENDING = 0
COMPLETED = 1
FAILED = 2
_OPERATIONSUMMARY = DESCRIPTOR.message_types_by_name['OperationSummary']
_OPERATIONERROR = DESCRIPTOR.message_types_by_name['OperationError']
_ORDER = DESCRIPTOR.message_types_by_name['Order']
OperationSummary = _reflection.GeneratedProtocolMessageType('OperationSummary', (_message.Message,), {'DESCRIPTOR': _OPERATIONSUMMARY, '__module__': 'relay.processing.v1.models_pb2'})
_sym_db.RegisterMessage(OperationSummary)
OperationError = _reflection.GeneratedProtocolMessageType('OperationError', (_message.Message,), {'DESCRIPTOR': _OPERATIONERROR, '__module__': 'relay.processing.v1.models_pb2'})
_sym_db.RegisterMessage(OperationError)
Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {'DESCRIPTOR': _ORDER, '__module__': 'relay.processing.v1.models_pb2'})
_sym_db.RegisterMessage(Order)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1\xaa\x02\x13Relay.Processing.V1'
    _OPERATION._serialized_start = 581
    _OPERATION._serialized_end = 656
    _OPERATIONSTATUS._serialized_start = 658
    _OPERATIONSTATUS._serialized_end = 715
    _OPERATIONSUMMARY._serialized_start = 123
    _OPERATIONSUMMARY._serialized_end = 438
    _OPERATIONERROR._serialized_start = 440
    _OPERATIONERROR._serialized_end = 487
    _ORDER._serialized_start = 489
    _ORDER._serialized_end = 579