# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: validator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.cloud.asset_v1.proto import assets_pb2 as google_dot_cloud_dot_asset_dot_v1_dot_assets__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='validator.proto',
  package='validator',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fvalidator.proto\x12\tvalidator\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\"google/cloud/asset/v1/assets.proto\"\x9e\x01\n\x05\x41sset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nasset_type\x18\x02 \x01(\t\x12\x15\n\rancestry_path\x18\x03 \x01(\t\x12\x31\n\x08resource\x18\x04 \x01(\x0b\x32\x1f.google.cloud.asset.v1.Resource\x12)\n\niam_policy\x18\x05 \x01(\x0b\x32\x15.google.iam.v1.Policy\"l\n\tViolation\x12\x12\n\nconstraint\x18\x01 \x01(\t\x12\x10\n\x08resource\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12(\n\x08metadata\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Value\"2\n\x0e\x41\x64\x64\x44\x61taRequest\x12 \n\x06\x61ssets\x18\x01 \x03(\x0b\x32\x10.validator.Asset\"\x11\n\x0f\x41\x64\x64\x44\x61taResponse\"\x0e\n\x0c\x41uditRequest\"9\n\rAuditResponse\x12(\n\nviolations\x18\x01 \x03(\x0b\x32\x14.validator.Violation\"\x0e\n\x0cResetRequest\"\x0f\n\rResetResponse2\xcb\x01\n\tValidator\x12\x42\n\x07\x41\x64\x64\x44\x61ta\x12\x19.validator.AddDataRequest\x1a\x1a.validator.AddDataResponse\"\x00\x12<\n\x05\x41udit\x12\x17.validator.AuditRequest\x1a\x18.validator.AuditResponse\"\x00\x12<\n\x05Reset\x12\x17.validator.ResetRequest\x1a\x18.validator.ResetResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_iam_dot_v1_dot_policy__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_cloud_dot_asset_dot_v1_dot_assets__pb2.DESCRIPTOR,])




_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='validator.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='validator.Asset.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_type', full_name='validator.Asset.asset_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ancestry_path', full_name='validator.Asset.ancestry_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource', full_name='validator.Asset.resource', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iam_policy', full_name='validator.Asset.iam_policy', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=125,
  serialized_end=283,
)


_VIOLATION = _descriptor.Descriptor(
  name='Violation',
  full_name='validator.Violation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='constraint', full_name='validator.Violation.constraint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource', full_name='validator.Violation.resource', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='validator.Violation.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='validator.Violation.metadata', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=285,
  serialized_end=393,
)


_ADDDATAREQUEST = _descriptor.Descriptor(
  name='AddDataRequest',
  full_name='validator.AddDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='assets', full_name='validator.AddDataRequest.assets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=395,
  serialized_end=445,
)


_ADDDATARESPONSE = _descriptor.Descriptor(
  name='AddDataResponse',
  full_name='validator.AddDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=447,
  serialized_end=464,
)


_AUDITREQUEST = _descriptor.Descriptor(
  name='AuditRequest',
  full_name='validator.AuditRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=466,
  serialized_end=480,
)


_AUDITRESPONSE = _descriptor.Descriptor(
  name='AuditResponse',
  full_name='validator.AuditResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='violations', full_name='validator.AuditResponse.violations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=482,
  serialized_end=539,
)


_RESETREQUEST = _descriptor.Descriptor(
  name='ResetRequest',
  full_name='validator.ResetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=541,
  serialized_end=555,
)


_RESETRESPONSE = _descriptor.Descriptor(
  name='ResetResponse',
  full_name='validator.ResetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=557,
  serialized_end=572,
)

_ASSET.fields_by_name['resource'].message_type = google_dot_cloud_dot_asset_dot_v1_dot_assets__pb2._RESOURCE
_ASSET.fields_by_name['iam_policy'].message_type = google_dot_iam_dot_v1_dot_policy__pb2._POLICY
_VIOLATION.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_ADDDATAREQUEST.fields_by_name['assets'].message_type = _ASSET
_AUDITRESPONSE.fields_by_name['violations'].message_type = _VIOLATION
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['Violation'] = _VIOLATION
DESCRIPTOR.message_types_by_name['AddDataRequest'] = _ADDDATAREQUEST
DESCRIPTOR.message_types_by_name['AddDataResponse'] = _ADDDATARESPONSE
DESCRIPTOR.message_types_by_name['AuditRequest'] = _AUDITREQUEST
DESCRIPTOR.message_types_by_name['AuditResponse'] = _AUDITRESPONSE
DESCRIPTOR.message_types_by_name['ResetRequest'] = _RESETREQUEST
DESCRIPTOR.message_types_by_name['ResetResponse'] = _RESETRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), dict(
  DESCRIPTOR = _ASSET,
  __module__ = 'validator_pb2'
  # @@protoc_insertion_point(class_scope:validator.Asset)
  ))
_sym_db.RegisterMessage(Asset)

Violation = _reflection.GeneratedProtocolMessageType('Violation', (_message.Message,), dict(
  DESCRIPTOR = _VIOLATION,
  __module__ = 'validator_pb2'
  # @@protoc_insertion_point(class_scope:validator.Violation)
  ))
_sym_db.RegisterMessage(Violation)

AddDataRequest = _reflection.GeneratedProtocolMessageType('AddDataRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDDATAREQUEST,
  __module__ = 'validator_pb2'
  # @@protoc_insertion_point(class_scope:validator.AddDataRequest)
  ))
_sym_db.RegisterMessage(AddDataRequest)

AddDataResponse = _reflection.GeneratedProtocolMessageType('AddDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDDATARESPONSE,
  __module__ = 'validator_pb2'
  # @@protoc_insertion_point(class_scope:validator.AddDataResponse)
  ))
_sym_db.RegisterMessage(AddDataResponse)

AuditRequest = _reflection.GeneratedProtocolMessageType('AuditRequest', (_message.Message,), dict(
  DESCRIPTOR = _AUDITREQUEST,
  __module__ = 'validator_pb2'
  # @@protoc_insertion_point(class_scope:validator.AuditRequest)
  ))
_sym_db.RegisterMessage(AuditRequest)

AuditResponse = _reflection.GeneratedProtocolMessageType('AuditResponse', (_message.Message,), dict(
  DESCRIPTOR = _AUDITRESPONSE,
  __module__ = 'validator_pb2'
  # @@protoc_insertion_point(class_scope:validator.AuditResponse)
  ))
_sym_db.RegisterMessage(AuditResponse)

ResetRequest = _reflection.GeneratedProtocolMessageType('ResetRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESETREQUEST,
  __module__ = 'validator_pb2'
  # @@protoc_insertion_point(class_scope:validator.ResetRequest)
  ))
_sym_db.RegisterMessage(ResetRequest)

ResetResponse = _reflection.GeneratedProtocolMessageType('ResetResponse', (_message.Message,), dict(
  DESCRIPTOR = _RESETRESPONSE,
  __module__ = 'validator_pb2'
  # @@protoc_insertion_point(class_scope:validator.ResetResponse)
  ))
_sym_db.RegisterMessage(ResetResponse)



_VALIDATOR = _descriptor.ServiceDescriptor(
  name='Validator',
  full_name='validator.Validator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=575,
  serialized_end=778,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddData',
    full_name='validator.Validator.AddData',
    index=0,
    containing_service=None,
    input_type=_ADDDATAREQUEST,
    output_type=_ADDDATARESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Audit',
    full_name='validator.Validator.Audit',
    index=1,
    containing_service=None,
    input_type=_AUDITREQUEST,
    output_type=_AUDITRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Reset',
    full_name='validator.Validator.Reset',
    index=2,
    containing_service=None,
    input_type=_RESETREQUEST,
    output_type=_RESETRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_VALIDATOR)

DESCRIPTOR.services_by_name['Validator'] = _VALIDATOR

# @@protoc_insertion_point(module_scope)
