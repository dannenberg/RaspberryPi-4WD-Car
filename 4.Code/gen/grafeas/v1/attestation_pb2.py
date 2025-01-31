# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grafeas/v1/attestation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from grafeas.v1 import common_pb2 as grafeas_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grafeas/v1/attestation.proto',
  package='grafeas.v1',
  syntax='proto3',
  serialized_options=b'\n\rio.grafeas.v1P\001Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\242\002\003GRA',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cgrafeas/v1/attestation.proto\x12\ngrafeas.v1\x1a\x17grafeas/v1/common.proto\"\x7f\n\x0f\x41ttestationNote\x12\x34\n\x04hint\x18\x01 \x01(\x0b\x32 .grafeas.v1.AttestationNote.HintR\x04hint\x1a\x36\n\x04Hint\x12.\n\x13human_readable_name\x18\x01 \x01(\tR\x11humanReadableName\"&\n\x03Jwt\x12\x1f\n\x0b\x63ompact_jwt\x18\x01 \x01(\tR\ncompactJwt\"\xa2\x01\n\x15\x41ttestationOccurrence\x12-\n\x12serialized_payload\x18\x01 \x01(\x0cR\x11serializedPayload\x12\x35\n\nsignatures\x18\x02 \x03(\x0b\x32\x15.grafeas.v1.SignatureR\nsignatures\x12#\n\x04jwts\x18\x03 \x03(\x0b\x32\x0f.grafeas.v1.JwtR\x04jwtsBQ\n\rio.grafeas.v1P\x01Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\xa2\x02\x03GRAb\x06proto3'
  ,
  dependencies=[grafeas_dot_v1_dot_common__pb2.DESCRIPTOR,])




_ATTESTATIONNOTE_HINT = _descriptor.Descriptor(
  name='Hint',
  full_name='grafeas.v1.AttestationNote.Hint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='human_readable_name', full_name='grafeas.v1.AttestationNote.Hint.human_readable_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='humanReadableName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=142,
  serialized_end=196,
)

_ATTESTATIONNOTE = _descriptor.Descriptor(
  name='AttestationNote',
  full_name='grafeas.v1.AttestationNote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hint', full_name='grafeas.v1.AttestationNote.hint', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hint', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ATTESTATIONNOTE_HINT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=196,
)


_JWT = _descriptor.Descriptor(
  name='Jwt',
  full_name='grafeas.v1.Jwt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='compact_jwt', full_name='grafeas.v1.Jwt.compact_jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='compactJwt', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=198,
  serialized_end=236,
)


_ATTESTATIONOCCURRENCE = _descriptor.Descriptor(
  name='AttestationOccurrence',
  full_name='grafeas.v1.AttestationOccurrence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_payload', full_name='grafeas.v1.AttestationOccurrence.serialized_payload', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serializedPayload', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='grafeas.v1.AttestationOccurrence.signatures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signatures', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jwts', full_name='grafeas.v1.AttestationOccurrence.jwts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='jwts', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=239,
  serialized_end=401,
)

_ATTESTATIONNOTE_HINT.containing_type = _ATTESTATIONNOTE
_ATTESTATIONNOTE.fields_by_name['hint'].message_type = _ATTESTATIONNOTE_HINT
_ATTESTATIONOCCURRENCE.fields_by_name['signatures'].message_type = grafeas_dot_v1_dot_common__pb2._SIGNATURE
_ATTESTATIONOCCURRENCE.fields_by_name['jwts'].message_type = _JWT
DESCRIPTOR.message_types_by_name['AttestationNote'] = _ATTESTATIONNOTE
DESCRIPTOR.message_types_by_name['Jwt'] = _JWT
DESCRIPTOR.message_types_by_name['AttestationOccurrence'] = _ATTESTATIONOCCURRENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AttestationNote = _reflection.GeneratedProtocolMessageType('AttestationNote', (_message.Message,), {

  'Hint' : _reflection.GeneratedProtocolMessageType('Hint', (_message.Message,), {
    'DESCRIPTOR' : _ATTESTATIONNOTE_HINT,
    '__module__' : 'grafeas.v1.attestation_pb2'
    # @@protoc_insertion_point(class_scope:grafeas.v1.AttestationNote.Hint)
    })
  ,
  'DESCRIPTOR' : _ATTESTATIONNOTE,
  '__module__' : 'grafeas.v1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1.AttestationNote)
  })
_sym_db.RegisterMessage(AttestationNote)
_sym_db.RegisterMessage(AttestationNote.Hint)

Jwt = _reflection.GeneratedProtocolMessageType('Jwt', (_message.Message,), {
  'DESCRIPTOR' : _JWT,
  '__module__' : 'grafeas.v1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1.Jwt)
  })
_sym_db.RegisterMessage(Jwt)

AttestationOccurrence = _reflection.GeneratedProtocolMessageType('AttestationOccurrence', (_message.Message,), {
  'DESCRIPTOR' : _ATTESTATIONOCCURRENCE,
  '__module__' : 'grafeas.v1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1.AttestationOccurrence)
  })
_sym_db.RegisterMessage(AttestationOccurrence)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
