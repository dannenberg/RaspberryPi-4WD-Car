# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/conversion_custom_variable_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/errors/conversion_custom_variable_error.proto',
  package='google.ads.googleads.v9.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v9.errorsB\"ConversionCustomVariableErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nEgoogle/ads/googleads/v9/errors/conversion_custom_variable_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"\x89\x01\n!ConversionCustomVariableErrorEnum\"d\n\x1d\x43onversionCustomVariableError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x12\n\x0e\x44UPLICATE_NAME\x10\x02\x12\x11\n\rDUPLICATE_TAG\x10\x03\x42\xfd\x01\n\"com.google.ads.googleads.v9.errorsB\"ConversionCustomVariableErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CONVERSIONCUSTOMVARIABLEERRORENUM_CONVERSIONCUSTOMVARIABLEERROR = _descriptor.EnumDescriptor(
  name='ConversionCustomVariableError',
  full_name='google.ads.googleads.v9.errors.ConversionCustomVariableErrorEnum.ConversionCustomVariableError',
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
      name='DUPLICATE_NAME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_TAG', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=173,
  serialized_end=273,
)
_sym_db.RegisterEnumDescriptor(_CONVERSIONCUSTOMVARIABLEERRORENUM_CONVERSIONCUSTOMVARIABLEERROR)


_CONVERSIONCUSTOMVARIABLEERRORENUM = _descriptor.Descriptor(
  name='ConversionCustomVariableErrorEnum',
  full_name='google.ads.googleads.v9.errors.ConversionCustomVariableErrorEnum',
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
    _CONVERSIONCUSTOMVARIABLEERRORENUM_CONVERSIONCUSTOMVARIABLEERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=273,
)

_CONVERSIONCUSTOMVARIABLEERRORENUM_CONVERSIONCUSTOMVARIABLEERROR.containing_type = _CONVERSIONCUSTOMVARIABLEERRORENUM
DESCRIPTOR.message_types_by_name['ConversionCustomVariableErrorEnum'] = _CONVERSIONCUSTOMVARIABLEERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConversionCustomVariableErrorEnum = _reflection.GeneratedProtocolMessageType('ConversionCustomVariableErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSIONCUSTOMVARIABLEERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.conversion_custom_variable_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.ConversionCustomVariableErrorEnum)
  })
_sym_db.RegisterMessage(ConversionCustomVariableErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
