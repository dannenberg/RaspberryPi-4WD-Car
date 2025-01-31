# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/integrations/v1alpha/event_parameter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.integrations.v1alpha import value_type_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_value__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/integrations/v1alpha/event_parameter.proto',
  package='google.cloud.integrations.v1alpha',
  syntax='proto3',
  serialized_options=b'\n%com.google.cloud.integrations.v1alphaB\023EventParameterProtoP\001ZMgoogle.golang.org/genproto/googleapis/cloud/integrations/v1alpha;integrations',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7google/cloud/integrations/v1alpha/event_parameter.proto\x12!google.cloud.integrations.v1alpha\x1a\x32google/cloud/integrations/v1alpha/value_type.proto\"f\n\x0e\x45ventParameter\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x42\n\x05value\x18\x02 \x01(\x0b\x32,.google.cloud.integrations.v1alpha.ValueTypeR\x05valueB\x8d\x01\n%com.google.cloud.integrations.v1alphaB\x13\x45ventParameterProtoP\x01ZMgoogle.golang.org/genproto/googleapis/cloud/integrations/v1alpha;integrationsb\x06proto3'
  ,
  dependencies=[google_dot_cloud_dot_integrations_dot_v1alpha_dot_value__type__pb2.DESCRIPTOR,])




_EVENTPARAMETER = _descriptor.Descriptor(
  name='EventParameter',
  full_name='google.cloud.integrations.v1alpha.EventParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.integrations.v1alpha.EventParameter.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.integrations.v1alpha.EventParameter.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=146,
  serialized_end=248,
)

_EVENTPARAMETER.fields_by_name['value'].message_type = google_dot_cloud_dot_integrations_dot_v1alpha_dot_value__type__pb2._VALUETYPE
DESCRIPTOR.message_types_by_name['EventParameter'] = _EVENTPARAMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventParameter = _reflection.GeneratedProtocolMessageType('EventParameter', (_message.Message,), {
  'DESCRIPTOR' : _EVENTPARAMETER,
  '__module__' : 'google.cloud.integrations.v1alpha.event_parameter_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.EventParameter)
  })
_sym_db.RegisterMessage(EventParameter)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
