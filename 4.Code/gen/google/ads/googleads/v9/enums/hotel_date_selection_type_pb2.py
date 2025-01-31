# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/enums/hotel_date_selection_type.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/enums/hotel_date_selection_type.proto',
  package='google.ads.googleads.v9.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v9.enumsB\033HotelDateSelectionTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V9.Enums\312\002\035Google\\Ads\\GoogleAds\\V9\\Enums\352\002!Google::Ads::GoogleAds::V9::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=google/ads/googleads/v9/enums/hotel_date_selection_type.proto\x12\x1dgoogle.ads.googleads.v9.enums\x1a\x1cgoogle/api/annotations.proto\"~\n\x1aHotelDateSelectionTypeEnum\"`\n\x16HotelDateSelectionType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x15\n\x11\x44\x45\x46\x41ULT_SELECTION\x10\x32\x12\x11\n\rUSER_SELECTED\x10\x33\x42\xf0\x01\n!com.google.ads.googleads.v9.enumsB\x1bHotelDateSelectionTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V9.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V9\\Enums\xea\x02!Google::Ads::GoogleAds::V9::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_HOTELDATESELECTIONTYPEENUM_HOTELDATESELECTIONTYPE = _descriptor.EnumDescriptor(
  name='HotelDateSelectionType',
  full_name='google.ads.googleads.v9.enums.HotelDateSelectionTypeEnum.HotelDateSelectionType',
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
      name='DEFAULT_SELECTION', index=2, number=50,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='USER_SELECTED', index=3, number=51,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=156,
  serialized_end=252,
)
_sym_db.RegisterEnumDescriptor(_HOTELDATESELECTIONTYPEENUM_HOTELDATESELECTIONTYPE)


_HOTELDATESELECTIONTYPEENUM = _descriptor.Descriptor(
  name='HotelDateSelectionTypeEnum',
  full_name='google.ads.googleads.v9.enums.HotelDateSelectionTypeEnum',
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
    _HOTELDATESELECTIONTYPEENUM_HOTELDATESELECTIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=252,
)

_HOTELDATESELECTIONTYPEENUM_HOTELDATESELECTIONTYPE.containing_type = _HOTELDATESELECTIONTYPEENUM
DESCRIPTOR.message_types_by_name['HotelDateSelectionTypeEnum'] = _HOTELDATESELECTIONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HotelDateSelectionTypeEnum = _reflection.GeneratedProtocolMessageType('HotelDateSelectionTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _HOTELDATESELECTIONTYPEENUM,
  '__module__' : 'google.ads.googleads.v9.enums.hotel_date_selection_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.enums.HotelDateSelectionTypeEnum)
  })
_sym_db.RegisterMessage(HotelDateSelectionTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
