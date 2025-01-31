# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/genomics/v1/readgroupset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.genomics.v1 import readgroup_pb2 as google_dot_genomics_dot_v1_dot_readgroup__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/genomics/v1/readgroupset.proto',
  package='google.genomics.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.google.genomics.v1B\021ReadGroupSetProtoP\001Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%google/genomics/v1/readgroupset.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\"google/genomics/v1/readgroup.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xec\x02\n\x0cReadGroupSet\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\ndataset_id\x18\x02 \x01(\tR\tdatasetId\x12(\n\x10reference_set_id\x18\x03 \x01(\tR\x0ereferenceSetId\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x1a\n\x08\x66ilename\x18\x05 \x01(\tR\x08\x66ilename\x12>\n\x0bread_groups\x18\x06 \x03(\x0b\x32\x1d.google.genomics.v1.ReadGroupR\nreadGroups\x12>\n\x04info\x18\x07 \x03(\x0b\x32*.google.genomics.v1.ReadGroupSet.InfoEntryR\x04info\x1aS\n\tInfoEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValueR\x05value:\x02\x38\x01\x42l\n\x16\x63om.google.genomics.v1B\x11ReadGroupSetProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_genomics_dot_v1_dot_readgroup__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_READGROUPSET_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='google.genomics.v1.ReadGroupSet.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.genomics.v1.ReadGroupSet.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.genomics.v1.ReadGroupSet.InfoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=439,
  serialized_end=522,
)

_READGROUPSET = _descriptor.Descriptor(
  name='ReadGroupSet',
  full_name='google.genomics.v1.ReadGroupSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.genomics.v1.ReadGroupSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='google.genomics.v1.ReadGroupSet.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='datasetId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='google.genomics.v1.ReadGroupSet.reference_set_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='referenceSetId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.genomics.v1.ReadGroupSet.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filename', full_name='google.genomics.v1.ReadGroupSet.filename', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='filename', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='read_groups', full_name='google.genomics.v1.ReadGroupSet.read_groups', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='readGroups', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='google.genomics.v1.ReadGroupSet.info', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='info', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_READGROUPSET_INFOENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=522,
)

_READGROUPSET_INFOENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_READGROUPSET_INFOENTRY.containing_type = _READGROUPSET
_READGROUPSET.fields_by_name['read_groups'].message_type = google_dot_genomics_dot_v1_dot_readgroup__pb2._READGROUP
_READGROUPSET.fields_by_name['info'].message_type = _READGROUPSET_INFOENTRY
DESCRIPTOR.message_types_by_name['ReadGroupSet'] = _READGROUPSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadGroupSet = _reflection.GeneratedProtocolMessageType('ReadGroupSet', (_message.Message,), {

  'InfoEntry' : _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), {
    'DESCRIPTOR' : _READGROUPSET_INFOENTRY,
    '__module__' : 'google.genomics.v1.readgroupset_pb2'
    # @@protoc_insertion_point(class_scope:google.genomics.v1.ReadGroupSet.InfoEntry)
    })
  ,
  'DESCRIPTOR' : _READGROUPSET,
  '__module__' : 'google.genomics.v1.readgroupset_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.ReadGroupSet)
  })
_sym_db.RegisterMessage(ReadGroupSet)
_sym_db.RegisterMessage(ReadGroupSet.InfoEntry)


DESCRIPTOR._options = None
_READGROUPSET_INFOENTRY._options = None
# @@protoc_insertion_point(module_scope)
