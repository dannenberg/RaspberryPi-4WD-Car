# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/enums/response_content_type.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/enums/response_content_type.proto',
  package='google.ads.googleads.v9.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v9.enumsB\030ResponseContentTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V9.Enums\312\002\035Google\\Ads\\GoogleAds\\V9\\Enums\352\002!Google::Ads::GoogleAds::V9::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9google/ads/googleads/v9/enums/response_content_type.proto\x12\x1dgoogle.ads.googleads.v9.enums\x1a\x1cgoogle/api/annotations.proto\"o\n\x17ResponseContentTypeEnum\"T\n\x13ResponseContentType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x16\n\x12RESOURCE_NAME_ONLY\x10\x01\x12\x14\n\x10MUTABLE_RESOURCE\x10\x02\x42\xed\x01\n!com.google.ads.googleads.v9.enumsB\x18ResponseContentTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V9.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V9\\Enums\xea\x02!Google::Ads::GoogleAds::V9::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_RESPONSECONTENTTYPEENUM_RESPONSECONTENTTYPE = _descriptor.EnumDescriptor(
  name='ResponseContentType',
  full_name='google.ads.googleads.v9.enums.ResponseContentTypeEnum.ResponseContentType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_NAME_ONLY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MUTABLE_RESOURCE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=149,
  serialized_end=233,
)
_sym_db.RegisterEnumDescriptor(_RESPONSECONTENTTYPEENUM_RESPONSECONTENTTYPE)


_RESPONSECONTENTTYPEENUM = _descriptor.Descriptor(
  name='ResponseContentTypeEnum',
  full_name='google.ads.googleads.v9.enums.ResponseContentTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSECONTENTTYPEENUM_RESPONSECONTENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=233,
)

_RESPONSECONTENTTYPEENUM_RESPONSECONTENTTYPE.containing_type = _RESPONSECONTENTTYPEENUM
DESCRIPTOR.message_types_by_name['ResponseContentTypeEnum'] = _RESPONSECONTENTTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseContentTypeEnum = _reflection.GeneratedProtocolMessageType('ResponseContentTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSECONTENTTYPEENUM,
  '__module__' : 'google.ads.googleads.v9.enums.response_content_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.enums.ResponseContentTypeEnum)
  })
_sym_db.RegisterMessage(ResponseContentTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
