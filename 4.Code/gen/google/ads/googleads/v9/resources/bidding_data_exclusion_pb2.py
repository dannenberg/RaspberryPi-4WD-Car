# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/bidding_data_exclusion.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import advertising_channel_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_advertising__channel__type__pb2
from google.ads.googleads.v9.enums import device_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_device__pb2
from google.ads.googleads.v9.enums import seasonality_event_scope_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_seasonality__event__scope__pb2
from google.ads.googleads.v9.enums import seasonality_event_status_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_seasonality__event__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/resources/bidding_data_exclusion.proto',
  package='google.ads.googleads.v9.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v9.resourcesB\031BiddingDataExclusionProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>google/ads/googleads/v9/resources/bidding_data_exclusion.proto\x12!google.ads.googleads.v9.resources\x1a<google/ads/googleads/v9/enums/advertising_channel_type.proto\x1a*google/ads/googleads/v9/enums/device.proto\x1a;google/ads/googleads/v9/enums/seasonality_event_scope.proto\x1a<google/ads/googleads/v9/enums/seasonality_event_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xa4\x07\n\x14\x42iddingDataExclusion\x12[\n\rresource_name\x18\x01 \x01(\tB6\xe2\x41\x01\x05\xfa\x41/\n-googleads.googleapis.com/BiddingDataExclusionR\x0cresourceName\x12\x30\n\x11\x64\x61ta_exclusion_id\x18\x02 \x01(\x03\x42\x04\xe2\x41\x01\x03R\x0f\x64\x61taExclusionId\x12\x64\n\x05scope\x18\x03 \x01(\x0e\x32N.google.ads.googleads.v9.enums.SeasonalityEventScopeEnum.SeasonalityEventScopeR\x05scope\x12n\n\x06status\x18\x04 \x01(\x0e\x32P.google.ads.googleads.v9.enums.SeasonalityEventStatusEnum.SeasonalityEventStatusB\x04\xe2\x41\x01\x03R\x06status\x12,\n\x0fstart_date_time\x18\x05 \x01(\tB\x04\xe2\x41\x01\x02R\rstartDateTime\x12(\n\rend_date_time\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02R\x0b\x65ndDateTime\x12\x12\n\x04name\x18\x07 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\x12J\n\x07\x64\x65vices\x18\t \x03(\x0e\x32\x30.google.ads.googleads.v9.enums.DeviceEnum.DeviceR\x07\x64\x65vices\x12\x44\n\tcampaigns\x18\n \x03(\tB&\xfa\x41#\n!googleads.googleapis.com/CampaignR\tcampaigns\x12\x8c\x01\n\x19\x61\x64vertising_channel_types\x18\x0b \x03(\x0e\x32P.google.ads.googleads.v9.enums.AdvertisingChannelTypeEnum.AdvertisingChannelTypeR\x17\x61\x64vertisingChannelTypes:x\xea\x41u\n-googleads.googleapis.com/BiddingDataExclusion\x12\x44\x63ustomers/{customer_id}/biddingDataExclusions/{seasonality_event_id}B\x86\x02\n%com.google.ads.googleads.v9.resourcesB\x19\x42iddingDataExclusionProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_advertising__channel__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_device__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_seasonality__event__scope__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_seasonality__event__status__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_BIDDINGDATAEXCLUSION = _descriptor.Descriptor(
  name='BiddingDataExclusion',
  full_name='google.ads.googleads.v9.resources.BiddingDataExclusion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v9.resources.BiddingDataExclusion.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A/\n-googleads.googleapis.com/BiddingDataExclusion', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_exclusion_id', full_name='google.ads.googleads.v9.resources.BiddingDataExclusion.data_exclusion_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='dataExclusionId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scope', full_name='google.ads.googleads.v9.resources.BiddingDataExclusion.scope', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='scope', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v9.resources.BiddingDataExclusion.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date_time', full_name='google.ads.googleads.v9.resources.BiddingDataExclusion.start_date_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='startDateTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_date_time', full_name='google.ads.googleads.v9.resources.BiddingDataExclusion.end_date_time', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='endDateTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v9.resources.BiddingDataExclusion.name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.ads.googleads.v9.resources.BiddingDataExclusion.description', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='devices', full_name='google.ads.googleads.v9.resources.BiddingDataExclusion.devices', index=8,
      number=9, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='devices', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaigns', full_name='google.ads.googleads.v9.resources.BiddingDataExclusion.campaigns', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A#\n!googleads.googleapis.com/Campaign', json_name='campaigns', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='advertising_channel_types', full_name='google.ads.googleads.v9.resources.BiddingDataExclusion.advertising_channel_types', index=10,
      number=11, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='advertisingChannelTypes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Au\n-googleads.googleapis.com/BiddingDataExclusion\022Dcustomers/{customer_id}/biddingDataExclusions/{seasonality_event_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=1353,
)

_BIDDINGDATAEXCLUSION.fields_by_name['scope'].enum_type = google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_seasonality__event__scope__pb2._SEASONALITYEVENTSCOPEENUM_SEASONALITYEVENTSCOPE
_BIDDINGDATAEXCLUSION.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_seasonality__event__status__pb2._SEASONALITYEVENTSTATUSENUM_SEASONALITYEVENTSTATUS
_BIDDINGDATAEXCLUSION.fields_by_name['devices'].enum_type = google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_device__pb2._DEVICEENUM_DEVICE
_BIDDINGDATAEXCLUSION.fields_by_name['advertising_channel_types'].enum_type = google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_advertising__channel__type__pb2._ADVERTISINGCHANNELTYPEENUM_ADVERTISINGCHANNELTYPE
DESCRIPTOR.message_types_by_name['BiddingDataExclusion'] = _BIDDINGDATAEXCLUSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BiddingDataExclusion = _reflection.GeneratedProtocolMessageType('BiddingDataExclusion', (_message.Message,), {
  'DESCRIPTOR' : _BIDDINGDATAEXCLUSION,
  '__module__' : 'google.ads.googleads.v9.resources.bidding_data_exclusion_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.BiddingDataExclusion)
  })
_sym_db.RegisterMessage(BiddingDataExclusion)


DESCRIPTOR._options = None
_BIDDINGDATAEXCLUSION.fields_by_name['resource_name']._options = None
_BIDDINGDATAEXCLUSION.fields_by_name['data_exclusion_id']._options = None
_BIDDINGDATAEXCLUSION.fields_by_name['status']._options = None
_BIDDINGDATAEXCLUSION.fields_by_name['start_date_time']._options = None
_BIDDINGDATAEXCLUSION.fields_by_name['end_date_time']._options = None
_BIDDINGDATAEXCLUSION.fields_by_name['campaigns']._options = None
_BIDDINGDATAEXCLUSION._options = None
# @@protoc_insertion_point(module_scope)
