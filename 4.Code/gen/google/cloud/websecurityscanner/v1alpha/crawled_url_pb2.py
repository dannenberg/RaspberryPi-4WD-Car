# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner/v1alpha/crawled_url.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/websecurityscanner/v1alpha/crawled_url.proto',
  package='google.cloud.websecurityscanner.v1alpha',
  syntax='proto3',
  serialized_options=b'\n+com.google.cloud.websecurityscanner.v1alphaB\017CrawledUrlProtoP\001ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscanner',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9google/cloud/websecurityscanner/v1alpha/crawled_url.proto\x12\'google.cloud.websecurityscanner.v1alpha\"S\n\nCrawledUrl\x12\x1f\n\x0bhttp_method\x18\x01 \x01(\tR\nhttpMethod\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x12\x12\n\x04\x62ody\x18\x03 \x01(\tR\x04\x62odyB\x9b\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x0f\x43rawledUrlProtoP\x01ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscannerb\x06proto3'
)




_CRAWLEDURL = _descriptor.Descriptor(
  name='CrawledUrl',
  full_name='google.cloud.websecurityscanner.v1alpha.CrawledUrl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_method', full_name='google.cloud.websecurityscanner.v1alpha.CrawledUrl.http_method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='httpMethod', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='google.cloud.websecurityscanner.v1alpha.CrawledUrl.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='url', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='google.cloud.websecurityscanner.v1alpha.CrawledUrl.body', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='body', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=102,
  serialized_end=185,
)

DESCRIPTOR.message_types_by_name['CrawledUrl'] = _CRAWLEDURL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CrawledUrl = _reflection.GeneratedProtocolMessageType('CrawledUrl', (_message.Message,), {
  'DESCRIPTOR' : _CRAWLEDURL,
  '__module__' : 'google.cloud.websecurityscanner.v1alpha.crawled_url_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.CrawledUrl)
  })
_sym_db.RegisterMessage(CrawledUrl)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
