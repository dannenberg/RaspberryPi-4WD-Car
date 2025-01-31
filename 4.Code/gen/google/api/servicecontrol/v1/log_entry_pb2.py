# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/servicecontrol/v1/log_entry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api.servicecontrol.v1 import http_request_pb2 as google_dot_api_dot_servicecontrol_dot_v1_dot_http__request__pb2
from google.logging.type import log_severity_pb2 as google_dot_logging_dot_type_dot_log__severity__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/servicecontrol/v1/log_entry.proto',
  package='google.api.servicecontrol.v1',
  syntax='proto3',
  serialized_options=b'\n com.google.api.servicecontrol.v1B\rLogEntryProtoP\001ZJgoogle.golang.org/genproto/googleapis/api/servicecontrol/v1;servicecontrol\252\002\036Google.Cloud.ServiceControl.V1\312\002\036Google\\Cloud\\ServiceControl\\V1\352\002!Google::Cloud::ServiceControl::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,google/api/servicecontrol/v1/log_entry.proto\x12\x1cgoogle.api.servicecontrol.v1\x1a/google/api/servicecontrol/v1/http_request.proto\x1a&google/logging/type/log_severity.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfb\x05\n\x08LogEntry\x12\x12\n\x04name\x18\n \x01(\tR\x04name\x12\x38\n\ttimestamp\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12<\n\x08severity\x18\x0c \x01(\x0e\x32 .google.logging.type.LogSeverityR\x08severity\x12L\n\x0chttp_request\x18\x0e \x01(\x0b\x32).google.api.servicecontrol.v1.HttpRequestR\x0bhttpRequest\x12\x14\n\x05trace\x18\x0f \x01(\tR\x05trace\x12\x1b\n\tinsert_id\x18\x04 \x01(\tR\x08insertId\x12J\n\x06labels\x18\r \x03(\x0b\x32\x32.google.api.servicecontrol.v1.LogEntry.LabelsEntryR\x06labels\x12;\n\rproto_payload\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\x0cprotoPayload\x12#\n\x0ctext_payload\x18\x03 \x01(\tH\x00R\x0btextPayload\x12@\n\x0estruct_payload\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructH\x00R\rstructPayload\x12M\n\toperation\x18\x10 \x01(\x0b\x32/.google.api.servicecontrol.v1.LogEntryOperationR\toperation\x12]\n\x0fsource_location\x18\x11 \x01(\x0b\x32\x34.google.api.servicecontrol.v1.LogEntrySourceLocationR\x0esourceLocation\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\t\n\x07payload\"i\n\x11LogEntryOperation\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1a\n\x08producer\x18\x02 \x01(\tR\x08producer\x12\x14\n\x05\x66irst\x18\x03 \x01(\x08R\x05\x66irst\x12\x12\n\x04last\x18\x04 \x01(\x08R\x04last\"\\\n\x16LogEntrySourceLocation\x12\x12\n\x04\x66ile\x18\x01 \x01(\tR\x04\x66ile\x12\x12\n\x04line\x18\x02 \x01(\x03R\x04line\x12\x1a\n\x08\x66unction\x18\x03 \x01(\tR\x08\x66unctionB\xe5\x01\n com.google.api.servicecontrol.v1B\rLogEntryProtoP\x01ZJgoogle.golang.org/genproto/googleapis/api/servicecontrol/v1;servicecontrol\xaa\x02\x1eGoogle.Cloud.ServiceControl.V1\xca\x02\x1eGoogle\\Cloud\\ServiceControl\\V1\xea\x02!Google::Cloud::ServiceControl::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_servicecontrol_dot_v1_dot_http__request__pb2.DESCRIPTOR,google_dot_logging_dot_type_dot_log__severity__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_LOGENTRY_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.api.servicecontrol.v1.LogEntry.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.api.servicecontrol.v1.LogEntry.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.api.servicecontrol.v1.LogEntry.LabelsEntry.value', index=1,
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
  serialized_start=953,
  serialized_end=1010,
)

_LOGENTRY = _descriptor.Descriptor(
  name='LogEntry',
  full_name='google.api.servicecontrol.v1.LogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.api.servicecontrol.v1.LogEntry.name', index=0,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='google.api.servicecontrol.v1.LogEntry.timestamp', index=1,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='severity', full_name='google.api.servicecontrol.v1.LogEntry.severity', index=2,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='severity', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='http_request', full_name='google.api.servicecontrol.v1.LogEntry.http_request', index=3,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='httpRequest', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace', full_name='google.api.servicecontrol.v1.LogEntry.trace', index=4,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='trace', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='insert_id', full_name='google.api.servicecontrol.v1.LogEntry.insert_id', index=5,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='insertId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.api.servicecontrol.v1.LogEntry.labels', index=6,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proto_payload', full_name='google.api.servicecontrol.v1.LogEntry.proto_payload', index=7,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='protoPayload', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text_payload', full_name='google.api.servicecontrol.v1.LogEntry.text_payload', index=8,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='textPayload', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='struct_payload', full_name='google.api.servicecontrol.v1.LogEntry.struct_payload', index=9,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='structPayload', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation', full_name='google.api.servicecontrol.v1.LogEntry.operation', index=10,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='operation', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_location', full_name='google.api.servicecontrol.v1.LogEntry.source_location', index=11,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sourceLocation', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LOGENTRY_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='google.api.servicecontrol.v1.LogEntry.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=258,
  serialized_end=1021,
)


_LOGENTRYOPERATION = _descriptor.Descriptor(
  name='LogEntryOperation',
  full_name='google.api.servicecontrol.v1.LogEntryOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.api.servicecontrol.v1.LogEntryOperation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='producer', full_name='google.api.servicecontrol.v1.LogEntryOperation.producer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='producer', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first', full_name='google.api.servicecontrol.v1.LogEntryOperation.first', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='first', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last', full_name='google.api.servicecontrol.v1.LogEntryOperation.last', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='last', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1023,
  serialized_end=1128,
)


_LOGENTRYSOURCELOCATION = _descriptor.Descriptor(
  name='LogEntrySourceLocation',
  full_name='google.api.servicecontrol.v1.LogEntrySourceLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='google.api.servicecontrol.v1.LogEntrySourceLocation.file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='file', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line', full_name='google.api.servicecontrol.v1.LogEntrySourceLocation.line', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='line', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='function', full_name='google.api.servicecontrol.v1.LogEntrySourceLocation.function', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='function', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1130,
  serialized_end=1222,
)

_LOGENTRY_LABELSENTRY.containing_type = _LOGENTRY
_LOGENTRY.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGENTRY.fields_by_name['severity'].enum_type = google_dot_logging_dot_type_dot_log__severity__pb2._LOGSEVERITY
_LOGENTRY.fields_by_name['http_request'].message_type = google_dot_api_dot_servicecontrol_dot_v1_dot_http__request__pb2._HTTPREQUEST
_LOGENTRY.fields_by_name['labels'].message_type = _LOGENTRY_LABELSENTRY
_LOGENTRY.fields_by_name['proto_payload'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_LOGENTRY.fields_by_name['struct_payload'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LOGENTRY.fields_by_name['operation'].message_type = _LOGENTRYOPERATION
_LOGENTRY.fields_by_name['source_location'].message_type = _LOGENTRYSOURCELOCATION
_LOGENTRY.oneofs_by_name['payload'].fields.append(
  _LOGENTRY.fields_by_name['proto_payload'])
_LOGENTRY.fields_by_name['proto_payload'].containing_oneof = _LOGENTRY.oneofs_by_name['payload']
_LOGENTRY.oneofs_by_name['payload'].fields.append(
  _LOGENTRY.fields_by_name['text_payload'])
_LOGENTRY.fields_by_name['text_payload'].containing_oneof = _LOGENTRY.oneofs_by_name['payload']
_LOGENTRY.oneofs_by_name['payload'].fields.append(
  _LOGENTRY.fields_by_name['struct_payload'])
_LOGENTRY.fields_by_name['struct_payload'].containing_oneof = _LOGENTRY.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['LogEntry'] = _LOGENTRY
DESCRIPTOR.message_types_by_name['LogEntryOperation'] = _LOGENTRYOPERATION
DESCRIPTOR.message_types_by_name['LogEntrySourceLocation'] = _LOGENTRYSOURCELOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogEntry = _reflection.GeneratedProtocolMessageType('LogEntry', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOGENTRY_LABELSENTRY,
    '__module__' : 'google.api.servicecontrol.v1.log_entry_pb2'
    # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.LogEntry.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LOGENTRY,
  '__module__' : 'google.api.servicecontrol.v1.log_entry_pb2'
  # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.LogEntry)
  })
_sym_db.RegisterMessage(LogEntry)
_sym_db.RegisterMessage(LogEntry.LabelsEntry)

LogEntryOperation = _reflection.GeneratedProtocolMessageType('LogEntryOperation', (_message.Message,), {
  'DESCRIPTOR' : _LOGENTRYOPERATION,
  '__module__' : 'google.api.servicecontrol.v1.log_entry_pb2'
  # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.LogEntryOperation)
  })
_sym_db.RegisterMessage(LogEntryOperation)

LogEntrySourceLocation = _reflection.GeneratedProtocolMessageType('LogEntrySourceLocation', (_message.Message,), {
  'DESCRIPTOR' : _LOGENTRYSOURCELOCATION,
  '__module__' : 'google.api.servicecontrol.v1.log_entry_pb2'
  # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.LogEntrySourceLocation)
  })
_sym_db.RegisterMessage(LogEntrySourceLocation)


DESCRIPTOR._options = None
_LOGENTRY_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
