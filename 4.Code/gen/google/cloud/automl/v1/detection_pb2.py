# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl/v1/detection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl.v1 import geometry_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_geometry__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/automl/v1/detection.proto',
  package='google.cloud.automl.v1',
  syntax='proto3',
  serialized_options=b'\n\032com.google.cloud.automl.v1P\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoMl\\V1\352\002\031Google::Cloud::AutoML::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&google/cloud/automl/v1/detection.proto\x12\x16google.cloud.automl.v1\x1a%google/cloud/automl/v1/geometry.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/api/annotations.proto\"\x7f\n\x1eImageObjectDetectionAnnotation\x12G\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32$.google.cloud.automl.v1.BoundingPolyR\x0b\x62oundingBox\x12\x14\n\x05score\x18\x02 \x01(\x02R\x05score\"\x9a\x03\n\x17\x42oundingBoxMetricsEntry\x12#\n\riou_threshold\x18\x01 \x01(\x02R\x0ciouThreshold\x12\x34\n\x16mean_average_precision\x18\x02 \x01(\x02R\x14meanAveragePrecision\x12\x84\x01\n\x1a\x63onfidence_metrics_entries\x18\x03 \x03(\x0b\x32\x46.google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntryR\x18\x63onfidenceMetricsEntries\x1a\x9c\x01\n\x16\x43onfidenceMetricsEntry\x12\x31\n\x14\x63onfidence_threshold\x18\x01 \x01(\x02R\x13\x63onfidenceThreshold\x12\x16\n\x06recall\x18\x02 \x01(\x02R\x06recall\x12\x1c\n\tprecision\x18\x03 \x01(\x02R\tprecision\x12\x19\n\x08\x66\x31_score\x18\x04 \x01(\x02R\x07\x66\x31Score\"\xa8\x02\n%ImageObjectDetectionEvaluationMetrics\x12?\n\x1c\x65valuated_bounding_box_count\x18\x01 \x01(\x05R\x19\x65valuatedBoundingBoxCount\x12p\n\x1c\x62ounding_box_metrics_entries\x18\x02 \x03(\x0b\x32/.google.cloud.automl.v1.BoundingBoxMetricsEntryR\x19\x62oundingBoxMetricsEntries\x12L\n#bounding_box_mean_average_precision\x18\x03 \x01(\x02R\x1f\x62oundingBoxMeanAveragePrecisionB\xaa\x01\n\x1a\x63om.google.cloud.automl.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3'
  ,
  dependencies=[google_dot_cloud_dot_automl_dot_v1_dot_geometry__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_IMAGEOBJECTDETECTIONANNOTATION = _descriptor.Descriptor(
  name='ImageObjectDetectionAnnotation',
  full_name='google.cloud.automl.v1.ImageObjectDetectionAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bounding_box', full_name='google.cloud.automl.v1.ImageObjectDetectionAnnotation.bounding_box', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='boundingBox', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='google.cloud.automl.v1.ImageObjectDetectionAnnotation.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='score', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=167,
  serialized_end=294,
)


_BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY = _descriptor.Descriptor(
  name='ConfidenceMetricsEntry',
  full_name='google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='confidence_threshold', full_name='google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry.confidence_threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='confidenceThreshold', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recall', full_name='google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry.recall', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='recall', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='precision', full_name='google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry.precision', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='precision', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f1_score', full_name='google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry.f1_score', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='f1Score', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=551,
  serialized_end=707,
)

_BOUNDINGBOXMETRICSENTRY = _descriptor.Descriptor(
  name='BoundingBoxMetricsEntry',
  full_name='google.cloud.automl.v1.BoundingBoxMetricsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='iou_threshold', full_name='google.cloud.automl.v1.BoundingBoxMetricsEntry.iou_threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='iouThreshold', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mean_average_precision', full_name='google.cloud.automl.v1.BoundingBoxMetricsEntry.mean_average_precision', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='meanAveragePrecision', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence_metrics_entries', full_name='google.cloud.automl.v1.BoundingBoxMetricsEntry.confidence_metrics_entries', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='confidenceMetricsEntries', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=707,
)


_IMAGEOBJECTDETECTIONEVALUATIONMETRICS = _descriptor.Descriptor(
  name='ImageObjectDetectionEvaluationMetrics',
  full_name='google.cloud.automl.v1.ImageObjectDetectionEvaluationMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='evaluated_bounding_box_count', full_name='google.cloud.automl.v1.ImageObjectDetectionEvaluationMetrics.evaluated_bounding_box_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='evaluatedBoundingBoxCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bounding_box_metrics_entries', full_name='google.cloud.automl.v1.ImageObjectDetectionEvaluationMetrics.bounding_box_metrics_entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='boundingBoxMetricsEntries', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bounding_box_mean_average_precision', full_name='google.cloud.automl.v1.ImageObjectDetectionEvaluationMetrics.bounding_box_mean_average_precision', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='boundingBoxMeanAveragePrecision', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=710,
  serialized_end=1006,
)

_IMAGEOBJECTDETECTIONANNOTATION.fields_by_name['bounding_box'].message_type = google_dot_cloud_dot_automl_dot_v1_dot_geometry__pb2._BOUNDINGPOLY
_BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY.containing_type = _BOUNDINGBOXMETRICSENTRY
_BOUNDINGBOXMETRICSENTRY.fields_by_name['confidence_metrics_entries'].message_type = _BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY
_IMAGEOBJECTDETECTIONEVALUATIONMETRICS.fields_by_name['bounding_box_metrics_entries'].message_type = _BOUNDINGBOXMETRICSENTRY
DESCRIPTOR.message_types_by_name['ImageObjectDetectionAnnotation'] = _IMAGEOBJECTDETECTIONANNOTATION
DESCRIPTOR.message_types_by_name['BoundingBoxMetricsEntry'] = _BOUNDINGBOXMETRICSENTRY
DESCRIPTOR.message_types_by_name['ImageObjectDetectionEvaluationMetrics'] = _IMAGEOBJECTDETECTIONEVALUATIONMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageObjectDetectionAnnotation = _reflection.GeneratedProtocolMessageType('ImageObjectDetectionAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEOBJECTDETECTIONANNOTATION,
  '__module__' : 'google.cloud.automl.v1.detection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageObjectDetectionAnnotation)
  })
_sym_db.RegisterMessage(ImageObjectDetectionAnnotation)

BoundingBoxMetricsEntry = _reflection.GeneratedProtocolMessageType('BoundingBoxMetricsEntry', (_message.Message,), {

  'ConfidenceMetricsEntry' : _reflection.GeneratedProtocolMessageType('ConfidenceMetricsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY,
    '__module__' : 'google.cloud.automl.v1.detection_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry)
    })
  ,
  'DESCRIPTOR' : _BOUNDINGBOXMETRICSENTRY,
  '__module__' : 'google.cloud.automl.v1.detection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BoundingBoxMetricsEntry)
  })
_sym_db.RegisterMessage(BoundingBoxMetricsEntry)
_sym_db.RegisterMessage(BoundingBoxMetricsEntry.ConfidenceMetricsEntry)

ImageObjectDetectionEvaluationMetrics = _reflection.GeneratedProtocolMessageType('ImageObjectDetectionEvaluationMetrics', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEOBJECTDETECTIONEVALUATIONMETRICS,
  '__module__' : 'google.cloud.automl.v1.detection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageObjectDetectionEvaluationMetrics)
  })
_sym_db.RegisterMessage(ImageObjectDetectionEvaluationMetrics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
