# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl/v1/image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.automl.v1 import annotation_spec_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_annotation__spec__pb2
from google.cloud.automl.v1 import classification_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_classification__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/automl/v1/image.proto',
  package='google.cloud.automl.v1',
  syntax='proto3',
  serialized_options=b'\n\032com.google.cloud.automl.v1B\nImageProtoP\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoMl\\V1\352\002\031Google::Cloud::AutoML::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"google/cloud/automl/v1/image.proto\x12\x16google.cloud.automl.v1\x1a\x19google/api/resource.proto\x1a,google/cloud/automl/v1/annotation_spec.proto\x1a+google/cloud/automl/v1/classification.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x81\x01\n\"ImageClassificationDatasetMetadata\x12[\n\x13\x63lassification_type\x18\x01 \x01(\x0e\x32*.google.cloud.automl.v1.ClassificationTypeR\x12\x63lassificationType\"%\n#ImageObjectDetectionDatasetMetadata\"\xc0\x02\n ImageClassificationModelMetadata\x12\"\n\rbase_model_id\x18\x01 \x01(\tR\x0b\x62\x61seModelId\x12@\n\x1dtrain_budget_milli_node_hours\x18\x10 \x01(\x03R\x19trainBudgetMilliNodeHours\x12<\n\x1btrain_cost_milli_node_hours\x18\x11 \x01(\x03R\x17trainCostMilliNodeHours\x12\x1f\n\x0bstop_reason\x18\x05 \x01(\tR\nstopReason\x12\x1d\n\nmodel_type\x18\x07 \x01(\tR\tmodelType\x12\x19\n\x08node_qps\x18\r \x01(\x01R\x07nodeQps\x12\x1d\n\nnode_count\x18\x0e \x01(\x03R\tnodeCount\"\x9d\x02\n!ImageObjectDetectionModelMetadata\x12\x1d\n\nmodel_type\x18\x01 \x01(\tR\tmodelType\x12\x1d\n\nnode_count\x18\x03 \x01(\x03R\tnodeCount\x12\x19\n\x08node_qps\x18\x04 \x01(\x01R\x07nodeQps\x12\x1f\n\x0bstop_reason\x18\x05 \x01(\tR\nstopReason\x12@\n\x1dtrain_budget_milli_node_hours\x18\x06 \x01(\x03R\x19trainBudgetMilliNodeHours\x12<\n\x1btrain_cost_milli_node_hours\x18\x07 \x01(\x03R\x17trainCostMilliNodeHours\"K\n*ImageClassificationModelDeploymentMetadata\x12\x1d\n\nnode_count\x18\x01 \x01(\x03R\tnodeCount\"L\n+ImageObjectDetectionModelDeploymentMetadata\x12\x1d\n\nnode_count\x18\x01 \x01(\x03R\tnodeCountB\xb6\x01\n\x1a\x63om.google.cloud.automl.v1B\nImageProtoP\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_automl_dot_v1_dot_annotation__spec__pb2.DESCRIPTOR,google_dot_cloud_dot_automl_dot_v1_dot_classification__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_IMAGECLASSIFICATIONDATASETMETADATA = _descriptor.Descriptor(
  name='ImageClassificationDatasetMetadata',
  full_name='google.cloud.automl.v1.ImageClassificationDatasetMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='classification_type', full_name='google.cloud.automl.v1.ImageClassificationDatasetMetadata.classification_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='classificationType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=244,
  serialized_end=373,
)


_IMAGEOBJECTDETECTIONDATASETMETADATA = _descriptor.Descriptor(
  name='ImageObjectDetectionDatasetMetadata',
  full_name='google.cloud.automl.v1.ImageObjectDetectionDatasetMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=375,
  serialized_end=412,
)


_IMAGECLASSIFICATIONMODELMETADATA = _descriptor.Descriptor(
  name='ImageClassificationModelMetadata',
  full_name='google.cloud.automl.v1.ImageClassificationModelMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_model_id', full_name='google.cloud.automl.v1.ImageClassificationModelMetadata.base_model_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='baseModelId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='train_budget_milli_node_hours', full_name='google.cloud.automl.v1.ImageClassificationModelMetadata.train_budget_milli_node_hours', index=1,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='trainBudgetMilliNodeHours', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='train_cost_milli_node_hours', full_name='google.cloud.automl.v1.ImageClassificationModelMetadata.train_cost_milli_node_hours', index=2,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='trainCostMilliNodeHours', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stop_reason', full_name='google.cloud.automl.v1.ImageClassificationModelMetadata.stop_reason', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stopReason', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_type', full_name='google.cloud.automl.v1.ImageClassificationModelMetadata.model_type', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='modelType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_qps', full_name='google.cloud.automl.v1.ImageClassificationModelMetadata.node_qps', index=5,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nodeQps', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_count', full_name='google.cloud.automl.v1.ImageClassificationModelMetadata.node_count', index=6,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nodeCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=415,
  serialized_end=735,
)


_IMAGEOBJECTDETECTIONMODELMETADATA = _descriptor.Descriptor(
  name='ImageObjectDetectionModelMetadata',
  full_name='google.cloud.automl.v1.ImageObjectDetectionModelMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_type', full_name='google.cloud.automl.v1.ImageObjectDetectionModelMetadata.model_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='modelType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_count', full_name='google.cloud.automl.v1.ImageObjectDetectionModelMetadata.node_count', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nodeCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_qps', full_name='google.cloud.automl.v1.ImageObjectDetectionModelMetadata.node_qps', index=2,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nodeQps', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stop_reason', full_name='google.cloud.automl.v1.ImageObjectDetectionModelMetadata.stop_reason', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stopReason', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='train_budget_milli_node_hours', full_name='google.cloud.automl.v1.ImageObjectDetectionModelMetadata.train_budget_milli_node_hours', index=4,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='trainBudgetMilliNodeHours', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='train_cost_milli_node_hours', full_name='google.cloud.automl.v1.ImageObjectDetectionModelMetadata.train_cost_milli_node_hours', index=5,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='trainCostMilliNodeHours', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=738,
  serialized_end=1023,
)


_IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA = _descriptor.Descriptor(
  name='ImageClassificationModelDeploymentMetadata',
  full_name='google.cloud.automl.v1.ImageClassificationModelDeploymentMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_count', full_name='google.cloud.automl.v1.ImageClassificationModelDeploymentMetadata.node_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nodeCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1025,
  serialized_end=1100,
)


_IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA = _descriptor.Descriptor(
  name='ImageObjectDetectionModelDeploymentMetadata',
  full_name='google.cloud.automl.v1.ImageObjectDetectionModelDeploymentMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_count', full_name='google.cloud.automl.v1.ImageObjectDetectionModelDeploymentMetadata.node_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nodeCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1102,
  serialized_end=1178,
)

_IMAGECLASSIFICATIONDATASETMETADATA.fields_by_name['classification_type'].enum_type = google_dot_cloud_dot_automl_dot_v1_dot_classification__pb2._CLASSIFICATIONTYPE
DESCRIPTOR.message_types_by_name['ImageClassificationDatasetMetadata'] = _IMAGECLASSIFICATIONDATASETMETADATA
DESCRIPTOR.message_types_by_name['ImageObjectDetectionDatasetMetadata'] = _IMAGEOBJECTDETECTIONDATASETMETADATA
DESCRIPTOR.message_types_by_name['ImageClassificationModelMetadata'] = _IMAGECLASSIFICATIONMODELMETADATA
DESCRIPTOR.message_types_by_name['ImageObjectDetectionModelMetadata'] = _IMAGEOBJECTDETECTIONMODELMETADATA
DESCRIPTOR.message_types_by_name['ImageClassificationModelDeploymentMetadata'] = _IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA
DESCRIPTOR.message_types_by_name['ImageObjectDetectionModelDeploymentMetadata'] = _IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageClassificationDatasetMetadata = _reflection.GeneratedProtocolMessageType('ImageClassificationDatasetMetadata', (_message.Message,), {
  'DESCRIPTOR' : _IMAGECLASSIFICATIONDATASETMETADATA,
  '__module__' : 'google.cloud.automl.v1.image_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageClassificationDatasetMetadata)
  })
_sym_db.RegisterMessage(ImageClassificationDatasetMetadata)

ImageObjectDetectionDatasetMetadata = _reflection.GeneratedProtocolMessageType('ImageObjectDetectionDatasetMetadata', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEOBJECTDETECTIONDATASETMETADATA,
  '__module__' : 'google.cloud.automl.v1.image_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageObjectDetectionDatasetMetadata)
  })
_sym_db.RegisterMessage(ImageObjectDetectionDatasetMetadata)

ImageClassificationModelMetadata = _reflection.GeneratedProtocolMessageType('ImageClassificationModelMetadata', (_message.Message,), {
  'DESCRIPTOR' : _IMAGECLASSIFICATIONMODELMETADATA,
  '__module__' : 'google.cloud.automl.v1.image_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageClassificationModelMetadata)
  })
_sym_db.RegisterMessage(ImageClassificationModelMetadata)

ImageObjectDetectionModelMetadata = _reflection.GeneratedProtocolMessageType('ImageObjectDetectionModelMetadata', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEOBJECTDETECTIONMODELMETADATA,
  '__module__' : 'google.cloud.automl.v1.image_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageObjectDetectionModelMetadata)
  })
_sym_db.RegisterMessage(ImageObjectDetectionModelMetadata)

ImageClassificationModelDeploymentMetadata = _reflection.GeneratedProtocolMessageType('ImageClassificationModelDeploymentMetadata', (_message.Message,), {
  'DESCRIPTOR' : _IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA,
  '__module__' : 'google.cloud.automl.v1.image_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageClassificationModelDeploymentMetadata)
  })
_sym_db.RegisterMessage(ImageClassificationModelDeploymentMetadata)

ImageObjectDetectionModelDeploymentMetadata = _reflection.GeneratedProtocolMessageType('ImageObjectDetectionModelDeploymentMetadata', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA,
  '__module__' : 'google.cloud.automl.v1.image_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageObjectDetectionModelDeploymentMetadata)
  })
_sym_db.RegisterMessage(ImageObjectDetectionModelDeploymentMetadata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
