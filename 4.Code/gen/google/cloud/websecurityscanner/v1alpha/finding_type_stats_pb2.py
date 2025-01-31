# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner/v1alpha/finding_type_stats.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.websecurityscanner.v1alpha import finding_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1alpha_dot_finding__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/websecurityscanner/v1alpha/finding_type_stats.proto',
  package='google.cloud.websecurityscanner.v1alpha',
  syntax='proto3',
  serialized_options=b'\n+com.google.cloud.websecurityscanner.v1alphaB\025FindingTypeStatsProtoP\001ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscanner',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n@google/cloud/websecurityscanner/v1alpha/finding_type_stats.proto\x12\'google.cloud.websecurityscanner.v1alpha\x1a\x35google/cloud/websecurityscanner/v1alpha/finding.proto\"\x98\x01\n\x10\x46indingTypeStats\x12_\n\x0c\x66inding_type\x18\x01 \x01(\x0e\x32<.google.cloud.websecurityscanner.v1alpha.Finding.FindingTypeR\x0b\x66indingType\x12#\n\rfinding_count\x18\x02 \x01(\x05R\x0c\x66indingCountB\xa1\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x15\x46indingTypeStatsProtoP\x01ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscannerb\x06proto3'
  ,
  dependencies=[google_dot_cloud_dot_websecurityscanner_dot_v1alpha_dot_finding__pb2.DESCRIPTOR,])




_FINDINGTYPESTATS = _descriptor.Descriptor(
  name='FindingTypeStats',
  full_name='google.cloud.websecurityscanner.v1alpha.FindingTypeStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='finding_type', full_name='google.cloud.websecurityscanner.v1alpha.FindingTypeStats.finding_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='findingType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finding_count', full_name='google.cloud.websecurityscanner.v1alpha.FindingTypeStats.finding_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='findingCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=165,
  serialized_end=317,
)

_FINDINGTYPESTATS.fields_by_name['finding_type'].enum_type = google_dot_cloud_dot_websecurityscanner_dot_v1alpha_dot_finding__pb2._FINDING_FINDINGTYPE
DESCRIPTOR.message_types_by_name['FindingTypeStats'] = _FINDINGTYPESTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FindingTypeStats = _reflection.GeneratedProtocolMessageType('FindingTypeStats', (_message.Message,), {
  'DESCRIPTOR' : _FINDINGTYPESTATS,
  '__module__' : 'google.cloud.websecurityscanner.v1alpha.finding_type_stats_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.FindingTypeStats)
  })
_sym_db.RegisterMessage(FindingTypeStats)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
