# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner/v1beta/scan_run.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.websecurityscanner.v1beta import scan_run_error_trace_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__error__trace__pb2
from google.cloud.websecurityscanner.v1beta import scan_run_warning_trace_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__warning__trace__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/websecurityscanner/v1beta/scan_run.proto',
  package='google.cloud.websecurityscanner.v1beta',
  syntax='proto3',
  serialized_options=b'\n*com.google.cloud.websecurityscanner.v1betaB\014ScanRunProtoP\001ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\252\002&Google.Cloud.WebSecurityScanner.V1Beta\312\002&Google\\Cloud\\WebSecurityScanner\\V1beta\352\002)Google::Cloud::WebSecurityScanner::V1beta',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5google/cloud/websecurityscanner/v1beta/scan_run.proto\x12&google.cloud.websecurityscanner.v1beta\x1a\x19google/api/resource.proto\x1a\x41google/cloud/websecurityscanner/v1beta/scan_run_error_trace.proto\x1a\x43google/cloud/websecurityscanner/v1beta/scan_run_warning_trace.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xec\x07\n\x07ScanRun\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12g\n\x0f\x65xecution_state\x18\x02 \x01(\x0e\x32>.google.cloud.websecurityscanner.v1beta.ScanRun.ExecutionStateR\x0e\x65xecutionState\x12^\n\x0cresult_state\x18\x03 \x01(\x0e\x32;.google.cloud.websecurityscanner.v1beta.ScanRun.ResultStateR\x0bresultState\x12\x39\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12,\n\x12urls_crawled_count\x18\x06 \x01(\x03R\x10urlsCrawledCount\x12*\n\x11urls_tested_count\x18\x07 \x01(\x03R\x0furlsTestedCount\x12/\n\x13has_vulnerabilities\x18\x08 \x01(\x08R\x12hasVulnerabilities\x12)\n\x10progress_percent\x18\t \x01(\x05R\x0fprogressPercent\x12Z\n\x0b\x65rror_trace\x18\n \x01(\x0b\x32\x39.google.cloud.websecurityscanner.v1beta.ScanRunErrorTraceR\nerrorTrace\x12\x62\n\x0ewarning_traces\x18\x0b \x03(\x0b\x32;.google.cloud.websecurityscanner.v1beta.ScanRunWarningTraceR\rwarningTraces\"Y\n\x0e\x45xecutionState\x12\x1f\n\x1b\x45XECUTION_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\x0c\n\x08SCANNING\x10\x02\x12\x0c\n\x08\x46INISHED\x10\x03\"O\n\x0bResultState\x12\x1c\n\x18RESULT_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\n\n\x06KILLED\x10\x03:p\xea\x41m\n)websecurityscanner.googleapis.com/ScanRun\x12@projects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}B\x94\x02\n*com.google.cloud.websecurityscanner.v1betaB\x0cScanRunProtoP\x01ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1betab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__error__trace__pb2.DESCRIPTOR,google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__warning__trace__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_SCANRUN_EXECUTIONSTATE = _descriptor.EnumDescriptor(
  name='ExecutionState',
  full_name='google.cloud.websecurityscanner.v1beta.ScanRun.ExecutionState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXECUTION_STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUEUED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCANNING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINISHED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1014,
  serialized_end=1103,
)
_sym_db.RegisterEnumDescriptor(_SCANRUN_EXECUTIONSTATE)

_SCANRUN_RESULTSTATE = _descriptor.EnumDescriptor(
  name='ResultState',
  full_name='google.cloud.websecurityscanner.v1beta.ScanRun.ResultState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KILLED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1105,
  serialized_end=1184,
)
_sym_db.RegisterEnumDescriptor(_SCANRUN_RESULTSTATE)


_SCANRUN = _descriptor.Descriptor(
  name='ScanRun',
  full_name='google.cloud.websecurityscanner.v1beta.ScanRun',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.websecurityscanner.v1beta.ScanRun.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='execution_state', full_name='google.cloud.websecurityscanner.v1beta.ScanRun.execution_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='executionState', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_state', full_name='google.cloud.websecurityscanner.v1beta.ScanRun.result_state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resultState', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.cloud.websecurityscanner.v1beta.ScanRun.start_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='startTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.cloud.websecurityscanner.v1beta.ScanRun.end_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='endTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='urls_crawled_count', full_name='google.cloud.websecurityscanner.v1beta.ScanRun.urls_crawled_count', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='urlsCrawledCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='urls_tested_count', full_name='google.cloud.websecurityscanner.v1beta.ScanRun.urls_tested_count', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='urlsTestedCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_vulnerabilities', full_name='google.cloud.websecurityscanner.v1beta.ScanRun.has_vulnerabilities', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hasVulnerabilities', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress_percent', full_name='google.cloud.websecurityscanner.v1beta.ScanRun.progress_percent', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='progressPercent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_trace', full_name='google.cloud.websecurityscanner.v1beta.ScanRun.error_trace', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='errorTrace', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warning_traces', full_name='google.cloud.websecurityscanner.v1beta.ScanRun.warning_traces', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='warningTraces', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCANRUN_EXECUTIONSTATE,
    _SCANRUN_RESULTSTATE,
  ],
  serialized_options=b'\352Am\n)websecurityscanner.googleapis.com/ScanRun\022@projects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=1298,
)

_SCANRUN.fields_by_name['execution_state'].enum_type = _SCANRUN_EXECUTIONSTATE
_SCANRUN.fields_by_name['result_state'].enum_type = _SCANRUN_RESULTSTATE
_SCANRUN.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SCANRUN.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SCANRUN.fields_by_name['error_trace'].message_type = google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__error__trace__pb2._SCANRUNERRORTRACE
_SCANRUN.fields_by_name['warning_traces'].message_type = google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__warning__trace__pb2._SCANRUNWARNINGTRACE
_SCANRUN_EXECUTIONSTATE.containing_type = _SCANRUN
_SCANRUN_RESULTSTATE.containing_type = _SCANRUN
DESCRIPTOR.message_types_by_name['ScanRun'] = _SCANRUN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScanRun = _reflection.GeneratedProtocolMessageType('ScanRun', (_message.Message,), {
  'DESCRIPTOR' : _SCANRUN,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.scan_run_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ScanRun)
  })
_sym_db.RegisterMessage(ScanRun)


DESCRIPTOR._options = None
_SCANRUN._options = None
# @@protoc_insertion_point(module_scope)
