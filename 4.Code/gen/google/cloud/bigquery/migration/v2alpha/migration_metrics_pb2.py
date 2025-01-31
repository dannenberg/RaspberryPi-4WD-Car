# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/migration/v2alpha/migration_metrics.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import distribution_pb2 as google_dot_api_dot_distribution__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import metric_pb2 as google_dot_api_dot_metric__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/bigquery/migration/v2alpha/migration_metrics.proto',
  package='google.cloud.bigquery.migration.v2alpha',
  syntax='proto3',
  serialized_options=b'\n+com.google.cloud.bigquery.migration.v2alphaB\025MigrationMetricsProtoP\001ZPgoogle.golang.org/genproto/googleapis/cloud/bigquery/migration/v2alpha;migration\252\002\'Google.Cloud.BigQuery.Migration.V2Alpha\312\002\'Google\\Cloud\\BigQuery\\Migration\\V2alpha',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?google/cloud/bigquery/migration/v2alpha/migration_metrics.proto\x12\'google.cloud.bigquery.migration.v2alpha\x1a\x1dgoogle/api/distribution.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/api/metric.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x95\x02\n\nTimeSeries\x12\x1c\n\x06metric\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06metric\x12K\n\nvalue_type\x18\x02 \x01(\x0e\x32&.google.api.MetricDescriptor.ValueTypeB\x04\xe2\x41\x01\x02R\tvalueType\x12N\n\x0bmetric_kind\x18\x03 \x01(\x0e\x32\'.google.api.MetricDescriptor.MetricKindB\x04\xe2\x41\x01\x01R\nmetricKind\x12L\n\x06points\x18\x04 \x03(\x0b\x32..google.cloud.bigquery.migration.v2alpha.PointB\x04\xe2\x41\x01\x02R\x06points\"\xa5\x01\n\x05Point\x12Q\n\x08interval\x18\x01 \x01(\x0b\x32\x35.google.cloud.bigquery.migration.v2alpha.TimeIntervalR\x08interval\x12I\n\x05value\x18\x02 \x01(\x0b\x32\x33.google.cloud.bigquery.migration.v2alpha.TypedValueR\x05value\"\x8c\x01\n\x0cTimeInterval\x12?\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x01R\tstartTime\x12;\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02R\x07\x65ndTime\"\xee\x01\n\nTypedValue\x12\x1f\n\nbool_value\x18\x01 \x01(\x08H\x00R\tboolValue\x12!\n\x0bint64_value\x18\x02 \x01(\x03H\x00R\nint64Value\x12#\n\x0c\x64ouble_value\x18\x03 \x01(\x01H\x00R\x0b\x64oubleValue\x12#\n\x0cstring_value\x18\x04 \x01(\tH\x00R\x0bstringValue\x12I\n\x12\x64istribution_value\x18\x05 \x01(\x0b\x32\x18.google.api.DistributionH\x00R\x11\x64istributionValueB\x07\n\x05valueB\xec\x01\n+com.google.cloud.bigquery.migration.v2alphaB\x15MigrationMetricsProtoP\x01ZPgoogle.golang.org/genproto/googleapis/cloud/bigquery/migration/v2alpha;migration\xaa\x02\'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02\'Google\\Cloud\\BigQuery\\Migration\\V2alphab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_distribution__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_metric__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_TIMESERIES = _descriptor.Descriptor(
  name='TimeSeries',
  full_name='google.cloud.bigquery.migration.v2alpha.TimeSeries',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric', full_name='google.cloud.bigquery.migration.v2alpha.TimeSeries.metric', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='metric', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value_type', full_name='google.cloud.bigquery.migration.v2alpha.TimeSeries.value_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='valueType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric_kind', full_name='google.cloud.bigquery.migration.v2alpha.TimeSeries.metric_kind', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='metricKind', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='points', full_name='google.cloud.bigquery.migration.v2alpha.TimeSeries.points', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='points', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=231,
  serialized_end=508,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='google.cloud.bigquery.migration.v2alpha.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='interval', full_name='google.cloud.bigquery.migration.v2alpha.Point.interval', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='interval', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.bigquery.migration.v2alpha.Point.value', index=1,
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
  serialized_start=511,
  serialized_end=676,
)


_TIMEINTERVAL = _descriptor.Descriptor(
  name='TimeInterval',
  full_name='google.cloud.bigquery.migration.v2alpha.TimeInterval',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.cloud.bigquery.migration.v2alpha.TimeInterval.start_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='startTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.cloud.bigquery.migration.v2alpha.TimeInterval.end_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='endTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=679,
  serialized_end=819,
)


_TYPEDVALUE = _descriptor.Descriptor(
  name='TypedValue',
  full_name='google.cloud.bigquery.migration.v2alpha.TypedValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='google.cloud.bigquery.migration.v2alpha.TypedValue.bool_value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='boolValue', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='google.cloud.bigquery.migration.v2alpha.TypedValue.int64_value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='int64Value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='google.cloud.bigquery.migration.v2alpha.TypedValue.double_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='doubleValue', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='google.cloud.bigquery.migration.v2alpha.TypedValue.string_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stringValue', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distribution_value', full_name='google.cloud.bigquery.migration.v2alpha.TypedValue.distribution_value', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='distributionValue', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='value', full_name='google.cloud.bigquery.migration.v2alpha.TypedValue.value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=822,
  serialized_end=1060,
)

_TIMESERIES.fields_by_name['value_type'].enum_type = google_dot_api_dot_metric__pb2._METRICDESCRIPTOR_VALUETYPE
_TIMESERIES.fields_by_name['metric_kind'].enum_type = google_dot_api_dot_metric__pb2._METRICDESCRIPTOR_METRICKIND
_TIMESERIES.fields_by_name['points'].message_type = _POINT
_POINT.fields_by_name['interval'].message_type = _TIMEINTERVAL
_POINT.fields_by_name['value'].message_type = _TYPEDVALUE
_TIMEINTERVAL.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMEINTERVAL.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TYPEDVALUE.fields_by_name['distribution_value'].message_type = google_dot_api_dot_distribution__pb2._DISTRIBUTION
_TYPEDVALUE.oneofs_by_name['value'].fields.append(
  _TYPEDVALUE.fields_by_name['bool_value'])
_TYPEDVALUE.fields_by_name['bool_value'].containing_oneof = _TYPEDVALUE.oneofs_by_name['value']
_TYPEDVALUE.oneofs_by_name['value'].fields.append(
  _TYPEDVALUE.fields_by_name['int64_value'])
_TYPEDVALUE.fields_by_name['int64_value'].containing_oneof = _TYPEDVALUE.oneofs_by_name['value']
_TYPEDVALUE.oneofs_by_name['value'].fields.append(
  _TYPEDVALUE.fields_by_name['double_value'])
_TYPEDVALUE.fields_by_name['double_value'].containing_oneof = _TYPEDVALUE.oneofs_by_name['value']
_TYPEDVALUE.oneofs_by_name['value'].fields.append(
  _TYPEDVALUE.fields_by_name['string_value'])
_TYPEDVALUE.fields_by_name['string_value'].containing_oneof = _TYPEDVALUE.oneofs_by_name['value']
_TYPEDVALUE.oneofs_by_name['value'].fields.append(
  _TYPEDVALUE.fields_by_name['distribution_value'])
_TYPEDVALUE.fields_by_name['distribution_value'].containing_oneof = _TYPEDVALUE.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['TimeSeries'] = _TIMESERIES
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['TimeInterval'] = _TIMEINTERVAL
DESCRIPTOR.message_types_by_name['TypedValue'] = _TYPEDVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeSeries = _reflection.GeneratedProtocolMessageType('TimeSeries', (_message.Message,), {
  'DESCRIPTOR' : _TIMESERIES,
  '__module__' : 'google.cloud.bigquery.migration.v2alpha.migration_metrics_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.migration.v2alpha.TimeSeries)
  })
_sym_db.RegisterMessage(TimeSeries)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'google.cloud.bigquery.migration.v2alpha.migration_metrics_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.migration.v2alpha.Point)
  })
_sym_db.RegisterMessage(Point)

TimeInterval = _reflection.GeneratedProtocolMessageType('TimeInterval', (_message.Message,), {
  'DESCRIPTOR' : _TIMEINTERVAL,
  '__module__' : 'google.cloud.bigquery.migration.v2alpha.migration_metrics_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.migration.v2alpha.TimeInterval)
  })
_sym_db.RegisterMessage(TimeInterval)

TypedValue = _reflection.GeneratedProtocolMessageType('TypedValue', (_message.Message,), {
  'DESCRIPTOR' : _TYPEDVALUE,
  '__module__' : 'google.cloud.bigquery.migration.v2alpha.migration_metrics_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.migration.v2alpha.TypedValue)
  })
_sym_db.RegisterMessage(TypedValue)


DESCRIPTOR._options = None
_TIMESERIES.fields_by_name['metric']._options = None
_TIMESERIES.fields_by_name['value_type']._options = None
_TIMESERIES.fields_by_name['metric_kind']._options = None
_TIMESERIES.fields_by_name['points']._options = None
_TIMEINTERVAL.fields_by_name['start_time']._options = None
_TIMEINTERVAL.fields_by_name['end_time']._options = None
# @@protoc_insertion_point(module_scope)
