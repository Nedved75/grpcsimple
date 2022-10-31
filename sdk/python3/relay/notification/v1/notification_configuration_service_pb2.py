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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>relay/notification/v1/notification_configuration_service.proto\x12\x15relay.notification.v1\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x12relay/models.proto"T\n!CreateWebhookConfigurationRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06events\x18\x02 \x03(\t\x12\x0b\n\x03url\x18\x03 \x01(\t"\x88\x01\n"CreateWebhookConfigurationResponse\x12C\n\x1dnotification_configuration_id\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status"@\n\x17GetConfigurationRequest\x12%\n\x1dnotification_configuration_id\x18\x01 \x01(\t"m\n\x18GetConfigurationResponse\x12\x0e\n\x06events\x18\x01 \x03(\t\x12"\n\x04data\x18d \x01(\x0b2\x14.google.protobuf.Any\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status"C\n\x1aDeleteConfigurationRequest\x12%\n\x1dnotification_configuration_id\x18\x01 \x01(\t"<\n\x1bDeleteConfigurationResponse\x12\x1d\n\x06status\x18e \x01(\x0b2\r.relay.Status2\x8e\x03\n\x19NotificationConfiguration\x12\x93\x01\n\x1aCreateWebhookConfiguration\x128.relay.notification.v1.CreateWebhookConfigurationRequest\x1a9.relay.notification.v1.CreateWebhookConfigurationResponse"\x00\x12h\n\x03Get\x12..relay.notification.v1.GetConfigurationRequest\x1a/.relay.notification.v1.GetConfigurationResponse"\x00\x12q\n\x06Delete\x121.relay.notification.v1.DeleteConfigurationRequest\x1a2.relay.notification.v1.DeleteConfigurationResponse"\x00BUZ;github.com/Nedved75/grpcsimple/sdk/go/relay/notification/v1\xaa\x02\x15Relay.Notification.V1b\x06proto3')
_CREATEWEBHOOKCONFIGURATIONREQUEST = DESCRIPTOR.message_types_by_name['CreateWebhookConfigurationRequest']
_CREATEWEBHOOKCONFIGURATIONRESPONSE = DESCRIPTOR.message_types_by_name['CreateWebhookConfigurationResponse']
_GETCONFIGURATIONREQUEST = DESCRIPTOR.message_types_by_name['GetConfigurationRequest']
_GETCONFIGURATIONRESPONSE = DESCRIPTOR.message_types_by_name['GetConfigurationResponse']
_DELETECONFIGURATIONREQUEST = DESCRIPTOR.message_types_by_name['DeleteConfigurationRequest']
_DELETECONFIGURATIONRESPONSE = DESCRIPTOR.message_types_by_name['DeleteConfigurationResponse']
CreateWebhookConfigurationRequest = _reflection.GeneratedProtocolMessageType('CreateWebhookConfigurationRequest', (_message.Message,), {'DESCRIPTOR': _CREATEWEBHOOKCONFIGURATIONREQUEST, '__module__': 'relay.notification.v1.notification_configuration_service_pb2'})
_sym_db.RegisterMessage(CreateWebhookConfigurationRequest)
CreateWebhookConfigurationResponse = _reflection.GeneratedProtocolMessageType('CreateWebhookConfigurationResponse', (_message.Message,), {'DESCRIPTOR': _CREATEWEBHOOKCONFIGURATIONRESPONSE, '__module__': 'relay.notification.v1.notification_configuration_service_pb2'})
_sym_db.RegisterMessage(CreateWebhookConfigurationResponse)
GetConfigurationRequest = _reflection.GeneratedProtocolMessageType('GetConfigurationRequest', (_message.Message,), {'DESCRIPTOR': _GETCONFIGURATIONREQUEST, '__module__': 'relay.notification.v1.notification_configuration_service_pb2'})
_sym_db.RegisterMessage(GetConfigurationRequest)
GetConfigurationResponse = _reflection.GeneratedProtocolMessageType('GetConfigurationResponse', (_message.Message,), {'DESCRIPTOR': _GETCONFIGURATIONRESPONSE, '__module__': 'relay.notification.v1.notification_configuration_service_pb2'})
_sym_db.RegisterMessage(GetConfigurationResponse)
DeleteConfigurationRequest = _reflection.GeneratedProtocolMessageType('DeleteConfigurationRequest', (_message.Message,), {'DESCRIPTOR': _DELETECONFIGURATIONREQUEST, '__module__': 'relay.notification.v1.notification_configuration_service_pb2'})
_sym_db.RegisterMessage(DeleteConfigurationRequest)
DeleteConfigurationResponse = _reflection.GeneratedProtocolMessageType('DeleteConfigurationResponse', (_message.Message,), {'DESCRIPTOR': _DELETECONFIGURATIONRESPONSE, '__module__': 'relay.notification.v1.notification_configuration_service_pb2'})
_sym_db.RegisterMessage(DeleteConfigurationResponse)
_NOTIFICATIONCONFIGURATION = DESCRIPTOR.services_by_name['NotificationConfiguration']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z;github.com/Nedved75/grpcsimple/sdk/go/relay/notification/v1\xaa\x02\x15Relay.Notification.V1'
    _CREATEWEBHOOKCONFIGURATIONREQUEST._serialized_start = 168
    _CREATEWEBHOOKCONFIGURATIONREQUEST._serialized_end = 252
    _CREATEWEBHOOKCONFIGURATIONRESPONSE._serialized_start = 255
    _CREATEWEBHOOKCONFIGURATIONRESPONSE._serialized_end = 391
    _GETCONFIGURATIONREQUEST._serialized_start = 393
    _GETCONFIGURATIONREQUEST._serialized_end = 457
    _GETCONFIGURATIONRESPONSE._serialized_start = 459
    _GETCONFIGURATIONRESPONSE._serialized_end = 568
    _DELETECONFIGURATIONREQUEST._serialized_start = 570
    _DELETECONFIGURATIONREQUEST._serialized_end = 637
    _DELETECONFIGURATIONRESPONSE._serialized_start = 639
    _DELETECONFIGURATIONRESPONSE._serialized_end = 699
    _NOTIFICATIONCONFIGURATION._serialized_start = 702
    _NOTIFICATIONCONFIGURATION._serialized_end = 1100