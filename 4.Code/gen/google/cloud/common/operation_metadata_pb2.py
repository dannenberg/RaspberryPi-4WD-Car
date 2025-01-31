# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/common/operation_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/common/operation_metadata.proto',
  package='google.cloud.common',
  syntax='proto3',
  serialized_options=b'\n\027com.google.cloud.commonP\001Z9google.golang.org/genproto/googleapis/cloud/common;common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,google/cloud/common/operation_metadata.proto\x12\x13google.cloud.common\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xce\x02\n\x11OperationMetadata\x12\x41\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12;\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x07\x65ndTime\x12\x1c\n\x06target\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03R\x06target\x12\x18\n\x04verb\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03R\x04verb\x12)\n\rstatus_detail\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03R\x0cstatusDetail\x12/\n\x10\x63\x61ncel_requested\x18\x06 \x01(\x08\x42\x04\xe2\x41\x01\x03R\x0f\x63\x61ncelRequested\x12%\n\x0b\x61pi_version\x18\x07 \x01(\tB\x04\xe2\x41\x01\x03R\napiVersionBV\n\x17\x63om.google.cloud.commonP\x01Z9google.golang.org/genproto/googleapis/cloud/common;commonb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_OPERATIONMETADATA = _descriptor.Descriptor(
  name='OperationMetadata',
  full_name='google.cloud.common.OperationMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.common.OperationMetadata.create_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='createTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.cloud.common.OperationMetadata.end_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='endTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='google.cloud.common.OperationMetadata.target', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='target', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='verb', full_name='google.cloud.common.OperationMetadata.verb', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='verb', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_detail', full_name='google.cloud.common.OperationMetadata.status_detail', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='statusDetail', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cancel_requested', full_name='google.cloud.common.OperationMetadata.cancel_requested', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='cancelRequested', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='api_version', full_name='google.cloud.common.OperationMetadata.api_version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='apiVersion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=136,
  serialized_end=470,
)

_OPERATIONMETADATA.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPERATIONMETADATA.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['OperationMetadata'] = _OPERATIONMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperationMetadata = _reflection.GeneratedProtocolMessageType('OperationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONMETADATA,
  '__module__' : 'google.cloud.common.operation_metadata_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.common.OperationMetadata)
  })
_sym_db.RegisterMessage(OperationMetadata)


DESCRIPTOR._options = None
_OPERATIONMETADATA.fields_by_name['create_time']._options = None
_OPERATIONMETADATA.fields_by_name['end_time']._options = None
_OPERATIONMETADATA.fields_by_name['target']._options = None
_OPERATIONMETADATA.fields_by_name['verb']._options = None
_OPERATIONMETADATA.fields_by_name['status_detail']._options = None
_OPERATIONMETADATA.fields_by_name['cancel_requested']._options = None
_OPERATIONMETADATA.fields_by_name['api_version']._options = None
# @@protoc_insertion_point(module_scope)
