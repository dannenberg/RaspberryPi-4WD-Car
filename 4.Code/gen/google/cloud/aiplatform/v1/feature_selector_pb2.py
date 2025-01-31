# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/feature_selector.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/aiplatform/v1/feature_selector.proto',
  package='google.cloud.aiplatform.v1',
  syntax='proto3',
  serialized_options=b'\n\036com.google.cloud.aiplatform.v1B\024FeatureSelectorProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\252\002\032Google.Cloud.AIPlatform.V1\312\002\032Google\\Cloud\\AIPlatform\\V1\352\002\035Google::Cloud::AIPlatform::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1google/cloud/aiplatform/v1/feature_selector.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/api/annotations.proto\"#\n\tIdMatcher\x12\x16\n\x03ids\x18\x01 \x03(\tB\x04\xe2\x41\x01\x02R\x03ids\"]\n\x0f\x46\x65\x61tureSelector\x12J\n\nid_matcher\x18\x01 \x01(\x0b\x32%.google.cloud.aiplatform.v1.IdMatcherB\x04\xe2\x41\x01\x02R\tidMatcherB\xd8\x01\n\x1e\x63om.google.cloud.aiplatform.v1B\x14\x46\x65\x61tureSelectorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_IDMATCHER = _descriptor.Descriptor(
  name='IdMatcher',
  full_name='google.cloud.aiplatform.v1.IdMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='google.cloud.aiplatform.v1.IdMatcher.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='ids', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=144,
  serialized_end=179,
)


_FEATURESELECTOR = _descriptor.Descriptor(
  name='FeatureSelector',
  full_name='google.cloud.aiplatform.v1.FeatureSelector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_matcher', full_name='google.cloud.aiplatform.v1.FeatureSelector.id_matcher', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='idMatcher', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=181,
  serialized_end=274,
)

_FEATURESELECTOR.fields_by_name['id_matcher'].message_type = _IDMATCHER
DESCRIPTOR.message_types_by_name['IdMatcher'] = _IDMATCHER
DESCRIPTOR.message_types_by_name['FeatureSelector'] = _FEATURESELECTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IdMatcher = _reflection.GeneratedProtocolMessageType('IdMatcher', (_message.Message,), {
  'DESCRIPTOR' : _IDMATCHER,
  '__module__' : 'google.cloud.aiplatform.v1.feature_selector_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.IdMatcher)
  })
_sym_db.RegisterMessage(IdMatcher)

FeatureSelector = _reflection.GeneratedProtocolMessageType('FeatureSelector', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESELECTOR,
  '__module__' : 'google.cloud.aiplatform.v1.feature_selector_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.FeatureSelector)
  })
_sym_db.RegisterMessage(FeatureSelector)


DESCRIPTOR._options = None
_IDMATCHER.fields_by_name['ids']._options = None
_FEATURESELECTOR.fields_by_name['id_matcher']._options = None
# @@protoc_insertion_point(module_scope)
