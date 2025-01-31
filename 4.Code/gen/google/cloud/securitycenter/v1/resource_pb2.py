# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/securitycenter/v1/resource.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.securitycenter.v1 import folder_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_folder__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/securitycenter/v1/resource.proto',
  package='google.cloud.securitycenter.v1',
  syntax='proto3',
  serialized_options=b'\n\"com.google.cloud.securitycenter.v1B\rResourceProtoP\001ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\252\002\036Google.Cloud.SecurityCenter.V1\312\002\036Google\\Cloud\\SecurityCenter\\V1\352\002!Google::Cloud::SecurityCenter::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-google/cloud/securitycenter/v1/resource.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a+google/cloud/securitycenter/v1/folder.proto\x1a\x1cgoogle/api/annotations.proto\"\xb1\x02\n\x08Resource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07project\x18\x02 \x01(\tR\x07project\x12\x30\n\x14project_display_name\x18\x03 \x01(\tR\x12projectDisplayName\x12\x16\n\x06parent\x18\x04 \x01(\tR\x06parent\x12.\n\x13parent_display_name\x18\x05 \x01(\tR\x11parentDisplayName\x12\x12\n\x04type\x18\x06 \x01(\tR\x04type\x12\x46\n\x07\x66olders\x18\x07 \x03(\x0b\x32&.google.cloud.securitycenter.v1.FolderB\x04\xe2\x41\x01\x03R\x07\x66olders\x12!\n\x0c\x64isplay_name\x18\x08 \x01(\tR\x0b\x64isplayNameB\xe9\x01\n\"com.google.cloud.securitycenter.v1B\rResourceProtoP\x01ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_cloud_dot_securitycenter_dot_v1_dot_folder__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='google.cloud.securitycenter.v1.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.securitycenter.v1.Resource.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project', full_name='google.cloud.securitycenter.v1.Resource.project', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='project', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_display_name', full_name='google.cloud.securitycenter.v1.Resource.project_display_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='projectDisplayName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.securitycenter.v1.Resource.parent', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_display_name', full_name='google.cloud.securitycenter.v1.Resource.parent_display_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parentDisplayName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.cloud.securitycenter.v1.Resource.type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folders', full_name='google.cloud.securitycenter.v1.Resource.folders', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='folders', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.securitycenter.v1.Resource.display_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='displayName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=190,
  serialized_end=495,
)

_RESOURCE.fields_by_name['folders'].message_type = google_dot_cloud_dot_securitycenter_dot_v1_dot_folder__pb2._FOLDER
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCE,
  '__module__' : 'google.cloud.securitycenter.v1.resource_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1.Resource)
  })
_sym_db.RegisterMessage(Resource)


DESCRIPTOR._options = None
_RESOURCE.fields_by_name['folders']._options = None
# @@protoc_insertion_point(module_scope)
