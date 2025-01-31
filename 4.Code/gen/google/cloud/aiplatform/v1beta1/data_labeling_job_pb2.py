# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/data_labeling_job.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.aiplatform.v1beta1 import accelerator_type_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_accelerator__type__pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from google.cloud.aiplatform.v1beta1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_job__state__pb2
from google.cloud.aiplatform.v1beta1 import specialist_pool_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_specialist__pool__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.type import money_pb2 as google_dot_type_dot_money__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/aiplatform/v1beta1/data_labeling_job.proto',
  package='google.cloud.aiplatform.v1beta1',
  syntax='proto3',
  serialized_options=b'\n#com.google.cloud.aiplatform.v1beta1B\024DataLabelingJobProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\252\002\037Google.Cloud.AIPlatform.V1Beta1\312\002\037Google\\Cloud\\AIPlatform\\V1beta1\352\002\"Google::Cloud::AIPlatform::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7google/cloud/aiplatform/v1beta1/data_labeling_job.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x36google/cloud/aiplatform/v1beta1/accelerator_type.proto\x1a\x35google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a/google/cloud/aiplatform/v1beta1/job_state.proto\x1a\x35google/cloud/aiplatform/v1beta1/specialist_pool.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x17google/type/money.proto\x1a\x1cgoogle/api/annotations.proto\"\x88\x0b\n\x0f\x44\x61taLabelingJob\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\'\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0b\x64isplayName\x12\x46\n\x08\x64\x61tasets\x18\x03 \x03(\tB*\xe2\x41\x01\x02\xfa\x41#\n!aiplatform.googleapis.com/DatasetR\x08\x64\x61tasets\x12s\n\x11\x61nnotation_labels\x18\x0c \x03(\x0b\x32\x46.google.cloud.aiplatform.v1beta1.DataLabelingJob.AnnotationLabelsEntryR\x10\x61nnotationLabels\x12)\n\rlabeler_count\x18\x04 \x01(\x05\x42\x04\xe2\x41\x01\x02R\x0clabelerCount\x12-\n\x0finstruction_uri\x18\x05 \x01(\tB\x04\xe2\x41\x01\x02R\x0einstructionUri\x12\x30\n\x11inputs_schema_uri\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02R\x0finputsSchemaUri\x12\x34\n\x06inputs\x18\x07 \x01(\x0b\x32\x16.google.protobuf.ValueB\x04\xe2\x41\x01\x02R\x06inputs\x12\x45\n\x05state\x18\x08 \x01(\x0e\x32).google.cloud.aiplatform.v1beta1.JobStateB\x04\xe2\x41\x01\x03R\x05state\x12\x31\n\x11labeling_progress\x18\r \x01(\x05\x42\x04\xe2\x41\x01\x03R\x10labelingProgress\x12=\n\rcurrent_spend\x18\x0e \x01(\x0b\x32\x12.google.type.MoneyB\x04\xe2\x41\x01\x03R\x0c\x63urrentSpend\x12\x41\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12.\n\x05\x65rror\x18\x16 \x01(\x0b\x32\x12.google.rpc.StatusB\x04\xe2\x41\x01\x03R\x05\x65rror\x12T\n\x06labels\x18\x0b \x03(\x0b\x32<.google.cloud.aiplatform.v1beta1.DataLabelingJob.LabelsEntryR\x06labels\x12)\n\x10specialist_pools\x18\x10 \x03(\tR\x0fspecialistPools\x12X\n\x0f\x65ncryption_spec\x18\x14 \x01(\x0b\x32/.google.cloud.aiplatform.v1beta1.EncryptionSpecR\x0e\x65ncryptionSpec\x12k\n\x16\x61\x63tive_learning_config\x18\x15 \x01(\x0b\x32\x35.google.cloud.aiplatform.v1beta1.ActiveLearningConfigR\x14\x61\x63tiveLearningConfig\x1a\x43\n\x15\x41nnotationLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:|\xea\x41y\n)aiplatform.googleapis.com/DataLabelingJob\x12Lprojects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}\"\xc9\x02\n\x14\x41\x63tiveLearningConfig\x12/\n\x13max_data_item_count\x18\x01 \x01(\x03H\x00R\x10maxDataItemCount\x12\x39\n\x18max_data_item_percentage\x18\x02 \x01(\x05H\x00R\x15maxDataItemPercentage\x12R\n\rsample_config\x18\x03 \x01(\x0b\x32-.google.cloud.aiplatform.v1beta1.SampleConfigR\x0csampleConfig\x12X\n\x0ftraining_config\x18\x04 \x01(\x0b\x32/.google.cloud.aiplatform.v1beta1.TrainingConfigR\x0etrainingConfigB\x17\n\x15human_labeling_budget\"\x8b\x03\n\x0cSampleConfig\x12G\n\x1finitial_batch_sample_percentage\x18\x01 \x01(\x05H\x00R\x1cinitialBatchSamplePercentage\x12K\n!following_batch_sample_percentage\x18\x03 \x01(\x05H\x01R\x1e\x66ollowingBatchSamplePercentage\x12\x65\n\x0fsample_strategy\x18\x05 \x01(\x0e\x32<.google.cloud.aiplatform.v1beta1.SampleConfig.SampleStrategyR\x0esampleStrategy\"B\n\x0eSampleStrategy\x12\x1f\n\x1bSAMPLE_STRATEGY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bUNCERTAINTY\x10\x01\x42\x1b\n\x19initial_batch_sample_sizeB\x1d\n\x1b\x66ollowing_batch_sample_size\"Q\n\x0eTrainingConfig\x12?\n\x1ctimeout_training_milli_hours\x18\x01 \x01(\x03R\x19timeoutTrainingMilliHoursB\xf1\x01\n#com.google.cloud.aiplatform.v1beta1B\x14\x44\x61taLabelingJobProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02\"Google::Cloud::AIPlatform::V1beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_accelerator__type__pb2.DESCRIPTOR,google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2.DESCRIPTOR,google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_job__state__pb2.DESCRIPTOR,google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_specialist__pool__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_type_dot_money__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_SAMPLECONFIG_SAMPLESTRATEGY = _descriptor.EnumDescriptor(
  name='SampleStrategy',
  full_name='google.cloud.aiplatform.v1beta1.SampleConfig.SampleStrategy',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SAMPLE_STRATEGY_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNCERTAINTY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2531,
  serialized_end=2597,
)
_sym_db.RegisterEnumDescriptor(_SAMPLECONFIG_SAMPLESTRATEGY)


_DATALABELINGJOB_ANNOTATIONLABELSENTRY = _descriptor.Descriptor(
  name='AnnotationLabelsEntry',
  full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.AnnotationLabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.AnnotationLabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.AnnotationLabelsEntry.value', index=1,
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
  serialized_start=1675,
  serialized_end=1742,
)

_DATALABELINGJOB_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.LabelsEntry.value', index=1,
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
  serialized_start=1744,
  serialized_end=1801,
)

_DATALABELINGJOB = _descriptor.Descriptor(
  name='DataLabelingJob',
  full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='displayName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='datasets', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.datasets', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A#\n!aiplatform.googleapis.com/Dataset', json_name='datasets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='annotation_labels', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.annotation_labels', index=3,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='annotationLabels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labeler_count', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.labeler_count', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='labelerCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instruction_uri', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.instruction_uri', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='instructionUri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputs_schema_uri', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.inputs_schema_uri', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='inputsSchemaUri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.inputs', index=7,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='inputs', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.state', index=8,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='state', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labeling_progress', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.labeling_progress', index=9,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='labelingProgress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_spend', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.current_spend', index=10,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='currentSpend', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.create_time', index=11,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='createTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.update_time', index=12,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='updateTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.error', index=13,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='error', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.labels', index=14,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='specialist_pools', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.specialist_pools', index=15,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='specialistPools', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encryption_spec', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.encryption_spec', index=16,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='encryptionSpec', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active_learning_config', full_name='google.cloud.aiplatform.v1beta1.DataLabelingJob.active_learning_config', index=17,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='activeLearningConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATALABELINGJOB_ANNOTATIONLABELSENTRY, _DATALABELINGJOB_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=b'\352Ay\n)aiplatform.googleapis.com/DataLabelingJob\022Lprojects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=1927,
)


_ACTIVELEARNINGCONFIG = _descriptor.Descriptor(
  name='ActiveLearningConfig',
  full_name='google.cloud.aiplatform.v1beta1.ActiveLearningConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_data_item_count', full_name='google.cloud.aiplatform.v1beta1.ActiveLearningConfig.max_data_item_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='maxDataItemCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_data_item_percentage', full_name='google.cloud.aiplatform.v1beta1.ActiveLearningConfig.max_data_item_percentage', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='maxDataItemPercentage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_config', full_name='google.cloud.aiplatform.v1beta1.ActiveLearningConfig.sample_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sampleConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='training_config', full_name='google.cloud.aiplatform.v1beta1.ActiveLearningConfig.training_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='trainingConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='human_labeling_budget', full_name='google.cloud.aiplatform.v1beta1.ActiveLearningConfig.human_labeling_budget',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1930,
  serialized_end=2259,
)


_SAMPLECONFIG = _descriptor.Descriptor(
  name='SampleConfig',
  full_name='google.cloud.aiplatform.v1beta1.SampleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='initial_batch_sample_percentage', full_name='google.cloud.aiplatform.v1beta1.SampleConfig.initial_batch_sample_percentage', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='initialBatchSamplePercentage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='following_batch_sample_percentage', full_name='google.cloud.aiplatform.v1beta1.SampleConfig.following_batch_sample_percentage', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='followingBatchSamplePercentage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_strategy', full_name='google.cloud.aiplatform.v1beta1.SampleConfig.sample_strategy', index=2,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sampleStrategy', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SAMPLECONFIG_SAMPLESTRATEGY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='initial_batch_sample_size', full_name='google.cloud.aiplatform.v1beta1.SampleConfig.initial_batch_sample_size',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='following_batch_sample_size', full_name='google.cloud.aiplatform.v1beta1.SampleConfig.following_batch_sample_size',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=2262,
  serialized_end=2657,
)


_TRAININGCONFIG = _descriptor.Descriptor(
  name='TrainingConfig',
  full_name='google.cloud.aiplatform.v1beta1.TrainingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout_training_milli_hours', full_name='google.cloud.aiplatform.v1beta1.TrainingConfig.timeout_training_milli_hours', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timeoutTrainingMilliHours', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2659,
  serialized_end=2740,
)

_DATALABELINGJOB_ANNOTATIONLABELSENTRY.containing_type = _DATALABELINGJOB
_DATALABELINGJOB_LABELSENTRY.containing_type = _DATALABELINGJOB
_DATALABELINGJOB.fields_by_name['annotation_labels'].message_type = _DATALABELINGJOB_ANNOTATIONLABELSENTRY
_DATALABELINGJOB.fields_by_name['inputs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_DATALABELINGJOB.fields_by_name['state'].enum_type = google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_job__state__pb2._JOBSTATE
_DATALABELINGJOB.fields_by_name['current_spend'].message_type = google_dot_type_dot_money__pb2._MONEY
_DATALABELINGJOB.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATALABELINGJOB.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATALABELINGJOB.fields_by_name['error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_DATALABELINGJOB.fields_by_name['labels'].message_type = _DATALABELINGJOB_LABELSENTRY
_DATALABELINGJOB.fields_by_name['encryption_spec'].message_type = google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2._ENCRYPTIONSPEC
_DATALABELINGJOB.fields_by_name['active_learning_config'].message_type = _ACTIVELEARNINGCONFIG
_ACTIVELEARNINGCONFIG.fields_by_name['sample_config'].message_type = _SAMPLECONFIG
_ACTIVELEARNINGCONFIG.fields_by_name['training_config'].message_type = _TRAININGCONFIG
_ACTIVELEARNINGCONFIG.oneofs_by_name['human_labeling_budget'].fields.append(
  _ACTIVELEARNINGCONFIG.fields_by_name['max_data_item_count'])
_ACTIVELEARNINGCONFIG.fields_by_name['max_data_item_count'].containing_oneof = _ACTIVELEARNINGCONFIG.oneofs_by_name['human_labeling_budget']
_ACTIVELEARNINGCONFIG.oneofs_by_name['human_labeling_budget'].fields.append(
  _ACTIVELEARNINGCONFIG.fields_by_name['max_data_item_percentage'])
_ACTIVELEARNINGCONFIG.fields_by_name['max_data_item_percentage'].containing_oneof = _ACTIVELEARNINGCONFIG.oneofs_by_name['human_labeling_budget']
_SAMPLECONFIG.fields_by_name['sample_strategy'].enum_type = _SAMPLECONFIG_SAMPLESTRATEGY
_SAMPLECONFIG_SAMPLESTRATEGY.containing_type = _SAMPLECONFIG
_SAMPLECONFIG.oneofs_by_name['initial_batch_sample_size'].fields.append(
  _SAMPLECONFIG.fields_by_name['initial_batch_sample_percentage'])
_SAMPLECONFIG.fields_by_name['initial_batch_sample_percentage'].containing_oneof = _SAMPLECONFIG.oneofs_by_name['initial_batch_sample_size']
_SAMPLECONFIG.oneofs_by_name['following_batch_sample_size'].fields.append(
  _SAMPLECONFIG.fields_by_name['following_batch_sample_percentage'])
_SAMPLECONFIG.fields_by_name['following_batch_sample_percentage'].containing_oneof = _SAMPLECONFIG.oneofs_by_name['following_batch_sample_size']
DESCRIPTOR.message_types_by_name['DataLabelingJob'] = _DATALABELINGJOB
DESCRIPTOR.message_types_by_name['ActiveLearningConfig'] = _ACTIVELEARNINGCONFIG
DESCRIPTOR.message_types_by_name['SampleConfig'] = _SAMPLECONFIG
DESCRIPTOR.message_types_by_name['TrainingConfig'] = _TRAININGCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataLabelingJob = _reflection.GeneratedProtocolMessageType('DataLabelingJob', (_message.Message,), {

  'AnnotationLabelsEntry' : _reflection.GeneratedProtocolMessageType('AnnotationLabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATALABELINGJOB_ANNOTATIONLABELSENTRY,
    '__module__' : 'google.cloud.aiplatform.v1beta1.data_labeling_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.DataLabelingJob.AnnotationLabelsEntry)
    })
  ,

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATALABELINGJOB_LABELSENTRY,
    '__module__' : 'google.cloud.aiplatform.v1beta1.data_labeling_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.DataLabelingJob.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _DATALABELINGJOB,
  '__module__' : 'google.cloud.aiplatform.v1beta1.data_labeling_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.DataLabelingJob)
  })
_sym_db.RegisterMessage(DataLabelingJob)
_sym_db.RegisterMessage(DataLabelingJob.AnnotationLabelsEntry)
_sym_db.RegisterMessage(DataLabelingJob.LabelsEntry)

ActiveLearningConfig = _reflection.GeneratedProtocolMessageType('ActiveLearningConfig', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVELEARNINGCONFIG,
  '__module__' : 'google.cloud.aiplatform.v1beta1.data_labeling_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ActiveLearningConfig)
  })
_sym_db.RegisterMessage(ActiveLearningConfig)

SampleConfig = _reflection.GeneratedProtocolMessageType('SampleConfig', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLECONFIG,
  '__module__' : 'google.cloud.aiplatform.v1beta1.data_labeling_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.SampleConfig)
  })
_sym_db.RegisterMessage(SampleConfig)

TrainingConfig = _reflection.GeneratedProtocolMessageType('TrainingConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRAININGCONFIG,
  '__module__' : 'google.cloud.aiplatform.v1beta1.data_labeling_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.TrainingConfig)
  })
_sym_db.RegisterMessage(TrainingConfig)


DESCRIPTOR._options = None
_DATALABELINGJOB_ANNOTATIONLABELSENTRY._options = None
_DATALABELINGJOB_LABELSENTRY._options = None
_DATALABELINGJOB.fields_by_name['name']._options = None
_DATALABELINGJOB.fields_by_name['display_name']._options = None
_DATALABELINGJOB.fields_by_name['datasets']._options = None
_DATALABELINGJOB.fields_by_name['labeler_count']._options = None
_DATALABELINGJOB.fields_by_name['instruction_uri']._options = None
_DATALABELINGJOB.fields_by_name['inputs_schema_uri']._options = None
_DATALABELINGJOB.fields_by_name['inputs']._options = None
_DATALABELINGJOB.fields_by_name['state']._options = None
_DATALABELINGJOB.fields_by_name['labeling_progress']._options = None
_DATALABELINGJOB.fields_by_name['current_spend']._options = None
_DATALABELINGJOB.fields_by_name['create_time']._options = None
_DATALABELINGJOB.fields_by_name['update_time']._options = None
_DATALABELINGJOB.fields_by_name['error']._options = None
_DATALABELINGJOB._options = None
# @@protoc_insertion_point(module_scope)
