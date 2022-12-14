// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.18.1
// source: relay/processing/v1/paymentmethods/expressbank.proto

package paymentmethods

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// Express Bank refund reason codes
type RefundReasonCode int32

const (
	RefundReasonCode_DEFECT_IN_PRODUCT         RefundReasonCode = 0
	RefundReasonCode_CUSTOMER_CHANGED_HIS_MIND RefundReasonCode = 1
	RefundReasonCode_PRODUCT_RECALLED          RefundReasonCode = 2
	RefundReasonCode_TECHNICAL_OR_HUMAN_ERROR  RefundReasonCode = 3
)

// Enum value maps for RefundReasonCode.
var (
	RefundReasonCode_name = map[int32]string{
		0: "DEFECT_IN_PRODUCT",
		1: "CUSTOMER_CHANGED_HIS_MIND",
		2: "PRODUCT_RECALLED",
		3: "TECHNICAL_OR_HUMAN_ERROR",
	}
	RefundReasonCode_value = map[string]int32{
		"DEFECT_IN_PRODUCT":         0,
		"CUSTOMER_CHANGED_HIS_MIND": 1,
		"PRODUCT_RECALLED":          2,
		"TECHNICAL_OR_HUMAN_ERROR":  3,
	}
)

func (x RefundReasonCode) Enum() *RefundReasonCode {
	p := new(RefundReasonCode)
	*p = x
	return p
}

func (x RefundReasonCode) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (RefundReasonCode) Descriptor() protoreflect.EnumDescriptor {
	return file_relay_processing_v1_paymentmethods_expressbank_proto_enumTypes[0].Descriptor()
}

func (RefundReasonCode) Type() protoreflect.EnumType {
	return &file_relay_processing_v1_paymentmethods_expressbank_proto_enumTypes[0]
}

func (x RefundReasonCode) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use RefundReasonCode.Descriptor instead.
func (RefundReasonCode) EnumDescriptor() ([]byte, []int) {
	return file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescGZIP(), []int{0}
}

type AuthorizeRequestData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PaymentFlowData *PaymentFlowRedirectRequestData `protobuf:"bytes,1,opt,name=payment_flow_data,json=paymentFlowData,proto3" json:"payment_flow_data,omitempty"`
	// Regex: ^.{1,30}$
	Items []string `protobuf:"bytes,2,rep,name=items,proto3" json:"items,omitempty"`
}

func (x *AuthorizeRequestData) Reset() {
	*x = AuthorizeRequestData{}
	if protoimpl.UnsafeEnabled {
		mi := &file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *AuthorizeRequestData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AuthorizeRequestData) ProtoMessage() {}

func (x *AuthorizeRequestData) ProtoReflect() protoreflect.Message {
	mi := &file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AuthorizeRequestData.ProtoReflect.Descriptor instead.
func (*AuthorizeRequestData) Descriptor() ([]byte, []int) {
	return file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescGZIP(), []int{0}
}

func (x *AuthorizeRequestData) GetPaymentFlowData() *PaymentFlowRedirectRequestData {
	if x != nil {
		return x.PaymentFlowData
	}
	return nil
}

func (x *AuthorizeRequestData) GetItems() []string {
	if x != nil {
		return x.Items
	}
	return nil
}

type AuthorizeResponseData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PaymentFlowData *PaymentFlowRedirectResponseData `protobuf:"bytes,1,opt,name=payment_flow_data,json=paymentFlowData,proto3" json:"payment_flow_data,omitempty"`
}

func (x *AuthorizeResponseData) Reset() {
	*x = AuthorizeResponseData{}
	if protoimpl.UnsafeEnabled {
		mi := &file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *AuthorizeResponseData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AuthorizeResponseData) ProtoMessage() {}

func (x *AuthorizeResponseData) ProtoReflect() protoreflect.Message {
	mi := &file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AuthorizeResponseData.ProtoReflect.Descriptor instead.
func (*AuthorizeResponseData) Descriptor() ([]byte, []int) {
	return file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescGZIP(), []int{1}
}

func (x *AuthorizeResponseData) GetPaymentFlowData() *PaymentFlowRedirectResponseData {
	if x != nil {
		return x.PaymentFlowData
	}
	return nil
}

type PaymentFlowRedirectResponseData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ApprovalUrl string `protobuf:"bytes,1,opt,name=approval_url,json=approvalUrl,proto3" json:"approval_url,omitempty"`
}

func (x *PaymentFlowRedirectResponseData) Reset() {
	*x = PaymentFlowRedirectResponseData{}
	if protoimpl.UnsafeEnabled {
		mi := &file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PaymentFlowRedirectResponseData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PaymentFlowRedirectResponseData) ProtoMessage() {}

func (x *PaymentFlowRedirectResponseData) ProtoReflect() protoreflect.Message {
	mi := &file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PaymentFlowRedirectResponseData.ProtoReflect.Descriptor instead.
func (*PaymentFlowRedirectResponseData) Descriptor() ([]byte, []int) {
	return file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescGZIP(), []int{2}
}

func (x *PaymentFlowRedirectResponseData) GetApprovalUrl() string {
	if x != nil {
		return x.ApprovalUrl
	}
	return ""
}

type RefundRequestData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Express Bank refund reason code
	ReasonCode RefundReasonCode `protobuf:"varint,1,opt,name=reason_code,json=reasonCode,proto3,enum=relay.processing.v1.paymentmethods.expressbank.RefundReasonCode" json:"reason_code,omitempty"`
}

func (x *RefundRequestData) Reset() {
	*x = RefundRequestData{}
	if protoimpl.UnsafeEnabled {
		mi := &file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RefundRequestData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RefundRequestData) ProtoMessage() {}

func (x *RefundRequestData) ProtoReflect() protoreflect.Message {
	mi := &file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RefundRequestData.ProtoReflect.Descriptor instead.
func (*RefundRequestData) Descriptor() ([]byte, []int) {
	return file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescGZIP(), []int{3}
}

func (x *RefundRequestData) GetReasonCode() RefundReasonCode {
	if x != nil {
		return x.ReasonCode
	}
	return RefundReasonCode_DEFECT_IN_PRODUCT
}

type PaymentFlowRedirectRequestData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// PaymentId and AuthorizeId are appended as query parameters
	SuccessUrl string `protobuf:"bytes,1,opt,name=success_url,json=successUrl,proto3" json:"success_url,omitempty"`
	// PaymentId and AuthorizeId are appended as query parameters
	FailedUrl string `protobuf:"bytes,2,opt,name=failed_url,json=failedUrl,proto3" json:"failed_url,omitempty"`
}

func (x *PaymentFlowRedirectRequestData) Reset() {
	*x = PaymentFlowRedirectRequestData{}
	if protoimpl.UnsafeEnabled {
		mi := &file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PaymentFlowRedirectRequestData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PaymentFlowRedirectRequestData) ProtoMessage() {}

func (x *PaymentFlowRedirectRequestData) ProtoReflect() protoreflect.Message {
	mi := &file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PaymentFlowRedirectRequestData.ProtoReflect.Descriptor instead.
func (*PaymentFlowRedirectRequestData) Descriptor() ([]byte, []int) {
	return file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescGZIP(), []int{4}
}

func (x *PaymentFlowRedirectRequestData) GetSuccessUrl() string {
	if x != nil {
		return x.SuccessUrl
	}
	return ""
}

func (x *PaymentFlowRedirectRequestData) GetFailedUrl() string {
	if x != nil {
		return x.FailedUrl
	}
	return ""
}

var File_relay_processing_v1_paymentmethods_expressbank_proto protoreflect.FileDescriptor

var file_relay_processing_v1_paymentmethods_expressbank_proto_rawDesc = []byte{
	0x0a, 0x34, 0x72, 0x65, 0x6c, 0x61, 0x79, 0x2f, 0x70, 0x72, 0x6f, 0x63, 0x65, 0x73, 0x73, 0x69,
	0x6e, 0x67, 0x2f, 0x76, 0x31, 0x2f, 0x70, 0x61, 0x79, 0x6d, 0x65, 0x6e, 0x74, 0x6d, 0x65, 0x74,
	0x68, 0x6f, 0x64, 0x73, 0x2f, 0x65, 0x78, 0x70, 0x72, 0x65, 0x73, 0x73, 0x62, 0x61, 0x6e, 0x6b,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x2e, 0x72, 0x65, 0x6c, 0x61, 0x79, 0x2e, 0x70, 0x72,
	0x6f, 0x63, 0x65, 0x73, 0x73, 0x69, 0x6e, 0x67, 0x2e, 0x76, 0x31, 0x2e, 0x70, 0x61, 0x79, 0x6d,
	0x65, 0x6e, 0x74, 0x6d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x73, 0x2e, 0x65, 0x78, 0x70, 0x72, 0x65,
	0x73, 0x73, 0x62, 0x61, 0x6e, 0x6b, 0x22, 0xa8, 0x01, 0x0a, 0x14, 0x41, 0x75, 0x74, 0x68, 0x6f,
	0x72, 0x69, 0x7a, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x44, 0x61, 0x74, 0x61, 0x12,
	0x7a, 0x0a, 0x11, 0x70, 0x61, 0x79, 0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x66, 0x6c, 0x6f, 0x77, 0x5f,
	0x64, 0x61, 0x74, 0x61, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x4e, 0x2e, 0x72, 0x65, 0x6c,
	0x61, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x63, 0x65, 0x73, 0x73, 0x69, 0x6e, 0x67, 0x2e, 0x76, 0x31,
	0x2e, 0x70, 0x61, 0x79, 0x6d, 0x65, 0x6e, 0x74, 0x6d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x73, 0x2e,
	0x65, 0x78, 0x70, 0x72, 0x65, 0x73, 0x73, 0x62, 0x61, 0x6e, 0x6b, 0x2e, 0x50, 0x61, 0x79, 0x6d,
	0x65, 0x6e, 0x74, 0x46, 0x6c, 0x6f, 0x77, 0x52, 0x65, 0x64, 0x69, 0x72, 0x65, 0x63, 0x74, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x44, 0x61, 0x74, 0x61, 0x52, 0x0f, 0x70, 0x61, 0x79, 0x6d,
	0x65, 0x6e, 0x74, 0x46, 0x6c, 0x6f, 0x77, 0x44, 0x61, 0x74, 0x61, 0x12, 0x14, 0x0a, 0x05, 0x69,
	0x74, 0x65, 0x6d, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x09, 0x52, 0x05, 0x69, 0x74, 0x65, 0x6d,
	0x73, 0x22, 0x94, 0x01, 0x0a, 0x15, 0x41, 0x75, 0x74, 0x68, 0x6f, 0x72, 0x69, 0x7a, 0x65, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x44, 0x61, 0x74, 0x61, 0x12, 0x7b, 0x0a, 0x11, 0x70,
	0x61, 0x79, 0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x66, 0x6c, 0x6f, 0x77, 0x5f, 0x64, 0x61, 0x74, 0x61,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x4f, 0x2e, 0x72, 0x65, 0x6c, 0x61, 0x79, 0x2e, 0x70,
	0x72, 0x6f, 0x63, 0x65, 0x73, 0x73, 0x69, 0x6e, 0x67, 0x2e, 0x76, 0x31, 0x2e, 0x70, 0x61, 0x79,
	0x6d, 0x65, 0x6e, 0x74, 0x6d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x73, 0x2e, 0x65, 0x78, 0x70, 0x72,
	0x65, 0x73, 0x73, 0x62, 0x61, 0x6e, 0x6b, 0x2e, 0x50, 0x61, 0x79, 0x6d, 0x65, 0x6e, 0x74, 0x46,
	0x6c, 0x6f, 0x77, 0x52, 0x65, 0x64, 0x69, 0x72, 0x65, 0x63, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f,
	0x6e, 0x73, 0x65, 0x44, 0x61, 0x74, 0x61, 0x52, 0x0f, 0x70, 0x61, 0x79, 0x6d, 0x65, 0x6e, 0x74,
	0x46, 0x6c, 0x6f, 0x77, 0x44, 0x61, 0x74, 0x61, 0x22, 0x44, 0x0a, 0x1f, 0x50, 0x61, 0x79, 0x6d,
	0x65, 0x6e, 0x74, 0x46, 0x6c, 0x6f, 0x77, 0x52, 0x65, 0x64, 0x69, 0x72, 0x65, 0x63, 0x74, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x44, 0x61, 0x74, 0x61, 0x12, 0x21, 0x0a, 0x0c, 0x61,
	0x70, 0x70, 0x72, 0x6f, 0x76, 0x61, 0x6c, 0x5f, 0x75, 0x72, 0x6c, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x0b, 0x61, 0x70, 0x70, 0x72, 0x6f, 0x76, 0x61, 0x6c, 0x55, 0x72, 0x6c, 0x22, 0x76,
	0x0a, 0x11, 0x52, 0x65, 0x66, 0x75, 0x6e, 0x64, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x44,
	0x61, 0x74, 0x61, 0x12, 0x61, 0x0a, 0x0b, 0x72, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x5f, 0x63, 0x6f,
	0x64, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x40, 0x2e, 0x72, 0x65, 0x6c, 0x61, 0x79,
	0x2e, 0x70, 0x72, 0x6f, 0x63, 0x65, 0x73, 0x73, 0x69, 0x6e, 0x67, 0x2e, 0x76, 0x31, 0x2e, 0x70,
	0x61, 0x79, 0x6d, 0x65, 0x6e, 0x74, 0x6d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x73, 0x2e, 0x65, 0x78,
	0x70, 0x72, 0x65, 0x73, 0x73, 0x62, 0x61, 0x6e, 0x6b, 0x2e, 0x52, 0x65, 0x66, 0x75, 0x6e, 0x64,
	0x52, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x43, 0x6f, 0x64, 0x65, 0x52, 0x0a, 0x72, 0x65, 0x61, 0x73,
	0x6f, 0x6e, 0x43, 0x6f, 0x64, 0x65, 0x22, 0x60, 0x0a, 0x1e, 0x50, 0x61, 0x79, 0x6d, 0x65, 0x6e,
	0x74, 0x46, 0x6c, 0x6f, 0x77, 0x52, 0x65, 0x64, 0x69, 0x72, 0x65, 0x63, 0x74, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x44, 0x61, 0x74, 0x61, 0x12, 0x1f, 0x0a, 0x0b, 0x73, 0x75, 0x63, 0x63,
	0x65, 0x73, 0x73, 0x5f, 0x75, 0x72, 0x6c, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x73,
	0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x55, 0x72, 0x6c, 0x12, 0x1d, 0x0a, 0x0a, 0x66, 0x61, 0x69,
	0x6c, 0x65, 0x64, 0x5f, 0x75, 0x72, 0x6c, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x66,
	0x61, 0x69, 0x6c, 0x65, 0x64, 0x55, 0x72, 0x6c, 0x2a, 0x7c, 0x0a, 0x10, 0x52, 0x65, 0x66, 0x75,
	0x6e, 0x64, 0x52, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x43, 0x6f, 0x64, 0x65, 0x12, 0x15, 0x0a, 0x11,
	0x44, 0x45, 0x46, 0x45, 0x43, 0x54, 0x5f, 0x49, 0x4e, 0x5f, 0x50, 0x52, 0x4f, 0x44, 0x55, 0x43,
	0x54, 0x10, 0x00, 0x12, 0x1d, 0x0a, 0x19, 0x43, 0x55, 0x53, 0x54, 0x4f, 0x4d, 0x45, 0x52, 0x5f,
	0x43, 0x48, 0x41, 0x4e, 0x47, 0x45, 0x44, 0x5f, 0x48, 0x49, 0x53, 0x5f, 0x4d, 0x49, 0x4e, 0x44,
	0x10, 0x01, 0x12, 0x14, 0x0a, 0x10, 0x50, 0x52, 0x4f, 0x44, 0x55, 0x43, 0x54, 0x5f, 0x52, 0x45,
	0x43, 0x41, 0x4c, 0x4c, 0x45, 0x44, 0x10, 0x02, 0x12, 0x1c, 0x0a, 0x18, 0x54, 0x45, 0x43, 0x48,
	0x4e, 0x49, 0x43, 0x41, 0x4c, 0x5f, 0x4f, 0x52, 0x5f, 0x48, 0x55, 0x4d, 0x41, 0x4e, 0x5f, 0x45,
	0x52, 0x52, 0x4f, 0x52, 0x10, 0x03, 0x42, 0x7b, 0x5a, 0x48, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62,
	0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x4e, 0x65, 0x64, 0x76, 0x65, 0x64, 0x37, 0x35, 0x2f, 0x67, 0x72,
	0x70, 0x63, 0x73, 0x69, 0x6d, 0x70, 0x6c, 0x65, 0x2f, 0x73, 0x64, 0x6b, 0x2f, 0x67, 0x6f, 0x2f,
	0x72, 0x65, 0x6c, 0x61, 0x79, 0x2f, 0x70, 0x72, 0x6f, 0x63, 0x65, 0x73, 0x73, 0x69, 0x6e, 0x67,
	0x2f, 0x76, 0x31, 0x2f, 0x70, 0x61, 0x79, 0x6d, 0x65, 0x6e, 0x74, 0x6d, 0x65, 0x74, 0x68, 0x6f,
	0x64, 0x73, 0xaa, 0x02, 0x2e, 0x52, 0x65, 0x6c, 0x61, 0x79, 0x2e, 0x50, 0x72, 0x6f, 0x63, 0x65,
	0x73, 0x73, 0x69, 0x6e, 0x67, 0x2e, 0x56, 0x31, 0x2e, 0x50, 0x61, 0x79, 0x6d, 0x65, 0x6e, 0x74,
	0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x73, 0x2e, 0x45, 0x78, 0x70, 0x72, 0x65, 0x73, 0x73, 0x42,
	0x61, 0x6e, 0x6b, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescOnce sync.Once
	file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescData = file_relay_processing_v1_paymentmethods_expressbank_proto_rawDesc
)

func file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescGZIP() []byte {
	file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescOnce.Do(func() {
		file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescData = protoimpl.X.CompressGZIP(file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescData)
	})
	return file_relay_processing_v1_paymentmethods_expressbank_proto_rawDescData
}

var file_relay_processing_v1_paymentmethods_expressbank_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_relay_processing_v1_paymentmethods_expressbank_proto_goTypes = []interface{}{
	(RefundReasonCode)(0),                   // 0: relay.processing.v1.paymentmethods.expressbank.RefundReasonCode
	(*AuthorizeRequestData)(nil),            // 1: relay.processing.v1.paymentmethods.expressbank.AuthorizeRequestData
	(*AuthorizeResponseData)(nil),           // 2: relay.processing.v1.paymentmethods.expressbank.AuthorizeResponseData
	(*PaymentFlowRedirectResponseData)(nil), // 3: relay.processing.v1.paymentmethods.expressbank.PaymentFlowRedirectResponseData
	(*RefundRequestData)(nil),               // 4: relay.processing.v1.paymentmethods.expressbank.RefundRequestData
	(*PaymentFlowRedirectRequestData)(nil),  // 5: relay.processing.v1.paymentmethods.expressbank.PaymentFlowRedirectRequestData
}
var file_relay_processing_v1_paymentmethods_expressbank_proto_depIdxs = []int32{
	5, // 0: relay.processing.v1.paymentmethods.expressbank.AuthorizeRequestData.payment_flow_data:type_name -> relay.processing.v1.paymentmethods.expressbank.PaymentFlowRedirectRequestData
	3, // 1: relay.processing.v1.paymentmethods.expressbank.AuthorizeResponseData.payment_flow_data:type_name -> relay.processing.v1.paymentmethods.expressbank.PaymentFlowRedirectResponseData
	0, // 2: relay.processing.v1.paymentmethods.expressbank.RefundRequestData.reason_code:type_name -> relay.processing.v1.paymentmethods.expressbank.RefundReasonCode
	3, // [3:3] is the sub-list for method output_type
	3, // [3:3] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_relay_processing_v1_paymentmethods_expressbank_proto_init() }
func file_relay_processing_v1_paymentmethods_expressbank_proto_init() {
	if File_relay_processing_v1_paymentmethods_expressbank_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*AuthorizeRequestData); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*AuthorizeResponseData); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PaymentFlowRedirectResponseData); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*RefundRequestData); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PaymentFlowRedirectRequestData); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_relay_processing_v1_paymentmethods_expressbank_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_relay_processing_v1_paymentmethods_expressbank_proto_goTypes,
		DependencyIndexes: file_relay_processing_v1_paymentmethods_expressbank_proto_depIdxs,
		EnumInfos:         file_relay_processing_v1_paymentmethods_expressbank_proto_enumTypes,
		MessageInfos:      file_relay_processing_v1_paymentmethods_expressbank_proto_msgTypes,
	}.Build()
	File_relay_processing_v1_paymentmethods_expressbank_proto = out.File
	file_relay_processing_v1_paymentmethods_expressbank_proto_rawDesc = nil
	file_relay_processing_v1_paymentmethods_expressbank_proto_goTypes = nil
	file_relay_processing_v1_paymentmethods_expressbank_proto_depIdxs = nil
}
