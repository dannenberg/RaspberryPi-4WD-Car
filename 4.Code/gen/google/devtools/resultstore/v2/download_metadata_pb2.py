# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/resultstore/v2/download_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.devtools.resultstore.v2 import common_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/resultstore/v2/download_metadata.proto',
  package='google.devtools.resultstore.v2',
  syntax='proto3',
  serialized_options=b'\n\"com.google.devtools.resultstore.v2B\025DownloadMetadataProtoP\001ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6google/devtools/resultstore/v2/download_metadata.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x19google/api/resource.proto\x1a+google/devtools/resultstore/v2/common.proto\"\xd6\x01\n\x10\x44ownloadMetadata\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12Q\n\rupload_status\x18\x02 \x01(\x0e\x32,.google.devtools.resultstore.v2.UploadStatusR\x0cuploadStatus:[\xea\x41X\n+resultstore.googleapis.com/DownloadMetadata\x12)invocations/{invocation}/downloadMetadataB\x88\x01\n\"com.google.devtools.resultstore.v2B\x15\x44ownloadMetadataProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2.DESCRIPTOR,])




_DOWNLOADMETADATA = _descriptor.Descriptor(
  name='DownloadMetadata',
  full_name='google.devtools.resultstore.v2.DownloadMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.resultstore.v2.DownloadMetadata.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upload_status', full_name='google.devtools.resultstore.v2.DownloadMetadata.upload_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='uploadStatus', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352AX\n+resultstore.googleapis.com/DownloadMetadata\022)invocations/{invocation}/downloadMetadata',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=377,
)

_DOWNLOADMETADATA.fields_by_name['upload_status'].enum_type = google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2._UPLOADSTATUS
DESCRIPTOR.message_types_by_name['DownloadMetadata'] = _DOWNLOADMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DownloadMetadata = _reflection.GeneratedProtocolMessageType('DownloadMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADMETADATA,
  '__module__' : 'google.devtools.resultstore.v2.download_metadata_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.DownloadMetadata)
  })
_sym_db.RegisterMessage(DownloadMetadata)


DESCRIPTOR._options = None
_DOWNLOADMETADATA._options = None
# @@protoc_insertion_point(module_scope)
