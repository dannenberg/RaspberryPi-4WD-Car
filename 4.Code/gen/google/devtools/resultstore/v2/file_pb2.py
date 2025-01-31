# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/resultstore/v2/file.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/resultstore/v2/file.proto',
  package='google.devtools.resultstore.v2',
  syntax='proto3',
  serialized_options=b'\n\"com.google.devtools.resultstore.v2B\tFileProtoP\001ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)google/devtools/resultstore/v2/file.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x1egoogle/protobuf/wrappers.proto\"\xe0\x03\n\x04\x46ile\x12\x10\n\x03uid\x18\x01 \x01(\tR\x03uid\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri\x12\x33\n\x06length\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x06length\x12!\n\x0c\x63ontent_type\x18\x04 \x01(\tR\x0b\x63ontentType\x12Q\n\rarchive_entry\x18\x05 \x01(\x0b\x32,.google.devtools.resultstore.v2.ArchiveEntryR\x0c\x61rchiveEntry\x12%\n\x0e\x63ontent_viewer\x18\x06 \x01(\tR\rcontentViewer\x12\x16\n\x06hidden\x18\x07 \x01(\x08R\x06hidden\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\x12\x16\n\x06\x64igest\x18\t \x01(\tR\x06\x64igest\x12J\n\thash_type\x18\n \x01(\x0e\x32-.google.devtools.resultstore.v2.File.HashTypeR\x08hashType\"D\n\x08HashType\x12\x19\n\x15HASH_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03MD5\x10\x01\x12\x08\n\x04SHA1\x10\x02\x12\n\n\x06SHA256\x10\x03\"z\n\x0c\x41rchiveEntry\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12\x33\n\x06length\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x06length\x12!\n\x0c\x63ontent_type\x18\x03 \x01(\tR\x0b\x63ontentTypeB|\n\"com.google.devtools.resultstore.v2B\tFileProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])



_FILE_HASHTYPE = _descriptor.EnumDescriptor(
  name='HashType',
  full_name='google.devtools.resultstore.v2.File.HashType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HASH_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MD5', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHA1', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHA256', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=522,
  serialized_end=590,
)
_sym_db.RegisterEnumDescriptor(_FILE_HASHTYPE)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='google.devtools.resultstore.v2.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='google.devtools.resultstore.v2.File.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='uid', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uri', full_name='google.devtools.resultstore.v2.File.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='uri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='google.devtools.resultstore.v2.File.length', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='length', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='google.devtools.resultstore.v2.File.content_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='archive_entry', full_name='google.devtools.resultstore.v2.File.archive_entry', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='archiveEntry', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content_viewer', full_name='google.devtools.resultstore.v2.File.content_viewer', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentViewer', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='google.devtools.resultstore.v2.File.hidden', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hidden', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.devtools.resultstore.v2.File.description', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='digest', full_name='google.devtools.resultstore.v2.File.digest', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='digest', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash_type', full_name='google.devtools.resultstore.v2.File.hash_type', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hashType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FILE_HASHTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=590,
)


_ARCHIVEENTRY = _descriptor.Descriptor(
  name='ArchiveEntry',
  full_name='google.devtools.resultstore.v2.ArchiveEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='google.devtools.resultstore.v2.ArchiveEntry.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='path', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='google.devtools.resultstore.v2.ArchiveEntry.length', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='length', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='google.devtools.resultstore.v2.ArchiveEntry.content_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=592,
  serialized_end=714,
)

_FILE.fields_by_name['length'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_FILE.fields_by_name['archive_entry'].message_type = _ARCHIVEENTRY
_FILE.fields_by_name['hash_type'].enum_type = _FILE_HASHTYPE
_FILE_HASHTYPE.containing_type = _FILE
_ARCHIVEENTRY.fields_by_name['length'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['ArchiveEntry'] = _ARCHIVEENTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'google.devtools.resultstore.v2.file_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.File)
  })
_sym_db.RegisterMessage(File)

ArchiveEntry = _reflection.GeneratedProtocolMessageType('ArchiveEntry', (_message.Message,), {
  'DESCRIPTOR' : _ARCHIVEENTRY,
  '__module__' : 'google.devtools.resultstore.v2.file_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ArchiveEntry)
  })
_sym_db.RegisterMessage(ArchiveEntry)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
