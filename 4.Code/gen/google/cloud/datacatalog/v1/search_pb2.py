# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datacatalog/v1/search.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.datacatalog.v1 import common_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/datacatalog/v1/search.proto',
  package='google.cloud.datacatalog.v1',
  syntax='proto3',
  serialized_options=b'\n\037com.google.cloud.datacatalog.v1P\001ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\370\001\001\252\002\033Google.Cloud.DataCatalog.V1\312\002\033Google\\Cloud\\DataCatalog\\V1\352\002\036Google::Cloud::DataCatalog::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(google/cloud/datacatalog/v1/search.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a(google/cloud/datacatalog/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xdd\x04\n\x13SearchCatalogResult\x12[\n\x12search_result_type\x18\x01 \x01(\x0e\x32-.google.cloud.datacatalog.v1.SearchResultTypeR\x10searchResultType\x12\x32\n\x15search_result_subtype\x18\x02 \x01(\tR\x13searchResultSubtype\x12\x34\n\x16relative_resource_name\x18\x03 \x01(\tR\x14relativeResourceName\x12\'\n\x0flinked_resource\x18\x04 \x01(\tR\x0elinkedResource\x12;\n\x0bmodify_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nmodifyTime\x12\x62\n\x11integrated_system\x18\x08 \x01(\x0e\x32-.google.cloud.datacatalog.v1.IntegratedSystemB\x04\xe2\x41\x01\x03H\x00R\x10integratedSystem\x12\x34\n\x15user_specified_system\x18\t \x01(\tH\x00R\x13userSpecifiedSystem\x12\x30\n\x14\x66ully_qualified_name\x18\n \x01(\tR\x12\x66ullyQualifiedName\x12!\n\x0c\x64isplay_name\x18\x0c \x01(\tR\x0b\x64isplayName\x12 \n\x0b\x64\x65scription\x18\r \x01(\tR\x0b\x64\x65scriptionB\x08\n\x06system*d\n\x10SearchResultType\x12\"\n\x1eSEARCH_RESULT_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05\x45NTRY\x10\x01\x12\x10\n\x0cTAG_TEMPLATE\x10\x02\x12\x0f\n\x0b\x45NTRY_GROUP\x10\x03\x42\xcb\x01\n\x1f\x63om.google.cloud.datacatalog.v1P\x01ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\xf8\x01\x01\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_cloud_dot_datacatalog_dot_v1_dot_common__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_SEARCHRESULTTYPE = _descriptor.EnumDescriptor(
  name='SearchResultType',
  full_name='google.cloud.datacatalog.v1.SearchResultType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SEARCH_RESULT_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTRY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TAG_TEMPLATE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTRY_GROUP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=789,
  serialized_end=889,
)
_sym_db.RegisterEnumDescriptor(_SEARCHRESULTTYPE)

SearchResultType = enum_type_wrapper.EnumTypeWrapper(_SEARCHRESULTTYPE)
SEARCH_RESULT_TYPE_UNSPECIFIED = 0
ENTRY = 1
TAG_TEMPLATE = 2
ENTRY_GROUP = 3



_SEARCHCATALOGRESULT = _descriptor.Descriptor(
  name='SearchCatalogResult',
  full_name='google.cloud.datacatalog.v1.SearchCatalogResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='search_result_type', full_name='google.cloud.datacatalog.v1.SearchCatalogResult.search_result_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='searchResultType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='search_result_subtype', full_name='google.cloud.datacatalog.v1.SearchCatalogResult.search_result_subtype', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='searchResultSubtype', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relative_resource_name', full_name='google.cloud.datacatalog.v1.SearchCatalogResult.relative_resource_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='relativeResourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='linked_resource', full_name='google.cloud.datacatalog.v1.SearchCatalogResult.linked_resource', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='linkedResource', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modify_time', full_name='google.cloud.datacatalog.v1.SearchCatalogResult.modify_time', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='modifyTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='integrated_system', full_name='google.cloud.datacatalog.v1.SearchCatalogResult.integrated_system', index=5,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='integratedSystem', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_specified_system', full_name='google.cloud.datacatalog.v1.SearchCatalogResult.user_specified_system', index=6,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='userSpecifiedSystem', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fully_qualified_name', full_name='google.cloud.datacatalog.v1.SearchCatalogResult.fully_qualified_name', index=7,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fullyQualifiedName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.datacatalog.v1.SearchCatalogResult.display_name', index=8,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='displayName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.datacatalog.v1.SearchCatalogResult.description', index=9,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='system', full_name='google.cloud.datacatalog.v1.SearchCatalogResult.system',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=182,
  serialized_end=787,
)

_SEARCHCATALOGRESULT.fields_by_name['search_result_type'].enum_type = _SEARCHRESULTTYPE
_SEARCHCATALOGRESULT.fields_by_name['modify_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SEARCHCATALOGRESULT.fields_by_name['integrated_system'].enum_type = google_dot_cloud_dot_datacatalog_dot_v1_dot_common__pb2._INTEGRATEDSYSTEM
_SEARCHCATALOGRESULT.oneofs_by_name['system'].fields.append(
  _SEARCHCATALOGRESULT.fields_by_name['integrated_system'])
_SEARCHCATALOGRESULT.fields_by_name['integrated_system'].containing_oneof = _SEARCHCATALOGRESULT.oneofs_by_name['system']
_SEARCHCATALOGRESULT.oneofs_by_name['system'].fields.append(
  _SEARCHCATALOGRESULT.fields_by_name['user_specified_system'])
_SEARCHCATALOGRESULT.fields_by_name['user_specified_system'].containing_oneof = _SEARCHCATALOGRESULT.oneofs_by_name['system']
DESCRIPTOR.message_types_by_name['SearchCatalogResult'] = _SEARCHCATALOGRESULT
DESCRIPTOR.enum_types_by_name['SearchResultType'] = _SEARCHRESULTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchCatalogResult = _reflection.GeneratedProtocolMessageType('SearchCatalogResult', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHCATALOGRESULT,
  '__module__' : 'google.cloud.datacatalog.v1.search_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1.SearchCatalogResult)
  })
_sym_db.RegisterMessage(SearchCatalogResult)


DESCRIPTOR._options = None
_SEARCHCATALOGRESULT.fields_by_name['integrated_system']._options = None
# @@protoc_insertion_point(module_scope)
