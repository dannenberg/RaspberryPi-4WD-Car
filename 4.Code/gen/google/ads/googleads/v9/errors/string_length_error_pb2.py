# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/string_length_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/errors/string_length_error.proto',
  package='google.ads.googleads.v9.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v9.errorsB\026StringLengthErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/ads/googleads/v9/errors/string_length_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"r\n\x15StringLengthErrorEnum\"Y\n\x11StringLengthError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\t\n\x05\x45MPTY\x10\x04\x12\r\n\tTOO_SHORT\x10\x02\x12\x0c\n\x08TOO_LONG\x10\x03\x42\xf1\x01\n\"com.google.ads.googleads.v9.errorsB\x16StringLengthErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_STRINGLENGTHERRORENUM_STRINGLENGTHERROR = _descriptor.EnumDescriptor(
  name='StringLengthError',
  full_name='google.ads.googleads.v9.errors.StringLengthErrorEnum.StringLengthError',
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
      name='EMPTY', index=2, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_SHORT', index=3, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_LONG', index=4, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=147,
  serialized_end=236,
)
_sym_db.RegisterEnumDescriptor(_STRINGLENGTHERRORENUM_STRINGLENGTHERROR)


_STRINGLENGTHERRORENUM = _descriptor.Descriptor(
  name='StringLengthErrorEnum',
  full_name='google.ads.googleads.v9.errors.StringLengthErrorEnum',
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
    _STRINGLENGTHERRORENUM_STRINGLENGTHERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=236,
)

_STRINGLENGTHERRORENUM_STRINGLENGTHERROR.containing_type = _STRINGLENGTHERRORENUM
DESCRIPTOR.message_types_by_name['StringLengthErrorEnum'] = _STRINGLENGTHERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StringLengthErrorEnum = _reflection.GeneratedProtocolMessageType('StringLengthErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _STRINGLENGTHERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.string_length_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.StringLengthErrorEnum)
  })
_sym_db.RegisterMessage(StringLengthErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
