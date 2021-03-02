# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/serviceProfile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.as_pb.external.api import profiles_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_profiles__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chirpstack-api/as_pb/external/api/serviceProfile.proto',
  package='api',
  syntax='proto3',
  serialized_options=b'\n!io.chirpstack.api.as.external.apiB\023ServiceProfileProtoP\001Z7github.com/brocaar/chirpstack-api/go/v3/as/external/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6chirpstack-api/as_pb/external/api/serviceProfile.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x30\x63hirpstack-api/as_pb/external/api/profiles.proto\"K\n\x1b\x43reateServiceProfileRequest\x12,\n\x0fservice_profile\x18\x01 \x01(\x0b\x32\x13.api.ServiceProfile\"*\n\x1c\x43reateServiceProfileResponse\x12\n\n\x02id\x18\x01 \x01(\t\"&\n\x18GetServiceProfileRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xa9\x01\n\x19GetServiceProfileResponse\x12,\n\x0fservice_profile\x18\x01 \x01(\x0b\x32\x13.api.ServiceProfile\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"K\n\x1bUpdateServiceProfileRequest\x12,\n\x0fservice_profile\x18\x01 \x01(\x0b\x32\x13.api.ServiceProfile\")\n\x1b\x44\x65leteServiceProfileRequest\x12\n\n\x02id\x18\x01 \x01(\t\"c\n\x19ListServiceProfileRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\'\n\x0forganization_id\x18\x03 \x01(\x03R\x0eorganizationID\"\x84\x02\n\x16ServiceProfileListItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\x0forganization_id\x18\x03 \x01(\x03R\x0eorganizationID\x12*\n\x11network_server_id\x18\x04 \x01(\x03R\x0fnetworkServerID\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13network_server_name\x18\x07 \x01(\t\"^\n\x1aListServiceProfileResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12+\n\x06result\x18\x02 \x03(\x0b\x32\x1b.api.ServiceProfileListItem2\xbd\x04\n\x15ServiceProfileService\x12o\n\x06\x43reate\x12 .api.CreateServiceProfileRequest\x1a!.api.CreateServiceProfileResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/api/service-profiles:\x01*\x12h\n\x03Get\x12\x1d.api.GetServiceProfileRequest\x1a\x1e.api.GetServiceProfileResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/service-profiles/{id}\x12y\n\x06Update\x12 .api.UpdateServiceProfileRequest\x1a\x16.google.protobuf.Empty\"5\x82\xd3\xe4\x93\x02/\x1a*/api/service-profiles/{service_profile.id}:\x01*\x12\x66\n\x06\x44\x65lete\x12 .api.DeleteServiceProfileRequest\x1a\x16.google.protobuf.Empty\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/api/service-profiles/{id}\x12\x66\n\x04List\x12\x1e.api.ListServiceProfileRequest\x1a\x1f.api.ListServiceProfileResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/api/service-profilesBs\n!io.chirpstack.api.as.external.apiB\x13ServiceProfileProtoP\x01Z7github.com/brocaar/chirpstack-api/go/v3/as/external/apib\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,chirpstack__api_dot_as__pb_dot_external_dot_api_dot_profiles__pb2.DESCRIPTOR,])




_CREATESERVICEPROFILEREQUEST = _descriptor.Descriptor(
  name='CreateServiceProfileRequest',
  full_name='api.CreateServiceProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_profile', full_name='api.CreateServiceProfileRequest.service_profile', index=0,
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
  serialized_start=205,
  serialized_end=280,
)


_CREATESERVICEPROFILERESPONSE = _descriptor.Descriptor(
  name='CreateServiceProfileResponse',
  full_name='api.CreateServiceProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.CreateServiceProfileResponse.id', index=0,
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
  serialized_start=282,
  serialized_end=324,
)


_GETSERVICEPROFILEREQUEST = _descriptor.Descriptor(
  name='GetServiceProfileRequest',
  full_name='api.GetServiceProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.GetServiceProfileRequest.id', index=0,
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
  serialized_start=326,
  serialized_end=364,
)


_GETSERVICEPROFILERESPONSE = _descriptor.Descriptor(
  name='GetServiceProfileResponse',
  full_name='api.GetServiceProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_profile', full_name='api.GetServiceProfileResponse.service_profile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='api.GetServiceProfileResponse.created_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='api.GetServiceProfileResponse.updated_at', index=2,
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
  serialized_start=367,
  serialized_end=536,
)


_UPDATESERVICEPROFILEREQUEST = _descriptor.Descriptor(
  name='UpdateServiceProfileRequest',
  full_name='api.UpdateServiceProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_profile', full_name='api.UpdateServiceProfileRequest.service_profile', index=0,
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
  serialized_start=538,
  serialized_end=613,
)


_DELETESERVICEPROFILEREQUEST = _descriptor.Descriptor(
  name='DeleteServiceProfileRequest',
  full_name='api.DeleteServiceProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.DeleteServiceProfileRequest.id', index=0,
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
  serialized_start=615,
  serialized_end=656,
)


_LISTSERVICEPROFILEREQUEST = _descriptor.Descriptor(
  name='ListServiceProfileRequest',
  full_name='api.ListServiceProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='api.ListServiceProfileRequest.limit', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='api.ListServiceProfileRequest.offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='api.ListServiceProfileRequest.organization_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='organizationID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=658,
  serialized_end=757,
)


_SERVICEPROFILELISTITEM = _descriptor.Descriptor(
  name='ServiceProfileListItem',
  full_name='api.ServiceProfileListItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.ServiceProfileListItem.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.ServiceProfileListItem.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='api.ServiceProfileListItem.organization_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='organizationID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_server_id', full_name='api.ServiceProfileListItem.network_server_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='networkServerID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='api.ServiceProfileListItem.created_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='api.ServiceProfileListItem.updated_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_server_name', full_name='api.ServiceProfileListItem.network_server_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=760,
  serialized_end=1020,
)


_LISTSERVICEPROFILERESPONSE = _descriptor.Descriptor(
  name='ListServiceProfileResponse',
  full_name='api.ListServiceProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_count', full_name='api.ListServiceProfileResponse.total_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='api.ListServiceProfileResponse.result', index=1,
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
  serialized_start=1022,
  serialized_end=1116,
)

_CREATESERVICEPROFILEREQUEST.fields_by_name['service_profile'].message_type = chirpstack__api_dot_as__pb_dot_external_dot_api_dot_profiles__pb2._SERVICEPROFILE
_GETSERVICEPROFILERESPONSE.fields_by_name['service_profile'].message_type = chirpstack__api_dot_as__pb_dot_external_dot_api_dot_profiles__pb2._SERVICEPROFILE
_GETSERVICEPROFILERESPONSE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETSERVICEPROFILERESPONSE.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPDATESERVICEPROFILEREQUEST.fields_by_name['service_profile'].message_type = chirpstack__api_dot_as__pb_dot_external_dot_api_dot_profiles__pb2._SERVICEPROFILE
_SERVICEPROFILELISTITEM.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SERVICEPROFILELISTITEM.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTSERVICEPROFILERESPONSE.fields_by_name['result'].message_type = _SERVICEPROFILELISTITEM
DESCRIPTOR.message_types_by_name['CreateServiceProfileRequest'] = _CREATESERVICEPROFILEREQUEST
DESCRIPTOR.message_types_by_name['CreateServiceProfileResponse'] = _CREATESERVICEPROFILERESPONSE
DESCRIPTOR.message_types_by_name['GetServiceProfileRequest'] = _GETSERVICEPROFILEREQUEST
DESCRIPTOR.message_types_by_name['GetServiceProfileResponse'] = _GETSERVICEPROFILERESPONSE
DESCRIPTOR.message_types_by_name['UpdateServiceProfileRequest'] = _UPDATESERVICEPROFILEREQUEST
DESCRIPTOR.message_types_by_name['DeleteServiceProfileRequest'] = _DELETESERVICEPROFILEREQUEST
DESCRIPTOR.message_types_by_name['ListServiceProfileRequest'] = _LISTSERVICEPROFILEREQUEST
DESCRIPTOR.message_types_by_name['ServiceProfileListItem'] = _SERVICEPROFILELISTITEM
DESCRIPTOR.message_types_by_name['ListServiceProfileResponse'] = _LISTSERVICEPROFILERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateServiceProfileRequest = _reflection.GeneratedProtocolMessageType('CreateServiceProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVICEPROFILEREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.serviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateServiceProfileRequest)
  })
_sym_db.RegisterMessage(CreateServiceProfileRequest)

CreateServiceProfileResponse = _reflection.GeneratedProtocolMessageType('CreateServiceProfileResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVICEPROFILERESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.serviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateServiceProfileResponse)
  })
_sym_db.RegisterMessage(CreateServiceProfileResponse)

GetServiceProfileRequest = _reflection.GeneratedProtocolMessageType('GetServiceProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVICEPROFILEREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.serviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.GetServiceProfileRequest)
  })
_sym_db.RegisterMessage(GetServiceProfileRequest)

GetServiceProfileResponse = _reflection.GeneratedProtocolMessageType('GetServiceProfileResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVICEPROFILERESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.serviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.GetServiceProfileResponse)
  })
_sym_db.RegisterMessage(GetServiceProfileResponse)

UpdateServiceProfileRequest = _reflection.GeneratedProtocolMessageType('UpdateServiceProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESERVICEPROFILEREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.serviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateServiceProfileRequest)
  })
_sym_db.RegisterMessage(UpdateServiceProfileRequest)

DeleteServiceProfileRequest = _reflection.GeneratedProtocolMessageType('DeleteServiceProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESERVICEPROFILEREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.serviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.DeleteServiceProfileRequest)
  })
_sym_db.RegisterMessage(DeleteServiceProfileRequest)

ListServiceProfileRequest = _reflection.GeneratedProtocolMessageType('ListServiceProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVICEPROFILEREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.serviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.ListServiceProfileRequest)
  })
_sym_db.RegisterMessage(ListServiceProfileRequest)

ServiceProfileListItem = _reflection.GeneratedProtocolMessageType('ServiceProfileListItem', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEPROFILELISTITEM,
  '__module__' : 'chirpstack_api.as_pb.external.api.serviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.ServiceProfileListItem)
  })
_sym_db.RegisterMessage(ServiceProfileListItem)

ListServiceProfileResponse = _reflection.GeneratedProtocolMessageType('ListServiceProfileResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVICEPROFILERESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.serviceProfile_pb2'
  # @@protoc_insertion_point(class_scope:api.ListServiceProfileResponse)
  })
_sym_db.RegisterMessage(ListServiceProfileResponse)


DESCRIPTOR._options = None

_SERVICEPROFILESERVICE = _descriptor.ServiceDescriptor(
  name='ServiceProfileService',
  full_name='api.ServiceProfileService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1119,
  serialized_end=1692,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='api.ServiceProfileService.Create',
    index=0,
    containing_service=None,
    input_type=_CREATESERVICEPROFILEREQUEST,
    output_type=_CREATESERVICEPROFILERESPONSE,
    serialized_options=b'\202\323\344\223\002\032\"\025/api/service-profiles:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='api.ServiceProfileService.Get',
    index=1,
    containing_service=None,
    input_type=_GETSERVICEPROFILEREQUEST,
    output_type=_GETSERVICEPROFILERESPONSE,
    serialized_options=b'\202\323\344\223\002\034\022\032/api/service-profiles/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='api.ServiceProfileService.Update',
    index=2,
    containing_service=None,
    input_type=_UPDATESERVICEPROFILEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002/\032*/api/service-profiles/{service_profile.id}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='api.ServiceProfileService.Delete',
    index=3,
    containing_service=None,
    input_type=_DELETESERVICEPROFILEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\034*\032/api/service-profiles/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='api.ServiceProfileService.List',
    index=4,
    containing_service=None,
    input_type=_LISTSERVICEPROFILEREQUEST,
    output_type=_LISTSERVICEPROFILERESPONSE,
    serialized_options=b'\202\323\344\223\002\027\022\025/api/service-profiles',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICEPROFILESERVICE)

DESCRIPTOR.services_by_name['ServiceProfileService'] = _SERVICEPROFILESERVICE

# @@protoc_insertion_point(module_scope)
