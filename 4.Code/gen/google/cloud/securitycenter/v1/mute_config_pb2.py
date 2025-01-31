# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/securitycenter/v1/mute_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/securitycenter/v1/mute_config.proto',
  package='google.cloud.securitycenter.v1',
  syntax='proto3',
  serialized_options=b'\n\"com.google.cloud.securitycenter.v1B\017MuteConfigProtoP\001ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\252\002\036Google.Cloud.SecurityCenter.V1\312\002\036Google\\Cloud\\SecurityCenter\\V1\352\002!Google::Cloud::SecurityCenter::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0google/cloud/securitycenter/v1/mute_config.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x84\x04\n\nMuteConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12%\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x02\x18\x01R\x0b\x64isplayName\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1c\n\x06\x66ilter\x18\x04 \x01(\tB\x04\xe2\x41\x01\x02R\x06\x66ilter\x12\x41\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12\x32\n\x12most_recent_editor\x18\x07 \x01(\tB\x04\xe2\x41\x01\x03R\x10mostRecentEditor:\xc0\x01\xea\x41\xbc\x01\n(securitycenter.googleapis.com/MuteConfig\x12\x36organizations/{organization}/muteConfigs/{mute_config}\x12*folders/{folder}/muteConfigs/{mute_config}\x12,projects/{project}/muteConfigs/{mute_config}B\xeb\x01\n\"com.google.cloud.securitycenter.v1B\x0fMuteConfigProtoP\x01ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_MUTECONFIG = _descriptor.Descriptor(
  name='MuteConfig',
  full_name='google.cloud.securitycenter.v1.MuteConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.securitycenter.v1.MuteConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.securitycenter.v1.MuteConfig.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', json_name='displayName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.securitycenter.v1.MuteConfig.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.cloud.securitycenter.v1.MuteConfig.filter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='filter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.securitycenter.v1.MuteConfig.create_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='createTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.cloud.securitycenter.v1.MuteConfig.update_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='updateTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='most_recent_editor', full_name='google.cloud.securitycenter.v1.MuteConfig.most_recent_editor', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='mostRecentEditor', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A\274\001\n(securitycenter.googleapis.com/MuteConfig\0226organizations/{organization}/muteConfigs/{mute_config}\022*folders/{folder}/muteConfigs/{mute_config}\022,projects/{project}/muteConfigs/{mute_config}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=724,
)

_MUTECONFIG.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MUTECONFIG.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['MuteConfig'] = _MUTECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MuteConfig = _reflection.GeneratedProtocolMessageType('MuteConfig', (_message.Message,), {
  'DESCRIPTOR' : _MUTECONFIG,
  '__module__' : 'google.cloud.securitycenter.v1.mute_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1.MuteConfig)
  })
_sym_db.RegisterMessage(MuteConfig)


DESCRIPTOR._options = None
_MUTECONFIG.fields_by_name['display_name']._options = None
_MUTECONFIG.fields_by_name['filter']._options = None
_MUTECONFIG.fields_by_name['create_time']._options = None
_MUTECONFIG.fields_by_name['update_time']._options = None
_MUTECONFIG.fields_by_name['most_recent_editor']._options = None
_MUTECONFIG._options = None
# @@protoc_insertion_point(module_scope)
