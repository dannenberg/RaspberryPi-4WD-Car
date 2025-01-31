# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/firestore/admin/v1beta2/firestore_admin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.firestore.admin.v1beta2 import field_pb2 as google_dot_firestore_dot_admin_dot_v1beta2_dot_field__pb2
from google.firestore.admin.v1beta2 import index_pb2 as google_dot_firestore_dot_admin_dot_v1beta2_dot_index__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/firestore/admin/v1beta2/firestore_admin.proto',
  package='google.firestore.admin.v1beta2',
  syntax='proto3',
  serialized_options=b'\n\"com.google.firestore.admin.v1beta2B\023FirestoreAdminProtoP\001ZCgoogle.golang.org/genproto/googleapis/firestore/admin/v1beta2;admin\242\002\004GCFS\252\002$Google.Cloud.Firestore.Admin.V1Beta2',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4google/firestore/admin/v1beta2/firestore_admin.proto\x12\x1egoogle.firestore.admin.v1beta2\x1a\x1cgoogle/api/annotations.proto\x1a*google/firestore/admin/v1beta2/field.proto\x1a*google/firestore/admin/v1beta2/index.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/api/client.proto\"i\n\x12\x43reateIndexRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12;\n\x05index\x18\x02 \x01(\x0b\x32%.google.firestore.admin.v1beta2.IndexR\x05index\"\x80\x01\n\x12ListIndexesRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\"~\n\x13ListIndexesResponse\x12?\n\x07indexes\x18\x01 \x03(\x0b\x32%.google.firestore.admin.v1beta2.IndexR\x07indexes\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"%\n\x0fGetIndexRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"(\n\x12\x44\x65leteIndexRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"\x8e\x01\n\x12UpdateFieldRequest\x12;\n\x05\x66ield\x18\x01 \x01(\x0b\x32%.google.firestore.admin.v1beta2.FieldR\x05\x66ield\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"%\n\x0fGetFieldRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"\x7f\n\x11ListFieldsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\"{\n\x12ListFieldsResponse\x12=\n\x06\x66ields\x18\x01 \x03(\x0b\x32%.google.firestore.admin.v1beta2.FieldR\x06\x66ields\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\x7f\n\x16\x45xportDocumentsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12%\n\x0e\x63ollection_ids\x18\x02 \x03(\tR\rcollectionIds\x12*\n\x11output_uri_prefix\x18\x03 \x01(\tR\x0foutputUriPrefix\"}\n\x16ImportDocumentsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12%\n\x0e\x63ollection_ids\x18\x02 \x03(\tR\rcollectionIds\x12(\n\x10input_uri_prefix\x18\x03 \x01(\tR\x0einputUriPrefix2\xeb\r\n\x0e\x46irestoreAdmin\x12\xb4\x01\n\x0b\x43reateIndex\x12\x32.google.firestore.admin.v1beta2.CreateIndexRequest\x1a\x1d.google.longrunning.Operation\"R\x82\xd3\xe4\x93\x02L\"C/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/indexes:\x05index\x12\xc3\x01\n\x0bListIndexes\x12\x32.google.firestore.admin.v1beta2.ListIndexesRequest\x1a\x33.google.firestore.admin.v1beta2.ListIndexesResponse\"K\x82\xd3\xe4\x93\x02\x45\x12\x43/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/indexes\x12\xaf\x01\n\x08GetIndex\x12/.google.firestore.admin.v1beta2.GetIndexRequest\x1a%.google.firestore.admin.v1beta2.Index\"K\x82\xd3\xe4\x93\x02\x45\x12\x43/v1beta2/{name=projects/*/databases/*/collectionGroups/*/indexes/*}\x12\xa6\x01\n\x0b\x44\x65leteIndex\x12\x32.google.firestore.admin.v1beta2.DeleteIndexRequest\x1a\x16.google.protobuf.Empty\"K\x82\xd3\xe4\x93\x02\x45*C/v1beta2/{name=projects/*/databases/*/collectionGroups/*/indexes/*}\x12\xae\x01\n\x08GetField\x12/.google.firestore.admin.v1beta2.GetFieldRequest\x1a%.google.firestore.admin.v1beta2.Field\"J\x82\xd3\xe4\x93\x02\x44\x12\x42/v1beta2/{name=projects/*/databases/*/collectionGroups/*/fields/*}\x12\xb9\x01\n\x0bUpdateField\x12\x32.google.firestore.admin.v1beta2.UpdateFieldRequest\x1a\x1d.google.longrunning.Operation\"W\x82\xd3\xe4\x93\x02Q2H/v1beta2/{field.name=projects/*/databases/*/collectionGroups/*/fields/*}:\x05\x66ield\x12\xbf\x01\n\nListFields\x12\x31.google.firestore.admin.v1beta2.ListFieldsRequest\x1a\x32.google.firestore.admin.v1beta2.ListFieldsResponse\"J\x82\xd3\xe4\x93\x02\x44\x12\x42/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/fields\x12\xab\x01\n\x0f\x45xportDocuments\x12\x36.google.firestore.admin.v1beta2.ExportDocumentsRequest\x1a\x1d.google.longrunning.Operation\"A\x82\xd3\xe4\x93\x02;\"6/v1beta2/{name=projects/*/databases/*}:exportDocuments:\x01*\x12\xab\x01\n\x0fImportDocuments\x12\x36.google.firestore.admin.v1beta2.ImportDocumentsRequest\x1a\x1d.google.longrunning.Operation\"A\x82\xd3\xe4\x93\x02;\"6/v1beta2/{name=projects/*/databases/*}:importDocuments:\x01*\x1av\xca\x41\x18\x66irestore.googleapis.com\xd2\x41Xhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastoreB\xae\x01\n\"com.google.firestore.admin.v1beta2B\x13\x46irestoreAdminProtoP\x01ZCgoogle.golang.org/genproto/googleapis/firestore/admin/v1beta2;admin\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta2b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_firestore_dot_admin_dot_v1beta2_dot_field__pb2.DESCRIPTOR,google_dot_firestore_dot_admin_dot_v1beta2_dot_index__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_CREATEINDEXREQUEST = _descriptor.Descriptor(
  name='CreateIndexRequest',
  full_name='google.firestore.admin.v1beta2.CreateIndexRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.firestore.admin.v1beta2.CreateIndexRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='google.firestore.admin.v1beta2.CreateIndexRequest.index', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='index', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=331,
  serialized_end=436,
)


_LISTINDEXESREQUEST = _descriptor.Descriptor(
  name='ListIndexesRequest',
  full_name='google.firestore.admin.v1beta2.ListIndexesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.firestore.admin.v1beta2.ListIndexesRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.firestore.admin.v1beta2.ListIndexesRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='filter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.firestore.admin.v1beta2.ListIndexesRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.firestore.admin.v1beta2.ListIndexesRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=439,
  serialized_end=567,
)


_LISTINDEXESRESPONSE = _descriptor.Descriptor(
  name='ListIndexesResponse',
  full_name='google.firestore.admin.v1beta2.ListIndexesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='indexes', full_name='google.firestore.admin.v1beta2.ListIndexesResponse.indexes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='indexes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.firestore.admin.v1beta2.ListIndexesResponse.next_page_token', index=1,
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
  serialized_start=569,
  serialized_end=695,
)


_GETINDEXREQUEST = _descriptor.Descriptor(
  name='GetIndexRequest',
  full_name='google.firestore.admin.v1beta2.GetIndexRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.firestore.admin.v1beta2.GetIndexRequest.name', index=0,
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
  serialized_start=697,
  serialized_end=734,
)


_DELETEINDEXREQUEST = _descriptor.Descriptor(
  name='DeleteIndexRequest',
  full_name='google.firestore.admin.v1beta2.DeleteIndexRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.firestore.admin.v1beta2.DeleteIndexRequest.name', index=0,
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
  serialized_start=736,
  serialized_end=776,
)


_UPDATEFIELDREQUEST = _descriptor.Descriptor(
  name='UpdateFieldRequest',
  full_name='google.firestore.admin.v1beta2.UpdateFieldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='google.firestore.admin.v1beta2.UpdateFieldRequest.field', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='field', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.firestore.admin.v1beta2.UpdateFieldRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='updateMask', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=779,
  serialized_end=921,
)


_GETFIELDREQUEST = _descriptor.Descriptor(
  name='GetFieldRequest',
  full_name='google.firestore.admin.v1beta2.GetFieldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.firestore.admin.v1beta2.GetFieldRequest.name', index=0,
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
  serialized_start=923,
  serialized_end=960,
)


_LISTFIELDSREQUEST = _descriptor.Descriptor(
  name='ListFieldsRequest',
  full_name='google.firestore.admin.v1beta2.ListFieldsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.firestore.admin.v1beta2.ListFieldsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.firestore.admin.v1beta2.ListFieldsRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='filter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.firestore.admin.v1beta2.ListFieldsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.firestore.admin.v1beta2.ListFieldsRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=962,
  serialized_end=1089,
)


_LISTFIELDSRESPONSE = _descriptor.Descriptor(
  name='ListFieldsResponse',
  full_name='google.firestore.admin.v1beta2.ListFieldsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='google.firestore.admin.v1beta2.ListFieldsResponse.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fields', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.firestore.admin.v1beta2.ListFieldsResponse.next_page_token', index=1,
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
  serialized_start=1091,
  serialized_end=1214,
)


_EXPORTDOCUMENTSREQUEST = _descriptor.Descriptor(
  name='ExportDocumentsRequest',
  full_name='google.firestore.admin.v1beta2.ExportDocumentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.firestore.admin.v1beta2.ExportDocumentsRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collection_ids', full_name='google.firestore.admin.v1beta2.ExportDocumentsRequest.collection_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='collectionIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_uri_prefix', full_name='google.firestore.admin.v1beta2.ExportDocumentsRequest.output_uri_prefix', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='outputUriPrefix', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1216,
  serialized_end=1343,
)


_IMPORTDOCUMENTSREQUEST = _descriptor.Descriptor(
  name='ImportDocumentsRequest',
  full_name='google.firestore.admin.v1beta2.ImportDocumentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.firestore.admin.v1beta2.ImportDocumentsRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collection_ids', full_name='google.firestore.admin.v1beta2.ImportDocumentsRequest.collection_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='collectionIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_uri_prefix', full_name='google.firestore.admin.v1beta2.ImportDocumentsRequest.input_uri_prefix', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='inputUriPrefix', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1345,
  serialized_end=1470,
)

_CREATEINDEXREQUEST.fields_by_name['index'].message_type = google_dot_firestore_dot_admin_dot_v1beta2_dot_index__pb2._INDEX
_LISTINDEXESRESPONSE.fields_by_name['indexes'].message_type = google_dot_firestore_dot_admin_dot_v1beta2_dot_index__pb2._INDEX
_UPDATEFIELDREQUEST.fields_by_name['field'].message_type = google_dot_firestore_dot_admin_dot_v1beta2_dot_field__pb2._FIELD
_UPDATEFIELDREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_LISTFIELDSRESPONSE.fields_by_name['fields'].message_type = google_dot_firestore_dot_admin_dot_v1beta2_dot_field__pb2._FIELD
DESCRIPTOR.message_types_by_name['CreateIndexRequest'] = _CREATEINDEXREQUEST
DESCRIPTOR.message_types_by_name['ListIndexesRequest'] = _LISTINDEXESREQUEST
DESCRIPTOR.message_types_by_name['ListIndexesResponse'] = _LISTINDEXESRESPONSE
DESCRIPTOR.message_types_by_name['GetIndexRequest'] = _GETINDEXREQUEST
DESCRIPTOR.message_types_by_name['DeleteIndexRequest'] = _DELETEINDEXREQUEST
DESCRIPTOR.message_types_by_name['UpdateFieldRequest'] = _UPDATEFIELDREQUEST
DESCRIPTOR.message_types_by_name['GetFieldRequest'] = _GETFIELDREQUEST
DESCRIPTOR.message_types_by_name['ListFieldsRequest'] = _LISTFIELDSREQUEST
DESCRIPTOR.message_types_by_name['ListFieldsResponse'] = _LISTFIELDSRESPONSE
DESCRIPTOR.message_types_by_name['ExportDocumentsRequest'] = _EXPORTDOCUMENTSREQUEST
DESCRIPTOR.message_types_by_name['ImportDocumentsRequest'] = _IMPORTDOCUMENTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateIndexRequest = _reflection.GeneratedProtocolMessageType('CreateIndexRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEINDEXREQUEST,
  '__module__' : 'google.firestore.admin.v1beta2.firestore_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.admin.v1beta2.CreateIndexRequest)
  })
_sym_db.RegisterMessage(CreateIndexRequest)

ListIndexesRequest = _reflection.GeneratedProtocolMessageType('ListIndexesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTINDEXESREQUEST,
  '__module__' : 'google.firestore.admin.v1beta2.firestore_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.admin.v1beta2.ListIndexesRequest)
  })
_sym_db.RegisterMessage(ListIndexesRequest)

ListIndexesResponse = _reflection.GeneratedProtocolMessageType('ListIndexesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINDEXESRESPONSE,
  '__module__' : 'google.firestore.admin.v1beta2.firestore_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.admin.v1beta2.ListIndexesResponse)
  })
_sym_db.RegisterMessage(ListIndexesResponse)

GetIndexRequest = _reflection.GeneratedProtocolMessageType('GetIndexRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINDEXREQUEST,
  '__module__' : 'google.firestore.admin.v1beta2.firestore_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.admin.v1beta2.GetIndexRequest)
  })
_sym_db.RegisterMessage(GetIndexRequest)

DeleteIndexRequest = _reflection.GeneratedProtocolMessageType('DeleteIndexRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEINDEXREQUEST,
  '__module__' : 'google.firestore.admin.v1beta2.firestore_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.admin.v1beta2.DeleteIndexRequest)
  })
_sym_db.RegisterMessage(DeleteIndexRequest)

UpdateFieldRequest = _reflection.GeneratedProtocolMessageType('UpdateFieldRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFIELDREQUEST,
  '__module__' : 'google.firestore.admin.v1beta2.firestore_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.admin.v1beta2.UpdateFieldRequest)
  })
_sym_db.RegisterMessage(UpdateFieldRequest)

GetFieldRequest = _reflection.GeneratedProtocolMessageType('GetFieldRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFIELDREQUEST,
  '__module__' : 'google.firestore.admin.v1beta2.firestore_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.admin.v1beta2.GetFieldRequest)
  })
_sym_db.RegisterMessage(GetFieldRequest)

ListFieldsRequest = _reflection.GeneratedProtocolMessageType('ListFieldsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFIELDSREQUEST,
  '__module__' : 'google.firestore.admin.v1beta2.firestore_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.admin.v1beta2.ListFieldsRequest)
  })
_sym_db.RegisterMessage(ListFieldsRequest)

ListFieldsResponse = _reflection.GeneratedProtocolMessageType('ListFieldsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFIELDSRESPONSE,
  '__module__' : 'google.firestore.admin.v1beta2.firestore_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.admin.v1beta2.ListFieldsResponse)
  })
_sym_db.RegisterMessage(ListFieldsResponse)

ExportDocumentsRequest = _reflection.GeneratedProtocolMessageType('ExportDocumentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTDOCUMENTSREQUEST,
  '__module__' : 'google.firestore.admin.v1beta2.firestore_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.admin.v1beta2.ExportDocumentsRequest)
  })
_sym_db.RegisterMessage(ExportDocumentsRequest)

ImportDocumentsRequest = _reflection.GeneratedProtocolMessageType('ImportDocumentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTDOCUMENTSREQUEST,
  '__module__' : 'google.firestore.admin.v1beta2.firestore_admin_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.admin.v1beta2.ImportDocumentsRequest)
  })
_sym_db.RegisterMessage(ImportDocumentsRequest)


DESCRIPTOR._options = None

_FIRESTOREADMIN = _descriptor.ServiceDescriptor(
  name='FirestoreAdmin',
  full_name='google.firestore.admin.v1beta2.FirestoreAdmin',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030firestore.googleapis.com\322AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastore',
  create_key=_descriptor._internal_create_key,
  serialized_start=1473,
  serialized_end=3244,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateIndex',
    full_name='google.firestore.admin.v1beta2.FirestoreAdmin.CreateIndex',
    index=0,
    containing_service=None,
    input_type=_CREATEINDEXREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002L\"C/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/indexes:\005index',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListIndexes',
    full_name='google.firestore.admin.v1beta2.FirestoreAdmin.ListIndexes',
    index=1,
    containing_service=None,
    input_type=_LISTINDEXESREQUEST,
    output_type=_LISTINDEXESRESPONSE,
    serialized_options=b'\202\323\344\223\002E\022C/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/indexes',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetIndex',
    full_name='google.firestore.admin.v1beta2.FirestoreAdmin.GetIndex',
    index=2,
    containing_service=None,
    input_type=_GETINDEXREQUEST,
    output_type=google_dot_firestore_dot_admin_dot_v1beta2_dot_index__pb2._INDEX,
    serialized_options=b'\202\323\344\223\002E\022C/v1beta2/{name=projects/*/databases/*/collectionGroups/*/indexes/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteIndex',
    full_name='google.firestore.admin.v1beta2.FirestoreAdmin.DeleteIndex',
    index=3,
    containing_service=None,
    input_type=_DELETEINDEXREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002E*C/v1beta2/{name=projects/*/databases/*/collectionGroups/*/indexes/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetField',
    full_name='google.firestore.admin.v1beta2.FirestoreAdmin.GetField',
    index=4,
    containing_service=None,
    input_type=_GETFIELDREQUEST,
    output_type=google_dot_firestore_dot_admin_dot_v1beta2_dot_field__pb2._FIELD,
    serialized_options=b'\202\323\344\223\002D\022B/v1beta2/{name=projects/*/databases/*/collectionGroups/*/fields/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateField',
    full_name='google.firestore.admin.v1beta2.FirestoreAdmin.UpdateField',
    index=5,
    containing_service=None,
    input_type=_UPDATEFIELDREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002Q2H/v1beta2/{field.name=projects/*/databases/*/collectionGroups/*/fields/*}:\005field',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListFields',
    full_name='google.firestore.admin.v1beta2.FirestoreAdmin.ListFields',
    index=6,
    containing_service=None,
    input_type=_LISTFIELDSREQUEST,
    output_type=_LISTFIELDSRESPONSE,
    serialized_options=b'\202\323\344\223\002D\022B/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/fields',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExportDocuments',
    full_name='google.firestore.admin.v1beta2.FirestoreAdmin.ExportDocuments',
    index=7,
    containing_service=None,
    input_type=_EXPORTDOCUMENTSREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002;\"6/v1beta2/{name=projects/*/databases/*}:exportDocuments:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ImportDocuments',
    full_name='google.firestore.admin.v1beta2.FirestoreAdmin.ImportDocuments',
    index=8,
    containing_service=None,
    input_type=_IMPORTDOCUMENTSREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002;\"6/v1beta2/{name=projects/*/databases/*}:importDocuments:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FIRESTOREADMIN)

DESCRIPTOR.services_by_name['FirestoreAdmin'] = _FIRESTOREADMIN

# @@protoc_insertion_point(module_scope)
