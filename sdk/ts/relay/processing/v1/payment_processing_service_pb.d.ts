/* eslint-disable */
/*Generated by GenDocu.com*/
// package: relay.processing.v1
// file: relay/processing/v1/payment_processing_service.proto

import * as jspb from "google-protobuf";
import * as google_protobuf_any_pb from "google-protobuf/google/protobuf/any_pb";
import * as relay_models_pb from "../../../relay/models_pb";
import * as relay_processing_v1_models_pb from "../../../relay/processing/v1/models_pb";

export class ChargeRequest extends jspb.Message {
  getPaymentMethodConfigurationId(): string;
  setPaymentMethodConfigurationId(value: string): void;

  getRequestId(): string;
  setRequestId(value: string): void;

  getReference(): string;
  setReference(value: string): void;

  getPaymentMethod(): relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap];
  setPaymentMethod(value: relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap]): void;

  hasOrder(): boolean;
  clearOrder(): void;
  getOrder(): relay_processing_v1_models_pb.Order | undefined;
  setOrder(value?: relay_processing_v1_models_pb.Order): void;

  hasData(): boolean;
  clearData(): void;
  getData(): google_protobuf_any_pb.Any | undefined;
  setData(value?: google_protobuf_any_pb.Any): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ChargeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ChargeRequest): ChargeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ChargeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ChargeRequest;
  static deserializeBinaryFromReader(message: ChargeRequest, reader: jspb.BinaryReader): ChargeRequest;
}

export namespace ChargeRequest {
  export type AsObject = {
    paymentMethodConfigurationId: string,
    requestId: string,
    reference: string,
    paymentMethod: relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap],
    order?: relay_processing_v1_models_pb.Order.AsObject,
    data?: google_protobuf_any_pb.Any.AsObject,
  }
}

export class ChargeResponse extends jspb.Message {
  getPaymentId(): string;
  setPaymentId(value: string): void;

  getChargeId(): string;
  setChargeId(value: string): void;

  hasData(): boolean;
  clearData(): void;
  getData(): google_protobuf_any_pb.Any | undefined;
  setData(value?: google_protobuf_any_pb.Any): void;

  hasStatus(): boolean;
  clearStatus(): void;
  getStatus(): relay_models_pb.Status | undefined;
  setStatus(value?: relay_models_pb.Status): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ChargeResponse.AsObject;
  static toObject(includeInstance: boolean, msg: ChargeResponse): ChargeResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ChargeResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ChargeResponse;
  static deserializeBinaryFromReader(message: ChargeResponse, reader: jspb.BinaryReader): ChargeResponse;
}

export namespace ChargeResponse {
  export type AsObject = {
    paymentId: string,
    chargeId: string,
    data?: google_protobuf_any_pb.Any.AsObject,
    status?: relay_models_pb.Status.AsObject,
  }
}

export class RefundRequest extends jspb.Message {
  getPaymentId(): string;
  setPaymentId(value: string): void;

  getRequestId(): string;
  setRequestId(value: string): void;

  getReference(): string;
  setReference(value: string): void;

  getAmount(): number;
  setAmount(value: number): void;

  hasData(): boolean;
  clearData(): void;
  getData(): google_protobuf_any_pb.Any | undefined;
  setData(value?: google_protobuf_any_pb.Any): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RefundRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RefundRequest): RefundRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RefundRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RefundRequest;
  static deserializeBinaryFromReader(message: RefundRequest, reader: jspb.BinaryReader): RefundRequest;
}

export namespace RefundRequest {
  export type AsObject = {
    paymentId: string,
    requestId: string,
    reference: string,
    amount: number,
    data?: google_protobuf_any_pb.Any.AsObject,
  }
}

export class RefundResponse extends jspb.Message {
  getRefundId(): string;
  setRefundId(value: string): void;

  hasData(): boolean;
  clearData(): void;
  getData(): google_protobuf_any_pb.Any | undefined;
  setData(value?: google_protobuf_any_pb.Any): void;

  hasStatus(): boolean;
  clearStatus(): void;
  getStatus(): relay_models_pb.Status | undefined;
  setStatus(value?: relay_models_pb.Status): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RefundResponse.AsObject;
  static toObject(includeInstance: boolean, msg: RefundResponse): RefundResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RefundResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RefundResponse;
  static deserializeBinaryFromReader(message: RefundResponse, reader: jspb.BinaryReader): RefundResponse;
}

export namespace RefundResponse {
  export type AsObject = {
    refundId: string,
    data?: google_protobuf_any_pb.Any.AsObject,
    status?: relay_models_pb.Status.AsObject,
  }
}

export class GetSummaryRequest extends jspb.Message {
  getPaymentId(): string;
  setPaymentId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSummaryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSummaryRequest): GetSummaryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSummaryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSummaryRequest;
  static deserializeBinaryFromReader(message: GetSummaryRequest, reader: jspb.BinaryReader): GetSummaryRequest;
}

export namespace GetSummaryRequest {
  export type AsObject = {
    paymentId: string,
  }
}

export class GetSummaryResponse extends jspb.Message {
  getAuthorizedAmount(): number;
  setAuthorizedAmount(value: number): void;

  getChargedAmount(): number;
  setChargedAmount(value: number): void;

  getCanceledAmount(): number;
  setCanceledAmount(value: number): void;

  getRefundedAmount(): number;
  setRefundedAmount(value: number): void;

  getCurrency(): string;
  setCurrency(value: string): void;

  hasStatus(): boolean;
  clearStatus(): void;
  getStatus(): relay_models_pb.Status | undefined;
  setStatus(value?: relay_models_pb.Status): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSummaryResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetSummaryResponse): GetSummaryResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSummaryResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSummaryResponse;
  static deserializeBinaryFromReader(message: GetSummaryResponse, reader: jspb.BinaryReader): GetSummaryResponse;
}

export namespace GetSummaryResponse {
  export type AsObject = {
    authorizedAmount: number,
    chargedAmount: number,
    canceledAmount: number,
    refundedAmount: number,
    currency: string,
    status?: relay_models_pb.Status.AsObject,
  }
}

export class GetOperationsSummaryRequest extends jspb.Message {
  getPaymentId(): string;
  setPaymentId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetOperationsSummaryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetOperationsSummaryRequest): GetOperationsSummaryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetOperationsSummaryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetOperationsSummaryRequest;
  static deserializeBinaryFromReader(message: GetOperationsSummaryRequest, reader: jspb.BinaryReader): GetOperationsSummaryRequest;
}

export namespace GetOperationsSummaryRequest {
  export type AsObject = {
    paymentId: string,
  }
}

export class GetOperationsSummaryResponse extends jspb.Message {
  clearOperationsList(): void;
  getOperationsList(): Array<relay_processing_v1_models_pb.OperationSummary>;
  setOperationsList(value: Array<relay_processing_v1_models_pb.OperationSummary>): void;
  addOperations(value?: relay_processing_v1_models_pb.OperationSummary, index?: number): relay_processing_v1_models_pb.OperationSummary;

  hasStatus(): boolean;
  clearStatus(): void;
  getStatus(): relay_models_pb.Status | undefined;
  setStatus(value?: relay_models_pb.Status): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetOperationsSummaryResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetOperationsSummaryResponse): GetOperationsSummaryResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetOperationsSummaryResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetOperationsSummaryResponse;
  static deserializeBinaryFromReader(message: GetOperationsSummaryResponse, reader: jspb.BinaryReader): GetOperationsSummaryResponse;
}

export namespace GetOperationsSummaryResponse {
  export type AsObject = {
    operationsList: Array<relay_processing_v1_models_pb.OperationSummary.AsObject>,
    status?: relay_models_pb.Status.AsObject,
  }
}
