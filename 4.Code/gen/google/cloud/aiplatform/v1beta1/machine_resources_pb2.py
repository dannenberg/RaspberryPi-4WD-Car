# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/machine_resources.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.aiplatform.v1beta1 import accelerator_type_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_accelerator__type__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/aiplatform/v1beta1/machine_resources.proto',
  package='google.cloud.aiplatform.v1beta1',
  syntax='proto3',
  serialized_options=b'\n#com.google.cloud.aiplatform.v1beta1B\025MachineResourcesProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\252\002\037Google.Cloud.AIPlatform.V1Beta1\312\002\037Google\\Cloud\\AIPlatform\\V1beta1\352\002\"Google::Cloud::AIPlatform::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7google/cloud/aiplatform/v1beta1/machine_resources.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x36google/cloud/aiplatform/v1beta1/accelerator_type.proto\x1a\x1cgoogle/api/annotations.proto\"\xc6\x01\n\x0bMachineSpec\x12\'\n\x0cmachine_type\x18\x01 \x01(\tB\x04\xe2\x41\x01\x05R\x0bmachineType\x12\x61\n\x10\x61\x63\x63\x65lerator_type\x18\x02 \x01(\x0e\x32\x30.google.cloud.aiplatform.v1beta1.AcceleratorTypeB\x04\xe2\x41\x01\x05R\x0f\x61\x63\x63\x65leratorType\x12+\n\x11\x61\x63\x63\x65lerator_count\x18\x03 \x01(\x05R\x10\x61\x63\x63\x65leratorCount\"\xc9\x02\n\x12\x44\x65\x64icatedResources\x12V\n\x0cmachine_spec\x18\x01 \x01(\x0b\x32,.google.cloud.aiplatform.v1beta1.MachineSpecB\x05\xe2\x41\x02\x02\x05R\x0bmachineSpec\x12\x31\n\x11min_replica_count\x18\x02 \x01(\x05\x42\x05\xe2\x41\x02\x02\x05R\x0fminReplicaCount\x12\x30\n\x11max_replica_count\x18\x03 \x01(\x05\x42\x04\xe2\x41\x01\x05R\x0fmaxReplicaCount\x12v\n\x18\x61utoscaling_metric_specs\x18\x04 \x03(\x0b\x32\x36.google.cloud.aiplatform.v1beta1.AutoscalingMetricSpecB\x04\xe2\x41\x01\x05R\x16\x61utoscalingMetricSpecs\"x\n\x12\x41utomaticResources\x12\x30\n\x11min_replica_count\x18\x01 \x01(\x05\x42\x04\xe2\x41\x01\x05R\x0fminReplicaCount\x12\x30\n\x11max_replica_count\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x05R\x0fmaxReplicaCount\"\xdf\x01\n\x17\x42\x61tchDedicatedResources\x12V\n\x0cmachine_spec\x18\x01 \x01(\x0b\x32,.google.cloud.aiplatform.v1beta1.MachineSpecB\x05\xe2\x41\x02\x02\x05R\x0bmachineSpec\x12:\n\x16starting_replica_count\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x05R\x14startingReplicaCount\x12\x30\n\x11max_replica_count\x18\x03 \x01(\x05\x42\x04\xe2\x41\x01\x05R\x0fmaxReplicaCount\">\n\x11ResourcesConsumed\x12)\n\rreplica_hours\x18\x01 \x01(\x01\x42\x04\xe2\x41\x01\x03R\x0creplicaHours\"[\n\x08\x44iskSpec\x12$\n\x0e\x62oot_disk_type\x18\x01 \x01(\tR\x0c\x62ootDiskType\x12)\n\x11\x62oot_disk_size_gb\x18\x02 \x01(\x05R\x0e\x62ootDiskSizeGb\"V\n\x15\x41utoscalingMetricSpec\x12%\n\x0bmetric_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\nmetricName\x12\x16\n\x06target\x18\x02 \x01(\x05R\x06targetB\xf2\x01\n#com.google.cloud.aiplatform.v1beta1B\x15MachineResourcesProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02\"Google::Cloud::AIPlatform::V1beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_accelerator__type__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_MACHINESPEC = _descriptor.Descriptor(
  name='MachineSpec',
  full_name='google.cloud.aiplatform.v1beta1.MachineSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machine_type', full_name='google.cloud.aiplatform.v1beta1.MachineSpec.machine_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='machineType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accelerator_type', full_name='google.cloud.aiplatform.v1beta1.MachineSpec.accelerator_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='acceleratorType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accelerator_count', full_name='google.cloud.aiplatform.v1beta1.MachineSpec.accelerator_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='acceleratorCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=212,
  serialized_end=410,
)


_DEDICATEDRESOURCES = _descriptor.Descriptor(
  name='DedicatedResources',
  full_name='google.cloud.aiplatform.v1beta1.DedicatedResources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machine_spec', full_name='google.cloud.aiplatform.v1beta1.DedicatedResources.machine_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\002\002\005', json_name='machineSpec', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_replica_count', full_name='google.cloud.aiplatform.v1beta1.DedicatedResources.min_replica_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\002\002\005', json_name='minReplicaCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_replica_count', full_name='google.cloud.aiplatform.v1beta1.DedicatedResources.max_replica_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='maxReplicaCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autoscaling_metric_specs', full_name='google.cloud.aiplatform.v1beta1.DedicatedResources.autoscaling_metric_specs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='autoscalingMetricSpecs', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=413,
  serialized_end=742,
)


_AUTOMATICRESOURCES = _descriptor.Descriptor(
  name='AutomaticResources',
  full_name='google.cloud.aiplatform.v1beta1.AutomaticResources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_replica_count', full_name='google.cloud.aiplatform.v1beta1.AutomaticResources.min_replica_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='minReplicaCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_replica_count', full_name='google.cloud.aiplatform.v1beta1.AutomaticResources.max_replica_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='maxReplicaCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=744,
  serialized_end=864,
)


_BATCHDEDICATEDRESOURCES = _descriptor.Descriptor(
  name='BatchDedicatedResources',
  full_name='google.cloud.aiplatform.v1beta1.BatchDedicatedResources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machine_spec', full_name='google.cloud.aiplatform.v1beta1.BatchDedicatedResources.machine_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\002\002\005', json_name='machineSpec', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='starting_replica_count', full_name='google.cloud.aiplatform.v1beta1.BatchDedicatedResources.starting_replica_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='startingReplicaCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_replica_count', full_name='google.cloud.aiplatform.v1beta1.BatchDedicatedResources.max_replica_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='maxReplicaCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=867,
  serialized_end=1090,
)


_RESOURCESCONSUMED = _descriptor.Descriptor(
  name='ResourcesConsumed',
  full_name='google.cloud.aiplatform.v1beta1.ResourcesConsumed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='replica_hours', full_name='google.cloud.aiplatform.v1beta1.ResourcesConsumed.replica_hours', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='replicaHours', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1092,
  serialized_end=1154,
)


_DISKSPEC = _descriptor.Descriptor(
  name='DiskSpec',
  full_name='google.cloud.aiplatform.v1beta1.DiskSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='boot_disk_type', full_name='google.cloud.aiplatform.v1beta1.DiskSpec.boot_disk_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bootDiskType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='boot_disk_size_gb', full_name='google.cloud.aiplatform.v1beta1.DiskSpec.boot_disk_size_gb', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bootDiskSizeGb', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1156,
  serialized_end=1247,
)


_AUTOSCALINGMETRICSPEC = _descriptor.Descriptor(
  name='AutoscalingMetricSpec',
  full_name='google.cloud.aiplatform.v1beta1.AutoscalingMetricSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_name', full_name='google.cloud.aiplatform.v1beta1.AutoscalingMetricSpec.metric_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='metricName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='google.cloud.aiplatform.v1beta1.AutoscalingMetricSpec.target', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='target', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1249,
  serialized_end=1335,
)

_MACHINESPEC.fields_by_name['accelerator_type'].enum_type = google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_accelerator__type__pb2._ACCELERATORTYPE
_DEDICATEDRESOURCES.fields_by_name['machine_spec'].message_type = _MACHINESPEC
_DEDICATEDRESOURCES.fields_by_name['autoscaling_metric_specs'].message_type = _AUTOSCALINGMETRICSPEC
_BATCHDEDICATEDRESOURCES.fields_by_name['machine_spec'].message_type = _MACHINESPEC
DESCRIPTOR.message_types_by_name['MachineSpec'] = _MACHINESPEC
DESCRIPTOR.message_types_by_name['DedicatedResources'] = _DEDICATEDRESOURCES
DESCRIPTOR.message_types_by_name['AutomaticResources'] = _AUTOMATICRESOURCES
DESCRIPTOR.message_types_by_name['BatchDedicatedResources'] = _BATCHDEDICATEDRESOURCES
DESCRIPTOR.message_types_by_name['ResourcesConsumed'] = _RESOURCESCONSUMED
DESCRIPTOR.message_types_by_name['DiskSpec'] = _DISKSPEC
DESCRIPTOR.message_types_by_name['AutoscalingMetricSpec'] = _AUTOSCALINGMETRICSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MachineSpec = _reflection.GeneratedProtocolMessageType('MachineSpec', (_message.Message,), {
  'DESCRIPTOR' : _MACHINESPEC,
  '__module__' : 'google.cloud.aiplatform.v1beta1.machine_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.MachineSpec)
  })
_sym_db.RegisterMessage(MachineSpec)

DedicatedResources = _reflection.GeneratedProtocolMessageType('DedicatedResources', (_message.Message,), {
  'DESCRIPTOR' : _DEDICATEDRESOURCES,
  '__module__' : 'google.cloud.aiplatform.v1beta1.machine_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.DedicatedResources)
  })
_sym_db.RegisterMessage(DedicatedResources)

AutomaticResources = _reflection.GeneratedProtocolMessageType('AutomaticResources', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMATICRESOURCES,
  '__module__' : 'google.cloud.aiplatform.v1beta1.machine_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.AutomaticResources)
  })
_sym_db.RegisterMessage(AutomaticResources)

BatchDedicatedResources = _reflection.GeneratedProtocolMessageType('BatchDedicatedResources', (_message.Message,), {
  'DESCRIPTOR' : _BATCHDEDICATEDRESOURCES,
  '__module__' : 'google.cloud.aiplatform.v1beta1.machine_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.BatchDedicatedResources)
  })
_sym_db.RegisterMessage(BatchDedicatedResources)

ResourcesConsumed = _reflection.GeneratedProtocolMessageType('ResourcesConsumed', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCESCONSUMED,
  '__module__' : 'google.cloud.aiplatform.v1beta1.machine_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ResourcesConsumed)
  })
_sym_db.RegisterMessage(ResourcesConsumed)

DiskSpec = _reflection.GeneratedProtocolMessageType('DiskSpec', (_message.Message,), {
  'DESCRIPTOR' : _DISKSPEC,
  '__module__' : 'google.cloud.aiplatform.v1beta1.machine_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.DiskSpec)
  })
_sym_db.RegisterMessage(DiskSpec)

AutoscalingMetricSpec = _reflection.GeneratedProtocolMessageType('AutoscalingMetricSpec', (_message.Message,), {
  'DESCRIPTOR' : _AUTOSCALINGMETRICSPEC,
  '__module__' : 'google.cloud.aiplatform.v1beta1.machine_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.AutoscalingMetricSpec)
  })
_sym_db.RegisterMessage(AutoscalingMetricSpec)


DESCRIPTOR._options = None
_MACHINESPEC.fields_by_name['machine_type']._options = None
_MACHINESPEC.fields_by_name['accelerator_type']._options = None
_DEDICATEDRESOURCES.fields_by_name['machine_spec']._options = None
_DEDICATEDRESOURCES.fields_by_name['min_replica_count']._options = None
_DEDICATEDRESOURCES.fields_by_name['max_replica_count']._options = None
_DEDICATEDRESOURCES.fields_by_name['autoscaling_metric_specs']._options = None
_AUTOMATICRESOURCES.fields_by_name['min_replica_count']._options = None
_AUTOMATICRESOURCES.fields_by_name['max_replica_count']._options = None
_BATCHDEDICATEDRESOURCES.fields_by_name['machine_spec']._options = None
_BATCHDEDICATEDRESOURCES.fields_by_name['starting_replica_count']._options = None
_BATCHDEDICATEDRESOURCES.fields_by_name['max_replica_count']._options = None
_RESOURCESCONSUMED.fields_by_name['replica_hours']._options = None
_AUTOSCALINGMETRICSPEC.fields_by_name['metric_name']._options = None
# @@protoc_insertion_point(module_scope)
