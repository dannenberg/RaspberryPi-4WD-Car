# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/sql/v1/cloud_sql_tiers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/sql/v1/cloud_sql_tiers.proto',
  package='google.cloud.sql.v1',
  syntax='proto3',
  serialized_options=b'\n\027com.google.cloud.sql.v1B\022CloudSqlTiersProtoP\001Z6google.golang.org/genproto/googleapis/cloud/sql/v1;sql',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)google/cloud/sql/v1/cloud_sql_tiers.proto\x12\x13google.cloud.sql.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\"/\n\x13SqlTiersListRequest\x12\x18\n\x07project\x18\x01 \x01(\tR\x07project\"X\n\x11TiersListResponse\x12\x12\n\x04kind\x18\x01 \x01(\tR\x04kind\x12/\n\x05items\x18\x02 \x03(\x0b\x32\x19.google.cloud.sql.v1.TierR\x05items\"w\n\x04Tier\x12\x12\n\x04tier\x18\x01 \x01(\tR\x04tier\x12\x10\n\x03RAM\x18\x02 \x01(\x03R\x03RAM\x12\x12\n\x04kind\x18\x03 \x01(\tR\x04kind\x12\x1d\n\nDisk_Quota\x18\x04 \x01(\x03R\tDiskQuota\x12\x16\n\x06region\x18\x05 \x03(\tR\x06region2\x8f\x02\n\x0fSqlTiersService\x12~\n\x04List\x12(.google.cloud.sql.v1.SqlTiersListRequest\x1a&.google.cloud.sql.v1.TiersListResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/projects/{project}/tiers\x1a|\xca\x41\x17sqladmin.googleapis.com\xd2\x41_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.adminBg\n\x17\x63om.google.cloud.sql.v1B\x12\x43loudSqlTiersProtoP\x01Z6google.golang.org/genproto/googleapis/cloud/sql/v1;sqlb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_SQLTIERSLISTREQUEST = _descriptor.Descriptor(
  name='SqlTiersListRequest',
  full_name='google.cloud.sql.v1.SqlTiersListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='google.cloud.sql.v1.SqlTiersListRequest.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='project', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=121,
  serialized_end=168,
)


_TIERSLISTRESPONSE = _descriptor.Descriptor(
  name='TiersListResponse',
  full_name='google.cloud.sql.v1.TiersListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='google.cloud.sql.v1.TiersListResponse.kind', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='kind', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='google.cloud.sql.v1.TiersListResponse.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='items', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=170,
  serialized_end=258,
)


_TIER = _descriptor.Descriptor(
  name='Tier',
  full_name='google.cloud.sql.v1.Tier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tier', full_name='google.cloud.sql.v1.Tier.tier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tier', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RAM', full_name='google.cloud.sql.v1.Tier.RAM', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='RAM', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kind', full_name='google.cloud.sql.v1.Tier.kind', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='kind', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Disk_Quota', full_name='google.cloud.sql.v1.Tier.Disk_Quota', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='DiskQuota', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='google.cloud.sql.v1.Tier.region', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='region', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=260,
  serialized_end=379,
)

_TIERSLISTRESPONSE.fields_by_name['items'].message_type = _TIER
DESCRIPTOR.message_types_by_name['SqlTiersListRequest'] = _SQLTIERSLISTREQUEST
DESCRIPTOR.message_types_by_name['TiersListResponse'] = _TIERSLISTRESPONSE
DESCRIPTOR.message_types_by_name['Tier'] = _TIER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SqlTiersListRequest = _reflection.GeneratedProtocolMessageType('SqlTiersListRequest', (_message.Message,), {
  'DESCRIPTOR' : _SQLTIERSLISTREQUEST,
  '__module__' : 'google.cloud.sql.v1.cloud_sql_tiers_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.sql.v1.SqlTiersListRequest)
  })
_sym_db.RegisterMessage(SqlTiersListRequest)

TiersListResponse = _reflection.GeneratedProtocolMessageType('TiersListResponse', (_message.Message,), {
  'DESCRIPTOR' : _TIERSLISTRESPONSE,
  '__module__' : 'google.cloud.sql.v1.cloud_sql_tiers_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.sql.v1.TiersListResponse)
  })
_sym_db.RegisterMessage(TiersListResponse)

Tier = _reflection.GeneratedProtocolMessageType('Tier', (_message.Message,), {
  'DESCRIPTOR' : _TIER,
  '__module__' : 'google.cloud.sql.v1.cloud_sql_tiers_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.sql.v1.Tier)
  })
_sym_db.RegisterMessage(Tier)


DESCRIPTOR._options = None

_SQLTIERSSERVICE = _descriptor.ServiceDescriptor(
  name='SqlTiersService',
  full_name='google.cloud.sql.v1.SqlTiersService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\027sqladmin.googleapis.com\322A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.admin',
  create_key=_descriptor._internal_create_key,
  serialized_start=382,
  serialized_end=653,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='google.cloud.sql.v1.SqlTiersService.List',
    index=0,
    containing_service=None,
    input_type=_SQLTIERSLISTREQUEST,
    output_type=_TIERSLISTRESPONSE,
    serialized_options=b'\202\323\344\223\002\036\022\034/v1/projects/{project}/tiers',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SQLTIERSSERVICE)

DESCRIPTOR.services_by_name['SqlTiersService'] = _SQLTIERSSERVICE

# @@protoc_insertion_point(module_scope)
