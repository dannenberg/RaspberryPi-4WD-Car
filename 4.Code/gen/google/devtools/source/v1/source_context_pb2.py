# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/source/v1/source_context.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/source/v1/source_context.proto',
  package='google.devtools.source.v1',
  syntax='proto3',
  serialized_options=b'\n\035com.google.devtools.source.v1B\022SourceContextProtoP\001Z?google.golang.org/genproto/googleapis/devtools/source/v1;source\370\001\001\252\002\037Google.Cloud.DevTools.Source.V1\312\002\037Google\\Cloud\\DevTools\\Source\\V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.google/devtools/source/v1/source_context.proto\x12\x19google.devtools.source.v1\x1a\x1cgoogle/api/annotations.proto\"\xdc\x02\n\rSourceContext\x12R\n\ncloud_repo\x18\x01 \x01(\x0b\x32\x31.google.devtools.source.v1.CloudRepoSourceContextH\x00R\tcloudRepo\x12\x61\n\x0f\x63loud_workspace\x18\x02 \x01(\x0b\x32\x36.google.devtools.source.v1.CloudWorkspaceSourceContextH\x00R\x0e\x63loudWorkspace\x12H\n\x06gerrit\x18\x03 \x01(\x0b\x32..google.devtools.source.v1.GerritSourceContextH\x00R\x06gerrit\x12?\n\x03git\x18\x06 \x01(\x0b\x32+.google.devtools.source.v1.GitSourceContextH\x00R\x03gitB\t\n\x07\x63ontext\"\xec\x01\n\x15\x45xtendedSourceContext\x12\x42\n\x07\x63ontext\x18\x01 \x01(\x0b\x32(.google.devtools.source.v1.SourceContextR\x07\x63ontext\x12T\n\x06labels\x18\x02 \x03(\x0b\x32<.google.devtools.source.v1.ExtendedSourceContext.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x98\x01\n\x0c\x41liasContext\x12@\n\x04kind\x18\x01 \x01(\x0e\x32,.google.devtools.source.v1.AliasContext.KindR\x04kind\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"2\n\x04Kind\x12\x07\n\x03\x41NY\x10\x00\x12\t\n\x05\x46IXED\x10\x01\x12\x0b\n\x07MOVABLE\x10\x02\x12\t\n\x05OTHER\x10\x04\"\xf8\x01\n\x16\x43loudRepoSourceContext\x12:\n\x07repo_id\x18\x01 \x01(\x0b\x32!.google.devtools.source.v1.RepoIdR\x06repoId\x12!\n\x0brevision_id\x18\x02 \x01(\tH\x00R\nrevisionId\x12#\n\nalias_name\x18\x03 \x01(\tB\x02\x18\x01H\x00R\taliasName\x12N\n\ralias_context\x18\x04 \x01(\x0b\x32\'.google.devtools.source.v1.AliasContextH\x00R\x0c\x61liasContextB\n\n\x08revision\"\x8e\x01\n\x1b\x43loudWorkspaceSourceContext\x12N\n\x0cworkspace_id\x18\x01 \x01(\x0b\x32+.google.devtools.source.v1.CloudWorkspaceIdR\x0bworkspaceId\x12\x1f\n\x0bsnapshot_id\x18\x02 \x01(\tR\nsnapshotId\"\xfb\x01\n\x13GerritSourceContext\x12\x19\n\x08host_uri\x18\x01 \x01(\tR\x07hostUri\x12%\n\x0egerrit_project\x18\x02 \x01(\tR\rgerritProject\x12!\n\x0brevision_id\x18\x03 \x01(\tH\x00R\nrevisionId\x12#\n\nalias_name\x18\x04 \x01(\tB\x02\x18\x01H\x00R\taliasName\x12N\n\ralias_context\x18\x05 \x01(\x0b\x32\'.google.devtools.source.v1.AliasContextH\x00R\x0c\x61liasContextB\n\n\x08revision\"E\n\x10GitSourceContext\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x1f\n\x0brevision_id\x18\x02 \x01(\tR\nrevisionId\"v\n\x06RepoId\x12R\n\x0fproject_repo_id\x18\x01 \x01(\x0b\x32(.google.devtools.source.v1.ProjectRepoIdH\x00R\rprojectRepoId\x12\x12\n\x03uid\x18\x02 \x01(\tH\x00R\x03uidB\x04\n\x02id\"K\n\rProjectRepoId\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x1b\n\trepo_name\x18\x02 \x01(\tR\x08repoName\"b\n\x10\x43loudWorkspaceId\x12:\n\x07repo_id\x18\x01 \x01(\x0b\x32!.google.devtools.source.v1.RepoIdR\x06repoId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04nameB\xbd\x01\n\x1d\x63om.google.devtools.source.v1B\x12SourceContextProtoP\x01Z?google.golang.org/genproto/googleapis/devtools/source/v1;source\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.DevTools.Source.V1\xca\x02\x1fGoogle\\Cloud\\DevTools\\Source\\V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ALIASCONTEXT_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='google.devtools.source.v1.AliasContext.Kind',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIXED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOVABLE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=800,
  serialized_end=850,
)
_sym_db.RegisterEnumDescriptor(_ALIASCONTEXT_KIND)


_SOURCECONTEXT = _descriptor.Descriptor(
  name='SourceContext',
  full_name='google.devtools.source.v1.SourceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_repo', full_name='google.devtools.source.v1.SourceContext.cloud_repo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='cloudRepo', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cloud_workspace', full_name='google.devtools.source.v1.SourceContext.cloud_workspace', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='cloudWorkspace', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gerrit', full_name='google.devtools.source.v1.SourceContext.gerrit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gerrit', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='git', full_name='google.devtools.source.v1.SourceContext.git', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='git', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='context', full_name='google.devtools.source.v1.SourceContext.context',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=108,
  serialized_end=456,
)


_EXTENDEDSOURCECONTEXT_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.devtools.source.v1.ExtendedSourceContext.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.devtools.source.v1.ExtendedSourceContext.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.devtools.source.v1.ExtendedSourceContext.LabelsEntry.value', index=1,
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
  serialized_start=638,
  serialized_end=695,
)

_EXTENDEDSOURCECONTEXT = _descriptor.Descriptor(
  name='ExtendedSourceContext',
  full_name='google.devtools.source.v1.ExtendedSourceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='google.devtools.source.v1.ExtendedSourceContext.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='context', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.devtools.source.v1.ExtendedSourceContext.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EXTENDEDSOURCECONTEXT_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=459,
  serialized_end=695,
)


_ALIASCONTEXT = _descriptor.Descriptor(
  name='AliasContext',
  full_name='google.devtools.source.v1.AliasContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='google.devtools.source.v1.AliasContext.kind', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='kind', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.source.v1.AliasContext.name', index=1,
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
    _ALIASCONTEXT_KIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=698,
  serialized_end=850,
)


_CLOUDREPOSOURCECONTEXT = _descriptor.Descriptor(
  name='CloudRepoSourceContext',
  full_name='google.devtools.source.v1.CloudRepoSourceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='repo_id', full_name='google.devtools.source.v1.CloudRepoSourceContext.repo_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='repoId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision_id', full_name='google.devtools.source.v1.CloudRepoSourceContext.revision_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='revisionId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alias_name', full_name='google.devtools.source.v1.CloudRepoSourceContext.alias_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', json_name='aliasName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alias_context', full_name='google.devtools.source.v1.CloudRepoSourceContext.alias_context', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='aliasContext', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='revision', full_name='google.devtools.source.v1.CloudRepoSourceContext.revision',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=853,
  serialized_end=1101,
)


_CLOUDWORKSPACESOURCECONTEXT = _descriptor.Descriptor(
  name='CloudWorkspaceSourceContext',
  full_name='google.devtools.source.v1.CloudWorkspaceSourceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='workspace_id', full_name='google.devtools.source.v1.CloudWorkspaceSourceContext.workspace_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='workspaceId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='google.devtools.source.v1.CloudWorkspaceSourceContext.snapshot_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='snapshotId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1104,
  serialized_end=1246,
)


_GERRITSOURCECONTEXT = _descriptor.Descriptor(
  name='GerritSourceContext',
  full_name='google.devtools.source.v1.GerritSourceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_uri', full_name='google.devtools.source.v1.GerritSourceContext.host_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hostUri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gerrit_project', full_name='google.devtools.source.v1.GerritSourceContext.gerrit_project', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gerritProject', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision_id', full_name='google.devtools.source.v1.GerritSourceContext.revision_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='revisionId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alias_name', full_name='google.devtools.source.v1.GerritSourceContext.alias_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', json_name='aliasName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alias_context', full_name='google.devtools.source.v1.GerritSourceContext.alias_context', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='aliasContext', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='revision', full_name='google.devtools.source.v1.GerritSourceContext.revision',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1249,
  serialized_end=1500,
)


_GITSOURCECONTEXT = _descriptor.Descriptor(
  name='GitSourceContext',
  full_name='google.devtools.source.v1.GitSourceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='google.devtools.source.v1.GitSourceContext.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='url', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision_id', full_name='google.devtools.source.v1.GitSourceContext.revision_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='revisionId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1502,
  serialized_end=1571,
)


_REPOID = _descriptor.Descriptor(
  name='RepoId',
  full_name='google.devtools.source.v1.RepoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_repo_id', full_name='google.devtools.source.v1.RepoId.project_repo_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='projectRepoId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uid', full_name='google.devtools.source.v1.RepoId.uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='uid', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='id', full_name='google.devtools.source.v1.RepoId.id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1573,
  serialized_end=1691,
)


_PROJECTREPOID = _descriptor.Descriptor(
  name='ProjectRepoId',
  full_name='google.devtools.source.v1.ProjectRepoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.source.v1.ProjectRepoId.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='projectId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repo_name', full_name='google.devtools.source.v1.ProjectRepoId.repo_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='repoName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1693,
  serialized_end=1768,
)


_CLOUDWORKSPACEID = _descriptor.Descriptor(
  name='CloudWorkspaceId',
  full_name='google.devtools.source.v1.CloudWorkspaceId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='repo_id', full_name='google.devtools.source.v1.CloudWorkspaceId.repo_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='repoId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.source.v1.CloudWorkspaceId.name', index=1,
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
  serialized_start=1770,
  serialized_end=1868,
)

_SOURCECONTEXT.fields_by_name['cloud_repo'].message_type = _CLOUDREPOSOURCECONTEXT
_SOURCECONTEXT.fields_by_name['cloud_workspace'].message_type = _CLOUDWORKSPACESOURCECONTEXT
_SOURCECONTEXT.fields_by_name['gerrit'].message_type = _GERRITSOURCECONTEXT
_SOURCECONTEXT.fields_by_name['git'].message_type = _GITSOURCECONTEXT
_SOURCECONTEXT.oneofs_by_name['context'].fields.append(
  _SOURCECONTEXT.fields_by_name['cloud_repo'])
_SOURCECONTEXT.fields_by_name['cloud_repo'].containing_oneof = _SOURCECONTEXT.oneofs_by_name['context']
_SOURCECONTEXT.oneofs_by_name['context'].fields.append(
  _SOURCECONTEXT.fields_by_name['cloud_workspace'])
_SOURCECONTEXT.fields_by_name['cloud_workspace'].containing_oneof = _SOURCECONTEXT.oneofs_by_name['context']
_SOURCECONTEXT.oneofs_by_name['context'].fields.append(
  _SOURCECONTEXT.fields_by_name['gerrit'])
_SOURCECONTEXT.fields_by_name['gerrit'].containing_oneof = _SOURCECONTEXT.oneofs_by_name['context']
_SOURCECONTEXT.oneofs_by_name['context'].fields.append(
  _SOURCECONTEXT.fields_by_name['git'])
_SOURCECONTEXT.fields_by_name['git'].containing_oneof = _SOURCECONTEXT.oneofs_by_name['context']
_EXTENDEDSOURCECONTEXT_LABELSENTRY.containing_type = _EXTENDEDSOURCECONTEXT
_EXTENDEDSOURCECONTEXT.fields_by_name['context'].message_type = _SOURCECONTEXT
_EXTENDEDSOURCECONTEXT.fields_by_name['labels'].message_type = _EXTENDEDSOURCECONTEXT_LABELSENTRY
_ALIASCONTEXT.fields_by_name['kind'].enum_type = _ALIASCONTEXT_KIND
_ALIASCONTEXT_KIND.containing_type = _ALIASCONTEXT
_CLOUDREPOSOURCECONTEXT.fields_by_name['repo_id'].message_type = _REPOID
_CLOUDREPOSOURCECONTEXT.fields_by_name['alias_context'].message_type = _ALIASCONTEXT
_CLOUDREPOSOURCECONTEXT.oneofs_by_name['revision'].fields.append(
  _CLOUDREPOSOURCECONTEXT.fields_by_name['revision_id'])
_CLOUDREPOSOURCECONTEXT.fields_by_name['revision_id'].containing_oneof = _CLOUDREPOSOURCECONTEXT.oneofs_by_name['revision']
_CLOUDREPOSOURCECONTEXT.oneofs_by_name['revision'].fields.append(
  _CLOUDREPOSOURCECONTEXT.fields_by_name['alias_name'])
_CLOUDREPOSOURCECONTEXT.fields_by_name['alias_name'].containing_oneof = _CLOUDREPOSOURCECONTEXT.oneofs_by_name['revision']
_CLOUDREPOSOURCECONTEXT.oneofs_by_name['revision'].fields.append(
  _CLOUDREPOSOURCECONTEXT.fields_by_name['alias_context'])
_CLOUDREPOSOURCECONTEXT.fields_by_name['alias_context'].containing_oneof = _CLOUDREPOSOURCECONTEXT.oneofs_by_name['revision']
_CLOUDWORKSPACESOURCECONTEXT.fields_by_name['workspace_id'].message_type = _CLOUDWORKSPACEID
_GERRITSOURCECONTEXT.fields_by_name['alias_context'].message_type = _ALIASCONTEXT
_GERRITSOURCECONTEXT.oneofs_by_name['revision'].fields.append(
  _GERRITSOURCECONTEXT.fields_by_name['revision_id'])
_GERRITSOURCECONTEXT.fields_by_name['revision_id'].containing_oneof = _GERRITSOURCECONTEXT.oneofs_by_name['revision']
_GERRITSOURCECONTEXT.oneofs_by_name['revision'].fields.append(
  _GERRITSOURCECONTEXT.fields_by_name['alias_name'])
_GERRITSOURCECONTEXT.fields_by_name['alias_name'].containing_oneof = _GERRITSOURCECONTEXT.oneofs_by_name['revision']
_GERRITSOURCECONTEXT.oneofs_by_name['revision'].fields.append(
  _GERRITSOURCECONTEXT.fields_by_name['alias_context'])
_GERRITSOURCECONTEXT.fields_by_name['alias_context'].containing_oneof = _GERRITSOURCECONTEXT.oneofs_by_name['revision']
_REPOID.fields_by_name['project_repo_id'].message_type = _PROJECTREPOID
_REPOID.oneofs_by_name['id'].fields.append(
  _REPOID.fields_by_name['project_repo_id'])
_REPOID.fields_by_name['project_repo_id'].containing_oneof = _REPOID.oneofs_by_name['id']
_REPOID.oneofs_by_name['id'].fields.append(
  _REPOID.fields_by_name['uid'])
_REPOID.fields_by_name['uid'].containing_oneof = _REPOID.oneofs_by_name['id']
_CLOUDWORKSPACEID.fields_by_name['repo_id'].message_type = _REPOID
DESCRIPTOR.message_types_by_name['SourceContext'] = _SOURCECONTEXT
DESCRIPTOR.message_types_by_name['ExtendedSourceContext'] = _EXTENDEDSOURCECONTEXT
DESCRIPTOR.message_types_by_name['AliasContext'] = _ALIASCONTEXT
DESCRIPTOR.message_types_by_name['CloudRepoSourceContext'] = _CLOUDREPOSOURCECONTEXT
DESCRIPTOR.message_types_by_name['CloudWorkspaceSourceContext'] = _CLOUDWORKSPACESOURCECONTEXT
DESCRIPTOR.message_types_by_name['GerritSourceContext'] = _GERRITSOURCECONTEXT
DESCRIPTOR.message_types_by_name['GitSourceContext'] = _GITSOURCECONTEXT
DESCRIPTOR.message_types_by_name['RepoId'] = _REPOID
DESCRIPTOR.message_types_by_name['ProjectRepoId'] = _PROJECTREPOID
DESCRIPTOR.message_types_by_name['CloudWorkspaceId'] = _CLOUDWORKSPACEID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SourceContext = _reflection.GeneratedProtocolMessageType('SourceContext', (_message.Message,), {
  'DESCRIPTOR' : _SOURCECONTEXT,
  '__module__' : 'google.devtools.source.v1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.source.v1.SourceContext)
  })
_sym_db.RegisterMessage(SourceContext)

ExtendedSourceContext = _reflection.GeneratedProtocolMessageType('ExtendedSourceContext', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXTENDEDSOURCECONTEXT_LABELSENTRY,
    '__module__' : 'google.devtools.source.v1.source_context_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.source.v1.ExtendedSourceContext.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _EXTENDEDSOURCECONTEXT,
  '__module__' : 'google.devtools.source.v1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.source.v1.ExtendedSourceContext)
  })
_sym_db.RegisterMessage(ExtendedSourceContext)
_sym_db.RegisterMessage(ExtendedSourceContext.LabelsEntry)

AliasContext = _reflection.GeneratedProtocolMessageType('AliasContext', (_message.Message,), {
  'DESCRIPTOR' : _ALIASCONTEXT,
  '__module__' : 'google.devtools.source.v1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.source.v1.AliasContext)
  })
_sym_db.RegisterMessage(AliasContext)

CloudRepoSourceContext = _reflection.GeneratedProtocolMessageType('CloudRepoSourceContext', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDREPOSOURCECONTEXT,
  '__module__' : 'google.devtools.source.v1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.source.v1.CloudRepoSourceContext)
  })
_sym_db.RegisterMessage(CloudRepoSourceContext)

CloudWorkspaceSourceContext = _reflection.GeneratedProtocolMessageType('CloudWorkspaceSourceContext', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDWORKSPACESOURCECONTEXT,
  '__module__' : 'google.devtools.source.v1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.source.v1.CloudWorkspaceSourceContext)
  })
_sym_db.RegisterMessage(CloudWorkspaceSourceContext)

GerritSourceContext = _reflection.GeneratedProtocolMessageType('GerritSourceContext', (_message.Message,), {
  'DESCRIPTOR' : _GERRITSOURCECONTEXT,
  '__module__' : 'google.devtools.source.v1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.source.v1.GerritSourceContext)
  })
_sym_db.RegisterMessage(GerritSourceContext)

GitSourceContext = _reflection.GeneratedProtocolMessageType('GitSourceContext', (_message.Message,), {
  'DESCRIPTOR' : _GITSOURCECONTEXT,
  '__module__' : 'google.devtools.source.v1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.source.v1.GitSourceContext)
  })
_sym_db.RegisterMessage(GitSourceContext)

RepoId = _reflection.GeneratedProtocolMessageType('RepoId', (_message.Message,), {
  'DESCRIPTOR' : _REPOID,
  '__module__' : 'google.devtools.source.v1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.source.v1.RepoId)
  })
_sym_db.RegisterMessage(RepoId)

ProjectRepoId = _reflection.GeneratedProtocolMessageType('ProjectRepoId', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTREPOID,
  '__module__' : 'google.devtools.source.v1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.source.v1.ProjectRepoId)
  })
_sym_db.RegisterMessage(ProjectRepoId)

CloudWorkspaceId = _reflection.GeneratedProtocolMessageType('CloudWorkspaceId', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDWORKSPACEID,
  '__module__' : 'google.devtools.source.v1.source_context_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.source.v1.CloudWorkspaceId)
  })
_sym_db.RegisterMessage(CloudWorkspaceId)


DESCRIPTOR._options = None
_EXTENDEDSOURCECONTEXT_LABELSENTRY._options = None
_CLOUDREPOSOURCECONTEXT.fields_by_name['alias_name']._options = None
_GERRITSOURCECONTEXT.fields_by_name['alias_name']._options = None
# @@protoc_insertion_point(module_scope)
