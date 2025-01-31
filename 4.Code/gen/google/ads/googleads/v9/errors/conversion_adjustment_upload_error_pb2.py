# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/conversion_adjustment_upload_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/errors/conversion_adjustment_upload_error.proto',
  package='google.ads.googleads.v9.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v9.errorsB$ConversionAdjustmentUploadErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nGgoogle/ads/googleads/v9/errors/conversion_adjustment_upload_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"\xca\x06\n#ConversionAdjustmentUploadErrorEnum\"\xa2\x06\n\x1f\x43onversionAdjustmentUploadError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12 \n\x1cTOO_RECENT_CONVERSION_ACTION\x10\x02\x12\x1d\n\x19INVALID_CONVERSION_ACTION\x10\x03\x12 \n\x1c\x43ONVERSION_ALREADY_RETRACTED\x10\x04\x12\x18\n\x14\x43ONVERSION_NOT_FOUND\x10\x05\x12\x16\n\x12\x43ONVERSION_EXPIRED\x10\x06\x12\"\n\x1e\x41\x44JUSTMENT_PRECEDES_CONVERSION\x10\x07\x12!\n\x1dMORE_RECENT_RESTATEMENT_FOUND\x10\x08\x12\x19\n\x15TOO_RECENT_CONVERSION\x10\t\x12N\nJCANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE\x10\n\x12#\n\x1fTOO_MANY_ADJUSTMENTS_IN_REQUEST\x10\x0b\x12\x18\n\x14TOO_MANY_ADJUSTMENTS\x10\x0c\x12\x1e\n\x1aRESTATEMENT_ALREADY_EXISTS\x10\r\x12#\n\x1f\x44UPLICATE_ADJUSTMENT_IN_REQUEST\x10\x0e\x12-\n)CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS\x10\x0f\x12\x32\n.CONVERSION_ACTION_NOT_ELIGIBLE_FOR_ENHANCEMENT\x10\x10\x12\x1b\n\x17INVALID_USER_IDENTIFIER\x10\x11\x12\x1f\n\x1bUNSUPPORTED_USER_IDENTIFIER\x10\x12\x12.\n*GCLID_DATE_TIME_PAIR_AND_ORDER_ID_BOTH_SET\x10\x14\x12\x1f\n\x1b\x43ONVERSION_ALREADY_ENHANCED\x10\x15\x12$\n DUPLICATE_ENHANCEMENT_IN_REQUEST\x10\x16\x42\xff\x01\n\"com.google.ads.googleads.v9.errorsB$ConversionAdjustmentUploadErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CONVERSIONADJUSTMENTUPLOADERRORENUM_CONVERSIONADJUSTMENTUPLOADERROR = _descriptor.EnumDescriptor(
  name='ConversionAdjustmentUploadError',
  full_name='google.ads.googleads.v9.errors.ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError',
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
      name='TOO_RECENT_CONVERSION_ACTION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CONVERSION_ACTION', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_ALREADY_RETRACTED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_NOT_FOUND', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_EXPIRED', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADJUSTMENT_PRECEDES_CONVERSION', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MORE_RECENT_RESTATEMENT_FOUND', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_RECENT_CONVERSION', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_ADJUSTMENTS_IN_REQUEST', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_ADJUSTMENTS', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESTATEMENT_ALREADY_EXISTS', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_ADJUSTMENT_IN_REQUEST', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_ACTION_NOT_ELIGIBLE_FOR_ENHANCEMENT', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_USER_IDENTIFIER', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_USER_IDENTIFIER', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GCLID_DATE_TIME_PAIR_AND_ORDER_ID_BOTH_SET', index=19, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_ALREADY_ENHANCED', index=20, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_ENHANCEMENT_IN_REQUEST', index=21, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=178,
  serialized_end=980,
)
_sym_db.RegisterEnumDescriptor(_CONVERSIONADJUSTMENTUPLOADERRORENUM_CONVERSIONADJUSTMENTUPLOADERROR)


_CONVERSIONADJUSTMENTUPLOADERRORENUM = _descriptor.Descriptor(
  name='ConversionAdjustmentUploadErrorEnum',
  full_name='google.ads.googleads.v9.errors.ConversionAdjustmentUploadErrorEnum',
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
    _CONVERSIONADJUSTMENTUPLOADERRORENUM_CONVERSIONADJUSTMENTUPLOADERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=980,
)

_CONVERSIONADJUSTMENTUPLOADERRORENUM_CONVERSIONADJUSTMENTUPLOADERROR.containing_type = _CONVERSIONADJUSTMENTUPLOADERRORENUM
DESCRIPTOR.message_types_by_name['ConversionAdjustmentUploadErrorEnum'] = _CONVERSIONADJUSTMENTUPLOADERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConversionAdjustmentUploadErrorEnum = _reflection.GeneratedProtocolMessageType('ConversionAdjustmentUploadErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSIONADJUSTMENTUPLOADERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.conversion_adjustment_upload_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.ConversionAdjustmentUploadErrorEnum)
  })
_sym_db.RegisterMessage(ConversionAdjustmentUploadErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
