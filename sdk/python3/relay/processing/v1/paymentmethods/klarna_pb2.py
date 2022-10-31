"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/relay/processing/v1/paymentmethods/klarna.proto\x12)relay.processing.v1.paymentmethods.klarna\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xc8\x03\n\x14AuthorizeRequestData\x12E\n\x08customer\x18\x01 \x01(\x0b23.relay.processing.v1.paymentmethods.klarna.Customer\x12K\n\x0fbilling_address\x18\x02 \x01(\x0b22.relay.processing.v1.paymentmethods.klarna.Address\x12N\n\rorder_details\x18\x03 \x01(\x0b27.relay.processing.v1.paymentmethods.klarna.OrderDetails\x12V\n\x11acquiring_channel\x18\x04 \x01(\x0e2;.relay.processing.v1.paymentmethods.klarna.AcquiringChannel\x12\x0e\n\x06locale\x18\x05 \x01(\t\x12d\n\x11payment_flow_data\x18d \x01(\x0b2I.relay.processing.v1.paymentmethods.klarna.PaymentFlowRedirectRequestData"\xae\x01\n\x15AuthorizeResponseData\x12e\n\x11payment_flow_data\x18\x01 \x01(\x0b2J.relay.processing.v1.paymentmethods.klarna.PaymentFlowRedirectResponseData\x12.\n\nexpires_at\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xc5\x03\n\x11ChargeRequestData\x12E\n\x08customer\x18\x01 \x01(\x0b23.relay.processing.v1.paymentmethods.klarna.Customer\x12K\n\x0fbilling_address\x18\x02 \x01(\x0b22.relay.processing.v1.paymentmethods.klarna.Address\x12N\n\rorder_details\x18\x03 \x01(\x0b27.relay.processing.v1.paymentmethods.klarna.OrderDetails\x12V\n\x11acquiring_channel\x18\x04 \x01(\x0e2;.relay.processing.v1.paymentmethods.klarna.AcquiringChannel\x12\x0e\n\x06locale\x18\x05 \x01(\t\x12d\n\x11payment_flow_data\x18d \x01(\x0b2I.relay.processing.v1.paymentmethods.klarna.PaymentFlowRedirectRequestData"\xab\x01\n\x12ChargeResponseData\x12e\n\x11payment_flow_data\x18\x01 \x01(\x0b2J.relay.processing.v1.paymentmethods.klarna.PaymentFlowRedirectResponseData\x12.\n\nexpires_at\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xe2\x01\n\x12CaptureRequestData\x12I\n\x0border_items\x18\x01 \x03(\x0b24.relay.processing.v1.paymentmethods.klarna.OrderItem\x121\n\x0bdescription\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x12N\n\rshipping_info\x18\x03 \x03(\x0b27.relay.processing.v1.paymentmethods.klarna.ShippingInfo"\xbd\x03\n\x0cShippingInfo\x12=\n\x17return_shipping_company\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12<\n\x16return_tracking_number\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x129\n\x13return_tracking_uri\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValue\x126\n\x10shipping_company\x18\x04 \x01(\x0b2\x1c.google.protobuf.StringValue\x12R\n\x0fshipping_method\x18\x05 \x01(\x0e29.relay.processing.v1.paymentmethods.klarna.ShippingMethod\x125\n\x0ftracking_number\x18\x06 \x01(\x0b2\x1c.google.protobuf.StringValue\x122\n\x0ctracking_uri\x18\x07 \x01(\x0b2\x1c.google.protobuf.StringValue"\x91\x01\n\x11RefundRequestData\x12I\n\x0border_items\x18\x01 \x03(\x0b24.relay.processing.v1.paymentmethods.klarna.OrderItem\x121\n\x0bdescription\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue"\x9a\x01\n\x08Customer\x12E\n\x08consumer\x18\x01 \x01(\x0b23.relay.processing.v1.paymentmethods.klarna.Consumer\x12G\n\tbussiness\x18\x02 \x01(\x0b24.relay.processing.v1.paymentmethods.klarna.Bussiness"\x95\x02\n\x08Consumer\x123\n\rdate_of_birth\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12,\n\x06gender\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x123\n\rlast_four_ssn\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValue\x12D\n\x1enational_identification_number\x18\x04 \x01(\x0b2\x1c.google.protobuf.StringValue\x12+\n\x05title\x18\x05 \x01(\x0b2\x1c.google.protobuf.StringValue"\xbd\x01\n\tBussiness\x12>\n\x18organization_entity_type\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12B\n\x1corganization_registration_id\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x12,\n\x06vat_id\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValue"\x9c\x05\n\x07Address\x12/\n\tattention\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x12*\n\x04city\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x122\n\x0ccountry_code\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValue\x123\n\remail_address\x18\x04 \x01(\x0b2\x1c.google.protobuf.StringValue\x121\n\x0bfamily_name\x18\x05 \x01(\x0b2\x1c.google.protobuf.StringValue\x120\n\ngiven_name\x18\x06 \x01(\x0b2\x1c.google.protobuf.StringValue\x127\n\x11organization_name\x18\x07 \x01(\x0b2\x1c.google.protobuf.StringValue\x122\n\x0cphone_number\x18\x08 \x01(\x0b2\x1c.google.protobuf.StringValue\x121\n\x0bpostal_code\x18\t \x01(\x0b2\x1c.google.protobuf.StringValue\x12,\n\x06region\x18\n \x01(\x0b2\x1c.google.protobuf.StringValue\x124\n\x0estreet_address\x18\x0b \x01(\x0b2\x1c.google.protobuf.StringValue\x125\n\x0fstreet_address2\x18\x0c \x01(\x0b2\x1c.google.protobuf.StringValue\x12+\n\x05title\x18\r \x01(\x0b2\x1c.google.protobuf.StringValue"\xbd\x01\n\x0cOrderDetails\x12I\n\x0border_items\x18\x01 \x03(\x0b24.relay.processing.v1.paymentmethods.klarna.OrderItem\x12\x14\n\x0ccountry_code\x18\x02 \x01(\t\x12L\n\x10shipping_address\x18\x03 \x01(\x0b22.relay.processing.v1.paymentmethods.klarna.Address"\xdb\x03\n\tOrderItem\x12/\n\timage_url\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x123\n\rmerchant_data\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x12\x0c\n\x04name\x18\x03 \x01(\t\x12X\n\x12product_identifier\x18\x04 \x01(\x0b2<.relay.processing.v1.paymentmethods.klarna.ProductIdentifier\x121\n\x0bproduct_url\x18\x05 \x01(\x0b2\x1c.google.protobuf.StringValue\x12\x10\n\x08quantity\x18\x06 \x01(\x03\x12\x15\n\rquantity_unit\x18\x07 \x01(\t\x12/\n\treference\x18\x08 \x01(\x0b2\x1c.google.protobuf.StringValue\x12\x10\n\x08tax_rate\x18\t \x01(\x03\x12\x1d\n\x15total_discount_amount\x18\n \x01(\x03\x12\x18\n\x10total_tax_amount\x18\x0b \x01(\x03\x12\x12\n\nunit_price\x18\x0c \x01(\x03\x12\x14\n\x0ctotal_amount\x18\r \x01(\x03"\xce\x02\n\x11ProductIdentifier\x12+\n\x05brand\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue\x123\n\rcategory_path\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x12>\n\x18global_trade_item_number\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValue\x12>\n\x18manufacturer_part_number\x18\x04 \x01(\x0b2\x1c.google.protobuf.StringValue\x12+\n\x05color\x18\x05 \x01(\x0b2\x1c.google.protobuf.StringValue\x12*\n\x04size\x18\x06 \x01(\x0b2\x1c.google.protobuf.StringValue"\xa1\x02\n\x1ePaymentFlowRedirectRequestData\x12\x10\n\x08back_url\x18\x01 \x01(\t\x12\x12\n\ncancel_url\x18\x02 \x01(\t\x12\x12\n\nfailed_url\x18\x03 \x01(\t\x12\x13\n\x0bsuccess_url\x18\x04 \x01(\t\x12.\n\x08logo_url\x18\x05 \x01(\x0b2\x1c.google.protobuf.StringValue\x120\n\npage_title\x18\x06 \x01(\x0b2\x1c.google.protobuf.StringValue\x12N\n\rpurchase_type\x18\x07 \x01(\x0e27.relay.processing.v1.paymentmethods.klarna.PurchaseType"7\n\x1fPaymentFlowRedirectResponseData\x12\x14\n\x0capproval_url\x18\x01 \x01(\t*a\n\x0cPurchaseType\x12\x07\n\x03BUY\x10\x00\x12\x08\n\x04RENT\x10\x01\x12\x08\n\x04BOOK\x10\x02\x12\r\n\tSUBSCRIBE\x10\x03\x12\x0c\n\x08DOWNLOAD\x10\x04\x12\t\n\x05ORDER\x10\x05\x12\x0c\n\x08CONTINUE\x10\x06*>\n\x10AcquiringChannel\x12\r\n\tECOMMERCE\x10\x00\x12\x0c\n\x08IN_STORE\x10\x01\x12\r\n\tTELESALES\x10\x02*\xd6\x01\n\x0eShippingMethod\x12\r\n\tUndefined\x10\x00\x12\x0f\n\x0bPickUpStore\x10\x01\x12\x08\n\x04Home\x10\x02\x12\n\n\x06BoxReg\x10\x03\x12\x0c\n\x08BoxUnreg\x10\x04\x12\x0f\n\x0bPickUpPoint\x10\x05\x12\x07\n\x03Own\x10\x06\x12\n\n\x06Postal\x10\x07\x12\x12\n\x0eDHLPackstation\x10\x08\x12\x0b\n\x07Digital\x10\t\x12\x13\n\x0fPickUpWarehouse\x10\n\x12\x10\n\x0cClickCollect\x10\x0b\x12\x12\n\x0ePalletDelivery\x10\x0cBvZHgithub.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1/paymentmethods\xaa\x02)Relay.Processing.V1.PaymentMethods.Klarnab\x06proto3')
_PURCHASETYPE = DESCRIPTOR.enum_types_by_name['PurchaseType']
PurchaseType = enum_type_wrapper.EnumTypeWrapper(_PURCHASETYPE)
_ACQUIRINGCHANNEL = DESCRIPTOR.enum_types_by_name['AcquiringChannel']
AcquiringChannel = enum_type_wrapper.EnumTypeWrapper(_ACQUIRINGCHANNEL)
_SHIPPINGMETHOD = DESCRIPTOR.enum_types_by_name['ShippingMethod']
ShippingMethod = enum_type_wrapper.EnumTypeWrapper(_SHIPPINGMETHOD)
BUY = 0
RENT = 1
BOOK = 2
SUBSCRIBE = 3
DOWNLOAD = 4
ORDER = 5
CONTINUE = 6
ECOMMERCE = 0
IN_STORE = 1
TELESALES = 2
Undefined = 0
PickUpStore = 1
Home = 2
BoxReg = 3
BoxUnreg = 4
PickUpPoint = 5
Own = 6
Postal = 7
DHLPackstation = 8
Digital = 9
PickUpWarehouse = 10
ClickCollect = 11
PalletDelivery = 12
_AUTHORIZEREQUESTDATA = DESCRIPTOR.message_types_by_name['AuthorizeRequestData']
_AUTHORIZERESPONSEDATA = DESCRIPTOR.message_types_by_name['AuthorizeResponseData']
_CHARGEREQUESTDATA = DESCRIPTOR.message_types_by_name['ChargeRequestData']
_CHARGERESPONSEDATA = DESCRIPTOR.message_types_by_name['ChargeResponseData']
_CAPTUREREQUESTDATA = DESCRIPTOR.message_types_by_name['CaptureRequestData']
_SHIPPINGINFO = DESCRIPTOR.message_types_by_name['ShippingInfo']
_REFUNDREQUESTDATA = DESCRIPTOR.message_types_by_name['RefundRequestData']
_CUSTOMER = DESCRIPTOR.message_types_by_name['Customer']
_CONSUMER = DESCRIPTOR.message_types_by_name['Consumer']
_BUSSINESS = DESCRIPTOR.message_types_by_name['Bussiness']
_ADDRESS = DESCRIPTOR.message_types_by_name['Address']
_ORDERDETAILS = DESCRIPTOR.message_types_by_name['OrderDetails']
_ORDERITEM = DESCRIPTOR.message_types_by_name['OrderItem']
_PRODUCTIDENTIFIER = DESCRIPTOR.message_types_by_name['ProductIdentifier']
_PAYMENTFLOWREDIRECTREQUESTDATA = DESCRIPTOR.message_types_by_name['PaymentFlowRedirectRequestData']
_PAYMENTFLOWREDIRECTRESPONSEDATA = DESCRIPTOR.message_types_by_name['PaymentFlowRedirectResponseData']
AuthorizeRequestData = _reflection.GeneratedProtocolMessageType('AuthorizeRequestData', (_message.Message,), {'DESCRIPTOR': _AUTHORIZEREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(AuthorizeRequestData)
AuthorizeResponseData = _reflection.GeneratedProtocolMessageType('AuthorizeResponseData', (_message.Message,), {'DESCRIPTOR': _AUTHORIZERESPONSEDATA, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(AuthorizeResponseData)
ChargeRequestData = _reflection.GeneratedProtocolMessageType('ChargeRequestData', (_message.Message,), {'DESCRIPTOR': _CHARGEREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(ChargeRequestData)
ChargeResponseData = _reflection.GeneratedProtocolMessageType('ChargeResponseData', (_message.Message,), {'DESCRIPTOR': _CHARGERESPONSEDATA, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(ChargeResponseData)
CaptureRequestData = _reflection.GeneratedProtocolMessageType('CaptureRequestData', (_message.Message,), {'DESCRIPTOR': _CAPTUREREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(CaptureRequestData)
ShippingInfo = _reflection.GeneratedProtocolMessageType('ShippingInfo', (_message.Message,), {'DESCRIPTOR': _SHIPPINGINFO, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(ShippingInfo)
RefundRequestData = _reflection.GeneratedProtocolMessageType('RefundRequestData', (_message.Message,), {'DESCRIPTOR': _REFUNDREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(RefundRequestData)
Customer = _reflection.GeneratedProtocolMessageType('Customer', (_message.Message,), {'DESCRIPTOR': _CUSTOMER, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(Customer)
Consumer = _reflection.GeneratedProtocolMessageType('Consumer', (_message.Message,), {'DESCRIPTOR': _CONSUMER, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(Consumer)
Bussiness = _reflection.GeneratedProtocolMessageType('Bussiness', (_message.Message,), {'DESCRIPTOR': _BUSSINESS, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(Bussiness)
Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {'DESCRIPTOR': _ADDRESS, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(Address)
OrderDetails = _reflection.GeneratedProtocolMessageType('OrderDetails', (_message.Message,), {'DESCRIPTOR': _ORDERDETAILS, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(OrderDetails)
OrderItem = _reflection.GeneratedProtocolMessageType('OrderItem', (_message.Message,), {'DESCRIPTOR': _ORDERITEM, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(OrderItem)
ProductIdentifier = _reflection.GeneratedProtocolMessageType('ProductIdentifier', (_message.Message,), {'DESCRIPTOR': _PRODUCTIDENTIFIER, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(ProductIdentifier)
PaymentFlowRedirectRequestData = _reflection.GeneratedProtocolMessageType('PaymentFlowRedirectRequestData', (_message.Message,), {'DESCRIPTOR': _PAYMENTFLOWREDIRECTREQUESTDATA, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(PaymentFlowRedirectRequestData)
PaymentFlowRedirectResponseData = _reflection.GeneratedProtocolMessageType('PaymentFlowRedirectResponseData', (_message.Message,), {'DESCRIPTOR': _PAYMENTFLOWREDIRECTRESPONSEDATA, '__module__': 'relay.processing.v1.paymentmethods.klarna_pb2'})
_sym_db.RegisterMessage(PaymentFlowRedirectResponseData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZHgithub.com/Nedved75/grpcsimple/sdk/go/relay/processing/v1/paymentmethods\xaa\x02)Relay.Processing.V1.PaymentMethods.Klarna'
    _PURCHASETYPE._serialized_start = 4906
    _PURCHASETYPE._serialized_end = 5003
    _ACQUIRINGCHANNEL._serialized_start = 5005
    _ACQUIRINGCHANNEL._serialized_end = 5067
    _SHIPPINGMETHOD._serialized_start = 5070
    _SHIPPINGMETHOD._serialized_end = 5284
    _AUTHORIZEREQUESTDATA._serialized_start = 160
    _AUTHORIZEREQUESTDATA._serialized_end = 616
    _AUTHORIZERESPONSEDATA._serialized_start = 619
    _AUTHORIZERESPONSEDATA._serialized_end = 793
    _CHARGEREQUESTDATA._serialized_start = 796
    _CHARGEREQUESTDATA._serialized_end = 1249
    _CHARGERESPONSEDATA._serialized_start = 1252
    _CHARGERESPONSEDATA._serialized_end = 1423
    _CAPTUREREQUESTDATA._serialized_start = 1426
    _CAPTUREREQUESTDATA._serialized_end = 1652
    _SHIPPINGINFO._serialized_start = 1655
    _SHIPPINGINFO._serialized_end = 2100
    _REFUNDREQUESTDATA._serialized_start = 2103
    _REFUNDREQUESTDATA._serialized_end = 2248
    _CUSTOMER._serialized_start = 2251
    _CUSTOMER._serialized_end = 2405
    _CONSUMER._serialized_start = 2408
    _CONSUMER._serialized_end = 2685
    _BUSSINESS._serialized_start = 2688
    _BUSSINESS._serialized_end = 2877
    _ADDRESS._serialized_start = 2880
    _ADDRESS._serialized_end = 3548
    _ORDERDETAILS._serialized_start = 3551
    _ORDERDETAILS._serialized_end = 3740
    _ORDERITEM._serialized_start = 3743
    _ORDERITEM._serialized_end = 4218
    _PRODUCTIDENTIFIER._serialized_start = 4221
    _PRODUCTIDENTIFIER._serialized_end = 4555
    _PAYMENTFLOWREDIRECTREQUESTDATA._serialized_start = 4558
    _PAYMENTFLOWREDIRECTREQUESTDATA._serialized_end = 4847
    _PAYMENTFLOWREDIRECTRESPONSEDATA._serialized_start = 4849
    _PAYMENTFLOWREDIRECTRESPONSEDATA._serialized_end = 4904