# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/iam/v1/logging/audit_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/iam/v1/logging/audit_data.proto',
  package='google.iam.v1.logging',
  syntax='proto3',
  serialized_options=b'\n\031com.google.iam.v1.loggingB\016AuditDataProtoP\001Z<google.golang.org/genproto/googleapis/iam/v1/logging;logging\252\002\033Google.Cloud.Iam.V1.Logging',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&google/iam/v1/logging/audit_data.proto\x12\x15google.iam.v1.logging\x1a\x1cgoogle/api/annotations.proto\x1a\x1agoogle/iam/v1/policy.proto\"J\n\tAuditData\x12=\n\x0cpolicy_delta\x18\x02 \x01(\x0b\x32\x1a.google.iam.v1.PolicyDeltaR\x0bpolicyDeltaB\x89\x01\n\x19\x63om.google.iam.v1.loggingB\x0e\x41uditDataProtoP\x01Z<google.golang.org/genproto/googleapis/iam/v1/logging;logging\xaa\x02\x1bGoogle.Cloud.Iam.V1.Loggingb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_iam_dot_v1_dot_policy__pb2.DESCRIPTOR,])




_AUDITDATA = _descriptor.Descriptor(
  name='AuditData',
  full_name='google.iam.v1.logging.AuditData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy_delta', full_name='google.iam.v1.logging.AuditData.policy_delta', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='policyDelta', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=123,
  serialized_end=197,
)

_AUDITDATA.fields_by_name['policy_delta'].message_type = google_dot_iam_dot_v1_dot_policy__pb2._POLICYDELTA
DESCRIPTOR.message_types_by_name['AuditData'] = _AUDITDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuditData = _reflection.GeneratedProtocolMessageType('AuditData', (_message.Message,), {
  'DESCRIPTOR' : _AUDITDATA,
  '__module__' : 'google.iam.v1.logging.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.iam.v1.logging.AuditData)
  })
_sym_db.RegisterMessage(AuditData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
