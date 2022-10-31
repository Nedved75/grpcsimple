"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ....relay import models_pb2 as relay_dot_models__pb2
from ....relay.onboarding.v1.paymentmethods import expressbank_pb2 as relay_dot_onboarding_dot_v1_dot_paymentmethods_dot_expressbank__pb2
from ....relay.onboarding.v1.paymentmethods import klarna_pb2 as relay_dot_onboarding_dot_v1_dot_paymentmethods_dot_klarna__pb2
from ....relay.onboarding.v1.paymentmethods import ppro_pb2 as relay_dot_onboarding_dot_v1_dot_paymentmethods_dot_ppro__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;relay/onboarding/v1/payment_method_onboarding_service.proto\x12\x13relay.onboarding.v1\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x12relay/models.proto\x1a4relay/onboarding/v1/paymentmethods/expressbank.proto\x1a/relay/onboarding/v1/paymentmethods/klarna.proto\x1a-relay/onboarding/v1/paymentmethods/ppro.proto"\x91\x03\n\x11InitializeRequest\x12\x11\n\treference\x18\x01 \x01(\t\x12,\n\x0epayment_method\x18\x02 \x01(\x0e2\x14.relay.PaymentMethod\x12_\n\x15InitializeRequestPPRO\x18\x03 \x01(\x0b2>.relay.onboarding.v1.paymentmethods.ppro.InitializeRequestDataH\x00\x12m\n\x1cInitializeRequestExpressBank\x18\x04 \x01(\x0b2E.relay.onboarding.v1.paymentmethods.expressbank.InitializeRequestDataH\x00\x12c\n\x17InitializeRequestKlarna\x18\x05 \x01(\x0b2@.relay.onboarding.v1.paymentmethods.klarna.InitializeRequestDataH\x00B\x06\n\x04data"\x9e\x01\n\x12InitializeResponse\x12E\n\x1fpayment_method_configuration_id\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status"\x8b\x03\n\rUpdateRequest\x12\'\n\x1fpayment_method_configuration_id\x18\x01 \x01(\t\x12,\n\x0epayment_method\x18\x02 \x01(\x0e2\x14.relay.PaymentMethod\x12W\n\x11UpdateRequestPPRO\x18\x03 \x01(\x0b2:.relay.onboarding.v1.paymentmethods.ppro.UpdateRequestDataH\x00\x12e\n\x18UpdateRequestExpressBank\x18\x04 \x01(\x0b2A.relay.onboarding.v1.paymentmethods.expressbank.UpdateRequestDataH\x00\x12[\n\x13UpdateRequestKlarna\x18\x05 \x01(\x0b2<.relay.onboarding.v1.paymentmethods.klarna.UpdateRequestDataH\x00B\x06\n\x04data"S\n\x0eUpdateResponse\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status"c\n\nGetRequest\x12\'\n\x1fpayment_method_configuration_id\x18\x01 \x01(\t\x12,\n\x0epayment_method\x18\x02 \x01(\x0e2\x14.relay.PaymentMethod"\xae\x01\n\x0bGetResponse\x12\\\n payment_method_onboarding_status\x18\x01 \x01(\x0e22.relay.onboarding.v1.PaymentMethodOnboardingStatus\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status*o\n\x1dPaymentMethodOnboardingStatus\x12\x0b\n\x07PENDING\x10\x00\x12\r\n\tACTIVATED\x10\x01\x12\x11\n\rNON_COMPLIANT\x10\x02\x12\x0f\n\x0bDEACTIVATED\x10\x03\x12\x0e\n\nTERMINATED\x10\x042\x9b\x02\n\x17PaymentMethodOnboarding\x12_\n\nInitialize\x12&.relay.onboarding.v1.InitializeRequest\x1a\'.relay.onboarding.v1.InitializeResponse"\x00\x12S\n\x06Update\x12".relay.onboarding.v1.UpdateRequest\x1a#.relay.onboarding.v1.UpdateResponse"\x00\x12J\n\x03Get\x12\x1f.relay.onboarding.v1.GetRequest\x1a .relay.onboarding.v1.GetResponse"\x00BQZ9github.com/Nedved75/grpcsimple/sdk/go/relay/onboarding/v1\xaa\x02\x13Relay.Onboarding.V1b\x06proto3')
_PAYMENTMETHODONBOARDINGSTATUS = DESCRIPTOR.enum_types_by_name['PaymentMethodOnboardingStatus']
PaymentMethodOnboardingStatus = enum_type_wrapper.EnumTypeWrapper(_PAYMENTMETHODONBOARDINGSTATUS)
PENDING = 0
ACTIVATED = 1
NON_COMPLIANT = 2
DEACTIVATED = 3
TERMINATED = 4
_INITIALIZEREQUEST = DESCRIPTOR.message_types_by_name['InitializeRequest']
_INITIALIZERESPONSE = DESCRIPTOR.message_types_by_name['InitializeResponse']
_UPDATEREQUEST = DESCRIPTOR.message_types_by_name['UpdateRequest']
_UPDATERESPONSE = DESCRIPTOR.message_types_by_name['UpdateResponse']
_GETREQUEST = DESCRIPTOR.message_types_by_name['GetRequest']
_GETRESPONSE = DESCRIPTOR.message_types_by_name['GetResponse']
InitializeRequest = _reflection.GeneratedProtocolMessageType('InitializeRequest', (_message.Message,), {'DESCRIPTOR': _INITIALIZEREQUEST, '__module__': 'relay.onboarding.v1.payment_method_onboarding_service_pb2'})
_sym_db.RegisterMessage(InitializeRequest)
InitializeResponse = _reflection.GeneratedProtocolMessageType('InitializeResponse', (_message.Message,), {'DESCRIPTOR': _INITIALIZERESPONSE, '__module__': 'relay.onboarding.v1.payment_method_onboarding_service_pb2'})
_sym_db.RegisterMessage(InitializeResponse)
UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {'DESCRIPTOR': _UPDATEREQUEST, '__module__': 'relay.onboarding.v1.payment_method_onboarding_service_pb2'})
_sym_db.RegisterMessage(UpdateRequest)
UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {'DESCRIPTOR': _UPDATERESPONSE, '__module__': 'relay.onboarding.v1.payment_method_onboarding_service_pb2'})
_sym_db.RegisterMessage(UpdateResponse)
GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {'DESCRIPTOR': _GETREQUEST, '__module__': 'relay.onboarding.v1.payment_method_onboarding_service_pb2'})
_sym_db.RegisterMessage(GetRequest)
GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {'DESCRIPTOR': _GETRESPONSE, '__module__': 'relay.onboarding.v1.payment_method_onboarding_service_pb2'})
_sym_db.RegisterMessage(GetResponse)
_PAYMENTMETHODONBOARDING = DESCRIPTOR.services_by_name['PaymentMethodOnboarding']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/Nedved75/grpcsimple/sdk/go/relay/onboarding/v1\xaa\x02\x13Relay.Onboarding.V1'
    _PAYMENTMETHODONBOARDINGSTATUS._serialized_start = 1639
    _PAYMENTMETHODONBOARDINGSTATUS._serialized_end = 1750
    _INITIALIZEREQUEST._serialized_start = 314
    _INITIALIZEREQUEST._serialized_end = 715
    _INITIALIZERESPONSE._serialized_start = 718
    _INITIALIZERESPONSE._serialized_end = 876
    _UPDATEREQUEST._serialized_start = 879
    _UPDATEREQUEST._serialized_end = 1274
    _UPDATERESPONSE._serialized_start = 1276
    _UPDATERESPONSE._serialized_end = 1359
    _GETREQUEST._serialized_start = 1361
    _GETREQUEST._serialized_end = 1460
    _GETRESPONSE._serialized_start = 1463
    _GETRESPONSE._serialized_end = 1637
    _PAYMENTMETHODONBOARDING._serialized_start = 1753
    _PAYMENTMETHODONBOARDING._serialized_end = 2036