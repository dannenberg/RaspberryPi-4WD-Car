# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/datastore/admin/v1/index.proto
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
  name='google/datastore/admin/v1/index.proto',
  package='google.datastore.admin.v1',
  syntax='proto3',
  serialized_options=b'\n\035com.google.datastore.admin.v1B\nIndexProtoP\001Z>google.golang.org/genproto/googleapis/datastore/admin/v1;admin\252\002\037Google.Cloud.Datastore.Admin.V1\312\002\037Google\\Cloud\\Datastore\\Admin\\V1\352\002#Google::Cloud::Datastore::Admin::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%google/datastore/admin/v1/index.proto\x12\x19google.datastore.admin.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/api/annotations.proto\"\xb6\x05\n\x05Index\x12#\n\nproject_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\tprojectId\x12\x1f\n\x08index_id\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03R\x07indexId\x12\x18\n\x04kind\x18\x04 \x01(\tB\x04\xe2\x41\x01\x02R\x04kind\x12O\n\x08\x61ncestor\x18\x05 \x01(\x0e\x32-.google.datastore.admin.v1.Index.AncestorModeB\x04\xe2\x41\x01\x02R\x08\x61ncestor\x12V\n\nproperties\x18\x06 \x03(\x0b\x32\x30.google.datastore.admin.v1.Index.IndexedPropertyB\x04\xe2\x41\x01\x02R\nproperties\x12\x42\n\x05state\x18\x07 \x01(\x0e\x32&.google.datastore.admin.v1.Index.StateB\x04\xe2\x41\x01\x03R\x05state\x1a{\n\x0fIndexedProperty\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12N\n\tdirection\x18\x02 \x01(\x0e\x32*.google.datastore.admin.v1.Index.DirectionB\x04\xe2\x41\x01\x02R\tdirection\"J\n\x0c\x41ncestorMode\x12\x1d\n\x19\x41NCESTOR_MODE_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x11\n\rALL_ANCESTORS\x10\x02\"E\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02\"P\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x42\xd7\x01\n\x1d\x63om.google.datastore.admin.v1B\nIndexProtoP\x01Z>google.golang.org/genproto/googleapis/datastore/admin/v1;admin\xaa\x02\x1fGoogle.Cloud.Datastore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Datastore\\Admin\\V1\xea\x02#Google::Cloud::Datastore::Admin::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_INDEX_ANCESTORMODE = _descriptor.EnumDescriptor(
  name='AncestorMode',
  full_name='google.datastore.admin.v1.Index.AncestorMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANCESTOR_MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALL_ANCESTORS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=599,
  serialized_end=673,
)
_sym_db.RegisterEnumDescriptor(_INDEX_ANCESTORMODE)

_INDEX_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='google.datastore.admin.v1.Index.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ASCENDING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DESCENDING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=675,
  serialized_end=744,
)
_sym_db.RegisterEnumDescriptor(_INDEX_DIRECTION)

_INDEX_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='google.datastore.admin.v1.Index.State',
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
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='READY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=746,
  serialized_end=826,
)
_sym_db.RegisterEnumDescriptor(_INDEX_STATE)


_INDEX_INDEXEDPROPERTY = _descriptor.Descriptor(
  name='IndexedProperty',
  full_name='google.datastore.admin.v1.Index.IndexedProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.datastore.admin.v1.Index.IndexedProperty.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='google.datastore.admin.v1.Index.IndexedProperty.direction', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='direction', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=474,
  serialized_end=597,
)

_INDEX = _descriptor.Descriptor(
  name='Index',
  full_name='google.datastore.admin.v1.Index',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.datastore.admin.v1.Index.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='projectId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index_id', full_name='google.datastore.admin.v1.Index.index_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='indexId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kind', full_name='google.datastore.admin.v1.Index.kind', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='kind', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ancestor', full_name='google.datastore.admin.v1.Index.ancestor', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='ancestor', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='google.datastore.admin.v1.Index.properties', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='properties', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='google.datastore.admin.v1.Index.state', index=5,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='state', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_INDEX_INDEXEDPROPERTY, ],
  enum_types=[
    _INDEX_ANCESTORMODE,
    _INDEX_DIRECTION,
    _INDEX_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=826,
)

_INDEX_INDEXEDPROPERTY.fields_by_name['direction'].enum_type = _INDEX_DIRECTION
_INDEX_INDEXEDPROPERTY.containing_type = _INDEX
_INDEX.fields_by_name['ancestor'].enum_type = _INDEX_ANCESTORMODE
_INDEX.fields_by_name['properties'].message_type = _INDEX_INDEXEDPROPERTY
_INDEX.fields_by_name['state'].enum_type = _INDEX_STATE
_INDEX_ANCESTORMODE.containing_type = _INDEX
_INDEX_DIRECTION.containing_type = _INDEX
_INDEX_STATE.containing_type = _INDEX
DESCRIPTOR.message_types_by_name['Index'] = _INDEX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Index = _reflection.GeneratedProtocolMessageType('Index', (_message.Message,), {

  'IndexedProperty' : _reflection.GeneratedProtocolMessageType('IndexedProperty', (_message.Message,), {
    'DESCRIPTOR' : _INDEX_INDEXEDPROPERTY,
    '__module__' : 'google.datastore.admin.v1.index_pb2'
    # @@protoc_insertion_point(class_scope:google.datastore.admin.v1.Index.IndexedProperty)
    })
  ,
  'DESCRIPTOR' : _INDEX,
  '__module__' : 'google.datastore.admin.v1.index_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.admin.v1.Index)
  })
_sym_db.RegisterMessage(Index)
_sym_db.RegisterMessage(Index.IndexedProperty)


DESCRIPTOR._options = None
_INDEX_INDEXEDPROPERTY.fields_by_name['name']._options = None
_INDEX_INDEXEDPROPERTY.fields_by_name['direction']._options = None
_INDEX.fields_by_name['project_id']._options = None
_INDEX.fields_by_name['index_id']._options = None
_INDEX.fields_by_name['kind']._options = None
_INDEX.fields_by_name['ancestor']._options = None
_INDEX.fields_by_name['properties']._options = None
_INDEX.fields_by_name['state']._options = None
# @@protoc_insertion_point(module_scope)
