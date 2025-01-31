# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/services/asset_field_type_view_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.resources import asset_field_type_view_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_asset__field__type__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v8/services/asset_field_type_view_service.proto',
  package='google.ads.googleads.v8.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v8.servicesB\036AssetFieldTypeViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V8.Services\312\002 Google\\Ads\\GoogleAds\\V8\\Services\352\002$Google::Ads::GoogleAds::V8::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDgoogle/ads/googleads/v8/services/asset_field_type_view_service.proto\x12 google.ads.googleads.v8.services\x1a=google/ads/googleads/v8/resources/asset_field_type_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"y\n\x1cGetAssetFieldTypeViewRequest\x12Y\n\rresource_name\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+googleads.googleapis.com/AssetFieldTypeViewR\x0cresourceName2\xc2\x02\n\x19\x41ssetFieldTypeViewService\x12\xdd\x01\n\x15GetAssetFieldTypeView\x12>.google.ads.googleads.v8.services.GetAssetFieldTypeViewRequest\x1a\x35.google.ads.googleads.v8.resources.AssetFieldTypeView\"M\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x37\x12\x35/v8/{resource_name=customers/*/assetFieldTypeViews/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x85\x02\n$com.google.ads.googleads.v8.servicesB\x1e\x41ssetFieldTypeViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V8.Services\xca\x02 Google\\Ads\\GoogleAds\\V8\\Services\xea\x02$Google::Ads::GoogleAds::V8::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_asset__field__type__view__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETASSETFIELDTYPEVIEWREQUEST = _descriptor.Descriptor(
  name='GetAssetFieldTypeViewRequest',
  full_name='google.ads.googleads.v8.services.GetAssetFieldTypeViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v8.services.GetAssetFieldTypeViewRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A-\n+googleads.googleapis.com/AssetFieldTypeView', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=284,
  serialized_end=405,
)

DESCRIPTOR.message_types_by_name['GetAssetFieldTypeViewRequest'] = _GETASSETFIELDTYPEVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAssetFieldTypeViewRequest = _reflection.GeneratedProtocolMessageType('GetAssetFieldTypeViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETASSETFIELDTYPEVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v8.services.asset_field_type_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.GetAssetFieldTypeViewRequest)
  })
_sym_db.RegisterMessage(GetAssetFieldTypeViewRequest)


DESCRIPTOR._options = None
_GETASSETFIELDTYPEVIEWREQUEST.fields_by_name['resource_name']._options = None

_ASSETFIELDTYPEVIEWSERVICE = _descriptor.ServiceDescriptor(
  name='AssetFieldTypeViewService',
  full_name='google.ads.googleads.v8.services.AssetFieldTypeViewService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords',
  create_key=_descriptor._internal_create_key,
  serialized_start=408,
  serialized_end=730,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAssetFieldTypeView',
    full_name='google.ads.googleads.v8.services.AssetFieldTypeViewService.GetAssetFieldTypeView',
    index=0,
    containing_service=None,
    input_type=_GETASSETFIELDTYPEVIEWREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_asset__field__type__view__pb2._ASSETFIELDTYPEVIEW,
    serialized_options=b'\332A\rresource_name\202\323\344\223\0027\0225/v8/{resource_name=customers/*/assetFieldTypeViews/*}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ASSETFIELDTYPEVIEWSERVICE)

DESCRIPTOR.services_by_name['AssetFieldTypeViewService'] = _ASSETFIELDTYPEVIEWSERVICE

# @@protoc_insertion_point(module_scope)
