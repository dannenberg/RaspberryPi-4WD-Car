# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/schema/predict/instance/image_segmentation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/aiplatform/v1/schema/predict/instance/image_segmentation.proto',
  package='google.cloud.aiplatform.v1.schema.predict.instance',
  syntax='proto3',
  serialized_options=b'\n6com.google.cloud.aiplatform.v1.schema.predict.instanceB(ImageSegmentationPredictionInstanceProtoP\001ZZgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1/schema/predict/instance;instance\252\0022Google.Cloud.AIPlatform.V1.Schema.Predict.Instance\312\0022Google\\Cloud\\AIPlatform\\V1\\Schema\\Predict\\Instance\352\0028Google::Cloud::AIPlatform::V1::Schema::Predict::Instance',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nKgoogle/cloud/aiplatform/v1/schema/predict/instance/image_segmentation.proto\x12\x32google.cloud.aiplatform.v1.schema.predict.instance\x1a\x1cgoogle/api/annotations.proto\"\\\n#ImageSegmentationPredictionInstance\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeTypeB\xe5\x02\n6com.google.cloud.aiplatform.v1.schema.predict.instanceB(ImageSegmentationPredictionInstanceProtoP\x01ZZgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1/schema/predict/instance;instance\xaa\x02\x32Google.Cloud.AIPlatform.V1.Schema.Predict.Instance\xca\x02\x32Google\\Cloud\\AIPlatform\\V1\\Schema\\Predict\\Instance\xea\x02\x38Google::Cloud::AIPlatform::V1::Schema::Predict::Instanceb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_IMAGESEGMENTATIONPREDICTIONINSTANCE = _descriptor.Descriptor(
  name='ImageSegmentationPredictionInstance',
  full_name='google.cloud.aiplatform.v1.schema.predict.instance.ImageSegmentationPredictionInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='google.cloud.aiplatform.v1.schema.predict.instance.ImageSegmentationPredictionInstance.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='content', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='google.cloud.aiplatform.v1.schema.predict.instance.ImageSegmentationPredictionInstance.mime_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='mimeType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=161,
  serialized_end=253,
)

DESCRIPTOR.message_types_by_name['ImageSegmentationPredictionInstance'] = _IMAGESEGMENTATIONPREDICTIONINSTANCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageSegmentationPredictionInstance = _reflection.GeneratedProtocolMessageType('ImageSegmentationPredictionInstance', (_message.Message,), {
  'DESCRIPTOR' : _IMAGESEGMENTATIONPREDICTIONINSTANCE,
  '__module__' : 'google.cloud.aiplatform.v1.schema.predict.instance.image_segmentation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.schema.predict.instance.ImageSegmentationPredictionInstance)
  })
_sym_db.RegisterMessage(ImageSegmentationPredictionInstance)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
