# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/fragmentationDeployment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.as_pb.external.api import multicastGroup_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chirpstack-api/as_pb/external/api/fragmentationDeployment.proto',
  package='api',
  syntax='proto3',
  serialized_options=b'Z7github.com/brocaar/chirpstack-api/go/v3/as/external/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?chirpstack-api/as_pb/external/api/fragmentationDeployment.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x36\x63hirpstack-api/as_pb/external/api/multicastGroup.proto\"\xb0\x02\n\x17\x46ragmentationDeployment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\x07\x64\x65v_eui\x18\x03 \x01(\tR\x06\x64\x65vEUI\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x12+\n\ngroup_type\x18\x05 \x01(\x0e\x32\x17.api.MulticastGroupType\x12\x18\n\x10ping_slot_period\x18\x06 \x01(\r\x12\x12\n\nredundancy\x18\x07 \x01(\r\x12\x32\n\x0funicast_timeout\x18\x08 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\r\n\x05state\x18\t \x01(\t\x12\x33\n\x0fnext_step_after\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x89\x03\n\x1aGetFragmentationDeployment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\x07\x64\x65v_eui\x18\x03 \x01(\tR\x06\x64\x65vEUI\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x12\x14\n\x0cpayload_size\x18\x05 \x01(\r\x12+\n\ngroup_type\x18\x06 \x01(\x0e\x32\x17.api.MulticastGroupType\x12\x18\n\x10ping_slot_period\x18\x07 \x01(\r\x12\x11\n\tfrag_size\x18\x08 \x01(\r\x12\x12\n\nredundancy\x18\t \x01(\r\x12\x32\n\x0funicast_timeout\x18\n \x01(\x0b\x32\x19.google.protobuf.Duration\x12\r\n\x05state\x18\x0b \x01(\t\x12\x14\n\x0c\x64\x65vice_state\x18\x0c \x01(\t\x12\x15\n\rerror_message\x18\r \x01(\t\x12\x33\n\x0fnext_step_after\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"_\n\x1e\x46ragmentationDeploymentRequest\x12=\n\x17\x66ragmentationDeployment\x18\x01 \x01(\x0b\x32\x1c.api.FragmentationDeployment\"-\n\x1f\x46ragmentationDeploymentResponse\x12\n\n\x02id\x18\x01 \x01(\t\"/\n!GetFragmentationDeploymentRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xc6\x01\n\"GetFragmentationDeploymentResponse\x12@\n\x17\x66ragmentationDeployment\x18\x01 \x01(\x0b\x32\x1f.api.GetFragmentationDeployment\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"f\n$UpdateFragmentationDeploymentRequest\x12>\n\x18\x66ragmentation_deployment\x18\x01 \x01(\x0b\x32\x1c.api.FragmentationDeployment\"2\n$DeleteFragmentationDeploymentRequest\x12\n\n\x02id\x18\x01 \x01(\t\"l\n\"ListFragmentationDeploymentRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0e\n\x06search\x18\x03 \x01(\t\x12\x17\n\x07\x64\x65v_eui\x18\x04 \x01(\tR\x06\x64\x65vEUI\"k\n#ListFragmentationDeploymentResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12/\n\x06result\x18\x02 \x03(\x0b\x32\x1f.api.GetFragmentationDeployment2\x82\x05\n\x1e\x46ragmentationDeploymentService\x12s\n\x06\x43reate\x12#.api.FragmentationDeploymentRequest\x1a$.api.FragmentationDeploymentResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/api/fragmentations:\x01*\x12x\n\x03Get\x12&.api.GetFragmentationDeploymentRequest\x1a\'.api.GetFragmentationDeploymentResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/api/fragmentations/{id}\x12\x89\x01\n\x06Update\x12).api.UpdateFragmentationDeploymentRequest\x1a\x16.google.protobuf.Empty\"<\x82\xd3\xe4\x93\x02\x36\x1a\x31/api/fragmentations/{fragmentation_deployment.id}:\x01*\x12m\n\x06\x44\x65lete\x12).api.DeleteFragmentationDeploymentRequest\x1a\x16.google.protobuf.Empty\" \x82\xd3\xe4\x93\x02\x1a*\x18/api/fragmentations/{id}\x12v\n\x04List\x12\'.api.ListFragmentationDeploymentRequest\x1a(.api.ListFragmentationDeploymentResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/api/fragmentationsB9Z7github.com/brocaar/chirpstack-api/go/v3/as/external/apib\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2.DESCRIPTOR,])




_FRAGMENTATIONDEPLOYMENT = _descriptor.Descriptor(
  name='FragmentationDeployment',
  full_name='api.FragmentationDeployment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.FragmentationDeployment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.FragmentationDeployment.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dev_eui', full_name='api.FragmentationDeployment.dev_eui', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='devEUI', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='api.FragmentationDeployment.payload', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_type', full_name='api.FragmentationDeployment.group_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ping_slot_period', full_name='api.FragmentationDeployment.ping_slot_period', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='redundancy', full_name='api.FragmentationDeployment.redundancy', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unicast_timeout', full_name='api.FragmentationDeployment.unicast_timeout', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='api.FragmentationDeployment.state', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_step_after', full_name='api.FragmentationDeployment.next_step_after', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=253,
  serialized_end=557,
)


_GETFRAGMENTATIONDEPLOYMENT = _descriptor.Descriptor(
  name='GetFragmentationDeployment',
  full_name='api.GetFragmentationDeployment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.GetFragmentationDeployment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.GetFragmentationDeployment.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dev_eui', full_name='api.GetFragmentationDeployment.dev_eui', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='devEUI', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='api.GetFragmentationDeployment.payload', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload_size', full_name='api.GetFragmentationDeployment.payload_size', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_type', full_name='api.GetFragmentationDeployment.group_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ping_slot_period', full_name='api.GetFragmentationDeployment.ping_slot_period', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frag_size', full_name='api.GetFragmentationDeployment.frag_size', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='redundancy', full_name='api.GetFragmentationDeployment.redundancy', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unicast_timeout', full_name='api.GetFragmentationDeployment.unicast_timeout', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='api.GetFragmentationDeployment.state', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_state', full_name='api.GetFragmentationDeployment.device_state', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='api.GetFragmentationDeployment.error_message', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_step_after', full_name='api.GetFragmentationDeployment.next_step_after', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=560,
  serialized_end=953,
)


_FRAGMENTATIONDEPLOYMENTREQUEST = _descriptor.Descriptor(
  name='FragmentationDeploymentRequest',
  full_name='api.FragmentationDeploymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fragmentationDeployment', full_name='api.FragmentationDeploymentRequest.fragmentationDeployment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=955,
  serialized_end=1050,
)


_FRAGMENTATIONDEPLOYMENTRESPONSE = _descriptor.Descriptor(
  name='FragmentationDeploymentResponse',
  full_name='api.FragmentationDeploymentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.FragmentationDeploymentResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1052,
  serialized_end=1097,
)


_GETFRAGMENTATIONDEPLOYMENTREQUEST = _descriptor.Descriptor(
  name='GetFragmentationDeploymentRequest',
  full_name='api.GetFragmentationDeploymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.GetFragmentationDeploymentRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1099,
  serialized_end=1146,
)


_GETFRAGMENTATIONDEPLOYMENTRESPONSE = _descriptor.Descriptor(
  name='GetFragmentationDeploymentResponse',
  full_name='api.GetFragmentationDeploymentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fragmentationDeployment', full_name='api.GetFragmentationDeploymentResponse.fragmentationDeployment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='api.GetFragmentationDeploymentResponse.created_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='api.GetFragmentationDeploymentResponse.updated_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1149,
  serialized_end=1347,
)


_UPDATEFRAGMENTATIONDEPLOYMENTREQUEST = _descriptor.Descriptor(
  name='UpdateFragmentationDeploymentRequest',
  full_name='api.UpdateFragmentationDeploymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fragmentation_deployment', full_name='api.UpdateFragmentationDeploymentRequest.fragmentation_deployment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1349,
  serialized_end=1451,
)


_DELETEFRAGMENTATIONDEPLOYMENTREQUEST = _descriptor.Descriptor(
  name='DeleteFragmentationDeploymentRequest',
  full_name='api.DeleteFragmentationDeploymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.DeleteFragmentationDeploymentRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1453,
  serialized_end=1503,
)


_LISTFRAGMENTATIONDEPLOYMENTREQUEST = _descriptor.Descriptor(
  name='ListFragmentationDeploymentRequest',
  full_name='api.ListFragmentationDeploymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='api.ListFragmentationDeploymentRequest.limit', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='api.ListFragmentationDeploymentRequest.offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='search', full_name='api.ListFragmentationDeploymentRequest.search', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dev_eui', full_name='api.ListFragmentationDeploymentRequest.dev_eui', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='devEUI', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1505,
  serialized_end=1613,
)


_LISTFRAGMENTATIONDEPLOYMENTRESPONSE = _descriptor.Descriptor(
  name='ListFragmentationDeploymentResponse',
  full_name='api.ListFragmentationDeploymentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_count', full_name='api.ListFragmentationDeploymentResponse.total_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='api.ListFragmentationDeploymentResponse.result', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1615,
  serialized_end=1722,
)

_FRAGMENTATIONDEPLOYMENT.fields_by_name['group_type'].enum_type = chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2._MULTICASTGROUPTYPE
_FRAGMENTATIONDEPLOYMENT.fields_by_name['unicast_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_FRAGMENTATIONDEPLOYMENT.fields_by_name['next_step_after'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETFRAGMENTATIONDEPLOYMENT.fields_by_name['group_type'].enum_type = chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2._MULTICASTGROUPTYPE
_GETFRAGMENTATIONDEPLOYMENT.fields_by_name['unicast_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_GETFRAGMENTATIONDEPLOYMENT.fields_by_name['next_step_after'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FRAGMENTATIONDEPLOYMENTREQUEST.fields_by_name['fragmentationDeployment'].message_type = _FRAGMENTATIONDEPLOYMENT
_GETFRAGMENTATIONDEPLOYMENTRESPONSE.fields_by_name['fragmentationDeployment'].message_type = _GETFRAGMENTATIONDEPLOYMENT
_GETFRAGMENTATIONDEPLOYMENTRESPONSE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETFRAGMENTATIONDEPLOYMENTRESPONSE.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPDATEFRAGMENTATIONDEPLOYMENTREQUEST.fields_by_name['fragmentation_deployment'].message_type = _FRAGMENTATIONDEPLOYMENT
_LISTFRAGMENTATIONDEPLOYMENTRESPONSE.fields_by_name['result'].message_type = _GETFRAGMENTATIONDEPLOYMENT
DESCRIPTOR.message_types_by_name['FragmentationDeployment'] = _FRAGMENTATIONDEPLOYMENT
DESCRIPTOR.message_types_by_name['GetFragmentationDeployment'] = _GETFRAGMENTATIONDEPLOYMENT
DESCRIPTOR.message_types_by_name['FragmentationDeploymentRequest'] = _FRAGMENTATIONDEPLOYMENTREQUEST
DESCRIPTOR.message_types_by_name['FragmentationDeploymentResponse'] = _FRAGMENTATIONDEPLOYMENTRESPONSE
DESCRIPTOR.message_types_by_name['GetFragmentationDeploymentRequest'] = _GETFRAGMENTATIONDEPLOYMENTREQUEST
DESCRIPTOR.message_types_by_name['GetFragmentationDeploymentResponse'] = _GETFRAGMENTATIONDEPLOYMENTRESPONSE
DESCRIPTOR.message_types_by_name['UpdateFragmentationDeploymentRequest'] = _UPDATEFRAGMENTATIONDEPLOYMENTREQUEST
DESCRIPTOR.message_types_by_name['DeleteFragmentationDeploymentRequest'] = _DELETEFRAGMENTATIONDEPLOYMENTREQUEST
DESCRIPTOR.message_types_by_name['ListFragmentationDeploymentRequest'] = _LISTFRAGMENTATIONDEPLOYMENTREQUEST
DESCRIPTOR.message_types_by_name['ListFragmentationDeploymentResponse'] = _LISTFRAGMENTATIONDEPLOYMENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FragmentationDeployment = _reflection.GeneratedProtocolMessageType('FragmentationDeployment', (_message.Message,), {
  'DESCRIPTOR' : _FRAGMENTATIONDEPLOYMENT,
  '__module__' : 'chirpstack_api.as_pb.external.api.fragmentationDeployment_pb2'
  # @@protoc_insertion_point(class_scope:api.FragmentationDeployment)
  })
_sym_db.RegisterMessage(FragmentationDeployment)

GetFragmentationDeployment = _reflection.GeneratedProtocolMessageType('GetFragmentationDeployment', (_message.Message,), {
  'DESCRIPTOR' : _GETFRAGMENTATIONDEPLOYMENT,
  '__module__' : 'chirpstack_api.as_pb.external.api.fragmentationDeployment_pb2'
  # @@protoc_insertion_point(class_scope:api.GetFragmentationDeployment)
  })
_sym_db.RegisterMessage(GetFragmentationDeployment)

FragmentationDeploymentRequest = _reflection.GeneratedProtocolMessageType('FragmentationDeploymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _FRAGMENTATIONDEPLOYMENTREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.fragmentationDeployment_pb2'
  # @@protoc_insertion_point(class_scope:api.FragmentationDeploymentRequest)
  })
_sym_db.RegisterMessage(FragmentationDeploymentRequest)

FragmentationDeploymentResponse = _reflection.GeneratedProtocolMessageType('FragmentationDeploymentResponse', (_message.Message,), {
  'DESCRIPTOR' : _FRAGMENTATIONDEPLOYMENTRESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.fragmentationDeployment_pb2'
  # @@protoc_insertion_point(class_scope:api.FragmentationDeploymentResponse)
  })
_sym_db.RegisterMessage(FragmentationDeploymentResponse)

GetFragmentationDeploymentRequest = _reflection.GeneratedProtocolMessageType('GetFragmentationDeploymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFRAGMENTATIONDEPLOYMENTREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.fragmentationDeployment_pb2'
  # @@protoc_insertion_point(class_scope:api.GetFragmentationDeploymentRequest)
  })
_sym_db.RegisterMessage(GetFragmentationDeploymentRequest)

GetFragmentationDeploymentResponse = _reflection.GeneratedProtocolMessageType('GetFragmentationDeploymentResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFRAGMENTATIONDEPLOYMENTRESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.fragmentationDeployment_pb2'
  # @@protoc_insertion_point(class_scope:api.GetFragmentationDeploymentResponse)
  })
_sym_db.RegisterMessage(GetFragmentationDeploymentResponse)

UpdateFragmentationDeploymentRequest = _reflection.GeneratedProtocolMessageType('UpdateFragmentationDeploymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFRAGMENTATIONDEPLOYMENTREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.fragmentationDeployment_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateFragmentationDeploymentRequest)
  })
_sym_db.RegisterMessage(UpdateFragmentationDeploymentRequest)

DeleteFragmentationDeploymentRequest = _reflection.GeneratedProtocolMessageType('DeleteFragmentationDeploymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFRAGMENTATIONDEPLOYMENTREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.fragmentationDeployment_pb2'
  # @@protoc_insertion_point(class_scope:api.DeleteFragmentationDeploymentRequest)
  })
_sym_db.RegisterMessage(DeleteFragmentationDeploymentRequest)

ListFragmentationDeploymentRequest = _reflection.GeneratedProtocolMessageType('ListFragmentationDeploymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFRAGMENTATIONDEPLOYMENTREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.fragmentationDeployment_pb2'
  # @@protoc_insertion_point(class_scope:api.ListFragmentationDeploymentRequest)
  })
_sym_db.RegisterMessage(ListFragmentationDeploymentRequest)

ListFragmentationDeploymentResponse = _reflection.GeneratedProtocolMessageType('ListFragmentationDeploymentResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFRAGMENTATIONDEPLOYMENTRESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.fragmentationDeployment_pb2'
  # @@protoc_insertion_point(class_scope:api.ListFragmentationDeploymentResponse)
  })
_sym_db.RegisterMessage(ListFragmentationDeploymentResponse)


DESCRIPTOR._options = None

_FRAGMENTATIONDEPLOYMENTSERVICE = _descriptor.ServiceDescriptor(
  name='FragmentationDeploymentService',
  full_name='api.FragmentationDeploymentService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1725,
  serialized_end=2367,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='api.FragmentationDeploymentService.Create',
    index=0,
    containing_service=None,
    input_type=_FRAGMENTATIONDEPLOYMENTREQUEST,
    output_type=_FRAGMENTATIONDEPLOYMENTRESPONSE,
    serialized_options=b'\202\323\344\223\002\030\"\023/api/fragmentations:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='api.FragmentationDeploymentService.Get',
    index=1,
    containing_service=None,
    input_type=_GETFRAGMENTATIONDEPLOYMENTREQUEST,
    output_type=_GETFRAGMENTATIONDEPLOYMENTRESPONSE,
    serialized_options=b'\202\323\344\223\002\032\022\030/api/fragmentations/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='api.FragmentationDeploymentService.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATEFRAGMENTATIONDEPLOYMENTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\0026\0321/api/fragmentations/{fragmentation_deployment.id}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='api.FragmentationDeploymentService.Delete',
    index=3,
    containing_service=None,
    input_type=_DELETEFRAGMENTATIONDEPLOYMENTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\032*\030/api/fragmentations/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='api.FragmentationDeploymentService.List',
    index=4,
    containing_service=None,
    input_type=_LISTFRAGMENTATIONDEPLOYMENTREQUEST,
    output_type=_LISTFRAGMENTATIONDEPLOYMENTRESPONSE,
    serialized_options=b'\202\323\344\223\002\025\022\023/api/fragmentations',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FRAGMENTATIONDEPLOYMENTSERVICE)

DESCRIPTOR.services_by_name['FragmentationDeploymentService'] = _FRAGMENTATIONDEPLOYMENTSERVICE

# @@protoc_insertion_point(module_scope)
