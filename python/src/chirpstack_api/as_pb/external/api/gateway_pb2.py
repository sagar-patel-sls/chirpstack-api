# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/gateway.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.as_pb.external.api import frameLog_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_frameLog__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/chirpstack-api/as_pb/external/api/gateway.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\"chirpstack-api/common/common.proto\x1a\x30\x63hirpstack-api/as_pb/external/api/frameLog.proto\"\x98\x04\n\x07Gateway\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\"\n\x08location\x18\x04 \x01(\x0b\x32\x10.common.Location\x12\'\n\x0forganization_id\x18\x05 \x01(\x03R\x0eorganizationID\x12\x19\n\x11\x64iscovery_enabled\x18\x06 \x01(\x08\x12*\n\x11network_server_id\x18\x07 \x01(\x03R\x0fnetworkServerID\x12,\n\x12gateway_profile_id\x18\x08 \x01(\tR\x10gatewayProfileID\x12!\n\x06\x62oards\x18\t \x03(\x0b\x32\x11.api.GatewayBoard\x12$\n\x04tags\x18\n \x03(\x0b\x32\x16.api.Gateway.TagsEntry\x12,\n\x08metadata\x18\x0b \x03(\x0b\x32\x1a.api.Gateway.MetadataEntry\x12,\n\x12service_profile_id\x18\x0c \x01(\tR\x10serviceProfileID\x12\x19\n\x11stat_notification\x18\r \x01(\x08\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"C\n\x0cGatewayBoard\x12\x17\n\x07\x66pga_id\x18\x01 \x01(\tR\x06\x66pgaID\x12\x1a\n\x12\x66ine_timestamp_key\x18\x02 \x01(\t\"5\n\x14\x43reateGatewayRequest\x12\x1d\n\x07gateway\x18\x01 \x01(\x0b\x32\x0c.api.Gateway\"\x1f\n\x11GetGatewayRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x8b\x02\n\x12GetGatewayResponse\x12\x1d\n\x07gateway\x18\x01 \x01(\x0b\x32\x0c.api.Gateway\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rfirst_seen_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_seen_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tconn_stat\x18\x06 \x01(\t\"\"\n\x14\x44\x65leteGatewayRequest\x12\n\n\x02id\x18\x01 \x01(\t\"=\n\'GenerateGatewayClientCertificateRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\t\"\x8e\x01\n(GenerateGatewayClientCertificateResponse\x12\x10\n\x08tls_cert\x18\x01 \x01(\t\x12\x0f\n\x07tls_key\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61_cert\x18\x03 \x01(\t\x12.\n\nexpires_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"l\n\x12ListGatewayRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\'\n\x0forganization_id\x18\x03 \x01(\x03R\x0eorganizationID\x12\x0e\n\x06search\x18\x04 \x01(\t\"\xae\x03\n\x0fGatewayListItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rfirst_seen_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_seen_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x0forganization_id\x18\x06 \x01(\x03R\x0eorganizationID\x12*\n\x11network_server_id\x18\x07 \x01(\x03R\x0fnetworkServerID\x12\"\n\x08location\x18\n \x01(\x0b\x32\x10.common.Location\x12\x1b\n\x13network_server_name\x18\x0b \x01(\t\x12\x11\n\tconn_stat\x18\x0c \x01(\t\"P\n\x13ListGatewayResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12$\n\x06result\x18\x02 \x03(\x0b\x32\x14.api.GatewayListItem\"5\n\x14UpdateGatewayRequest\x12\x1d\n\x07gateway\x18\x01 \x01(\x0b\x32\x0c.api.Gateway\"\xc6\x07\n\x0cGatewayStats\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13rx_packets_received\x18\x02 \x01(\x05\x12\x33\n\x16rx_packets_received_ok\x18\x03 \x01(\x05R\x13rxPacketsReceivedOK\x12\x1b\n\x13tx_packets_received\x18\x04 \x01(\x05\x12\x1a\n\x12tx_packets_emitted\x18\x05 \x01(\x05\x12N\n\x18tx_packets_per_frequency\x18\x06 \x03(\x0b\x32,.api.GatewayStats.TxPacketsPerFrequencyEntry\x12N\n\x18rx_packets_per_frequency\x18\x07 \x03(\x0b\x32,.api.GatewayStats.RxPacketsPerFrequencyEntry\x12@\n\x11tx_packets_per_dr\x18\x08 \x03(\x0b\x32%.api.GatewayStats.TxPacketsPerDrEntry\x12@\n\x11rx_packets_per_dr\x18\t \x03(\x0b\x32%.api.GatewayStats.RxPacketsPerDrEntry\x12H\n\x15tx_packets_per_status\x18\n \x03(\x0b\x32).api.GatewayStats.TxPacketsPerStatusEntry\x12\x36\n\x0bmtype_count\x18\x0b \x03(\x0b\x32!.api.GatewayStats.MtypeCountEntry\x1a<\n\x1aTxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a<\n\x1aRxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x35\n\x13TxPacketsPerDrEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x35\n\x13RxPacketsPerDrEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x39\n\x17TxPacketsPerStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x31\n\x0fMtypeCountEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\xb1\x01\n\x16GetGatewayStatsRequest\x12\x1d\n\ngateway_id\x18\x01 \x01(\tR\tgatewayID\x12\x10\n\x08interval\x18\x02 \x01(\t\x12\x33\n\x0fstart_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"<\n\x17GetGatewayStatsResponse\x12!\n\x06result\x18\x01 \x03(\x0b\x32\x11.api.GatewayStats\"\x87\x01\n\x06PingRX\x12\x1d\n\ngateway_id\x18\x01 \x01(\tR\tgatewayID\x12\x0c\n\x04rssi\x18\x02 \x01(\x05\x12\x19\n\x08lora_snr\x18\x03 \x01(\x01R\x07loRaSNR\x12\x10\n\x08latitude\x18\x04 \x01(\x01\x12\x11\n\tlongitude\x18\x05 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x06 \x01(\x01\"3\n\x12GetLastPingRequest\x12\x1d\n\ngateway_id\x18\x01 \x01(\tR\tgatewayID\"\x8a\x01\n\x13GetLastPingResponse\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tfrequency\x18\x02 \x01(\r\x12\n\n\x02\x64r\x18\x03 \x01(\r\x12$\n\x07ping_rx\x18\x04 \x03(\x0b\x32\x0b.api.PingRXR\x06pingRX\">\n\x1dStreamGatewayFrameLogsRequest\x12\x1d\n\ngateway_id\x18\x01 \x01(\tR\tgatewayID\"\x87\x01\n\x1eStreamGatewayFrameLogsResponse\x12+\n\x0cuplink_frame\x18\x01 \x01(\x0b\x32\x13.api.UplinkFrameLogH\x00\x12/\n\x0e\x64ownlink_frame\x18\x02 \x01(\x0b\x32\x15.api.DownlinkFrameLogH\x00\x42\x07\n\x05\x66rame\"l\n#StreamGlobalGatewayFrameLogsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\x03R\x0eorganizationID\x12\x1c\n\x06region\x18\x02 \x01(\x0e\x32\x0c.api.ISMBand\"\xae\x01\n$StreamGlobalGatewayFrameLogsResponse\x12\x1f\n\x0bgateway_eui\x18\x01 \x01(\tR\ngatewayEUI\x12+\n\x0cuplink_frame\x18\x02 \x01(\x0b\x32\x13.api.UplinkFrameLogH\x00\x12/\n\x0e\x64ownlink_frame\x18\x03 \x01(\x0b\x32\x15.api.DownlinkFrameLogH\x00\x42\x07\n\x05\x66rame*\xab\x01\n\x07ISMBand\x12\t\n\x05IN865\x10\x00\x12\t\n\x05\x45U868\x10\x01\x12\t\n\x05US915\x10\x02\x12\t\n\x05\x43N779\x10\x03\x12\t\n\x05\x45U433\x10\x04\x12\t\n\x05\x41U915\x10\x05\x12\t\n\x05\x43N470\x10\x06\x12\t\n\x05\x41S923\x10\x07\x12\x0b\n\x07\x41S923_2\x10\x08\x12\x0b\n\x07\x41S923_3\x10\t\x12\x0b\n\x07\x41S923_4\x10\n\x12\t\n\x05KR920\x10\x0b\x12\t\n\x05RU864\x10\x0c\x12\x0b\n\x07ISM2400\x10\r2\xa0\t\n\x0eGatewayService\x12U\n\x06\x43reate\x12\x19.api.CreateGatewayRequest\x1a\x16.google.protobuf.Empty\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/api/gateways:\x01*\x12R\n\x03Get\x12\x16.api.GetGatewayRequest\x1a\x17.api.GetGatewayResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/api/gateways/{id}\x12\x62\n\x06Update\x12\x19.api.UpdateGatewayRequest\x1a\x16.google.protobuf.Empty\"%\x82\xd3\xe4\x93\x02\x1f\x1a\x1a/api/gateways/{gateway.id}:\x01*\x12W\n\x06\x44\x65lete\x12\x19.api.DeleteGatewayRequest\x1a\x16.google.protobuf.Empty\"\x1a\x82\xd3\xe4\x93\x02\x14*\x12/api/gateways/{id}\x12P\n\x04List\x12\x17.api.ListGatewayRequest\x1a\x18.api.ListGatewayResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/api/gateways\x12o\n\x08GetStats\x12\x1b.api.GetGatewayStatsRequest\x1a\x1c.api.GetGatewayStatsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /api/gateways/{gateway_id}/stats\x12o\n\x0bGetLastPing\x12\x17.api.GetLastPingRequest\x1a\x18.api.GetLastPingResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/api/gateways/{gateway_id}/pings/last\x12\xb8\x01\n GenerateGatewayClientCertificate\x12,.api.GenerateGatewayClientCertificateRequest\x1a-.api.GenerateGatewayClientCertificateResponse\"7\x82\xd3\xe4\x93\x02\x31\"//api/gateways/{gateway_id}/generate-certificate\x12\x87\x01\n\x0fStreamFrameLogs\x12\".api.StreamGatewayFrameLogsRequest\x1a#.api.StreamGatewayFrameLogsResponse\")\x82\xd3\xe4\x93\x02#\x12!/api/gateways/{gateway_id}/frames0\x01\x12\xac\x01\n\x15StreamGlobalFrameLogs\x12(.api.StreamGlobalGatewayFrameLogsRequest\x1a).api.StreamGlobalGatewayFrameLogsResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/api/organizations/{organization_id}/gateways/frames0\x01\x42t\n!io.chirpstack.api.as.external.apiB\x0cGatewayProtoP\x01Z?github.com/sagar-patel-sls/chirpstack-api/go/v3/as/external/apib\x06proto3')

_ISMBAND = DESCRIPTOR.enum_types_by_name['ISMBand']
ISMBand = enum_type_wrapper.EnumTypeWrapper(_ISMBAND)
IN865 = 0
EU868 = 1
US915 = 2
CN779 = 3
EU433 = 4
AU915 = 5
CN470 = 6
AS923 = 7
AS923_2 = 8
AS923_3 = 9
AS923_4 = 10
KR920 = 11
RU864 = 12
ISM2400 = 13


_GATEWAY = DESCRIPTOR.message_types_by_name['Gateway']
_GATEWAY_TAGSENTRY = _GATEWAY.nested_types_by_name['TagsEntry']
_GATEWAY_METADATAENTRY = _GATEWAY.nested_types_by_name['MetadataEntry']
_GATEWAYBOARD = DESCRIPTOR.message_types_by_name['GatewayBoard']
_CREATEGATEWAYREQUEST = DESCRIPTOR.message_types_by_name['CreateGatewayRequest']
_GETGATEWAYREQUEST = DESCRIPTOR.message_types_by_name['GetGatewayRequest']
_GETGATEWAYRESPONSE = DESCRIPTOR.message_types_by_name['GetGatewayResponse']
_DELETEGATEWAYREQUEST = DESCRIPTOR.message_types_by_name['DeleteGatewayRequest']
_GENERATEGATEWAYCLIENTCERTIFICATEREQUEST = DESCRIPTOR.message_types_by_name['GenerateGatewayClientCertificateRequest']
_GENERATEGATEWAYCLIENTCERTIFICATERESPONSE = DESCRIPTOR.message_types_by_name['GenerateGatewayClientCertificateResponse']
_LISTGATEWAYREQUEST = DESCRIPTOR.message_types_by_name['ListGatewayRequest']
_GATEWAYLISTITEM = DESCRIPTOR.message_types_by_name['GatewayListItem']
_LISTGATEWAYRESPONSE = DESCRIPTOR.message_types_by_name['ListGatewayResponse']
_UPDATEGATEWAYREQUEST = DESCRIPTOR.message_types_by_name['UpdateGatewayRequest']
_GATEWAYSTATS = DESCRIPTOR.message_types_by_name['GatewayStats']
_GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY = _GATEWAYSTATS.nested_types_by_name['TxPacketsPerFrequencyEntry']
_GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY = _GATEWAYSTATS.nested_types_by_name['RxPacketsPerFrequencyEntry']
_GATEWAYSTATS_TXPACKETSPERDRENTRY = _GATEWAYSTATS.nested_types_by_name['TxPacketsPerDrEntry']
_GATEWAYSTATS_RXPACKETSPERDRENTRY = _GATEWAYSTATS.nested_types_by_name['RxPacketsPerDrEntry']
_GATEWAYSTATS_TXPACKETSPERSTATUSENTRY = _GATEWAYSTATS.nested_types_by_name['TxPacketsPerStatusEntry']
_GATEWAYSTATS_MTYPECOUNTENTRY = _GATEWAYSTATS.nested_types_by_name['MtypeCountEntry']
_GETGATEWAYSTATSREQUEST = DESCRIPTOR.message_types_by_name['GetGatewayStatsRequest']
_GETGATEWAYSTATSRESPONSE = DESCRIPTOR.message_types_by_name['GetGatewayStatsResponse']
_PINGRX = DESCRIPTOR.message_types_by_name['PingRX']
_GETLASTPINGREQUEST = DESCRIPTOR.message_types_by_name['GetLastPingRequest']
_GETLASTPINGRESPONSE = DESCRIPTOR.message_types_by_name['GetLastPingResponse']
_STREAMGATEWAYFRAMELOGSREQUEST = DESCRIPTOR.message_types_by_name['StreamGatewayFrameLogsRequest']
_STREAMGATEWAYFRAMELOGSRESPONSE = DESCRIPTOR.message_types_by_name['StreamGatewayFrameLogsResponse']
_STREAMGLOBALGATEWAYFRAMELOGSREQUEST = DESCRIPTOR.message_types_by_name['StreamGlobalGatewayFrameLogsRequest']
_STREAMGLOBALGATEWAYFRAMELOGSRESPONSE = DESCRIPTOR.message_types_by_name['StreamGlobalGatewayFrameLogsResponse']
Gateway = _reflection.GeneratedProtocolMessageType('Gateway', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAY_TAGSENTRY,
    '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
    # @@protoc_insertion_point(class_scope:api.Gateway.TagsEntry)
    })
  ,

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAY_METADATAENTRY,
    '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
    # @@protoc_insertion_point(class_scope:api.Gateway.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _GATEWAY,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.Gateway)
  })
_sym_db.RegisterMessage(Gateway)
_sym_db.RegisterMessage(Gateway.TagsEntry)
_sym_db.RegisterMessage(Gateway.MetadataEntry)

GatewayBoard = _reflection.GeneratedProtocolMessageType('GatewayBoard', (_message.Message,), {
  'DESCRIPTOR' : _GATEWAYBOARD,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.GatewayBoard)
  })
_sym_db.RegisterMessage(GatewayBoard)

CreateGatewayRequest = _reflection.GeneratedProtocolMessageType('CreateGatewayRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGATEWAYREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateGatewayRequest)
  })
_sym_db.RegisterMessage(CreateGatewayRequest)

GetGatewayRequest = _reflection.GeneratedProtocolMessageType('GetGatewayRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGATEWAYREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.GetGatewayRequest)
  })
_sym_db.RegisterMessage(GetGatewayRequest)

GetGatewayResponse = _reflection.GeneratedProtocolMessageType('GetGatewayResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETGATEWAYRESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.GetGatewayResponse)
  })
_sym_db.RegisterMessage(GetGatewayResponse)

DeleteGatewayRequest = _reflection.GeneratedProtocolMessageType('DeleteGatewayRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEGATEWAYREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.DeleteGatewayRequest)
  })
_sym_db.RegisterMessage(DeleteGatewayRequest)

GenerateGatewayClientCertificateRequest = _reflection.GeneratedProtocolMessageType('GenerateGatewayClientCertificateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEGATEWAYCLIENTCERTIFICATEREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.GenerateGatewayClientCertificateRequest)
  })
_sym_db.RegisterMessage(GenerateGatewayClientCertificateRequest)

GenerateGatewayClientCertificateResponse = _reflection.GeneratedProtocolMessageType('GenerateGatewayClientCertificateResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEGATEWAYCLIENTCERTIFICATERESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.GenerateGatewayClientCertificateResponse)
  })
_sym_db.RegisterMessage(GenerateGatewayClientCertificateResponse)

ListGatewayRequest = _reflection.GeneratedProtocolMessageType('ListGatewayRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTGATEWAYREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.ListGatewayRequest)
  })
_sym_db.RegisterMessage(ListGatewayRequest)

GatewayListItem = _reflection.GeneratedProtocolMessageType('GatewayListItem', (_message.Message,), {
  'DESCRIPTOR' : _GATEWAYLISTITEM,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.GatewayListItem)
  })
_sym_db.RegisterMessage(GatewayListItem)

ListGatewayResponse = _reflection.GeneratedProtocolMessageType('ListGatewayResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTGATEWAYRESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.ListGatewayResponse)
  })
_sym_db.RegisterMessage(ListGatewayResponse)

UpdateGatewayRequest = _reflection.GeneratedProtocolMessageType('UpdateGatewayRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEGATEWAYREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateGatewayRequest)
  })
_sym_db.RegisterMessage(UpdateGatewayRequest)

GatewayStats = _reflection.GeneratedProtocolMessageType('GatewayStats', (_message.Message,), {

  'TxPacketsPerFrequencyEntry' : _reflection.GeneratedProtocolMessageType('TxPacketsPerFrequencyEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY,
    '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
    # @@protoc_insertion_point(class_scope:api.GatewayStats.TxPacketsPerFrequencyEntry)
    })
  ,

  'RxPacketsPerFrequencyEntry' : _reflection.GeneratedProtocolMessageType('RxPacketsPerFrequencyEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY,
    '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
    # @@protoc_insertion_point(class_scope:api.GatewayStats.RxPacketsPerFrequencyEntry)
    })
  ,

  'TxPacketsPerDrEntry' : _reflection.GeneratedProtocolMessageType('TxPacketsPerDrEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYSTATS_TXPACKETSPERDRENTRY,
    '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
    # @@protoc_insertion_point(class_scope:api.GatewayStats.TxPacketsPerDrEntry)
    })
  ,

  'RxPacketsPerDrEntry' : _reflection.GeneratedProtocolMessageType('RxPacketsPerDrEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYSTATS_RXPACKETSPERDRENTRY,
    '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
    # @@protoc_insertion_point(class_scope:api.GatewayStats.RxPacketsPerDrEntry)
    })
  ,

  'TxPacketsPerStatusEntry' : _reflection.GeneratedProtocolMessageType('TxPacketsPerStatusEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY,
    '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
    # @@protoc_insertion_point(class_scope:api.GatewayStats.TxPacketsPerStatusEntry)
    })
  ,

  'MtypeCountEntry' : _reflection.GeneratedProtocolMessageType('MtypeCountEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYSTATS_MTYPECOUNTENTRY,
    '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
    # @@protoc_insertion_point(class_scope:api.GatewayStats.MtypeCountEntry)
    })
  ,
  'DESCRIPTOR' : _GATEWAYSTATS,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.GatewayStats)
  })
_sym_db.RegisterMessage(GatewayStats)
_sym_db.RegisterMessage(GatewayStats.TxPacketsPerFrequencyEntry)
_sym_db.RegisterMessage(GatewayStats.RxPacketsPerFrequencyEntry)
_sym_db.RegisterMessage(GatewayStats.TxPacketsPerDrEntry)
_sym_db.RegisterMessage(GatewayStats.RxPacketsPerDrEntry)
_sym_db.RegisterMessage(GatewayStats.TxPacketsPerStatusEntry)
_sym_db.RegisterMessage(GatewayStats.MtypeCountEntry)

GetGatewayStatsRequest = _reflection.GeneratedProtocolMessageType('GetGatewayStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGATEWAYSTATSREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.GetGatewayStatsRequest)
  })
_sym_db.RegisterMessage(GetGatewayStatsRequest)

GetGatewayStatsResponse = _reflection.GeneratedProtocolMessageType('GetGatewayStatsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETGATEWAYSTATSRESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.GetGatewayStatsResponse)
  })
_sym_db.RegisterMessage(GetGatewayStatsResponse)

PingRX = _reflection.GeneratedProtocolMessageType('PingRX', (_message.Message,), {
  'DESCRIPTOR' : _PINGRX,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.PingRX)
  })
_sym_db.RegisterMessage(PingRX)

GetLastPingRequest = _reflection.GeneratedProtocolMessageType('GetLastPingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTPINGREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.GetLastPingRequest)
  })
_sym_db.RegisterMessage(GetLastPingRequest)

GetLastPingResponse = _reflection.GeneratedProtocolMessageType('GetLastPingResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTPINGRESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.GetLastPingResponse)
  })
_sym_db.RegisterMessage(GetLastPingResponse)

StreamGatewayFrameLogsRequest = _reflection.GeneratedProtocolMessageType('StreamGatewayFrameLogsRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMGATEWAYFRAMELOGSREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.StreamGatewayFrameLogsRequest)
  })
_sym_db.RegisterMessage(StreamGatewayFrameLogsRequest)

StreamGatewayFrameLogsResponse = _reflection.GeneratedProtocolMessageType('StreamGatewayFrameLogsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMGATEWAYFRAMELOGSRESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.StreamGatewayFrameLogsResponse)
  })
_sym_db.RegisterMessage(StreamGatewayFrameLogsResponse)

StreamGlobalGatewayFrameLogsRequest = _reflection.GeneratedProtocolMessageType('StreamGlobalGatewayFrameLogsRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMGLOBALGATEWAYFRAMELOGSREQUEST,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.StreamGlobalGatewayFrameLogsRequest)
  })
_sym_db.RegisterMessage(StreamGlobalGatewayFrameLogsRequest)

StreamGlobalGatewayFrameLogsResponse = _reflection.GeneratedProtocolMessageType('StreamGlobalGatewayFrameLogsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMGLOBALGATEWAYFRAMELOGSRESPONSE,
  '__module__' : 'chirpstack_api.as_pb.external.api.gateway_pb2'
  # @@protoc_insertion_point(class_scope:api.StreamGlobalGatewayFrameLogsResponse)
  })
_sym_db.RegisterMessage(StreamGlobalGatewayFrameLogsResponse)

_GATEWAYSERVICE = DESCRIPTOR.services_by_name['GatewayService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.chirpstack.api.as.external.apiB\014GatewayProtoP\001Z?github.com/sagar-patel-sls/chirpstack-api/go/v3/as/external/api'
  _GATEWAY_TAGSENTRY._options = None
  _GATEWAY_TAGSENTRY._serialized_options = b'8\001'
  _GATEWAY_METADATAENTRY._options = None
  _GATEWAY_METADATAENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._options = None
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERDRENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERDRENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_RXPACKETSPERDRENTRY._options = None
  _GATEWAYSTATS_RXPACKETSPERDRENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_MTYPECOUNTENTRY._options = None
  _GATEWAYSTATS_MTYPECOUNTENTRY._serialized_options = b'8\001'
  _GATEWAYSERVICE.methods_by_name['Create']._options = None
  _GATEWAYSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\022\"\r/api/gateways:\001*'
  _GATEWAYSERVICE.methods_by_name['Get']._options = None
  _GATEWAYSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\024\022\022/api/gateways/{id}'
  _GATEWAYSERVICE.methods_by_name['Update']._options = None
  _GATEWAYSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\037\032\032/api/gateways/{gateway.id}:\001*'
  _GATEWAYSERVICE.methods_by_name['Delete']._options = None
  _GATEWAYSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\024*\022/api/gateways/{id}'
  _GATEWAYSERVICE.methods_by_name['List']._options = None
  _GATEWAYSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\017\022\r/api/gateways'
  _GATEWAYSERVICE.methods_by_name['GetStats']._options = None
  _GATEWAYSERVICE.methods_by_name['GetStats']._serialized_options = b'\202\323\344\223\002\"\022 /api/gateways/{gateway_id}/stats'
  _GATEWAYSERVICE.methods_by_name['GetLastPing']._options = None
  _GATEWAYSERVICE.methods_by_name['GetLastPing']._serialized_options = b'\202\323\344\223\002\'\022%/api/gateways/{gateway_id}/pings/last'
  _GATEWAYSERVICE.methods_by_name['GenerateGatewayClientCertificate']._options = None
  _GATEWAYSERVICE.methods_by_name['GenerateGatewayClientCertificate']._serialized_options = b'\202\323\344\223\0021\"//api/gateways/{gateway_id}/generate-certificate'
  _GATEWAYSERVICE.methods_by_name['StreamFrameLogs']._options = None
  _GATEWAYSERVICE.methods_by_name['StreamFrameLogs']._serialized_options = b'\202\323\344\223\002#\022!/api/gateways/{gateway_id}/frames'
  _GATEWAYSERVICE.methods_by_name['StreamGlobalFrameLogs']._options = None
  _GATEWAYSERVICE.methods_by_name['StreamGlobalFrameLogs']._serialized_options = b'\202\323\344\223\0026\0224/api/organizations/{organization_id}/gateways/frames'
  _ISMBAND._serialized_start=4157
  _ISMBAND._serialized_end=4328
  _GATEWAY._serialized_start=235
  _GATEWAY._serialized_end=771
  _GATEWAY_TAGSENTRY._serialized_start=679
  _GATEWAY_TAGSENTRY._serialized_end=722
  _GATEWAY_METADATAENTRY._serialized_start=724
  _GATEWAY_METADATAENTRY._serialized_end=771
  _GATEWAYBOARD._serialized_start=773
  _GATEWAYBOARD._serialized_end=840
  _CREATEGATEWAYREQUEST._serialized_start=842
  _CREATEGATEWAYREQUEST._serialized_end=895
  _GETGATEWAYREQUEST._serialized_start=897
  _GETGATEWAYREQUEST._serialized_end=928
  _GETGATEWAYRESPONSE._serialized_start=931
  _GETGATEWAYRESPONSE._serialized_end=1198
  _DELETEGATEWAYREQUEST._serialized_start=1200
  _DELETEGATEWAYREQUEST._serialized_end=1234
  _GENERATEGATEWAYCLIENTCERTIFICATEREQUEST._serialized_start=1236
  _GENERATEGATEWAYCLIENTCERTIFICATEREQUEST._serialized_end=1297
  _GENERATEGATEWAYCLIENTCERTIFICATERESPONSE._serialized_start=1300
  _GENERATEGATEWAYCLIENTCERTIFICATERESPONSE._serialized_end=1442
  _LISTGATEWAYREQUEST._serialized_start=1444
  _LISTGATEWAYREQUEST._serialized_end=1552
  _GATEWAYLISTITEM._serialized_start=1555
  _GATEWAYLISTITEM._serialized_end=1985
  _LISTGATEWAYRESPONSE._serialized_start=1987
  _LISTGATEWAYRESPONSE._serialized_end=2067
  _UPDATEGATEWAYREQUEST._serialized_start=2069
  _UPDATEGATEWAYREQUEST._serialized_end=2122
  _GATEWAYSTATS._serialized_start=2125
  _GATEWAYSTATS._serialized_end=3091
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_start=2749
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_end=2809
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_start=2811
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_end=2871
  _GATEWAYSTATS_TXPACKETSPERDRENTRY._serialized_start=2873
  _GATEWAYSTATS_TXPACKETSPERDRENTRY._serialized_end=2926
  _GATEWAYSTATS_RXPACKETSPERDRENTRY._serialized_start=2928
  _GATEWAYSTATS_RXPACKETSPERDRENTRY._serialized_end=2981
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_start=2983
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_end=3040
  _GATEWAYSTATS_MTYPECOUNTENTRY._serialized_start=3042
  _GATEWAYSTATS_MTYPECOUNTENTRY._serialized_end=3091
  _GETGATEWAYSTATSREQUEST._serialized_start=3094
  _GETGATEWAYSTATSREQUEST._serialized_end=3271
  _GETGATEWAYSTATSRESPONSE._serialized_start=3273
  _GETGATEWAYSTATSRESPONSE._serialized_end=3333
  _PINGRX._serialized_start=3336
  _PINGRX._serialized_end=3471
  _GETLASTPINGREQUEST._serialized_start=3473
  _GETLASTPINGREQUEST._serialized_end=3524
  _GETLASTPINGRESPONSE._serialized_start=3527
  _GETLASTPINGRESPONSE._serialized_end=3665
  _STREAMGATEWAYFRAMELOGSREQUEST._serialized_start=3667
  _STREAMGATEWAYFRAMELOGSREQUEST._serialized_end=3729
  _STREAMGATEWAYFRAMELOGSRESPONSE._serialized_start=3732
  _STREAMGATEWAYFRAMELOGSRESPONSE._serialized_end=3867
  _STREAMGLOBALGATEWAYFRAMELOGSREQUEST._serialized_start=3869
  _STREAMGLOBALGATEWAYFRAMELOGSREQUEST._serialized_end=3977
  _STREAMGLOBALGATEWAYFRAMELOGSRESPONSE._serialized_start=3980
  _STREAMGLOBALGATEWAYFRAMELOGSRESPONSE._serialized_end=4154
  _GATEWAYSERVICE._serialized_start=4331
  _GATEWAYSERVICE._serialized_end=5515
# @@protoc_insertion_point(module_scope)
