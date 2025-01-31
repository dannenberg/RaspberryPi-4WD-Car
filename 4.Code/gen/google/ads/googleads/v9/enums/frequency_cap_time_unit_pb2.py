# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/enums/frequency_cap_time_unit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/enums/frequency_cap_time_unit.proto',
  package='google.ads.googleads.v9.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v9.enumsB\031FrequencyCapTimeUnitProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V9.Enums\312\002\035Google\\Ads\\GoogleAds\\V9\\Enums\352\002!Google::Ads::GoogleAds::V9::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;google/ads/googleads/v9/enums/frequency_cap_time_unit.proto\x12\x1dgoogle.ads.googleads.v9.enums\x1a\x1cgoogle/api/annotations.proto\"n\n\x18\x46requencyCapTimeUnitEnum\"R\n\x14\x46requencyCapTimeUnit\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x07\n\x03\x44\x41Y\x10\x02\x12\x08\n\x04WEEK\x10\x03\x12\t\n\x05MONTH\x10\x04\x42\xee\x01\n!com.google.ads.googleads.v9.enumsB\x19\x46requencyCapTimeUnitProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V9.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V9\\Enums\xea\x02!Google::Ads::GoogleAds::V9::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FREQUENCYCAPTIMEUNITENUM_FREQUENCYCAPTIMEUNIT = _descriptor.EnumDescriptor(
  name='FrequencyCapTimeUnit',
  full_name='google.ads.googleads.v9.enums.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit',
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
      name='DAY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WEEK', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MONTH', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=152,
  serialized_end=234,
)
_sym_db.RegisterEnumDescriptor(_FREQUENCYCAPTIMEUNITENUM_FREQUENCYCAPTIMEUNIT)


_FREQUENCYCAPTIMEUNITENUM = _descriptor.Descriptor(
  name='FrequencyCapTimeUnitEnum',
  full_name='google.ads.googleads.v9.enums.FrequencyCapTimeUnitEnum',
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
    _FREQUENCYCAPTIMEUNITENUM_FREQUENCYCAPTIMEUNIT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=234,
)

_FREQUENCYCAPTIMEUNITENUM_FREQUENCYCAPTIMEUNIT.containing_type = _FREQUENCYCAPTIMEUNITENUM
DESCRIPTOR.message_types_by_name['FrequencyCapTimeUnitEnum'] = _FREQUENCYCAPTIMEUNITENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrequencyCapTimeUnitEnum = _reflection.GeneratedProtocolMessageType('FrequencyCapTimeUnitEnum', (_message.Message,), {
  'DESCRIPTOR' : _FREQUENCYCAPTIMEUNITENUM,
  '__module__' : 'google.ads.googleads.v9.enums.frequency_cap_time_unit_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.enums.FrequencyCapTimeUnitEnum)
  })
_sym_db.RegisterMessage(FrequencyCapTimeUnitEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
