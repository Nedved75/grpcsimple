"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8relay/processing/v1/paymentmethods/ppro/bancontact.proto\x122relay.processing.v1.paymentmethods.ppro.bancontact"\xd2\x01\n\x11ChargeRequestData\x12m\n\x11payment_flow_data\x18\x01 \x01(\x0b2R.relay.processing.v1.paymentmethods.ppro.bancontact.PaymentFlowRedirectRequestData\x12N\n\x08consumer\x18\x02 \x01(\x0b2<.relay.processing.v1.paymentmethods.ppro.bancontact.Consumer"\x84\x01\n\x12ChargeResponseData\x12n\n\x11payment_flow_data\x18\x01 \x01(\x0b2S.relay.processing.v1.paymentmethods.ppro.bancontact.PaymentFlowRedirectResponseData"J\n\x08Consumer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0ccountry_code\x18\x02 \x01(\t\x12\x1a\n\x12preferred_language\x18\x03 \x01(\t"u\n\x1ePaymentFlowRedirectRequestData\x12\x13\n\x0bsuccess_url\x18\x01 \x01(\t\x12\x12\n\nfailed_url\x18\x02 \x01(\t\x12\x12\n\ncancel_url\x18\x03 \x01(\t\x12\x16\n\x0eapp_to_app_url\x18\x04 \x01(\t"7\n\x1fPaymentFlowRedirectResponseData\x12\x14\n\x0capproval_url\x18\x01 \x01(\tB\x84\x01ZMgithub.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1/paymentmethods/ppro\xaa\x022Relay.Processing.V1.PaymentMethods.Ppro.Bancontactb\x06proto3')
_CHARGEREQUESTDATA = DESCRIPTOR.message_types_by_name['ChargeRequestData']
_CHARGERESPONSEDATA = DESCRIPTOR.message_types_by_name['ChargeResponseData']
_CONSUMER = DESCRIPTOR.message_types_by_name['Consumer']
_PAYMENTFLOWREDIRECTREQUESTDATA = DESCRIPTOR.message_types_by_name['PaymentFlowRedirectRequestData']
_PAYMENTFLOWREDIRECTRESPONSEDATA = DESCRIPTOR.message_types_by_name['PaymentFlowRedirectResponseData']
ChargeRequestData = _reflection.GeneratedProtocolMessageType('ChargeRequestData', (_message.Message,), {'DESCRIPTOR': _CHARGEREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.ppro.bancontact_pb2'})
_sym_db.RegisterMessage(ChargeRequestData)
ChargeResponseData = _reflection.GeneratedProtocolMessageType('ChargeResponseData', (_message.Message,), {'DESCRIPTOR': _CHARGERESPONSEDATA, '__module__': 'relay.processing.v1.paymentmethods.ppro.bancontact_pb2'})
_sym_db.RegisterMessage(ChargeResponseData)
Consumer = _reflection.GeneratedProtocolMessageType('Consumer', (_message.Message,), {'DESCRIPTOR': _CONSUMER, '__module__': 'relay.processing.v1.paymentmethods.ppro.bancontact_pb2'})
_sym_db.RegisterMessage(Consumer)
PaymentFlowRedirectRequestData = _reflection.GeneratedProtocolMessageType('PaymentFlowRedirectRequestData', (_message.Message,), {'DESCRIPTOR': _PAYMENTFLOWREDIRECTREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.ppro.bancontact_pb2'})
_sym_db.RegisterMessage(PaymentFlowRedirectRequestData)
PaymentFlowRedirectResponseData = _reflection.GeneratedProtocolMessageType('PaymentFlowRedirectResponseData', (_message.Message,), {'DESCRIPTOR': _PAYMENTFLOWREDIRECTRESPONSEDATA, '__module__': 'relay.processing.v1.paymentmethods.ppro.bancontact_pb2'})
_sym_db.RegisterMessage(PaymentFlowRedirectResponseData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZMgithub.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1/paymentmethods/ppro\xaa\x022Relay.Processing.V1.PaymentMethods.Ppro.Bancontact'
    _CHARGEREQUESTDATA._serialized_start = 113
    _CHARGEREQUESTDATA._serialized_end = 323
    _CHARGERESPONSEDATA._serialized_start = 326
    _CHARGERESPONSEDATA._serialized_end = 458
    _CONSUMER._serialized_start = 460
    _CONSUMER._serialized_end = 534
    _PAYMENTFLOWREDIRECTREQUESTDATA._serialized_start = 536
    _PAYMENTFLOWREDIRECTREQUESTDATA._serialized_end = 653
    _PAYMENTFLOWREDIRECTRESPONSEDATA._serialized_start = 655
    _PAYMENTFLOWREDIRECTRESPONSEDATA._serialized_end = 710