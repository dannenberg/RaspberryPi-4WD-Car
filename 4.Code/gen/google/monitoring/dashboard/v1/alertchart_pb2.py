# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/monitoring/dashboard/v1/alertchart.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/monitoring/dashboard/v1/alertchart.proto',
  package='google.monitoring.dashboard.v1',
  syntax='proto3',
  serialized_options=b'\n\"com.google.monitoring.dashboard.v1B\017AlertChartProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\252\002$Google.Cloud.Monitoring.Dashboard.V1\312\002$Google\\Cloud\\Monitoring\\Dashboard\\V1\352\002(Google::Cloud::Monitoring::Dashboard::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/google/monitoring/dashboard/v1/alertchart.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"\x83\x01\n\nAlertChart\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name:[\xea\x41X\n%monitoring.googleapis.com/AlertPolicy\x12/projects/{project}/alertPolicies/{alert_policy}B\xf9\x01\n\"com.google.monitoring.dashboard.v1B\x0f\x41lertChartProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_ALERTCHART = _descriptor.Descriptor(
  name='AlertChart',
  full_name='google.monitoring.dashboard.v1.AlertChart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.monitoring.dashboard.v1.AlertChart.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352AX\n%monitoring.googleapis.com/AlertPolicy\022/projects/{project}/alertPolicies/{alert_policy}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=275,
)

DESCRIPTOR.message_types_by_name['AlertChart'] = _ALERTCHART
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlertChart = _reflection.GeneratedProtocolMessageType('AlertChart', (_message.Message,), {
  'DESCRIPTOR' : _ALERTCHART,
  '__module__' : 'google.monitoring.dashboard.v1.alertchart_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.AlertChart)
  })
_sym_db.RegisterMessage(AlertChart)


DESCRIPTOR._options = None
_ALERTCHART.fields_by_name['name']._options = None
_ALERTCHART._options = None
# @@protoc_insertion_point(module_scope)
