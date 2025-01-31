# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/genomics/v1/references.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/genomics/v1/references.proto',
  package='google.genomics.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.google.genomics.v1B\017ReferencesProtoP\001Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#google/genomics/v1/references.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\"\xd9\x01\n\tReference\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06length\x18\x02 \x01(\x03R\x06length\x12 \n\x0bmd5checksum\x18\x03 \x01(\tR\x0bmd5checksum\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x1d\n\nsource_uri\x18\x05 \x01(\tR\tsourceUri\x12+\n\x11source_accessions\x18\x06 \x03(\tR\x10sourceAccessions\x12\"\n\rncbi_taxon_id\x18\x07 \x01(\x05R\x0bncbiTaxonId\"\x98\x02\n\x0cReferenceSet\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12#\n\rreference_ids\x18\x02 \x03(\tR\x0creferenceIds\x12 \n\x0bmd5checksum\x18\x03 \x01(\tR\x0bmd5checksum\x12\"\n\rncbi_taxon_id\x18\x04 \x01(\x05R\x0bncbiTaxonId\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12\x1f\n\x0b\x61ssembly_id\x18\x06 \x01(\tR\nassemblyId\x12\x1d\n\nsource_uri\x18\x07 \x01(\tR\tsourceUri\x12+\n\x11source_accessions\x18\x08 \x03(\tR\x10sourceAccessions\"\xbd\x01\n\x1aSearchReferenceSetsRequest\x12\"\n\x0cmd5checksums\x18\x01 \x03(\tR\x0cmd5checksums\x12\x1e\n\naccessions\x18\x02 \x03(\tR\naccessions\x12\x1f\n\x0b\x61ssembly_id\x18\x03 \x01(\tR\nassemblyId\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x05 \x01(\x05R\x08pageSize\"\x8e\x01\n\x1bSearchReferenceSetsResponse\x12G\n\x0ereference_sets\x18\x01 \x03(\x0b\x32 .google.genomics.v1.ReferenceSetR\rreferenceSets\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"B\n\x16GetReferenceSetRequest\x12(\n\x10reference_set_id\x18\x01 \x01(\tR\x0ereferenceSetId\"\xc3\x01\n\x17SearchReferencesRequest\x12\"\n\x0cmd5checksums\x18\x01 \x03(\tR\x0cmd5checksums\x12\x1e\n\naccessions\x18\x02 \x03(\tR\naccessions\x12(\n\x10reference_set_id\x18\x03 \x01(\tR\x0ereferenceSetId\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x05 \x01(\x05R\x08pageSize\"\x81\x01\n\x18SearchReferencesResponse\x12=\n\nreferences\x18\x01 \x03(\x0b\x32\x1d.google.genomics.v1.ReferenceR\nreferences\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"8\n\x13GetReferenceRequest\x12!\n\x0creference_id\x18\x01 \x01(\tR\x0breferenceId\"\x99\x01\n\x10ListBasesRequest\x12!\n\x0creference_id\x18\x01 \x01(\tR\x0breferenceId\x12\x14\n\x05start\x18\x02 \x01(\x03R\x05start\x12\x10\n\x03\x65nd\x18\x03 \x01(\x03R\x03\x65nd\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x05 \x01(\x05R\x08pageSize\"o\n\x11ListBasesResponse\x12\x16\n\x06offset\x18\x01 \x01(\x03R\x06offset\x12\x1a\n\x08sequence\x18\x02 \x01(\tR\x08sequence\x12&\n\x0fnext_page_token\x18\x03 \x01(\tR\rnextPageToken2\xdb\x05\n\x12ReferenceServiceV1\x12\x9b\x01\n\x13SearchReferenceSets\x12..google.genomics.v1.SearchReferenceSetsRequest\x1a/.google.genomics.v1.SearchReferenceSetsResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/v1/referencesets/search:\x01*\x12\x8d\x01\n\x0fGetReferenceSet\x12*.google.genomics.v1.GetReferenceSetRequest\x1a .google.genomics.v1.ReferenceSet\",\x82\xd3\xe4\x93\x02&\x12$/v1/referencesets/{reference_set_id}\x12\x8f\x01\n\x10SearchReferences\x12+.google.genomics.v1.SearchReferencesRequest\x1a,.google.genomics.v1.SearchReferencesResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v1/references/search:\x01*\x12}\n\x0cGetReference\x12\'.google.genomics.v1.GetReferenceRequest\x1a\x1d.google.genomics.v1.Reference\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/references/{reference_id}\x12\x85\x01\n\tListBases\x12$.google.genomics.v1.ListBasesRequest\x1a%.google.genomics.v1.ListBasesResponse\"+\x82\xd3\xe4\x93\x02%\x12#/v1/references/{reference_id}/basesBj\n\x16\x63om.google.genomics.v1B\x0fReferencesProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_REFERENCE = _descriptor.Descriptor(
  name='Reference',
  full_name='google.genomics.v1.Reference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.genomics.v1.Reference.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='google.genomics.v1.Reference.length', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='length', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='md5checksum', full_name='google.genomics.v1.Reference.md5checksum', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='md5checksum', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.genomics.v1.Reference.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_uri', full_name='google.genomics.v1.Reference.source_uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sourceUri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_accessions', full_name='google.genomics.v1.Reference.source_accessions', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sourceAccessions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ncbi_taxon_id', full_name='google.genomics.v1.Reference.ncbi_taxon_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ncbiTaxonId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=90,
  serialized_end=307,
)


_REFERENCESET = _descriptor.Descriptor(
  name='ReferenceSet',
  full_name='google.genomics.v1.ReferenceSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.genomics.v1.ReferenceSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reference_ids', full_name='google.genomics.v1.ReferenceSet.reference_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='referenceIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='md5checksum', full_name='google.genomics.v1.ReferenceSet.md5checksum', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='md5checksum', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ncbi_taxon_id', full_name='google.genomics.v1.ReferenceSet.ncbi_taxon_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ncbiTaxonId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.genomics.v1.ReferenceSet.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assembly_id', full_name='google.genomics.v1.ReferenceSet.assembly_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='assemblyId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_uri', full_name='google.genomics.v1.ReferenceSet.source_uri', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sourceUri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_accessions', full_name='google.genomics.v1.ReferenceSet.source_accessions', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sourceAccessions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=310,
  serialized_end=590,
)


_SEARCHREFERENCESETSREQUEST = _descriptor.Descriptor(
  name='SearchReferenceSetsRequest',
  full_name='google.genomics.v1.SearchReferenceSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='md5checksums', full_name='google.genomics.v1.SearchReferenceSetsRequest.md5checksums', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='md5checksums', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessions', full_name='google.genomics.v1.SearchReferenceSetsRequest.accessions', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='accessions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assembly_id', full_name='google.genomics.v1.SearchReferenceSetsRequest.assembly_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='assemblyId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.genomics.v1.SearchReferenceSetsRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.genomics.v1.SearchReferenceSetsRequest.page_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=593,
  serialized_end=782,
)


_SEARCHREFERENCESETSRESPONSE = _descriptor.Descriptor(
  name='SearchReferenceSetsResponse',
  full_name='google.genomics.v1.SearchReferenceSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_sets', full_name='google.genomics.v1.SearchReferenceSetsResponse.reference_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='referenceSets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.genomics.v1.SearchReferenceSetsResponse.next_page_token', index=1,
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
  serialized_start=785,
  serialized_end=927,
)


_GETREFERENCESETREQUEST = _descriptor.Descriptor(
  name='GetReferenceSetRequest',
  full_name='google.genomics.v1.GetReferenceSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='google.genomics.v1.GetReferenceSetRequest.reference_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='referenceSetId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=929,
  serialized_end=995,
)


_SEARCHREFERENCESREQUEST = _descriptor.Descriptor(
  name='SearchReferencesRequest',
  full_name='google.genomics.v1.SearchReferencesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='md5checksums', full_name='google.genomics.v1.SearchReferencesRequest.md5checksums', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='md5checksums', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessions', full_name='google.genomics.v1.SearchReferencesRequest.accessions', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='accessions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='google.genomics.v1.SearchReferencesRequest.reference_set_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='referenceSetId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.genomics.v1.SearchReferencesRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.genomics.v1.SearchReferencesRequest.page_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=998,
  serialized_end=1193,
)


_SEARCHREFERENCESRESPONSE = _descriptor.Descriptor(
  name='SearchReferencesResponse',
  full_name='google.genomics.v1.SearchReferencesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='references', full_name='google.genomics.v1.SearchReferencesResponse.references', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='references', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.genomics.v1.SearchReferencesResponse.next_page_token', index=1,
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
  serialized_start=1196,
  serialized_end=1325,
)


_GETREFERENCEREQUEST = _descriptor.Descriptor(
  name='GetReferenceRequest',
  full_name='google.genomics.v1.GetReferenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_id', full_name='google.genomics.v1.GetReferenceRequest.reference_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='referenceId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1327,
  serialized_end=1383,
)


_LISTBASESREQUEST = _descriptor.Descriptor(
  name='ListBasesRequest',
  full_name='google.genomics.v1.ListBasesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_id', full_name='google.genomics.v1.ListBasesRequest.reference_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='referenceId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='google.genomics.v1.ListBasesRequest.start', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='start', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='google.genomics.v1.ListBasesRequest.end', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='end', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.genomics.v1.ListBasesRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.genomics.v1.ListBasesRequest.page_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1386,
  serialized_end=1539,
)


_LISTBASESRESPONSE = _descriptor.Descriptor(
  name='ListBasesResponse',
  full_name='google.genomics.v1.ListBasesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='google.genomics.v1.ListBasesResponse.offset', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='offset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='google.genomics.v1.ListBasesResponse.sequence', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sequence', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.genomics.v1.ListBasesResponse.next_page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1541,
  serialized_end=1652,
)

_SEARCHREFERENCESETSRESPONSE.fields_by_name['reference_sets'].message_type = _REFERENCESET
_SEARCHREFERENCESRESPONSE.fields_by_name['references'].message_type = _REFERENCE
DESCRIPTOR.message_types_by_name['Reference'] = _REFERENCE
DESCRIPTOR.message_types_by_name['ReferenceSet'] = _REFERENCESET
DESCRIPTOR.message_types_by_name['SearchReferenceSetsRequest'] = _SEARCHREFERENCESETSREQUEST
DESCRIPTOR.message_types_by_name['SearchReferenceSetsResponse'] = _SEARCHREFERENCESETSRESPONSE
DESCRIPTOR.message_types_by_name['GetReferenceSetRequest'] = _GETREFERENCESETREQUEST
DESCRIPTOR.message_types_by_name['SearchReferencesRequest'] = _SEARCHREFERENCESREQUEST
DESCRIPTOR.message_types_by_name['SearchReferencesResponse'] = _SEARCHREFERENCESRESPONSE
DESCRIPTOR.message_types_by_name['GetReferenceRequest'] = _GETREFERENCEREQUEST
DESCRIPTOR.message_types_by_name['ListBasesRequest'] = _LISTBASESREQUEST
DESCRIPTOR.message_types_by_name['ListBasesResponse'] = _LISTBASESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Reference = _reflection.GeneratedProtocolMessageType('Reference', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCE,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.Reference)
  })
_sym_db.RegisterMessage(Reference)

ReferenceSet = _reflection.GeneratedProtocolMessageType('ReferenceSet', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCESET,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.ReferenceSet)
  })
_sym_db.RegisterMessage(ReferenceSet)

SearchReferenceSetsRequest = _reflection.GeneratedProtocolMessageType('SearchReferenceSetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREFERENCESETSREQUEST,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.SearchReferenceSetsRequest)
  })
_sym_db.RegisterMessage(SearchReferenceSetsRequest)

SearchReferenceSetsResponse = _reflection.GeneratedProtocolMessageType('SearchReferenceSetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREFERENCESETSRESPONSE,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.SearchReferenceSetsResponse)
  })
_sym_db.RegisterMessage(SearchReferenceSetsResponse)

GetReferenceSetRequest = _reflection.GeneratedProtocolMessageType('GetReferenceSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREFERENCESETREQUEST,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.GetReferenceSetRequest)
  })
_sym_db.RegisterMessage(GetReferenceSetRequest)

SearchReferencesRequest = _reflection.GeneratedProtocolMessageType('SearchReferencesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREFERENCESREQUEST,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.SearchReferencesRequest)
  })
_sym_db.RegisterMessage(SearchReferencesRequest)

SearchReferencesResponse = _reflection.GeneratedProtocolMessageType('SearchReferencesResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREFERENCESRESPONSE,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.SearchReferencesResponse)
  })
_sym_db.RegisterMessage(SearchReferencesResponse)

GetReferenceRequest = _reflection.GeneratedProtocolMessageType('GetReferenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREFERENCEREQUEST,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.GetReferenceRequest)
  })
_sym_db.RegisterMessage(GetReferenceRequest)

ListBasesRequest = _reflection.GeneratedProtocolMessageType('ListBasesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBASESREQUEST,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.ListBasesRequest)
  })
_sym_db.RegisterMessage(ListBasesRequest)

ListBasesResponse = _reflection.GeneratedProtocolMessageType('ListBasesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBASESRESPONSE,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.ListBasesResponse)
  })
_sym_db.RegisterMessage(ListBasesResponse)


DESCRIPTOR._options = None

_REFERENCESERVICEV1 = _descriptor.ServiceDescriptor(
  name='ReferenceServiceV1',
  full_name='google.genomics.v1.ReferenceServiceV1',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1655,
  serialized_end=2386,
  methods=[
  _descriptor.MethodDescriptor(
    name='SearchReferenceSets',
    full_name='google.genomics.v1.ReferenceServiceV1.SearchReferenceSets',
    index=0,
    containing_service=None,
    input_type=_SEARCHREFERENCESETSREQUEST,
    output_type=_SEARCHREFERENCESETSRESPONSE,
    serialized_options=b'\202\323\344\223\002\035\"\030/v1/referencesets/search:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetReferenceSet',
    full_name='google.genomics.v1.ReferenceServiceV1.GetReferenceSet',
    index=1,
    containing_service=None,
    input_type=_GETREFERENCESETREQUEST,
    output_type=_REFERENCESET,
    serialized_options=b'\202\323\344\223\002&\022$/v1/referencesets/{reference_set_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchReferences',
    full_name='google.genomics.v1.ReferenceServiceV1.SearchReferences',
    index=2,
    containing_service=None,
    input_type=_SEARCHREFERENCESREQUEST,
    output_type=_SEARCHREFERENCESRESPONSE,
    serialized_options=b'\202\323\344\223\002\032\"\025/v1/references/search:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetReference',
    full_name='google.genomics.v1.ReferenceServiceV1.GetReference',
    index=3,
    containing_service=None,
    input_type=_GETREFERENCEREQUEST,
    output_type=_REFERENCE,
    serialized_options=b'\202\323\344\223\002\037\022\035/v1/references/{reference_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListBases',
    full_name='google.genomics.v1.ReferenceServiceV1.ListBases',
    index=4,
    containing_service=None,
    input_type=_LISTBASESREQUEST,
    output_type=_LISTBASESRESPONSE,
    serialized_options=b'\202\323\344\223\002%\022#/v1/references/{reference_id}/bases',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REFERENCESERVICEV1)

DESCRIPTOR.services_by_name['ReferenceServiceV1'] = _REFERENCESERVICEV1

# @@protoc_insertion_point(module_scope)
