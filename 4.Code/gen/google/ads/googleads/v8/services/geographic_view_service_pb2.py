# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/services/geographic_view_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.resources import geographic_view_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_geographic__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v8/services/geographic_view_service.proto',
  package='google.ads.googleads.v8.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v8.servicesB\032GeographicViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V8.Services\312\002 Google\\Ads\\GoogleAds\\V8\\Services\352\002$Google::Ads::GoogleAds::V8::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>google/ads/googleads/v8/services/geographic_view_service.proto\x12 google.ads.googleads.v8.services\x1a\x37google/ads/googleads/v8/resources/geographic_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"q\n\x18GetGeographicViewRequest\x12U\n\rresource_name\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\n\'googleads.googleapis.com/GeographicViewR\x0cresourceName2\xae\x02\n\x15GeographicViewService\x12\xcd\x01\n\x11GetGeographicView\x12:.google.ads.googleads.v8.services.GetGeographicViewRequest\x1a\x31.google.ads.googleads.v8.resources.GeographicView\"I\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x33\x12\x31/v8/{resource_name=customers/*/geographicViews/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x81\x02\n$com.google.ads.googleads.v8.servicesB\x1aGeographicViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V8.Services\xca\x02 Google\\Ads\\GoogleAds\\V8\\Services\xea\x02$Google::Ads::GoogleAds::V8::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_geographic__view__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETGEOGRAPHICVIEWREQUEST = _descriptor.Descriptor(
  name='GetGeographicViewRequest',
  full_name='google.ads.googleads.v8.services.GetGeographicViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v8.services.GetGeographicViewRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A)\n\'googleads.googleapis.com/GeographicView', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=272,
  serialized_end=385,
)

DESCRIPTOR.message_types_by_name['GetGeographicViewRequest'] = _GETGEOGRAPHICVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetGeographicViewRequest = _reflection.GeneratedProtocolMessageType('GetGeographicViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGEOGRAPHICVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v8.services.geographic_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.GetGeographicViewRequest)
  })
_sym_db.RegisterMessage(GetGeographicViewRequest)


DESCRIPTOR._options = None
_GETGEOGRAPHICVIEWREQUEST.fields_by_name['resource_name']._options = None

_GEOGRAPHICVIEWSERVICE = _descriptor.ServiceDescriptor(
  name='GeographicViewService',
  full_name='google.ads.googleads.v8.services.GeographicViewService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords',
  create_key=_descriptor._internal_create_key,
  serialized_start=388,
  serialized_end=690,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetGeographicView',
    full_name='google.ads.googleads.v8.services.GeographicViewService.GetGeographicView',
    index=0,
    containing_service=None,
    input_type=_GETGEOGRAPHICVIEWREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_geographic__view__pb2._GEOGRAPHICVIEW,
    serialized_options=b'\332A\rresource_name\202\323\344\223\0023\0221/v8/{resource_name=customers/*/geographicViews/*}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GEOGRAPHICVIEWSERVICE)

DESCRIPTOR.services_by_name['GeographicViewService'] = _GEOGRAPHICVIEWSERVICE

# @@protoc_insertion_point(module_scope)
