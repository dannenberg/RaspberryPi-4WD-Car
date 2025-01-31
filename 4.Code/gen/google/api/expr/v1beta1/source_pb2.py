# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/expr/v1beta1/source.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/expr/v1beta1/source.proto',
  package='google.api.expr.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\033com.google.api.expr.v1beta1B\013SourceProtoP\001Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$google/api/expr/v1beta1/source.proto\x12\x17google.api.expr.v1beta1\"\xdb\x01\n\nSourceInfo\x12\x1a\n\x08location\x18\x02 \x01(\tR\x08location\x12!\n\x0cline_offsets\x18\x03 \x03(\x05R\x0blineOffsets\x12P\n\tpositions\x18\x04 \x03(\x0b\x32\x32.google.api.expr.v1beta1.SourceInfo.PositionsEntryR\tpositions\x1a<\n\x0ePositionsEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\"p\n\x0eSourcePosition\x12\x1a\n\x08location\x18\x01 \x01(\tR\x08location\x12\x16\n\x06offset\x18\x02 \x01(\x05R\x06offset\x12\x12\n\x04line\x18\x03 \x01(\x05R\x04line\x12\x16\n\x06\x63olumn\x18\x04 \x01(\x05R\x06\x63olumnBl\n\x1b\x63om.google.api.expr.v1beta1B\x0bSourceProtoP\x01Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\xf8\x01\x01\x62\x06proto3'
)




_SOURCEINFO_POSITIONSENTRY = _descriptor.Descriptor(
  name='PositionsEntry',
  full_name='google.api.expr.v1beta1.SourceInfo.PositionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.api.expr.v1beta1.SourceInfo.PositionsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.api.expr.v1beta1.SourceInfo.PositionsEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=225,
  serialized_end=285,
)

_SOURCEINFO = _descriptor.Descriptor(
  name='SourceInfo',
  full_name='google.api.expr.v1beta1.SourceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='google.api.expr.v1beta1.SourceInfo.location', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='location', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line_offsets', full_name='google.api.expr.v1beta1.SourceInfo.line_offsets', index=1,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='lineOffsets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='positions', full_name='google.api.expr.v1beta1.SourceInfo.positions', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='positions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SOURCEINFO_POSITIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=285,
)


_SOURCEPOSITION = _descriptor.Descriptor(
  name='SourcePosition',
  full_name='google.api.expr.v1beta1.SourcePosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='google.api.expr.v1beta1.SourcePosition.location', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='location', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='google.api.expr.v1beta1.SourcePosition.offset', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='offset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line', full_name='google.api.expr.v1beta1.SourcePosition.line', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='line', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column', full_name='google.api.expr.v1beta1.SourcePosition.column', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='column', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=287,
  serialized_end=399,
)

_SOURCEINFO_POSITIONSENTRY.containing_type = _SOURCEINFO
_SOURCEINFO.fields_by_name['positions'].message_type = _SOURCEINFO_POSITIONSENTRY
DESCRIPTOR.message_types_by_name['SourceInfo'] = _SOURCEINFO
DESCRIPTOR.message_types_by_name['SourcePosition'] = _SOURCEPOSITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SourceInfo = _reflection.GeneratedProtocolMessageType('SourceInfo', (_message.Message,), {

  'PositionsEntry' : _reflection.GeneratedProtocolMessageType('PositionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SOURCEINFO_POSITIONSENTRY,
    '__module__' : 'google.api.expr.v1beta1.source_pb2'
    # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.SourceInfo.PositionsEntry)
    })
  ,
  'DESCRIPTOR' : _SOURCEINFO,
  '__module__' : 'google.api.expr.v1beta1.source_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.SourceInfo)
  })
_sym_db.RegisterMessage(SourceInfo)
_sym_db.RegisterMessage(SourceInfo.PositionsEntry)

SourcePosition = _reflection.GeneratedProtocolMessageType('SourcePosition', (_message.Message,), {
  'DESCRIPTOR' : _SOURCEPOSITION,
  '__module__' : 'google.api.expr.v1beta1.source_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1beta1.SourcePosition)
  })
_sym_db.RegisterMessage(SourcePosition)


DESCRIPTOR._options = None
_SOURCEINFO_POSITIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
