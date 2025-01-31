# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/enums/hotel_rate_type.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/enums/hotel_rate_type.proto',
  package='google.ads.googleads.v9.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v9.enumsB\022HotelRateTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V9.Enums\312\002\035Google\\Ads\\GoogleAds\\V9\\Enums\352\002!Google::Ads::GoogleAds::V9::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3google/ads/googleads/v9/enums/hotel_rate_type.proto\x12\x1dgoogle.ads.googleads.v9.enums\x1a\x1cgoogle/api/annotations.proto\"\x8a\x01\n\x11HotelRateTypeEnum\"u\n\rHotelRateType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0f\n\x0bUNAVAILABLE\x10\x02\x12\x0f\n\x0bPUBLIC_RATE\x10\x03\x12\x12\n\x0eQUALIFIED_RATE\x10\x04\x12\x10\n\x0cPRIVATE_RATE\x10\x05\x42\xe7\x01\n!com.google.ads.googleads.v9.enumsB\x12HotelRateTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V9.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V9\\Enums\xea\x02!Google::Ads::GoogleAds::V9::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_HOTELRATETYPEENUM_HOTELRATETYPE = _descriptor.EnumDescriptor(
  name='HotelRateType',
  full_name='google.ads.googleads.v9.enums.HotelRateTypeEnum.HotelRateType',
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
      name='UNAVAILABLE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUBLIC_RATE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUALIFIED_RATE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRIVATE_RATE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=138,
  serialized_end=255,
)
_sym_db.RegisterEnumDescriptor(_HOTELRATETYPEENUM_HOTELRATETYPE)


_HOTELRATETYPEENUM = _descriptor.Descriptor(
  name='HotelRateTypeEnum',
  full_name='google.ads.googleads.v9.enums.HotelRateTypeEnum',
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
    _HOTELRATETYPEENUM_HOTELRATETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=255,
)

_HOTELRATETYPEENUM_HOTELRATETYPE.containing_type = _HOTELRATETYPEENUM
DESCRIPTOR.message_types_by_name['HotelRateTypeEnum'] = _HOTELRATETYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HotelRateTypeEnum = _reflection.GeneratedProtocolMessageType('HotelRateTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _HOTELRATETYPEENUM,
  '__module__' : 'google.ads.googleads.v9.enums.hotel_rate_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.enums.HotelRateTypeEnum)
  })
_sym_db.RegisterMessage(HotelRateTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
