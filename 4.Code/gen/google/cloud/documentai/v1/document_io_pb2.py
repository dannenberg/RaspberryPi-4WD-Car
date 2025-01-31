# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/documentai/v1/document_io.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/documentai/v1/document_io.proto',
  package='google.cloud.documentai.v1',
  syntax='proto3',
  serialized_options=b'\n\036com.google.cloud.documentai.v1B\017DocumentIoProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/documentai/v1;documentai\252\002\032Google.Cloud.DocumentAI.V1\312\002\032Google\\Cloud\\DocumentAI\\V1\352\002\035Google::Cloud::DocumentAI::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,google/cloud/documentai/v1/document_io.proto\x12\x1agoogle.cloud.documentai.v1\x1a\x1cgoogle/api/annotations.proto\"D\n\x0bRawDocument\x12\x18\n\x07\x63ontent\x18\x01 \x01(\x0cR\x07\x63ontent\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType\"C\n\x0bGcsDocument\x12\x17\n\x07gcs_uri\x18\x01 \x01(\tR\x06gcsUri\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType\"U\n\x0cGcsDocuments\x12\x45\n\tdocuments\x18\x01 \x03(\x0b\x32\'.google.cloud.documentai.v1.GcsDocumentR\tdocuments\"1\n\tGcsPrefix\x12$\n\x0egcs_uri_prefix\x18\x01 \x01(\tR\x0cgcsUriPrefix\"\xbe\x01\n\x19\x42\x61tchDocumentsInputConfig\x12\x46\n\ngcs_prefix\x18\x01 \x01(\x0b\x32%.google.cloud.documentai.v1.GcsPrefixH\x00R\tgcsPrefix\x12O\n\rgcs_documents\x18\x02 \x01(\x0b\x32(.google.cloud.documentai.v1.GcsDocumentsH\x00R\x0cgcsDocumentsB\x08\n\x06source\"\xc1\x01\n\x14\x44ocumentOutputConfig\x12n\n\x11gcs_output_config\x18\x01 \x01(\x0b\x32@.google.cloud.documentai.v1.DocumentOutputConfig.GcsOutputConfigH\x00R\x0fgcsOutputConfig\x1a*\n\x0fGcsOutputConfig\x12\x17\n\x07gcs_uri\x18\x01 \x01(\tR\x06gcsUriB\r\n\x0b\x64\x65stinationB\xd3\x01\n\x1e\x63om.google.cloud.documentai.v1B\x0f\x44ocumentIoProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/documentai/v1;documentai\xaa\x02\x1aGoogle.Cloud.DocumentAI.V1\xca\x02\x1aGoogle\\Cloud\\DocumentAI\\V1\xea\x02\x1dGoogle::Cloud::DocumentAI::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_RAWDOCUMENT = _descriptor.Descriptor(
  name='RawDocument',
  full_name='google.cloud.documentai.v1.RawDocument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='google.cloud.documentai.v1.RawDocument.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='content', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='google.cloud.documentai.v1.RawDocument.mime_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='mimeType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=106,
  serialized_end=174,
)


_GCSDOCUMENT = _descriptor.Descriptor(
  name='GcsDocument',
  full_name='google.cloud.documentai.v1.GcsDocument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gcs_uri', full_name='google.cloud.documentai.v1.GcsDocument.gcs_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gcsUri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='google.cloud.documentai.v1.GcsDocument.mime_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='mimeType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=176,
  serialized_end=243,
)


_GCSDOCUMENTS = _descriptor.Descriptor(
  name='GcsDocuments',
  full_name='google.cloud.documentai.v1.GcsDocuments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='documents', full_name='google.cloud.documentai.v1.GcsDocuments.documents', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='documents', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=245,
  serialized_end=330,
)


_GCSPREFIX = _descriptor.Descriptor(
  name='GcsPrefix',
  full_name='google.cloud.documentai.v1.GcsPrefix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gcs_uri_prefix', full_name='google.cloud.documentai.v1.GcsPrefix.gcs_uri_prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gcsUriPrefix', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=332,
  serialized_end=381,
)


_BATCHDOCUMENTSINPUTCONFIG = _descriptor.Descriptor(
  name='BatchDocumentsInputConfig',
  full_name='google.cloud.documentai.v1.BatchDocumentsInputConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gcs_prefix', full_name='google.cloud.documentai.v1.BatchDocumentsInputConfig.gcs_prefix', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gcsPrefix', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gcs_documents', full_name='google.cloud.documentai.v1.BatchDocumentsInputConfig.gcs_documents', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gcsDocuments', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='source', full_name='google.cloud.documentai.v1.BatchDocumentsInputConfig.source',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=384,
  serialized_end=574,
)


_DOCUMENTOUTPUTCONFIG_GCSOUTPUTCONFIG = _descriptor.Descriptor(
  name='GcsOutputConfig',
  full_name='google.cloud.documentai.v1.DocumentOutputConfig.GcsOutputConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gcs_uri', full_name='google.cloud.documentai.v1.DocumentOutputConfig.GcsOutputConfig.gcs_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gcsUri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=713,
  serialized_end=755,
)

_DOCUMENTOUTPUTCONFIG = _descriptor.Descriptor(
  name='DocumentOutputConfig',
  full_name='google.cloud.documentai.v1.DocumentOutputConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gcs_output_config', full_name='google.cloud.documentai.v1.DocumentOutputConfig.gcs_output_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gcsOutputConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DOCUMENTOUTPUTCONFIG_GCSOUTPUTCONFIG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='destination', full_name='google.cloud.documentai.v1.DocumentOutputConfig.destination',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=577,
  serialized_end=770,
)

_GCSDOCUMENTS.fields_by_name['documents'].message_type = _GCSDOCUMENT
_BATCHDOCUMENTSINPUTCONFIG.fields_by_name['gcs_prefix'].message_type = _GCSPREFIX
_BATCHDOCUMENTSINPUTCONFIG.fields_by_name['gcs_documents'].message_type = _GCSDOCUMENTS
_BATCHDOCUMENTSINPUTCONFIG.oneofs_by_name['source'].fields.append(
  _BATCHDOCUMENTSINPUTCONFIG.fields_by_name['gcs_prefix'])
_BATCHDOCUMENTSINPUTCONFIG.fields_by_name['gcs_prefix'].containing_oneof = _BATCHDOCUMENTSINPUTCONFIG.oneofs_by_name['source']
_BATCHDOCUMENTSINPUTCONFIG.oneofs_by_name['source'].fields.append(
  _BATCHDOCUMENTSINPUTCONFIG.fields_by_name['gcs_documents'])
_BATCHDOCUMENTSINPUTCONFIG.fields_by_name['gcs_documents'].containing_oneof = _BATCHDOCUMENTSINPUTCONFIG.oneofs_by_name['source']
_DOCUMENTOUTPUTCONFIG_GCSOUTPUTCONFIG.containing_type = _DOCUMENTOUTPUTCONFIG
_DOCUMENTOUTPUTCONFIG.fields_by_name['gcs_output_config'].message_type = _DOCUMENTOUTPUTCONFIG_GCSOUTPUTCONFIG
_DOCUMENTOUTPUTCONFIG.oneofs_by_name['destination'].fields.append(
  _DOCUMENTOUTPUTCONFIG.fields_by_name['gcs_output_config'])
_DOCUMENTOUTPUTCONFIG.fields_by_name['gcs_output_config'].containing_oneof = _DOCUMENTOUTPUTCONFIG.oneofs_by_name['destination']
DESCRIPTOR.message_types_by_name['RawDocument'] = _RAWDOCUMENT
DESCRIPTOR.message_types_by_name['GcsDocument'] = _GCSDOCUMENT
DESCRIPTOR.message_types_by_name['GcsDocuments'] = _GCSDOCUMENTS
DESCRIPTOR.message_types_by_name['GcsPrefix'] = _GCSPREFIX
DESCRIPTOR.message_types_by_name['BatchDocumentsInputConfig'] = _BATCHDOCUMENTSINPUTCONFIG
DESCRIPTOR.message_types_by_name['DocumentOutputConfig'] = _DOCUMENTOUTPUTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RawDocument = _reflection.GeneratedProtocolMessageType('RawDocument', (_message.Message,), {
  'DESCRIPTOR' : _RAWDOCUMENT,
  '__module__' : 'google.cloud.documentai.v1.document_io_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1.RawDocument)
  })
_sym_db.RegisterMessage(RawDocument)

GcsDocument = _reflection.GeneratedProtocolMessageType('GcsDocument', (_message.Message,), {
  'DESCRIPTOR' : _GCSDOCUMENT,
  '__module__' : 'google.cloud.documentai.v1.document_io_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1.GcsDocument)
  })
_sym_db.RegisterMessage(GcsDocument)

GcsDocuments = _reflection.GeneratedProtocolMessageType('GcsDocuments', (_message.Message,), {
  'DESCRIPTOR' : _GCSDOCUMENTS,
  '__module__' : 'google.cloud.documentai.v1.document_io_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1.GcsDocuments)
  })
_sym_db.RegisterMessage(GcsDocuments)

GcsPrefix = _reflection.GeneratedProtocolMessageType('GcsPrefix', (_message.Message,), {
  'DESCRIPTOR' : _GCSPREFIX,
  '__module__' : 'google.cloud.documentai.v1.document_io_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1.GcsPrefix)
  })
_sym_db.RegisterMessage(GcsPrefix)

BatchDocumentsInputConfig = _reflection.GeneratedProtocolMessageType('BatchDocumentsInputConfig', (_message.Message,), {
  'DESCRIPTOR' : _BATCHDOCUMENTSINPUTCONFIG,
  '__module__' : 'google.cloud.documentai.v1.document_io_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1.BatchDocumentsInputConfig)
  })
_sym_db.RegisterMessage(BatchDocumentsInputConfig)

DocumentOutputConfig = _reflection.GeneratedProtocolMessageType('DocumentOutputConfig', (_message.Message,), {

  'GcsOutputConfig' : _reflection.GeneratedProtocolMessageType('GcsOutputConfig', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENTOUTPUTCONFIG_GCSOUTPUTCONFIG,
    '__module__' : 'google.cloud.documentai.v1.document_io_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1.DocumentOutputConfig.GcsOutputConfig)
    })
  ,
  'DESCRIPTOR' : _DOCUMENTOUTPUTCONFIG,
  '__module__' : 'google.cloud.documentai.v1.document_io_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1.DocumentOutputConfig)
  })
_sym_db.RegisterMessage(DocumentOutputConfig)
_sym_db.RegisterMessage(DocumentOutputConfig.GcsOutputConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
