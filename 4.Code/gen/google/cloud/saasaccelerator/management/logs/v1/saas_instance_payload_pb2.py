# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/saasaccelerator/management/logs/v1/saas_instance_payload.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/saasaccelerator/management/logs/v1/saas_instance_payload.proto',
  package='google.cloud.saasaccelerator.management.logs.v1',
  syntax='proto3',
  serialized_options=b'\n3com.google.cloud.saasaccelerator.management.logs.v1B\030SaasInstancePayloadProtoP\001ZSgoogle.golang.org/genproto/googleapis/cloud/saasaccelerator/management/logs/v1;logs',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nKgoogle/cloud/saasaccelerator/management/logs/v1/saas_instance_payload.proto\x12/google.cloud.saasaccelerator.management.logs.v1\"\x7f\n\rInstanceEvent\x12\x12\n\x04verb\x18\x01 \x01(\tR\x04verb\x12\x14\n\x05stage\x18\x02 \x01(\tR\x05stage\x12\x10\n\x03msg\x18\x03 \x01(\tR\x03msg\x12\x19\n\x08trace_id\x18\x04 \x01(\tR\x07traceId\x12\x17\n\x07node_id\x18\x05 \x01(\tR\x06nodeIdB\xa6\x01\n3com.google.cloud.saasaccelerator.management.logs.v1B\x18SaasInstancePayloadProtoP\x01ZSgoogle.golang.org/genproto/googleapis/cloud/saasaccelerator/management/logs/v1;logsb\x06proto3'
)




_INSTANCEEVENT = _descriptor.Descriptor(
  name='InstanceEvent',
  full_name='google.cloud.saasaccelerator.management.logs.v1.InstanceEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='verb', full_name='google.cloud.saasaccelerator.management.logs.v1.InstanceEvent.verb', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='verb', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stage', full_name='google.cloud.saasaccelerator.management.logs.v1.InstanceEvent.stage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='google.cloud.saasaccelerator.management.logs.v1.InstanceEvent.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='msg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='google.cloud.saasaccelerator.management.logs.v1.InstanceEvent.trace_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='traceId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='google.cloud.saasaccelerator.management.logs.v1.InstanceEvent.node_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nodeId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=128,
  serialized_end=255,
)

DESCRIPTOR.message_types_by_name['InstanceEvent'] = _INSTANCEEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstanceEvent = _reflection.GeneratedProtocolMessageType('InstanceEvent', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCEEVENT,
  '__module__' : 'google.cloud.saasaccelerator.management.logs.v1.saas_instance_payload_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.saasaccelerator.management.logs.v1.InstanceEvent)
  })
_sym_db.RegisterMessage(InstanceEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
