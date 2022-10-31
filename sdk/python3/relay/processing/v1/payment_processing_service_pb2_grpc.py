"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....relay.processing.v1 import payment_processing_service_pb2 as relay_dot_processing_dot_v1_dot_payment__processing__service__pb2

class PaymentProcessingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Authorize = channel.unary_unary('/relay.processing.v1.PaymentProcessing/Authorize', request_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.AuthorizeRequest.SerializeToString, response_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.AuthorizeResponse.FromString)
        self.Cancel = channel.unary_unary('/relay.processing.v1.PaymentProcessing/Cancel', request_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CancelRequest.SerializeToString, response_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CancelResponse.FromString)
        self.Capture = channel.unary_unary('/relay.processing.v1.PaymentProcessing/Capture', request_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CaptureRequest.SerializeToString, response_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CaptureResponse.FromString)
        self.Charge = channel.unary_unary('/relay.processing.v1.PaymentProcessing/Charge', request_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.ChargeRequest.SerializeToString, response_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.ChargeResponse.FromString)
        self.Refund = channel.unary_unary('/relay.processing.v1.PaymentProcessing/Refund', request_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.RefundRequest.SerializeToString, response_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.RefundResponse.FromString)
        self.GetSummary = channel.unary_unary('/relay.processing.v1.PaymentProcessing/GetSummary', request_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetSummaryRequest.SerializeToString, response_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetSummaryResponse.FromString)
        self.GetOperationsSummary = channel.unary_unary('/relay.processing.v1.PaymentProcessing/GetOperationsSummary', request_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetOperationsSummaryRequest.SerializeToString, response_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetOperationsSummaryResponse.FromString)

class PaymentProcessingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Authorize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Cancel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Capture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Charge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Refund(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSummary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOperationsSummary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_PaymentProcessingServicer_to_server(servicer, server):
    rpc_method_handlers = {'Authorize': grpc.unary_unary_rpc_method_handler(servicer.Authorize, request_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.AuthorizeRequest.FromString, response_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.AuthorizeResponse.SerializeToString), 'Cancel': grpc.unary_unary_rpc_method_handler(servicer.Cancel, request_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CancelRequest.FromString, response_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CancelResponse.SerializeToString), 'Capture': grpc.unary_unary_rpc_method_handler(servicer.Capture, request_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CaptureRequest.FromString, response_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CaptureResponse.SerializeToString), 'Charge': grpc.unary_unary_rpc_method_handler(servicer.Charge, request_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.ChargeRequest.FromString, response_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.ChargeResponse.SerializeToString), 'Refund': grpc.unary_unary_rpc_method_handler(servicer.Refund, request_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.RefundRequest.FromString, response_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.RefundResponse.SerializeToString), 'GetSummary': grpc.unary_unary_rpc_method_handler(servicer.GetSummary, request_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetSummaryRequest.FromString, response_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetSummaryResponse.SerializeToString), 'GetOperationsSummary': grpc.unary_unary_rpc_method_handler(servicer.GetOperationsSummary, request_deserializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetOperationsSummaryRequest.FromString, response_serializer=relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetOperationsSummaryResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('relay.processing.v1.PaymentProcessing', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class PaymentProcessing(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Authorize(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.processing.v1.PaymentProcessing/Authorize', relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.AuthorizeRequest.SerializeToString, relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.AuthorizeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Cancel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.processing.v1.PaymentProcessing/Cancel', relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CancelRequest.SerializeToString, relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CancelResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Capture(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.processing.v1.PaymentProcessing/Capture', relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CaptureRequest.SerializeToString, relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.CaptureResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Charge(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.processing.v1.PaymentProcessing/Charge', relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.ChargeRequest.SerializeToString, relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.ChargeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Refund(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.processing.v1.PaymentProcessing/Refund', relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.RefundRequest.SerializeToString, relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.RefundResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSummary(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.processing.v1.PaymentProcessing/GetSummary', relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetSummaryRequest.SerializeToString, relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetSummaryResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOperationsSummary(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/relay.processing.v1.PaymentProcessing/GetOperationsSummary', relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetOperationsSummaryRequest.SerializeToString, relay_dot_processing_dot_v1_dot_payment__processing__service__pb2.GetOperationsSummaryResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)