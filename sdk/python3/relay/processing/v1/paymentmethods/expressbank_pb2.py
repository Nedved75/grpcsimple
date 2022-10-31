"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4relay/processing/v1/paymentmethods/expressbank.proto\x12.relay.processing.v1.paymentmethods.expressbank"\x90\x01\n\x14AuthorizeRequestData\x12i\n\x11payment_flow_data\x18\x01 \x01(\x0b2N.relay.processing.v1.paymentmethods.expressbank.PaymentFlowRedirectRequestData\x12\r\n\x05items\x18\x02 \x03(\t"\x83\x01\n\x15AuthorizeResponseData\x12j\n\x11payment_flow_data\x18\x01 \x01(\x0b2O.relay.processing.v1.paymentmethods.expressbank.PaymentFlowRedirectResponseData"7\n\x1fPaymentFlowRedirectResponseData\x12\x14\n\x0capproval_url\x18\x01 \x01(\t"j\n\x11RefundRequestData\x12U\n\x0breason_code\x18\x01 \x01(\x0e2@.relay.processing.v1.paymentmethods.expressbank.RefundReasonCode"I\n\x1ePaymentFlowRedirectRequestData\x12\x13\n\x0bsuccess_url\x18\x01 \x01(\t\x12\x12\n\nfailed_url\x18\x02 \x01(\t*|\n\x10RefundReasonCode\x12\x15\n\x11DEFECT_IN_PRODUCT\x10\x00\x12\x1d\n\x19CUSTOMER_CHANGED_HIS_MIND\x10\x01\x12\x14\n\x10PRODUCT_RECALLED\x10\x02\x12\x1c\n\x18TECHNICAL_OR_HUMAN_ERROR\x10\x03B{ZHgithub.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1/paymentmethods\xaa\x02.Relay.Processing.V1.PaymentMethods.ExpressBankb\x06proto3')
_REFUNDREASONCODE = DESCRIPTOR.enum_types_by_name['RefundReasonCode']
RefundReasonCode = enum_type_wrapper.EnumTypeWrapper(_REFUNDREASONCODE)
DEFECT_IN_PRODUCT = 0
CUSTOMER_CHANGED_HIS_MIND = 1
PRODUCT_RECALLED = 2
TECHNICAL_OR_HUMAN_ERROR = 3
_AUTHORIZEREQUESTDATA = DESCRIPTOR.message_types_by_name['AuthorizeRequestData']
_AUTHORIZERESPONSEDATA = DESCRIPTOR.message_types_by_name['AuthorizeResponseData']
_PAYMENTFLOWREDIRECTRESPONSEDATA = DESCRIPTOR.message_types_by_name['PaymentFlowRedirectResponseData']
_REFUNDREQUESTDATA = DESCRIPTOR.message_types_by_name['RefundRequestData']
_PAYMENTFLOWREDIRECTREQUESTDATA = DESCRIPTOR.message_types_by_name['PaymentFlowRedirectRequestData']
AuthorizeRequestData = _reflection.GeneratedProtocolMessageType('AuthorizeRequestData', (_message.Message,), {'DESCRIPTOR': _AUTHORIZEREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.expressbank_pb2'})
_sym_db.RegisterMessage(AuthorizeRequestData)
AuthorizeResponseData = _reflection.GeneratedProtocolMessageType('AuthorizeResponseData', (_message.Message,), {'DESCRIPTOR': _AUTHORIZERESPONSEDATA, '__module__': 'relay.processing.v1.paymentmethods.expressbank_pb2'})
_sym_db.RegisterMessage(AuthorizeResponseData)
PaymentFlowRedirectResponseData = _reflection.GeneratedProtocolMessageType('PaymentFlowRedirectResponseData', (_message.Message,), {'DESCRIPTOR': _PAYMENTFLOWREDIRECTRESPONSEDATA, '__module__': 'relay.processing.v1.paymentmethods.expressbank_pb2'})
_sym_db.RegisterMessage(PaymentFlowRedirectResponseData)
RefundRequestData = _reflection.GeneratedProtocolMessageType('RefundRequestData', (_message.Message,), {'DESCRIPTOR': _REFUNDREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.expressbank_pb2'})
_sym_db.RegisterMessage(RefundRequestData)
PaymentFlowRedirectRequestData = _reflection.GeneratedProtocolMessageType('PaymentFlowRedirectRequestData', (_message.Message,), {'DESCRIPTOR': _PAYMENTFLOWREDIRECTREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.expressbank_pb2'})
_sym_db.RegisterMessage(PaymentFlowRedirectRequestData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZHgithub.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1/paymentmethods\xaa\x02.Relay.Processing.V1.PaymentMethods.ExpressBank'
    _REFUNDREASONCODE._serialized_start = 625
    _REFUNDREASONCODE._serialized_end = 749
    _AUTHORIZEREQUESTDATA._serialized_start = 105
    _AUTHORIZEREQUESTDATA._serialized_end = 249
    _AUTHORIZERESPONSEDATA._serialized_start = 252
    _AUTHORIZERESPONSEDATA._serialized_end = 383
    _PAYMENTFLOWREDIRECTRESPONSEDATA._serialized_start = 385
    _PAYMENTFLOWREDIRECTRESPONSEDATA._serialized_end = 440
    _REFUNDREQUESTDATA._serialized_start = 442
    _REFUNDREQUESTDATA._serialized_end = 548
    _PAYMENTFLOWREDIRECTREQUESTDATA._serialized_start = 550
    _PAYMENTFLOWREDIRECTREQUESTDATA._serialized_end = 623