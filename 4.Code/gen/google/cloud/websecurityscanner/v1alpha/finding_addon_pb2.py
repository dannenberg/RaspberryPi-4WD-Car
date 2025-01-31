# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner/v1alpha/finding_addon.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/websecurityscanner/v1alpha/finding_addon.proto',
  package='google.cloud.websecurityscanner.v1alpha',
  syntax='proto3',
  serialized_options=b'\n+com.google.cloud.websecurityscanner.v1alphaB\021FindingAddonProtoP\001ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscanner',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;google/cloud/websecurityscanner/v1alpha/finding_addon.proto\x12\'google.cloud.websecurityscanner.v1alpha\"v\n\x0fOutdatedLibrary\x12!\n\x0clibrary_name\x18\x01 \x01(\tR\x0blibraryName\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12&\n\x0flearn_more_urls\x18\x03 \x03(\tR\rlearnMoreUrls\"Y\n\x11ViolatingResource\x12!\n\x0c\x63ontent_type\x18\x01 \x01(\tR\x0b\x63ontentType\x12!\n\x0cresource_url\x18\x02 \x01(\tR\x0bresourceUrl\"?\n\x14VulnerableParameters\x12\'\n\x0fparameter_names\x18\x01 \x03(\tR\x0eparameterNames\"\x90\x02\n\x11VulnerableHeaders\x12[\n\x07headers\x18\x01 \x03(\x0b\x32\x41.google.cloud.websecurityscanner.v1alpha.VulnerableHeaders.HeaderR\x07headers\x12j\n\x0fmissing_headers\x18\x02 \x03(\x0b\x32\x41.google.cloud.websecurityscanner.v1alpha.VulnerableHeaders.HeaderR\x0emissingHeaders\x1a\x32\n\x06Header\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"M\n\x03Xss\x12!\n\x0cstack_traces\x18\x01 \x03(\tR\x0bstackTraces\x12#\n\rerror_message\x18\x02 \x01(\tR\x0c\x65rrorMessageB\x9d\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x11\x46indingAddonProtoP\x01ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscannerb\x06proto3'
)




_OUTDATEDLIBRARY = _descriptor.Descriptor(
  name='OutdatedLibrary',
  full_name='google.cloud.websecurityscanner.v1alpha.OutdatedLibrary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='library_name', full_name='google.cloud.websecurityscanner.v1alpha.OutdatedLibrary.library_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='libraryName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='google.cloud.websecurityscanner.v1alpha.OutdatedLibrary.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='version', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='learn_more_urls', full_name='google.cloud.websecurityscanner.v1alpha.OutdatedLibrary.learn_more_urls', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='learnMoreUrls', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=104,
  serialized_end=222,
)


_VIOLATINGRESOURCE = _descriptor.Descriptor(
  name='ViolatingResource',
  full_name='google.cloud.websecurityscanner.v1alpha.ViolatingResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content_type', full_name='google.cloud.websecurityscanner.v1alpha.ViolatingResource.content_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_url', full_name='google.cloud.websecurityscanner.v1alpha.ViolatingResource.resource_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resourceUrl', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=224,
  serialized_end=313,
)


_VULNERABLEPARAMETERS = _descriptor.Descriptor(
  name='VulnerableParameters',
  full_name='google.cloud.websecurityscanner.v1alpha.VulnerableParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameter_names', full_name='google.cloud.websecurityscanner.v1alpha.VulnerableParameters.parameter_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parameterNames', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=315,
  serialized_end=378,
)


_VULNERABLEHEADERS_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='google.cloud.websecurityscanner.v1alpha.VulnerableHeaders.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.websecurityscanner.v1alpha.VulnerableHeaders.Header.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.websecurityscanner.v1alpha.VulnerableHeaders.Header.value', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=653,
)

_VULNERABLEHEADERS = _descriptor.Descriptor(
  name='VulnerableHeaders',
  full_name='google.cloud.websecurityscanner.v1alpha.VulnerableHeaders',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='headers', full_name='google.cloud.websecurityscanner.v1alpha.VulnerableHeaders.headers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='headers', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='missing_headers', full_name='google.cloud.websecurityscanner.v1alpha.VulnerableHeaders.missing_headers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='missingHeaders', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_VULNERABLEHEADERS_HEADER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=381,
  serialized_end=653,
)


_XSS = _descriptor.Descriptor(
  name='Xss',
  full_name='google.cloud.websecurityscanner.v1alpha.Xss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stack_traces', full_name='google.cloud.websecurityscanner.v1alpha.Xss.stack_traces', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stackTraces', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='google.cloud.websecurityscanner.v1alpha.Xss.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='errorMessage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=655,
  serialized_end=732,
)

_VULNERABLEHEADERS_HEADER.containing_type = _VULNERABLEHEADERS
_VULNERABLEHEADERS.fields_by_name['headers'].message_type = _VULNERABLEHEADERS_HEADER
_VULNERABLEHEADERS.fields_by_name['missing_headers'].message_type = _VULNERABLEHEADERS_HEADER
DESCRIPTOR.message_types_by_name['OutdatedLibrary'] = _OUTDATEDLIBRARY
DESCRIPTOR.message_types_by_name['ViolatingResource'] = _VIOLATINGRESOURCE
DESCRIPTOR.message_types_by_name['VulnerableParameters'] = _VULNERABLEPARAMETERS
DESCRIPTOR.message_types_by_name['VulnerableHeaders'] = _VULNERABLEHEADERS
DESCRIPTOR.message_types_by_name['Xss'] = _XSS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OutdatedLibrary = _reflection.GeneratedProtocolMessageType('OutdatedLibrary', (_message.Message,), {
  'DESCRIPTOR' : _OUTDATEDLIBRARY,
  '__module__' : 'google.cloud.websecurityscanner.v1alpha.finding_addon_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.OutdatedLibrary)
  })
_sym_db.RegisterMessage(OutdatedLibrary)

ViolatingResource = _reflection.GeneratedProtocolMessageType('ViolatingResource', (_message.Message,), {
  'DESCRIPTOR' : _VIOLATINGRESOURCE,
  '__module__' : 'google.cloud.websecurityscanner.v1alpha.finding_addon_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.ViolatingResource)
  })
_sym_db.RegisterMessage(ViolatingResource)

VulnerableParameters = _reflection.GeneratedProtocolMessageType('VulnerableParameters', (_message.Message,), {
  'DESCRIPTOR' : _VULNERABLEPARAMETERS,
  '__module__' : 'google.cloud.websecurityscanner.v1alpha.finding_addon_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.VulnerableParameters)
  })
_sym_db.RegisterMessage(VulnerableParameters)

VulnerableHeaders = _reflection.GeneratedProtocolMessageType('VulnerableHeaders', (_message.Message,), {

  'Header' : _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
    'DESCRIPTOR' : _VULNERABLEHEADERS_HEADER,
    '__module__' : 'google.cloud.websecurityscanner.v1alpha.finding_addon_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.VulnerableHeaders.Header)
    })
  ,
  'DESCRIPTOR' : _VULNERABLEHEADERS,
  '__module__' : 'google.cloud.websecurityscanner.v1alpha.finding_addon_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.VulnerableHeaders)
  })
_sym_db.RegisterMessage(VulnerableHeaders)
_sym_db.RegisterMessage(VulnerableHeaders.Header)

Xss = _reflection.GeneratedProtocolMessageType('Xss', (_message.Message,), {
  'DESCRIPTOR' : _XSS,
  '__module__' : 'google.cloud.websecurityscanner.v1alpha.finding_addon_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.Xss)
  })
_sym_db.RegisterMessage(Xss)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
