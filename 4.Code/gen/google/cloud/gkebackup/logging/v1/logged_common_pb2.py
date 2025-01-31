# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/gkebackup/logging/v1/logged_common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/gkebackup/logging/v1/logged_common.proto',
  package='google.cloud.gkebackup.logging.v1',
  syntax='proto3',
  serialized_options=b'\n!google.cloud.gkebackup.logging.v1B\021LoggedCommonProtoP\001ZHgoogle.golang.org/genproto/googleapis/cloud/gkebackup/logging/v1;logging\252\002!Google.Cloud.GkeBackup.Logging.V1\312\002!Google\\Cloud\\GkeBackup\\Logging\\V1\352\002%Google::Cloud::GkeBackup::Logging::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5google/cloud/gkebackup/logging/v1/logged_common.proto\x12!google.cloud.gkebackup.logging.v1\",\n\nNamespaces\x12\x1e\n\nnamespaces\x18\x01 \x03(\tR\nnamespaces\"B\n\x0eNamespacedName\x12\x1c\n\tnamespace\x18\x01 \x01(\tR\tnamespace\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"o\n\x0fNamespacedNames\x12\\\n\x10namespaced_names\x18\x01 \x03(\x0b\x32\x31.google.cloud.gkebackup.logging.v1.NamespacedNameR\x0fnamespacedNames\"D\n\rEncryptionKey\x12\x33\n\x16gcp_kms_encryption_key\x18\x01 \x01(\tR\x13gcpKmsEncryptionKeyB\xf2\x01\n!google.cloud.gkebackup.logging.v1B\x11LoggedCommonProtoP\x01ZHgoogle.golang.org/genproto/googleapis/cloud/gkebackup/logging/v1;logging\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1b\x06proto3'
)




_NAMESPACES = _descriptor.Descriptor(
  name='Namespaces',
  full_name='google.cloud.gkebackup.logging.v1.Namespaces',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespaces', full_name='google.cloud.gkebackup.logging.v1.Namespaces.namespaces', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='namespaces', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=92,
  serialized_end=136,
)


_NAMESPACEDNAME = _descriptor.Descriptor(
  name='NamespacedName',
  full_name='google.cloud.gkebackup.logging.v1.NamespacedName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='google.cloud.gkebackup.logging.v1.NamespacedName.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='namespace', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.gkebackup.logging.v1.NamespacedName.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=138,
  serialized_end=204,
)


_NAMESPACEDNAMES = _descriptor.Descriptor(
  name='NamespacedNames',
  full_name='google.cloud.gkebackup.logging.v1.NamespacedNames',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespaced_names', full_name='google.cloud.gkebackup.logging.v1.NamespacedNames.namespaced_names', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='namespacedNames', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=206,
  serialized_end=317,
)


_ENCRYPTIONKEY = _descriptor.Descriptor(
  name='EncryptionKey',
  full_name='google.cloud.gkebackup.logging.v1.EncryptionKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gcp_kms_encryption_key', full_name='google.cloud.gkebackup.logging.v1.EncryptionKey.gcp_kms_encryption_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gcpKmsEncryptionKey', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=319,
  serialized_end=387,
)

_NAMESPACEDNAMES.fields_by_name['namespaced_names'].message_type = _NAMESPACEDNAME
DESCRIPTOR.message_types_by_name['Namespaces'] = _NAMESPACES
DESCRIPTOR.message_types_by_name['NamespacedName'] = _NAMESPACEDNAME
DESCRIPTOR.message_types_by_name['NamespacedNames'] = _NAMESPACEDNAMES
DESCRIPTOR.message_types_by_name['EncryptionKey'] = _ENCRYPTIONKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Namespaces = _reflection.GeneratedProtocolMessageType('Namespaces', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACES,
  '__module__' : 'google.cloud.gkebackup.logging.v1.logged_common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gkebackup.logging.v1.Namespaces)
  })
_sym_db.RegisterMessage(Namespaces)

NamespacedName = _reflection.GeneratedProtocolMessageType('NamespacedName', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACEDNAME,
  '__module__' : 'google.cloud.gkebackup.logging.v1.logged_common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gkebackup.logging.v1.NamespacedName)
  })
_sym_db.RegisterMessage(NamespacedName)

NamespacedNames = _reflection.GeneratedProtocolMessageType('NamespacedNames', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACEDNAMES,
  '__module__' : 'google.cloud.gkebackup.logging.v1.logged_common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gkebackup.logging.v1.NamespacedNames)
  })
_sym_db.RegisterMessage(NamespacedNames)

EncryptionKey = _reflection.GeneratedProtocolMessageType('EncryptionKey', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTIONKEY,
  '__module__' : 'google.cloud.gkebackup.logging.v1.logged_common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gkebackup.logging.v1.EncryptionKey)
  })
_sym_db.RegisterMessage(EncryptionKey)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
