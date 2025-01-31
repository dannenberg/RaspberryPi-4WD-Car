# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/osconfig/v1alpha/instance_os_policies_compliance.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.osconfig.v1alpha import config_common_pb2 as google_dot_cloud_dot_osconfig_dot_v1alpha_dot_config__common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/osconfig/v1alpha/instance_os_policies_compliance.proto',
  package='google.cloud.osconfig.v1alpha',
  syntax='proto3',
  serialized_options=b'\n!com.google.cloud.osconfig.v1alphaB!InstanceOSPoliciesComplianceProtoP\001ZEgoogle.golang.org/genproto/googleapis/cloud/osconfig/v1alpha;osconfig\252\002\035Google.Cloud.OsConfig.V1Alpha\312\002\035Google\\Cloud\\OsConfig\\V1alpha\352\002 Google::Cloud::OsConfig::V1alpha',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCgoogle/cloud/osconfig/v1alpha/instance_os_policies_compliance.proto\x12\x1dgoogle.cloud.osconfig.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x31google/cloud/osconfig/v1alpha/config_common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb3\x08\n\x1cInstanceOSPoliciesCompliance\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12 \n\x08instance\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x08instance\x12R\n\x05state\x18\x03 \x01(\x0e\x32\x36.google.cloud.osconfig.v1alpha.OSPolicyComplianceStateB\x04\xe2\x41\x01\x03R\x05state\x12+\n\x0e\x64\x65tailed_state\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03R\rdetailedState\x12\x38\n\x15\x64\x65tailed_state_reason\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03R\x13\x64\x65tailedStateReason\x12\x88\x01\n\x15os_policy_compliances\x18\x06 \x03(\x0b\x32N.google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.OSPolicyComplianceB\x04\xe2\x41\x01\x03R\x13osPolicyCompliances\x12]\n\x1alast_compliance_check_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x17lastComplianceCheckTime\x12\x39\n\x16last_compliance_run_id\x18\x08 \x01(\tB\x04\xe2\x41\x01\x03R\x13lastComplianceRunId\x1a\xe7\x02\n\x12OSPolicyCompliance\x12 \n\x0cos_policy_id\x18\x01 \x01(\tR\nosPolicyId\x12\x61\n\x14os_policy_assignment\x18\x02 \x01(\tB/\xfa\x41,\n*osconfig.googleapis.com/OSPolicyAssignmentR\x12osPolicyAssignment\x12L\n\x05state\x18\x04 \x01(\x0e\x32\x36.google.cloud.osconfig.v1alpha.OSPolicyComplianceStateR\x05state\x12~\n\x1eos_policy_resource_compliances\x18\x05 \x03(\x0b\x32\x39.google.cloud.osconfig.v1alpha.OSPolicyResourceComplianceR\x1bosPolicyResourceCompliances:\x8c\x01\xea\x41\x88\x01\n4osconfig.googleapis.com/InstanceOSPoliciesCompliance\x12Pprojects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}\"{\n&GetInstanceOSPoliciesComplianceRequest\x12Q\n\x04name\x18\x01 \x01(\tB=\xe2\x41\x01\x02\xfa\x41\x36\n4osconfig.googleapis.com/InstanceOSPoliciesComplianceR\x04name\"\xc2\x01\n(ListInstanceOSPoliciesCompliancesRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12\x16\n\x06\x66ilter\x18\x04 \x01(\tR\x06\x66ilter\"\xda\x01\n)ListInstanceOSPoliciesCompliancesResponse\x12\x84\x01\n instance_os_policies_compliances\x18\x01 \x03(\x0b\x32;.google.cloud.osconfig.v1alpha.InstanceOSPoliciesComplianceR\x1dinstanceOsPoliciesCompliances\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageTokenB\xf2\x01\n!com.google.cloud.osconfig.v1alphaB!InstanceOSPoliciesComplianceProtoP\x01ZEgoogle.golang.org/genproto/googleapis/cloud/osconfig/v1alpha;osconfig\xaa\x02\x1dGoogle.Cloud.OsConfig.V1Alpha\xca\x02\x1dGoogle\\Cloud\\OsConfig\\V1alpha\xea\x02 Google::Cloud::OsConfig::V1alphab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_osconfig_dot_v1alpha_dot_config__common__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE = _descriptor.Descriptor(
  name='OSPolicyCompliance',
  full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.OSPolicyCompliance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='os_policy_id', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.OSPolicyCompliance.os_policy_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='osPolicyId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os_policy_assignment', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.OSPolicyCompliance.os_policy_assignment', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A,\n*osconfig.googleapis.com/OSPolicyAssignment', json_name='osPolicyAssignment', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.OSPolicyCompliance.state', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='state', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os_policy_resource_compliances', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.OSPolicyCompliance.os_policy_resource_compliances', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='osPolicyResourceCompliances', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=820,
  serialized_end=1179,
)

_INSTANCEOSPOLICIESCOMPLIANCE = _descriptor.Descriptor(
  name='InstanceOSPoliciesCompliance',
  full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.instance', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='instance', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='state', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detailed_state', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.detailed_state', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='detailedState', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detailed_state_reason', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.detailed_state_reason', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='detailedStateReason', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os_policy_compliances', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.os_policy_compliances', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='osPolicyCompliances', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_compliance_check_time', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.last_compliance_check_time', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='lastComplianceCheckTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_compliance_run_id', full_name='google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.last_compliance_run_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='lastComplianceRunId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE, ],
  enum_types=[
  ],
  serialized_options=b'\352A\210\001\n4osconfig.googleapis.com/InstanceOSPoliciesCompliance\022Pprojects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=1322,
)


_GETINSTANCEOSPOLICIESCOMPLIANCEREQUEST = _descriptor.Descriptor(
  name='GetInstanceOSPoliciesComplianceRequest',
  full_name='google.cloud.osconfig.v1alpha.GetInstanceOSPoliciesComplianceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.osconfig.v1alpha.GetInstanceOSPoliciesComplianceRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A6\n4osconfig.googleapis.com/InstanceOSPoliciesCompliance', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1324,
  serialized_end=1447,
)


_LISTINSTANCEOSPOLICIESCOMPLIANCESREQUEST = _descriptor.Descriptor(
  name='ListInstanceOSPoliciesCompliancesRequest',
  full_name='google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A#\n!locations.googleapis.com/Location', json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesRequest.filter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='filter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1450,
  serialized_end=1644,
)


_LISTINSTANCEOSPOLICIESCOMPLIANCESRESPONSE = _descriptor.Descriptor(
  name='ListInstanceOSPoliciesCompliancesResponse',
  full_name='google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_os_policies_compliances', full_name='google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesResponse.instance_os_policies_compliances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='instanceOsPoliciesCompliances', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesResponse.next_page_token', index=1,
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
  serialized_start=1647,
  serialized_end=1865,
)

_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE.fields_by_name['state'].enum_type = google_dot_cloud_dot_osconfig_dot_v1alpha_dot_config__common__pb2._OSPOLICYCOMPLIANCESTATE
_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE.fields_by_name['os_policy_resource_compliances'].message_type = google_dot_cloud_dot_osconfig_dot_v1alpha_dot_config__common__pb2._OSPOLICYRESOURCECOMPLIANCE
_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE.containing_type = _INSTANCEOSPOLICIESCOMPLIANCE
_INSTANCEOSPOLICIESCOMPLIANCE.fields_by_name['state'].enum_type = google_dot_cloud_dot_osconfig_dot_v1alpha_dot_config__common__pb2._OSPOLICYCOMPLIANCESTATE
_INSTANCEOSPOLICIESCOMPLIANCE.fields_by_name['os_policy_compliances'].message_type = _INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE
_INSTANCEOSPOLICIESCOMPLIANCE.fields_by_name['last_compliance_check_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTINSTANCEOSPOLICIESCOMPLIANCESRESPONSE.fields_by_name['instance_os_policies_compliances'].message_type = _INSTANCEOSPOLICIESCOMPLIANCE
DESCRIPTOR.message_types_by_name['InstanceOSPoliciesCompliance'] = _INSTANCEOSPOLICIESCOMPLIANCE
DESCRIPTOR.message_types_by_name['GetInstanceOSPoliciesComplianceRequest'] = _GETINSTANCEOSPOLICIESCOMPLIANCEREQUEST
DESCRIPTOR.message_types_by_name['ListInstanceOSPoliciesCompliancesRequest'] = _LISTINSTANCEOSPOLICIESCOMPLIANCESREQUEST
DESCRIPTOR.message_types_by_name['ListInstanceOSPoliciesCompliancesResponse'] = _LISTINSTANCEOSPOLICIESCOMPLIANCESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstanceOSPoliciesCompliance = _reflection.GeneratedProtocolMessageType('InstanceOSPoliciesCompliance', (_message.Message,), {

  'OSPolicyCompliance' : _reflection.GeneratedProtocolMessageType('OSPolicyCompliance', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE,
    '__module__' : 'google.cloud.osconfig.v1alpha.instance_os_policies_compliance_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance.OSPolicyCompliance)
    })
  ,
  'DESCRIPTOR' : _INSTANCEOSPOLICIESCOMPLIANCE,
  '__module__' : 'google.cloud.osconfig.v1alpha.instance_os_policies_compliance_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance)
  })
_sym_db.RegisterMessage(InstanceOSPoliciesCompliance)
_sym_db.RegisterMessage(InstanceOSPoliciesCompliance.OSPolicyCompliance)

GetInstanceOSPoliciesComplianceRequest = _reflection.GeneratedProtocolMessageType('GetInstanceOSPoliciesComplianceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINSTANCEOSPOLICIESCOMPLIANCEREQUEST,
  '__module__' : 'google.cloud.osconfig.v1alpha.instance_os_policies_compliance_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.GetInstanceOSPoliciesComplianceRequest)
  })
_sym_db.RegisterMessage(GetInstanceOSPoliciesComplianceRequest)

ListInstanceOSPoliciesCompliancesRequest = _reflection.GeneratedProtocolMessageType('ListInstanceOSPoliciesCompliancesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTINSTANCEOSPOLICIESCOMPLIANCESREQUEST,
  '__module__' : 'google.cloud.osconfig.v1alpha.instance_os_policies_compliance_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesRequest)
  })
_sym_db.RegisterMessage(ListInstanceOSPoliciesCompliancesRequest)

ListInstanceOSPoliciesCompliancesResponse = _reflection.GeneratedProtocolMessageType('ListInstanceOSPoliciesCompliancesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINSTANCEOSPOLICIESCOMPLIANCESRESPONSE,
  '__module__' : 'google.cloud.osconfig.v1alpha.instance_os_policies_compliance_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesResponse)
  })
_sym_db.RegisterMessage(ListInstanceOSPoliciesCompliancesResponse)


DESCRIPTOR._options = None
_INSTANCEOSPOLICIESCOMPLIANCE_OSPOLICYCOMPLIANCE.fields_by_name['os_policy_assignment']._options = None
_INSTANCEOSPOLICIESCOMPLIANCE.fields_by_name['name']._options = None
_INSTANCEOSPOLICIESCOMPLIANCE.fields_by_name['instance']._options = None
_INSTANCEOSPOLICIESCOMPLIANCE.fields_by_name['state']._options = None
_INSTANCEOSPOLICIESCOMPLIANCE.fields_by_name['detailed_state']._options = None
_INSTANCEOSPOLICIESCOMPLIANCE.fields_by_name['detailed_state_reason']._options = None
_INSTANCEOSPOLICIESCOMPLIANCE.fields_by_name['os_policy_compliances']._options = None
_INSTANCEOSPOLICIESCOMPLIANCE.fields_by_name['last_compliance_check_time']._options = None
_INSTANCEOSPOLICIESCOMPLIANCE.fields_by_name['last_compliance_run_id']._options = None
_INSTANCEOSPOLICIESCOMPLIANCE._options = None
_GETINSTANCEOSPOLICIESCOMPLIANCEREQUEST.fields_by_name['name']._options = None
_LISTINSTANCEOSPOLICIESCOMPLIANCESREQUEST.fields_by_name['parent']._options = None
# @@protoc_insertion_point(module_scope)
