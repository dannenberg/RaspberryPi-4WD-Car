# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/enums/ad_group_type.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/enums/ad_group_type.proto',
  package='google.ads.googleads.v9.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v9.enumsB\020AdGroupTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V9.Enums\312\002\035Google\\Ads\\GoogleAds\\V9\\Enums\352\002!Google::Ads::GoogleAds::V9::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1google/ads/googleads/v9/enums/ad_group_type.proto\x12\x1dgoogle.ads.googleads.v9.enums\x1a\x1cgoogle/api/annotations.proto\"\xd2\x03\n\x0f\x41\x64GroupTypeEnum\"\xbe\x03\n\x0b\x41\x64GroupType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x13\n\x0fSEARCH_STANDARD\x10\x02\x12\x14\n\x10\x44ISPLAY_STANDARD\x10\x03\x12\x18\n\x14SHOPPING_PRODUCT_ADS\x10\x04\x12\r\n\tHOTEL_ADS\x10\x06\x12\x16\n\x12SHOPPING_SMART_ADS\x10\x07\x12\x10\n\x0cVIDEO_BUMPER\x10\x08\x12\x1d\n\x19VIDEO_TRUE_VIEW_IN_STREAM\x10\t\x12\x1e\n\x1aVIDEO_TRUE_VIEW_IN_DISPLAY\x10\n\x12!\n\x1dVIDEO_NON_SKIPPABLE_IN_STREAM\x10\x0b\x12\x13\n\x0fVIDEO_OUTSTREAM\x10\x0c\x12\x16\n\x12SEARCH_DYNAMIC_ADS\x10\r\x12#\n\x1fSHOPPING_COMPARISON_LISTING_ADS\x10\x0e\x12\x16\n\x12PROMOTED_HOTEL_ADS\x10\x0f\x12\x14\n\x10VIDEO_RESPONSIVE\x10\x10\x12\x19\n\x15VIDEO_EFFICIENT_REACH\x10\x11\x12\x16\n\x12SMART_CAMPAIGN_ADS\x10\x12\x42\xe5\x01\n!com.google.ads.googleads.v9.enumsB\x10\x41\x64GroupTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V9.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V9\\Enums\xea\x02!Google::Ads::GoogleAds::V9::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ADGROUPTYPEENUM_ADGROUPTYPE = _descriptor.EnumDescriptor(
  name='AdGroupType',
  full_name='google.ads.googleads.v9.enums.AdGroupTypeEnum.AdGroupType',
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
      name='SEARCH_STANDARD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY_STANDARD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHOPPING_PRODUCT_ADS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOTEL_ADS', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHOPPING_SMART_ADS', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_BUMPER', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_TRUE_VIEW_IN_STREAM', index=8, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_TRUE_VIEW_IN_DISPLAY', index=9, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_NON_SKIPPABLE_IN_STREAM', index=10, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_OUTSTREAM', index=11, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEARCH_DYNAMIC_ADS', index=12, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHOPPING_COMPARISON_LISTING_ADS', index=13, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROMOTED_HOTEL_ADS', index=14, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_RESPONSIVE', index=15, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_EFFICIENT_REACH', index=16, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SMART_CAMPAIGN_ADS', index=17, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=135,
  serialized_end=581,
)
_sym_db.RegisterEnumDescriptor(_ADGROUPTYPEENUM_ADGROUPTYPE)


_ADGROUPTYPEENUM = _descriptor.Descriptor(
  name='AdGroupTypeEnum',
  full_name='google.ads.googleads.v9.enums.AdGroupTypeEnum',
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
    _ADGROUPTYPEENUM_ADGROUPTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=581,
)

_ADGROUPTYPEENUM_ADGROUPTYPE.containing_type = _ADGROUPTYPEENUM
DESCRIPTOR.message_types_by_name['AdGroupTypeEnum'] = _ADGROUPTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupTypeEnum = _reflection.GeneratedProtocolMessageType('AdGroupTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPTYPEENUM,
  '__module__' : 'google.ads.googleads.v9.enums.ad_group_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.enums.AdGroupTypeEnum)
  })
_sym_db.RegisterMessage(AdGroupTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
