# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/resources/third_party_app_analytics_link.proto
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
  name='google/ads/googleads/v7/resources/third_party_app_analytics_link.proto',
  package='google.ads.googleads.v7.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v7.resourcesB\037ThirdPartyAppAnalyticsLinkProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V7.Resources\312\002!Google\\Ads\\GoogleAds\\V7\\Resources\352\002%Google::Ads::GoogleAds::V7::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nFgoogle/ads/googleads/v7/resources/third_party_app_analytics_link.proto\x12!google.ads.googleads.v7.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xcf\x02\n\x1aThirdPartyAppAnalyticsLink\x12\x61\n\rresource_name\x18\x01 \x01(\tB<\xe2\x41\x01\x05\xfa\x41\x35\n3googleads.googleapis.com/ThirdPartyAppAnalyticsLinkR\x0cresourceName\x12\x35\n\x11shareable_link_id\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03H\x00R\x0fshareableLinkId\x88\x01\x01:\x80\x01\xea\x41}\n3googleads.googleapis.com/ThirdPartyAppAnalyticsLink\x12\x46\x63ustomers/{customer_id}/thirdPartyAppAnalyticsLinks/{customer_link_id}B\x14\n\x12_shareable_link_idB\x8c\x02\n%com.google.ads.googleads.v7.resourcesB\x1fThirdPartyAppAnalyticsLinkProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V7.Resources\xca\x02!Google\\Ads\\GoogleAds\\V7\\Resources\xea\x02%Google::Ads::GoogleAds::V7::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_THIRDPARTYAPPANALYTICSLINK = _descriptor.Descriptor(
  name='ThirdPartyAppAnalyticsLink',
  full_name='google.ads.googleads.v7.resources.ThirdPartyAppAnalyticsLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v7.resources.ThirdPartyAppAnalyticsLink.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A5\n3googleads.googleapis.com/ThirdPartyAppAnalyticsLink', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shareable_link_id', full_name='google.ads.googleads.v7.resources.ThirdPartyAppAnalyticsLink.shareable_link_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='shareableLinkId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A}\n3googleads.googleapis.com/ThirdPartyAppAnalyticsLink\022Fcustomers/{customer_id}/thirdPartyAppAnalyticsLinks/{customer_link_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_shareable_link_id', full_name='google.ads.googleads.v7.resources.ThirdPartyAppAnalyticsLink._shareable_link_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=200,
  serialized_end=535,
)

_THIRDPARTYAPPANALYTICSLINK.oneofs_by_name['_shareable_link_id'].fields.append(
  _THIRDPARTYAPPANALYTICSLINK.fields_by_name['shareable_link_id'])
_THIRDPARTYAPPANALYTICSLINK.fields_by_name['shareable_link_id'].containing_oneof = _THIRDPARTYAPPANALYTICSLINK.oneofs_by_name['_shareable_link_id']
DESCRIPTOR.message_types_by_name['ThirdPartyAppAnalyticsLink'] = _THIRDPARTYAPPANALYTICSLINK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ThirdPartyAppAnalyticsLink = _reflection.GeneratedProtocolMessageType('ThirdPartyAppAnalyticsLink', (_message.Message,), {
  'DESCRIPTOR' : _THIRDPARTYAPPANALYTICSLINK,
  '__module__' : 'google.ads.googleads.v7.resources.third_party_app_analytics_link_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.resources.ThirdPartyAppAnalyticsLink)
  })
_sym_db.RegisterMessage(ThirdPartyAppAnalyticsLink)


DESCRIPTOR._options = None
_THIRDPARTYAPPANALYTICSLINK.fields_by_name['resource_name']._options = None
_THIRDPARTYAPPANALYTICSLINK.fields_by_name['shareable_link_id']._options = None
_THIRDPARTYAPPANALYTICSLINK._options = None
# @@protoc_insertion_point(module_scope)
