# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gribi_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gribi_aft_pb2 as gribi__aft__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gribi_service.proto',
  package='gribi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x13gribi_service.proto\x12\x05gribi\x1a\x0fgribi_aft.proto\"\x9a\x03\n\x0c\x41\x46TOperation\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x18\n\x10network_instance\x18\x02 \x01(\t\x12)\n\x02op\x18\x03 \x01(\x0e\x32\x1d.gribi.AFTOperation.Operation\x12,\n\x04ipv4\x18\x04 \x01(\x0b\x32\x1c.gribi_aft.Afts.Ipv4EntryKeyH\x00\x12,\n\x04ipv6\x18\x05 \x01(\x0b\x32\x1c.gribi_aft.Afts.Ipv6EntryKeyH\x00\x12-\n\x04mpls\x18\x06 \x01(\x0b\x32\x1d.gribi_aft.Afts.LabelEntryKeyH\x00\x12\x39\n\x0enext_hop_group\x18\x07 \x01(\x0b\x32\x1f.gribi_aft.Afts.NextHopGroupKeyH\x00\x12.\n\x08next_hop\x18\x08 \x01(\x0b\x32\x1a.gribi_aft.Afts.NextHopKeyH\x00\":\n\tOperation\x12\x0b\n\x07INVALID\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\x0b\n\x07REPLACE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x42\x07\n\x05\x65ntry\"7\n\rModifyRequest\x12&\n\toperation\x18\x01 \x03(\x0b\x32\x13.gribi.AFTOperation\"i\n\tAFTResult\x12\n\n\x02id\x18\x01 \x01(\x04\x12\'\n\x06status\x18\x02 \x01(\x0e\x32\x17.gribi.AFTResult.Status\"\'\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\"2\n\x0eModifyResponse\x12 \n\x06result\x18\x01 \x03(\x0b\x32\x10.gribi.AFTResult2B\n\x05gRIBI\x12\x39\n\x06Modify\x12\x14.gribi.ModifyRequest\x1a\x15.gribi.ModifyResponse(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[gribi__aft__pb2.DESCRIPTOR,])



_AFTOPERATION_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='gribi.AFTOperation.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLACE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=391,
  serialized_end=449,
)
_sym_db.RegisterEnumDescriptor(_AFTOPERATION_OPERATION)

_AFTRESULT_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='gribi.AFTResult.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=583,
  serialized_end=622,
)
_sym_db.RegisterEnumDescriptor(_AFTRESULT_STATUS)


_AFTOPERATION = _descriptor.Descriptor(
  name='AFTOperation',
  full_name='gribi.AFTOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gribi.AFTOperation.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_instance', full_name='gribi.AFTOperation.network_instance', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='gribi.AFTOperation.op', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv4', full_name='gribi.AFTOperation.ipv4', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv6', full_name='gribi.AFTOperation.ipv6', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mpls', full_name='gribi.AFTOperation.mpls', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_hop_group', full_name='gribi.AFTOperation.next_hop_group', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_hop', full_name='gribi.AFTOperation.next_hop', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AFTOPERATION_OPERATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='entry', full_name='gribi.AFTOperation.entry',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=48,
  serialized_end=458,
)


_MODIFYREQUEST = _descriptor.Descriptor(
  name='ModifyRequest',
  full_name='gribi.ModifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='gribi.ModifyRequest.operation', index=0,
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
  serialized_start=460,
  serialized_end=515,
)


_AFTRESULT = _descriptor.Descriptor(
  name='AFTResult',
  full_name='gribi.AFTResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gribi.AFTResult.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='gribi.AFTResult.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AFTRESULT_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=517,
  serialized_end=622,
)


_MODIFYRESPONSE = _descriptor.Descriptor(
  name='ModifyResponse',
  full_name='gribi.ModifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='gribi.ModifyResponse.result', index=0,
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
  serialized_start=624,
  serialized_end=674,
)

_AFTOPERATION.fields_by_name['op'].enum_type = _AFTOPERATION_OPERATION
_AFTOPERATION.fields_by_name['ipv4'].message_type = gribi__aft__pb2._AFTS_IPV4ENTRYKEY
_AFTOPERATION.fields_by_name['ipv6'].message_type = gribi__aft__pb2._AFTS_IPV6ENTRYKEY
_AFTOPERATION.fields_by_name['mpls'].message_type = gribi__aft__pb2._AFTS_LABELENTRYKEY
_AFTOPERATION.fields_by_name['next_hop_group'].message_type = gribi__aft__pb2._AFTS_NEXTHOPGROUPKEY
_AFTOPERATION.fields_by_name['next_hop'].message_type = gribi__aft__pb2._AFTS_NEXTHOPKEY
_AFTOPERATION_OPERATION.containing_type = _AFTOPERATION
_AFTOPERATION.oneofs_by_name['entry'].fields.append(
  _AFTOPERATION.fields_by_name['ipv4'])
_AFTOPERATION.fields_by_name['ipv4'].containing_oneof = _AFTOPERATION.oneofs_by_name['entry']
_AFTOPERATION.oneofs_by_name['entry'].fields.append(
  _AFTOPERATION.fields_by_name['ipv6'])
_AFTOPERATION.fields_by_name['ipv6'].containing_oneof = _AFTOPERATION.oneofs_by_name['entry']
_AFTOPERATION.oneofs_by_name['entry'].fields.append(
  _AFTOPERATION.fields_by_name['mpls'])
_AFTOPERATION.fields_by_name['mpls'].containing_oneof = _AFTOPERATION.oneofs_by_name['entry']
_AFTOPERATION.oneofs_by_name['entry'].fields.append(
  _AFTOPERATION.fields_by_name['next_hop_group'])
_AFTOPERATION.fields_by_name['next_hop_group'].containing_oneof = _AFTOPERATION.oneofs_by_name['entry']
_AFTOPERATION.oneofs_by_name['entry'].fields.append(
  _AFTOPERATION.fields_by_name['next_hop'])
_AFTOPERATION.fields_by_name['next_hop'].containing_oneof = _AFTOPERATION.oneofs_by_name['entry']
_MODIFYREQUEST.fields_by_name['operation'].message_type = _AFTOPERATION
_AFTRESULT.fields_by_name['status'].enum_type = _AFTRESULT_STATUS
_AFTRESULT_STATUS.containing_type = _AFTRESULT
_MODIFYRESPONSE.fields_by_name['result'].message_type = _AFTRESULT
DESCRIPTOR.message_types_by_name['AFTOperation'] = _AFTOPERATION
DESCRIPTOR.message_types_by_name['ModifyRequest'] = _MODIFYREQUEST
DESCRIPTOR.message_types_by_name['AFTResult'] = _AFTRESULT
DESCRIPTOR.message_types_by_name['ModifyResponse'] = _MODIFYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AFTOperation = _reflection.GeneratedProtocolMessageType('AFTOperation', (_message.Message,), {
  'DESCRIPTOR' : _AFTOPERATION,
  '__module__' : 'gribi_service_pb2'
  # @@protoc_insertion_point(class_scope:gribi.AFTOperation)
  })
_sym_db.RegisterMessage(AFTOperation)

ModifyRequest = _reflection.GeneratedProtocolMessageType('ModifyRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODIFYREQUEST,
  '__module__' : 'gribi_service_pb2'
  # @@protoc_insertion_point(class_scope:gribi.ModifyRequest)
  })
_sym_db.RegisterMessage(ModifyRequest)

AFTResult = _reflection.GeneratedProtocolMessageType('AFTResult', (_message.Message,), {
  'DESCRIPTOR' : _AFTRESULT,
  '__module__' : 'gribi_service_pb2'
  # @@protoc_insertion_point(class_scope:gribi.AFTResult)
  })
_sym_db.RegisterMessage(AFTResult)

ModifyResponse = _reflection.GeneratedProtocolMessageType('ModifyResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODIFYRESPONSE,
  '__module__' : 'gribi_service_pb2'
  # @@protoc_insertion_point(class_scope:gribi.ModifyResponse)
  })
_sym_db.RegisterMessage(ModifyResponse)



_GRIBI = _descriptor.ServiceDescriptor(
  name='gRIBI',
  full_name='gribi.gRIBI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=676,
  serialized_end=742,
  methods=[
  _descriptor.MethodDescriptor(
    name='Modify',
    full_name='gribi.gRIBI.Modify',
    index=0,
    containing_service=None,
    input_type=_MODIFYREQUEST,
    output_type=_MODIFYRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRIBI)

DESCRIPTOR.services_by_name['gRIBI'] = _GRIBI

# @@protoc_insertion_point(module_scope)
