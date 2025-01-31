# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/gender_view.proto
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
  name='google/ads/googleads/v9/resources/gender_view.proto',
  package='google.ads.googleads.v9.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v9.resourcesB\017GenderViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3google/ads/googleads/v9/resources/gender_view.proto\x12!google.ads.googleads.v9.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xcb\x01\n\nGenderView\x12Q\n\rresource_name\x18\x01 \x01(\tB,\xe2\x41\x01\x03\xfa\x41%\n#googleads.googleapis.com/GenderViewR\x0cresourceName:j\xea\x41g\n#googleads.googleapis.com/GenderView\x12@customers/{customer_id}/genderViews/{ad_group_id}~{criterion_id}B\xfc\x01\n%com.google.ads.googleads.v9.resourcesB\x0fGenderViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GENDERVIEW = _descriptor.Descriptor(
  name='GenderView',
  full_name='google.ads.googleads.v9.resources.GenderView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v9.resources.GenderView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003\372A%\n#googleads.googleapis.com/GenderView', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Ag\n#googleads.googleapis.com/GenderView\022@customers/{customer_id}/genderViews/{ad_group_id}~{criterion_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=384,
)

DESCRIPTOR.message_types_by_name['GenderView'] = _GENDERVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenderView = _reflection.GeneratedProtocolMessageType('GenderView', (_message.Message,), {
  'DESCRIPTOR' : _GENDERVIEW,
  '__module__' : 'google.ads.googleads.v9.resources.gender_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.GenderView)
  })
_sym_db.RegisterMessage(GenderView)


DESCRIPTOR._options = None
_GENDERVIEW.fields_by_name['resource_name']._options = None
_GENDERVIEW._options = None
# @@protoc_insertion_point(module_scope)
