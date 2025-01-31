# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/landing_page_view.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/resources/landing_page_view.proto',
  package='google.ads.googleads.v9.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v9.resourcesB\024LandingPageViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9google/ads/googleads/v9/resources/landing_page_view.proto\x12!google.ads.googleads.v9.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xbb\x02\n\x0fLandingPageView\x12V\n\rresource_name\x18\x01 \x01(\tB1\xe2\x41\x01\x03\xfa\x41*\n(googleads.googleapis.com/LandingPageViewR\x0cresourceName\x12;\n\x14unexpanded_final_url\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03H\x00R\x12unexpandedFinalUrl\x88\x01\x01:z\xea\x41w\n(googleads.googleapis.com/LandingPageView\x12Kcustomers/{customer_id}/landingPageViews/{unexpanded_final_url_fingerprint}B\x17\n\x15_unexpanded_final_urlB\x81\x02\n%com.google.ads.googleads.v9.resourcesB\x14LandingPageViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_LANDINGPAGEVIEW = _descriptor.Descriptor(
  name='LandingPageView',
  full_name='google.ads.googleads.v9.resources.LandingPageView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v9.resources.LandingPageView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003\372A*\n(googleads.googleapis.com/LandingPageView', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unexpanded_final_url', full_name='google.ads.googleads.v9.resources.LandingPageView.unexpanded_final_url', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='unexpandedFinalUrl', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Aw\n(googleads.googleapis.com/LandingPageView\022Kcustomers/{customer_id}/landingPageViews/{unexpanded_final_url_fingerprint}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_unexpanded_final_url', full_name='google.ads.googleads.v9.resources.LandingPageView._unexpanded_final_url',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=187,
  serialized_end=502,
)

_LANDINGPAGEVIEW.oneofs_by_name['_unexpanded_final_url'].fields.append(
  _LANDINGPAGEVIEW.fields_by_name['unexpanded_final_url'])
_LANDINGPAGEVIEW.fields_by_name['unexpanded_final_url'].containing_oneof = _LANDINGPAGEVIEW.oneofs_by_name['_unexpanded_final_url']
DESCRIPTOR.message_types_by_name['LandingPageView'] = _LANDINGPAGEVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LandingPageView = _reflection.GeneratedProtocolMessageType('LandingPageView', (_message.Message,), {
  'DESCRIPTOR' : _LANDINGPAGEVIEW,
  '__module__' : 'google.ads.googleads.v9.resources.landing_page_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.LandingPageView)
  })
_sym_db.RegisterMessage(LandingPageView)


DESCRIPTOR._options = None
_LANDINGPAGEVIEW.fields_by_name['resource_name']._options = None
_LANDINGPAGEVIEW.fields_by_name['unexpanded_final_url']._options = None
_LANDINGPAGEVIEW._options = None
# @@protoc_insertion_point(module_scope)
