# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/offline_user_data_job.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.common import offline_user_data_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_common_dot_offline__user__data__pb2
from google.ads.googleads.v8.enums import offline_user_data_job_failure_reason_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_offline__user__data__job__failure__reason__pb2
from google.ads.googleads.v8.enums import offline_user_data_job_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_offline__user__data__job__status__pb2
from google.ads.googleads.v8.enums import offline_user_data_job_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_offline__user__data__job__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v8/resources/offline_user_data_job.proto',
  package='google.ads.googleads.v8.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v8.resourcesB\027OfflineUserDataJobProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=google/ads/googleads/v8/resources/offline_user_data_job.proto\x12!google.ads.googleads.v8.resources\x1a\x36google/ads/googleads/v8/common/offline_user_data.proto\x1aHgoogle/ads/googleads/v8/enums/offline_user_data_job_failure_reason.proto\x1a@google/ads/googleads/v8/enums/offline_user_data_job_status.proto\x1a>google/ads/googleads/v8/enums/offline_user_data_job_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xc8\x07\n\x12OfflineUserDataJob\x12Y\n\rresource_name\x18\x01 \x01(\tB4\xe2\x41\x01\x05\xfa\x41-\n+googleads.googleapis.com/OfflineUserDataJobR\x0cresourceName\x12\x19\n\x02id\x18\t \x01(\x03\x42\x04\xe2\x41\x01\x03H\x01R\x02id\x88\x01\x01\x12*\n\x0b\x65xternal_id\x18\n \x01(\x03\x42\x04\xe2\x41\x01\x05H\x02R\nexternalId\x88\x01\x01\x12j\n\x04type\x18\x04 \x01(\x0e\x32P.google.ads.googleads.v8.enums.OfflineUserDataJobTypeEnum.OfflineUserDataJobTypeB\x04\xe2\x41\x01\x05R\x04type\x12r\n\x06status\x18\x05 \x01(\x0e\x32T.google.ads.googleads.v8.enums.OfflineUserDataJobStatusEnum.OfflineUserDataJobStatusB\x04\xe2\x41\x01\x03R\x06status\x12\x8f\x01\n\x0e\x66\x61ilure_reason\x18\x06 \x01(\x0e\x32\x62.google.ads.googleads.v8.enums.OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReasonB\x04\xe2\x41\x01\x03R\rfailureReason\x12\x8f\x01\n!customer_match_user_list_metadata\x18\x07 \x01(\x0b\x32=.google.ads.googleads.v8.common.CustomerMatchUserListMetadataB\x04\xe2\x41\x01\x05H\x00R\x1d\x63ustomerMatchUserListMetadata\x12l\n\x14store_sales_metadata\x18\x08 \x01(\x0b\x32\x32.google.ads.googleads.v8.common.StoreSalesMetadataB\x04\xe2\x41\x01\x05H\x00R\x12storeSalesMetadata:{\xea\x41x\n+googleads.googleapis.com/OfflineUserDataJob\x12Icustomers/{customer_id}/offlineUserDataJobs/{offline_user_data_update_id}B\n\n\x08metadataB\x05\n\x03_idB\x0e\n\x0c_external_idB\x84\x02\n%com.google.ads.googleads.v8.resourcesB\x17OfflineUserDataJobProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v8_dot_common_dot_offline__user__data__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_offline__user__data__job__failure__reason__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_offline__user__data__job__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_offline__user__data__job__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_OFFLINEUSERDATAJOB = _descriptor.Descriptor(
  name='OfflineUserDataJob',
  full_name='google.ads.googleads.v8.resources.OfflineUserDataJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v8.resources.OfflineUserDataJob.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A-\n+googleads.googleapis.com/OfflineUserDataJob', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v8.resources.OfflineUserDataJob.id', index=1,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external_id', full_name='google.ads.googleads.v8.resources.OfflineUserDataJob.external_id', index=2,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='externalId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v8.resources.OfflineUserDataJob.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v8.resources.OfflineUserDataJob.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failure_reason', full_name='google.ads.googleads.v8.resources.OfflineUserDataJob.failure_reason', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='failureReason', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_match_user_list_metadata', full_name='google.ads.googleads.v8.resources.OfflineUserDataJob.customer_match_user_list_metadata', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='customerMatchUserListMetadata', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='store_sales_metadata', full_name='google.ads.googleads.v8.resources.OfflineUserDataJob.store_sales_metadata', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='storeSalesMetadata', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Ax\n+googleads.googleapis.com/OfflineUserDataJob\022Icustomers/{customer_id}/offlineUserDataJobs/{offline_user_data_update_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='metadata', full_name='google.ads.googleads.v8.resources.OfflineUserDataJob.metadata',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_id', full_name='google.ads.googleads.v8.resources.OfflineUserDataJob._id',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_external_id', full_name='google.ads.googleads.v8.resources.OfflineUserDataJob._external_id',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=451,
  serialized_end=1419,
)

_OFFLINEUSERDATAJOB.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_offline__user__data__job__type__pb2._OFFLINEUSERDATAJOBTYPEENUM_OFFLINEUSERDATAJOBTYPE
_OFFLINEUSERDATAJOB.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_offline__user__data__job__status__pb2._OFFLINEUSERDATAJOBSTATUSENUM_OFFLINEUSERDATAJOBSTATUS
_OFFLINEUSERDATAJOB.fields_by_name['failure_reason'].enum_type = google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_offline__user__data__job__failure__reason__pb2._OFFLINEUSERDATAJOBFAILUREREASONENUM_OFFLINEUSERDATAJOBFAILUREREASON
_OFFLINEUSERDATAJOB.fields_by_name['customer_match_user_list_metadata'].message_type = google_dot_ads_dot_googleads_dot_v8_dot_common_dot_offline__user__data__pb2._CUSTOMERMATCHUSERLISTMETADATA
_OFFLINEUSERDATAJOB.fields_by_name['store_sales_metadata'].message_type = google_dot_ads_dot_googleads_dot_v8_dot_common_dot_offline__user__data__pb2._STORESALESMETADATA
_OFFLINEUSERDATAJOB.oneofs_by_name['metadata'].fields.append(
  _OFFLINEUSERDATAJOB.fields_by_name['customer_match_user_list_metadata'])
_OFFLINEUSERDATAJOB.fields_by_name['customer_match_user_list_metadata'].containing_oneof = _OFFLINEUSERDATAJOB.oneofs_by_name['metadata']
_OFFLINEUSERDATAJOB.oneofs_by_name['metadata'].fields.append(
  _OFFLINEUSERDATAJOB.fields_by_name['store_sales_metadata'])
_OFFLINEUSERDATAJOB.fields_by_name['store_sales_metadata'].containing_oneof = _OFFLINEUSERDATAJOB.oneofs_by_name['metadata']
_OFFLINEUSERDATAJOB.oneofs_by_name['_id'].fields.append(
  _OFFLINEUSERDATAJOB.fields_by_name['id'])
_OFFLINEUSERDATAJOB.fields_by_name['id'].containing_oneof = _OFFLINEUSERDATAJOB.oneofs_by_name['_id']
_OFFLINEUSERDATAJOB.oneofs_by_name['_external_id'].fields.append(
  _OFFLINEUSERDATAJOB.fields_by_name['external_id'])
_OFFLINEUSERDATAJOB.fields_by_name['external_id'].containing_oneof = _OFFLINEUSERDATAJOB.oneofs_by_name['_external_id']
DESCRIPTOR.message_types_by_name['OfflineUserDataJob'] = _OFFLINEUSERDATAJOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OfflineUserDataJob = _reflection.GeneratedProtocolMessageType('OfflineUserDataJob', (_message.Message,), {
  'DESCRIPTOR' : _OFFLINEUSERDATAJOB,
  '__module__' : 'google.ads.googleads.v8.resources.offline_user_data_job_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.OfflineUserDataJob)
  })
_sym_db.RegisterMessage(OfflineUserDataJob)


DESCRIPTOR._options = None
_OFFLINEUSERDATAJOB.fields_by_name['resource_name']._options = None
_OFFLINEUSERDATAJOB.fields_by_name['id']._options = None
_OFFLINEUSERDATAJOB.fields_by_name['external_id']._options = None
_OFFLINEUSERDATAJOB.fields_by_name['type']._options = None
_OFFLINEUSERDATAJOB.fields_by_name['status']._options = None
_OFFLINEUSERDATAJOB.fields_by_name['failure_reason']._options = None
_OFFLINEUSERDATAJOB.fields_by_name['customer_match_user_list_metadata']._options = None
_OFFLINEUSERDATAJOB.fields_by_name['store_sales_metadata']._options = None
_OFFLINEUSERDATAJOB._options = None
# @@protoc_insertion_point(module_scope)
