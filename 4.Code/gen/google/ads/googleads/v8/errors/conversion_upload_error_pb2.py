# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/errors/conversion_upload_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v8/errors/conversion_upload_error.proto',
  package='google.ads.googleads.v8.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v8.errorsB\032ConversionUploadErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V8.Errors\312\002\036Google\\Ads\\GoogleAds\\V8\\Errors\352\002\"Google::Ads::GoogleAds::V8::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<google/ads/googleads/v8/errors/conversion_upload_error.proto\x12\x1egoogle.ads.googleads.v8.errors\x1a\x1cgoogle/api/annotations.proto\"\xd1\t\n\x19\x43onversionUploadErrorEnum\"\xb3\t\n\x15\x43onversionUploadError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12#\n\x1fTOO_MANY_CONVERSIONS_IN_REQUEST\x10\x02\x12\x15\n\x11UNPARSEABLE_GCLID\x10\x03\x12\x1d\n\x19\x43ONVERSION_PRECEDES_GCLID\x10\x04\x12\x11\n\rEXPIRED_GCLID\x10\x05\x12\x14\n\x10TOO_RECENT_GCLID\x10\x06\x12\x13\n\x0fGCLID_NOT_FOUND\x10\x07\x12\x19\n\x15UNAUTHORIZED_CUSTOMER\x10\x08\x12\x1d\n\x19INVALID_CONVERSION_ACTION\x10\t\x12 \n\x1cTOO_RECENT_CONVERSION_ACTION\x10\n\x12\x36\n2CONVERSION_TRACKING_NOT_ENABLED_AT_IMPRESSION_TIME\x10\x0b\x12Q\nMEXTERNAL_ATTRIBUTION_DATA_SET_FOR_NON_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION\x10\x0c\x12Q\nMEXTERNAL_ATTRIBUTION_DATA_NOT_SET_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION\x10\r\x12\x46\nBORDER_ID_NOT_PERMITTED_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION\x10\x0e\x12\x1b\n\x17ORDER_ID_ALREADY_IN_USE\x10\x0f\x12\x16\n\x12\x44UPLICATE_ORDER_ID\x10\x10\x12\x13\n\x0fTOO_RECENT_CALL\x10\x11\x12\x10\n\x0c\x45XPIRED_CALL\x10\x12\x12\x12\n\x0e\x43\x41LL_NOT_FOUND\x10\x13\x12\x1c\n\x18\x43ONVERSION_PRECEDES_CALL\x10\x14\x12\x30\n,CONVERSION_TRACKING_NOT_ENABLED_AT_CALL_TIME\x10\x15\x12$\n UNPARSEABLE_CALLERS_PHONE_NUMBER\x10\x16\x12\x1f\n\x1b\x43USTOM_VARIABLE_NOT_ENABLED\x10\x1c\x12&\n\"CUSTOM_VARIABLE_VALUE_CONTAINS_PII\x10\x1d\x12\x1e\n\x1aINVALID_CUSTOMER_FOR_CLICK\x10\x1e\x12\x1d\n\x19INVALID_CUSTOMER_FOR_CALL\x10\x1f\x12,\n(CONVERSION_NOT_COMPLIANT_WITH_ATT_POLICY\x10 \x12\x13\n\x0f\x43LICK_NOT_FOUND\x10!\x12\x1b\n\x17INVALID_USER_IDENTIFIER\x10\"\x12N\nJEXTERNALLY_ATTRIBUTED_CONVERSION_ACTION_NOT_PERMITTED_WITH_USER_IDENTIFIER\x10#\x12\x1f\n\x1bUNSUPPORTED_USER_IDENTIFIER\x10$\x12\"\n\x1eINVALID_USER_IDENTIFIER_SOURCE\x10%B\xf5\x01\n\"com.google.ads.googleads.v8.errorsB\x1a\x43onversionUploadErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V8.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V8\\Errors\xea\x02\"Google::Ads::GoogleAds::V8::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CONVERSIONUPLOADERRORENUM_CONVERSIONUPLOADERROR = _descriptor.EnumDescriptor(
  name='ConversionUploadError',
  full_name='google.ads.googleads.v8.errors.ConversionUploadErrorEnum.ConversionUploadError',
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
      name='TOO_MANY_CONVERSIONS_IN_REQUEST', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNPARSEABLE_GCLID', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_PRECEDES_GCLID', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED_GCLID', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_RECENT_GCLID', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GCLID_NOT_FOUND', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNAUTHORIZED_CUSTOMER', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CONVERSION_ACTION', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_RECENT_CONVERSION_ACTION', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_TRACKING_NOT_ENABLED_AT_IMPRESSION_TIME', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL_ATTRIBUTION_DATA_SET_FOR_NON_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL_ATTRIBUTION_DATA_NOT_SET_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_ID_NOT_PERMITTED_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_ID_ALREADY_IN_USE', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_ORDER_ID', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_RECENT_CALL', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED_CALL', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CALL_NOT_FOUND', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_PRECEDES_CALL', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_TRACKING_NOT_ENABLED_AT_CALL_TIME', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNPARSEABLE_CALLERS_PHONE_NUMBER', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_VARIABLE_NOT_ENABLED', index=23, number=28,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_VARIABLE_VALUE_CONTAINS_PII', index=24, number=29,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CUSTOMER_FOR_CLICK', index=25, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CUSTOMER_FOR_CALL', index=26, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_NOT_COMPLIANT_WITH_ATT_POLICY', index=27, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLICK_NOT_FOUND', index=28, number=33,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_USER_IDENTIFIER', index=29, number=34,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION_NOT_PERMITTED_WITH_USER_IDENTIFIER', index=30, number=35,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_USER_IDENTIFIER', index=31, number=36,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_USER_IDENTIFIER_SOURCE', index=32, number=37,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=157,
  serialized_end=1360,
)
_sym_db.RegisterEnumDescriptor(_CONVERSIONUPLOADERRORENUM_CONVERSIONUPLOADERROR)


_CONVERSIONUPLOADERRORENUM = _descriptor.Descriptor(
  name='ConversionUploadErrorEnum',
  full_name='google.ads.googleads.v8.errors.ConversionUploadErrorEnum',
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
    _CONVERSIONUPLOADERRORENUM_CONVERSIONUPLOADERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=1360,
)

_CONVERSIONUPLOADERRORENUM_CONVERSIONUPLOADERROR.containing_type = _CONVERSIONUPLOADERRORENUM
DESCRIPTOR.message_types_by_name['ConversionUploadErrorEnum'] = _CONVERSIONUPLOADERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConversionUploadErrorEnum = _reflection.GeneratedProtocolMessageType('ConversionUploadErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSIONUPLOADERRORENUM,
  '__module__' : 'google.ads.googleads.v8.errors.conversion_upload_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.errors.ConversionUploadErrorEnum)
  })
_sym_db.RegisterMessage(ConversionUploadErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
