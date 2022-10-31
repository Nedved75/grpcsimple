"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5relay/processing/v1/paymentmethods/ppro/trustly.proto\x12/relay.processing.v1.paymentmethods.ppro.trustly"\xcc\x01\n\x11ChargeRequestData\x12j\n\x11payment_flow_data\x18\x01 \x01(\x0b2O.relay.processing.v1.paymentmethods.ppro.trustly.PaymentFlowRedirectRequestData\x12K\n\x08consumer\x18\x02 \x01(\x0b29.relay.processing.v1.paymentmethods.ppro.trustly.Consumer"\x81\x01\n\x12ChargeResponseData\x12k\n\x11payment_flow_data\x18\x01 \x01(\x0b2P.relay.processing.v1.paymentmethods.ppro.trustly.PaymentFlowRedirectResponseData"A\n\x08Consumer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0ccountry_code\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t"]\n\x1ePaymentFlowRedirectRequestData\x12\x13\n\x0bsuccess_url\x18\x01 \x01(\t\x12\x12\n\nfailed_url\x18\x02 \x01(\t\x12\x12\n\ncancel_url\x18\x03 \x01(\t"7\n\x1fPaymentFlowRedirectResponseData\x12\x14\n\x0capproval_url\x18\x01 \x01(\tB\x81\x01ZMgithub.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1/paymentmethods/ppro\xaa\x02/Relay.Processing.V1.PaymentMethods.Ppro.Trustlyb\x06proto3')
_CHARGEREQUESTDATA = DESCRIPTOR.message_types_by_name['ChargeRequestData']
_CHARGERESPONSEDATA = DESCRIPTOR.message_types_by_name['ChargeResponseData']
_CONSUMER = DESCRIPTOR.message_types_by_name['Consumer']
_PAYMENTFLOWREDIRECTREQUESTDATA = DESCRIPTOR.message_types_by_name['PaymentFlowRedirectRequestData']
_PAYMENTFLOWREDIRECTRESPONSEDATA = DESCRIPTOR.message_types_by_name['PaymentFlowRedirectResponseData']
ChargeRequestData = _reflection.GeneratedProtocolMessageType('ChargeRequestData', (_message.Message,), {'DESCRIPTOR': _CHARGEREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.ppro.trustly_pb2'})
_sym_db.RegisterMessage(ChargeRequestData)
ChargeResponseData = _reflection.GeneratedProtocolMessageType('ChargeResponseData', (_message.Message,), {'DESCRIPTOR': _CHARGERESPONSEDATA, '__module__': 'relay.processing.v1.paymentmethods.ppro.trustly_pb2'})
_sym_db.RegisterMessage(ChargeResponseData)
Consumer = _reflection.GeneratedProtocolMessageType('Consumer', (_message.Message,), {'DESCRIPTOR': _CONSUMER, '__module__': 'relay.processing.v1.paymentmethods.ppro.trustly_pb2'})
_sym_db.RegisterMessage(Consumer)
PaymentFlowRedirectRequestData = _reflection.GeneratedProtocolMessageType('PaymentFlowRedirectRequestData', (_message.Message,), {'DESCRIPTOR': _PAYMENTFLOWREDIRECTREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.ppro.trustly_pb2'})
_sym_db.RegisterMessage(PaymentFlowRedirectRequestData)
PaymentFlowRedirectResponseData = _reflection.GeneratedProtocolMessageType('PaymentFlowRedirectResponseData', (_message.Message,), {'DESCRIPTOR': _PAYMENTFLOWREDIRECTRESPONSEDATA, '__module__': 'relay.processing.v1.paymentmethods.ppro.trustly_pb2'})
_sym_db.RegisterMessage(PaymentFlowRedirectResponseData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZMgithub.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1/paymentmethods/ppro\xaa\x02/Relay.Processing.V1.PaymentMethods.Ppro.Trustly'
    _CHARGEREQUESTDATA._serialized_start = 107
    _CHARGEREQUESTDATA._serialized_end = 311
    _CHARGERESPONSEDATA._serialized_start = 314
    _CHARGERESPONSEDATA._serialized_end = 443
    _CONSUMER._serialized_start = 445
    _CONSUMER._serialized_end = 510
    _PAYMENTFLOWREDIRECTREQUESTDATA._serialized_start = 512
    _PAYMENTFLOWREDIRECTREQUESTDATA._serialized_end = 605
    _PAYMENTFLOWREDIRECTRESPONSEDATA._serialized_start = 607
    _PAYMENTFLOWREDIRECTRESPONSEDATA._serialized_end = 662