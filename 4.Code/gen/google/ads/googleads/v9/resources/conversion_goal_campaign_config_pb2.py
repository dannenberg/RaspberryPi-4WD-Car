# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/conversion_goal_campaign_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import goal_config_level_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_goal__config__level__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/resources/conversion_goal_campaign_config.proto',
  package='google.ads.googleads.v9.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v9.resourcesB!ConversionGoalCampaignConfigProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nGgoogle/ads/googleads/v9/resources/conversion_goal_campaign_config.proto\x12!google.ads.googleads.v9.resources\x1a\x35google/ads/googleads/v9/enums/goal_config_level.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xa6\x04\n\x1c\x43onversionGoalCampaignConfig\x12\x63\n\rresource_name\x18\x01 \x01(\tB>\xe2\x41\x01\x05\xfa\x41\x37\n5googleads.googleapis.com/ConversionGoalCampaignConfigR\x0cresourceName\x12\x46\n\x08\x63\x61mpaign\x18\x02 \x01(\tB*\xe2\x41\x01\x05\xfa\x41#\n!googleads.googleapis.com/CampaignR\x08\x63\x61mpaign\x12n\n\x11goal_config_level\x18\x03 \x01(\x0e\x32\x42.google.ads.googleads.v9.enums.GoalConfigLevelEnum.GoalConfigLevelR\x0fgoalConfigLevel\x12h\n\x16\x63ustom_conversion_goal\x18\x04 \x01(\tB2\xfa\x41/\n-googleads.googleapis.com/CustomConversionGoalR\x14\x63ustomConversionGoal:\x7f\xea\x41|\n5googleads.googleapis.com/ConversionGoalCampaignConfig\x12\x43\x63ustomers/{customer_id}/conversionGoalCampaignConfigs/{campaign_id}B\x8e\x02\n%com.google.ads.googleads.v9.resourcesB!ConversionGoalCampaignConfigProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_goal__config__level__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CONVERSIONGOALCAMPAIGNCONFIG = _descriptor.Descriptor(
  name='ConversionGoalCampaignConfig',
  full_name='google.ads.googleads.v9.resources.ConversionGoalCampaignConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v9.resources.ConversionGoalCampaignConfig.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A7\n5googleads.googleapis.com/ConversionGoalCampaignConfig', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v9.resources.ConversionGoalCampaignConfig.campaign', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A#\n!googleads.googleapis.com/Campaign', json_name='campaign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='goal_config_level', full_name='google.ads.googleads.v9.resources.ConversionGoalCampaignConfig.goal_config_level', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='goalConfigLevel', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_conversion_goal', full_name='google.ads.googleads.v9.resources.ConversionGoalCampaignConfig.custom_conversion_goal', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A/\n-googleads.googleapis.com/CustomConversionGoal', json_name='customConversionGoal', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A|\n5googleads.googleapis.com/ConversionGoalCampaignConfig\022Ccustomers/{customer_id}/conversionGoalCampaignConfigs/{campaign_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=806,
)

_CONVERSIONGOALCAMPAIGNCONFIG.fields_by_name['goal_config_level'].enum_type = google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_goal__config__level__pb2._GOALCONFIGLEVELENUM_GOALCONFIGLEVEL
DESCRIPTOR.message_types_by_name['ConversionGoalCampaignConfig'] = _CONVERSIONGOALCAMPAIGNCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConversionGoalCampaignConfig = _reflection.GeneratedProtocolMessageType('ConversionGoalCampaignConfig', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSIONGOALCAMPAIGNCONFIG,
  '__module__' : 'google.ads.googleads.v9.resources.conversion_goal_campaign_config_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.ConversionGoalCampaignConfig)
  })
_sym_db.RegisterMessage(ConversionGoalCampaignConfig)


DESCRIPTOR._options = None
_CONVERSIONGOALCAMPAIGNCONFIG.fields_by_name['resource_name']._options = None
_CONVERSIONGOALCAMPAIGNCONFIG.fields_by_name['campaign']._options = None
_CONVERSIONGOALCAMPAIGNCONFIG.fields_by_name['custom_conversion_goal']._options = None
_CONVERSIONGOALCAMPAIGNCONFIG._options = None
# @@protoc_insertion_point(module_scope)
