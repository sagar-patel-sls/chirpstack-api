# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/gatewayProfile.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6chirpstack-api/as_pb/external/api/gatewayProfile.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\"chirpstack-api/common/common.proto\"\xd4\x01\n\x0eGatewayProfile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\x11network_server_id\x18\x03 \x01(\x03R\x0fnetworkServerID\x12\x10\n\x08\x63hannels\x18\x04 \x03(\r\x12\x37\n\x0e\x65xtra_channels\x18\x05 \x03(\x0b\x32\x1f.api.GatewayProfileExtraChannel\x12\x31\n\x0estats_interval\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\"\xdb\x01\n\x16GatewayProfileListItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\x11network_server_id\x18\x03 \x01(\x03R\x0fnetworkServerID\x12\x1b\n\x13network_server_name\x18\x07 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x96\x01\n\x1aGatewayProfileExtraChannel\x12&\n\nmodulation\x18\x01 \x01(\x0e\x32\x12.common.Modulation\x12\x11\n\tfrequency\x18\x02 \x01(\r\x12\x11\n\tbandwidth\x18\x03 \x01(\r\x12\x0f\n\x07\x62itrate\x18\x04 \x01(\r\x12\x19\n\x11spreading_factors\x18\x05 \x03(\r\"K\n\x1b\x43reateGatewayProfileRequest\x12,\n\x0fgateway_profile\x18\x01 \x01(\x0b\x32\x13.api.GatewayProfile\"*\n\x1c\x43reateGatewayProfileResponse\x12\n\n\x02id\x18\x01 \x01(\t\"&\n\x18GetGatewayProfileRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xa9\x01\n\x19GetGatewayProfileResponse\x12,\n\x0fgateway_profile\x18\x01 \x01(\x0b\x32\x13.api.GatewayProfile\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"K\n\x1bUpdateGatewayProfileRequest\x12,\n\x0fgateway_profile\x18\x01 \x01(\x0b\x32\x13.api.GatewayProfile\")\n\x1b\x44\x65leteGatewayProfileRequest\x12\n\n\x02id\x18\x01 \x01(\t\"g\n\x1aListGatewayProfilesRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12*\n\x11network_server_id\x18\x03 \x01(\x03R\x0fnetworkServerID\"_\n\x1bListGatewayProfilesResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12+\n\x06result\x18\x02 \x03(\x0b\x32\x1b.api.GatewayProfileListItem2\xbf\x04\n\x15GatewayProfileService\x12o\n\x06\x43reate\x12 .api.CreateGatewayProfileRequest\x1a!.api.CreateGatewayProfileResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/api/gateway-profiles:\x01*\x12h\n\x03Get\x12\x1d.api.GetGatewayProfileRequest\x1a\x1e.api.GetGatewayProfileResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/gateway-profiles/{id}\x12y\n\x06Update\x12 .api.UpdateGatewayProfileRequest\x1a\x16.google.protobuf.Empty\"5\x82\xd3\xe4\x93\x02/\x1a*/api/gateway-profiles/{gateway_profile.id}:\x01*\x12\x66\n\x06\x44\x65lete\x12 .api.DeleteGatewayProfileRequest\x1a\x16.google.protobuf.Empty\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/api/gateway-profiles/{id}\x12h\n\x04List\x12\x1f.api.ListGatewayProfilesRequest\x1a .api.ListGatewayProfilesResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/api/gateway-profilesB{\n!io.chirpstack.api.as.external.apiB\x13GatewayProfileProtoP\x01Z?github.com/sagar-patel-sls/chirpstack-api/go/v3/as/external/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.as_pb.external.api.gatewayProfile_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.chirpstack.api.as.external.apiB\023GatewayProfileProtoP\001Z?github.com/sagar-patel-sls/chirpstack-api/go/v3/as/external/api'
  _GATEWAYPROFILESERVICE.methods_by_name['Create']._options = None
  _GATEWAYPROFILESERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\032\"\025/api/gateway-profiles:\001*'
  _GATEWAYPROFILESERVICE.methods_by_name['Get']._options = None
  _GATEWAYPROFILESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\034\022\032/api/gateway-profiles/{id}'
  _GATEWAYPROFILESERVICE.methods_by_name['Update']._options = None
  _GATEWAYPROFILESERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002/\032*/api/gateway-profiles/{gateway_profile.id}:\001*'
  _GATEWAYPROFILESERVICE.methods_by_name['Delete']._options = None
  _GATEWAYPROFILESERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\034*\032/api/gateway-profiles/{id}'
  _GATEWAYPROFILESERVICE.methods_by_name['List']._options = None
  _GATEWAYPROFILESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\027\022\025/api/gateway-profiles'
  _GATEWAYPROFILE._serialized_start=224
  _GATEWAYPROFILE._serialized_end=436
  _GATEWAYPROFILELISTITEM._serialized_start=439
  _GATEWAYPROFILELISTITEM._serialized_end=658
  _GATEWAYPROFILEEXTRACHANNEL._serialized_start=661
  _GATEWAYPROFILEEXTRACHANNEL._serialized_end=811
  _CREATEGATEWAYPROFILEREQUEST._serialized_start=813
  _CREATEGATEWAYPROFILEREQUEST._serialized_end=888
  _CREATEGATEWAYPROFILERESPONSE._serialized_start=890
  _CREATEGATEWAYPROFILERESPONSE._serialized_end=932
  _GETGATEWAYPROFILEREQUEST._serialized_start=934
  _GETGATEWAYPROFILEREQUEST._serialized_end=972
  _GETGATEWAYPROFILERESPONSE._serialized_start=975
  _GETGATEWAYPROFILERESPONSE._serialized_end=1144
  _UPDATEGATEWAYPROFILEREQUEST._serialized_start=1146
  _UPDATEGATEWAYPROFILEREQUEST._serialized_end=1221
  _DELETEGATEWAYPROFILEREQUEST._serialized_start=1223
  _DELETEGATEWAYPROFILEREQUEST._serialized_end=1264
  _LISTGATEWAYPROFILESREQUEST._serialized_start=1266
  _LISTGATEWAYPROFILESREQUEST._serialized_end=1369
  _LISTGATEWAYPROFILESRESPONSE._serialized_start=1371
  _LISTGATEWAYPROFILESRESPONSE._serialized_end=1466
  _GATEWAYPROFILESERVICE._serialized_start=1469
  _GATEWAYPROFILESERVICE._serialized_end=2044
# @@protoc_insertion_point(module_scope)
