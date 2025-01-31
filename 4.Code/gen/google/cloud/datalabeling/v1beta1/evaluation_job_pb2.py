# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datalabeling/v1beta1/evaluation_job.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.datalabeling.v1beta1 import dataset_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_dataset__pb2
from google.cloud.datalabeling.v1beta1 import evaluation_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_evaluation__pb2
from google.cloud.datalabeling.v1beta1 import human_annotation_config_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_human__annotation__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/datalabeling/v1beta1/evaluation_job.proto',
  package='google.cloud.datalabeling.v1beta1',
  syntax='proto3',
  serialized_options=b'\n%com.google.cloud.datalabeling.v1beta1P\001ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabeling\252\002!Google.Cloud.DataLabeling.V1Beta1\312\002!Google\\Cloud\\DataLabeling\\V1beta1\352\002$Google::Cloud::DataLabeling::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6google/cloud/datalabeling/v1beta1/evaluation_job.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/datalabeling/v1beta1/dataset.proto\x1a\x32google/cloud/datalabeling/v1beta1/evaluation.proto\x1a?google/cloud/datalabeling/v1beta1/human_annotation_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"\xeb\x05\n\rEvaluationJob\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12L\n\x05state\x18\x03 \x01(\x0e\x32\x36.google.cloud.datalabeling.v1beta1.EvaluationJob.StateR\x05state\x12\x1a\n\x08schedule\x18\x04 \x01(\tR\x08schedule\x12#\n\rmodel_version\x18\x05 \x01(\tR\x0cmodelVersion\x12j\n\x15\x65valuation_job_config\x18\x06 \x01(\x0b\x32\x36.google.cloud.datalabeling.v1beta1.EvaluationJobConfigR\x13\x65valuationJobConfig\x12.\n\x13\x61nnotation_spec_set\x18\x07 \x01(\tR\x11\x61nnotationSpecSet\x12;\n\x1alabel_missing_ground_truth\x18\x08 \x01(\x08R\x17labelMissingGroundTruth\x12\x46\n\x08\x61ttempts\x18\t \x03(\x0b\x32*.google.cloud.datalabeling.v1beta1.AttemptR\x08\x61ttempts\x12;\n\x0b\x63reate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\"S\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSCHEDULED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\n\n\x06PAUSED\x10\x03\x12\x0b\n\x07STOPPED\x10\x04:b\xea\x41_\n)datalabeling.googleapis.com/EvaluationJob\x12\x32projects/{project}/evaluationJobs/{evaluation_job}\"\xee\x08\n\x13\x45valuationJobConfig\x12~\n\x1bimage_classification_config\x18\x04 \x01(\x0b\x32<.google.cloud.datalabeling.v1beta1.ImageClassificationConfigH\x00R\x19imageClassificationConfig\x12i\n\x14\x62ounding_poly_config\x18\x05 \x01(\x0b\x32\x35.google.cloud.datalabeling.v1beta1.BoundingPolyConfigH\x00R\x12\x62oundingPolyConfig\x12{\n\x1atext_classification_config\x18\x08 \x01(\x0b\x32;.google.cloud.datalabeling.v1beta1.TextClassificationConfigH\x00R\x18textClassificationConfig\x12Q\n\x0cinput_config\x18\x01 \x01(\x0b\x32..google.cloud.datalabeling.v1beta1.InputConfigR\x0binputConfig\x12`\n\x11\x65valuation_config\x18\x02 \x01(\x0b\x32\x33.google.cloud.datalabeling.v1beta1.EvaluationConfigR\x10\x65valuationConfig\x12p\n\x17human_annotation_config\x18\x03 \x01(\x0b\x32\x38.google.cloud.datalabeling.v1beta1.HumanAnnotationConfigR\x15humanAnnotationConfig\x12\x80\x01\n\x14\x62igquery_import_keys\x18\t \x03(\x0b\x32N.google.cloud.datalabeling.v1beta1.EvaluationJobConfig.BigqueryImportKeysEntryR\x12\x62igqueryImportKeys\x12#\n\rexample_count\x18\n \x01(\x05R\x0c\x65xampleCount\x12:\n\x19\x65xample_sample_percentage\x18\x0b \x01(\x01R\x17\x65xampleSamplePercentage\x12z\n\x1b\x65valuation_job_alert_config\x18\r \x01(\x0b\x32;.google.cloud.datalabeling.v1beta1.EvaluationJobAlertConfigR\x18\x65valuationJobAlertConfig\x1a\x45\n\x17\x42igqueryImportKeysEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42!\n\x1fhuman_annotation_request_config\"\x82\x01\n\x18\x45valuationJobAlertConfig\x12\x14\n\x05\x65mail\x18\x01 \x01(\tR\x05\x65mail\x12P\n%min_acceptable_mean_average_precision\x18\x02 \x01(\x01R!minAcceptableMeanAveragePrecision\"\x87\x01\n\x07\x41ttempt\x12=\n\x0c\x61ttempt_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x61ttemptTime\x12=\n\x10partial_failures\x18\x02 \x03(\x0b\x32\x12.google.rpc.StatusR\x0fpartialFailuresB\xe7\x01\n%com.google.cloud.datalabeling.v1beta1P\x01ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabeling\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_dataset__pb2.DESCRIPTOR,google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_evaluation__pb2.DESCRIPTOR,google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_human__annotation__config__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])



_EVALUATIONJOB_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='google.cloud.datalabeling.v1beta1.EvaluationJob.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCHEDULED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=939,
  serialized_end=1022,
)
_sym_db.RegisterEnumDescriptor(_EVALUATIONJOB_STATE)


_EVALUATIONJOB = _descriptor.Descriptor(
  name='EvaluationJob',
  full_name='google.cloud.datalabeling.v1beta1.EvaluationJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.datalabeling.v1beta1.EvaluationJob.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.datalabeling.v1beta1.EvaluationJob.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='google.cloud.datalabeling.v1beta1.EvaluationJob.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='state', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schedule', full_name='google.cloud.datalabeling.v1beta1.EvaluationJob.schedule', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='schedule', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_version', full_name='google.cloud.datalabeling.v1beta1.EvaluationJob.model_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='modelVersion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evaluation_job_config', full_name='google.cloud.datalabeling.v1beta1.EvaluationJob.evaluation_job_config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='evaluationJobConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='annotation_spec_set', full_name='google.cloud.datalabeling.v1beta1.EvaluationJob.annotation_spec_set', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='annotationSpecSet', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label_missing_ground_truth', full_name='google.cloud.datalabeling.v1beta1.EvaluationJob.label_missing_ground_truth', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labelMissingGroundTruth', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attempts', full_name='google.cloud.datalabeling.v1beta1.EvaluationJob.attempts', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='attempts', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.datalabeling.v1beta1.EvaluationJob.create_time', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='createTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVALUATIONJOB_STATE,
  ],
  serialized_options=b'\352A_\n)datalabeling.googleapis.com/EvaluationJob\0222projects/{project}/evaluationJobs/{evaluation_job}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=1122,
)


_EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY = _descriptor.Descriptor(
  name='BigqueryImportKeysEntry',
  full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.BigqueryImportKeysEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.BigqueryImportKeysEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.BigqueryImportKeysEntry.value', index=1,
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
  serialized_start=2155,
  serialized_end=2224,
)

_EVALUATIONJOBCONFIG = _descriptor.Descriptor(
  name='EvaluationJobConfig',
  full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_classification_config', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.image_classification_config', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='imageClassificationConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bounding_poly_config', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.bounding_poly_config', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='boundingPolyConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text_classification_config', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.text_classification_config', index=2,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='textClassificationConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_config', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.input_config', index=3,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='inputConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evaluation_config', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.evaluation_config', index=4,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='evaluationConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='human_annotation_config', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.human_annotation_config', index=5,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='humanAnnotationConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bigquery_import_keys', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.bigquery_import_keys', index=6,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bigqueryImportKeys', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='example_count', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.example_count', index=7,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='exampleCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='example_sample_percentage', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.example_sample_percentage', index=8,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='exampleSamplePercentage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evaluation_job_alert_config', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.evaluation_job_alert_config', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='evaluationJobAlertConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='human_annotation_request_config', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobConfig.human_annotation_request_config',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1125,
  serialized_end=2259,
)


_EVALUATIONJOBALERTCONFIG = _descriptor.Descriptor(
  name='EvaluationJobAlertConfig',
  full_name='google.cloud.datalabeling.v1beta1.EvaluationJobAlertConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobAlertConfig.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='email', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_acceptable_mean_average_precision', full_name='google.cloud.datalabeling.v1beta1.EvaluationJobAlertConfig.min_acceptable_mean_average_precision', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='minAcceptableMeanAveragePrecision', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2262,
  serialized_end=2392,
)


_ATTEMPT = _descriptor.Descriptor(
  name='Attempt',
  full_name='google.cloud.datalabeling.v1beta1.Attempt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attempt_time', full_name='google.cloud.datalabeling.v1beta1.Attempt.attempt_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='attemptTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partial_failures', full_name='google.cloud.datalabeling.v1beta1.Attempt.partial_failures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='partialFailures', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2395,
  serialized_end=2530,
)

_EVALUATIONJOB.fields_by_name['state'].enum_type = _EVALUATIONJOB_STATE
_EVALUATIONJOB.fields_by_name['evaluation_job_config'].message_type = _EVALUATIONJOBCONFIG
_EVALUATIONJOB.fields_by_name['attempts'].message_type = _ATTEMPT
_EVALUATIONJOB.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVALUATIONJOB_STATE.containing_type = _EVALUATIONJOB
_EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY.containing_type = _EVALUATIONJOBCONFIG
_EVALUATIONJOBCONFIG.fields_by_name['image_classification_config'].message_type = google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_human__annotation__config__pb2._IMAGECLASSIFICATIONCONFIG
_EVALUATIONJOBCONFIG.fields_by_name['bounding_poly_config'].message_type = google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_human__annotation__config__pb2._BOUNDINGPOLYCONFIG
_EVALUATIONJOBCONFIG.fields_by_name['text_classification_config'].message_type = google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_human__annotation__config__pb2._TEXTCLASSIFICATIONCONFIG
_EVALUATIONJOBCONFIG.fields_by_name['input_config'].message_type = google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_dataset__pb2._INPUTCONFIG
_EVALUATIONJOBCONFIG.fields_by_name['evaluation_config'].message_type = google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_evaluation__pb2._EVALUATIONCONFIG
_EVALUATIONJOBCONFIG.fields_by_name['human_annotation_config'].message_type = google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_human__annotation__config__pb2._HUMANANNOTATIONCONFIG
_EVALUATIONJOBCONFIG.fields_by_name['bigquery_import_keys'].message_type = _EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY
_EVALUATIONJOBCONFIG.fields_by_name['evaluation_job_alert_config'].message_type = _EVALUATIONJOBALERTCONFIG
_EVALUATIONJOBCONFIG.oneofs_by_name['human_annotation_request_config'].fields.append(
  _EVALUATIONJOBCONFIG.fields_by_name['image_classification_config'])
_EVALUATIONJOBCONFIG.fields_by_name['image_classification_config'].containing_oneof = _EVALUATIONJOBCONFIG.oneofs_by_name['human_annotation_request_config']
_EVALUATIONJOBCONFIG.oneofs_by_name['human_annotation_request_config'].fields.append(
  _EVALUATIONJOBCONFIG.fields_by_name['bounding_poly_config'])
_EVALUATIONJOBCONFIG.fields_by_name['bounding_poly_config'].containing_oneof = _EVALUATIONJOBCONFIG.oneofs_by_name['human_annotation_request_config']
_EVALUATIONJOBCONFIG.oneofs_by_name['human_annotation_request_config'].fields.append(
  _EVALUATIONJOBCONFIG.fields_by_name['text_classification_config'])
_EVALUATIONJOBCONFIG.fields_by_name['text_classification_config'].containing_oneof = _EVALUATIONJOBCONFIG.oneofs_by_name['human_annotation_request_config']
_ATTEMPT.fields_by_name['attempt_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ATTEMPT.fields_by_name['partial_failures'].message_type = google_dot_rpc_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['EvaluationJob'] = _EVALUATIONJOB
DESCRIPTOR.message_types_by_name['EvaluationJobConfig'] = _EVALUATIONJOBCONFIG
DESCRIPTOR.message_types_by_name['EvaluationJobAlertConfig'] = _EVALUATIONJOBALERTCONFIG
DESCRIPTOR.message_types_by_name['Attempt'] = _ATTEMPT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EvaluationJob = _reflection.GeneratedProtocolMessageType('EvaluationJob', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATIONJOB,
  '__module__' : 'google.cloud.datalabeling.v1beta1.evaluation_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.EvaluationJob)
  })
_sym_db.RegisterMessage(EvaluationJob)

EvaluationJobConfig = _reflection.GeneratedProtocolMessageType('EvaluationJobConfig', (_message.Message,), {

  'BigqueryImportKeysEntry' : _reflection.GeneratedProtocolMessageType('BigqueryImportKeysEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY,
    '__module__' : 'google.cloud.datalabeling.v1beta1.evaluation_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.EvaluationJobConfig.BigqueryImportKeysEntry)
    })
  ,
  'DESCRIPTOR' : _EVALUATIONJOBCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.evaluation_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.EvaluationJobConfig)
  })
_sym_db.RegisterMessage(EvaluationJobConfig)
_sym_db.RegisterMessage(EvaluationJobConfig.BigqueryImportKeysEntry)

EvaluationJobAlertConfig = _reflection.GeneratedProtocolMessageType('EvaluationJobAlertConfig', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATIONJOBALERTCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.evaluation_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.EvaluationJobAlertConfig)
  })
_sym_db.RegisterMessage(EvaluationJobAlertConfig)

Attempt = _reflection.GeneratedProtocolMessageType('Attempt', (_message.Message,), {
  'DESCRIPTOR' : _ATTEMPT,
  '__module__' : 'google.cloud.datalabeling.v1beta1.evaluation_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.Attempt)
  })
_sym_db.RegisterMessage(Attempt)


DESCRIPTOR._options = None
_EVALUATIONJOB._options = None
_EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY._options = None
# @@protoc_insertion_point(module_scope)
