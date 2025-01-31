# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/storage/v1beta2/protobuf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/bigquery/storage/v1beta2/protobuf.proto',
  package='google.cloud.bigquery.storage.v1beta2',
  syntax='proto3',
  serialized_options=b'\n)com.google.cloud.bigquery.storage.v1beta2B\rProtoBufProtoP\001ZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta2;storage',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4google/cloud/bigquery/storage/v1beta2/protobuf.proto\x12%google.cloud.bigquery.storage.v1beta2\x1a google/protobuf/descriptor.proto\"Z\n\x0bProtoSchema\x12K\n\x10proto_descriptor\x18\x01 \x01(\x0b\x32 .google.protobuf.DescriptorProtoR\x0fprotoDescriptor\"4\n\tProtoRows\x12\'\n\x0fserialized_rows\x18\x01 \x03(\x0cR\x0eserializedRowsB\x8a\x01\n)com.google.cloud.bigquery.storage.v1beta2B\rProtoBufProtoP\x01ZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta2;storageb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])




_PROTOSCHEMA = _descriptor.Descriptor(
  name='ProtoSchema',
  full_name='google.cloud.bigquery.storage.v1beta2.ProtoSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proto_descriptor', full_name='google.cloud.bigquery.storage.v1beta2.ProtoSchema.proto_descriptor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='protoDescriptor', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=129,
  serialized_end=219,
)


_PROTOROWS = _descriptor.Descriptor(
  name='ProtoRows',
  full_name='google.cloud.bigquery.storage.v1beta2.ProtoRows',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_rows', full_name='google.cloud.bigquery.storage.v1beta2.ProtoRows.serialized_rows', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serializedRows', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=221,
  serialized_end=273,
)

_PROTOSCHEMA.fields_by_name['proto_descriptor'].message_type = google_dot_protobuf_dot_descriptor__pb2._DESCRIPTORPROTO
DESCRIPTOR.message_types_by_name['ProtoSchema'] = _PROTOSCHEMA
DESCRIPTOR.message_types_by_name['ProtoRows'] = _PROTOROWS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtoSchema = _reflection.GeneratedProtocolMessageType('ProtoSchema', (_message.Message,), {
  'DESCRIPTOR' : _PROTOSCHEMA,
  '__module__' : 'google.cloud.bigquery.storage.v1beta2.protobuf_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta2.ProtoSchema)
  })
_sym_db.RegisterMessage(ProtoSchema)

ProtoRows = _reflection.GeneratedProtocolMessageType('ProtoRows', (_message.Message,), {
  'DESCRIPTOR' : _PROTOROWS,
  '__module__' : 'google.cloud.bigquery.storage.v1beta2.protobuf_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta2.ProtoRows)
  })
_sym_db.RegisterMessage(ProtoRows)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
