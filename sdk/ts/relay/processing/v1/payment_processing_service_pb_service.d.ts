/* eslint-disable */
/*Generated by GenDocu.com*/
// package: relay.processing.v1
// file: relay/processing/v1/payment_processing_service.proto

import * as relay_processing_v1_payment_processing_service_pb from "../../../relay/processing/v1/payment_processing_service_pb";
import {grpc} from "@improbable-eng/grpc-web";

type PaymentProcessingCharge = {
  readonly methodName: string;
  readonly service: typeof PaymentProcessing;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof relay_processing_v1_payment_processing_service_pb.ChargeRequest;
  readonly responseType: typeof relay_processing_v1_payment_processing_service_pb.ChargeResponse;
};

type PaymentProcessingRefund = {
  readonly methodName: string;
  readonly service: typeof PaymentProcessing;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof relay_processing_v1_payment_processing_service_pb.RefundRequest;
  readonly responseType: typeof relay_processing_v1_payment_processing_service_pb.RefundResponse;
};

type PaymentProcessingGetSummary = {
  readonly methodName: string;
  readonly service: typeof PaymentProcessing;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof relay_processing_v1_payment_processing_service_pb.GetSummaryRequest;
  readonly responseType: typeof relay_processing_v1_payment_processing_service_pb.GetSummaryResponse;
};

type PaymentProcessingGetOperationsSummary = {
  readonly methodName: string;
  readonly service: typeof PaymentProcessing;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof relay_processing_v1_payment_processing_service_pb.GetOperationsSummaryRequest;
  readonly responseType: typeof relay_processing_v1_payment_processing_service_pb.GetOperationsSummaryResponse;
};

export class PaymentProcessing {
  static readonly serviceName: string;
  static readonly Charge: PaymentProcessingCharge;
  static readonly Refund: PaymentProcessingRefund;
  static readonly GetSummary: PaymentProcessingGetSummary;
  static readonly GetOperationsSummary: PaymentProcessingGetOperationsSummary;
}

export type ServiceError = { message: string, code: number; metadata: grpc.Metadata }
export type Status = { details: string, code: number; metadata: grpc.Metadata }

interface UnaryResponse {
  cancel(): void;
}
interface ResponseStream<T> {
  cancel(): void;
  on(type: 'data', handler: (message: T) => void): ResponseStream<T>;
  on(type: 'end', handler: (status?: Status) => void): ResponseStream<T>;
  on(type: 'status', handler: (status: Status) => void): ResponseStream<T>;
}
interface RequestStream<T> {
  write(message: T): RequestStream<T>;
  end(): void;
  cancel(): void;
  on(type: 'end', handler: (status?: Status) => void): RequestStream<T>;
  on(type: 'status', handler: (status: Status) => void): RequestStream<T>;
}
interface BidirectionalStream<ReqT, ResT> {
  write(message: ReqT): BidirectionalStream<ReqT, ResT>;
  end(): void;
  cancel(): void;
  on(type: 'data', handler: (message: ResT) => void): BidirectionalStream<ReqT, ResT>;
  on(type: 'end', handler: (status?: Status) => void): BidirectionalStream<ReqT, ResT>;
  on(type: 'status', handler: (status: Status) => void): BidirectionalStream<ReqT, ResT>;
}

export class PaymentProcessingClient {
  readonly serviceHost: string;

  constructor(serviceHost: string, options?: grpc.RpcOptions);
  charge(
    requestMessage: relay_processing_v1_payment_processing_service_pb.ChargeRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: relay_processing_v1_payment_processing_service_pb.ChargeResponse|null) => void
  ): UnaryResponse;
  charge(
    requestMessage: relay_processing_v1_payment_processing_service_pb.ChargeRequest,
    callback: (error: ServiceError|null, responseMessage: relay_processing_v1_payment_processing_service_pb.ChargeResponse|null) => void
  ): UnaryResponse;
  refund(
    requestMessage: relay_processing_v1_payment_processing_service_pb.RefundRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: relay_processing_v1_payment_processing_service_pb.RefundResponse|null) => void
  ): UnaryResponse;
  refund(
    requestMessage: relay_processing_v1_payment_processing_service_pb.RefundRequest,
    callback: (error: ServiceError|null, responseMessage: relay_processing_v1_payment_processing_service_pb.RefundResponse|null) => void
  ): UnaryResponse;
  getSummary(
    requestMessage: relay_processing_v1_payment_processing_service_pb.GetSummaryRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: relay_processing_v1_payment_processing_service_pb.GetSummaryResponse|null) => void
  ): UnaryResponse;
  getSummary(
    requestMessage: relay_processing_v1_payment_processing_service_pb.GetSummaryRequest,
    callback: (error: ServiceError|null, responseMessage: relay_processing_v1_payment_processing_service_pb.GetSummaryResponse|null) => void
  ): UnaryResponse;
  getOperationsSummary(
    requestMessage: relay_processing_v1_payment_processing_service_pb.GetOperationsSummaryRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: relay_processing_v1_payment_processing_service_pb.GetOperationsSummaryResponse|null) => void
  ): UnaryResponse;
  getOperationsSummary(
    requestMessage: relay_processing_v1_payment_processing_service_pb.GetOperationsSummaryRequest,
    callback: (error: ServiceError|null, responseMessage: relay_processing_v1_payment_processing_service_pb.GetOperationsSummaryResponse|null) => void
  ): UnaryResponse;
}

