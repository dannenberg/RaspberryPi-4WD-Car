# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/enums/reach_plan_network.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/enums/reach_plan_network.proto',
  package='google.ads.googleads.v9.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v9.enumsB\025ReachPlanNetworkProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V9.Enums\312\002\035Google\\Ads\\GoogleAds\\V9\\Enums\352\002!Google::Ads::GoogleAds::V9::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6google/ads/googleads/v9/enums/reach_plan_network.proto\x12\x1dgoogle.ads.googleads.v9.enums\x1a\x1cgoogle/api/annotations.proto\"\x97\x01\n\x14ReachPlanNetworkEnum\"\x7f\n\x10ReachPlanNetwork\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07YOUTUBE\x10\x02\x12\x19\n\x15GOOGLE_VIDEO_PARTNERS\x10\x03\x12%\n!YOUTUBE_AND_GOOGLE_VIDEO_PARTNERS\x10\x04\x42\xea\x01\n!com.google.ads.googleads.v9.enumsB\x15ReachPlanNetworkProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v9/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V9.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V9\\Enums\xea\x02!Google::Ads::GoogleAds::V9::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_REACHPLANNETWORKENUM_REACHPLANNETWORK = _descriptor.EnumDescriptor(
  name='ReachPlanNetwork',
  full_name='google.ads.googleads.v9.enums.ReachPlanNetworkEnum.ReachPlanNetwork',
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
      name='YOUTUBE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_VIDEO_PARTNERS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE_AND_GOOGLE_VIDEO_PARTNERS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=144,
  serialized_end=271,
)
_sym_db.RegisterEnumDescriptor(_REACHPLANNETWORKENUM_REACHPLANNETWORK)


_REACHPLANNETWORKENUM = _descriptor.Descriptor(
  name='ReachPlanNetworkEnum',
  full_name='google.ads.googleads.v9.enums.ReachPlanNetworkEnum',
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
    _REACHPLANNETWORKENUM_REACHPLANNETWORK,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=271,
)

_REACHPLANNETWORKENUM_REACHPLANNETWORK.containing_type = _REACHPLANNETWORKENUM
DESCRIPTOR.message_types_by_name['ReachPlanNetworkEnum'] = _REACHPLANNETWORKENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReachPlanNetworkEnum = _reflection.GeneratedProtocolMessageType('ReachPlanNetworkEnum', (_message.Message,), {
  'DESCRIPTOR' : _REACHPLANNETWORKENUM,
  '__module__' : 'google.ads.googleads.v9.enums.reach_plan_network_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.enums.ReachPlanNetworkEnum)
  })
_sym_db.RegisterMessage(ReachPlanNetworkEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
