# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/ns/ns.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.gw import gw_pb2 as chirpstack__api_dot_gw_dot_gw__pb2
from chirpstack_api.ns import profiles_pb2 as chirpstack__api_dot_ns_dot_profiles__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63hirpstack-api/ns/ns.proto\x12\x02ns\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\"chirpstack-api/common/common.proto\x1a\x1a\x63hirpstack-api/gw/gw.proto\x1a chirpstack-api/ns/profiles.proto\"J\n\x1b\x43reateServiceProfileRequest\x12+\n\x0fservice_profile\x18\x01 \x01(\x0b\x32\x12.ns.ServiceProfile\"*\n\x1c\x43reateServiceProfileResponse\x12\n\n\x02id\x18\x01 \x01(\x0c\"&\n\x18GetServiceProfileRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"\xa8\x01\n\x19GetServiceProfileResponse\x12+\n\x0fservice_profile\x18\x01 \x01(\x0b\x32\x12.ns.ServiceProfile\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"J\n\x1bUpdateServiceProfileRequest\x12+\n\x0fservice_profile\x18\x01 \x01(\x0b\x32\x12.ns.ServiceProfile\")\n\x1b\x44\x65leteServiceProfileRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"J\n\x1b\x43reateRoutingProfileRequest\x12+\n\x0frouting_profile\x18\x01 \x01(\x0b\x32\x12.ns.RoutingProfile\"*\n\x1c\x43reateRoutingProfileResponse\x12\n\n\x02id\x18\x01 \x01(\x0c\"&\n\x18GetRoutingProfileRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"\xa8\x01\n\x19GetRoutingProfileResponse\x12+\n\x0frouting_profile\x18\x01 \x01(\x0b\x32\x12.ns.RoutingProfile\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"J\n\x1bUpdateRoutingProfileRequest\x12+\n\x0frouting_profile\x18\x01 \x01(\x0b\x32\x12.ns.RoutingProfile\")\n\x1b\x44\x65leteRoutingProfileRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"G\n\x1a\x43reateDeviceProfileRequest\x12)\n\x0e\x64\x65vice_profile\x18\x01 \x01(\x0b\x32\x11.ns.DeviceProfile\")\n\x1b\x43reateDeviceProfileResponse\x12\n\n\x02id\x18\x01 \x01(\x0c\"%\n\x17GetDeviceProfileRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"\xa5\x01\n\x18GetDeviceProfileResponse\x12)\n\x0e\x64\x65vice_profile\x18\x01 \x01(\x0b\x32\x11.ns.DeviceProfile\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"G\n\x1aUpdateDeviceProfileRequest\x12)\n\x0e\x64\x65vice_profile\x18\x01 \x01(\x0b\x32\x11.ns.DeviceProfile\"(\n\x1a\x44\x65leteDeviceProfileRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"\xb7\x01\n\x06\x44\x65vice\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x19\n\x11\x64\x65vice_profile_id\x18\x02 \x01(\x0c\x12\x1a\n\x12service_profile_id\x18\x03 \x01(\x0c\x12\x1a\n\x12routing_profile_id\x18\x04 \x01(\x0c\x12\x18\n\x10skip_f_cnt_check\x18\x05 \x01(\x08\x12\x1a\n\x12reference_altitude\x18\x06 \x01(\x01\x12\x13\n\x0bis_disabled\x18\x07 \x01(\x08\"1\n\x13\x43reateDeviceRequest\x12\x1a\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\n.ns.Device\"#\n\x10GetDeviceRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\"\xa3\x01\n\x11GetDeviceResponse\x12\x1a\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\n.ns.Device\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nDeviceMode\x18\x04 \x01(\t\"1\n\x13UpdateDeviceRequest\x12\x1a\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\n.ns.Device\"&\n\x13\x44\x65leteDeviceRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\"\xd6\x01\n\x10\x44\x65viceActivation\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x10\n\x08\x64\x65v_addr\x18\x02 \x01(\x0c\x12\x17\n\x0fs_nwk_s_int_key\x18\x03 \x01(\x0c\x12\x17\n\x0f\x66_nwk_s_int_key\x18\x04 \x01(\x0c\x12\x15\n\rnwk_s_enc_key\x18\x05 \x01(\x0c\x12\x10\n\x08\x66_cnt_up\x18\x06 \x01(\r\x12\x14\n\x0cn_f_cnt_down\x18\x07 \x01(\r\x12\x14\n\x0c\x61_f_cnt_down\x18\x08 \x01(\r\x12\x18\n\x10skip_f_cnt_check\x18\t \x01(\x08\"\xe9\x01\n\x15\x45xtraSessionParameter\x12\x0f\n\x07RXDelay\x18\x01 \x01(\r\x12\x13\n\x0bRX1DROffset\x18\x02 \x01(\r\x12\r\n\x05RX2DR\x18\x03 \x01(\r\x12\x14\n\x0cRX2Frequency\x18\x04 \x01(\r\x12\x14\n\x0cTXPowerIndex\x18\x05 \x01(\x05\x12\x30\n\x15\x65xtra_uplink_channels\x18\x06 \x03(\x0b\x32\x11.ns.ExtraChannels\x12=\n\x19last_dev_status_requested\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"O\n\rExtraChannels\x12\r\n\x05index\x18\x01 \x01(\r\x12\x11\n\tfrequency\x18\x02 \x01(\r\x12\r\n\x05minDR\x18\x03 \x01(\r\x12\r\n\x05maxDR\x18\x04 \x01(\r\"H\n\x15\x41\x63tivateDeviceRequest\x12/\n\x11\x64\x65vice_activation\x18\x01 \x01(\x0b\x32\x14.ns.DeviceActivation\"*\n\x17\x44\x65\x61\x63tivateDeviceRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\"-\n\x1aGetDeviceActivationRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\"\x8a\x01\n\x1bGetDeviceActivationResponse\x12/\n\x11\x64\x65vice_activation\x18\x01 \x01(\x0b\x32\x14.ns.DeviceActivation\x12:\n\x17\x65xtra_session_parameter\x18\x02 \x01(\x0b\x32\x19.ns.ExtraSessionParameter\",\n\x18GetRandomDevAddrResponse\x12\x10\n\x08\x64\x65v_addr\x18\x01 \x01(\x0c\"R\n CreateMACCommandQueueItemRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x0b\n\x03\x63id\x18\x04 \x01(\r\x12\x10\n\x08\x63ommands\x18\x05 \x03(\x0c\"\x96\x01\n\x1dSendProprietaryPayloadRequest\x12\x13\n\x0bmac_payload\x18\x01 \x01(\x0c\x12\x0b\n\x03mic\x18\x02 \x01(\x0c\x12\x14\n\x0cgateway_macs\x18\x03 \x03(\x0c\x12\x1e\n\x16polarization_inversion\x18\x04 \x01(\x08\x12\x11\n\tfrequency\x18\x05 \x01(\r\x12\n\n\x02\x64r\x18\x06 \x01(\r\"\xaf\x01\n\x07Gateway\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\"\n\x08location\x18\x02 \x01(\x0b\x32\x10.common.Location\x12\x1a\n\x12gateway_profile_id\x18\x03 \x01(\x0c\x12 \n\x06\x62oards\x18\x04 \x03(\x0b\x32\x10.ns.GatewayBoard\x12\x1a\n\x12routing_profile_id\x18\x05 \x01(\x0c\x12\x1a\n\x12service_profile_id\x18\x06 \x01(\x0c\";\n\x0cGatewayBoard\x12\x0f\n\x07\x66pga_id\x18\x01 \x01(\x0c\x12\x1a\n\x12\x66ine_timestamp_key\x18\x02 \x01(\x0c\"4\n\x14\x43reateGatewayRequest\x12\x1c\n\x07gateway\x18\x01 \x01(\x0b\x32\x0b.ns.Gateway\"\x1f\n\x11GetGatewayRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"\xf7\x01\n\x12GetGatewayResponse\x12\x1c\n\x07gateway\x18\x01 \x01(\x0b\x32\x0b.ns.Gateway\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rfirst_seen_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_seen_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"4\n\x14UpdateGatewayRequest\x12\x1c\n\x07gateway\x18\x01 \x01(\x0b\x32\x0b.ns.Gateway\"\"\n\x14\x44\x65leteGatewayRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"5\n\'GenerateGatewayClientCertificateRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"\x8e\x01\n(GenerateGatewayClientCertificateResponse\x12\x10\n\x08tls_cert\x18\x01 \x01(\x0c\x12\x0f\n\x07tls_key\x18\x02 \x01(\x0c\x12\x0f\n\x07\x63\x61_cert\x18\x03 \x01(\x0c\x12.\n\nexpires_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xb3\x01\n\x0cGatewayStats\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13rx_packets_received\x18\x02 \x01(\x05\x12\x1e\n\x16rx_packets_received_ok\x18\x03 \x01(\x05\x12\x1b\n\x13tx_packets_received\x18\x04 \x01(\x05\x12\x1a\n\x12tx_packets_emitted\x18\x05 \x01(\x05\"\xbf\x01\n\x16GetGatewayStatsRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12)\n\x08interval\x18\x02 \x01(\x0e\x32\x17.ns.AggregationInterval\x12\x33\n\x0fstart_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\";\n\x17GetGatewayStatsResponse\x12 \n\x06result\x18\x01 \x03(\x0b\x32\x10.ns.GatewayStats\"{\n\x0f\x44\x65viceQueueItem\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x13\n\x0b\x66rm_payload\x18\x02 \x01(\x0c\x12\r\n\x05\x66_cnt\x18\x03 \x01(\r\x12\x0e\n\x06\x66_port\x18\x04 \x01(\r\x12\x11\n\tconfirmed\x18\x05 \x01(\x08\x12\x10\n\x08\x64\x65v_addr\x18\x06 \x01(\x0c\"A\n\x1c\x43reateDeviceQueueItemRequest\x12!\n\x04item\x18\x01 \x01(\x0b\x32\x13.ns.DeviceQueueItem\"3\n FlushDeviceQueueForDevEUIRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\"J\n#GetDeviceQueueItemsForDevEUIRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x12\n\ncount_only\x18\x02 \x01(\x08\"_\n$GetDeviceQueueItemsForDevEUIResponse\x12\"\n\x05items\x18\x01 \x03(\x0b\x32\x13.ns.DeviceQueueItem\x12\x13\n\x0btotal_count\x18\x02 \x01(\r\"6\n#GetNextDownlinkFCntForDevEUIRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\"5\n$GetNextDownlinkFCntForDevEUIResponse\x12\r\n\x05\x66_cnt\x18\x01 \x01(\r\"\xdf\x01\n\x0eUplinkFrameLog\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12!\n\x07tx_info\x18\x02 \x01(\x0b\x32\x10.gw.UplinkTXInfo\x12!\n\x07rx_info\x18\x03 \x03(\x0b\x32\x10.gw.UplinkRXInfo\x12\x1d\n\x06m_type\x18\x04 \x01(\x0e\x32\r.common.MType\x12\x10\n\x08\x64\x65v_addr\x18\x05 \x01(\x0c\x12\x0f\n\x07\x64\x65v_eui\x18\x06 \x01(\x0c\x12\x30\n\x0cpublished_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x8f\x02\n\x10\x44ownlinkFrameLog\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12#\n\x07tx_info\x18\x02 \x01(\x0b\x32\x12.gw.DownlinkTXInfo\x12\r\n\x05token\x18\x03 \x01(\r\x12\x1f\n\x0b\x64ownlink_id\x18\x04 \x01(\x0cR\ndownlinkID\x12\x1d\n\ngateway_id\x18\x05 \x01(\x0cR\tgatewayID\x12\x1d\n\x06m_type\x18\x06 \x01(\x0e\x32\r.common.MType\x12\x10\n\x08\x64\x65v_addr\x18\x07 \x01(\x0c\x12\x0f\n\x07\x64\x65v_eui\x18\x08 \x01(\x0c\x12\x30\n\x0cpublished_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xfd\x03\n\x14GatewayStatsFrameLog\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12\n\n\x02ip\x18\t \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x08location\x18\x03 \x01(\x0b\x32\x10.common.Location\x12\x16\n\x0e\x63onfig_version\x18\x04 \x01(\t\x12\x1b\n\x13rx_packets_received\x18\x05 \x01(\r\x12\x33\n\x16rx_packets_received_ok\x18\x06 \x01(\rR\x13rxPacketsReceivedOK\x12\x1b\n\x13tx_packets_received\x18\x07 \x01(\r\x12\x1a\n\x12tx_packets_emitted\x18\x08 \x01(\r\x12\x39\n\tmeta_data\x18\n \x03(\x0b\x32&.ns.GatewayStatsFrameLog.MetaDataEntry\x12\x19\n\x08stats_id\x18\x0b \x01(\x0cR\x07statsID\x12\x30\n\x0cpublished_at\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x61\x63k_rate\x18\r \x01(\x02\x1a/\n\rMetaDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"6\n StreamFrameLogsForGatewayRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\"\xbd\x01\n!StreamFrameLogsForGatewayResponse\x12.\n\x10uplink_frame_set\x18\x01 \x01(\x0b\x32\x12.ns.UplinkFrameLogH\x00\x12.\n\x0e\x64ownlink_frame\x18\x02 \x01(\x0b\x32\x14.ns.DownlinkFrameLogH\x00\x12/\n\x0bstats_frame\x18\x03 \x01(\x0b\x32\x18.ns.GatewayStatsFrameLogH\x00\x42\x07\n\x05\x66rame\"\xd8\x01\n\'StreamGlobalFrameLogsForGatewayResponse\x12.\n\x10uplink_frame_set\x18\x01 \x01(\x0b\x32\x12.ns.UplinkFrameLogH\x00\x12.\n\x0e\x64ownlink_frame\x18\x02 \x01(\x0b\x32\x14.ns.DownlinkFrameLogH\x00\x12/\n\x0bstats_frame\x18\x03 \x01(\x0b\x32\x18.ns.GatewayStatsFrameLogH\x00\x12\x13\n\x0bgateway_eui\x18\x04 \x01(\x0c\x42\x07\n\x05\x66rame\"2\n\x1fStreamFrameLogsForDeviceRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\"\x8b\x01\n StreamFrameLogsForDeviceResponse\x12.\n\x10uplink_frame_set\x18\x01 \x01(\x0b\x32\x12.ns.UplinkFrameLogH\x00\x12.\n\x0e\x64ownlink_frame\x18\x02 \x01(\x0b\x32\x14.ns.DownlinkFrameLogH\x00\x42\x07\n\x05\x66rame\"\xa2\x01\n&StreamGlobalFrameLogsForDeviceResponse\x12.\n\x10uplink_frame_set\x18\x01 \x01(\x0b\x32\x12.ns.UplinkFrameLogH\x00\x12.\n\x0e\x64ownlink_frame\x18\x02 \x01(\x0b\x32\x14.ns.DownlinkFrameLogH\x00\x12\x0f\n\x07\x64\x65v_eui\x18\x03 \x01(\x0c\x42\x07\n\x05\x66rame\"E\n\x12GetVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1e\n\x06region\x18\x02 \x01(\x0e\x32\x0e.common.Region\"\x99\x01\n\x0eGatewayProfile\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x10\n\x08\x63hannels\x18\x02 \x03(\r\x12\x36\n\x0e\x65xtra_channels\x18\x03 \x03(\x0b\x32\x1e.ns.GatewayProfileExtraChannel\x12\x31\n\x0estats_interval\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x96\x01\n\x1aGatewayProfileExtraChannel\x12&\n\nmodulation\x18\x01 \x01(\x0e\x32\x12.common.Modulation\x12\x11\n\tfrequency\x18\x02 \x01(\r\x12\x11\n\tbandwidth\x18\x03 \x01(\r\x12\x0f\n\x07\x62itrate\x18\x04 \x01(\r\x12\x19\n\x11spreading_factors\x18\x05 \x03(\r\"J\n\x1b\x43reateGatewayProfileRequest\x12+\n\x0fgateway_profile\x18\x01 \x01(\x0b\x32\x12.ns.GatewayProfile\"*\n\x1c\x43reateGatewayProfileResponse\x12\n\n\x02id\x18\x01 \x01(\x0c\"&\n\x18GetGatewayProfileRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"\xa8\x01\n\x19GetGatewayProfileResponse\x12+\n\x0fgateway_profile\x18\x01 \x01(\x0b\x32\x12.ns.GatewayProfile\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"J\n\x1bUpdateGatewayProfileRequest\x12+\n\x0fgateway_profile\x18\x01 \x01(\x0b\x32\x12.ns.GatewayProfile\")\n\x1b\x44\x65leteGatewayProfileRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"\xef\x01\n\x0eMulticastGroup\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0f\n\x07mc_addr\x18\x02 \x01(\x0c\x12\x14\n\x0cmc_nwk_s_key\x18\x03 \x01(\x0c\x12\r\n\x05\x66_cnt\x18\x04 \x01(\r\x12*\n\ngroup_type\x18\x05 \x01(\x0e\x32\x16.ns.MulticastGroupType\x12\n\n\x02\x64r\x18\x06 \x01(\r\x12\x11\n\tfrequency\x18\x07 \x01(\r\x12\x18\n\x10ping_slot_period\x18\x08 \x01(\r\x12\x1a\n\x12service_profile_id\x18\t \x01(\x0c\x12\x1a\n\x12routing_profile_id\x18\n \x01(\x0c\"J\n\x1b\x43reateMulticastGroupRequest\x12+\n\x0fmulticast_group\x18\x01 \x01(\x0b\x32\x12.ns.MulticastGroup\"*\n\x1c\x43reateMulticastGroupResponse\x12\n\n\x02id\x18\x01 \x01(\x0c\"&\n\x18GetMulticastGroupRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"\xa8\x01\n\x19GetMulticastGroupResponse\x12+\n\x0fmulticast_group\x18\x01 \x01(\x0b\x32\x12.ns.MulticastGroup\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"J\n\x1bUpdateMulticastGroupRequest\x12+\n\x0fmulticast_group\x18\x01 \x01(\x0b\x32\x12.ns.MulticastGroup\")\n\x1b\x44\x65leteMulticastGroupRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"O\n AddDeviceToMulticastGroupRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x1a\n\x12multicast_group_id\x18\x02 \x01(\x0c\"T\n%RemoveDeviceFromMulticastGroupRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x1a\n\x12multicast_group_id\x18\x02 \x01(\x0c\"d\n\x12MulticastQueueItem\x12\x1a\n\x12multicast_group_id\x18\x01 \x01(\x0c\x12\r\n\x05\x66_cnt\x18\x02 \x01(\r\x12\x0e\n\x06\x66_port\x18\x03 \x01(\r\x12\x13\n\x0b\x66rm_payload\x18\x04 \x01(\x0c\"X\n EnqueueMulticastQueueItemRequest\x12\x34\n\x14multicast_queue_item\x18\x01 \x01(\x0b\x32\x16.ns.MulticastQueueItem\"I\n+FlushMulticastQueueForMulticastGroupRequest\x12\x1a\n\x12multicast_group_id\x18\x01 \x01(\x0c\"L\n.GetMulticastQueueItemsForMulticastGroupRequest\x12\x1a\n\x12multicast_group_id\x18\x01 \x01(\x0c\"h\n/GetMulticastQueueItemsForMulticastGroupResponse\x12\x35\n\x15multicast_queue_items\x18\x01 \x03(\x0b\x32\x16.ns.MulticastQueueItem\"D\n\x18GetADRAlgorithmsResponse\x12(\n\x0e\x61\x64r_algorithms\x18\x01 \x03(\x0b\x32\x10.ns.ADRAlgorithm\"(\n\x0c\x41\x44RAlgorithm\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"-\n\x1a\x43learDeviceDevNonceRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c*\x1c\n\x08RXWindow\x12\x07\n\x03RX1\x10\x00\x12\x07\n\x03RX2\x10\x01*l\n\x13\x41ggregationInterval\x12\n\n\x06SECOND\x10\x00\x12\n\n\x06MINUTE\x10\x01\x12\x08\n\x04HOUR\x10\x02\x12\x07\n\x03\x44\x41Y\x10\x03\x12\x08\n\x04WEEK\x10\x04\x12\t\n\x05MONTH\x10\x05\x12\x0b\n\x07QUARTER\x10\x06\x12\x08\n\x04YEAR\x10\x07*.\n\x12MulticastGroupType\x12\x0b\n\x07\x43LASS_C\x10\x00\x12\x0b\n\x07\x43LASS_B\x10\x01\x32\xe0#\n\x14NetworkServerService\x12[\n\x14\x43reateServiceProfile\x12\x1f.ns.CreateServiceProfileRequest\x1a .ns.CreateServiceProfileResponse\"\x00\x12R\n\x11GetServiceProfile\x12\x1c.ns.GetServiceProfileRequest\x1a\x1d.ns.GetServiceProfileResponse\"\x00\x12Q\n\x14UpdateServiceProfile\x12\x1f.ns.UpdateServiceProfileRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Q\n\x14\x44\x65leteServiceProfile\x12\x1f.ns.DeleteServiceProfileRequest\x1a\x16.google.protobuf.Empty\"\x00\x12[\n\x14\x43reateRoutingProfile\x12\x1f.ns.CreateRoutingProfileRequest\x1a .ns.CreateRoutingProfileResponse\"\x00\x12R\n\x11GetRoutingProfile\x12\x1c.ns.GetRoutingProfileRequest\x1a\x1d.ns.GetRoutingProfileResponse\"\x00\x12Q\n\x14UpdateRoutingProfile\x12\x1f.ns.UpdateRoutingProfileRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Q\n\x14\x44\x65leteRoutingProfile\x12\x1f.ns.DeleteRoutingProfileRequest\x1a\x16.google.protobuf.Empty\"\x00\x12X\n\x13\x43reateDeviceProfile\x12\x1e.ns.CreateDeviceProfileRequest\x1a\x1f.ns.CreateDeviceProfileResponse\"\x00\x12O\n\x10GetDeviceProfile\x12\x1b.ns.GetDeviceProfileRequest\x1a\x1c.ns.GetDeviceProfileResponse\"\x00\x12O\n\x13UpdateDeviceProfile\x12\x1e.ns.UpdateDeviceProfileRequest\x1a\x16.google.protobuf.Empty\"\x00\x12O\n\x13\x44\x65leteDeviceProfile\x12\x1e.ns.DeleteDeviceProfileRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x41\n\x0c\x43reateDevice\x12\x17.ns.CreateDeviceRequest\x1a\x16.google.protobuf.Empty\"\x00\x12:\n\tGetDevice\x12\x14.ns.GetDeviceRequest\x1a\x15.ns.GetDeviceResponse\"\x00\x12\x41\n\x0cUpdateDevice\x12\x17.ns.UpdateDeviceRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x41\n\x0c\x44\x65leteDevice\x12\x17.ns.DeleteDeviceRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x45\n\x0e\x41\x63tivateDevice\x12\x19.ns.ActivateDeviceRequest\x1a\x16.google.protobuf.Empty\"\x00\x12I\n\x10\x44\x65\x61\x63tivateDevice\x12\x1b.ns.DeactivateDeviceRequest\x1a\x16.google.protobuf.Empty\"\x00\x12X\n\x13GetDeviceActivation\x12\x1e.ns.GetDeviceActivationRequest\x1a\x1f.ns.GetDeviceActivationResponse\"\x00\x12S\n\x15\x43reateDeviceQueueItem\x12 .ns.CreateDeviceQueueItemRequest\x1a\x16.google.protobuf.Empty\"\x00\x12[\n\x19\x46lushDeviceQueueForDevEUI\x12$.ns.FlushDeviceQueueForDevEUIRequest\x1a\x16.google.protobuf.Empty\"\x00\x12s\n\x1cGetDeviceQueueItemsForDevEUI\x12\'.ns.GetDeviceQueueItemsForDevEUIRequest\x1a(.ns.GetDeviceQueueItemsForDevEUIResponse\"\x00\x12s\n\x1cGetNextDownlinkFCntForDevEUI\x12\'.ns.GetNextDownlinkFCntForDevEUIRequest\x1a(.ns.GetNextDownlinkFCntForDevEUIResponse\"\x00\x12J\n\x10GetRandomDevAddr\x12\x16.google.protobuf.Empty\x1a\x1c.ns.GetRandomDevAddrResponse\"\x00\x12[\n\x19\x43reateMACCommandQueueItem\x12$.ns.CreateMACCommandQueueItemRequest\x1a\x16.google.protobuf.Empty\"\x00\x12U\n\x16SendProprietaryPayload\x12!.ns.SendProprietaryPayloadRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x43\n\rCreateGateway\x12\x18.ns.CreateGatewayRequest\x1a\x16.google.protobuf.Empty\"\x00\x12=\n\nGetGateway\x12\x15.ns.GetGatewayRequest\x1a\x16.ns.GetGatewayResponse\"\x00\x12\x43\n\rUpdateGateway\x12\x18.ns.UpdateGatewayRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x43\n\rDeleteGateway\x12\x18.ns.DeleteGatewayRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x7f\n GenerateGatewayClientCertificate\x12+.ns.GenerateGatewayClientCertificateRequest\x1a,.ns.GenerateGatewayClientCertificateResponse\"\x00\x12[\n\x14\x43reateGatewayProfile\x12\x1f.ns.CreateGatewayProfileRequest\x1a .ns.CreateGatewayProfileResponse\"\x00\x12R\n\x11GetGatewayProfile\x12\x1c.ns.GetGatewayProfileRequest\x1a\x1d.ns.GetGatewayProfileResponse\"\x00\x12Q\n\x14UpdateGatewayProfile\x12\x1f.ns.UpdateGatewayProfileRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Q\n\x14\x44\x65leteGatewayProfile\x12\x1f.ns.DeleteGatewayProfileRequest\x1a\x16.google.protobuf.Empty\"\x00\x12L\n\x0fGetGatewayStats\x12\x1a.ns.GetGatewayStatsRequest\x1a\x1b.ns.GetGatewayStatsResponse\"\x00\x12l\n\x19StreamFrameLogsForGateway\x12$.ns.StreamFrameLogsForGatewayRequest\x1a%.ns.StreamFrameLogsForGatewayResponse\"\x00\x30\x01\x12i\n\x18StreamFrameLogsForDevice\x12#.ns.StreamFrameLogsForDeviceRequest\x1a$.ns.StreamFrameLogsForDeviceResponse\"\x00\x30\x01\x12[\n\x14\x43reateMulticastGroup\x12\x1f.ns.CreateMulticastGroupRequest\x1a .ns.CreateMulticastGroupResponse\"\x00\x12R\n\x11GetMulticastGroup\x12\x1c.ns.GetMulticastGroupRequest\x1a\x1d.ns.GetMulticastGroupResponse\"\x00\x12Q\n\x14UpdateMulticastGroup\x12\x1f.ns.UpdateMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Q\n\x14\x44\x65leteMulticastGroup\x12\x1f.ns.DeleteMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"\x00\x12[\n\x19\x41\x64\x64\x44\x65viceToMulticastGroup\x12$.ns.AddDeviceToMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x65\n\x1eRemoveDeviceFromMulticastGroup\x12).ns.RemoveDeviceFromMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"\x00\x12[\n\x19\x45nqueueMulticastQueueItem\x12$.ns.EnqueueMulticastQueueItemRequest\x1a\x16.google.protobuf.Empty\"\x00\x12q\n$FlushMulticastQueueForMulticastGroup\x12/.ns.FlushMulticastQueueForMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x94\x01\n\'GetMulticastQueueItemsForMulticastGroup\x12\x32.ns.GetMulticastQueueItemsForMulticastGroupRequest\x1a\x33.ns.GetMulticastQueueItemsForMulticastGroupResponse\"\x00\x12>\n\nGetVersion\x12\x16.google.protobuf.Empty\x1a\x16.ns.GetVersionResponse\"\x00\x12J\n\x10GetADRAlgorithms\x12\x16.google.protobuf.Empty\x1a\x1c.ns.GetADRAlgorithmsResponse\"\x00\x12j\n\x1fStreamGlobalFrameLogsForGateway\x12\x16.google.protobuf.Empty\x1a+.ns.StreamGlobalFrameLogsForGatewayResponse\"\x00\x30\x01\x12h\n\x1eStreamGlobalFrameLogsForDevice\x12\x16.google.protobuf.Empty\x1a*.ns.StreamGlobalFrameLogsForDeviceResponse\"\x00\x30\x01\x12O\n\x13\x43learDeviceDevNonce\x12\x1e.ns.ClearDeviceDevNonceRequest\x1a\x16.google.protobuf.Empty\"\x00\x42j\n\x14io.chirpstack.api.nsB\x12NetworkServerProtoP\x01Z,github.com/sagar-patel-sls/chirpstack-api/ns\xaa\x02\rchirpstack.nsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.ns.ns_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024io.chirpstack.api.nsB\022NetworkServerProtoP\001Z,github.com/sagar-patel-sls/chirpstack-api/ns\252\002\rchirpstack.ns'
  _GATEWAYSTATSFRAMELOG_METADATAENTRY._options = None
  _GATEWAYSTATSFRAMELOG_METADATAENTRY._serialized_options = b'8\001'
  _RXWINDOW._serialized_start=9187
  _RXWINDOW._serialized_end=9215
  _AGGREGATIONINTERVAL._serialized_start=9217
  _AGGREGATIONINTERVAL._serialized_end=9325
  _MULTICASTGROUPTYPE._serialized_start=9327
  _MULTICASTGROUPTYPE._serialized_end=9373
  _CREATESERVICEPROFILEREQUEST._serialized_start=226
  _CREATESERVICEPROFILEREQUEST._serialized_end=300
  _CREATESERVICEPROFILERESPONSE._serialized_start=302
  _CREATESERVICEPROFILERESPONSE._serialized_end=344
  _GETSERVICEPROFILEREQUEST._serialized_start=346
  _GETSERVICEPROFILEREQUEST._serialized_end=384
  _GETSERVICEPROFILERESPONSE._serialized_start=387
  _GETSERVICEPROFILERESPONSE._serialized_end=555
  _UPDATESERVICEPROFILEREQUEST._serialized_start=557
  _UPDATESERVICEPROFILEREQUEST._serialized_end=631
  _DELETESERVICEPROFILEREQUEST._serialized_start=633
  _DELETESERVICEPROFILEREQUEST._serialized_end=674
  _CREATEROUTINGPROFILEREQUEST._serialized_start=676
  _CREATEROUTINGPROFILEREQUEST._serialized_end=750
  _CREATEROUTINGPROFILERESPONSE._serialized_start=752
  _CREATEROUTINGPROFILERESPONSE._serialized_end=794
  _GETROUTINGPROFILEREQUEST._serialized_start=796
  _GETROUTINGPROFILEREQUEST._serialized_end=834
  _GETROUTINGPROFILERESPONSE._serialized_start=837
  _GETROUTINGPROFILERESPONSE._serialized_end=1005
  _UPDATEROUTINGPROFILEREQUEST._serialized_start=1007
  _UPDATEROUTINGPROFILEREQUEST._serialized_end=1081
  _DELETEROUTINGPROFILEREQUEST._serialized_start=1083
  _DELETEROUTINGPROFILEREQUEST._serialized_end=1124
  _CREATEDEVICEPROFILEREQUEST._serialized_start=1126
  _CREATEDEVICEPROFILEREQUEST._serialized_end=1197
  _CREATEDEVICEPROFILERESPONSE._serialized_start=1199
  _CREATEDEVICEPROFILERESPONSE._serialized_end=1240
  _GETDEVICEPROFILEREQUEST._serialized_start=1242
  _GETDEVICEPROFILEREQUEST._serialized_end=1279
  _GETDEVICEPROFILERESPONSE._serialized_start=1282
  _GETDEVICEPROFILERESPONSE._serialized_end=1447
  _UPDATEDEVICEPROFILEREQUEST._serialized_start=1449
  _UPDATEDEVICEPROFILEREQUEST._serialized_end=1520
  _DELETEDEVICEPROFILEREQUEST._serialized_start=1522
  _DELETEDEVICEPROFILEREQUEST._serialized_end=1562
  _DEVICE._serialized_start=1565
  _DEVICE._serialized_end=1748
  _CREATEDEVICEREQUEST._serialized_start=1750
  _CREATEDEVICEREQUEST._serialized_end=1799
  _GETDEVICEREQUEST._serialized_start=1801
  _GETDEVICEREQUEST._serialized_end=1836
  _GETDEVICERESPONSE._serialized_start=1839
  _GETDEVICERESPONSE._serialized_end=2002
  _UPDATEDEVICEREQUEST._serialized_start=2004
  _UPDATEDEVICEREQUEST._serialized_end=2053
  _DELETEDEVICEREQUEST._serialized_start=2055
  _DELETEDEVICEREQUEST._serialized_end=2093
  _DEVICEACTIVATION._serialized_start=2096
  _DEVICEACTIVATION._serialized_end=2310
  _EXTRASESSIONPARAMETER._serialized_start=2313
  _EXTRASESSIONPARAMETER._serialized_end=2546
  _EXTRACHANNELS._serialized_start=2548
  _EXTRACHANNELS._serialized_end=2627
  _ACTIVATEDEVICEREQUEST._serialized_start=2629
  _ACTIVATEDEVICEREQUEST._serialized_end=2701
  _DEACTIVATEDEVICEREQUEST._serialized_start=2703
  _DEACTIVATEDEVICEREQUEST._serialized_end=2745
  _GETDEVICEACTIVATIONREQUEST._serialized_start=2747
  _GETDEVICEACTIVATIONREQUEST._serialized_end=2792
  _GETDEVICEACTIVATIONRESPONSE._serialized_start=2795
  _GETDEVICEACTIVATIONRESPONSE._serialized_end=2933
  _GETRANDOMDEVADDRRESPONSE._serialized_start=2935
  _GETRANDOMDEVADDRRESPONSE._serialized_end=2979
  _CREATEMACCOMMANDQUEUEITEMREQUEST._serialized_start=2981
  _CREATEMACCOMMANDQUEUEITEMREQUEST._serialized_end=3063
  _SENDPROPRIETARYPAYLOADREQUEST._serialized_start=3066
  _SENDPROPRIETARYPAYLOADREQUEST._serialized_end=3216
  _GATEWAY._serialized_start=3219
  _GATEWAY._serialized_end=3394
  _GATEWAYBOARD._serialized_start=3396
  _GATEWAYBOARD._serialized_end=3455
  _CREATEGATEWAYREQUEST._serialized_start=3457
  _CREATEGATEWAYREQUEST._serialized_end=3509
  _GETGATEWAYREQUEST._serialized_start=3511
  _GETGATEWAYREQUEST._serialized_end=3542
  _GETGATEWAYRESPONSE._serialized_start=3545
  _GETGATEWAYRESPONSE._serialized_end=3792
  _UPDATEGATEWAYREQUEST._serialized_start=3794
  _UPDATEGATEWAYREQUEST._serialized_end=3846
  _DELETEGATEWAYREQUEST._serialized_start=3848
  _DELETEGATEWAYREQUEST._serialized_end=3882
  _GENERATEGATEWAYCLIENTCERTIFICATEREQUEST._serialized_start=3884
  _GENERATEGATEWAYCLIENTCERTIFICATEREQUEST._serialized_end=3937
  _GENERATEGATEWAYCLIENTCERTIFICATERESPONSE._serialized_start=3940
  _GENERATEGATEWAYCLIENTCERTIFICATERESPONSE._serialized_end=4082
  _GATEWAYSTATS._serialized_start=4085
  _GATEWAYSTATS._serialized_end=4264
  _GETGATEWAYSTATSREQUEST._serialized_start=4267
  _GETGATEWAYSTATSREQUEST._serialized_end=4458
  _GETGATEWAYSTATSRESPONSE._serialized_start=4460
  _GETGATEWAYSTATSRESPONSE._serialized_end=4519
  _DEVICEQUEUEITEM._serialized_start=4521
  _DEVICEQUEUEITEM._serialized_end=4644
  _CREATEDEVICEQUEUEITEMREQUEST._serialized_start=4646
  _CREATEDEVICEQUEUEITEMREQUEST._serialized_end=4711
  _FLUSHDEVICEQUEUEFORDEVEUIREQUEST._serialized_start=4713
  _FLUSHDEVICEQUEUEFORDEVEUIREQUEST._serialized_end=4764
  _GETDEVICEQUEUEITEMSFORDEVEUIREQUEST._serialized_start=4766
  _GETDEVICEQUEUEITEMSFORDEVEUIREQUEST._serialized_end=4840
  _GETDEVICEQUEUEITEMSFORDEVEUIRESPONSE._serialized_start=4842
  _GETDEVICEQUEUEITEMSFORDEVEUIRESPONSE._serialized_end=4937
  _GETNEXTDOWNLINKFCNTFORDEVEUIREQUEST._serialized_start=4939
  _GETNEXTDOWNLINKFCNTFORDEVEUIREQUEST._serialized_end=4993
  _GETNEXTDOWNLINKFCNTFORDEVEUIRESPONSE._serialized_start=4995
  _GETNEXTDOWNLINKFCNTFORDEVEUIRESPONSE._serialized_end=5048
  _UPLINKFRAMELOG._serialized_start=5051
  _UPLINKFRAMELOG._serialized_end=5274
  _DOWNLINKFRAMELOG._serialized_start=5277
  _DOWNLINKFRAMELOG._serialized_end=5548
  _GATEWAYSTATSFRAMELOG._serialized_start=5551
  _GATEWAYSTATSFRAMELOG._serialized_end=6060
  _GATEWAYSTATSFRAMELOG_METADATAENTRY._serialized_start=6013
  _GATEWAYSTATSFRAMELOG_METADATAENTRY._serialized_end=6060
  _STREAMFRAMELOGSFORGATEWAYREQUEST._serialized_start=6062
  _STREAMFRAMELOGSFORGATEWAYREQUEST._serialized_end=6116
  _STREAMFRAMELOGSFORGATEWAYRESPONSE._serialized_start=6119
  _STREAMFRAMELOGSFORGATEWAYRESPONSE._serialized_end=6308
  _STREAMGLOBALFRAMELOGSFORGATEWAYRESPONSE._serialized_start=6311
  _STREAMGLOBALFRAMELOGSFORGATEWAYRESPONSE._serialized_end=6527
  _STREAMFRAMELOGSFORDEVICEREQUEST._serialized_start=6529
  _STREAMFRAMELOGSFORDEVICEREQUEST._serialized_end=6579
  _STREAMFRAMELOGSFORDEVICERESPONSE._serialized_start=6582
  _STREAMFRAMELOGSFORDEVICERESPONSE._serialized_end=6721
  _STREAMGLOBALFRAMELOGSFORDEVICERESPONSE._serialized_start=6724
  _STREAMGLOBALFRAMELOGSFORDEVICERESPONSE._serialized_end=6886
  _GETVERSIONRESPONSE._serialized_start=6888
  _GETVERSIONRESPONSE._serialized_end=6957
  _GATEWAYPROFILE._serialized_start=6960
  _GATEWAYPROFILE._serialized_end=7113
  _GATEWAYPROFILEEXTRACHANNEL._serialized_start=7116
  _GATEWAYPROFILEEXTRACHANNEL._serialized_end=7266
  _CREATEGATEWAYPROFILEREQUEST._serialized_start=7268
  _CREATEGATEWAYPROFILEREQUEST._serialized_end=7342
  _CREATEGATEWAYPROFILERESPONSE._serialized_start=7344
  _CREATEGATEWAYPROFILERESPONSE._serialized_end=7386
  _GETGATEWAYPROFILEREQUEST._serialized_start=7388
  _GETGATEWAYPROFILEREQUEST._serialized_end=7426
  _GETGATEWAYPROFILERESPONSE._serialized_start=7429
  _GETGATEWAYPROFILERESPONSE._serialized_end=7597
  _UPDATEGATEWAYPROFILEREQUEST._serialized_start=7599
  _UPDATEGATEWAYPROFILEREQUEST._serialized_end=7673
  _DELETEGATEWAYPROFILEREQUEST._serialized_start=7675
  _DELETEGATEWAYPROFILEREQUEST._serialized_end=7716
  _MULTICASTGROUP._serialized_start=7719
  _MULTICASTGROUP._serialized_end=7958
  _CREATEMULTICASTGROUPREQUEST._serialized_start=7960
  _CREATEMULTICASTGROUPREQUEST._serialized_end=8034
  _CREATEMULTICASTGROUPRESPONSE._serialized_start=8036
  _CREATEMULTICASTGROUPRESPONSE._serialized_end=8078
  _GETMULTICASTGROUPREQUEST._serialized_start=8080
  _GETMULTICASTGROUPREQUEST._serialized_end=8118
  _GETMULTICASTGROUPRESPONSE._serialized_start=8121
  _GETMULTICASTGROUPRESPONSE._serialized_end=8289
  _UPDATEMULTICASTGROUPREQUEST._serialized_start=8291
  _UPDATEMULTICASTGROUPREQUEST._serialized_end=8365
  _DELETEMULTICASTGROUPREQUEST._serialized_start=8367
  _DELETEMULTICASTGROUPREQUEST._serialized_end=8408
  _ADDDEVICETOMULTICASTGROUPREQUEST._serialized_start=8410
  _ADDDEVICETOMULTICASTGROUPREQUEST._serialized_end=8489
  _REMOVEDEVICEFROMMULTICASTGROUPREQUEST._serialized_start=8491
  _REMOVEDEVICEFROMMULTICASTGROUPREQUEST._serialized_end=8575
  _MULTICASTQUEUEITEM._serialized_start=8577
  _MULTICASTQUEUEITEM._serialized_end=8677
  _ENQUEUEMULTICASTQUEUEITEMREQUEST._serialized_start=8679
  _ENQUEUEMULTICASTQUEUEITEMREQUEST._serialized_end=8767
  _FLUSHMULTICASTQUEUEFORMULTICASTGROUPREQUEST._serialized_start=8769
  _FLUSHMULTICASTQUEUEFORMULTICASTGROUPREQUEST._serialized_end=8842
  _GETMULTICASTQUEUEITEMSFORMULTICASTGROUPREQUEST._serialized_start=8844
  _GETMULTICASTQUEUEITEMSFORMULTICASTGROUPREQUEST._serialized_end=8920
  _GETMULTICASTQUEUEITEMSFORMULTICASTGROUPRESPONSE._serialized_start=8922
  _GETMULTICASTQUEUEITEMSFORMULTICASTGROUPRESPONSE._serialized_end=9026
  _GETADRALGORITHMSRESPONSE._serialized_start=9028
  _GETADRALGORITHMSRESPONSE._serialized_end=9096
  _ADRALGORITHM._serialized_start=9098
  _ADRALGORITHM._serialized_end=9138
  _CLEARDEVICEDEVNONCEREQUEST._serialized_start=9140
  _CLEARDEVICEDEVNONCEREQUEST._serialized_end=9185
  _NETWORKSERVERSERVICE._serialized_start=9376
  _NETWORKSERVERSERVICE._serialized_end=13952
# @@protoc_insertion_point(module_scope)
