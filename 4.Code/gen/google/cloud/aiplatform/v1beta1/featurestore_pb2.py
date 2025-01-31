# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/featurestore.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/aiplatform/v1beta1/featurestore.proto',
  package='google.cloud.aiplatform.v1beta1',
  syntax='proto3',
  serialized_options=b'\n#com.google.cloud.aiplatform.v1beta1B\021FeaturestoreProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\252\002\037Google.Cloud.AIPlatform.V1Beta1\312\002\037Google\\Cloud\\AIPlatform\\V1beta1\352\002\"Google::Cloud::AIPlatform::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2google/cloud/aiplatform/v1beta1/featurestore.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x35google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xf8\x06\n\x0c\x46\x65\x61turestore\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\x41\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12\x18\n\x04\x65tag\x18\x05 \x01(\tB\x04\xe2\x41\x01\x01R\x04\x65tag\x12W\n\x06labels\x18\x06 \x03(\x0b\x32\x39.google.cloud.aiplatform.v1beta1.Featurestore.LabelsEntryB\x04\xe2\x41\x01\x01R\x06labels\x12{\n\x15online_serving_config\x18\x07 \x01(\x0b\x32\x41.google.cloud.aiplatform.v1beta1.Featurestore.OnlineServingConfigB\x04\xe2\x41\x01\x02R\x13onlineServingConfig\x12O\n\x05state\x18\x08 \x01(\x0e\x32\x33.google.cloud.aiplatform.v1beta1.Featurestore.StateB\x04\xe2\x41\x01\x03R\x05state\x12^\n\x0f\x65ncryption_spec\x18\n \x01(\x0b\x32/.google.cloud.aiplatform.v1beta1.EncryptionSpecB\x04\xe2\x41\x01\x01R\x0e\x65ncryptionSpec\x1a?\n\x13OnlineServingConfig\x12(\n\x10\x66ixed_node_count\x18\x02 \x01(\x05R\x0e\x66ixedNodeCount\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"8\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06STABLE\x10\x01\x12\x0c\n\x08UPDATING\x10\x02:q\xea\x41n\n&aiplatform.googleapis.com/Featurestore\x12\x44projects/{project}/locations/{location}/featurestores/{featurestore}B\xee\x01\n#com.google.cloud.aiplatform.v1beta1B\x11\x46\x65\x61turestoreProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02\"Google::Cloud::AIPlatform::V1beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FEATURESTORE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='google.cloud.aiplatform.v1beta1.Featurestore.State',
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
      name='STABLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=983,
  serialized_end=1039,
)
_sym_db.RegisterEnumDescriptor(_FEATURESTORE_STATE)


_FEATURESTORE_ONLINESERVINGCONFIG = _descriptor.Descriptor(
  name='OnlineServingConfig',
  full_name='google.cloud.aiplatform.v1beta1.Featurestore.OnlineServingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fixed_node_count', full_name='google.cloud.aiplatform.v1beta1.Featurestore.OnlineServingConfig.fixed_node_count', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fixedNodeCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=859,
  serialized_end=922,
)

_FEATURESTORE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.cloud.aiplatform.v1beta1.Featurestore.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.aiplatform.v1beta1.Featurestore.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.aiplatform.v1beta1.Featurestore.LabelsEntry.value', index=1,
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
  serialized_start=924,
  serialized_end=981,
)

_FEATURESTORE = _descriptor.Descriptor(
  name='Featurestore',
  full_name='google.cloud.aiplatform.v1beta1.Featurestore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.aiplatform.v1beta1.Featurestore.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.aiplatform.v1beta1.Featurestore.create_time', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='createTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.cloud.aiplatform.v1beta1.Featurestore.update_time', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='updateTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='etag', full_name='google.cloud.aiplatform.v1beta1.Featurestore.etag', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='etag', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.cloud.aiplatform.v1beta1.Featurestore.labels', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='online_serving_config', full_name='google.cloud.aiplatform.v1beta1.Featurestore.online_serving_config', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='onlineServingConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='google.cloud.aiplatform.v1beta1.Featurestore.state', index=6,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='state', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encryption_spec', full_name='google.cloud.aiplatform.v1beta1.Featurestore.encryption_spec', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='encryptionSpec', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FEATURESTORE_ONLINESERVINGCONFIG, _FEATURESTORE_LABELSENTRY, ],
  enum_types=[
    _FEATURESTORE_STATE,
  ],
  serialized_options=b'\352An\n&aiplatform.googleapis.com/Featurestore\022Dprojects/{project}/locations/{location}/featurestores/{featurestore}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=1154,
)

_FEATURESTORE_ONLINESERVINGCONFIG.containing_type = _FEATURESTORE
_FEATURESTORE_LABELSENTRY.containing_type = _FEATURESTORE
_FEATURESTORE.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FEATURESTORE.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FEATURESTORE.fields_by_name['labels'].message_type = _FEATURESTORE_LABELSENTRY
_FEATURESTORE.fields_by_name['online_serving_config'].message_type = _FEATURESTORE_ONLINESERVINGCONFIG
_FEATURESTORE.fields_by_name['state'].enum_type = _FEATURESTORE_STATE
_FEATURESTORE.fields_by_name['encryption_spec'].message_type = google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2._ENCRYPTIONSPEC
_FEATURESTORE_STATE.containing_type = _FEATURESTORE
DESCRIPTOR.message_types_by_name['Featurestore'] = _FEATURESTORE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Featurestore = _reflection.GeneratedProtocolMessageType('Featurestore', (_message.Message,), {

  'OnlineServingConfig' : _reflection.GeneratedProtocolMessageType('OnlineServingConfig', (_message.Message,), {
    'DESCRIPTOR' : _FEATURESTORE_ONLINESERVINGCONFIG,
    '__module__' : 'google.cloud.aiplatform.v1beta1.featurestore_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.Featurestore.OnlineServingConfig)
    })
  ,

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEATURESTORE_LABELSENTRY,
    '__module__' : 'google.cloud.aiplatform.v1beta1.featurestore_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.Featurestore.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _FEATURESTORE,
  '__module__' : 'google.cloud.aiplatform.v1beta1.featurestore_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.Featurestore)
  })
_sym_db.RegisterMessage(Featurestore)
_sym_db.RegisterMessage(Featurestore.OnlineServingConfig)
_sym_db.RegisterMessage(Featurestore.LabelsEntry)


DESCRIPTOR._options = None
_FEATURESTORE_LABELSENTRY._options = None
_FEATURESTORE.fields_by_name['name']._options = None
_FEATURESTORE.fields_by_name['create_time']._options = None
_FEATURESTORE.fields_by_name['update_time']._options = None
_FEATURESTORE.fields_by_name['etag']._options = None
_FEATURESTORE.fields_by_name['labels']._options = None
_FEATURESTORE.fields_by_name['online_serving_config']._options = None
_FEATURESTORE.fields_by_name['state']._options = None
_FEATURESTORE.fields_by_name['encryption_spec']._options = None
_FEATURESTORE._options = None
# @@protoc_insertion_point(module_scope)
