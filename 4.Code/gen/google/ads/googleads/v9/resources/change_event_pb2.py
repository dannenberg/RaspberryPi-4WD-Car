# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/change_event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import ad_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_ad__type__pb2
from google.ads.googleads.v9.enums import advertising_channel_sub_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_advertising__channel__sub__type__pb2
from google.ads.googleads.v9.enums import advertising_channel_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_advertising__channel__type__pb2
from google.ads.googleads.v9.enums import asset_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_asset__type__pb2
from google.ads.googleads.v9.enums import change_client_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_change__client__type__pb2
from google.ads.googleads.v9.enums import change_event_resource_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_change__event__resource__type__pb2
from google.ads.googleads.v9.enums import criterion_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_criterion__type__pb2
from google.ads.googleads.v9.enums import feed_origin_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_feed__origin__pb2
from google.ads.googleads.v9.enums import resource_change_operation_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_resource__change__operation__pb2
from google.ads.googleads.v9.resources import ad_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__pb2
from google.ads.googleads.v9.resources import ad_group_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__pb2
from google.ads.googleads.v9.resources import ad_group_ad_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__ad__pb2
from google.ads.googleads.v9.resources import ad_group_asset_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__asset__pb2
from google.ads.googleads.v9.resources import ad_group_bid_modifier_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__bid__modifier__pb2
from google.ads.googleads.v9.resources import ad_group_criterion_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__criterion__pb2
from google.ads.googleads.v9.resources import ad_group_feed_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__feed__pb2
from google.ads.googleads.v9.resources import asset_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_asset__pb2
from google.ads.googleads.v9.resources import campaign_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__pb2
from google.ads.googleads.v9.resources import campaign_asset_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__asset__pb2
from google.ads.googleads.v9.resources import campaign_budget_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__budget__pb2
from google.ads.googleads.v9.resources import campaign_criterion_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__criterion__pb2
from google.ads.googleads.v9.resources import campaign_feed_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__feed__pb2
from google.ads.googleads.v9.resources import customer_asset_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_customer__asset__pb2
from google.ads.googleads.v9.resources import feed_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_feed__pb2
from google.ads.googleads.v9.resources import feed_item_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_feed__item__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/resources/change_event.proto',
  package='google.ads.googleads.v9.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v9.resourcesB\020ChangeEventProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4google/ads/googleads/v9/resources/change_event.proto\x12!google.ads.googleads.v9.resources\x1a+google/ads/googleads/v9/enums/ad_type.proto\x1a@google/ads/googleads/v9/enums/advertising_channel_sub_type.proto\x1a<google/ads/googleads/v9/enums/advertising_channel_type.proto\x1a.google/ads/googleads/v9/enums/asset_type.proto\x1a\x36google/ads/googleads/v9/enums/change_client_type.proto\x1a>google/ads/googleads/v9/enums/change_event_resource_type.proto\x1a\x32google/ads/googleads/v9/enums/criterion_type.proto\x1a/google/ads/googleads/v9/enums/feed_origin.proto\x1a=google/ads/googleads/v9/enums/resource_change_operation.proto\x1a*google/ads/googleads/v9/resources/ad.proto\x1a\x30google/ads/googleads/v9/resources/ad_group.proto\x1a\x33google/ads/googleads/v9/resources/ad_group_ad.proto\x1a\x36google/ads/googleads/v9/resources/ad_group_asset.proto\x1a=google/ads/googleads/v9/resources/ad_group_bid_modifier.proto\x1a:google/ads/googleads/v9/resources/ad_group_criterion.proto\x1a\x35google/ads/googleads/v9/resources/ad_group_feed.proto\x1a-google/ads/googleads/v9/resources/asset.proto\x1a\x30google/ads/googleads/v9/resources/campaign.proto\x1a\x36google/ads/googleads/v9/resources/campaign_asset.proto\x1a\x37google/ads/googleads/v9/resources/campaign_budget.proto\x1a:google/ads/googleads/v9/resources/campaign_criterion.proto\x1a\x35google/ads/googleads/v9/resources/campaign_feed.proto\x1a\x36google/ads/googleads/v9/resources/customer_asset.proto\x1a,google/ads/googleads/v9/resources/feed.proto\x1a\x31google/ads/googleads/v9/resources/feed_item.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\"\x81\x16\n\x0b\x43hangeEvent\x12R\n\rresource_name\x18\x01 \x01(\tB-\xe2\x41\x01\x03\xfa\x41&\n$googleads.googleapis.com/ChangeEventR\x0cresourceName\x12.\n\x10\x63hange_date_time\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x0e\x63hangeDateTime\x12\x8a\x01\n\x14\x63hange_resource_type\x18\x03 \x01(\x0e\x32R.google.ads.googleads.v9.enums.ChangeEventResourceTypeEnum.ChangeEventResourceTypeB\x04\xe2\x41\x01\x03R\x12\x63hangeResourceType\x12\x36\n\x14\x63hange_resource_name\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03R\x12\x63hangeResourceName\x12k\n\x0b\x63lient_type\x18\x05 \x01(\x0e\x32\x44.google.ads.googleads.v9.enums.ChangeClientTypeEnum.ChangeClientTypeB\x04\xe2\x41\x01\x03R\nclientType\x12#\n\nuser_email\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03R\tuserEmail\x12g\n\x0cold_resource\x18\x07 \x01(\x0b\x32>.google.ads.googleads.v9.resources.ChangeEvent.ChangedResourceB\x04\xe2\x41\x01\x03R\x0boldResource\x12g\n\x0cnew_resource\x18\x08 \x01(\x0b\x32>.google.ads.googleads.v9.resources.ChangeEvent.ChangedResourceB\x04\xe2\x41\x01\x03R\x0bnewResource\x12\x94\x01\n\x19resource_change_operation\x18\t \x01(\x0e\x32R.google.ads.googleads.v9.enums.ResourceChangeOperationEnum.ResourceChangeOperationB\x04\xe2\x41\x01\x03R\x17resourceChangeOperation\x12G\n\x0e\x63hanged_fields\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x03R\rchangedFields\x12\x46\n\x08\x63\x61mpaign\x18\x0b \x01(\tB*\xe2\x41\x01\x03\xfa\x41#\n!googleads.googleapis.com/CampaignR\x08\x63\x61mpaign\x12\x44\n\x08\x61\x64_group\x18\x0c \x01(\tB)\xe2\x41\x01\x03\xfa\x41\"\n googleads.googleapis.com/AdGroupR\x07\x61\x64Group\x12:\n\x04\x66\x65\x65\x64\x18\r \x01(\tB&\xe2\x41\x01\x03\xfa\x41\x1f\n\x1dgoogleads.googleapis.com/FeedR\x04\x66\x65\x65\x64\x12G\n\tfeed_item\x18\x0e \x01(\tB*\xe2\x41\x01\x03\xfa\x41#\n!googleads.googleapis.com/FeedItemR\x08\x66\x65\x65\x64Item\x12=\n\x05\x61sset\x18\x14 \x01(\tB\'\xe2\x41\x01\x03\xfa\x41 \n\x1egoogleads.googleapis.com/AssetR\x05\x61sset\x1a\x8e\x0b\n\x0f\x43hangedResource\x12;\n\x02\x61\x64\x18\x01 \x01(\x0b\x32%.google.ads.googleads.v9.resources.AdB\x04\xe2\x41\x01\x03R\x02\x61\x64\x12K\n\x08\x61\x64_group\x18\x02 \x01(\x0b\x32*.google.ads.googleads.v9.resources.AdGroupB\x04\xe2\x41\x01\x03R\x07\x61\x64Group\x12g\n\x12\x61\x64_group_criterion\x18\x03 \x01(\x0b\x32\x33.google.ads.googleads.v9.resources.AdGroupCriterionB\x04\xe2\x41\x01\x03R\x10\x61\x64GroupCriterion\x12M\n\x08\x63\x61mpaign\x18\x04 \x01(\x0b\x32+.google.ads.googleads.v9.resources.CampaignB\x04\xe2\x41\x01\x03R\x08\x63\x61mpaign\x12`\n\x0f\x63\x61mpaign_budget\x18\x05 \x01(\x0b\x32\x31.google.ads.googleads.v9.resources.CampaignBudgetB\x04\xe2\x41\x01\x03R\x0e\x63\x61mpaignBudget\x12n\n\x15\x61\x64_group_bid_modifier\x18\x06 \x01(\x0b\x32\x35.google.ads.googleads.v9.resources.AdGroupBidModifierB\x04\xe2\x41\x01\x03R\x12\x61\x64GroupBidModifier\x12i\n\x12\x63\x61mpaign_criterion\x18\x07 \x01(\x0b\x32\x34.google.ads.googleads.v9.resources.CampaignCriterionB\x04\xe2\x41\x01\x03R\x11\x63\x61mpaignCriterion\x12\x41\n\x04\x66\x65\x65\x64\x18\x08 \x01(\x0b\x32\'.google.ads.googleads.v9.resources.FeedB\x04\xe2\x41\x01\x03R\x04\x66\x65\x65\x64\x12N\n\tfeed_item\x18\t \x01(\x0b\x32+.google.ads.googleads.v9.resources.FeedItemB\x04\xe2\x41\x01\x03R\x08\x66\x65\x65\x64Item\x12Z\n\rcampaign_feed\x18\n \x01(\x0b\x32/.google.ads.googleads.v9.resources.CampaignFeedB\x04\xe2\x41\x01\x03R\x0c\x63\x61mpaignFeed\x12X\n\rad_group_feed\x18\x0b \x01(\x0b\x32..google.ads.googleads.v9.resources.AdGroupFeedB\x04\xe2\x41\x01\x03R\x0b\x61\x64GroupFeed\x12R\n\x0b\x61\x64_group_ad\x18\x0c \x01(\x0b\x32,.google.ads.googleads.v9.resources.AdGroupAdB\x04\xe2\x41\x01\x03R\tadGroupAd\x12\x44\n\x05\x61sset\x18\r \x01(\x0b\x32(.google.ads.googleads.v9.resources.AssetB\x04\xe2\x41\x01\x03R\x05\x61sset\x12]\n\x0e\x63ustomer_asset\x18\x0e \x01(\x0b\x32\x30.google.ads.googleads.v9.resources.CustomerAssetB\x04\xe2\x41\x01\x03R\rcustomerAsset\x12]\n\x0e\x63\x61mpaign_asset\x18\x0f \x01(\x0b\x32\x30.google.ads.googleads.v9.resources.CampaignAssetB\x04\xe2\x41\x01\x03R\rcampaignAsset\x12[\n\x0e\x61\x64_group_asset\x18\x10 \x01(\x0b\x32/.google.ads.googleads.v9.resources.AdGroupAssetB\x04\xe2\x41\x01\x03R\x0c\x61\x64GroupAsset:\x81\x01\xea\x41~\n$googleads.googleapis.com/ChangeEvent\x12Vcustomers/{customer_id}/changeEvents/{timestamp_micros}~{command_index}~{mutate_index}B\xfd\x01\n%com.google.ads.googleads.v9.resourcesB\x10\x43hangeEventProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_ad__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_advertising__channel__sub__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_advertising__channel__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_asset__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_change__client__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_change__event__resource__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_criterion__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_feed__origin__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_resource__change__operation__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__ad__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__asset__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__bid__modifier__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__criterion__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__feed__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_asset__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__asset__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__budget__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__criterion__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__feed__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_customer__asset__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_feed__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_feed__item__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CHANGEEVENT_CHANGEDRESOURCE = _descriptor.Descriptor(
  name='ChangedResource',
  full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ad', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.ad', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='ad', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.ad_group', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='adGroup', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_criterion', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.ad_group_criterion', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='adGroupCriterion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.campaign', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='campaign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign_budget', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.campaign_budget', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='campaignBudget', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_bid_modifier', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.ad_group_bid_modifier', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='adGroupBidModifier', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign_criterion', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.campaign_criterion', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='campaignCriterion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.feed', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='feed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed_item', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.feed_item', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='feedItem', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign_feed', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.campaign_feed', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='campaignFeed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_feed', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.ad_group_feed', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='adGroupFeed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_ad', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.ad_group_ad', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='adGroupAd', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.asset', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='asset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_asset', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.customer_asset', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='customerAsset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign_asset', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.campaign_asset', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='campaignAsset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_asset', full_name='google.ads.googleads.v9.resources.ChangeEvent.ChangedResource.ad_group_asset', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='adGroupAsset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2843,
  serialized_end=4265,
)

_CHANGEEVENT = _descriptor.Descriptor(
  name='ChangeEvent',
  full_name='google.ads.googleads.v9.resources.ChangeEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v9.resources.ChangeEvent.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003\372A&\n$googleads.googleapis.com/ChangeEvent', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='change_date_time', full_name='google.ads.googleads.v9.resources.ChangeEvent.change_date_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='changeDateTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='change_resource_type', full_name='google.ads.googleads.v9.resources.ChangeEvent.change_resource_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='changeResourceType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='change_resource_name', full_name='google.ads.googleads.v9.resources.ChangeEvent.change_resource_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='changeResourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_type', full_name='google.ads.googleads.v9.resources.ChangeEvent.client_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='clientType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='google.ads.googleads.v9.resources.ChangeEvent.user_email', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='userEmail', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='old_resource', full_name='google.ads.googleads.v9.resources.ChangeEvent.old_resource', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='oldResource', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_resource', full_name='google.ads.googleads.v9.resources.ChangeEvent.new_resource', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='newResource', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_change_operation', full_name='google.ads.googleads.v9.resources.ChangeEvent.resource_change_operation', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='resourceChangeOperation', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='changed_fields', full_name='google.ads.googleads.v9.resources.ChangeEvent.changed_fields', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='changedFields', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v9.resources.ChangeEvent.campaign', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003\372A#\n!googleads.googleapis.com/Campaign', json_name='campaign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v9.resources.ChangeEvent.ad_group', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003\372A\"\n googleads.googleapis.com/AdGroup', json_name='adGroup', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed', full_name='google.ads.googleads.v9.resources.ChangeEvent.feed', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003\372A\037\n\035googleads.googleapis.com/Feed', json_name='feed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed_item', full_name='google.ads.googleads.v9.resources.ChangeEvent.feed_item', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003\372A#\n!googleads.googleapis.com/FeedItem', json_name='feedItem', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset', full_name='google.ads.googleads.v9.resources.ChangeEvent.asset', index=14,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003\372A \n\036googleads.googleapis.com/Asset', json_name='asset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CHANGEEVENT_CHANGEDRESOURCE, ],
  enum_types=[
  ],
  serialized_options=b'\352A~\n$googleads.googleapis.com/ChangeEvent\022Vcustomers/{customer_id}/changeEvents/{timestamp_micros}~{command_index}~{mutate_index}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1580,
  serialized_end=4397,
)

_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__pb2._AD
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__pb2._ADGROUP
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group_criterion'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__criterion__pb2._ADGROUPCRITERION
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['campaign'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__pb2._CAMPAIGN
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['campaign_budget'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__budget__pb2._CAMPAIGNBUDGET
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group_bid_modifier'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__bid__modifier__pb2._ADGROUPBIDMODIFIER
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['campaign_criterion'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__criterion__pb2._CAMPAIGNCRITERION
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['feed'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_feed__pb2._FEED
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['feed_item'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_feed__item__pb2._FEEDITEM
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['campaign_feed'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__feed__pb2._CAMPAIGNFEED
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group_feed'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__feed__pb2._ADGROUPFEED
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group_ad'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__ad__pb2._ADGROUPAD
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['asset'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_asset__pb2._ASSET
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['customer_asset'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_customer__asset__pb2._CUSTOMERASSET
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['campaign_asset'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__asset__pb2._CAMPAIGNASSET
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group_asset'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__asset__pb2._ADGROUPASSET
_CHANGEEVENT_CHANGEDRESOURCE.containing_type = _CHANGEEVENT
_CHANGEEVENT.fields_by_name['change_resource_type'].enum_type = google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_change__event__resource__type__pb2._CHANGEEVENTRESOURCETYPEENUM_CHANGEEVENTRESOURCETYPE
_CHANGEEVENT.fields_by_name['client_type'].enum_type = google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_change__client__type__pb2._CHANGECLIENTTYPEENUM_CHANGECLIENTTYPE
_CHANGEEVENT.fields_by_name['old_resource'].message_type = _CHANGEEVENT_CHANGEDRESOURCE
_CHANGEEVENT.fields_by_name['new_resource'].message_type = _CHANGEEVENT_CHANGEDRESOURCE
_CHANGEEVENT.fields_by_name['resource_change_operation'].enum_type = google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_resource__change__operation__pb2._RESOURCECHANGEOPERATIONENUM_RESOURCECHANGEOPERATION
_CHANGEEVENT.fields_by_name['changed_fields'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['ChangeEvent'] = _CHANGEEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChangeEvent = _reflection.GeneratedProtocolMessageType('ChangeEvent', (_message.Message,), {

  'ChangedResource' : _reflection.GeneratedProtocolMessageType('ChangedResource', (_message.Message,), {
    'DESCRIPTOR' : _CHANGEEVENT_CHANGEDRESOURCE,
    '__module__' : 'google.ads.googleads.v9.resources.change_event_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.ChangeEvent.ChangedResource)
    })
  ,
  'DESCRIPTOR' : _CHANGEEVENT,
  '__module__' : 'google.ads.googleads.v9.resources.change_event_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.ChangeEvent)
  })
_sym_db.RegisterMessage(ChangeEvent)
_sym_db.RegisterMessage(ChangeEvent.ChangedResource)


DESCRIPTOR._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group_criterion']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['campaign']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['campaign_budget']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group_bid_modifier']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['campaign_criterion']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['feed']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['feed_item']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['campaign_feed']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group_feed']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group_ad']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['asset']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['customer_asset']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['campaign_asset']._options = None
_CHANGEEVENT_CHANGEDRESOURCE.fields_by_name['ad_group_asset']._options = None
_CHANGEEVENT.fields_by_name['resource_name']._options = None
_CHANGEEVENT.fields_by_name['change_date_time']._options = None
_CHANGEEVENT.fields_by_name['change_resource_type']._options = None
_CHANGEEVENT.fields_by_name['change_resource_name']._options = None
_CHANGEEVENT.fields_by_name['client_type']._options = None
_CHANGEEVENT.fields_by_name['user_email']._options = None
_CHANGEEVENT.fields_by_name['old_resource']._options = None
_CHANGEEVENT.fields_by_name['new_resource']._options = None
_CHANGEEVENT.fields_by_name['resource_change_operation']._options = None
_CHANGEEVENT.fields_by_name['changed_fields']._options = None
_CHANGEEVENT.fields_by_name['campaign']._options = None
_CHANGEEVENT.fields_by_name['ad_group']._options = None
_CHANGEEVENT.fields_by_name['feed']._options = None
_CHANGEEVENT.fields_by_name['feed_item']._options = None
_CHANGEEVENT.fields_by_name['asset']._options = None
_CHANGEEVENT._options = None
# @@protoc_insertion_point(module_scope)
