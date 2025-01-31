# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/group_placement_view.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import placement_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_placement__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/resources/group_placement_view.proto',
  package='google.ads.googleads.v9.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v9.resourcesB\027GroupPlacementViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<google/ads/googleads/v9/resources/group_placement_view.proto\x12!google.ads.googleads.v9.resources\x1a\x32google/ads/googleads/v9/enums/placement_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\x8b\x04\n\x12GroupPlacementView\x12Y\n\rresource_name\x18\x01 \x01(\tB4\xe2\x41\x01\x03\xfa\x41-\n+googleads.googleapis.com/GroupPlacementViewR\x0cresourceName\x12\'\n\tplacement\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03H\x00R\tplacement\x88\x01\x01\x12,\n\x0c\x64isplay_name\x18\x07 \x01(\tB\x04\xe2\x41\x01\x03H\x01R\x0b\x64isplayName\x88\x01\x01\x12(\n\ntarget_url\x18\x08 \x01(\tB\x04\xe2\x41\x01\x03H\x02R\ttargetUrl\x88\x01\x01\x12k\n\x0eplacement_type\x18\x05 \x01(\x0e\x32>.google.ads.googleads.v9.enums.PlacementTypeEnum.PlacementTypeB\x04\xe2\x41\x01\x03R\rplacementType:~\xea\x41{\n+googleads.googleapis.com/GroupPlacementView\x12Lcustomers/{customer_id}/groupPlacementViews/{ad_group_id}~{base64_placement}B\x0c\n\n_placementB\x0f\n\r_display_nameB\r\n\x0b_target_urlB\x84\x02\n%com.google.ads.googleads.v9.resourcesB\x17GroupPlacementViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_placement__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GROUPPLACEMENTVIEW = _descriptor.Descriptor(
  name='GroupPlacementView',
  full_name='google.ads.googleads.v9.resources.GroupPlacementView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v9.resources.GroupPlacementView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003\372A-\n+googleads.googleapis.com/GroupPlacementView', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='placement', full_name='google.ads.googleads.v9.resources.GroupPlacementView.placement', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='placement', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.ads.googleads.v9.resources.GroupPlacementView.display_name', index=2,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='displayName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_url', full_name='google.ads.googleads.v9.resources.GroupPlacementView.target_url', index=3,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='targetUrl', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='placement_type', full_name='google.ads.googleads.v9.resources.GroupPlacementView.placement_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='placementType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A{\n+googleads.googleapis.com/GroupPlacementView\022Lcustomers/{customer_id}/groupPlacementViews/{ad_group_id}~{base64_placement}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_placement', full_name='google.ads.googleads.v9.resources.GroupPlacementView._placement',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_display_name', full_name='google.ads.googleads.v9.resources.GroupPlacementView._display_name',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_target_url', full_name='google.ads.googleads.v9.resources.GroupPlacementView._target_url',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=242,
  serialized_end=765,
)

_GROUPPLACEMENTVIEW.fields_by_name['placement_type'].enum_type = google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_placement__type__pb2._PLACEMENTTYPEENUM_PLACEMENTTYPE
_GROUPPLACEMENTVIEW.oneofs_by_name['_placement'].fields.append(
  _GROUPPLACEMENTVIEW.fields_by_name['placement'])
_GROUPPLACEMENTVIEW.fields_by_name['placement'].containing_oneof = _GROUPPLACEMENTVIEW.oneofs_by_name['_placement']
_GROUPPLACEMENTVIEW.oneofs_by_name['_display_name'].fields.append(
  _GROUPPLACEMENTVIEW.fields_by_name['display_name'])
_GROUPPLACEMENTVIEW.fields_by_name['display_name'].containing_oneof = _GROUPPLACEMENTVIEW.oneofs_by_name['_display_name']
_GROUPPLACEMENTVIEW.oneofs_by_name['_target_url'].fields.append(
  _GROUPPLACEMENTVIEW.fields_by_name['target_url'])
_GROUPPLACEMENTVIEW.fields_by_name['target_url'].containing_oneof = _GROUPPLACEMENTVIEW.oneofs_by_name['_target_url']
DESCRIPTOR.message_types_by_name['GroupPlacementView'] = _GROUPPLACEMENTVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GroupPlacementView = _reflection.GeneratedProtocolMessageType('GroupPlacementView', (_message.Message,), {
  'DESCRIPTOR' : _GROUPPLACEMENTVIEW,
  '__module__' : 'google.ads.googleads.v9.resources.group_placement_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.GroupPlacementView)
  })
_sym_db.RegisterMessage(GroupPlacementView)


DESCRIPTOR._options = None
_GROUPPLACEMENTVIEW.fields_by_name['resource_name']._options = None
_GROUPPLACEMENTVIEW.fields_by_name['placement']._options = None
_GROUPPLACEMENTVIEW.fields_by_name['display_name']._options = None
_GROUPPLACEMENTVIEW.fields_by_name['target_url']._options = None
_GROUPPLACEMENTVIEW.fields_by_name['placement_type']._options = None
_GROUPPLACEMENTVIEW._options = None
# @@protoc_insertion_point(module_scope)
