# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grafeas/v1/image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grafeas/v1/image.proto',
  package='grafeas.v1',
  syntax='proto3',
  serialized_options=b'\n\rio.grafeas.v1P\001Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\242\002\003GRA',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16grafeas/v1/image.proto\x12\ngrafeas.v1\"C\n\x05Layer\x12\x1c\n\tdirective\x18\x01 \x01(\tR\tdirective\x12\x1c\n\targuments\x18\x02 \x01(\tR\targuments\"X\n\x0b\x46ingerprint\x12\x17\n\x07v1_name\x18\x01 \x01(\tR\x06v1Name\x12\x17\n\x07v2_blob\x18\x02 \x03(\tR\x06v2Blob\x12\x17\n\x07v2_name\x18\x03 \x01(\tR\x06v2Name\"i\n\tImageNote\x12!\n\x0cresource_url\x18\x01 \x01(\tR\x0bresourceUrl\x12\x39\n\x0b\x66ingerprint\x18\x02 \x01(\x0b\x32\x17.grafeas.v1.FingerprintR\x0b\x66ingerprint\"\xc6\x01\n\x0fImageOccurrence\x12\x39\n\x0b\x66ingerprint\x18\x01 \x01(\x0b\x32\x17.grafeas.v1.FingerprintR\x0b\x66ingerprint\x12\x1a\n\x08\x64istance\x18\x02 \x01(\x05R\x08\x64istance\x12\x30\n\nlayer_info\x18\x03 \x03(\x0b\x32\x11.grafeas.v1.LayerR\tlayerInfo\x12*\n\x11\x62\x61se_resource_url\x18\x04 \x01(\tR\x0f\x62\x61seResourceUrlBQ\n\rio.grafeas.v1P\x01Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\xa2\x02\x03GRAb\x06proto3'
)




_LAYER = _descriptor.Descriptor(
  name='Layer',
  full_name='grafeas.v1.Layer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='directive', full_name='grafeas.v1.Layer.directive', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='directive', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='grafeas.v1.Layer.arguments', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='arguments', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=38,
  serialized_end=105,
)


_FINGERPRINT = _descriptor.Descriptor(
  name='Fingerprint',
  full_name='grafeas.v1.Fingerprint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='v1_name', full_name='grafeas.v1.Fingerprint.v1_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='v1Name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v2_blob', full_name='grafeas.v1.Fingerprint.v2_blob', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='v2Blob', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v2_name', full_name='grafeas.v1.Fingerprint.v2_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='v2Name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=107,
  serialized_end=195,
)


_IMAGENOTE = _descriptor.Descriptor(
  name='ImageNote',
  full_name='grafeas.v1.ImageNote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_url', full_name='grafeas.v1.ImageNote.resource_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resourceUrl', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='grafeas.v1.ImageNote.fingerprint', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fingerprint', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=197,
  serialized_end=302,
)


_IMAGEOCCURRENCE = _descriptor.Descriptor(
  name='ImageOccurrence',
  full_name='grafeas.v1.ImageOccurrence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='grafeas.v1.ImageOccurrence.fingerprint', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fingerprint', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distance', full_name='grafeas.v1.ImageOccurrence.distance', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='distance', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='layer_info', full_name='grafeas.v1.ImageOccurrence.layer_info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='layerInfo', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_resource_url', full_name='grafeas.v1.ImageOccurrence.base_resource_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='baseResourceUrl', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=305,
  serialized_end=503,
)

_IMAGENOTE.fields_by_name['fingerprint'].message_type = _FINGERPRINT
_IMAGEOCCURRENCE.fields_by_name['fingerprint'].message_type = _FINGERPRINT
_IMAGEOCCURRENCE.fields_by_name['layer_info'].message_type = _LAYER
DESCRIPTOR.message_types_by_name['Layer'] = _LAYER
DESCRIPTOR.message_types_by_name['Fingerprint'] = _FINGERPRINT
DESCRIPTOR.message_types_by_name['ImageNote'] = _IMAGENOTE
DESCRIPTOR.message_types_by_name['ImageOccurrence'] = _IMAGEOCCURRENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Layer = _reflection.GeneratedProtocolMessageType('Layer', (_message.Message,), {
  'DESCRIPTOR' : _LAYER,
  '__module__' : 'grafeas.v1.image_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1.Layer)
  })
_sym_db.RegisterMessage(Layer)

Fingerprint = _reflection.GeneratedProtocolMessageType('Fingerprint', (_message.Message,), {
  'DESCRIPTOR' : _FINGERPRINT,
  '__module__' : 'grafeas.v1.image_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1.Fingerprint)
  })
_sym_db.RegisterMessage(Fingerprint)

ImageNote = _reflection.GeneratedProtocolMessageType('ImageNote', (_message.Message,), {
  'DESCRIPTOR' : _IMAGENOTE,
  '__module__' : 'grafeas.v1.image_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1.ImageNote)
  })
_sym_db.RegisterMessage(ImageNote)

ImageOccurrence = _reflection.GeneratedProtocolMessageType('ImageOccurrence', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEOCCURRENCE,
  '__module__' : 'grafeas.v1.image_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1.ImageOccurrence)
  })
_sym_db.RegisterMessage(ImageOccurrence)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
