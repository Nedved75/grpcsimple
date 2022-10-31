/* eslint-disable */
/*Generated by GenDocu.com*/
// package: relay.onboarding.v1.paymentmethods.klarna
// file: relay/onboarding/v1/paymentmethods/klarna.proto

import * as jspb from "google-protobuf";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
import * as google_protobuf_wrappers_pb from "google-protobuf/google/protobuf/wrappers_pb";

export class InitializeRequestData extends jspb.Message {
  hasBusinessDetails(): boolean;
  clearBusinessDetails(): void;
  getBusinessDetails(): BusinessDetails | undefined;
  setBusinessDetails(value?: BusinessDetails): void;

  hasStoreDetails(): boolean;
  clearStoreDetails(): void;
  getStoreDetails(): StoreDetails | undefined;
  setStoreDetails(value?: StoreDetails): void;

  clearStakeholdersDetailsList(): void;
  getStakeholdersDetailsList(): Array<StakeholderDetails>;
  setStakeholdersDetailsList(value: Array<StakeholderDetails>): void;
  addStakeholdersDetails(value?: StakeholderDetails, index?: number): StakeholderDetails;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InitializeRequestData.AsObject;
  static toObject(includeInstance: boolean, msg: InitializeRequestData): InitializeRequestData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InitializeRequestData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InitializeRequestData;
  static deserializeBinaryFromReader(message: InitializeRequestData, reader: jspb.BinaryReader): InitializeRequestData;
}

export namespace InitializeRequestData {
  export type AsObject = {
    businessDetails?: BusinessDetails.AsObject,
    storeDetails?: StoreDetails.AsObject,
    stakeholdersDetailsList: Array<StakeholderDetails.AsObject>,
  }
}

export class UpdateRequestData extends jspb.Message {
  hasBusinessDetails(): boolean;
  clearBusinessDetails(): void;
  getBusinessDetails(): BusinessDetails | undefined;
  setBusinessDetails(value?: BusinessDetails): void;

  hasStoreDetails(): boolean;
  clearStoreDetails(): void;
  getStoreDetails(): StoreDetails | undefined;
  setStoreDetails(value?: StoreDetails): void;

  clearStakeholdersDetailsList(): void;
  getStakeholdersDetailsList(): Array<StakeholderDetails>;
  setStakeholdersDetailsList(value: Array<StakeholderDetails>): void;
  addStakeholdersDetails(value?: StakeholderDetails, index?: number): StakeholderDetails;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateRequestData.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateRequestData): UpdateRequestData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateRequestData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateRequestData;
  static deserializeBinaryFromReader(message: UpdateRequestData, reader: jspb.BinaryReader): UpdateRequestData;
}

export namespace UpdateRequestData {
  export type AsObject = {
    businessDetails?: BusinessDetails.AsObject,
    storeDetails?: StoreDetails.AsObject,
    stakeholdersDetailsList: Array<StakeholderDetails.AsObject>,
  }
}

export class BusinessDetails extends jspb.Message {
  hasName(): boolean;
  clearName(): void;
  getName(): google_protobuf_wrappers_pb.StringValue | undefined;
  setName(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasRegisteredAddress(): boolean;
  clearRegisteredAddress(): void;
  getRegisteredAddress(): Address | undefined;
  setRegisteredAddress(value?: Address): void;

  getIsRegistered(): boolean;
  setIsRegistered(value: boolean): void;

  hasRegistrationId(): boolean;
  clearRegistrationId(): void;
  getRegistrationId(): google_protobuf_wrappers_pb.StringValue | undefined;
  setRegistrationId(value?: google_protobuf_wrappers_pb.StringValue): void;

  getSubjectToVat(): boolean;
  setSubjectToVat(value: boolean): void;

  hasVatId(): boolean;
  clearVatId(): void;
  getVatId(): google_protobuf_wrappers_pb.StringValue | undefined;
  setVatId(value?: google_protobuf_wrappers_pb.StringValue): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BusinessDetails.AsObject;
  static toObject(includeInstance: boolean, msg: BusinessDetails): BusinessDetails.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BusinessDetails, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BusinessDetails;
  static deserializeBinaryFromReader(message: BusinessDetails, reader: jspb.BinaryReader): BusinessDetails;
}

export namespace BusinessDetails {
  export type AsObject = {
    name?: google_protobuf_wrappers_pb.StringValue.AsObject,
    registeredAddress?: Address.AsObject,
    isRegistered: boolean,
    registrationId?: google_protobuf_wrappers_pb.StringValue.AsObject,
    subjectToVat: boolean,
    vatId?: google_protobuf_wrappers_pb.StringValue.AsObject,
  }
}

export class StakeholderDetails extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): google_protobuf_wrappers_pb.StringValue | undefined;
  setResourceId(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasGivenName(): boolean;
  clearGivenName(): void;
  getGivenName(): google_protobuf_wrappers_pb.StringValue | undefined;
  setGivenName(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasFamilyName(): boolean;
  clearFamilyName(): void;
  getFamilyName(): google_protobuf_wrappers_pb.StringValue | undefined;
  setFamilyName(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasDateOfBirth(): boolean;
  clearDateOfBirth(): void;
  getDateOfBirth(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setDateOfBirth(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasAddress(): boolean;
  clearAddress(): void;
  getAddress(): Address | undefined;
  setAddress(value?: Address): void;

  hasPersonalId(): boolean;
  clearPersonalId(): void;
  getPersonalId(): google_protobuf_wrappers_pb.StringValue | undefined;
  setPersonalId(value?: google_protobuf_wrappers_pb.StringValue): void;

  clearRolesList(): void;
  getRolesList(): Array<RolesMap[keyof RolesMap]>;
  setRolesList(value: Array<RolesMap[keyof RolesMap]>): void;
  addRoles(value: RolesMap[keyof RolesMap], index?: number): RolesMap[keyof RolesMap];

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): StakeholderDetails.AsObject;
  static toObject(includeInstance: boolean, msg: StakeholderDetails): StakeholderDetails.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: StakeholderDetails, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): StakeholderDetails;
  static deserializeBinaryFromReader(message: StakeholderDetails, reader: jspb.BinaryReader): StakeholderDetails;
}

export namespace StakeholderDetails {
  export type AsObject = {
    resourceId?: google_protobuf_wrappers_pb.StringValue.AsObject,
    givenName?: google_protobuf_wrappers_pb.StringValue.AsObject,
    familyName?: google_protobuf_wrappers_pb.StringValue.AsObject,
    dateOfBirth?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    address?: Address.AsObject,
    personalId?: google_protobuf_wrappers_pb.StringValue.AsObject,
    rolesList: Array<RolesMap[keyof RolesMap]>,
  }
}

export class Address extends jspb.Message {
  hasStreet(): boolean;
  clearStreet(): void;
  getStreet(): google_protobuf_wrappers_pb.StringValue | undefined;
  setStreet(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasStreet2(): boolean;
  clearStreet2(): void;
  getStreet2(): google_protobuf_wrappers_pb.StringValue | undefined;
  setStreet2(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasPostalCode(): boolean;
  clearPostalCode(): void;
  getPostalCode(): google_protobuf_wrappers_pb.StringValue | undefined;
  setPostalCode(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasCity(): boolean;
  clearCity(): void;
  getCity(): google_protobuf_wrappers_pb.StringValue | undefined;
  setCity(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasCountryCode(): boolean;
  clearCountryCode(): void;
  getCountryCode(): google_protobuf_wrappers_pb.StringValue | undefined;
  setCountryCode(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasRegion(): boolean;
  clearRegion(): void;
  getRegion(): google_protobuf_wrappers_pb.StringValue | undefined;
  setRegion(value?: google_protobuf_wrappers_pb.StringValue): void;

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
    street?: google_protobuf_wrappers_pb.StringValue.AsObject,
    street2?: google_protobuf_wrappers_pb.StringValue.AsObject,
    postalCode?: google_protobuf_wrappers_pb.StringValue.AsObject,
    city?: google_protobuf_wrappers_pb.StringValue.AsObject,
    countryCode?: google_protobuf_wrappers_pb.StringValue.AsObject,
    region?: google_protobuf_wrappers_pb.StringValue.AsObject,
  }
}

export class StoreDetails extends jspb.Message {
  hasName(): boolean;
  clearName(): void;
  getName(): google_protobuf_wrappers_pb.StringValue | undefined;
  setName(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasUrl(): boolean;
  clearUrl(): void;
  getUrl(): google_protobuf_wrappers_pb.StringValue | undefined;
  setUrl(value?: google_protobuf_wrappers_pb.StringValue): void;

  getCategory(): CategoryMap[keyof CategoryMap];
  setCategory(value: CategoryMap[keyof CategoryMap]): void;

  hasCountryCode(): boolean;
  clearCountryCode(): void;
  getCountryCode(): google_protobuf_wrappers_pb.StringValue | undefined;
  setCountryCode(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasLogoUrl(): boolean;
  clearLogoUrl(): void;
  getLogoUrl(): google_protobuf_wrappers_pb.StringValue | undefined;
  setLogoUrl(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasIconUrl(): boolean;
  clearIconUrl(): void;
  getIconUrl(): google_protobuf_wrappers_pb.StringValue | undefined;
  setIconUrl(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasFeatureImageUrl(): boolean;
  clearFeatureImageUrl(): void;
  getFeatureImageUrl(): google_protobuf_wrappers_pb.StringValue | undefined;
  setFeatureImageUrl(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasFacebookUrl(): boolean;
  clearFacebookUrl(): void;
  getFacebookUrl(): google_protobuf_wrappers_pb.StringValue | undefined;
  setFacebookUrl(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasInstagramUrl(): boolean;
  clearInstagramUrl(): void;
  getInstagramUrl(): google_protobuf_wrappers_pb.StringValue | undefined;
  setInstagramUrl(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasAdminEmailAddress(): boolean;
  clearAdminEmailAddress(): void;
  getAdminEmailAddress(): google_protobuf_wrappers_pb.StringValue | undefined;
  setAdminEmailAddress(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasRiskEmailAddress(): boolean;
  clearRiskEmailAddress(): void;
  getRiskEmailAddress(): google_protobuf_wrappers_pb.StringValue | undefined;
  setRiskEmailAddress(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasCustomerSupportEmailAddress(): boolean;
  clearCustomerSupportEmailAddress(): void;
  getCustomerSupportEmailAddress(): google_protobuf_wrappers_pb.StringValue | undefined;
  setCustomerSupportEmailAddress(value?: google_protobuf_wrappers_pb.StringValue): void;

  hasCustomerSupportPhoneNumber(): boolean;
  clearCustomerSupportPhoneNumber(): void;
  getCustomerSupportPhoneNumber(): google_protobuf_wrappers_pb.StringValue | undefined;
  setCustomerSupportPhoneNumber(value?: google_protobuf_wrappers_pb.StringValue): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): StoreDetails.AsObject;
  static toObject(includeInstance: boolean, msg: StoreDetails): StoreDetails.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: StoreDetails, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): StoreDetails;
  static deserializeBinaryFromReader(message: StoreDetails, reader: jspb.BinaryReader): StoreDetails;
}

export namespace StoreDetails {
  export type AsObject = {
    name?: google_protobuf_wrappers_pb.StringValue.AsObject,
    url?: google_protobuf_wrappers_pb.StringValue.AsObject,
    category: CategoryMap[keyof CategoryMap],
    countryCode?: google_protobuf_wrappers_pb.StringValue.AsObject,
    logoUrl?: google_protobuf_wrappers_pb.StringValue.AsObject,
    iconUrl?: google_protobuf_wrappers_pb.StringValue.AsObject,
    featureImageUrl?: google_protobuf_wrappers_pb.StringValue.AsObject,
    facebookUrl?: google_protobuf_wrappers_pb.StringValue.AsObject,
    instagramUrl?: google_protobuf_wrappers_pb.StringValue.AsObject,
    adminEmailAddress?: google_protobuf_wrappers_pb.StringValue.AsObject,
    riskEmailAddress?: google_protobuf_wrappers_pb.StringValue.AsObject,
    customerSupportEmailAddress?: google_protobuf_wrappers_pb.StringValue.AsObject,
    customerSupportPhoneNumber?: google_protobuf_wrappers_pb.StringValue.AsObject,
  }
}

export interface CategoryMap {
  ADULT_SHOES_AND_CLOTHING: 0;
  AUTOMOTIVE_PARTS_AND_ACCESSORIES: 1;
  BAGS_AND_WALLETS: 2;
  BODY_AND_HAIR_CARE: 3;
  BOOK_AND_MAGAZINES: 4;
  CANDY: 5;
  CAR_ELECTRONICS: 6;
  CHILDREN_CLOTHES_AND_NURTURING_PRODUCTS: 7;
  CHILDREN_TOYS: 8;
  CLEANING_AND_SANITARY: 9;
  COLLECTIBLES: 10;
  CONCEPT_STORES_AND_MISCELLANEOUS: 11;
  COSMETICS: 12;
  COSTUMES_AND_PARTY_SUPPLIES: 13;
  DATING_SERVICES: 14;
  DECORATION_AND_ART: 15;
  DIETARY_SUPPLEMENTS: 16;
  DIGITAL_SERVICES: 17;
  DIVERSIFIED_CHILDREN_PRODUCTS: 18;
  DIVERSIFIED_ELECTRONICS: 19;
  DIVERSIFIED_ENTERTAINMENT: 20;
  DIVERSIFIED_EROTIC_MATERIAL: 21;
  DIVERSIFIED_HOME_AND_GARDEN_PRODUCTS: 22;
  DIVERSIFIED_JEWELRY_AND_ACCESSORIES: 23;
  DIVERSIFIED_HEALTH_AND_BEAUTY_PRODUCTS: 24;
  DIVERSIFIES_HEALTH_AND_BEAUTY_PRODUCTS: 25;
  EDUCATION: 26;
  ELECTRONIC_EQUIPMENT_AND_RELATED_ACCESSORIES: 27;
  EROTIC_CLOTHING_AND_ACCESSORIES: 28;
  EVENT_TICKETS: 29;
  FOOD_AND_BEVERAGE: 30;
  FRAGRANCES: 31;
  FURNITURE: 32;
  GENERAL_SHOES_AND_CLOTHING: 33;
  HOBBY_ARTICLES: 34;
  HOUSEHOLD_ELECTRONICS: 35;
  JEWELRY_AND_WATCHES: 36;
  KITCHENWARE: 37;
  MARKETPLACES: 38;
  MUSIC_AND_MOVIES: 39;
  MUSICAL_INSTRUMENTS_AND_EQUIPMENT: 40;
  NON_PRESCRIPTION_SUNGLASSES_AND_LENSES: 41;
  OFFICE_MACHINES_AND_RELATED_ACCESSORIES: 42;
  OTHER_SERVICES: 43;
  PERSONAL_CARE_AND_BODY_IMPROVEMENT: 44;
  PET_SUPPLIES: 45;
  PHARMACEUTICAL_PRODUCTS: 46;
  PLANTS_AND_FLOWERS: 47;
  PRESCRIPTION_OPTICS: 48;
  PRINTS_AND_PHOTOS: 49;
  SAFETY_PRODUCTS: 50;
  SEX_TOYS: 51;
  SPORTS_GEAR_AND_OUTDOOR: 52;
  TOBACCO: 53;
  TOOLS_AND_HOME_IMPROVEMENT: 54;
  TRAVEL_SERVICES: 55;
  UNDERWEAR: 56;
  VIDEO_GAMES_AND_RELATED_ACCESSORIES: 57;
  WHEELS_AND_TIRES: 58;
  WINE_BEER_AND_LIQUOR: 59;
  YOUTHFUL_SHOES_AND_CLOTHING: 60;
}

export const Category: CategoryMap;

export interface RolesMap {
  APPLICANT: 0;
  CONTROL_OVER_MANAGEMENT: 1;
  OWNER: 2;
  PARTNER: 3;
  SOLE_TRADER: 4;
  ULTIMATE_BENEFICIAL_OWNER: 5;
  MANAGING_DIRECTOR: 6;
  POLITICALLY_EXPOSED_PERSON: 7;
  MATERIAL_INFLUENCER: 8;
  NOT_APPLICABLE: 9;
}

export const Roles: RolesMap;

