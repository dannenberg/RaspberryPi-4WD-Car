# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/common/feed_item_set_filter_type_infos.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.enums import feed_item_set_string_filter_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_feed__item__set__string__filter__type__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v8/common/feed_item_set_filter_type_infos.proto',
  package='google.ads.googleads.v8.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v8.commonB\037FeedItemSetFilterTypeInfosProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V8.Common\312\002\036Google\\Ads\\GoogleAds\\V8\\Common\352\002\"Google::Ads::GoogleAds::V8::Common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDgoogle/ads/googleads/v8/common/feed_item_set_filter_type_infos.proto\x12\x1egoogle.ads.googleads.v8.common\x1a\x44google/ads/googleads/v8/enums/feed_item_set_string_filter_type.proto\x1a\x1cgoogle/api/annotations.proto\"\x98\x01\n\x18\x44ynamicLocationSetFilter\x12\x16\n\x06labels\x18\x01 \x03(\tR\x06labels\x12\x64\n\x14\x62usiness_name_filter\x18\x02 \x01(\x0b\x32\x32.google.ads.googleads.v8.common.BusinessNameFilterR\x12\x62usinessNameFilter\"\xb6\x01\n\x12\x42usinessNameFilter\x12#\n\rbusiness_name\x18\x01 \x01(\tR\x0c\x62usinessName\x12{\n\x0b\x66ilter_type\x18\x02 \x01(\x0e\x32Z.google.ads.googleads.v8.enums.FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterTypeR\nfilterType\"@\n!DynamicAffiliateLocationSetFilter\x12\x1b\n\tchain_ids\x18\x01 \x03(\x03R\x08\x63hainIdsB\xfa\x01\n\"com.google.ads.googleads.v8.commonB\x1f\x46\x65\x65\x64ItemSetFilterTypeInfosProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V8.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V8\\Common\xea\x02\"Google::Ads::GoogleAds::V8::Commonb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_feed__item__set__string__filter__type__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_DYNAMICLOCATIONSETFILTER = _descriptor.Descriptor(
  name='DynamicLocationSetFilter',
  full_name='google.ads.googleads.v8.common.DynamicLocationSetFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.ads.googleads.v8.common.DynamicLocationSetFilter.labels', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='business_name_filter', full_name='google.ads.googleads.v8.common.DynamicLocationSetFilter.business_name_filter', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='businessNameFilter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=357,
)


_BUSINESSNAMEFILTER = _descriptor.Descriptor(
  name='BusinessNameFilter',
  full_name='google.ads.googleads.v8.common.BusinessNameFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='business_name', full_name='google.ads.googleads.v8.common.BusinessNameFilter.business_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='businessName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter_type', full_name='google.ads.googleads.v8.common.BusinessNameFilter.filter_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='filterType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=542,
)


_DYNAMICAFFILIATELOCATIONSETFILTER = _descriptor.Descriptor(
  name='DynamicAffiliateLocationSetFilter',
  full_name='google.ads.googleads.v8.common.DynamicAffiliateLocationSetFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chain_ids', full_name='google.ads.googleads.v8.common.DynamicAffiliateLocationSetFilter.chain_ids', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chainIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=608,
)

_DYNAMICLOCATIONSETFILTER.fields_by_name['business_name_filter'].message_type = _BUSINESSNAMEFILTER
_BUSINESSNAMEFILTER.fields_by_name['filter_type'].enum_type = google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_feed__item__set__string__filter__type__pb2._FEEDITEMSETSTRINGFILTERTYPEENUM_FEEDITEMSETSTRINGFILTERTYPE
DESCRIPTOR.message_types_by_name['DynamicLocationSetFilter'] = _DYNAMICLOCATIONSETFILTER
DESCRIPTOR.message_types_by_name['BusinessNameFilter'] = _BUSINESSNAMEFILTER
DESCRIPTOR.message_types_by_name['DynamicAffiliateLocationSetFilter'] = _DYNAMICAFFILIATELOCATIONSETFILTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DynamicLocationSetFilter = _reflection.GeneratedProtocolMessageType('DynamicLocationSetFilter', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMICLOCATIONSETFILTER,
  '__module__' : 'google.ads.googleads.v8.common.feed_item_set_filter_type_infos_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.common.DynamicLocationSetFilter)
  })
_sym_db.RegisterMessage(DynamicLocationSetFilter)

BusinessNameFilter = _reflection.GeneratedProtocolMessageType('BusinessNameFilter', (_message.Message,), {
  'DESCRIPTOR' : _BUSINESSNAMEFILTER,
  '__module__' : 'google.ads.googleads.v8.common.feed_item_set_filter_type_infos_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.common.BusinessNameFilter)
  })
_sym_db.RegisterMessage(BusinessNameFilter)

DynamicAffiliateLocationSetFilter = _reflection.GeneratedProtocolMessageType('DynamicAffiliateLocationSetFilter', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMICAFFILIATELOCATIONSETFILTER,
  '__module__' : 'google.ads.googleads.v8.common.feed_item_set_filter_type_infos_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.common.DynamicAffiliateLocationSetFilter)
  })
_sym_db.RegisterMessage(DynamicAffiliateLocationSetFilter)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
