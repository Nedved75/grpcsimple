"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....relay.onboarding.v1 import payment_method_onboarding_service_pb2 as relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2

class PaymentMethodOnboardingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Initialize = channel.unary_unary('/relay.onboarding.v1.PaymentMethodOnboarding/Initialize', request_serializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.InitializeRequest.SerializeToString, response_deserializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.InitializeResponse.FromString)
        self.Update = channel.unary_unary('/relay.onboarding.v1.PaymentMethodOnboarding/Update', request_serializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.UpdateRequest.SerializeToString, response_deserializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.UpdateResponse.FromString)
        self.Get = channel.unary_unary('/relay.onboarding.v1.PaymentMethodOnboarding/Get', request_serializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.GetRequest.SerializeToString, response_deserializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.GetResponse.FromString)

class PaymentMethodOnboardingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Initialize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_PaymentMethodOnboardingServicer_to_server(servicer, server):
    rpc_method_handlers = {'Initialize': grpc.unary_unary_rpc_method_handler(servicer.Initialize, request_deserializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.InitializeRequest.FromString, response_serializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.InitializeResponse.SerializeToString), 'Update': grpc.unary_unary_rpc_method_handler(servicer.Update, request_deserializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.UpdateRequest.FromString, response_serializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.UpdateResponse.SerializeToString), 'Get': grpc.unary_unary_rpc_method_handler(servicer.Get, request_deserializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.GetRequest.FromString, response_serializer=relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.GetResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('relay.onboarding.v1.PaymentMethodOnboarding', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class PaymentMethodOnboarding(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Initialize(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.onboarding.v1.PaymentMethodOnboarding/Initialize', relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.InitializeRequest.SerializeToString, relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.InitializeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.onboarding.v1.PaymentMethodOnboarding/Update', relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.UpdateRequest.SerializeToString, relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.UpdateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.onboarding.v1.PaymentMethodOnboarding/Get', relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.GetRequest.SerializeToString, relay_dot_onboarding_dot_v1_dot_payment__method__onboarding__service__pb2.GetResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)