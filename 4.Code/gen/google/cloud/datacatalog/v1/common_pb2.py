# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datacatalog/v1/common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/datacatalog/v1/common.proto',
  package='google.cloud.datacatalog.v1',
  syntax='proto3',
  serialized_options=b'\n\037com.google.cloud.datacatalog.v1P\001ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\370\001\001\252\002\033Google.Cloud.DataCatalog.V1\312\002\033Google\\Cloud\\DataCatalog\\V1\352\002\036Google::Cloud::DataCatalog::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(google/cloud/datacatalog/v1/common.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/protobuf/timestamp.proto*m\n\x10IntegratedSystem\x12!\n\x1dINTEGRATED_SYSTEM_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x42IGQUERY\x10\x01\x12\x10\n\x0c\x43LOUD_PUBSUB\x10\x02\x12\x16\n\x12\x44\x41TAPROC_METASTORE\x10\x03\x42\xcb\x01\n\x1f\x63om.google.cloud.datacatalog.v1P\x01ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\xf8\x01\x01\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_INTEGRATEDSYSTEM = _descriptor.EnumDescriptor(
  name='IntegratedSystem',
  full_name='google.cloud.datacatalog.v1.IntegratedSystem',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INTEGRATED_SYSTEM_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BIGQUERY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLOUD_PUBSUB', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DATAPROC_METASTORE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=106,
  serialized_end=215,
)
_sym_db.RegisterEnumDescriptor(_INTEGRATEDSYSTEM)

IntegratedSystem = enum_type_wrapper.EnumTypeWrapper(_INTEGRATEDSYSTEM)
INTEGRATED_SYSTEM_UNSPECIFIED = 0
BIGQUERY = 1
CLOUD_PUBSUB = 2
DATAPROC_METASTORE = 3


DESCRIPTOR.enum_types_by_name['IntegratedSystem'] = _INTEGRATEDSYSTEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
