/* eslint-disable */
/*Generated by GenDocu.com*/
// package: relay.processing.v1.paymentmethods.klarna
// file: relay/processing/v1/paymentmethods/klarna.proto

import * as jspb from "google-protobuf";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
import * as google_protobuf_wrappers_pb from "google-protobuf/google/protobuf/wrappers_pb";

export class AuthorizeRequestData extends jspb.Message {
  hasCustomer(): boolean;
  clearCustomer(): void;
  getCustomer(): Customer | undefined;
  setCustomer(value?: Customer): void;

  hasBillingAddress(): boolean;
  clearBillingAddress(): void;
  getBillingAddress(): Address | undefined;
  setBillingAddress(value?: Address): void;

  hasOrderDetails(): boolean;
  clearOrderDetails(): void;
  getOrderDetails(): OrderDetails | undefined;
  setOrderDetails(value?: OrderDetails): void;

  getAcquiringChannel(): AcquiringChannelMap[keyof AcquiringChannelMap];
  setAcquiringChannel(value: AcquiringChannelMap[keyof AcquiringChannelMap]): void;

  getLocale(): string;
  setLocale(value: string): void;

  hasPaymentFlowData(): boolean;
  clearPaymentFlowData(): void;
  getPaymentFlowData(): PaymentFlowRedirectRequestData | undefined;
  setPaymentFlowData(value?: PaymentFlowRedirectRequestData): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AuthorizeRequestData.AsObject;
  static toObject(includeInstance: boolean, msg: AuthorizeRequestData): AuthorizeRequestData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AuthorizeRequestData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AuthorizeRequestData;
  static deserializeBinaryFromReader(message: AuthorizeRequestData, reader: jspb.BinaryReader): AuthorizeRequestData;
}

export namespace AuthorizeRequestData {
  export type AsObject = {
    customer?: Customer.AsObject,
    billingAddress?: Address.AsObject,
    orderDetails?: OrderDetails.AsObject,
    acquiringChannel: AcquiringChannelMap[keyof AcquiringChannelMap],
    locale: string,
    paymentFlowData?: PaymentFlowRedirectRequestData.AsObject,
  }
}

export class AuthorizeResponseData extends jspb.Message {
  hasPaymentFlowData(): boolean;
  clearPaymentFlowData(): void;
  getPaymentFlowData(): PaymentFlowRedirectResponseData | undefined;
  setPaymentFlowData(value?: PaymentFlowRedirectResponseData): void;

  hasExpiresAt(): boolean;
  clearExpiresAt(): void;
  getExpiresAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setExpiresAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AuthorizeResponseData.AsObject;
  static toObject(includeInstance: boolean, msg: AuthorizeResponseData): AuthorizeResponseData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AuthorizeResponseData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AuthorizeResponseData;
  static deserializeBinaryFromReader(message: AuthorizeResponseData, reader: jspb.BinaryReader): AuthorizeResponseData;
}

export namespace AuthorizeResponseData {
  export type AsObject = {
    paymentFlowData?: PaymentFlowRedirectResponseData.AsObject,
    expiresAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class ChargeRequestData extends jspb.Message {
  hasCustomer(): boolean;
  clearCustomer(): void;
  getCustomer(): Customer | undefined;
  setCustomer(value?: Customer): void;

  hasBillingAddress(): boolean;
  clearBillingAddress(): void;
  getBillingAddress(): Address | undefined;
  setBillingAddress(value?: Address): void;

  hasOrderDetails(): boolean;
  clearOrderDetails(): void;
  getOrderDetails(): OrderDetails | undefined;
  setOrderDetails(value?: OrderDetails): void;

  getAcquiringChannel(): AcquiringChannelMap[keyof AcquiringChannelMap];
  setAcquiringChannel(value: AcquiringChannelMap[keyof AcquiringChannelMap]): void;

  getLocale(): string;
  setLocale(value: string): void;

  hasPaymentFlowData(): boolean;
  clearPaymentFlowData(): void;
  getPaymentFlowData(): PaymentFlowRedirectRequestData | undefined;
  setPaymentFlowData(value?: PaymentFlowRedirectRequestData): void;

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
    customer?: Customer.AsObject,
    billingAddress?: Address.AsObject,
    orderDetails?: OrderDetails.AsObject,
    acquiringChannel: AcquiringChannelMap[keyof AcquiringChannelMap],
    locale: string,
    paymentFlowData?: PaymentFlowRedirectRequestData.AsObject,
  }
}

export class ChargeResponseData extends jspb.Message {
  hasPaymentFlowData(): boolean;
  clearPaymentFlowData(): void;
  getPaymentFlowData(): PaymentFlowRedirectResponseData | undefined;
  setPaymentFlowData(value?: PaymentFlowRedirectResponseData): void;

  hasExpiresAt(): boolean;
  clearExpiresAt(): void;
  getExpiresAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setExpiresAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

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
    expiresAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class CaptureRequestData extends jspb.Message {
  clearOrderItemsList(): void;
  getOrderItemsList(): Array<OrderItem>;
  setOrderItemsList(value: Array<OrderItem>): void;
  addOrderItems(value?: OrderItem, index?: number): OrderItem;

  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): google_protobuf_wrappers_pb.StringValue | undefined;
  setDescription(value?: google_protobuf_wrappers_pb.StringValue): void;

  clearShippingInfoList(): void;
  getShippingInfoList(): Array<ShippingInfo>;
  setShippingInfoList(value: Array<ShippingInfo>): void;
  addShippingInfo(value?: ShippingInfo, index?: number): ShippingInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CaptureRequestData.AsObject;
  static toObject(includeInstance: boolean, msg: CaptureRequestData): CaptureRequestData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CaptureRequestData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CaptureRequestData;
  static deserializeBinaryFromReader(message: CaptureRequestData, reader: jspb.BinaryReader): CaptureRequestData;
}

export namespace CaptureRequestData {
  export type AsObject = {
    orderItemsList: Array<OrderItem.AsObject>,
    description?: google_protobuf_wrappers_pb.StringValue.AsObject,
    shippingInfoList: Array<ShippingInfo.AsObject>,
  }
}

export class ShippingInfo extends jspb.Message {
  hasReturnShippingCompany(): boolean;
  clearReturnShippingCompany(): void;
  getReturnShippingCompany(): google_protobuf_wrappers_pb.StringValue | undefined;
  setReturnShippingCompany(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasReturnTrackingNumber(): boolean;
  clearReturnTrackingNumber(): void;
  getReturnTrackingNumber(): google_protobuf_wrappers_pb.StringValue | undefined;
  setReturnTrackingNumber(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasReturnTrackingUri(): boolean;
  clearReturnTrackingUri(): void;
  getReturnTrackingUri(): google_protobuf_wrappers_pb.StringValue | undefined;
  setReturnTrackingUri(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasShippingCompany(): boolean;
  clearShippingCompany(): void;
  getShippingCompany(): google_protobuf_wrappers_pb.StringValue | undefined;
  setShippingCompany(value?: google_protobuf_wrappers_pb.StringValue): void;

  getShippingMethod(): ShippingMethodMap[keyof ShippingMethodMap];
  setShippingMethod(value: ShippingMethodMap[keyof ShippingMethodMap]): void;

  hasTrackingNumber(): boolean;
  clearTrackingNumber(): void;
  getTrackingNumber(): google_protobuf_wrappers_pb.StringValue | undefined;
  setTrackingNumber(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasTrackingUri(): boolean;
  clearTrackingUri(): void;
  getTrackingUri(): google_protobuf_wrappers_pb.StringValue | undefined;
  setTrackingUri(value?: google_protobuf_wrappers_pb.StringValue): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ShippingInfo.AsObject;
  static toObject(includeInstance: boolean, msg: ShippingInfo): ShippingInfo.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ShippingInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ShippingInfo;
  static deserializeBinaryFromReader(message: ShippingInfo, reader: jspb.BinaryReader): ShippingInfo;
}

export namespace ShippingInfo {
  export type AsObject = {
    returnShippingCompany?: google_protobuf_wrappers_pb.StringValue.AsObject,
    returnTrackingNumber?: google_protobuf_wrappers_pb.StringValue.AsObject,
    returnTrackingUri?: google_protobuf_wrappers_pb.StringValue.AsObject,
    shippingCompany?: google_protobuf_wrappers_pb.StringValue.AsObject,
    shippingMethod: ShippingMethodMap[keyof ShippingMethodMap],
    trackingNumber?: google_protobuf_wrappers_pb.StringValue.AsObject,
    trackingUri?: google_protobuf_wrappers_pb.StringValue.AsObject,
  }
}

export class RefundRequestData extends jspb.Message {
  clearOrderItemsList(): void;
  getOrderItemsList(): Array<OrderItem>;
  setOrderItemsList(value: Array<OrderItem>): void;
  addOrderItems(value?: OrderItem, index?: number): OrderItem;

  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): google_protobuf_wrappers_pb.StringValue | undefined;
  setDescription(value?: google_protobuf_wrappers_pb.StringValue): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RefundRequestData.AsObject;
  static toObject(includeInstance: boolean, msg: RefundRequestData): RefundRequestData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RefundRequestData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RefundRequestData;
  static deserializeBinaryFromReader(message: RefundRequestData, reader: jspb.BinaryReader): RefundRequestData;
}

export namespace RefundRequestData {
  export type AsObject = {
    orderItemsList: Array<OrderItem.AsObject>,
    description?: google_protobuf_wrappers_pb.StringValue.AsObject,
  }
}

export class Customer extends jspb.Message {
  hasConsumer(): boolean;
  clearConsumer(): void;
  getConsumer(): Consumer | undefined;
  setConsumer(value?: Consumer): void;

  hasBussiness(): boolean;
  clearBussiness(): void;
  getBussiness(): Bussiness | undefined;
  setBussiness(value?: Bussiness): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Customer.AsObject;
  static toObject(includeInstance: boolean, msg: Customer): Customer.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Customer, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Customer;
  static deserializeBinaryFromReader(message: Customer, reader: jspb.BinaryReader): Customer;
}

export namespace Customer {
  export type AsObject = {
    consumer?: Consumer.AsObject,
    bussiness?: Bussiness.AsObject,
  }
}

export class Consumer extends jspb.Message {
  hasDateOfBirth(): boolean;
  clearDateOfBirth(): void;
  getDateOfBirth(): google_protobuf_wrappers_pb.StringValue | undefined;
  setDateOfBirth(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasGender(): boolean;
  clearGender(): void;
  getGender(): google_protobuf_wrappers_pb.StringValue | undefined;
  setGender(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasLastFourSsn(): boolean;
  clearLastFourSsn(): void;
  getLastFourSsn(): google_protobuf_wrappers_pb.StringValue | undefined;
  setLastFourSsn(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasNationalIdentificationNumber(): boolean;
  clearNationalIdentificationNumber(): void;
  getNationalIdentificationNumber(): google_protobuf_wrappers_pb.StringValue | undefined;
  setNationalIdentificationNumber(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasTitle(): boolean;
  clearTitle(): void;
  getTitle(): google_protobuf_wrappers_pb.StringValue | undefined;
  setTitle(value?: google_protobuf_wrappers_pb.StringValue): void;

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
    dateOfBirth?: google_protobuf_wrappers_pb.StringValue.AsObject,
    gender?: google_protobuf_wrappers_pb.StringValue.AsObject,
    lastFourSsn?: google_protobuf_wrappers_pb.StringValue.AsObject,
    nationalIdentificationNumber?: google_protobuf_wrappers_pb.StringValue.AsObject,
    title?: google_protobuf_wrappers_pb.StringValue.AsObject,
  }
}

export class Bussiness extends jspb.Message {
  hasOrganizationEntityType(): boolean;
  clearOrganizationEntityType(): void;
  getOrganizationEntityType(): google_protobuf_wrappers_pb.StringValue | undefined;
  setOrganizationEntityType(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasOrganizationRegistrationId(): boolean;
  clearOrganizationRegistrationId(): void;
  getOrganizationRegistrationId(): google_protobuf_wrappers_pb.StringValue | undefined;
  setOrganizationRegistrationId(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasVatId(): boolean;
  clearVatId(): void;
  getVatId(): google_protobuf_wrappers_pb.StringValue | undefined;
  setVatId(value?: google_protobuf_wrappers_pb.StringValue): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Bussiness.AsObject;
  static toObject(includeInstance: boolean, msg: Bussiness): Bussiness.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Bussiness, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Bussiness;
  static deserializeBinaryFromReader(message: Bussiness, reader: jspb.BinaryReader): Bussiness;
}

export namespace Bussiness {
  export type AsObject = {
    organizationEntityType?: google_protobuf_wrappers_pb.StringValue.AsObject,
    organizationRegistrationId?: google_protobuf_wrappers_pb.StringValue.AsObject,
    vatId?: google_protobuf_wrappers_pb.StringValue.AsObject,
  }
}

export class Address extends jspb.Message {
  hasAttention(): boolean;
  clearAttention(): void;
  getAttention(): google_protobuf_wrappers_pb.StringValue | undefined;
  setAttention(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasCity(): boolean;
  clearCity(): void;
  getCity(): google_protobuf_wrappers_pb.StringValue | undefined;
  setCity(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasCountryCode(): boolean;
  clearCountryCode(): void;
  getCountryCode(): google_protobuf_wrappers_pb.StringValue | undefined;
  setCountryCode(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasEmailAddress(): boolean;
  clearEmailAddress(): void;
  getEmailAddress(): google_protobuf_wrappers_pb.StringValue | undefined;
  setEmailAddress(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasFamilyName(): boolean;
  clearFamilyName(): void;
  getFamilyName(): google_protobuf_wrappers_pb.StringValue | undefined;
  setFamilyName(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasGivenName(): boolean;
  clearGivenName(): void;
  getGivenName(): google_protobuf_wrappers_pb.StringValue | undefined;
  setGivenName(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasOrganizationName(): boolean;
  clearOrganizationName(): void;
  getOrganizationName(): google_protobuf_wrappers_pb.StringValue | undefined;
  setOrganizationName(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasPhoneNumber(): boolean;
  clearPhoneNumber(): void;
  getPhoneNumber(): google_protobuf_wrappers_pb.StringValue | undefined;
  setPhoneNumber(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasPostalCode(): boolean;
  clearPostalCode(): void;
  getPostalCode(): google_protobuf_wrappers_pb.StringValue | undefined;
  setPostalCode(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasRegion(): boolean;
  clearRegion(): void;
  getRegion(): google_protobuf_wrappers_pb.StringValue | undefined;
  setRegion(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasStreetAddress(): boolean;
  clearStreetAddress(): void;
  getStreetAddress(): google_protobuf_wrappers_pb.StringValue | undefined;
  setStreetAddress(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasStreetAddress2(): boolean;
  clearStreetAddress2(): void;
  getStreetAddress2(): google_protobuf_wrappers_pb.StringValue | undefined;
  setStreetAddress2(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasTitle(): boolean;
  clearTitle(): void;
  getTitle(): google_protobuf_wrappers_pb.StringValue | undefined;
  setTitle(value?: google_protobuf_wrappers_pb.StringValue): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Address.AsObject;
  static toObject(includeInstance: boolean, msg: Address): Address.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Address, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Address;
  static deserializeBinaryFromReader(message: Address, reader: jspb.BinaryReader): Address;
}

export namespace Address {
  export type AsObject = {
    attention?: google_protobuf_wrappers_pb.StringValue.AsObject,
    city?: google_protobuf_wrappers_pb.StringValue.AsObject,
    countryCode?: google_protobuf_wrappers_pb.StringValue.AsObject,
    emailAddress?: google_protobuf_wrappers_pb.StringValue.AsObject,
    familyName?: google_protobuf_wrappers_pb.StringValue.AsObject,
    givenName?: google_protobuf_wrappers_pb.StringValue.AsObject,
    organizationName?: google_protobuf_wrappers_pb.StringValue.AsObject,
    phoneNumber?: google_protobuf_wrappers_pb.StringValue.AsObject,
    postalCode?: google_protobuf_wrappers_pb.StringValue.AsObject,
    region?: google_protobuf_wrappers_pb.StringValue.AsObject,
    streetAddress?: google_protobuf_wrappers_pb.StringValue.AsObject,
    streetAddress2?: google_protobuf_wrappers_pb.StringValue.AsObject,
    title?: google_protobuf_wrappers_pb.StringValue.AsObject,
  }
}

export class OrderDetails extends jspb.Message {
  clearOrderItemsList(): void;
  getOrderItemsList(): Array<OrderItem>;
  setOrderItemsList(value: Array<OrderItem>): void;
  addOrderItems(value?: OrderItem, index?: number): OrderItem;

  getCountryCode(): string;
  setCountryCode(value: string): void;

  hasShippingAddress(): boolean;
  clearShippingAddress(): void;
  getShippingAddress(): Address | undefined;
  setShippingAddress(value?: Address): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OrderDetails.AsObject;
  static toObject(includeInstance: boolean, msg: OrderDetails): OrderDetails.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OrderDetails, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OrderDetails;
  static deserializeBinaryFromReader(message: OrderDetails, reader: jspb.BinaryReader): OrderDetails;
}

export namespace OrderDetails {
  export type AsObject = {
    orderItemsList: Array<OrderItem.AsObject>,
    countryCode: string,
    shippingAddress?: Address.AsObject,
  }
}

export class OrderItem extends jspb.Message {
  hasImageUrl(): boolean;
  clearImageUrl(): void;
  getImageUrl(): google_protobuf_wrappers_pb.StringValue | undefined;
  setImageUrl(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasMerchantData(): boolean;
  clearMerchantData(): void;
  getMerchantData(): google_protobuf_wrappers_pb.StringValue | undefined;
  setMerchantData(value?: google_protobuf_wrappers_pb.StringValue): void;

  getName(): string;
  setName(value: string): void;

  hasProductIdentifier(): boolean;
  clearProductIdentifier(): void;
  getProductIdentifier(): ProductIdentifier | undefined;
  setProductIdentifier(value?: ProductIdentifier): void;

  hasProductUrl(): boolean;
  clearProductUrl(): void;
  getProductUrl(): google_protobuf_wrappers_pb.StringValue | undefined;
  setProductUrl(value?: google_protobuf_wrappers_pb.StringValue): void;

  getQuantity(): number;
  setQuantity(value: number): void;

  getQuantityUnit(): string;
  setQuantityUnit(value: string): void;

  hasReference(): boolean;
  clearReference(): void;
  getReference(): google_protobuf_wrappers_pb.StringValue | undefined;
  setReference(value?: google_protobuf_wrappers_pb.StringValue): void;

  getTaxRate(): number;
  setTaxRate(value: number): void;

  getTotalDiscountAmount(): number;
  setTotalDiscountAmount(value: number): void;

  getTotalTaxAmount(): number;
  setTotalTaxAmount(value: number): void;

  getUnitPrice(): number;
  setUnitPrice(value: number): void;

  getTotalAmount(): number;
  setTotalAmount(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OrderItem.AsObject;
  static toObject(includeInstance: boolean, msg: OrderItem): OrderItem.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OrderItem, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OrderItem;
  static deserializeBinaryFromReader(message: OrderItem, reader: jspb.BinaryReader): OrderItem;
}

export namespace OrderItem {
  export type AsObject = {
    imageUrl?: google_protobuf_wrappers_pb.StringValue.AsObject,
    merchantData?: google_protobuf_wrappers_pb.StringValue.AsObject,
    name: string,
    productIdentifier?: ProductIdentifier.AsObject,
    productUrl?: google_protobuf_wrappers_pb.StringValue.AsObject,
    quantity: number,
    quantityUnit: string,
    reference?: google_protobuf_wrappers_pb.StringValue.AsObject,
    taxRate: number,
    totalDiscountAmount: number,
    totalTaxAmount: number,
    unitPrice: number,
    totalAmount: number,
  }
}

export class ProductIdentifier extends jspb.Message {
  hasBrand(): boolean;
  clearBrand(): void;
  getBrand(): google_protobuf_wrappers_pb.StringValue | undefined;
  setBrand(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasCategoryPath(): boolean;
  clearCategoryPath(): void;
  getCategoryPath(): google_protobuf_wrappers_pb.StringValue | undefined;
  setCategoryPath(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasGlobalTradeItemNumber(): boolean;
  clearGlobalTradeItemNumber(): void;
  getGlobalTradeItemNumber(): google_protobuf_wrappers_pb.StringValue | undefined;
  setGlobalTradeItemNumber(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasManufacturerPartNumber(): boolean;
  clearManufacturerPartNumber(): void;
  getManufacturerPartNumber(): google_protobuf_wrappers_pb.StringValue | undefined;
  setManufacturerPartNumber(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasColor(): boolean;
  clearColor(): void;
  getColor(): google_protobuf_wrappers_pb.StringValue | undefined;
  setColor(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasSize(): boolean;
  clearSize(): void;
  getSize(): google_protobuf_wrappers_pb.StringValue | undefined;
  setSize(value?: google_protobuf_wrappers_pb.StringValue): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ProductIdentifier.AsObject;
  static toObject(includeInstance: boolean, msg: ProductIdentifier): ProductIdentifier.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ProductIdentifier, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ProductIdentifier;
  static deserializeBinaryFromReader(message: ProductIdentifier, reader: jspb.BinaryReader): ProductIdentifier;
}

export namespace ProductIdentifier {
  export type AsObject = {
    brand?: google_protobuf_wrappers_pb.StringValue.AsObject,
    categoryPath?: google_protobuf_wrappers_pb.StringValue.AsObject,
    globalTradeItemNumber?: google_protobuf_wrappers_pb.StringValue.AsObject,
    manufacturerPartNumber?: google_protobuf_wrappers_pb.StringValue.AsObject,
    color?: google_protobuf_wrappers_pb.StringValue.AsObject,
    size?: google_protobuf_wrappers_pb.StringValue.AsObject,
  }
}

export class PaymentFlowRedirectRequestData extends jspb.Message {
  getBackUrl(): string;
  setBackUrl(value: string): void;

  getCancelUrl(): string;
  setCancelUrl(value: string): void;

  getFailedUrl(): string;
  setFailedUrl(value: string): void;

  getSuccessUrl(): string;
  setSuccessUrl(value: string): void;

  hasLogoUrl(): boolean;
  clearLogoUrl(): void;
  getLogoUrl(): google_protobuf_wrappers_pb.StringValue | undefined;
  setLogoUrl(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasPageTitle(): boolean;
  clearPageTitle(): void;
  getPageTitle(): google_protobuf_wrappers_pb.StringValue | undefined;
  setPageTitle(value?: google_protobuf_wrappers_pb.StringValue): void;

  getPurchaseType(): PurchaseTypeMap[keyof PurchaseTypeMap];
  setPurchaseType(value: PurchaseTypeMap[keyof PurchaseTypeMap]): void;

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
    backUrl: string,
    cancelUrl: string,
    failedUrl: string,
    successUrl: string,
    logoUrl?: google_protobuf_wrappers_pb.StringValue.AsObject,
    pageTitle?: google_protobuf_wrappers_pb.StringValue.AsObject,
    purchaseType: PurchaseTypeMap[keyof PurchaseTypeMap],
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

export interface PurchaseTypeMap {
  BUY: 0;
  RENT: 1;
  BOOK: 2;
  SUBSCRIBE: 3;
  DOWNLOAD: 4;
  ORDER: 5;
  CONTINUE: 6;
}

export const PurchaseType: PurchaseTypeMap;

export interface AcquiringChannelMap {
  ECOMMERCE: 0;
  IN_STORE: 1;
  TELESALES: 2;
}

export const AcquiringChannel: AcquiringChannelMap;

export interface ShippingMethodMap {
  UNDEFINED: 0;
  PICKUPSTORE: 1;
  HOME: 2;
  BOXREG: 3;
  BOXUNREG: 4;
  PICKUPPOINT: 5;
  OWN: 6;
  POSTAL: 7;
  DHLPACKSTATION: 8;
  DIGITAL: 9;
  PICKUPWAREHOUSE: 10;
  CLICKCOLLECT: 11;
  PALLETDELIVERY: 12;
}

export const ShippingMethod: ShippingMethodMap;

