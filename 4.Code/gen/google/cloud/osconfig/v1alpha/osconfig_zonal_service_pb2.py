# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/osconfig/v1alpha/osconfig_zonal_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.osconfig.v1alpha import instance_os_policies_compliance_pb2 as google_dot_cloud_dot_osconfig_dot_v1alpha_dot_instance__os__policies__compliance__pb2
from google.cloud.osconfig.v1alpha import inventory_pb2 as google_dot_cloud_dot_osconfig_dot_v1alpha_dot_inventory__pb2
from google.cloud.osconfig.v1alpha import os_policy_assignments_pb2 as google_dot_cloud_dot_osconfig_dot_v1alpha_dot_os__policy__assignments__pb2
from google.cloud.osconfig.v1alpha import vulnerability_pb2 as google_dot_cloud_dot_osconfig_dot_v1alpha_dot_vulnerability__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/osconfig/v1alpha/osconfig_zonal_service.proto',
  package='google.cloud.osconfig.v1alpha',
  syntax='proto3',
  serialized_options=b'\n!com.google.cloud.osconfig.v1alphaB\031OsConfigZonalServiceProtoP\001ZEgoogle.golang.org/genproto/googleapis/cloud/osconfig/v1alpha;osconfig\252\002\035Google.Cloud.OsConfig.V1Alpha\312\002\035Google\\Cloud\\OsConfig\\V1alpha\352\002 Google::Cloud::OsConfig::V1alpha\352A_\n\037compute.googleapis.com/Instance\022<projects/{project}/locations/{location}/instances/{instance}',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:google/cloud/osconfig/v1alpha/osconfig_zonal_service.proto\x12\x1dgoogle.cloud.osconfig.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a\x43google/cloud/osconfig/v1alpha/instance_os_policies_compliance.proto\x1a-google/cloud/osconfig/v1alpha/inventory.proto\x1a\x39google/cloud/osconfig/v1alpha/os_policy_assignments.proto\x1a\x31google/cloud/osconfig/v1alpha/vulnerability.proto\x1a#google/longrunning/operations.proto2\xd4\x18\n\x14OsConfigZonalService\x12\xc8\x02\n\x18\x43reateOSPolicyAssignment\x12>.google.cloud.osconfig.v1alpha.CreateOSPolicyAssignmentRequest\x1a\x1d.google.longrunning.Operation\"\xcc\x01\xca\x41\x39\n\x12OSPolicyAssignment\x12#OSPolicyAssignmentOperationMetadata\xda\x41\x33parent,os_policy_assignment,os_policy_assignment_id\x82\xd3\xe4\x93\x02T\"</v1alpha/{parent=projects/*/locations/*}/osPolicyAssignments:\x14os_policy_assignment\x12\xca\x02\n\x18UpdateOSPolicyAssignment\x12>.google.cloud.osconfig.v1alpha.UpdateOSPolicyAssignmentRequest\x1a\x1d.google.longrunning.Operation\"\xce\x01\xca\x41\x39\n\x12OSPolicyAssignment\x12#OSPolicyAssignmentOperationMetadata\xda\x41 os_policy_assignment,update_mask\x82\xd3\xe4\x93\x02i2Q/v1alpha/{os_policy_assignment.name=projects/*/locations/*/osPolicyAssignments/*}:\x14os_policy_assignment\x12\xd4\x01\n\x15GetOSPolicyAssignment\x12;.google.cloud.osconfig.v1alpha.GetOSPolicyAssignmentRequest\x1a\x31.google.cloud.osconfig.v1alpha.OSPolicyAssignment\"K\xda\x41\x04name\x82\xd3\xe4\x93\x02>\x12</v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}\x12\xe7\x01\n\x17ListOSPolicyAssignments\x12=.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentsRequest\x1a>.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentsResponse\"M\xda\x41\x06parent\x82\xd3\xe4\x93\x02>\x12</v1alpha/{parent=projects/*/locations/*}/osPolicyAssignments\x12\x8b\x02\n\x1fListOSPolicyAssignmentRevisions\x12\x45.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentRevisionsRequest\x1a\x46.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentRevisionsResponse\"Y\xda\x41\x04name\x82\xd3\xe4\x93\x02L\x12J/v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}:listRevisions\x12\x86\x02\n\x18\x44\x65leteOSPolicyAssignment\x12>.google.cloud.osconfig.v1alpha.DeleteOSPolicyAssignmentRequest\x1a\x1d.google.longrunning.Operation\"\x8a\x01\xca\x41<\n\x15google.protobuf.Empty\x12#OSPolicyAssignmentOperationMetadata\xda\x41\x04name\x82\xd3\xe4\x93\x02>*</v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}\x12\xfc\x01\n\x1fGetInstanceOSPoliciesCompliance\x12\x45.google.cloud.osconfig.v1alpha.GetInstanceOSPoliciesComplianceRequest\x1a;.google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance\"U\xda\x41\x04name\x82\xd3\xe4\x93\x02H\x12\x46/v1alpha/{name=projects/*/locations/*/instanceOSPoliciesCompliances/*}\x12\x8f\x02\n!ListInstanceOSPoliciesCompliances\x12G.google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesRequest\x1aH.google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesResponse\"W\xda\x41\x06parent\x82\xd3\xe4\x93\x02H\x12\x46/v1alpha/{parent=projects/*/locations/*}/instanceOSPoliciesCompliances\x12\xb9\x01\n\x0cGetInventory\x12\x32.google.cloud.osconfig.v1alpha.GetInventoryRequest\x1a(.google.cloud.osconfig.v1alpha.Inventory\"K\xda\x41\x04name\x82\xd3\xe4\x93\x02>\x12</v1alpha/{name=projects/*/locations/*/instances/*/inventory}\x12\xd3\x01\n\x0fListInventories\x12\x35.google.cloud.osconfig.v1alpha.ListInventoriesRequest\x1a\x36.google.cloud.osconfig.v1alpha.ListInventoriesResponse\"Q\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x42\x12@/v1alpha/{parent=projects/*/locations/*/instances/*}/inventories\x12\xe1\x01\n\x16GetVulnerabilityReport\x12<.google.cloud.osconfig.v1alpha.GetVulnerabilityReportRequest\x1a\x32.google.cloud.osconfig.v1alpha.VulnerabilityReport\"U\xda\x41\x04name\x82\xd3\xe4\x93\x02H\x12\x46/v1alpha/{name=projects/*/locations/*/instances/*/vulnerabilityReport}\x12\xf7\x01\n\x18ListVulnerabilityReports\x12>.google.cloud.osconfig.v1alpha.ListVulnerabilityReportsRequest\x1a?.google.cloud.osconfig.v1alpha.ListVulnerabilityReportsResponse\"Z\xda\x41\x06parent\x82\xd3\xe4\x93\x02K\x12I/v1alpha/{parent=projects/*/locations/*/instances/*}/vulnerabilityReports\x1aK\xca\x41\x17osconfig.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xcc\x02\n!com.google.cloud.osconfig.v1alphaB\x19OsConfigZonalServiceProtoP\x01ZEgoogle.golang.org/genproto/googleapis/cloud/osconfig/v1alpha;osconfig\xaa\x02\x1dGoogle.Cloud.OsConfig.V1Alpha\xca\x02\x1dGoogle\\Cloud\\OsConfig\\V1alpha\xea\x02 Google::Cloud::OsConfig::V1alpha\xea\x41_\n\x1f\x63ompute.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_osconfig_dot_v1alpha_dot_instance__os__policies__compliance__pb2.DESCRIPTOR,google_dot_cloud_dot_osconfig_dot_v1alpha_dot_inventory__pb2.DESCRIPTOR,google_dot_cloud_dot_osconfig_dot_v1alpha_dot_os__policy__assignments__pb2.DESCRIPTOR,google_dot_cloud_dot_osconfig_dot_v1alpha_dot_vulnerability__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_OSCONFIGZONALSERVICE = _descriptor.ServiceDescriptor(
  name='OsConfigZonalService',
  full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\027osconfig.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  create_key=_descriptor._internal_create_key,
  serialized_start=439,
  serialized_end=3595,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateOSPolicyAssignment',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.CreateOSPolicyAssignment',
    index=0,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_os__policy__assignments__pb2._CREATEOSPOLICYASSIGNMENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A9\n\022OSPolicyAssignment\022#OSPolicyAssignmentOperationMetadata\332A3parent,os_policy_assignment,os_policy_assignment_id\202\323\344\223\002T\"</v1alpha/{parent=projects/*/locations/*}/osPolicyAssignments:\024os_policy_assignment',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateOSPolicyAssignment',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.UpdateOSPolicyAssignment',
    index=1,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_os__policy__assignments__pb2._UPDATEOSPOLICYASSIGNMENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A9\n\022OSPolicyAssignment\022#OSPolicyAssignmentOperationMetadata\332A os_policy_assignment,update_mask\202\323\344\223\002i2Q/v1alpha/{os_policy_assignment.name=projects/*/locations/*/osPolicyAssignments/*}:\024os_policy_assignment',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetOSPolicyAssignment',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.GetOSPolicyAssignment',
    index=2,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_os__policy__assignments__pb2._GETOSPOLICYASSIGNMENTREQUEST,
    output_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_os__policy__assignments__pb2._OSPOLICYASSIGNMENT,
    serialized_options=b'\332A\004name\202\323\344\223\002>\022</v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListOSPolicyAssignments',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.ListOSPolicyAssignments',
    index=3,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_os__policy__assignments__pb2._LISTOSPOLICYASSIGNMENTSREQUEST,
    output_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_os__policy__assignments__pb2._LISTOSPOLICYASSIGNMENTSRESPONSE,
    serialized_options=b'\332A\006parent\202\323\344\223\002>\022</v1alpha/{parent=projects/*/locations/*}/osPolicyAssignments',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListOSPolicyAssignmentRevisions',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.ListOSPolicyAssignmentRevisions',
    index=4,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_os__policy__assignments__pb2._LISTOSPOLICYASSIGNMENTREVISIONSREQUEST,
    output_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_os__policy__assignments__pb2._LISTOSPOLICYASSIGNMENTREVISIONSRESPONSE,
    serialized_options=b'\332A\004name\202\323\344\223\002L\022J/v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}:listRevisions',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteOSPolicyAssignment',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.DeleteOSPolicyAssignment',
    index=5,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_os__policy__assignments__pb2._DELETEOSPOLICYASSIGNMENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A<\n\025google.protobuf.Empty\022#OSPolicyAssignmentOperationMetadata\332A\004name\202\323\344\223\002>*</v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetInstanceOSPoliciesCompliance',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.GetInstanceOSPoliciesCompliance',
    index=6,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_instance__os__policies__compliance__pb2._GETINSTANCEOSPOLICIESCOMPLIANCEREQUEST,
    output_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_instance__os__policies__compliance__pb2._INSTANCEOSPOLICIESCOMPLIANCE,
    serialized_options=b'\332A\004name\202\323\344\223\002H\022F/v1alpha/{name=projects/*/locations/*/instanceOSPoliciesCompliances/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListInstanceOSPoliciesCompliances',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.ListInstanceOSPoliciesCompliances',
    index=7,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_instance__os__policies__compliance__pb2._LISTINSTANCEOSPOLICIESCOMPLIANCESREQUEST,
    output_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_instance__os__policies__compliance__pb2._LISTINSTANCEOSPOLICIESCOMPLIANCESRESPONSE,
    serialized_options=b'\332A\006parent\202\323\344\223\002H\022F/v1alpha/{parent=projects/*/locations/*}/instanceOSPoliciesCompliances',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetInventory',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.GetInventory',
    index=8,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_inventory__pb2._GETINVENTORYREQUEST,
    output_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_inventory__pb2._INVENTORY,
    serialized_options=b'\332A\004name\202\323\344\223\002>\022</v1alpha/{name=projects/*/locations/*/instances/*/inventory}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListInventories',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.ListInventories',
    index=9,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_inventory__pb2._LISTINVENTORIESREQUEST,
    output_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_inventory__pb2._LISTINVENTORIESRESPONSE,
    serialized_options=b'\332A\006parent\202\323\344\223\002B\022@/v1alpha/{parent=projects/*/locations/*/instances/*}/inventories',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetVulnerabilityReport',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.GetVulnerabilityReport',
    index=10,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_vulnerability__pb2._GETVULNERABILITYREPORTREQUEST,
    output_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_vulnerability__pb2._VULNERABILITYREPORT,
    serialized_options=b'\332A\004name\202\323\344\223\002H\022F/v1alpha/{name=projects/*/locations/*/instances/*/vulnerabilityReport}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListVulnerabilityReports',
    full_name='google.cloud.osconfig.v1alpha.OsConfigZonalService.ListVulnerabilityReports',
    index=11,
    containing_service=None,
    input_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_vulnerability__pb2._LISTVULNERABILITYREPORTSREQUEST,
    output_type=google_dot_cloud_dot_osconfig_dot_v1alpha_dot_vulnerability__pb2._LISTVULNERABILITYREPORTSRESPONSE,
    serialized_options=b'\332A\006parent\202\323\344\223\002K\022I/v1alpha/{parent=projects/*/locations/*/instances/*}/vulnerabilityReports',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OSCONFIGZONALSERVICE)

DESCRIPTOR.services_by_name['OsConfigZonalService'] = _OSCONFIGZONALSERVICE

# @@protoc_insertion_point(module_scope)
