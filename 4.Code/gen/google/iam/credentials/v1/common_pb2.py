# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/iam/credentials/v1/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/iam/credentials/v1/common.proto',
  package='google.iam.credentials.v1',
  syntax='proto3',
  serialized_options=b'\n#com.google.cloud.iam.credentials.v1B\031IAMCredentialsCommonProtoP\001ZDgoogle.golang.org/genproto/googleapis/iam/credentials/v1;credentials\370\001\001\252\002\037Google.Cloud.Iam.Credentials.V1\352AY\n!iam.googleapis.com/ServiceAccount\0224projects/{project}/serviceAccounts/{service_account}',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&google/iam/credentials/v1/common.proto\x12\x19google.iam.credentials.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcd\x01\n\x1aGenerateAccessTokenRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!iam.googleapis.com/ServiceAccountR\x04name\x12\x1c\n\tdelegates\x18\x02 \x03(\tR\tdelegates\x12\x1a\n\x05scope\x18\x04 \x03(\tB\x04\xe2\x41\x01\x02R\x05scope\x12\x35\n\x08lifetime\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08lifetime\"}\n\x1bGenerateAccessTokenResponse\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\tR\x0b\x61\x63\x63\x65ssToken\x12;\n\x0b\x65xpire_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nexpireTime\"\x8f\x01\n\x0fSignBlobRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!iam.googleapis.com/ServiceAccountR\x04name\x12\x1c\n\tdelegates\x18\x03 \x03(\tR\tdelegates\x12\x1e\n\x07payload\x18\x05 \x01(\x0c\x42\x04\xe2\x41\x01\x02R\x07payload\"J\n\x10SignBlobResponse\x12\x15\n\x06key_id\x18\x01 \x01(\tR\x05keyId\x12\x1f\n\x0bsigned_blob\x18\x04 \x01(\x0cR\nsignedBlob\"\x8e\x01\n\x0eSignJwtRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!iam.googleapis.com/ServiceAccountR\x04name\x12\x1c\n\tdelegates\x18\x03 \x03(\tR\tdelegates\x12\x1e\n\x07payload\x18\x05 \x01(\tB\x04\xe2\x41\x01\x02R\x07payload\"G\n\x0fSignJwtResponse\x12\x15\n\x06key_id\x18\x01 \x01(\tR\x05keyId\x12\x1d\n\nsigned_jwt\x18\x02 \x01(\tR\tsignedJwt\"\xbd\x01\n\x16GenerateIdTokenRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!iam.googleapis.com/ServiceAccountR\x04name\x12\x1c\n\tdelegates\x18\x02 \x03(\tR\tdelegates\x12 \n\x08\x61udience\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x08\x61udience\x12#\n\rinclude_email\x18\x04 \x01(\x08R\x0cincludeEmail\"/\n\x17GenerateIdTokenResponse\x12\x14\n\x05token\x18\x01 \x01(\tR\x05tokenB\x89\x02\n#com.google.cloud.iam.credentials.v1B\x19IAMCredentialsCommonProtoP\x01ZDgoogle.golang.org/genproto/googleapis/iam/credentials/v1;credentials\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.Iam.Credentials.V1\xea\x41Y\n!iam.googleapis.com/ServiceAccount\x12\x34projects/{project}/serviceAccounts/{service_account}b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_GENERATEACCESSTOKENREQUEST = _descriptor.Descriptor(
  name='GenerateAccessTokenRequest',
  full_name='google.iam.credentials.v1.GenerateAccessTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.iam.credentials.v1.GenerateAccessTokenRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A#\n!iam.googleapis.com/ServiceAccount', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delegates', full_name='google.iam.credentials.v1.GenerateAccessTokenRequest.delegates', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='delegates', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scope', full_name='google.iam.credentials.v1.GenerateAccessTokenRequest.scope', index=2,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='scope', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lifetime', full_name='google.iam.credentials.v1.GenerateAccessTokenRequest.lifetime', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='lifetime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=195,
  serialized_end=400,
)


_GENERATEACCESSTOKENRESPONSE = _descriptor.Descriptor(
  name='GenerateAccessTokenResponse',
  full_name='google.iam.credentials.v1.GenerateAccessTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='google.iam.credentials.v1.GenerateAccessTokenResponse.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='accessToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expire_time', full_name='google.iam.credentials.v1.GenerateAccessTokenResponse.expire_time', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='expireTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=402,
  serialized_end=527,
)


_SIGNBLOBREQUEST = _descriptor.Descriptor(
  name='SignBlobRequest',
  full_name='google.iam.credentials.v1.SignBlobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.iam.credentials.v1.SignBlobRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A#\n!iam.googleapis.com/ServiceAccount', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delegates', full_name='google.iam.credentials.v1.SignBlobRequest.delegates', index=1,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='delegates', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='google.iam.credentials.v1.SignBlobRequest.payload', index=2,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='payload', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=530,
  serialized_end=673,
)


_SIGNBLOBRESPONSE = _descriptor.Descriptor(
  name='SignBlobResponse',
  full_name='google.iam.credentials.v1.SignBlobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='google.iam.credentials.v1.SignBlobResponse.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='keyId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signed_blob', full_name='google.iam.credentials.v1.SignBlobResponse.signed_blob', index=1,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signedBlob', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=675,
  serialized_end=749,
)


_SIGNJWTREQUEST = _descriptor.Descriptor(
  name='SignJwtRequest',
  full_name='google.iam.credentials.v1.SignJwtRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.iam.credentials.v1.SignJwtRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A#\n!iam.googleapis.com/ServiceAccount', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delegates', full_name='google.iam.credentials.v1.SignJwtRequest.delegates', index=1,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='delegates', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='google.iam.credentials.v1.SignJwtRequest.payload', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='payload', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=752,
  serialized_end=894,
)


_SIGNJWTRESPONSE = _descriptor.Descriptor(
  name='SignJwtResponse',
  full_name='google.iam.credentials.v1.SignJwtResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='google.iam.credentials.v1.SignJwtResponse.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='keyId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signed_jwt', full_name='google.iam.credentials.v1.SignJwtResponse.signed_jwt', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signedJwt', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=896,
  serialized_end=967,
)


_GENERATEIDTOKENREQUEST = _descriptor.Descriptor(
  name='GenerateIdTokenRequest',
  full_name='google.iam.credentials.v1.GenerateIdTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.iam.credentials.v1.GenerateIdTokenRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A#\n!iam.googleapis.com/ServiceAccount', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delegates', full_name='google.iam.credentials.v1.GenerateIdTokenRequest.delegates', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='delegates', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audience', full_name='google.iam.credentials.v1.GenerateIdTokenRequest.audience', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='audience', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='include_email', full_name='google.iam.credentials.v1.GenerateIdTokenRequest.include_email', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='includeEmail', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=970,
  serialized_end=1159,
)


_GENERATEIDTOKENRESPONSE = _descriptor.Descriptor(
  name='GenerateIdTokenResponse',
  full_name='google.iam.credentials.v1.GenerateIdTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='google.iam.credentials.v1.GenerateIdTokenResponse.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='token', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1161,
  serialized_end=1208,
)

_GENERATEACCESSTOKENREQUEST.fields_by_name['lifetime'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_GENERATEACCESSTOKENRESPONSE.fields_by_name['expire_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['GenerateAccessTokenRequest'] = _GENERATEACCESSTOKENREQUEST
DESCRIPTOR.message_types_by_name['GenerateAccessTokenResponse'] = _GENERATEACCESSTOKENRESPONSE
DESCRIPTOR.message_types_by_name['SignBlobRequest'] = _SIGNBLOBREQUEST
DESCRIPTOR.message_types_by_name['SignBlobResponse'] = _SIGNBLOBRESPONSE
DESCRIPTOR.message_types_by_name['SignJwtRequest'] = _SIGNJWTREQUEST
DESCRIPTOR.message_types_by_name['SignJwtResponse'] = _SIGNJWTRESPONSE
DESCRIPTOR.message_types_by_name['GenerateIdTokenRequest'] = _GENERATEIDTOKENREQUEST
DESCRIPTOR.message_types_by_name['GenerateIdTokenResponse'] = _GENERATEIDTOKENRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenerateAccessTokenRequest = _reflection.GeneratedProtocolMessageType('GenerateAccessTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEACCESSTOKENREQUEST,
  '__module__' : 'google.iam.credentials.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.GenerateAccessTokenRequest)
  })
_sym_db.RegisterMessage(GenerateAccessTokenRequest)

GenerateAccessTokenResponse = _reflection.GeneratedProtocolMessageType('GenerateAccessTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEACCESSTOKENRESPONSE,
  '__module__' : 'google.iam.credentials.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.GenerateAccessTokenResponse)
  })
_sym_db.RegisterMessage(GenerateAccessTokenResponse)

SignBlobRequest = _reflection.GeneratedProtocolMessageType('SignBlobRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNBLOBREQUEST,
  '__module__' : 'google.iam.credentials.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.SignBlobRequest)
  })
_sym_db.RegisterMessage(SignBlobRequest)

SignBlobResponse = _reflection.GeneratedProtocolMessageType('SignBlobResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNBLOBRESPONSE,
  '__module__' : 'google.iam.credentials.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.SignBlobResponse)
  })
_sym_db.RegisterMessage(SignBlobResponse)

SignJwtRequest = _reflection.GeneratedProtocolMessageType('SignJwtRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNJWTREQUEST,
  '__module__' : 'google.iam.credentials.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.SignJwtRequest)
  })
_sym_db.RegisterMessage(SignJwtRequest)

SignJwtResponse = _reflection.GeneratedProtocolMessageType('SignJwtResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNJWTRESPONSE,
  '__module__' : 'google.iam.credentials.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.SignJwtResponse)
  })
_sym_db.RegisterMessage(SignJwtResponse)

GenerateIdTokenRequest = _reflection.GeneratedProtocolMessageType('GenerateIdTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEIDTOKENREQUEST,
  '__module__' : 'google.iam.credentials.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.GenerateIdTokenRequest)
  })
_sym_db.RegisterMessage(GenerateIdTokenRequest)

GenerateIdTokenResponse = _reflection.GeneratedProtocolMessageType('GenerateIdTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEIDTOKENRESPONSE,
  '__module__' : 'google.iam.credentials.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.GenerateIdTokenResponse)
  })
_sym_db.RegisterMessage(GenerateIdTokenResponse)


DESCRIPTOR._options = None
_GENERATEACCESSTOKENREQUEST.fields_by_name['name']._options = None
_GENERATEACCESSTOKENREQUEST.fields_by_name['scope']._options = None
_SIGNBLOBREQUEST.fields_by_name['name']._options = None
_SIGNBLOBREQUEST.fields_by_name['payload']._options = None
_SIGNJWTREQUEST.fields_by_name['name']._options = None
_SIGNJWTREQUEST.fields_by_name['payload']._options = None
_GENERATEIDTOKENREQUEST.fields_by_name['name']._options = None
_GENERATEIDTOKENREQUEST.fields_by_name['audience']._options = None
# @@protoc_insertion_point(module_scope)
