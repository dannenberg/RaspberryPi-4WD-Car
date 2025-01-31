# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/asset_group_listing_group_filter_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/errors/asset_group_listing_group_filter_error.proto',
  package='google.ads.googleads.v9.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v9.errorsB&AssetGroupListingGroupFilterErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nKgoogle/ads/googleads/v9/errors/asset_group_listing_group_filter_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"\xc9\x04\n%AssetGroupListingGroupFilterErrorEnum\"\x9f\x04\n!AssetGroupListingGroupFilterError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x11\n\rTREE_TOO_DEEP\x10\x02\x12\x1d\n\x19UNIT_CANNOT_HAVE_CHILDREN\x10\x03\x12/\n+SUBDIVISION_MUST_HAVE_EVERYTHING_ELSE_CHILD\x10\x04\x12-\n)DIFFERENT_DIMENSION_TYPE_BETWEEN_SIBLINGS\x10\x05\x12)\n%SAME_DIMENSION_VALUE_BETWEEN_SIBLINGS\x10\x06\x12)\n%SAME_DIMENSION_TYPE_BETWEEN_ANCESTORS\x10\x07\x12\x12\n\x0eMULTIPLE_ROOTS\x10\x08\x12\x1b\n\x17INVALID_DIMENSION_VALUE\x10\t\x12(\n$MUST_REFINE_HIERARCHICAL_PARENT_TYPE\x10\n\x12$\n INVALID_PRODUCT_BIDDING_CATEGORY\x10\x0b\x12%\n!CHANGING_CASE_VALUE_WITH_CHILDREN\x10\x0c\x12\x1c\n\x18SUBDIVISION_HAS_CHILDREN\x10\r\x12.\n*CANNOT_REFINE_HIERARCHICAL_EVERYTHING_ELSE\x10\x0e\x42\x81\x02\n\"com.google.ads.googleads.v9.errorsB&AssetGroupListingGroupFilterErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ASSETGROUPLISTINGGROUPFILTERERRORENUM_ASSETGROUPLISTINGGROUPFILTERERROR = _descriptor.EnumDescriptor(
  name='AssetGroupListingGroupFilterError',
  full_name='google.ads.googleads.v9.errors.AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError',
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
      name='TREE_TOO_DEEP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNIT_CANNOT_HAVE_CHILDREN', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUBDIVISION_MUST_HAVE_EVERYTHING_ELSE_CHILD', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIFFERENT_DIMENSION_TYPE_BETWEEN_SIBLINGS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SAME_DIMENSION_VALUE_BETWEEN_SIBLINGS', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SAME_DIMENSION_TYPE_BETWEEN_ANCESTORS', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE_ROOTS', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DIMENSION_VALUE', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MUST_REFINE_HIERARCHICAL_PARENT_TYPE', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PRODUCT_BIDDING_CATEGORY', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANGING_CASE_VALUE_WITH_CHILDREN', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUBDIVISION_HAS_CHILDREN', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_REFINE_HIERARCHICAL_EVERYTHING_ELSE', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=184,
  serialized_end=727,
)
_sym_db.RegisterEnumDescriptor(_ASSETGROUPLISTINGGROUPFILTERERRORENUM_ASSETGROUPLISTINGGROUPFILTERERROR)


_ASSETGROUPLISTINGGROUPFILTERERRORENUM = _descriptor.Descriptor(
  name='AssetGroupListingGroupFilterErrorEnum',
  full_name='google.ads.googleads.v9.errors.AssetGroupListingGroupFilterErrorEnum',
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
    _ASSETGROUPLISTINGGROUPFILTERERRORENUM_ASSETGROUPLISTINGGROUPFILTERERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=727,
)

_ASSETGROUPLISTINGGROUPFILTERERRORENUM_ASSETGROUPLISTINGGROUPFILTERERROR.containing_type = _ASSETGROUPLISTINGGROUPFILTERERRORENUM
DESCRIPTOR.message_types_by_name['AssetGroupListingGroupFilterErrorEnum'] = _ASSETGROUPLISTINGGROUPFILTERERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AssetGroupListingGroupFilterErrorEnum = _reflection.GeneratedProtocolMessageType('AssetGroupListingGroupFilterErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _ASSETGROUPLISTINGGROUPFILTERERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.asset_group_listing_group_filter_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.AssetGroupListingGroupFilterErrorEnum)
  })
_sym_db.RegisterMessage(AssetGroupListingGroupFilterErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
