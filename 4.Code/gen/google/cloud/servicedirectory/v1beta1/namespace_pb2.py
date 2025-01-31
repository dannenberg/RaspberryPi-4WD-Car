# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/servicedirectory/v1beta1/namespace.proto
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
  name='google/cloud/servicedirectory/v1beta1/namespace.proto',
  package='google.cloud.servicedirectory.v1beta1',
  syntax='proto3',
  serialized_options=b'\n)com.google.cloud.servicedirectory.v1beta1B\016NamespaceProtoP\001ZUgoogle.golang.org/genproto/googleapis/cloud/servicedirectory/v1beta1;servicedirectory\370\001\001\252\002%Google.Cloud.ServiceDirectory.V1Beta1\312\002%Google\\Cloud\\ServiceDirectory\\V1beta1\352\002(Google::Cloud::ServiceDirectory::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5google/cloud/servicedirectory/v1beta1/namespace.proto\x12%google.cloud.servicedirectory.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xb2\x03\n\tNamespace\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x05R\x04name\x12Z\n\x06labels\x18\x02 \x03(\x0b\x32<.google.cloud.servicedirectory.v1beta1.Namespace.LabelsEntryB\x04\xe2\x41\x01\x01R\x06labels\x12\x41\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:n\xea\x41k\n)servicedirectory.googleapis.com/Namespace\x12>projects/{project}/locations/{location}/namespaces/{namespace}B\x92\x02\n)com.google.cloud.servicedirectory.v1beta1B\x0eNamespaceProtoP\x01ZUgoogle.golang.org/genproto/googleapis/cloud/servicedirectory/v1beta1;servicedirectory\xf8\x01\x01\xaa\x02%Google.Cloud.ServiceDirectory.V1Beta1\xca\x02%Google\\Cloud\\ServiceDirectory\\V1beta1\xea\x02(Google::Cloud::ServiceDirectory::V1beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_NAMESPACE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.cloud.servicedirectory.v1beta1.Namespace.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.servicedirectory.v1beta1.Namespace.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.servicedirectory.v1beta1.Namespace.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=485,
  serialized_end=542,
)

_NAMESPACE = _descriptor.Descriptor(
  name='Namespace',
  full_name='google.cloud.servicedirectory.v1beta1.Namespace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.servicedirectory.v1beta1.Namespace.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.cloud.servicedirectory.v1beta1.Namespace.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.servicedirectory.v1beta1.Namespace.create_time', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='createTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.cloud.servicedirectory.v1beta1.Namespace.update_time', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='updateTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NAMESPACE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=b'\352Ak\n)servicedirectory.googleapis.com/Namespace\022>projects/{project}/locations/{location}/namespaces/{namespace}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=654,
)

_NAMESPACE_LABELSENTRY.containing_type = _NAMESPACE
_NAMESPACE.fields_by_name['labels'].message_type = _NAMESPACE_LABELSENTRY
_NAMESPACE.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_NAMESPACE.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Namespace'] = _NAMESPACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Namespace = _reflection.GeneratedProtocolMessageType('Namespace', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _NAMESPACE_LABELSENTRY,
    '__module__' : 'google.cloud.servicedirectory.v1beta1.namespace_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.servicedirectory.v1beta1.Namespace.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _NAMESPACE,
  '__module__' : 'google.cloud.servicedirectory.v1beta1.namespace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.servicedirectory.v1beta1.Namespace)
  })
_sym_db.RegisterMessage(Namespace)
_sym_db.RegisterMessage(Namespace.LabelsEntry)


DESCRIPTOR._options = None
_NAMESPACE_LABELSENTRY._options = None
_NAMESPACE.fields_by_name['name']._options = None
_NAMESPACE.fields_by_name['labels']._options = None
_NAMESPACE.fields_by_name['create_time']._options = None
_NAMESPACE.fields_by_name['update_time']._options = None
_NAMESPACE._options = None
# @@protoc_insertion_point(module_scope)
