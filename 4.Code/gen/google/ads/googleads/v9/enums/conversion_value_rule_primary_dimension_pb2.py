# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/enums/conversion_value_rule_primary_dimension.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/enums/conversion_value_rule_primary_dimension.proto',
  package='google.ads.googleads.v9.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v9.enumsB(ConversionValueRulePrimaryDimensionProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V9.Enums\312\002\035Google\\Ads\\GoogleAds\\V9\\Enums\352\002!Google::Ads::GoogleAds::V9::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nKgoogle/ads/googleads/v9/enums/conversion_value_rule_primary_dimension.proto\x12\x1dgoogle.ads.googleads.v9.enums\x1a\x1cgoogle/api/annotations.proto\"\xe7\x01\n\'ConversionValueRulePrimaryDimensionEnum\"\xbb\x01\n#ConversionValueRulePrimaryDimension\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x13\n\x0fNO_RULE_APPLIED\x10\x02\x12\x0c\n\x08ORIGINAL\x10\x03\x12\x19\n\x15NEW_VS_RETURNING_USER\x10\x04\x12\x10\n\x0cGEO_LOCATION\x10\x05\x12\n\n\x06\x44\x45VICE\x10\x06\x12\x0c\n\x08\x41UDIENCE\x10\x07\x12\x0c\n\x08MULTIPLE\x10\x08\x42\xfd\x01\n!com.google.ads.googleads.v9.enumsB(ConversionValueRulePrimaryDimensionProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V9.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V9\\Enums\xea\x02!Google::Ads::GoogleAds::V9::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CONVERSIONVALUERULEPRIMARYDIMENSIONENUM_CONVERSIONVALUERULEPRIMARYDIMENSION = _descriptor.EnumDescriptor(
  name='ConversionValueRulePrimaryDimension',
  full_name='google.ads.googleads.v9.enums.ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension',
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
      name='NO_RULE_APPLIED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORIGINAL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NEW_VS_RETURNING_USER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GEO_LOCATION', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEVICE', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUDIENCE', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=185,
  serialized_end=372,
)
_sym_db.RegisterEnumDescriptor(_CONVERSIONVALUERULEPRIMARYDIMENSIONENUM_CONVERSIONVALUERULEPRIMARYDIMENSION)


_CONVERSIONVALUERULEPRIMARYDIMENSIONENUM = _descriptor.Descriptor(
  name='ConversionValueRulePrimaryDimensionEnum',
  full_name='google.ads.googleads.v9.enums.ConversionValueRulePrimaryDimensionEnum',
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
    _CONVERSIONVALUERULEPRIMARYDIMENSIONENUM_CONVERSIONVALUERULEPRIMARYDIMENSION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=372,
)

_CONVERSIONVALUERULEPRIMARYDIMENSIONENUM_CONVERSIONVALUERULEPRIMARYDIMENSION.containing_type = _CONVERSIONVALUERULEPRIMARYDIMENSIONENUM
DESCRIPTOR.message_types_by_name['ConversionValueRulePrimaryDimensionEnum'] = _CONVERSIONVALUERULEPRIMARYDIMENSIONENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConversionValueRulePrimaryDimensionEnum = _reflection.GeneratedProtocolMessageType('ConversionValueRulePrimaryDimensionEnum', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSIONVALUERULEPRIMARYDIMENSIONENUM,
  '__module__' : 'google.ads.googleads.v9.enums.conversion_value_rule_primary_dimension_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.enums.ConversionValueRulePrimaryDimensionEnum)
  })
_sym_db.RegisterMessage(ConversionValueRulePrimaryDimensionEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
