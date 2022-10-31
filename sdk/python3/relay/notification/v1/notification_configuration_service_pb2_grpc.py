"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....relay.notification.v1 import notification_configuration_service_pb2 as relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2

class NotificationConfigurationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateWebhookConfiguration = channel.unary_unary('/relay.notification.v1.NotificationConfiguration/CreateWebhookConfiguration', request_serializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.CreateWebhookConfigurationRequest.SerializeToString, response_deserializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.CreateWebhookConfigurationResponse.FromString)
        self.Get = channel.unary_unary('/relay.notification.v1.NotificationConfiguration/Get', request_serializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.GetConfigurationRequest.SerializeToString, response_deserializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.GetConfigurationResponse.FromString)
        self.Delete = channel.unary_unary('/relay.notification.v1.NotificationConfiguration/Delete', request_serializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.DeleteConfigurationRequest.SerializeToString, response_deserializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.DeleteConfigurationResponse.FromString)

class NotificationConfigurationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateWebhookConfiguration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_NotificationConfigurationServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateWebhookConfiguration': grpc.unary_unary_rpc_method_handler(servicer.CreateWebhookConfiguration, request_deserializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.CreateWebhookConfigurationRequest.FromString, response_serializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.CreateWebhookConfigurationResponse.SerializeToString), 'Get': grpc.unary_unary_rpc_method_handler(servicer.Get, request_deserializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.GetConfigurationRequest.FromString, response_serializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.GetConfigurationResponse.SerializeToString), 'Delete': grpc.unary_unary_rpc_method_handler(servicer.Delete, request_deserializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.DeleteConfigurationRequest.FromString, response_serializer=relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.DeleteConfigurationResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('relay.notification.v1.NotificationConfiguration', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class NotificationConfiguration(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateWebhookConfiguration(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.notification.v1.NotificationConfiguration/CreateWebhookConfiguration', relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.CreateWebhookConfigurationRequest.SerializeToString, relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.CreateWebhookConfigurationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.notification.v1.NotificationConfiguration/Get', relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.GetConfigurationRequest.SerializeToString, relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.GetConfigurationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.notification.v1.NotificationConfiguration/Delete', relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.DeleteConfigurationRequest.SerializeToString, relay_dot_notification_dot_v1_dot_notification__configuration__service__pb2.DeleteConfigurationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)