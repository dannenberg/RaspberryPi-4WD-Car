# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/scheduler/v1/target.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/scheduler/v1/target.proto',
  package='google.cloud.scheduler.v1',
  syntax='proto3',
  serialized_options=b'\n\035com.google.cloud.scheduler.v1B\013TargetProtoP\001ZBgoogle.golang.org/genproto/googleapis/cloud/scheduler/v1;scheduler\352A@\n\033pubsub.googleapis.com/Topic\022!projects/{project}/topics/{topic}',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&google/cloud/scheduler/v1/target.proto\x12\x19google.cloud.scheduler.v1\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xad\x03\n\nHttpTarget\x12\x10\n\x03uri\x18\x01 \x01(\tR\x03uri\x12\x46\n\x0bhttp_method\x18\x02 \x01(\x0e\x32%.google.cloud.scheduler.v1.HttpMethodR\nhttpMethod\x12L\n\x07headers\x18\x03 \x03(\x0b\x32\x32.google.cloud.scheduler.v1.HttpTarget.HeadersEntryR\x07headers\x12\x12\n\x04\x62ody\x18\x04 \x01(\x0cR\x04\x62ody\x12H\n\x0boauth_token\x18\x05 \x01(\x0b\x32%.google.cloud.scheduler.v1.OAuthTokenH\x00R\noauthToken\x12\x45\n\noidc_token\x18\x06 \x01(\x0b\x32$.google.cloud.scheduler.v1.OidcTokenH\x00R\toidcToken\x1a:\n\x0cHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x16\n\x14\x61uthorization_header\"\x82\x03\n\x13\x41ppEngineHttpTarget\x12\x46\n\x0bhttp_method\x18\x01 \x01(\x0e\x32%.google.cloud.scheduler.v1.HttpMethodR\nhttpMethod\x12Y\n\x12\x61pp_engine_routing\x18\x02 \x01(\x0b\x32+.google.cloud.scheduler.v1.AppEngineRoutingR\x10\x61ppEngineRouting\x12!\n\x0crelative_uri\x18\x03 \x01(\tR\x0brelativeUri\x12U\n\x07headers\x18\x04 \x03(\x0b\x32;.google.cloud.scheduler.v1.AppEngineHttpTarget.HeadersEntryR\x07headers\x12\x12\n\x04\x62ody\x18\x05 \x01(\x0cR\x04\x62ody\x1a:\n\x0cHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xfb\x01\n\x0cPubsubTarget\x12?\n\ntopic_name\x18\x01 \x01(\tB \xfa\x41\x1d\n\x1bpubsub.googleapis.com/TopicR\ttopicName\x12\x12\n\x04\x64\x61ta\x18\x03 \x01(\x0cR\x04\x64\x61ta\x12W\n\nattributes\x18\x04 \x03(\x0b\x32\x37.google.cloud.scheduler.v1.PubsubTarget.AttributesEntryR\nattributes\x1a=\n\x0f\x41ttributesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"v\n\x10\x41ppEngineRouting\x12\x18\n\x07service\x18\x01 \x01(\tR\x07service\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12\x1a\n\x08instance\x18\x03 \x01(\tR\x08instance\x12\x12\n\x04host\x18\x04 \x01(\tR\x04host\"V\n\nOAuthToken\x12\x32\n\x15service_account_email\x18\x01 \x01(\tR\x13serviceAccountEmail\x12\x14\n\x05scope\x18\x02 \x01(\tR\x05scope\"[\n\tOidcToken\x12\x32\n\x15service_account_email\x18\x01 \x01(\tR\x13serviceAccountEmail\x12\x1a\n\x08\x61udience\x18\x02 \x01(\tR\x08\x61udience*s\n\nHttpMethod\x12\x1b\n\x17HTTP_METHOD_UNSPECIFIED\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x07\n\x03GET\x10\x02\x12\x08\n\x04HEAD\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06\x44\x45LETE\x10\x05\x12\t\n\x05PATCH\x10\x06\x12\x0b\n\x07OPTIONS\x10\x07\x42\xb5\x01\n\x1d\x63om.google.cloud.scheduler.v1B\x0bTargetProtoP\x01ZBgoogle.golang.org/genproto/googleapis/cloud/scheduler/v1;scheduler\xea\x41@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_HTTPMETHOD = _descriptor.EnumDescriptor(
  name='HttpMethod',
  full_name='google.cloud.scheduler.v1.HttpMethod',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HTTP_METHOD_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POST', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GET', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HEAD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PATCH', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPTIONS', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1502,
  serialized_end=1617,
)
_sym_db.RegisterEnumDescriptor(_HTTPMETHOD)

HttpMethod = enum_type_wrapper.EnumTypeWrapper(_HTTPMETHOD)
HTTP_METHOD_UNSPECIFIED = 0
POST = 1
GET = 2
HEAD = 3
PUT = 4
DELETE = 5
PATCH = 6
OPTIONS = 7



_HTTPTARGET_HEADERSENTRY = _descriptor.Descriptor(
  name='HeadersEntry',
  full_name='google.cloud.scheduler.v1.HttpTarget.HeadersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.scheduler.v1.HttpTarget.HeadersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.scheduler.v1.HttpTarget.HeadersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=474,
  serialized_end=532,
)

_HTTPTARGET = _descriptor.Descriptor(
  name='HttpTarget',
  full_name='google.cloud.scheduler.v1.HttpTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='google.cloud.scheduler.v1.HttpTarget.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='uri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='http_method', full_name='google.cloud.scheduler.v1.HttpTarget.http_method', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='httpMethod', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='headers', full_name='google.cloud.scheduler.v1.HttpTarget.headers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='headers', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='google.cloud.scheduler.v1.HttpTarget.body', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='body', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oauth_token', full_name='google.cloud.scheduler.v1.HttpTarget.oauth_token', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='oauthToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oidc_token', full_name='google.cloud.scheduler.v1.HttpTarget.oidc_token', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='oidcToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HTTPTARGET_HEADERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='authorization_header', full_name='google.cloud.scheduler.v1.HttpTarget.authorization_header',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=127,
  serialized_end=556,
)


_APPENGINEHTTPTARGET_HEADERSENTRY = _descriptor.Descriptor(
  name='HeadersEntry',
  full_name='google.cloud.scheduler.v1.AppEngineHttpTarget.HeadersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.scheduler.v1.AppEngineHttpTarget.HeadersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.scheduler.v1.AppEngineHttpTarget.HeadersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=474,
  serialized_end=532,
)

_APPENGINEHTTPTARGET = _descriptor.Descriptor(
  name='AppEngineHttpTarget',
  full_name='google.cloud.scheduler.v1.AppEngineHttpTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_method', full_name='google.cloud.scheduler.v1.AppEngineHttpTarget.http_method', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='httpMethod', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_engine_routing', full_name='google.cloud.scheduler.v1.AppEngineHttpTarget.app_engine_routing', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='appEngineRouting', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relative_uri', full_name='google.cloud.scheduler.v1.AppEngineHttpTarget.relative_uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='relativeUri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='headers', full_name='google.cloud.scheduler.v1.AppEngineHttpTarget.headers', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='headers', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='google.cloud.scheduler.v1.AppEngineHttpTarget.body', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='body', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_APPENGINEHTTPTARGET_HEADERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=945,
)


_PUBSUBTARGET_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='google.cloud.scheduler.v1.PubsubTarget.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.scheduler.v1.PubsubTarget.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.scheduler.v1.PubsubTarget.AttributesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1138,
  serialized_end=1199,
)

_PUBSUBTARGET = _descriptor.Descriptor(
  name='PubsubTarget',
  full_name='google.cloud.scheduler.v1.PubsubTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_name', full_name='google.cloud.scheduler.v1.PubsubTarget.topic_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A\035\n\033pubsub.googleapis.com/Topic', json_name='topicName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='google.cloud.scheduler.v1.PubsubTarget.data', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='data', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='google.cloud.scheduler.v1.PubsubTarget.attributes', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='attributes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PUBSUBTARGET_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=948,
  serialized_end=1199,
)


_APPENGINEROUTING = _descriptor.Descriptor(
  name='AppEngineRouting',
  full_name='google.cloud.scheduler.v1.AppEngineRouting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='google.cloud.scheduler.v1.AppEngineRouting.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='service', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='google.cloud.scheduler.v1.AppEngineRouting.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='version', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance', full_name='google.cloud.scheduler.v1.AppEngineRouting.instance', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='instance', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='google.cloud.scheduler.v1.AppEngineRouting.host', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='host', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1201,
  serialized_end=1319,
)


_OAUTHTOKEN = _descriptor.Descriptor(
  name='OAuthToken',
  full_name='google.cloud.scheduler.v1.OAuthToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_email', full_name='google.cloud.scheduler.v1.OAuthToken.service_account_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serviceAccountEmail', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scope', full_name='google.cloud.scheduler.v1.OAuthToken.scope', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='scope', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1321,
  serialized_end=1407,
)


_OIDCTOKEN = _descriptor.Descriptor(
  name='OidcToken',
  full_name='google.cloud.scheduler.v1.OidcToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_email', full_name='google.cloud.scheduler.v1.OidcToken.service_account_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serviceAccountEmail', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audience', full_name='google.cloud.scheduler.v1.OidcToken.audience', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='audience', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1409,
  serialized_end=1500,
)

_HTTPTARGET_HEADERSENTRY.containing_type = _HTTPTARGET
_HTTPTARGET.fields_by_name['http_method'].enum_type = _HTTPMETHOD
_HTTPTARGET.fields_by_name['headers'].message_type = _HTTPTARGET_HEADERSENTRY
_HTTPTARGET.fields_by_name['oauth_token'].message_type = _OAUTHTOKEN
_HTTPTARGET.fields_by_name['oidc_token'].message_type = _OIDCTOKEN
_HTTPTARGET.oneofs_by_name['authorization_header'].fields.append(
  _HTTPTARGET.fields_by_name['oauth_token'])
_HTTPTARGET.fields_by_name['oauth_token'].containing_oneof = _HTTPTARGET.oneofs_by_name['authorization_header']
_HTTPTARGET.oneofs_by_name['authorization_header'].fields.append(
  _HTTPTARGET.fields_by_name['oidc_token'])
_HTTPTARGET.fields_by_name['oidc_token'].containing_oneof = _HTTPTARGET.oneofs_by_name['authorization_header']
_APPENGINEHTTPTARGET_HEADERSENTRY.containing_type = _APPENGINEHTTPTARGET
_APPENGINEHTTPTARGET.fields_by_name['http_method'].enum_type = _HTTPMETHOD
_APPENGINEHTTPTARGET.fields_by_name['app_engine_routing'].message_type = _APPENGINEROUTING
_APPENGINEHTTPTARGET.fields_by_name['headers'].message_type = _APPENGINEHTTPTARGET_HEADERSENTRY
_PUBSUBTARGET_ATTRIBUTESENTRY.containing_type = _PUBSUBTARGET
_PUBSUBTARGET.fields_by_name['attributes'].message_type = _PUBSUBTARGET_ATTRIBUTESENTRY
DESCRIPTOR.message_types_by_name['HttpTarget'] = _HTTPTARGET
DESCRIPTOR.message_types_by_name['AppEngineHttpTarget'] = _APPENGINEHTTPTARGET
DESCRIPTOR.message_types_by_name['PubsubTarget'] = _PUBSUBTARGET
DESCRIPTOR.message_types_by_name['AppEngineRouting'] = _APPENGINEROUTING
DESCRIPTOR.message_types_by_name['OAuthToken'] = _OAUTHTOKEN
DESCRIPTOR.message_types_by_name['OidcToken'] = _OIDCTOKEN
DESCRIPTOR.enum_types_by_name['HttpMethod'] = _HTTPMETHOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HttpTarget = _reflection.GeneratedProtocolMessageType('HttpTarget', (_message.Message,), {

  'HeadersEntry' : _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _HTTPTARGET_HEADERSENTRY,
    '__module__' : 'google.cloud.scheduler.v1.target_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.HttpTarget.HeadersEntry)
    })
  ,
  'DESCRIPTOR' : _HTTPTARGET,
  '__module__' : 'google.cloud.scheduler.v1.target_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.HttpTarget)
  })
_sym_db.RegisterMessage(HttpTarget)
_sym_db.RegisterMessage(HttpTarget.HeadersEntry)

AppEngineHttpTarget = _reflection.GeneratedProtocolMessageType('AppEngineHttpTarget', (_message.Message,), {

  'HeadersEntry' : _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _APPENGINEHTTPTARGET_HEADERSENTRY,
    '__module__' : 'google.cloud.scheduler.v1.target_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.AppEngineHttpTarget.HeadersEntry)
    })
  ,
  'DESCRIPTOR' : _APPENGINEHTTPTARGET,
  '__module__' : 'google.cloud.scheduler.v1.target_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.AppEngineHttpTarget)
  })
_sym_db.RegisterMessage(AppEngineHttpTarget)
_sym_db.RegisterMessage(AppEngineHttpTarget.HeadersEntry)

PubsubTarget = _reflection.GeneratedProtocolMessageType('PubsubTarget', (_message.Message,), {

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _PUBSUBTARGET_ATTRIBUTESENTRY,
    '__module__' : 'google.cloud.scheduler.v1.target_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.PubsubTarget.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _PUBSUBTARGET,
  '__module__' : 'google.cloud.scheduler.v1.target_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.PubsubTarget)
  })
_sym_db.RegisterMessage(PubsubTarget)
_sym_db.RegisterMessage(PubsubTarget.AttributesEntry)

AppEngineRouting = _reflection.GeneratedProtocolMessageType('AppEngineRouting', (_message.Message,), {
  'DESCRIPTOR' : _APPENGINEROUTING,
  '__module__' : 'google.cloud.scheduler.v1.target_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.AppEngineRouting)
  })
_sym_db.RegisterMessage(AppEngineRouting)

OAuthToken = _reflection.GeneratedProtocolMessageType('OAuthToken', (_message.Message,), {
  'DESCRIPTOR' : _OAUTHTOKEN,
  '__module__' : 'google.cloud.scheduler.v1.target_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.OAuthToken)
  })
_sym_db.RegisterMessage(OAuthToken)

OidcToken = _reflection.GeneratedProtocolMessageType('OidcToken', (_message.Message,), {
  'DESCRIPTOR' : _OIDCTOKEN,
  '__module__' : 'google.cloud.scheduler.v1.target_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.OidcToken)
  })
_sym_db.RegisterMessage(OidcToken)


DESCRIPTOR._options = None
_HTTPTARGET_HEADERSENTRY._options = None
_APPENGINEHTTPTARGET_HEADERSENTRY._options = None
_PUBSUBTARGET_ATTRIBUTESENTRY._options = None
_PUBSUBTARGET.fields_by_name['topic_name']._options = None
# @@protoc_insertion_point(module_scope)
