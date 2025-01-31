# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/example/endpointsapis/v1/workspace.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/example/endpointsapis/v1/workspace.proto',
  package='google.example.endpointsapis.v1',
  syntax='proto3',
  serialized_options=b'\n#com.google.example.endpointsapis.v1B\016WorkspaceProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/google/example/endpointsapis/v1/workspace.proto\x12\x1fgoogle.example.endpointsapis.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x1f\n\tWorkspace\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"k\n\x15ListWorkspacesRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\x82\x01\n\x16ListWorkspacesResponse\x12@\n\x05items\x18\x01 \x03(\x0b\x32*.google.example.endpointsapis.v1.WorkspaceR\x05items\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\")\n\x13GetWorkspaceRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"z\n\x16\x43reateWorkspaceRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12H\n\tworkspace\x18\x02 \x01(\x0b\x32*.google.example.endpointsapis.v1.WorkspaceR\tworkspace\"v\n\x16UpdateWorkspaceRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12H\n\tworkspace\x18\x02 \x01(\x0b\x32*.google.example.endpointsapis.v1.WorkspaceR\tworkspace\",\n\x16\x44\x65leteWorkspaceRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name2\x88\x07\n\nWorkspaces\x12\xb9\x01\n\x0eListWorkspaces\x12\x36.google.example.endpointsapis.v1.ListWorkspacesRequest\x1a\x37.google.example.endpointsapis.v1.ListWorkspacesResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./v1/{parent=projects/*/locations/*}/workspaces\x12\xa8\x01\n\x0cGetWorkspace\x12\x34.google.example.endpointsapis.v1.GetWorkspaceRequest\x1a*.google.example.endpointsapis.v1.Workspace\"6\x82\xd3\xe4\x93\x02\x30\x12./v1/{name=projects/*/locations/*/workspaces/*}\x12\xb9\x01\n\x0f\x43reateWorkspace\x12\x37.google.example.endpointsapis.v1.CreateWorkspaceRequest\x1a*.google.example.endpointsapis.v1.Workspace\"A\x82\xd3\xe4\x93\x02;\"./v1/{parent=projects/*/locations/*}/workspaces:\tworkspace\x12\xb9\x01\n\x0fUpdateWorkspace\x12\x37.google.example.endpointsapis.v1.UpdateWorkspaceRequest\x1a*.google.example.endpointsapis.v1.Workspace\"A\x82\xd3\xe4\x93\x02;2./v1/{name=projects/*/locations/*/Workspaces/*}:\tworkspace\x12\x9a\x01\n\x0f\x44\x65leteWorkspace\x12\x37.google.example.endpointsapis.v1.DeleteWorkspaceRequest\x1a\x16.google.protobuf.Empty\"6\x82\xd3\xe4\x93\x02\x30*./v1/{name=projects/*/locations/*/workspaces/*}B7\n#com.google.example.endpointsapis.v1B\x0eWorkspaceProtoP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_WORKSPACE = _descriptor.Descriptor(
  name='Workspace',
  full_name='google.example.endpointsapis.v1.Workspace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.endpointsapis.v1.Workspace.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=143,
  serialized_end=174,
)


_LISTWORKSPACESREQUEST = _descriptor.Descriptor(
  name='ListWorkspacesRequest',
  full_name='google.example.endpointsapis.v1.ListWorkspacesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.example.endpointsapis.v1.ListWorkspacesRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.example.endpointsapis.v1.ListWorkspacesRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.example.endpointsapis.v1.ListWorkspacesRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=283,
)


_LISTWORKSPACESRESPONSE = _descriptor.Descriptor(
  name='ListWorkspacesResponse',
  full_name='google.example.endpointsapis.v1.ListWorkspacesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='google.example.endpointsapis.v1.ListWorkspacesResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='items', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.example.endpointsapis.v1.ListWorkspacesResponse.next_page_token', index=1,
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
  serialized_start=286,
  serialized_end=416,
)


_GETWORKSPACEREQUEST = _descriptor.Descriptor(
  name='GetWorkspaceRequest',
  full_name='google.example.endpointsapis.v1.GetWorkspaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.endpointsapis.v1.GetWorkspaceRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=418,
  serialized_end=459,
)


_CREATEWORKSPACEREQUEST = _descriptor.Descriptor(
  name='CreateWorkspaceRequest',
  full_name='google.example.endpointsapis.v1.CreateWorkspaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.example.endpointsapis.v1.CreateWorkspaceRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workspace', full_name='google.example.endpointsapis.v1.CreateWorkspaceRequest.workspace', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='workspace', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=461,
  serialized_end=583,
)


_UPDATEWORKSPACEREQUEST = _descriptor.Descriptor(
  name='UpdateWorkspaceRequest',
  full_name='google.example.endpointsapis.v1.UpdateWorkspaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.endpointsapis.v1.UpdateWorkspaceRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workspace', full_name='google.example.endpointsapis.v1.UpdateWorkspaceRequest.workspace', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='workspace', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=585,
  serialized_end=703,
)


_DELETEWORKSPACEREQUEST = _descriptor.Descriptor(
  name='DeleteWorkspaceRequest',
  full_name='google.example.endpointsapis.v1.DeleteWorkspaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.endpointsapis.v1.DeleteWorkspaceRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=705,
  serialized_end=749,
)

_LISTWORKSPACESRESPONSE.fields_by_name['items'].message_type = _WORKSPACE
_CREATEWORKSPACEREQUEST.fields_by_name['workspace'].message_type = _WORKSPACE
_UPDATEWORKSPACEREQUEST.fields_by_name['workspace'].message_type = _WORKSPACE
DESCRIPTOR.message_types_by_name['Workspace'] = _WORKSPACE
DESCRIPTOR.message_types_by_name['ListWorkspacesRequest'] = _LISTWORKSPACESREQUEST
DESCRIPTOR.message_types_by_name['ListWorkspacesResponse'] = _LISTWORKSPACESRESPONSE
DESCRIPTOR.message_types_by_name['GetWorkspaceRequest'] = _GETWORKSPACEREQUEST
DESCRIPTOR.message_types_by_name['CreateWorkspaceRequest'] = _CREATEWORKSPACEREQUEST
DESCRIPTOR.message_types_by_name['UpdateWorkspaceRequest'] = _UPDATEWORKSPACEREQUEST
DESCRIPTOR.message_types_by_name['DeleteWorkspaceRequest'] = _DELETEWORKSPACEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Workspace = _reflection.GeneratedProtocolMessageType('Workspace', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACE,
  '__module__' : 'google.example.endpointsapis.v1.workspace_pb2'
  # @@protoc_insertion_point(class_scope:google.example.endpointsapis.v1.Workspace)
  })
_sym_db.RegisterMessage(Workspace)

ListWorkspacesRequest = _reflection.GeneratedProtocolMessageType('ListWorkspacesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTWORKSPACESREQUEST,
  '__module__' : 'google.example.endpointsapis.v1.workspace_pb2'
  # @@protoc_insertion_point(class_scope:google.example.endpointsapis.v1.ListWorkspacesRequest)
  })
_sym_db.RegisterMessage(ListWorkspacesRequest)

ListWorkspacesResponse = _reflection.GeneratedProtocolMessageType('ListWorkspacesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTWORKSPACESRESPONSE,
  '__module__' : 'google.example.endpointsapis.v1.workspace_pb2'
  # @@protoc_insertion_point(class_scope:google.example.endpointsapis.v1.ListWorkspacesResponse)
  })
_sym_db.RegisterMessage(ListWorkspacesResponse)

GetWorkspaceRequest = _reflection.GeneratedProtocolMessageType('GetWorkspaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETWORKSPACEREQUEST,
  '__module__' : 'google.example.endpointsapis.v1.workspace_pb2'
  # @@protoc_insertion_point(class_scope:google.example.endpointsapis.v1.GetWorkspaceRequest)
  })
_sym_db.RegisterMessage(GetWorkspaceRequest)

CreateWorkspaceRequest = _reflection.GeneratedProtocolMessageType('CreateWorkspaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWORKSPACEREQUEST,
  '__module__' : 'google.example.endpointsapis.v1.workspace_pb2'
  # @@protoc_insertion_point(class_scope:google.example.endpointsapis.v1.CreateWorkspaceRequest)
  })
_sym_db.RegisterMessage(CreateWorkspaceRequest)

UpdateWorkspaceRequest = _reflection.GeneratedProtocolMessageType('UpdateWorkspaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEWORKSPACEREQUEST,
  '__module__' : 'google.example.endpointsapis.v1.workspace_pb2'
  # @@protoc_insertion_point(class_scope:google.example.endpointsapis.v1.UpdateWorkspaceRequest)
  })
_sym_db.RegisterMessage(UpdateWorkspaceRequest)

DeleteWorkspaceRequest = _reflection.GeneratedProtocolMessageType('DeleteWorkspaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEWORKSPACEREQUEST,
  '__module__' : 'google.example.endpointsapis.v1.workspace_pb2'
  # @@protoc_insertion_point(class_scope:google.example.endpointsapis.v1.DeleteWorkspaceRequest)
  })
_sym_db.RegisterMessage(DeleteWorkspaceRequest)


DESCRIPTOR._options = None

_WORKSPACES = _descriptor.ServiceDescriptor(
  name='Workspaces',
  full_name='google.example.endpointsapis.v1.Workspaces',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=752,
  serialized_end=1656,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListWorkspaces',
    full_name='google.example.endpointsapis.v1.Workspaces.ListWorkspaces',
    index=0,
    containing_service=None,
    input_type=_LISTWORKSPACESREQUEST,
    output_type=_LISTWORKSPACESRESPONSE,
    serialized_options=b'\202\323\344\223\0020\022./v1/{parent=projects/*/locations/*}/workspaces',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetWorkspace',
    full_name='google.example.endpointsapis.v1.Workspaces.GetWorkspace',
    index=1,
    containing_service=None,
    input_type=_GETWORKSPACEREQUEST,
    output_type=_WORKSPACE,
    serialized_options=b'\202\323\344\223\0020\022./v1/{name=projects/*/locations/*/workspaces/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateWorkspace',
    full_name='google.example.endpointsapis.v1.Workspaces.CreateWorkspace',
    index=2,
    containing_service=None,
    input_type=_CREATEWORKSPACEREQUEST,
    output_type=_WORKSPACE,
    serialized_options=b'\202\323\344\223\002;\"./v1/{parent=projects/*/locations/*}/workspaces:\tworkspace',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateWorkspace',
    full_name='google.example.endpointsapis.v1.Workspaces.UpdateWorkspace',
    index=3,
    containing_service=None,
    input_type=_UPDATEWORKSPACEREQUEST,
    output_type=_WORKSPACE,
    serialized_options=b'\202\323\344\223\002;2./v1/{name=projects/*/locations/*/Workspaces/*}:\tworkspace',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteWorkspace',
    full_name='google.example.endpointsapis.v1.Workspaces.DeleteWorkspace',
    index=4,
    containing_service=None,
    input_type=_DELETEWORKSPACEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\0020*./v1/{name=projects/*/locations/*/workspaces/*}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKSPACES)

DESCRIPTOR.services_by_name['Workspaces'] = _WORKSPACES

# @@protoc_insertion_point(module_scope)
