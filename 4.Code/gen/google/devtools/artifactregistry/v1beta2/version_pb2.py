# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/artifactregistry/v1beta2/version.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.devtools.artifactregistry.v1beta2 import tag_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/artifactregistry/v1beta2/version.proto',
  package='google.devtools.artifactregistry.v1beta2',
  syntax='proto3',
  serialized_options=b'\n,com.google.devtools.artifactregistry.v1beta2B\014VersionProtoP\001ZXgoogle.golang.org/genproto/googleapis/devtools/artifactregistry/v1beta2;artifactregistry\252\002%Google.Cloud.ArtifactRegistry.V1Beta2\312\002%Google\\Cloud\\ArtifactRegistry\\V1beta2\352\002(Google::Cloud::ArtifactRegistry::V1beta2',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6google/devtools/artifactregistry/v1beta2/version.proto\x12(google.devtools.artifactregistry.v1beta2\x1a\x32google/devtools/artifactregistry/v1beta2/tag.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x8b\x02\n\x07Version\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12P\n\x0crelated_tags\x18\x07 \x03(\x0b\x32-.google.devtools.artifactregistry.v1beta2.TagR\x0brelatedTags\"\xb4\x01\n\x13ListVersionsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12I\n\x04view\x18\x04 \x01(\x0e\x32\x35.google.devtools.artifactregistry.v1beta2.VersionViewR\x04view\"\x8d\x01\n\x14ListVersionsResponse\x12M\n\x08versions\x18\x01 \x03(\x0b\x32\x31.google.devtools.artifactregistry.v1beta2.VersionR\x08versions\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"r\n\x11GetVersionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12I\n\x04view\x18\x02 \x01(\x0e\x32\x35.google.devtools.artifactregistry.v1beta2.VersionViewR\x04view\"@\n\x14\x44\x65leteVersionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05\x66orce\x18\x02 \x01(\x08R\x05\x66orce*@\n\x0bVersionView\x12\x1c\n\x18VERSION_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05\x42\x41SIC\x10\x01\x12\x08\n\x04\x46ULL\x10\x02\x42\x93\x02\n,com.google.devtools.artifactregistry.v1beta2B\x0cVersionProtoP\x01ZXgoogle.golang.org/genproto/googleapis/devtools/artifactregistry/v1beta2;artifactregistry\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2b\x06proto3'
  ,
  dependencies=[google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_VERSIONVIEW = _descriptor.EnumDescriptor(
  name='VersionView',
  full_name='google.devtools.artifactregistry.v1beta2.VersionView',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VERSION_VIEW_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BASIC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=994,
  serialized_end=1058,
)
_sym_db.RegisterEnumDescriptor(_VERSIONVIEW)

VersionView = enum_type_wrapper.EnumTypeWrapper(_VERSIONVIEW)
VERSION_VIEW_UNSPECIFIED = 0
BASIC = 1
FULL = 2



_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='google.devtools.artifactregistry.v1beta2.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.artifactregistry.v1beta2.Version.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.devtools.artifactregistry.v1beta2.Version.description', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.devtools.artifactregistry.v1beta2.Version.create_time', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='createTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.devtools.artifactregistry.v1beta2.Version.update_time', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='updateTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='related_tags', full_name='google.devtools.artifactregistry.v1beta2.Version.related_tags', index=4,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='relatedTags', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=216,
  serialized_end=483,
)


_LISTVERSIONSREQUEST = _descriptor.Descriptor(
  name='ListVersionsRequest',
  full_name='google.devtools.artifactregistry.v1beta2.ListVersionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.devtools.artifactregistry.v1beta2.ListVersionsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.devtools.artifactregistry.v1beta2.ListVersionsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.devtools.artifactregistry.v1beta2.ListVersionsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='view', full_name='google.devtools.artifactregistry.v1beta2.ListVersionsRequest.view', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='view', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=486,
  serialized_end=666,
)


_LISTVERSIONSRESPONSE = _descriptor.Descriptor(
  name='ListVersionsResponse',
  full_name='google.devtools.artifactregistry.v1beta2.ListVersionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='versions', full_name='google.devtools.artifactregistry.v1beta2.ListVersionsResponse.versions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='versions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.devtools.artifactregistry.v1beta2.ListVersionsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nextPageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=669,
  serialized_end=810,
)


_GETVERSIONREQUEST = _descriptor.Descriptor(
  name='GetVersionRequest',
  full_name='google.devtools.artifactregistry.v1beta2.GetVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.artifactregistry.v1beta2.GetVersionRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='view', full_name='google.devtools.artifactregistry.v1beta2.GetVersionRequest.view', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='view', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=812,
  serialized_end=926,
)


_DELETEVERSIONREQUEST = _descriptor.Descriptor(
  name='DeleteVersionRequest',
  full_name='google.devtools.artifactregistry.v1beta2.DeleteVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.artifactregistry.v1beta2.DeleteVersionRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='force', full_name='google.devtools.artifactregistry.v1beta2.DeleteVersionRequest.force', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='force', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=928,
  serialized_end=992,
)

_VERSION.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_VERSION.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_VERSION.fields_by_name['related_tags'].message_type = google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2._TAG
_LISTVERSIONSREQUEST.fields_by_name['view'].enum_type = _VERSIONVIEW
_LISTVERSIONSRESPONSE.fields_by_name['versions'].message_type = _VERSION
_GETVERSIONREQUEST.fields_by_name['view'].enum_type = _VERSIONVIEW
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['ListVersionsRequest'] = _LISTVERSIONSREQUEST
DESCRIPTOR.message_types_by_name['ListVersionsResponse'] = _LISTVERSIONSRESPONSE
DESCRIPTOR.message_types_by_name['GetVersionRequest'] = _GETVERSIONREQUEST
DESCRIPTOR.message_types_by_name['DeleteVersionRequest'] = _DELETEVERSIONREQUEST
DESCRIPTOR.enum_types_by_name['VersionView'] = _VERSIONVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.version_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.Version)
  })
_sym_db.RegisterMessage(Version)

ListVersionsRequest = _reflection.GeneratedProtocolMessageType('ListVersionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTVERSIONSREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.version_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.ListVersionsRequest)
  })
_sym_db.RegisterMessage(ListVersionsRequest)

ListVersionsResponse = _reflection.GeneratedProtocolMessageType('ListVersionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTVERSIONSRESPONSE,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.version_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.ListVersionsResponse)
  })
_sym_db.RegisterMessage(ListVersionsResponse)

GetVersionRequest = _reflection.GeneratedProtocolMessageType('GetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVERSIONREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.version_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.GetVersionRequest)
  })
_sym_db.RegisterMessage(GetVersionRequest)

DeleteVersionRequest = _reflection.GeneratedProtocolMessageType('DeleteVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEVERSIONREQUEST,
  '__module__' : 'google.devtools.artifactregistry.v1beta2.version_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.artifactregistry.v1beta2.DeleteVersionRequest)
  })
_sym_db.RegisterMessage(DeleteVersionRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
