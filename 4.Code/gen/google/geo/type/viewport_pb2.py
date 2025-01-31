# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/geo/type/viewport.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/geo/type/viewport.proto',
  package='google.geo.type',
  syntax='proto3',
  serialized_options=b'\n\023com.google.geo.typeB\rViewportProtoP\001Z@google.golang.org/genproto/googleapis/geo/type/viewport;viewport\242\002\004GGTP',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1egoogle/geo/type/viewport.proto\x12\x0fgoogle.geo.type\x1a\x18google/type/latlng.proto\"Z\n\x08Viewport\x12%\n\x03low\x18\x01 \x01(\x0b\x32\x13.google.type.LatLngR\x03low\x12\'\n\x04high\x18\x02 \x01(\x0b\x32\x13.google.type.LatLngR\x04highBo\n\x13\x63om.google.geo.typeB\rViewportProtoP\x01Z@google.golang.org/genproto/googleapis/geo/type/viewport;viewport\xa2\x02\x04GGTPb\x06proto3'
  ,
  dependencies=[google_dot_type_dot_latlng__pb2.DESCRIPTOR,])




_VIEWPORT = _descriptor.Descriptor(
  name='Viewport',
  full_name='google.geo.type.Viewport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='low', full_name='google.geo.type.Viewport.low', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='low', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high', full_name='google.geo.type.Viewport.high', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='high', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=77,
  serialized_end=167,
)

_VIEWPORT.fields_by_name['low'].message_type = google_dot_type_dot_latlng__pb2._LATLNG
_VIEWPORT.fields_by_name['high'].message_type = google_dot_type_dot_latlng__pb2._LATLNG
DESCRIPTOR.message_types_by_name['Viewport'] = _VIEWPORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Viewport = _reflection.GeneratedProtocolMessageType('Viewport', (_message.Message,), {
  'DESCRIPTOR' : _VIEWPORT,
  '__module__' : 'google.geo.type.viewport_pb2'
  # @@protoc_insertion_point(class_scope:google.geo.type.Viewport)
  })
_sym_db.RegisterMessage(Viewport)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
