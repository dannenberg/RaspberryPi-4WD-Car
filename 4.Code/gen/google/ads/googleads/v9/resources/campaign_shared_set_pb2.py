# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/campaign_shared_set.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import campaign_shared_set_status_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_campaign__shared__set__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/resources/campaign_shared_set.proto',
  package='google.ads.googleads.v9.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v9.resourcesB\026CampaignSharedSetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;google/ads/googleads/v9/resources/campaign_shared_set.proto\x12!google.ads.googleads.v9.resources\x1a>google/ads/googleads/v9/enums/campaign_shared_set_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\x94\x04\n\x11\x43\x61mpaignSharedSet\x12X\n\rresource_name\x18\x01 \x01(\tB3\xe2\x41\x01\x05\xfa\x41,\n*googleads.googleapis.com/CampaignSharedSetR\x0cresourceName\x12K\n\x08\x63\x61mpaign\x18\x05 \x01(\tB*\xe2\x41\x01\x05\xfa\x41#\n!googleads.googleapis.com/CampaignH\x00R\x08\x63\x61mpaign\x88\x01\x01\x12O\n\nshared_set\x18\x06 \x01(\tB+\xe2\x41\x01\x05\xfa\x41$\n\"googleads.googleapis.com/SharedSetH\x01R\tsharedSet\x88\x01\x01\x12p\n\x06status\x18\x02 \x01(\x0e\x32R.google.ads.googleads.v9.enums.CampaignSharedSetStatusEnum.CampaignSharedSetStatusB\x04\xe2\x41\x01\x03R\x06status:y\xea\x41v\n*googleads.googleapis.com/CampaignSharedSet\x12Hcustomers/{customer_id}/campaignSharedSets/{campaign_id}~{shared_set_id}B\x0b\n\t_campaignB\r\n\x0b_shared_setB\x83\x02\n%com.google.ads.googleads.v9.resourcesB\x16\x43\x61mpaignSharedSetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_campaign__shared__set__status__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CAMPAIGNSHAREDSET = _descriptor.Descriptor(
  name='CampaignSharedSet',
  full_name='google.ads.googleads.v9.resources.CampaignSharedSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v9.resources.CampaignSharedSet.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A,\n*googleads.googleapis.com/CampaignSharedSet', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v9.resources.CampaignSharedSet.campaign', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A#\n!googleads.googleapis.com/Campaign', json_name='campaign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shared_set', full_name='google.ads.googleads.v9.resources.CampaignSharedSet.shared_set', index=2,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A$\n\"googleads.googleapis.com/SharedSet', json_name='sharedSet', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v9.resources.CampaignSharedSet.status', index=3,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Av\n*googleads.googleapis.com/CampaignSharedSet\022Hcustomers/{customer_id}/campaignSharedSets/{campaign_id}~{shared_set_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_campaign', full_name='google.ads.googleads.v9.resources.CampaignSharedSet._campaign',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_shared_set', full_name='google.ads.googleads.v9.resources.CampaignSharedSet._shared_set',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=253,
  serialized_end=785,
)

_CAMPAIGNSHAREDSET.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_campaign__shared__set__status__pb2._CAMPAIGNSHAREDSETSTATUSENUM_CAMPAIGNSHAREDSETSTATUS
_CAMPAIGNSHAREDSET.oneofs_by_name['_campaign'].fields.append(
  _CAMPAIGNSHAREDSET.fields_by_name['campaign'])
_CAMPAIGNSHAREDSET.fields_by_name['campaign'].containing_oneof = _CAMPAIGNSHAREDSET.oneofs_by_name['_campaign']
_CAMPAIGNSHAREDSET.oneofs_by_name['_shared_set'].fields.append(
  _CAMPAIGNSHAREDSET.fields_by_name['shared_set'])
_CAMPAIGNSHAREDSET.fields_by_name['shared_set'].containing_oneof = _CAMPAIGNSHAREDSET.oneofs_by_name['_shared_set']
DESCRIPTOR.message_types_by_name['CampaignSharedSet'] = _CAMPAIGNSHAREDSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignSharedSet = _reflection.GeneratedProtocolMessageType('CampaignSharedSet', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNSHAREDSET,
  '__module__' : 'google.ads.googleads.v9.resources.campaign_shared_set_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.CampaignSharedSet)
  })
_sym_db.RegisterMessage(CampaignSharedSet)


DESCRIPTOR._options = None
_CAMPAIGNSHAREDSET.fields_by_name['resource_name']._options = None
_CAMPAIGNSHAREDSET.fields_by_name['campaign']._options = None
_CAMPAIGNSHAREDSET.fields_by_name['shared_set']._options = None
_CAMPAIGNSHAREDSET.fields_by_name['status']._options = None
_CAMPAIGNSHAREDSET._options = None
# @@protoc_insertion_point(module_scope)
