# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner/v1/scan_run_error_trace.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.websecurityscanner.v1 import scan_config_error_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1_dot_scan__config__error__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/websecurityscanner/v1/scan_run_error_trace.proto',
  package='google.cloud.websecurityscanner.v1',
  syntax='proto3',
  serialized_options=b'\n&com.google.cloud.websecurityscanner.v1B\026ScanRunErrorTraceProtoP\001ZTgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1;websecurityscanner\252\002\"Google.Cloud.WebSecurityScanner.V1\312\002\"Google\\Cloud\\WebSecurityScanner\\V1\352\002%Google::Cloud::WebSecurityScanner::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=google/cloud/websecurityscanner/v1/scan_run_error_trace.proto\x12\"google.cloud.websecurityscanner.v1\x1a:google/cloud/websecurityscanner/v1/scan_config_error.proto\"\xbd\x03\n\x11ScanRunErrorTrace\x12N\n\x04\x63ode\x18\x01 \x01(\x0e\x32:.google.cloud.websecurityscanner.v1.ScanRunErrorTrace.CodeR\x04\x63ode\x12_\n\x11scan_config_error\x18\x02 \x01(\x0b\x32\x33.google.cloud.websecurityscanner.v1.ScanConfigErrorR\x0fscanConfigError\x12<\n\x1bmost_common_http_error_code\x18\x03 \x01(\x05R\x17mostCommonHttpErrorCode\"\xb8\x01\n\x04\x43ode\x12\x14\n\x10\x43ODE_UNSPECIFIED\x10\x00\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x15\n\x11SCAN_CONFIG_ISSUE\x10\x02\x12\x1f\n\x1b\x41UTHENTICATION_CONFIG_ISSUE\x10\x03\x12\x1c\n\x18TIMED_OUT_WHILE_SCANNING\x10\x04\x12\x16\n\x12TOO_MANY_REDIRECTS\x10\x05\x12\x18\n\x14TOO_MANY_HTTP_ERRORS\x10\x06\x42\x8a\x02\n&com.google.cloud.websecurityscanner.v1B\x16ScanRunErrorTraceProtoP\x01ZTgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1;websecurityscanner\xaa\x02\"Google.Cloud.WebSecurityScanner.V1\xca\x02\"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1b\x06proto3'
  ,
  dependencies=[google_dot_cloud_dot_websecurityscanner_dot_v1_dot_scan__config__error__pb2.DESCRIPTOR,])



_SCANRUNERRORTRACE_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='google.cloud.websecurityscanner.v1.ScanRunErrorTrace.Code',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCAN_CONFIG_ISSUE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTHENTICATION_CONFIG_ISSUE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIMED_OUT_WHILE_SCANNING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_REDIRECTS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_HTTP_ERRORS', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=423,
  serialized_end=607,
)
_sym_db.RegisterEnumDescriptor(_SCANRUNERRORTRACE_CODE)


_SCANRUNERRORTRACE = _descriptor.Descriptor(
  name='ScanRunErrorTrace',
  full_name='google.cloud.websecurityscanner.v1.ScanRunErrorTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='google.cloud.websecurityscanner.v1.ScanRunErrorTrace.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='code', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scan_config_error', full_name='google.cloud.websecurityscanner.v1.ScanRunErrorTrace.scan_config_error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='scanConfigError', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='most_common_http_error_code', full_name='google.cloud.websecurityscanner.v1.ScanRunErrorTrace.most_common_http_error_code', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='mostCommonHttpErrorCode', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCANRUNERRORTRACE_CODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=607,
)

_SCANRUNERRORTRACE.fields_by_name['code'].enum_type = _SCANRUNERRORTRACE_CODE
_SCANRUNERRORTRACE.fields_by_name['scan_config_error'].message_type = google_dot_cloud_dot_websecurityscanner_dot_v1_dot_scan__config__error__pb2._SCANCONFIGERROR
_SCANRUNERRORTRACE_CODE.containing_type = _SCANRUNERRORTRACE
DESCRIPTOR.message_types_by_name['ScanRunErrorTrace'] = _SCANRUNERRORTRACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScanRunErrorTrace = _reflection.GeneratedProtocolMessageType('ScanRunErrorTrace', (_message.Message,), {
  'DESCRIPTOR' : _SCANRUNERRORTRACE,
  '__module__' : 'google.cloud.websecurityscanner.v1.scan_run_error_trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1.ScanRunErrorTrace)
  })
_sym_db.RegisterMessage(ScanRunErrorTrace)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
