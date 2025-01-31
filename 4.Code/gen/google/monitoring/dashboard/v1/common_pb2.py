# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/monitoring/dashboard/v1/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import distribution_pb2 as google_dot_api_dot_distribution__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/monitoring/dashboard/v1/common.proto',
  package='google.monitoring.dashboard.v1',
  syntax='proto3',
  serialized_options=b'\n\"com.google.monitoring.dashboard.v1B\013CommonProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\252\002$Google.Cloud.Monitoring.Dashboard.V1\312\002$Google\\Cloud\\Monitoring\\Dashboard\\V1\352\002(Google::Cloud::Monitoring::Dashboard::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+google/monitoring/dashboard/v1/common.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1dgoogle/api/distribution.proto\x1a\x1egoogle/protobuf/duration.proto\"\x87\x08\n\x0b\x41ggregation\x12\x44\n\x10\x61lignment_period\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0f\x61lignmentPeriod\x12\x61\n\x12per_series_aligner\x18\x02 \x01(\x0e\x32\x33.google.monitoring.dashboard.v1.Aggregation.AlignerR\x10perSeriesAligner\x12\x65\n\x14\x63ross_series_reducer\x18\x04 \x01(\x0e\x32\x33.google.monitoring.dashboard.v1.Aggregation.ReducerR\x12\x63rossSeriesReducer\x12&\n\x0fgroup_by_fields\x18\x05 \x03(\tR\rgroupByFields\"\x8b\x03\n\x07\x41ligner\x12\x0e\n\nALIGN_NONE\x10\x00\x12\x0f\n\x0b\x41LIGN_DELTA\x10\x01\x12\x0e\n\nALIGN_RATE\x10\x02\x12\x15\n\x11\x41LIGN_INTERPOLATE\x10\x03\x12\x14\n\x10\x41LIGN_NEXT_OLDER\x10\x04\x12\r\n\tALIGN_MIN\x10\n\x12\r\n\tALIGN_MAX\x10\x0b\x12\x0e\n\nALIGN_MEAN\x10\x0c\x12\x0f\n\x0b\x41LIGN_COUNT\x10\r\x12\r\n\tALIGN_SUM\x10\x0e\x12\x10\n\x0c\x41LIGN_STDDEV\x10\x0f\x12\x14\n\x10\x41LIGN_COUNT_TRUE\x10\x10\x12\x15\n\x11\x41LIGN_COUNT_FALSE\x10\x18\x12\x17\n\x13\x41LIGN_FRACTION_TRUE\x10\x11\x12\x17\n\x13\x41LIGN_PERCENTILE_99\x10\x12\x12\x17\n\x13\x41LIGN_PERCENTILE_95\x10\x13\x12\x17\n\x13\x41LIGN_PERCENTILE_50\x10\x14\x12\x17\n\x13\x41LIGN_PERCENTILE_05\x10\x15\x12\x18\n\x14\x41LIGN_PERCENT_CHANGE\x10\x17\"\xb1\x02\n\x07Reducer\x12\x0f\n\x0bREDUCE_NONE\x10\x00\x12\x0f\n\x0bREDUCE_MEAN\x10\x01\x12\x0e\n\nREDUCE_MIN\x10\x02\x12\x0e\n\nREDUCE_MAX\x10\x03\x12\x0e\n\nREDUCE_SUM\x10\x04\x12\x11\n\rREDUCE_STDDEV\x10\x05\x12\x10\n\x0cREDUCE_COUNT\x10\x06\x12\x15\n\x11REDUCE_COUNT_TRUE\x10\x07\x12\x16\n\x12REDUCE_COUNT_FALSE\x10\x0f\x12\x18\n\x14REDUCE_FRACTION_TRUE\x10\x08\x12\x18\n\x14REDUCE_PERCENTILE_99\x10\t\x12\x18\n\x14REDUCE_PERCENTILE_95\x10\n\x12\x18\n\x14REDUCE_PERCENTILE_50\x10\x0b\x12\x18\n\x14REDUCE_PERCENTILE_05\x10\x0c\"\xb3\x03\n\x14PickTimeSeriesFilter\x12\x62\n\x0eranking_method\x18\x01 \x01(\x0e\x32;.google.monitoring.dashboard.v1.PickTimeSeriesFilter.MethodR\rrankingMethod\x12&\n\x0fnum_time_series\x18\x02 \x01(\x05R\rnumTimeSeries\x12\\\n\tdirection\x18\x03 \x01(\x0e\x32>.google.monitoring.dashboard.v1.PickTimeSeriesFilter.DirectionR\tdirection\"t\n\x06Method\x12\x16\n\x12METHOD_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMETHOD_MEAN\x10\x01\x12\x0e\n\nMETHOD_MAX\x10\x02\x12\x0e\n\nMETHOD_MIN\x10\x03\x12\x0e\n\nMETHOD_SUM\x10\x04\x12\x11\n\rMETHOD_LATEST\x10\x05\";\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\x07\n\x03TOP\x10\x01\x12\n\n\x06\x42OTTOM\x10\x02\"\xee\x01\n\x1bStatisticalTimeSeriesFilter\x12i\n\x0eranking_method\x18\x01 \x01(\x0e\x32\x42.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter.MethodR\rrankingMethod\x12&\n\x0fnum_time_series\x18\x02 \x01(\x05R\rnumTimeSeries\"<\n\x06Method\x12\x16\n\x12METHOD_UNSPECIFIED\x10\x00\x12\x1a\n\x16METHOD_CLUSTER_OUTLIER\x10\x01\x42\xf5\x01\n\"com.google.monitoring.dashboard.v1B\x0b\x43ommonProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_distribution__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])



_AGGREGATION_ALIGNER = _descriptor.EnumDescriptor(
  name='Aligner',
  full_name='google.monitoring.dashboard.v1.Aggregation.Aligner',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALIGN_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_DELTA', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_RATE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_INTERPOLATE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_NEXT_OLDER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_MIN', index=5, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_MAX', index=6, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_MEAN', index=7, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_COUNT', index=8, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_SUM', index=9, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_STDDEV', index=10, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_COUNT_TRUE', index=11, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_COUNT_FALSE', index=12, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_FRACTION_TRUE', index=13, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_PERCENTILE_99', index=14, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_PERCENTILE_95', index=15, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_PERCENTILE_50', index=16, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_PERCENTILE_05', index=17, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIGN_PERCENT_CHANGE', index=18, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=471,
  serialized_end=866,
)
_sym_db.RegisterEnumDescriptor(_AGGREGATION_ALIGNER)

_AGGREGATION_REDUCER = _descriptor.EnumDescriptor(
  name='Reducer',
  full_name='google.monitoring.dashboard.v1.Aggregation.Reducer',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REDUCE_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_MEAN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_MIN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_MAX', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_SUM', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_STDDEV', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_COUNT', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_COUNT_TRUE', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_COUNT_FALSE', index=8, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_FRACTION_TRUE', index=9, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_PERCENTILE_99', index=10, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_PERCENTILE_95', index=11, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_PERCENTILE_50', index=12, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDUCE_PERCENTILE_05', index=13, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=869,
  serialized_end=1174,
)
_sym_db.RegisterEnumDescriptor(_AGGREGATION_REDUCER)

_PICKTIMESERIESFILTER_METHOD = _descriptor.EnumDescriptor(
  name='Method',
  full_name='google.monitoring.dashboard.v1.PickTimeSeriesFilter.Method',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='METHOD_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METHOD_MEAN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METHOD_MAX', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METHOD_MIN', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METHOD_SUM', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METHOD_LATEST', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1435,
  serialized_end=1551,
)
_sym_db.RegisterEnumDescriptor(_PICKTIMESERIESFILTER_METHOD)

_PICKTIMESERIESFILTER_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='google.monitoring.dashboard.v1.PickTimeSeriesFilter.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOTTOM', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1553,
  serialized_end=1612,
)
_sym_db.RegisterEnumDescriptor(_PICKTIMESERIESFILTER_DIRECTION)

_STATISTICALTIMESERIESFILTER_METHOD = _descriptor.EnumDescriptor(
  name='Method',
  full_name='google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter.Method',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='METHOD_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METHOD_CLUSTER_OUTLIER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1793,
  serialized_end=1853,
)
_sym_db.RegisterEnumDescriptor(_STATISTICALTIMESERIESFILTER_METHOD)


_AGGREGATION = _descriptor.Descriptor(
  name='Aggregation',
  full_name='google.monitoring.dashboard.v1.Aggregation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alignment_period', full_name='google.monitoring.dashboard.v1.Aggregation.alignment_period', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='alignmentPeriod', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='per_series_aligner', full_name='google.monitoring.dashboard.v1.Aggregation.per_series_aligner', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='perSeriesAligner', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cross_series_reducer', full_name='google.monitoring.dashboard.v1.Aggregation.cross_series_reducer', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='crossSeriesReducer', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_by_fields', full_name='google.monitoring.dashboard.v1.Aggregation.group_by_fields', index=3,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='groupByFields', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AGGREGATION_ALIGNER,
    _AGGREGATION_REDUCER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=1174,
)


_PICKTIMESERIESFILTER = _descriptor.Descriptor(
  name='PickTimeSeriesFilter',
  full_name='google.monitoring.dashboard.v1.PickTimeSeriesFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ranking_method', full_name='google.monitoring.dashboard.v1.PickTimeSeriesFilter.ranking_method', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rankingMethod', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_time_series', full_name='google.monitoring.dashboard.v1.PickTimeSeriesFilter.num_time_series', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='numTimeSeries', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='google.monitoring.dashboard.v1.PickTimeSeriesFilter.direction', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='direction', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PICKTIMESERIESFILTER_METHOD,
    _PICKTIMESERIESFILTER_DIRECTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1177,
  serialized_end=1612,
)


_STATISTICALTIMESERIESFILTER = _descriptor.Descriptor(
  name='StatisticalTimeSeriesFilter',
  full_name='google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ranking_method', full_name='google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter.ranking_method', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rankingMethod', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_time_series', full_name='google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter.num_time_series', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='numTimeSeries', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATISTICALTIMESERIESFILTER_METHOD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1615,
  serialized_end=1853,
)

_AGGREGATION.fields_by_name['alignment_period'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_AGGREGATION.fields_by_name['per_series_aligner'].enum_type = _AGGREGATION_ALIGNER
_AGGREGATION.fields_by_name['cross_series_reducer'].enum_type = _AGGREGATION_REDUCER
_AGGREGATION_ALIGNER.containing_type = _AGGREGATION
_AGGREGATION_REDUCER.containing_type = _AGGREGATION
_PICKTIMESERIESFILTER.fields_by_name['ranking_method'].enum_type = _PICKTIMESERIESFILTER_METHOD
_PICKTIMESERIESFILTER.fields_by_name['direction'].enum_type = _PICKTIMESERIESFILTER_DIRECTION
_PICKTIMESERIESFILTER_METHOD.containing_type = _PICKTIMESERIESFILTER
_PICKTIMESERIESFILTER_DIRECTION.containing_type = _PICKTIMESERIESFILTER
_STATISTICALTIMESERIESFILTER.fields_by_name['ranking_method'].enum_type = _STATISTICALTIMESERIESFILTER_METHOD
_STATISTICALTIMESERIESFILTER_METHOD.containing_type = _STATISTICALTIMESERIESFILTER
DESCRIPTOR.message_types_by_name['Aggregation'] = _AGGREGATION
DESCRIPTOR.message_types_by_name['PickTimeSeriesFilter'] = _PICKTIMESERIESFILTER
DESCRIPTOR.message_types_by_name['StatisticalTimeSeriesFilter'] = _STATISTICALTIMESERIESFILTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Aggregation = _reflection.GeneratedProtocolMessageType('Aggregation', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATION,
  '__module__' : 'google.monitoring.dashboard.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.Aggregation)
  })
_sym_db.RegisterMessage(Aggregation)

PickTimeSeriesFilter = _reflection.GeneratedProtocolMessageType('PickTimeSeriesFilter', (_message.Message,), {
  'DESCRIPTOR' : _PICKTIMESERIESFILTER,
  '__module__' : 'google.monitoring.dashboard.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.PickTimeSeriesFilter)
  })
_sym_db.RegisterMessage(PickTimeSeriesFilter)

StatisticalTimeSeriesFilter = _reflection.GeneratedProtocolMessageType('StatisticalTimeSeriesFilter', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICALTIMESERIESFILTER,
  '__module__' : 'google.monitoring.dashboard.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter)
  })
_sym_db.RegisterMessage(StatisticalTimeSeriesFilter)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
