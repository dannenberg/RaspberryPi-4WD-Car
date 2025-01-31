# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/enums/age_range_type.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/enums/age_range_type.proto',
  package='google.ads.googleads.v9.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v9.enumsB\021AgeRangeTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V9.Enums\312\002\035Google\\Ads\\GoogleAds\\V9\\Enums\352\002!Google::Ads::GoogleAds::V9::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2google/ads/googleads/v9/enums/age_range_type.proto\x12\x1dgoogle.ads.googleads.v9.enums\x1a\x1cgoogle/api/annotations.proto\"\xe9\x01\n\x10\x41geRangeTypeEnum\"\xd4\x01\n\x0c\x41geRangeType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x15\n\x0f\x41GE_RANGE_18_24\x10\xd9\xd9\x1e\x12\x15\n\x0f\x41GE_RANGE_25_34\x10\xda\xd9\x1e\x12\x15\n\x0f\x41GE_RANGE_35_44\x10\xdb\xd9\x1e\x12\x15\n\x0f\x41GE_RANGE_45_54\x10\xdc\xd9\x1e\x12\x15\n\x0f\x41GE_RANGE_55_64\x10\xdd\xd9\x1e\x12\x15\n\x0f\x41GE_RANGE_65_UP\x10\xde\xd9\x1e\x12\x1c\n\x16\x41GE_RANGE_UNDETERMINED\x10\xbf\xe1\x1e\x42\xe6\x01\n!com.google.ads.googleads.v9.enumsB\x11\x41geRangeTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V9.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V9\\Enums\xea\x02!Google::Ads::GoogleAds::V9::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_AGERANGETYPEENUM_AGERANGETYPE = _descriptor.EnumDescriptor(
  name='AgeRangeType',
  full_name='google.ads.googleads.v9.enums.AgeRangeTypeEnum.AgeRangeType',
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
      name='AGE_RANGE_18_24', index=2, number=503001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AGE_RANGE_25_34', index=3, number=503002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AGE_RANGE_35_44', index=4, number=503003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AGE_RANGE_45_54', index=5, number=503004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AGE_RANGE_55_64', index=6, number=503005,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AGE_RANGE_65_UP', index=7, number=503006,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AGE_RANGE_UNDETERMINED', index=8, number=503999,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=137,
  serialized_end=349,
)
_sym_db.RegisterEnumDescriptor(_AGERANGETYPEENUM_AGERANGETYPE)


_AGERANGETYPEENUM = _descriptor.Descriptor(
  name='AgeRangeTypeEnum',
  full_name='google.ads.googleads.v9.enums.AgeRangeTypeEnum',
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
    _AGERANGETYPEENUM_AGERANGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=349,
)

_AGERANGETYPEENUM_AGERANGETYPE.containing_type = _AGERANGETYPEENUM
DESCRIPTOR.message_types_by_name['AgeRangeTypeEnum'] = _AGERANGETYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgeRangeTypeEnum = _reflection.GeneratedProtocolMessageType('AgeRangeTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _AGERANGETYPEENUM,
  '__module__' : 'google.ads.googleads.v9.enums.age_range_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.enums.AgeRangeTypeEnum)
  })
_sym_db.RegisterMessage(AgeRangeTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
