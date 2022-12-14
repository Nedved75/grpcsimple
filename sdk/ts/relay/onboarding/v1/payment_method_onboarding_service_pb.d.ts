/* eslint-disable */
/*Generated by GenDocu.com*/
// package: relay.onboarding.v1
// file: relay/onboarding/v1/payment_method_onboarding_service.proto

import * as jspb from "google-protobuf";
import * as google_protobuf_any_pb from "google-protobuf/google/protobuf/any_pb";
import * as google_protobuf_wrappers_pb from "google-protobuf/google/protobuf/wrappers_pb";
import * as relay_models_pb from "../../../relay/models_pb";
import * as relay_onboarding_v1_paymentmethods_expressbank_pb from "../../../relay/onboarding/v1/paymentmethods/expressbank_pb";
import * as relay_onboarding_v1_paymentmethods_klarna_pb from "../../../relay/onboarding/v1/paymentmethods/klarna_pb";
import * as relay_onboarding_v1_paymentmethods_ppro_pb from "../../../relay/onboarding/v1/paymentmethods/ppro_pb";

export class InitializeRequest extends jspb.Message {
  getReference(): string;
  setReference(value: string): void;

  getPaymentMethod(): relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap];
  setPaymentMethod(value: relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap]): void;

  hasInitializerequestppro(): boolean;
  clearInitializerequestppro(): void;
  getInitializerequestppro(): relay_onboarding_v1_paymentmethods_ppro_pb.InitializeRequestData | undefined;
  setInitializerequestppro(value?: relay_onboarding_v1_paymentmethods_ppro_pb.InitializeRequestData): void;

  hasInitializerequestexpressbank(): boolean;
  clearInitializerequestexpressbank(): void;
  getInitializerequestexpressbank(): relay_onboarding_v1_paymentmethods_expressbank_pb.InitializeRequestData | undefined;
  setInitializerequestexpressbank(value?: relay_onboarding_v1_paymentmethods_expressbank_pb.InitializeRequestData): void;

  hasInitializerequestklarna(): boolean;
  clearInitializerequestklarna(): void;
  getInitializerequestklarna(): relay_onboarding_v1_paymentmethods_klarna_pb.InitializeRequestData | undefined;
  setInitializerequestklarna(value?: relay_onboarding_v1_paymentmethods_klarna_pb.InitializeRequestData): void;

  getDataCase(): InitializeRequest.DataCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InitializeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: InitializeRequest): InitializeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InitializeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InitializeRequest;
  static deserializeBinaryFromReader(message: InitializeRequest, reader: jspb.BinaryReader): InitializeRequest;
}

export namespace InitializeRequest {
  export type AsObject = {
    reference: string,
    paymentMethod: relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap],
    initializerequestppro?: relay_onboarding_v1_paymentmethods_ppro_pb.InitializeRequestData.AsObject,
    initializerequestexpressbank?: relay_onboarding_v1_paymentmethods_expressbank_pb.InitializeRequestData.AsObject,
    initializerequestklarna?: relay_onboarding_v1_paymentmethods_klarna_pb.InitializeRequestData.AsObject,
  }

  export enum DataCase {
    DATA_NOT_SET = 0,
    INITIALIZEREQUESTPPRO = 3,
    INITIALIZEREQUESTEXPRESSBANK = 4,
    INITIALIZEREQUESTKLARNA = 5,
  }
}

export class InitializeResponse extends jspb.Message {
  hasPaymentMethodConfigurationId(): boolean;
  clearPaymentMethodConfigurationId(): void;
  getPaymentMethodConfigurationId(): google_protobuf_wrappers_pb.StringValue | undefined;
  setPaymentMethodConfigurationId(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasData(): boolean;
  clearData(): void;
  getData(): google_protobuf_any_pb.Any | undefined;
  setData(value?: google_protobuf_any_pb.Any): void;

  hasStatus(): boolean;
  clearStatus(): void;
  getStatus(): relay_models_pb.Status | undefined;
  setStatus(value?: relay_models_pb.Status): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InitializeResponse.AsObject;
  static toObject(includeInstance: boolean, msg: InitializeResponse): InitializeResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InitializeResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InitializeResponse;
  static deserializeBinaryFromReader(message: InitializeResponse, reader: jspb.BinaryReader): InitializeResponse;
}

export namespace InitializeResponse {
  export type AsObject = {
    paymentMethodConfigurationId?: google_protobuf_wrappers_pb.StringValue.AsObject,
    data?: google_protobuf_any_pb.Any.AsObject,
    status?: relay_models_pb.Status.AsObject,
  }
}

export class UpdateRequest extends jspb.Message {
  getPaymentMethodConfigurationId(): string;
  setPaymentMethodConfigurationId(value: string): void;

  getPaymentMethod(): relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap];
  setPaymentMethod(value: relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap]): void;

  hasUpdaterequestppro(): boolean;
  clearUpdaterequestppro(): void;
  getUpdaterequestppro(): relay_onboarding_v1_paymentmethods_ppro_pb.UpdateRequestData | undefined;
  setUpdaterequestppro(value?: relay_onboarding_v1_paymentmethods_ppro_pb.UpdateRequestData): void;

  hasUpdaterequestexpressbank(): boolean;
  clearUpdaterequestexpressbank(): void;
  getUpdaterequestexpressbank(): relay_onboarding_v1_paymentmethods_expressbank_pb.UpdateRequestData | undefined;
  setUpdaterequestexpressbank(value?: relay_onboarding_v1_paymentmethods_expressbank_pb.UpdateRequestData): void;

  hasUpdaterequestklarna(): boolean;
  clearUpdaterequestklarna(): void;
  getUpdaterequestklarna(): relay_onboarding_v1_paymentmethods_klarna_pb.UpdateRequestData | undefined;
  setUpdaterequestklarna(value?: relay_onboarding_v1_paymentmethods_klarna_pb.UpdateRequestData): void;

  getDataCase(): UpdateRequest.DataCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateRequest): UpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateRequest;
  static deserializeBinaryFromReader(message: UpdateRequest, reader: jspb.BinaryReader): UpdateRequest;
}

export namespace UpdateRequest {
  export type AsObject = {
    paymentMethodConfigurationId: string,
    paymentMethod: relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap],
    updaterequestppro?: relay_onboarding_v1_paymentmethods_ppro_pb.UpdateRequestData.AsObject,
    updaterequestexpressbank?: relay_onboarding_v1_paymentmethods_expressbank_pb.UpdateRequestData.AsObject,
    updaterequestklarna?: relay_onboarding_v1_paymentmethods_klarna_pb.UpdateRequestData.AsObject,
  }

  export enum DataCase {
    DATA_NOT_SET = 0,
    UPDATEREQUESTPPRO = 3,
    UPDATEREQUESTEXPRESSBANK = 4,
    UPDATEREQUESTKLARNA = 5,
  }
}

export class UpdateResponse extends jspb.Message {
  hasData(): boolean;
  clearData(): void;
  getData(): google_protobuf_any_pb.Any | undefined;
  setData(value?: google_protobuf_any_pb.Any): void;

  hasStatus(): boolean;
  clearStatus(): void;
  getStatus(): relay_models_pb.Status | undefined;
  setStatus(value?: relay_models_pb.Status): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateResponse.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateResponse): UpdateResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateResponse;
  static deserializeBinaryFromReader(message: UpdateResponse, reader: jspb.BinaryReader): UpdateResponse;
}

export namespace UpdateResponse {
  export type AsObject = {
    data?: google_protobuf_any_pb.Any.AsObject,
    status?: relay_models_pb.Status.AsObject,
  }
}

export class GetRequest extends jspb.Message {
  getPaymentMethodConfigurationId(): string;
  setPaymentMethodConfigurationId(value: string): void;

  getPaymentMethod(): relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap];
  setPaymentMethod(value: relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap]): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRequest): GetRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRequest;
  static deserializeBinaryFromReader(message: GetRequest, reader: jspb.BinaryReader): GetRequest;
}

export namespace GetRequest {
  export type AsObject = {
    paymentMethodConfigurationId: string,
    paymentMethod: relay_models_pb.PaymentMethodMap[keyof relay_models_pb.PaymentMethodMap],
  }
}

export class GetResponse extends jspb.Message {
  getPaymentMethodOnboardingStatus(): PaymentMethodOnboardingStatusMap[keyof PaymentMethodOnboardingStatusMap];
  setPaymentMethodOnboardingStatus(value: PaymentMethodOnboardingStatusMap[keyof PaymentMethodOnboardingStatusMap]): void;

  hasData(): boolean;
  clearData(): void;
  getData(): google_protobuf_any_pb.Any | undefined;
  setData(value?: google_protobuf_any_pb.Any): void;

  hasStatus(): boolean;
  clearStatus(): void;
  getStatus(): relay_models_pb.Status | undefined;
  setStatus(value?: relay_models_pb.Status): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetResponse): GetResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetResponse;
  static deserializeBinaryFromReader(message: GetResponse, reader: jspb.BinaryReader): GetResponse;
}

export namespace GetResponse {
  export type AsObject = {
    paymentMethodOnboardingStatus: PaymentMethodOnboardingStatusMap[keyof PaymentMethodOnboardingStatusMap],
    data?: google_protobuf_any_pb.Any.AsObject,
    status?: relay_models_pb.Status.AsObject,
  }
}

export interface PaymentMethodOnboardingStatusMap {
  PENDING: 0;
  ACTIVATED: 1;
  NON_COMPLIANT: 2;
  DEACTIVATED: 3;
  TERMINATED: 4;
}

export const PaymentMethodOnboardingStatus: PaymentMethodOnboardingStatusMap;

