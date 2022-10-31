"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ....relay import models_pb2 as relay_dot_models__pb2
from ....relay.processing.v1 import models_pb2 as relay_dot_processing_dot_v1_dot_models__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4relay/processing/v1/payment_processing_service.proto\x12\x13relay.processing.v1\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x12relay/models.proto\x1a relay/processing/v1/models.proto"\xdf\x01\n\x10AuthorizeRequest\x12\'\n\x1fpayment_method_configuration_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t\x12,\n\x0epayment_method\x18\x04 \x01(\x0e2\x14.relay.PaymentMethod\x12)\n\x05order\x18\x05 \x01(\x0b2\x1a.relay.processing.v1.Order\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any"\xc0\x01\n\x11AuthorizeResponse\x120\n\npayment_id\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x126\n\x10authorization_id\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status"n\n\rCancelRequest\x12\x12\n\npayment_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any"\xb6\x01\n\x0eCancelResponse\x120\n\npayment_id\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12/\n\tcancel_id\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status"\x7f\n\x0eCaptureRequest\x12\x12\n\npayment_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t\x12\x0e\n\x06amount\x18\x04 \x01(\x03\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any"\xb8\x01\n\x0fCaptureResponse\x120\n\npayment_id\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x120\n\ncapture_id\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status"\xdc\x01\n\rChargeRequest\x12\'\n\x1fpayment_method_configuration_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t\x12,\n\x0epayment_method\x18\x04 \x01(\x0e2\x14.relay.PaymentMethod\x12)\n\x05order\x18\x05 \x01(\x0b2\x1a.relay.processing.v1.Order\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any"\xb6\x01\n\x0eChargeResponse\x120\n\npayment_id\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12/\n\tcharge_id\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status"~\n\rRefundRequest\x12\x12\n\npayment_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t\x12\x0e\n\x06amount\x18\x04 \x01(\x03\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any"\x84\x01\n\x0eRefundResponse\x12/\n\trefund_id\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status"\'\n\x11GetSummaryRequest\x12\x12\n\npayment_id\x18\x01 \x01(\t"\xc9\x01\n\x12GetSummaryResponse\x12\x19\n\x11authorized_amount\x18\x01 \x01(\x03\x12\x17\n\x0fcaptured_amount\x18\x02 \x01(\x03\x12\x17\n\x0fcanceled_amount\x18\x03 \x01(\x03\x12\x17\n\x0frefunded_amount\x18\x04 \x01(\x03\x12.\n\x08currency\x18\x05 \x01(\x0b2\x1c.google.protobuf.StringValue\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status"1\n\x1bGetOperationsSummaryRequest\x12\x12\n\npayment_id\x18\x01 \x01(\t"x\n\x1cGetOperationsSummaryResponse\x129\n\noperations\x18\x01 \x03(\x0b2%.relay.processing.v1.OperationSummary\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status2\xa8\x05\n\x11PaymentProcessing\x12\\\n\tAuthorize\x12%.relay.processing.v1.AuthorizeRequest\x1a&.relay.processing.v1.AuthorizeResponse"\x00\x12S\n\x06Cancel\x12".relay.processing.v1.CancelRequest\x1a#.relay.processing.v1.CancelResponse"\x00\x12V\n\x07Capture\x12#.relay.processing.v1.CaptureRequest\x1a$.relay.processing.v1.CaptureResponse"\x00\x12S\n\x06Charge\x12".relay.processing.v1.ChargeRequest\x1a#.relay.processing.v1.ChargeResponse"\x00\x12S\n\x06Refund\x12".relay.processing.v1.RefundRequest\x1a#.relay.processing.v1.RefundResponse"\x00\x12_\n\nGetSummary\x12&.relay.processing.v1.GetSummaryRequest\x1a\'.relay.processing.v1.GetSummaryResponse"\x00\x12}\n\x14GetOperationsSummary\x120.relay.processing.v1.GetOperationsSummaryRequest\x1a1.relay.processing.v1.GetOperationsSummaryResponse"\x00BQZ9github.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1\xaa\x02\x13Relay.Processing.V1b\x06proto3')
_AUTHORIZEREQUEST = DESCRIPTOR.message_types_by_name['AuthorizeRequest']
_AUTHORIZERESPONSE = DESCRIPTOR.message_types_by_name['AuthorizeResponse']
_CANCELREQUEST = DESCRIPTOR.message_types_by_name['CancelRequest']
_CANCELRESPONSE = DESCRIPTOR.message_types_by_name['CancelResponse']
_CAPTUREREQUEST = DESCRIPTOR.message_types_by_name['CaptureRequest']
_CAPTURERESPONSE = DESCRIPTOR.message_types_by_name['CaptureResponse']
_CHARGEREQUEST = DESCRIPTOR.message_types_by_name['ChargeRequest']
_CHARGERESPONSE = DESCRIPTOR.message_types_by_name['ChargeResponse']
_REFUNDREQUEST = DESCRIPTOR.message_types_by_name['RefundRequest']
_REFUNDRESPONSE = DESCRIPTOR.message_types_by_name['RefundResponse']
_GETSUMMARYREQUEST = DESCRIPTOR.message_types_by_name['GetSummaryRequest']
_GETSUMMARYRESPONSE = DESCRIPTOR.message_types_by_name['GetSummaryResponse']
_GETOPERATIONSSUMMARYREQUEST = DESCRIPTOR.message_types_by_name['GetOperationsSummaryRequest']
_GETOPERATIONSSUMMARYRESPONSE = DESCRIPTOR.message_types_by_name['GetOperationsSummaryResponse']
AuthorizeRequest = _reflection.GeneratedProtocolMessageType('AuthorizeRequest', (_message.Message,), {'DESCRIPTOR': _AUTHORIZEREQUEST, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(AuthorizeRequest)
AuthorizeResponse = _reflection.GeneratedProtocolMessageType('AuthorizeResponse', (_message.Message,), {'DESCRIPTOR': _AUTHORIZERESPONSE, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(AuthorizeResponse)
CancelRequest = _reflection.GeneratedProtocolMessageType('CancelRequest', (_message.Message,), {'DESCRIPTOR': _CANCELREQUEST, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(CancelRequest)
CancelResponse = _reflection.GeneratedProtocolMessageType('CancelResponse', (_message.Message,), {'DESCRIPTOR': _CANCELRESPONSE, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(CancelResponse)
CaptureRequest = _reflection.GeneratedProtocolMessageType('CaptureRequest', (_message.Message,), {'DESCRIPTOR': _CAPTUREREQUEST, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(CaptureRequest)
CaptureResponse = _reflection.GeneratedProtocolMessageType('CaptureResponse', (_message.Message,), {'DESCRIPTOR': _CAPTURERESPONSE, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(CaptureResponse)
ChargeRequest = _reflection.GeneratedProtocolMessageType('ChargeRequest', (_message.Message,), {'DESCRIPTOR': _CHARGEREQUEST, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(ChargeRequest)
ChargeResponse = _reflection.GeneratedProtocolMessageType('ChargeResponse', (_message.Message,), {'DESCRIPTOR': _CHARGERESPONSE, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(ChargeResponse)
RefundRequest = _reflection.GeneratedProtocolMessageType('RefundRequest', (_message.Message,), {'DESCRIPTOR': _REFUNDREQUEST, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(RefundRequest)
RefundResponse = _reflection.GeneratedProtocolMessageType('RefundResponse', (_message.Message,), {'DESCRIPTOR': _REFUNDRESPONSE, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(RefundResponse)
GetSummaryRequest = _reflection.GeneratedProtocolMessageType('GetSummaryRequest', (_message.Message,), {'DESCRIPTOR': _GETSUMMARYREQUEST, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(GetSummaryRequest)
GetSummaryResponse = _reflection.GeneratedProtocolMessageType('GetSummaryResponse', (_message.Message,), {'DESCRIPTOR': _GETSUMMARYRESPONSE, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(GetSummaryResponse)
GetOperationsSummaryRequest = _reflection.GeneratedProtocolMessageType('GetOperationsSummaryRequest', (_message.Message,), {'DESCRIPTOR': _GETOPERATIONSSUMMARYREQUEST, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(GetOperationsSummaryRequest)
GetOperationsSummaryResponse = _reflection.GeneratedProtocolMessageType('GetOperationsSummaryResponse', (_message.Message,), {'DESCRIPTOR': _GETOPERATIONSSUMMARYRESPONSE, '__module__': 'relay.processing.v1.payment_processing_service_pb2'})
_sym_db.RegisterMessage(GetOperationsSummaryResponse)
_PAYMENTPROCESSING = DESCRIPTOR.services_by_name['PaymentProcessing']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1\xaa\x02\x13Relay.Processing.V1'
    _AUTHORIZEREQUEST._serialized_start = 191
    _AUTHORIZEREQUEST._serialized_end = 414
    _AUTHORIZERESPONSE._serialized_start = 417
    _AUTHORIZERESPONSE._serialized_end = 609
    _CANCELREQUEST._serialized_start = 611
    _CANCELREQUEST._serialized_end = 721
    _CANCELRESPONSE._serialized_start = 724
    _CANCELRESPONSE._serialized_end = 906
    _CAPTUREREQUEST._serialized_start = 908
    _CAPTUREREQUEST._serialized_end = 1035
    _CAPTURERESPONSE._serialized_start = 1038
    _CAPTURERESPONSE._serialized_end = 1222
    _CHARGEREQUEST._serialized_start = 1225
    _CHARGEREQUEST._serialized_end = 1445
    _CHARGERESPONSE._serialized_start = 1448
    _CHARGERESPONSE._serialized_end = 1630
    _REFUNDREQUEST._serialized_start = 1632
    _REFUNDREQUEST._serialized_end = 1758
    _REFUNDRESPONSE._serialized_start = 1761
    _REFUNDRESPONSE._serialized_end = 1893
    _GETSUMMARYREQUEST._serialized_start = 1895
    _GETSUMMARYREQUEST._serialized_end = 1934
    _GETSUMMARYRESPONSE._serialized_start = 1937
    _GETSUMMARYRESPONSE._serialized_end = 2138
    _GETOPERATIONSSUMMARYREQUEST._serialized_start = 2140
    _GETOPERATIONSSUMMARYREQUEST._serialized_end = 2189
    _GETOPERATIONSSUMMARYRESPONSE._serialized_start = 2191
    _GETOPERATIONSSUMMARYRESPONSE._serialized_end = 2311
    _PAYMENTPROCESSING._serialized_start = 2314
    _PAYMENTPROCESSING._serialized_end = 2994