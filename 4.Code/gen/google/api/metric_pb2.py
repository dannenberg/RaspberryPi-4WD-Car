# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/metric.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import label_pb2 as google_dot_api_dot_label__pb2
from google.api import launch_stage_pb2 as google_dot_api_dot_launch__stage__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/metric.proto',
  package='google.api',
  syntax='proto3',
  serialized_options=b'\n\016com.google.apiB\013MetricProtoP\001Z7google.golang.org/genproto/googleapis/api/metric;metric\242\002\004GAPI',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17google/api/metric.proto\x12\ngoogle.api\x1a\x16google/api/label.proto\x1a\x1dgoogle/api/launch_stage.proto\x1a\x1egoogle/protobuf/duration.proto\"\xc1\x07\n\x10MetricDescriptor\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04type\x18\x08 \x01(\tR\x04type\x12\x33\n\x06labels\x18\x02 \x03(\x0b\x32\x1b.google.api.LabelDescriptorR\x06labels\x12H\n\x0bmetric_kind\x18\x03 \x01(\x0e\x32\'.google.api.MetricDescriptor.MetricKindR\nmetricKind\x12\x45\n\nvalue_type\x18\x04 \x01(\x0e\x32&.google.api.MetricDescriptor.ValueTypeR\tvalueType\x12\x12\n\x04unit\x18\x05 \x01(\tR\x04unit\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12!\n\x0c\x64isplay_name\x18\x07 \x01(\tR\x0b\x64isplayName\x12Q\n\x08metadata\x18\n \x01(\x0b\x32\x35.google.api.MetricDescriptor.MetricDescriptorMetadataR\x08metadata\x12:\n\x0claunch_stage\x18\x0c \x01(\x0e\x32\x17.google.api.LaunchStageR\x0blaunchStage\x12\x38\n\x18monitored_resource_types\x18\r \x03(\tR\x16monitoredResourceTypes\x1a\xd8\x01\n\x18MetricDescriptorMetadata\x12>\n\x0claunch_stage\x18\x01 \x01(\x0e\x32\x17.google.api.LaunchStageB\x02\x18\x01R\x0blaunchStage\x12>\n\rsample_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0csamplePeriod\x12<\n\x0cingest_delay\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0bingestDelay\"O\n\nMetricKind\x12\x1b\n\x17METRIC_KIND_UNSPECIFIED\x10\x00\x12\t\n\x05GAUGE\x10\x01\x12\t\n\x05\x44\x45LTA\x10\x02\x12\x0e\n\nCUMULATIVE\x10\x03\"q\n\tValueType\x12\x1a\n\x16VALUE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x42OOL\x10\x01\x12\t\n\x05INT64\x10\x02\x12\n\n\x06\x44OUBLE\x10\x03\x12\n\n\x06STRING\x10\x04\x12\x10\n\x0c\x44ISTRIBUTION\x10\x05\x12\t\n\x05MONEY\x10\x06\"\x8f\x01\n\x06Metric\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x12\x36\n\x06labels\x18\x02 \x03(\x0b\x32\x1e.google.api.Metric.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42_\n\x0e\x63om.google.apiB\x0bMetricProtoP\x01Z7google.golang.org/genproto/googleapis/api/metric;metric\xa2\x02\x04GAPIb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_label__pb2.DESCRIPTOR,google_dot_api_dot_launch__stage__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])



_METRICDESCRIPTOR_METRICKIND = _descriptor.EnumDescriptor(
  name='MetricKind',
  full_name='google.api.MetricDescriptor.MetricKind',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='METRIC_KIND_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GAUGE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELTA', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUMULATIVE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=894,
  serialized_end=973,
)
_sym_db.RegisterEnumDescriptor(_METRICDESCRIPTOR_METRICKIND)

_METRICDESCRIPTOR_VALUETYPE = _descriptor.EnumDescriptor(
  name='ValueType',
  full_name='google.api.MetricDescriptor.ValueType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VALUE_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISTRIBUTION', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MONEY', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=975,
  serialized_end=1088,
)
_sym_db.RegisterEnumDescriptor(_METRICDESCRIPTOR_VALUETYPE)


_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA = _descriptor.Descriptor(
  name='MetricDescriptorMetadata',
  full_name='google.api.MetricDescriptor.MetricDescriptorMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='launch_stage', full_name='google.api.MetricDescriptor.MetricDescriptorMetadata.launch_stage', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', json_name='launchStage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_period', full_name='google.api.MetricDescriptor.MetricDescriptorMetadata.sample_period', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='samplePeriod', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ingest_delay', full_name='google.api.MetricDescriptor.MetricDescriptorMetadata.ingest_delay', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ingestDelay', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=676,
  serialized_end=892,
)

_METRICDESCRIPTOR = _descriptor.Descriptor(
  name='MetricDescriptor',
  full_name='google.api.MetricDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.api.MetricDescriptor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.api.MetricDescriptor.type', index=1,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.api.MetricDescriptor.labels', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric_kind', full_name='google.api.MetricDescriptor.metric_kind', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metricKind', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value_type', full_name='google.api.MetricDescriptor.value_type', index=4,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='valueType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unit', full_name='google.api.MetricDescriptor.unit', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='unit', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.api.MetricDescriptor.description', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.api.MetricDescriptor.display_name', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='displayName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='google.api.MetricDescriptor.metadata', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metadata', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='launch_stage', full_name='google.api.MetricDescriptor.launch_stage', index=9,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='launchStage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monitored_resource_types', full_name='google.api.MetricDescriptor.monitored_resource_types', index=10,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='monitoredResourceTypes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA, ],
  enum_types=[
    _METRICDESCRIPTOR_METRICKIND,
    _METRICDESCRIPTOR_VALUETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=1088,
)


_METRIC_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.api.Metric.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.api.Metric.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.api.Metric.LabelsEntry.value', index=1,
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
  serialized_start=1177,
  serialized_end=1234,
)

_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='google.api.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='google.api.Metric.type', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.api.Metric.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_METRIC_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1091,
  serialized_end=1234,
)

_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA.fields_by_name['launch_stage'].enum_type = google_dot_api_dot_launch__stage__pb2._LAUNCHSTAGE
_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA.fields_by_name['sample_period'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA.fields_by_name['ingest_delay'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA.containing_type = _METRICDESCRIPTOR
_METRICDESCRIPTOR.fields_by_name['labels'].message_type = google_dot_api_dot_label__pb2._LABELDESCRIPTOR
_METRICDESCRIPTOR.fields_by_name['metric_kind'].enum_type = _METRICDESCRIPTOR_METRICKIND
_METRICDESCRIPTOR.fields_by_name['value_type'].enum_type = _METRICDESCRIPTOR_VALUETYPE
_METRICDESCRIPTOR.fields_by_name['metadata'].message_type = _METRICDESCRIPTOR_METRICDESCRIPTORMETADATA
_METRICDESCRIPTOR.fields_by_name['launch_stage'].enum_type = google_dot_api_dot_launch__stage__pb2._LAUNCHSTAGE
_METRICDESCRIPTOR_METRICKIND.containing_type = _METRICDESCRIPTOR
_METRICDESCRIPTOR_VALUETYPE.containing_type = _METRICDESCRIPTOR
_METRIC_LABELSENTRY.containing_type = _METRIC
_METRIC.fields_by_name['labels'].message_type = _METRIC_LABELSENTRY
DESCRIPTOR.message_types_by_name['MetricDescriptor'] = _METRICDESCRIPTOR
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetricDescriptor = _reflection.GeneratedProtocolMessageType('MetricDescriptor', (_message.Message,), {

  'MetricDescriptorMetadata' : _reflection.GeneratedProtocolMessageType('MetricDescriptorMetadata', (_message.Message,), {
    'DESCRIPTOR' : _METRICDESCRIPTOR_METRICDESCRIPTORMETADATA,
    '__module__' : 'google.api.metric_pb2'
    # @@protoc_insertion_point(class_scope:google.api.MetricDescriptor.MetricDescriptorMetadata)
    })
  ,
  'DESCRIPTOR' : _METRICDESCRIPTOR,
  '__module__' : 'google.api.metric_pb2'
  # @@protoc_insertion_point(class_scope:google.api.MetricDescriptor)
  })
_sym_db.RegisterMessage(MetricDescriptor)
_sym_db.RegisterMessage(MetricDescriptor.MetricDescriptorMetadata)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _METRIC_LABELSENTRY,
    '__module__' : 'google.api.metric_pb2'
    # @@protoc_insertion_point(class_scope:google.api.Metric.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'google.api.metric_pb2'
  # @@protoc_insertion_point(class_scope:google.api.Metric)
  })
_sym_db.RegisterMessage(Metric)
_sym_db.RegisterMessage(Metric.LabelsEntry)


DESCRIPTOR._options = None
_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA.fields_by_name['launch_stage']._options = None
_METRIC_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
