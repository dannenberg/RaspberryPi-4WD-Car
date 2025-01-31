# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/billing_setup_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/errors/billing_setup_error.proto',
  package='google.ads.googleads.v9.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v9.errorsB\026BillingSetupErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/ads/googleads/v9/errors/billing_setup_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"\xfb\x05\n\x15\x42illingSetupErrorEnum\"\xe1\x05\n\x11\x42illingSetupError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\'\n#CANNOT_USE_EXISTING_AND_NEW_ACCOUNT\x10\x02\x12\'\n#CANNOT_REMOVE_STARTED_BILLING_SETUP\x10\x03\x12\x32\n.CANNOT_CHANGE_BILLING_TO_SAME_PAYMENTS_ACCOUNT\x10\x04\x12\x33\n/BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_STATUS\x10\x05\x12\x1c\n\x18INVALID_PAYMENTS_ACCOUNT\x10\x06\x12\x35\n1BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_CATEGORY\x10\x07\x12\x1b\n\x17INVALID_START_TIME_TYPE\x10\x08\x12#\n\x1fTHIRD_PARTY_ALREADY_HAS_BILLING\x10\t\x12\x1d\n\x19\x42ILLING_SETUP_IN_PROGRESS\x10\n\x12\x18\n\x14NO_SIGNUP_PERMISSION\x10\x0b\x12!\n\x1d\x43HANGE_OF_BILL_TO_IN_PROGRESS\x10\x0c\x12\x1e\n\x1aPAYMENTS_PROFILE_NOT_FOUND\x10\r\x12\x1e\n\x1aPAYMENTS_ACCOUNT_NOT_FOUND\x10\x0e\x12\x1f\n\x1bPAYMENTS_PROFILE_INELIGIBLE\x10\x0f\x12\x1f\n\x1bPAYMENTS_ACCOUNT_INELIGIBLE\x10\x10\x12$\n CUSTOMER_NEEDS_INTERNAL_APPROVAL\x10\x11\x12\x36\n2PAYMENTS_ACCOUNT_INELIGIBLE_CURRENCY_CODE_MISMATCH\x10\x13\x12 \n\x1c\x46UTURE_START_TIME_PROHIBITED\x10\x14\x42\xf1\x01\n\"com.google.ads.googleads.v9.errorsB\x16\x42illingSetupErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_BILLINGSETUPERRORENUM_BILLINGSETUPERROR = _descriptor.EnumDescriptor(
  name='BillingSetupError',
  full_name='google.ads.googleads.v9.errors.BillingSetupErrorEnum.BillingSetupError',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_USE_EXISTING_AND_NEW_ACCOUNT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_REMOVE_STARTED_BILLING_SETUP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CHANGE_BILLING_TO_SAME_PAYMENTS_ACCOUNT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_STATUS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PAYMENTS_ACCOUNT', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_CATEGORY', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_START_TIME_TYPE', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='THIRD_PARTY_ALREADY_HAS_BILLING', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BILLING_SETUP_IN_PROGRESS', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_SIGNUP_PERMISSION', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_OF_BILL_TO_IN_PROGRESS', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAYMENTS_PROFILE_NOT_FOUND', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAYMENTS_ACCOUNT_NOT_FOUND', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAYMENTS_PROFILE_INELIGIBLE', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAYMENTS_ACCOUNT_INELIGIBLE', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_NEEDS_INTERNAL_APPROVAL', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAYMENTS_ACCOUNT_INELIGIBLE_CURRENCY_CODE_MISMATCH', index=18, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FUTURE_START_TIME_PROHIBITED', index=19, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=149,
  serialized_end=886,
)
_sym_db.RegisterEnumDescriptor(_BILLINGSETUPERRORENUM_BILLINGSETUPERROR)


_BILLINGSETUPERRORENUM = _descriptor.Descriptor(
  name='BillingSetupErrorEnum',
  full_name='google.ads.googleads.v9.errors.BillingSetupErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BILLINGSETUPERRORENUM_BILLINGSETUPERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=886,
)

_BILLINGSETUPERRORENUM_BILLINGSETUPERROR.containing_type = _BILLINGSETUPERRORENUM
DESCRIPTOR.message_types_by_name['BillingSetupErrorEnum'] = _BILLINGSETUPERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BillingSetupErrorEnum = _reflection.GeneratedProtocolMessageType('BillingSetupErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGSETUPERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.billing_setup_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.BillingSetupErrorEnum)
  })
_sym_db.RegisterMessage(BillingSetupErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
