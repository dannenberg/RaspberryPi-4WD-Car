# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/campaign_conversion_goal_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.resources import campaign_conversion_goal_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__conversion__goal__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/services/campaign_conversion_goal_service.proto',
  package='google.ads.googleads.v9.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v9.servicesB\"CampaignConversionGoalServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nGgoogle/ads/googleads/v9/services/campaign_conversion_goal_service.proto\x12 google.ads.googleads.v9.services\x1a@google/ads/googleads/v9/resources/campaign_conversion_goal.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a google/protobuf/field_mask.proto\"\xdb\x01\n$MutateCampaignConversionGoalsRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12g\n\noperations\x18\x02 \x03(\x0b\x32\x41.google.ads.googleads.v9.services.CampaignConversionGoalOperationB\x04\xe2\x41\x01\x02R\noperations\x12#\n\rvalidate_only\x18\x03 \x01(\x08R\x0cvalidateOnly\"\xc0\x01\n\x1f\x43\x61mpaignConversionGoalOperation\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12S\n\x06update\x18\x01 \x01(\x0b\x32\x39.google.ads.googleads.v9.resources.CampaignConversionGoalH\x00R\x06updateB\x0b\n\toperation\"\x87\x01\n%MutateCampaignConversionGoalsResponse\x12^\n\x07results\x18\x01 \x03(\x0b\x32\x44.google.ads.googleads.v9.services.MutateCampaignConversionGoalResultR\x07results\"I\n\"MutateCampaignConversionGoalResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName2\xfb\x02\n\x1d\x43\x61mpaignConversionGoalService\x12\x92\x02\n\x1dMutateCampaignConversionGoals\x12\x46.google.ads.googleads.v9.services.MutateCampaignConversionGoalsRequest\x1aG.google.ads.googleads.v9.services.MutateCampaignConversionGoalsResponse\"`\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02\x41\"</v9/customers/{customer_id=*}/campaignConversionGoals:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x89\x02\n$com.google.ads.googleads.v9.servicesB\"CampaignConversionGoalServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__conversion__goal__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_MUTATECAMPAIGNCONVERSIONGOALSREQUEST = _descriptor.Descriptor(
  name='MutateCampaignConversionGoalsRequest',
  full_name='google.ads.googleads.v9.services.MutateCampaignConversionGoalsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v9.services.MutateCampaignConversionGoalsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='customerId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v9.services.MutateCampaignConversionGoalsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='operations', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v9.services.MutateCampaignConversionGoalsRequest.validate_only', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='validateOnly', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=298,
  serialized_end=517,
)


_CAMPAIGNCONVERSIONGOALOPERATION = _descriptor.Descriptor(
  name='CampaignConversionGoalOperation',
  full_name='google.ads.googleads.v9.services.CampaignConversionGoalOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v9.services.CampaignConversionGoalOperation.update_mask', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='updateMask', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v9.services.CampaignConversionGoalOperation.update', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='update', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v9.services.CampaignConversionGoalOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=520,
  serialized_end=712,
)


_MUTATECAMPAIGNCONVERSIONGOALSRESPONSE = _descriptor.Descriptor(
  name='MutateCampaignConversionGoalsResponse',
  full_name='google.ads.googleads.v9.services.MutateCampaignConversionGoalsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v9.services.MutateCampaignConversionGoalsResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='results', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=715,
  serialized_end=850,
)


_MUTATECAMPAIGNCONVERSIONGOALRESULT = _descriptor.Descriptor(
  name='MutateCampaignConversionGoalResult',
  full_name='google.ads.googleads.v9.services.MutateCampaignConversionGoalResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v9.services.MutateCampaignConversionGoalResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=852,
  serialized_end=925,
)

_MUTATECAMPAIGNCONVERSIONGOALSREQUEST.fields_by_name['operations'].message_type = _CAMPAIGNCONVERSIONGOALOPERATION
_CAMPAIGNCONVERSIONGOALOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CAMPAIGNCONVERSIONGOALOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__conversion__goal__pb2._CAMPAIGNCONVERSIONGOAL
_CAMPAIGNCONVERSIONGOALOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNCONVERSIONGOALOPERATION.fields_by_name['update'])
_CAMPAIGNCONVERSIONGOALOPERATION.fields_by_name['update'].containing_oneof = _CAMPAIGNCONVERSIONGOALOPERATION.oneofs_by_name['operation']
_MUTATECAMPAIGNCONVERSIONGOALSRESPONSE.fields_by_name['results'].message_type = _MUTATECAMPAIGNCONVERSIONGOALRESULT
DESCRIPTOR.message_types_by_name['MutateCampaignConversionGoalsRequest'] = _MUTATECAMPAIGNCONVERSIONGOALSREQUEST
DESCRIPTOR.message_types_by_name['CampaignConversionGoalOperation'] = _CAMPAIGNCONVERSIONGOALOPERATION
DESCRIPTOR.message_types_by_name['MutateCampaignConversionGoalsResponse'] = _MUTATECAMPAIGNCONVERSIONGOALSRESPONSE
DESCRIPTOR.message_types_by_name['MutateCampaignConversionGoalResult'] = _MUTATECAMPAIGNCONVERSIONGOALRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MutateCampaignConversionGoalsRequest = _reflection.GeneratedProtocolMessageType('MutateCampaignConversionGoalsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNCONVERSIONGOALSREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateCampaignConversionGoalsRequest)
  })
_sym_db.RegisterMessage(MutateCampaignConversionGoalsRequest)

CampaignConversionGoalOperation = _reflection.GeneratedProtocolMessageType('CampaignConversionGoalOperation', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNCONVERSIONGOALOPERATION,
  '__module__' : 'google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.CampaignConversionGoalOperation)
  })
_sym_db.RegisterMessage(CampaignConversionGoalOperation)

MutateCampaignConversionGoalsResponse = _reflection.GeneratedProtocolMessageType('MutateCampaignConversionGoalsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNCONVERSIONGOALSRESPONSE,
  '__module__' : 'google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateCampaignConversionGoalsResponse)
  })
_sym_db.RegisterMessage(MutateCampaignConversionGoalsResponse)

MutateCampaignConversionGoalResult = _reflection.GeneratedProtocolMessageType('MutateCampaignConversionGoalResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNCONVERSIONGOALRESULT,
  '__module__' : 'google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateCampaignConversionGoalResult)
  })
_sym_db.RegisterMessage(MutateCampaignConversionGoalResult)


DESCRIPTOR._options = None
_MUTATECAMPAIGNCONVERSIONGOALSREQUEST.fields_by_name['customer_id']._options = None
_MUTATECAMPAIGNCONVERSIONGOALSREQUEST.fields_by_name['operations']._options = None

_CAMPAIGNCONVERSIONGOALSERVICE = _descriptor.ServiceDescriptor(
  name='CampaignConversionGoalService',
  full_name='google.ads.googleads.v9.services.CampaignConversionGoalService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords',
  create_key=_descriptor._internal_create_key,
  serialized_start=928,
  serialized_end=1307,
  methods=[
  _descriptor.MethodDescriptor(
    name='MutateCampaignConversionGoals',
    full_name='google.ads.googleads.v9.services.CampaignConversionGoalService.MutateCampaignConversionGoals',
    index=0,
    containing_service=None,
    input_type=_MUTATECAMPAIGNCONVERSIONGOALSREQUEST,
    output_type=_MUTATECAMPAIGNCONVERSIONGOALSRESPONSE,
    serialized_options=b'\332A\026customer_id,operations\202\323\344\223\002A\"</v9/customers/{customer_id=*}/campaignConversionGoals:mutate:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMPAIGNCONVERSIONGOALSERVICE)

DESCRIPTOR.services_by_name['CampaignConversionGoalService'] = _CAMPAIGNCONVERSIONGOALSERVICE

# @@protoc_insertion_point(module_scope)
