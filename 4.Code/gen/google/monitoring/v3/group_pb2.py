# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/monitoring/v3/group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/monitoring/v3/group.proto',
  package='google.monitoring.v3',
  syntax='proto3',
  serialized_options=b'\n\030com.google.monitoring.v3B\nGroupProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3\352\002\035Google::Cloud::Monitoring::V3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n google/monitoring/v3/group.proto\x12\x14google.monitoring.v3\x1a\x19google/api/resource.proto\"\xb2\x02\n\x05Group\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12\x1f\n\x0bparent_name\x18\x03 \x01(\tR\nparentName\x12\x16\n\x06\x66ilter\x18\x05 \x01(\tR\x06\x66ilter\x12\x1d\n\nis_cluster\x18\x06 \x01(\x08R\tisCluster:\x99\x01\xea\x41\x95\x01\n\x1fmonitoring.googleapis.com/Group\x12!projects/{project}/groups/{group}\x12+organizations/{organization}/groups/{group}\x12\x1f\x66olders/{folder}/groups/{group}\x12\x01*B\xc2\x01\n\x18\x63om.google.monitoring.v3B\nGroupProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GROUP = _descriptor.Descriptor(
  name='Group',
  full_name='google.monitoring.v3.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.monitoring.v3.Group.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.monitoring.v3.Group.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='displayName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_name', full_name='google.monitoring.v3.Group.parent_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parentName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.monitoring.v3.Group.filter', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='filter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_cluster', full_name='google.monitoring.v3.Group.is_cluster', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='isCluster', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A\225\001\n\037monitoring.googleapis.com/Group\022!projects/{project}/groups/{group}\022+organizations/{organization}/groups/{group}\022\037folders/{folder}/groups/{group}\022\001*',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=392,
)

DESCRIPTOR.message_types_by_name['Group'] = _GROUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Group = _reflection.GeneratedProtocolMessageType('Group', (_message.Message,), {
  'DESCRIPTOR' : _GROUP,
  '__module__' : 'google.monitoring.v3.group_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.v3.Group)
  })
_sym_db.RegisterMessage(Group)


DESCRIPTOR._options = None
_GROUP._options = None
# @@protoc_insertion_point(module_scope)
