# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/services/extension_feed_item_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_response__content__type__pb2
from google.ads.googleads.v7.resources import extension_feed_item_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_extension__feed__item__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v7/services/extension_feed_item_service.proto',
  package='google.ads.googleads.v7.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v7.servicesB\035ExtensionFeedItemServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V7.Services\312\002 Google\\Ads\\GoogleAds\\V7\\Services\352\002$Google::Ads::GoogleAds::V7::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nBgoogle/ads/googleads/v7/services/extension_feed_item_service.proto\x12 google.ads.googleads.v7.services\x1a\x39google/ads/googleads/v7/enums/response_content_type.proto\x1a;google/ads/googleads/v7/resources/extension_feed_item.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"w\n\x1bGetExtensionFeedItemRequest\x12X\n\rresource_name\x18\x01 \x01(\tB3\xe2\x41\x01\x02\xfa\x41,\n*googleads.googleapis.com/ExtensionFeedItemR\x0cresourceName\"\xfa\x02\n\x1fMutateExtensionFeedItemsRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12\x62\n\noperations\x18\x02 \x03(\x0b\x32<.google.ads.googleads.v7.services.ExtensionFeedItemOperationB\x04\xe2\x41\x01\x02R\noperations\x12\'\n\x0fpartial_failure\x18\x03 \x01(\x08R\x0epartialFailure\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\x12~\n\x15response_content_type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v7.enums.ResponseContentTypeEnum.ResponseContentTypeR\x13responseContentType\"\xa0\x02\n\x1a\x45xtensionFeedItemOperation\x12;\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12N\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x34.google.ads.googleads.v7.resources.ExtensionFeedItemH\x00R\x06\x63reate\x12N\n\x06update\x18\x02 \x01(\x0b\x32\x34.google.ads.googleads.v7.resources.ExtensionFeedItemH\x00R\x06update\x12\x18\n\x06remove\x18\x03 \x01(\tH\x00R\x06removeB\x0b\n\toperation\"\xc5\x01\n MutateExtensionFeedItemsResponse\x12\x46\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x13partialFailureError\x12Y\n\x07results\x18\x02 \x03(\x0b\x32?.google.ads.googleads.v7.services.MutateExtensionFeedItemResultR\x07results\"\xaa\x01\n\x1dMutateExtensionFeedItemResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName\x12\x64\n\x13\x65xtension_feed_item\x18\x02 \x01(\x0b\x32\x34.google.ads.googleads.v7.resources.ExtensionFeedItemR\x11\x65xtensionFeedItem2\xbe\x04\n\x18\x45xtensionFeedItemService\x12\xd9\x01\n\x14GetExtensionFeedItem\x12=.google.ads.googleads.v7.services.GetExtensionFeedItemRequest\x1a\x34.google.ads.googleads.v7.resources.ExtensionFeedItem\"L\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x36\x12\x34/v7/{resource_name=customers/*/extensionFeedItems/*}\x12\xfe\x01\n\x18MutateExtensionFeedItems\x12\x41.google.ads.googleads.v7.services.MutateExtensionFeedItemsRequest\x1a\x42.google.ads.googleads.v7.services.MutateExtensionFeedItemsResponse\"[\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02<\"7/v7/customers/{customer_id=*}/extensionFeedItems:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x84\x02\n$com.google.ads.googleads.v7.servicesB\x1d\x45xtensionFeedItemServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V7.Services\xca\x02 Google\\Ads\\GoogleAds\\V7\\Services\xea\x02$Google::Ads::GoogleAds::V7::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_response__content__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_extension__feed__item__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETEXTENSIONFEEDITEMREQUEST = _descriptor.Descriptor(
  name='GetExtensionFeedItemRequest',
  full_name='google.ads.googleads.v7.services.GetExtensionFeedItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v7.services.GetExtensionFeedItemRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A,\n*googleads.googleapis.com/ExtensionFeedItem', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=398,
  serialized_end=517,
)


_MUTATEEXTENSIONFEEDITEMSREQUEST = _descriptor.Descriptor(
  name='MutateExtensionFeedItemsRequest',
  full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='customerId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='operations', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='partialFailure', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='validateOnly', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_content_type', full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemsRequest.response_content_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='responseContentType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=520,
  serialized_end=898,
)


_EXTENSIONFEEDITEMOPERATION = _descriptor.Descriptor(
  name='ExtensionFeedItemOperation',
  full_name='google.ads.googleads.v7.services.ExtensionFeedItemOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v7.services.ExtensionFeedItemOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='updateMask', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v7.services.ExtensionFeedItemOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='create', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v7.services.ExtensionFeedItemOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='update', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v7.services.ExtensionFeedItemOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='remove', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v7.services.ExtensionFeedItemOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=901,
  serialized_end=1189,
)


_MUTATEEXTENSIONFEEDITEMSRESPONSE = _descriptor.Descriptor(
  name='MutateExtensionFeedItemsResponse',
  full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='partialFailureError', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='results', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1192,
  serialized_end=1389,
)


_MUTATEEXTENSIONFEEDITEMRESULT = _descriptor.Descriptor(
  name='MutateExtensionFeedItemResult',
  full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension_feed_item', full_name='google.ads.googleads.v7.services.MutateExtensionFeedItemResult.extension_feed_item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='extensionFeedItem', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1392,
  serialized_end=1562,
)

_MUTATEEXTENSIONFEEDITEMSREQUEST.fields_by_name['operations'].message_type = _EXTENSIONFEEDITEMOPERATION
_MUTATEEXTENSIONFEEDITEMSREQUEST.fields_by_name['response_content_type'].enum_type = google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_response__content__type__pb2._RESPONSECONTENTTYPEENUM_RESPONSECONTENTTYPE
_EXTENSIONFEEDITEMOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_EXTENSIONFEEDITEMOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_extension__feed__item__pb2._EXTENSIONFEEDITEM
_EXTENSIONFEEDITEMOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_extension__feed__item__pb2._EXTENSIONFEEDITEM
_EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation'].fields.append(
  _EXTENSIONFEEDITEMOPERATION.fields_by_name['create'])
_EXTENSIONFEEDITEMOPERATION.fields_by_name['create'].containing_oneof = _EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation']
_EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation'].fields.append(
  _EXTENSIONFEEDITEMOPERATION.fields_by_name['update'])
_EXTENSIONFEEDITEMOPERATION.fields_by_name['update'].containing_oneof = _EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation']
_EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation'].fields.append(
  _EXTENSIONFEEDITEMOPERATION.fields_by_name['remove'])
_EXTENSIONFEEDITEMOPERATION.fields_by_name['remove'].containing_oneof = _EXTENSIONFEEDITEMOPERATION.oneofs_by_name['operation']
_MUTATEEXTENSIONFEEDITEMSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEEXTENSIONFEEDITEMSRESPONSE.fields_by_name['results'].message_type = _MUTATEEXTENSIONFEEDITEMRESULT
_MUTATEEXTENSIONFEEDITEMRESULT.fields_by_name['extension_feed_item'].message_type = google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_extension__feed__item__pb2._EXTENSIONFEEDITEM
DESCRIPTOR.message_types_by_name['GetExtensionFeedItemRequest'] = _GETEXTENSIONFEEDITEMREQUEST
DESCRIPTOR.message_types_by_name['MutateExtensionFeedItemsRequest'] = _MUTATEEXTENSIONFEEDITEMSREQUEST
DESCRIPTOR.message_types_by_name['ExtensionFeedItemOperation'] = _EXTENSIONFEEDITEMOPERATION
DESCRIPTOR.message_types_by_name['MutateExtensionFeedItemsResponse'] = _MUTATEEXTENSIONFEEDITEMSRESPONSE
DESCRIPTOR.message_types_by_name['MutateExtensionFeedItemResult'] = _MUTATEEXTENSIONFEEDITEMRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetExtensionFeedItemRequest = _reflection.GeneratedProtocolMessageType('GetExtensionFeedItemRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEXTENSIONFEEDITEMREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.extension_feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.GetExtensionFeedItemRequest)
  })
_sym_db.RegisterMessage(GetExtensionFeedItemRequest)

MutateExtensionFeedItemsRequest = _reflection.GeneratedProtocolMessageType('MutateExtensionFeedItemsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEEXTENSIONFEEDITEMSREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.extension_feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateExtensionFeedItemsRequest)
  })
_sym_db.RegisterMessage(MutateExtensionFeedItemsRequest)

ExtensionFeedItemOperation = _reflection.GeneratedProtocolMessageType('ExtensionFeedItemOperation', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONFEEDITEMOPERATION,
  '__module__' : 'google.ads.googleads.v7.services.extension_feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.ExtensionFeedItemOperation)
  })
_sym_db.RegisterMessage(ExtensionFeedItemOperation)

MutateExtensionFeedItemsResponse = _reflection.GeneratedProtocolMessageType('MutateExtensionFeedItemsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEEXTENSIONFEEDITEMSRESPONSE,
  '__module__' : 'google.ads.googleads.v7.services.extension_feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateExtensionFeedItemsResponse)
  })
_sym_db.RegisterMessage(MutateExtensionFeedItemsResponse)

MutateExtensionFeedItemResult = _reflection.GeneratedProtocolMessageType('MutateExtensionFeedItemResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEEXTENSIONFEEDITEMRESULT,
  '__module__' : 'google.ads.googleads.v7.services.extension_feed_item_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateExtensionFeedItemResult)
  })
_sym_db.RegisterMessage(MutateExtensionFeedItemResult)


DESCRIPTOR._options = None
_GETEXTENSIONFEEDITEMREQUEST.fields_by_name['resource_name']._options = None
_MUTATEEXTENSIONFEEDITEMSREQUEST.fields_by_name['customer_id']._options = None
_MUTATEEXTENSIONFEEDITEMSREQUEST.fields_by_name['operations']._options = None

_EXTENSIONFEEDITEMSERVICE = _descriptor.ServiceDescriptor(
  name='ExtensionFeedItemService',
  full_name='google.ads.googleads.v7.services.ExtensionFeedItemService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords',
  create_key=_descriptor._internal_create_key,
  serialized_start=1565,
  serialized_end=2139,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetExtensionFeedItem',
    full_name='google.ads.googleads.v7.services.ExtensionFeedItemService.GetExtensionFeedItem',
    index=0,
    containing_service=None,
    input_type=_GETEXTENSIONFEEDITEMREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_extension__feed__item__pb2._EXTENSIONFEEDITEM,
    serialized_options=b'\332A\rresource_name\202\323\344\223\0026\0224/v7/{resource_name=customers/*/extensionFeedItems/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MutateExtensionFeedItems',
    full_name='google.ads.googleads.v7.services.ExtensionFeedItemService.MutateExtensionFeedItems',
    index=1,
    containing_service=None,
    input_type=_MUTATEEXTENSIONFEEDITEMSREQUEST,
    output_type=_MUTATEEXTENSIONFEEDITEMSRESPONSE,
    serialized_options=b'\332A\026customer_id,operations\202\323\344\223\002<\"7/v7/customers/{customer_id=*}/extensionFeedItems:mutate:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXTENSIONFEEDITEMSERVICE)

DESCRIPTOR.services_by_name['ExtensionFeedItemService'] = _EXTENSIONFEEDITEMSERVICE

# @@protoc_insertion_point(module_scope)
