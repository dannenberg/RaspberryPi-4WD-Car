# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/asset/v1p7beta1/assets.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.orgpolicy.v1 import orgpolicy_pb2 as google_dot_cloud_dot_orgpolicy_dot_v1_dot_orgpolicy__pb2
from google.cloud.osconfig.v1 import inventory_pb2 as google_dot_cloud_dot_osconfig_dot_v1_dot_inventory__pb2
from google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.identity.accesscontextmanager.v1 import access_level_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2
from google.identity.accesscontextmanager.v1 import access_policy_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2
from google.identity.accesscontextmanager.v1 import service_perimeter_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/asset/v1p7beta1/assets.proto',
  package='google.cloud.asset.v1p7beta1',
  syntax='proto3',
  serialized_options=b'\n com.google.cloud.asset.v1p7beta1B\nAssetProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/asset/v1p7beta1;asset\370\001\001\252\002\034Google.Cloud.Asset.V1P7Beta1\312\002\034Google\\Cloud\\Asset\\V1p7beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)google/cloud/asset/v1p7beta1/assets.proto\x12\x1cgoogle.cloud.asset.v1p7beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/orgpolicy/v1/orgpolicy.proto\x1a(google/cloud/osconfig/v1/inventory.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a:google/identity/accesscontextmanager/v1/access_level.proto\x1a;google/identity/accesscontextmanager/v1/access_policy.proto\x1a?google/identity/accesscontextmanager/v1/service_perimeter.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8a\x06\n\x05\x41sset\x12;\n\x0bupdate_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\nasset_type\x18\x02 \x01(\tR\tassetType\x12\x42\n\x08resource\x18\x03 \x01(\x0b\x32&.google.cloud.asset.v1p7beta1.ResourceR\x08resource\x12\x34\n\niam_policy\x18\x04 \x01(\x0b\x32\x15.google.iam.v1.PolicyR\tiamPolicy\x12@\n\norg_policy\x18\x06 \x03(\x0b\x32!.google.cloud.orgpolicy.v1.PolicyR\torgPolicy\x12\\\n\raccess_policy\x18\x07 \x01(\x0b\x32\x35.google.identity.accesscontextmanager.v1.AccessPolicyH\x00R\x0c\x61\x63\x63\x65ssPolicy\x12Y\n\x0c\x61\x63\x63\x65ss_level\x18\x08 \x01(\x0b\x32\x34.google.identity.accesscontextmanager.v1.AccessLevelH\x00R\x0b\x61\x63\x63\x65ssLevel\x12h\n\x11service_perimeter\x18\t \x01(\x0b\x32\x39.google.identity.accesscontextmanager.v1.ServicePerimeterH\x00R\x10servicePerimeter\x12R\n\x0erelated_assets\x18\r \x01(\x0b\x32+.google.cloud.asset.v1p7beta1.RelatedAssetsR\rrelatedAssets\x12\x1c\n\tancestors\x18\n \x03(\tR\tancestors:\'\xea\x41$\n\x1f\x63loudasset.googleapis.com/Asset\x12\x01*B\x17\n\x15\x61\x63\x63\x65ss_context_policy\"\x85\x02\n\x08Resource\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12\x34\n\x16\x64iscovery_document_uri\x18\x02 \x01(\tR\x14\x64iscoveryDocumentUri\x12%\n\x0e\x64iscovery_name\x18\x03 \x01(\tR\rdiscoveryName\x12!\n\x0cresource_url\x18\x04 \x01(\tR\x0bresourceUrl\x12\x16\n\x06parent\x18\x05 \x01(\tR\x06parent\x12+\n\x04\x64\x61ta\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructR\x04\x64\x61ta\x12\x1a\n\x08location\x18\x08 \x01(\tR\x08location\"\xc2\x01\n\rRelatedAssets\x12m\n\x17relationship_attributes\x18\x01 \x01(\x0b\x32\x34.google.cloud.asset.v1p7beta1.RelationshipAttributesR\x16relationshipAttributes\x12\x42\n\x06\x61ssets\x18\x02 \x03(\x0b\x32*.google.cloud.asset.v1p7beta1.RelatedAssetR\x06\x61ssets\"\xa8\x01\n\x16RelationshipAttributes\x12\x12\n\x04type\x18\x04 \x01(\tR\x04type\x12\x30\n\x14source_resource_type\x18\x01 \x01(\tR\x12sourceResourceType\x12\x30\n\x14target_resource_type\x18\x02 \x01(\tR\x12targetResourceType\x12\x16\n\x06\x61\x63tion\x18\x03 \x01(\tR\x06\x61\x63tion\"\x87\x01\n\x0cRelatedAsset\x12:\n\x05\x61sset\x18\x01 \x01(\tB$\xfa\x41!\n\x1f\x63loudasset.googleapis.com/AssetR\x05\x61sset\x12\x1d\n\nasset_type\x18\x02 \x01(\tR\tassetType\x12\x1c\n\tancestors\x18\x03 \x03(\tR\tancestorsB\xb4\x01\n com.google.cloud.asset.v1p7beta1B\nAssetProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/asset/v1p7beta1;asset\xf8\x01\x01\xaa\x02\x1cGoogle.Cloud.Asset.V1P7Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p7beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_orgpolicy_dot_v1_dot_orgpolicy__pb2.DESCRIPTOR,google_dot_cloud_dot_osconfig_dot_v1_dot_inventory__pb2.DESCRIPTOR,google_dot_iam_dot_v1_dot_policy__pb2.DESCRIPTOR,google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2.DESCRIPTOR,google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2.DESCRIPTOR,google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='google.cloud.asset.v1p7beta1.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.cloud.asset.v1p7beta1.Asset.update_time', index=0,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='updateTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.asset.v1p7beta1.Asset.name', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset_type', full_name='google.cloud.asset.v1p7beta1.Asset.asset_type', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='assetType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='google.cloud.asset.v1p7beta1.Asset.resource', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resource', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iam_policy', full_name='google.cloud.asset.v1p7beta1.Asset.iam_policy', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='iamPolicy', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='org_policy', full_name='google.cloud.asset.v1p7beta1.Asset.org_policy', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='orgPolicy', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_policy', full_name='google.cloud.asset.v1p7beta1.Asset.access_policy', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='accessPolicy', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_level', full_name='google.cloud.asset.v1p7beta1.Asset.access_level', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='accessLevel', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_perimeter', full_name='google.cloud.asset.v1p7beta1.Asset.service_perimeter', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='servicePerimeter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='related_assets', full_name='google.cloud.asset.v1p7beta1.Asset.related_assets', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='relatedAssets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ancestors', full_name='google.cloud.asset.v1p7beta1.Asset.ancestors', index=10,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ancestors', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A$\n\037cloudasset.googleapis.com/Asset\022\001*',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='access_context_policy', full_name='google.cloud.asset.v1p7beta1.Asset.access_context_policy',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=522,
  serialized_end=1300,
)


_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='google.cloud.asset.v1p7beta1.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='google.cloud.asset.v1p7beta1.Resource.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='version', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='discovery_document_uri', full_name='google.cloud.asset.v1p7beta1.Resource.discovery_document_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='discoveryDocumentUri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='discovery_name', full_name='google.cloud.asset.v1p7beta1.Resource.discovery_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='discoveryName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_url', full_name='google.cloud.asset.v1p7beta1.Resource.resource_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resourceUrl', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.asset.v1p7beta1.Resource.parent', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='google.cloud.asset.v1p7beta1.Resource.data', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='data', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='google.cloud.asset.v1p7beta1.Resource.location', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='location', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1303,
  serialized_end=1564,
)


_RELATEDASSETS = _descriptor.Descriptor(
  name='RelatedAssets',
  full_name='google.cloud.asset.v1p7beta1.RelatedAssets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='relationship_attributes', full_name='google.cloud.asset.v1p7beta1.RelatedAssets.relationship_attributes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='relationshipAttributes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assets', full_name='google.cloud.asset.v1p7beta1.RelatedAssets.assets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='assets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1567,
  serialized_end=1761,
)


_RELATIONSHIPATTRIBUTES = _descriptor.Descriptor(
  name='RelationshipAttributes',
  full_name='google.cloud.asset.v1p7beta1.RelationshipAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='google.cloud.asset.v1p7beta1.RelationshipAttributes.type', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_resource_type', full_name='google.cloud.asset.v1p7beta1.RelationshipAttributes.source_resource_type', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sourceResourceType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_resource_type', full_name='google.cloud.asset.v1p7beta1.RelationshipAttributes.target_resource_type', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='targetResourceType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='google.cloud.asset.v1p7beta1.RelationshipAttributes.action', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='action', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1764,
  serialized_end=1932,
)


_RELATEDASSET = _descriptor.Descriptor(
  name='RelatedAsset',
  full_name='google.cloud.asset.v1p7beta1.RelatedAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset', full_name='google.cloud.asset.v1p7beta1.RelatedAsset.asset', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A!\n\037cloudasset.googleapis.com/Asset', json_name='asset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset_type', full_name='google.cloud.asset.v1p7beta1.RelatedAsset.asset_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='assetType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ancestors', full_name='google.cloud.asset.v1p7beta1.RelatedAsset.ancestors', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ancestors', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1935,
  serialized_end=2070,
)

_ASSET.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ASSET.fields_by_name['resource'].message_type = _RESOURCE
_ASSET.fields_by_name['iam_policy'].message_type = google_dot_iam_dot_v1_dot_policy__pb2._POLICY
_ASSET.fields_by_name['org_policy'].message_type = google_dot_cloud_dot_orgpolicy_dot_v1_dot_orgpolicy__pb2._POLICY
_ASSET.fields_by_name['access_policy'].message_type = google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2._ACCESSPOLICY
_ASSET.fields_by_name['access_level'].message_type = google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2._ACCESSLEVEL
_ASSET.fields_by_name['service_perimeter'].message_type = google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2._SERVICEPERIMETER
_ASSET.fields_by_name['related_assets'].message_type = _RELATEDASSETS
_ASSET.oneofs_by_name['access_context_policy'].fields.append(
  _ASSET.fields_by_name['access_policy'])
_ASSET.fields_by_name['access_policy'].containing_oneof = _ASSET.oneofs_by_name['access_context_policy']
_ASSET.oneofs_by_name['access_context_policy'].fields.append(
  _ASSET.fields_by_name['access_level'])
_ASSET.fields_by_name['access_level'].containing_oneof = _ASSET.oneofs_by_name['access_context_policy']
_ASSET.oneofs_by_name['access_context_policy'].fields.append(
  _ASSET.fields_by_name['service_perimeter'])
_ASSET.fields_by_name['service_perimeter'].containing_oneof = _ASSET.oneofs_by_name['access_context_policy']
_RESOURCE.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RELATEDASSETS.fields_by_name['relationship_attributes'].message_type = _RELATIONSHIPATTRIBUTES
_RELATEDASSETS.fields_by_name['assets'].message_type = _RELATEDASSET
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
DESCRIPTOR.message_types_by_name['RelatedAssets'] = _RELATEDASSETS
DESCRIPTOR.message_types_by_name['RelationshipAttributes'] = _RELATIONSHIPATTRIBUTES
DESCRIPTOR.message_types_by_name['RelatedAsset'] = _RELATEDASSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {
  'DESCRIPTOR' : _ASSET,
  '__module__' : 'google.cloud.asset.v1p7beta1.assets_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p7beta1.Asset)
  })
_sym_db.RegisterMessage(Asset)

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCE,
  '__module__' : 'google.cloud.asset.v1p7beta1.assets_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p7beta1.Resource)
  })
_sym_db.RegisterMessage(Resource)

RelatedAssets = _reflection.GeneratedProtocolMessageType('RelatedAssets', (_message.Message,), {
  'DESCRIPTOR' : _RELATEDASSETS,
  '__module__' : 'google.cloud.asset.v1p7beta1.assets_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p7beta1.RelatedAssets)
  })
_sym_db.RegisterMessage(RelatedAssets)

RelationshipAttributes = _reflection.GeneratedProtocolMessageType('RelationshipAttributes', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONSHIPATTRIBUTES,
  '__module__' : 'google.cloud.asset.v1p7beta1.assets_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p7beta1.RelationshipAttributes)
  })
_sym_db.RegisterMessage(RelationshipAttributes)

RelatedAsset = _reflection.GeneratedProtocolMessageType('RelatedAsset', (_message.Message,), {
  'DESCRIPTOR' : _RELATEDASSET,
  '__module__' : 'google.cloud.asset.v1p7beta1.assets_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1p7beta1.RelatedAsset)
  })
_sym_db.RegisterMessage(RelatedAsset)


DESCRIPTOR._options = None
_ASSET._options = None
_RELATEDASSET.fields_by_name['asset']._options = None
# @@protoc_insertion_point(module_scope)
