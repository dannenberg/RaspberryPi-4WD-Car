# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/resources/feed_item_set.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.common import feed_item_set_filter_type_infos_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_common_dot_feed__item__set__filter__type__infos__pb2
from google.ads.googleads.v7.enums import feed_item_set_status_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_feed__item__set__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v7/resources/feed_item_set.proto',
  package='google.ads.googleads.v7.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v7.resourcesB\020FeedItemSetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V7.Resources\312\002!Google\\Ads\\GoogleAds\\V7\\Resources\352\002%Google::Ads::GoogleAds::V7::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5google/ads/googleads/v7/resources/feed_item_set.proto\x12!google.ads.googleads.v7.resources\x1a\x44google/ads/googleads/v7/common/feed_item_set_filter_type_infos.proto\x1a\x38google/ads/googleads/v7/enums/feed_item_set_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xec\x05\n\x0b\x46\x65\x65\x64ItemSet\x12R\n\rresource_name\x18\x01 \x01(\tB-\xe2\x41\x01\x05\xfa\x41&\n$googleads.googleapis.com/FeedItemSetR\x0cresourceName\x12:\n\x04\x66\x65\x65\x64\x18\x02 \x01(\tB&\xe2\x41\x01\x05\xfa\x41\x1f\n\x1dgoogleads.googleapis.com/FeedR\x04\x66\x65\x65\x64\x12-\n\x10\x66\x65\x65\x64_item_set_id\x18\x03 \x01(\x03\x42\x04\xe2\x41\x01\x03R\rfeedItemSetId\x12!\n\x0c\x64isplay_name\x18\x04 \x01(\tR\x0b\x64isplayName\x12\x64\n\x06status\x18\x08 \x01(\x0e\x32\x46.google.ads.googleads.v7.enums.FeedItemSetStatusEnum.FeedItemSetStatusB\x04\xe2\x41\x01\x03R\x06status\x12y\n\x1b\x64ynamic_location_set_filter\x18\x05 \x01(\x0b\x32\x38.google.ads.googleads.v7.common.DynamicLocationSetFilterH\x00R\x18\x64ynamicLocationSetFilter\x12\x95\x01\n%dynamic_affiliate_location_set_filter\x18\x06 \x01(\x0b\x32\x41.google.ads.googleads.v7.common.DynamicAffiliateLocationSetFilterH\x00R!dynamicAffiliateLocationSetFilter:l\xea\x41i\n$googleads.googleapis.com/FeedItemSet\x12\x41\x63ustomers/{customer_id}/feedItemSets/{feed_id}~{feed_item_set_id}B\x14\n\x12\x64ynamic_set_filterB\xfd\x01\n%com.google.ads.googleads.v7.resourcesB\x10\x46\x65\x65\x64ItemSetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V7.Resources\xca\x02!Google\\Ads\\GoogleAds\\V7\\Resources\xea\x02%Google::Ads::GoogleAds::V7::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v7_dot_common_dot_feed__item__set__filter__type__infos__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_feed__item__set__status__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_FEEDITEMSET = _descriptor.Descriptor(
  name='FeedItemSet',
  full_name='google.ads.googleads.v7.resources.FeedItemSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v7.resources.FeedItemSet.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A&\n$googleads.googleapis.com/FeedItemSet', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed', full_name='google.ads.googleads.v7.resources.FeedItemSet.feed', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A\037\n\035googleads.googleapis.com/Feed', json_name='feed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed_item_set_id', full_name='google.ads.googleads.v7.resources.FeedItemSet.feed_item_set_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='feedItemSetId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.ads.googleads.v7.resources.FeedItemSet.display_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='displayName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v7.resources.FeedItemSet.status', index=4,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dynamic_location_set_filter', full_name='google.ads.googleads.v7.resources.FeedItemSet.dynamic_location_set_filter', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dynamicLocationSetFilter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dynamic_affiliate_location_set_filter', full_name='google.ads.googleads.v7.resources.FeedItemSet.dynamic_affiliate_location_set_filter', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dynamicAffiliateLocationSetFilter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Ai\n$googleads.googleapis.com/FeedItemSet\022Acustomers/{customer_id}/feedItemSets/{feed_id}~{feed_item_set_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='dynamic_set_filter', full_name='google.ads.googleads.v7.resources.FeedItemSet.dynamic_set_filter',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=311,
  serialized_end=1059,
)

_FEEDITEMSET.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_feed__item__set__status__pb2._FEEDITEMSETSTATUSENUM_FEEDITEMSETSTATUS
_FEEDITEMSET.fields_by_name['dynamic_location_set_filter'].message_type = google_dot_ads_dot_googleads_dot_v7_dot_common_dot_feed__item__set__filter__type__infos__pb2._DYNAMICLOCATIONSETFILTER
_FEEDITEMSET.fields_by_name['dynamic_affiliate_location_set_filter'].message_type = google_dot_ads_dot_googleads_dot_v7_dot_common_dot_feed__item__set__filter__type__infos__pb2._DYNAMICAFFILIATELOCATIONSETFILTER
_FEEDITEMSET.oneofs_by_name['dynamic_set_filter'].fields.append(
  _FEEDITEMSET.fields_by_name['dynamic_location_set_filter'])
_FEEDITEMSET.fields_by_name['dynamic_location_set_filter'].containing_oneof = _FEEDITEMSET.oneofs_by_name['dynamic_set_filter']
_FEEDITEMSET.oneofs_by_name['dynamic_set_filter'].fields.append(
  _FEEDITEMSET.fields_by_name['dynamic_affiliate_location_set_filter'])
_FEEDITEMSET.fields_by_name['dynamic_affiliate_location_set_filter'].containing_oneof = _FEEDITEMSET.oneofs_by_name['dynamic_set_filter']
DESCRIPTOR.message_types_by_name['FeedItemSet'] = _FEEDITEMSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedItemSet = _reflection.GeneratedProtocolMessageType('FeedItemSet', (_message.Message,), {
  'DESCRIPTOR' : _FEEDITEMSET,
  '__module__' : 'google.ads.googleads.v7.resources.feed_item_set_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.resources.FeedItemSet)
  })
_sym_db.RegisterMessage(FeedItemSet)


DESCRIPTOR._options = None
_FEEDITEMSET.fields_by_name['resource_name']._options = None
_FEEDITEMSET.fields_by_name['feed']._options = None
_FEEDITEMSET.fields_by_name['feed_item_set_id']._options = None
_FEEDITEMSET.fields_by_name['status']._options = None
_FEEDITEMSET._options = None
# @@protoc_insertion_point(module_scope)
