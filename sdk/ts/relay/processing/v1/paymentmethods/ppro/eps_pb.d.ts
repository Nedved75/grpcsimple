/* eslint-disable */
/*Generated by GenDocu.com*/
// package: relay.processing.v1.paymentmethods.ppro.eps
// file: relay/processing/v1/paymentmethods/ppro/eps.proto

import * as jspb from "google-protobuf";

export class ChargeRequestData extends jspb.Message {
  hasPaymentFlowData(): boolean;
  clearPaymentFlowData(): void;
  getPaymentFlowData(): PaymentFlowRedirectRequestData | undefined;
  setPaymentFlowData(value?: PaymentFlowRedirectRequestData): void;

  hasConsumer(): boolean;
  clearConsumer(): void;
  getConsumer(): Consumer | undefined;
  setConsumer(value?: Consumer): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ChargeRequestData.AsObject;
  static toObject(includeInstance: boolean, msg: ChargeRequestData): ChargeRequestData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ChargeRequestData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ChargeRequestData;
  static deserializeBinaryFromReader(message: ChargeRequestData, reader: jspb.BinaryReader): ChargeRequestData;
}

export namespace ChargeRequestData {
  export type AsObject = {
    paymentFlowData?: PaymentFlowRedirectRequestData.AsObject,
    consumer?: Consumer.AsObject,
  }
}

export class ChargeResponseData extends jspb.Message {
  hasPaymentFlowData(): boolean;
  clearPaymentFlowData(): void;
  getPaymentFlowData(): PaymentFlowRedirectResponseData | undefined;
  setPaymentFlowData(value?: PaymentFlowRedirectResponseData): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ChargeResponseData.AsObject;
  static toObject(includeInstance: boolean, msg: ChargeResponseData): ChargeResponseData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ChargeResponseData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ChargeResponseData;
  static deserializeBinaryFromReader(message: ChargeResponseData, reader: jspb.BinaryReader): ChargeResponseData;
}

export namespace ChargeResponseData {
  export type AsObject = {
    paymentFlowData?: PaymentFlowRedirectResponseData.AsObject,
  }
}

export class Consumer extends jspb.Message {
  getName(): string;
  setName(value: string): void;

  getCountryCode(): string;
  setCountryCode(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Consumer.AsObject;
  static toObject(includeInstance: boolean, msg: Consumer): Consumer.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Consumer, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Consumer;
  static deserializeBinaryFromReader(message: Consumer, reader: jspb.BinaryReader): Consumer;
}

export namespace Consumer {
  export type AsObject = {
    name: string,
    countryCode: string,
  }
}

export class PaymentFlowRedirectRequestData extends jspb.Message {
  getSuccessUrl(): string;
  setSuccessUrl(value: string): void;

  getFailedUrl(): string;
  setFailedUrl(value: string): void;

  getCancelUrl(): string;
  setCancelUrl(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PaymentFlowRedirectRequestData.AsObject;
  static toObject(includeInstance: boolean, msg: PaymentFlowRedirectRequestData): PaymentFlowRedirectRequestData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: PaymentFlowRedirectRequestData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PaymentFlowRedirectRequestData;
  static deserializeBinaryFromReader(message: PaymentFlowRedirectRequestData, reader: jspb.BinaryReader): PaymentFlowRedirectRequestData;
}

export namespace PaymentFlowRedirectRequestData {
  export type AsObject = {
    successUrl: string,
    failedUrl: string,
    cancelUrl: string,
  }
}

export class PaymentFlowRedirectResponseData extends jspb.Message {
  getApprovalUrl(): string;
  setApprovalUrl(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PaymentFlowRedirectResponseData.AsObject;
  static toObject(includeInstance: boolean, msg: PaymentFlowRedirectResponseData): PaymentFlowRedirectResponseData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: PaymentFlowRedirectResponseData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PaymentFlowRedirectResponseData;
  static deserializeBinaryFromReader(message: PaymentFlowRedirectResponseData, reader: jspb.BinaryReader): PaymentFlowRedirectResponseData;
}

export namespace PaymentFlowRedirectResponseData {
  export type AsObject = {
    approvalUrl: string,
  }
}

