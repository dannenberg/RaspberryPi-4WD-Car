# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/enums/app_placeholder_field.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/enums/app_placeholder_field.proto',
  package='google.ads.googleads.v9.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v9.enumsB\030AppPlaceholderFieldProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V9.Enums\312\002\035Google\\Ads\\GoogleAds\\V9\\Enums\352\002!Google::Ads::GoogleAds::V9::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9google/ads/googleads/v9/enums/app_placeholder_field.proto\x12\x1dgoogle.ads.googleads.v9.enums\x1a\x1cgoogle/api/annotations.proto\"\xc9\x01\n\x17\x41ppPlaceholderFieldEnum\"\xad\x01\n\x13\x41ppPlaceholderField\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\t\n\x05STORE\x10\x02\x12\x06\n\x02ID\x10\x03\x12\r\n\tLINK_TEXT\x10\x04\x12\x07\n\x03URL\x10\x05\x12\x0e\n\nFINAL_URLS\x10\x06\x12\x15\n\x11\x46INAL_MOBILE_URLS\x10\x07\x12\x10\n\x0cTRACKING_URL\x10\x08\x12\x14\n\x10\x46INAL_URL_SUFFIX\x10\tB\xed\x01\n!com.google.ads.googleads.v9.enumsB\x18\x41ppPlaceholderFieldProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V9.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V9\\Enums\xea\x02!Google::Ads::GoogleAds::V9::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_APPPLACEHOLDERFIELDENUM_APPPLACEHOLDERFIELD = _descriptor.EnumDescriptor(
  name='AppPlaceholderField',
  full_name='google.ads.googleads.v9.enums.AppPlaceholderFieldEnum.AppPlaceholderField',
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
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STORE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ID', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LINK_TEXT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='URL', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINAL_URLS', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINAL_MOBILE_URLS', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRACKING_URL', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINAL_URL_SUFFIX', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=151,
  serialized_end=324,
)
_sym_db.RegisterEnumDescriptor(_APPPLACEHOLDERFIELDENUM_APPPLACEHOLDERFIELD)


_APPPLACEHOLDERFIELDENUM = _descriptor.Descriptor(
  name='AppPlaceholderFieldEnum',
  full_name='google.ads.googleads.v9.enums.AppPlaceholderFieldEnum',
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
    _APPPLACEHOLDERFIELDENUM_APPPLACEHOLDERFIELD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=324,
)

_APPPLACEHOLDERFIELDENUM_APPPLACEHOLDERFIELD.containing_type = _APPPLACEHOLDERFIELDENUM
DESCRIPTOR.message_types_by_name['AppPlaceholderFieldEnum'] = _APPPLACEHOLDERFIELDENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppPlaceholderFieldEnum = _reflection.GeneratedProtocolMessageType('AppPlaceholderFieldEnum', (_message.Message,), {
  'DESCRIPTOR' : _APPPLACEHOLDERFIELDENUM,
  '__module__' : 'google.ads.googleads.v9.enums.app_placeholder_field_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.enums.AppPlaceholderFieldEnum)
  })
_sym_db.RegisterMessage(AppPlaceholderFieldEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
