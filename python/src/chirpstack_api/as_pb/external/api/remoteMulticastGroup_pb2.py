# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/remoteMulticastGroup.proto
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
from chirpstack_api.as_pb.external.api import device_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_device__pb2
from chirpstack_api.as_pb.external.api import multicastGroup_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_multicastGroup__pb2
from chirpstack_api.as_pb.external.api import fuotaDeployment_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<chirpstack-api/as_pb/external/api/remoteMulticastGroup.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a.chirpstack-api/as_pb/external/api/device.proto\x1a\x36\x63hirpstack-api/as_pb/external/api/multicastGroup.proto\x1a\x37\x63hirpstack-api/as_pb/external/api/fuotaDeployment.proto\"\x88\x03\n\x14RemoteMulticastGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12,\n\x12service_profile_id\x18\x03 \x01(\tR\x10serviceProfileID\x12+\n\ngroup_type\x18\x04 \x01(\x0e\x32\x17.api.MulticastGroupType\x12\n\n\x02\x64r\x18\x05 \x01(\r\x12\x11\n\tfrequency\x18\x06 \x01(\r\x12\x18\n\x10ping_slot_period\x18\x07 \x01(\r\x12\x0f\n\x07mc_addr\x18\x08 \x01(\t\x12\x14\n\x0cmc_nwk_s_key\x18\t \x01(\t\x12\x14\n\x0cmc_app_s_key\x18\n \x01(\t\x12\r\n\x05\x66_cnt\x18\x0b \x01(\r\x12\r\n\x05state\x18\x0c \x01(\t\x12\x32\n\x0funicast_timeout\x18\r \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x33\n\x0fnext_step_after\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x84\x04\n\x1fRemoteMulticastDeploymentDevice\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x07\x64\x65v_eui\x18\x02 \x01(\tR\x06\x64\x65vEUI\x12\x13\n\x0b\x64\x65vice_name\x18\x03 \x01(\t\x12%\n\x0e\x61pplication_id\x18\x04 \x01(\x03R\rapplicationID\x12\x18\n\x10\x61pplication_name\x18\x05 \x01(\t\x12<\n\x0clast_seen_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nlastSeenAt\x12\x13\n\x0bmc_group_id\x18\x07 \x01(\r\x12.\n\ncreated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\x05state\x18\n \x01(\x0e\x32\x1f.api.FUOTADeploymentDeviceState\x12\x15\n\rerror_message\x18\x0b \x01(\t\x12>\n\x05\x65rror\x18\x0c \x03(\x0b\x32/.api.RemoteMulticastDeploymentDevice.ErrorEntry\x1a,\n\nErrorEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x93\x01\n\x1cRemoteMulticastGroupListItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12,\n\x12service_profile_id\x18\x03 \x01(\tR\x10serviceProfileID\x12\x1c\n\x14service_profile_name\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\"^\n!CreateRemoteMulticastGroupRequest\x12\x39\n\x16remote_multicast_group\x18\x01 \x01(\x0b\x32\x19.api.RemoteMulticastGroup\"0\n\"CreateRemoteMulticastGroupResponse\x12\n\n\x02id\x18\x01 \x01(\t\",\n\x1eGetRemoteMulticastGroupRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xbc\x01\n\x1fGetRemoteMulticastGroupResponse\x12\x39\n\x16remote_multicast_group\x18\x01 \x01(\x0b\x32\x19.api.RemoteMulticastGroup\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa7\x01\n\x1fListRemoteMulticastGroupRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\'\n\x0forganization_id\x18\x03 \x01(\x03R\x0eorganizationID\x12,\n\x12service_profile_id\x18\x04 \x01(\tR\x10serviceProfileID\x12\x0e\n\x06search\x18\x05 \x01(\t\"j\n ListRemoteMulticastGroupResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12\x31\n\x06result\x18\x02 \x03(\x0b\x32!.api.RemoteMulticastGroupListItem\"^\n!UpdateRemoteMulticastGroupRequest\x12\x39\n\x16remote_multicast_group\x18\x01 \x01(\x0b\x32\x19.api.RemoteMulticastGroup\"/\n!DeleteRemoteMulticastGroupRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x83\x01\n&AddDeviceToRemoteMulticastGroupRequest\x12>\n\x19remote_multicast_group_id\x18\x01 \x01(\tR\x1bremoteMulticastDeploymentID\x12\x19\n\x08\x64\x65v_euis\x18\x02 \x03(\tR\x07\x64\x65vEUIs\"\x86\x01\n+RemoveDeviceFromRemoteMulticastGroupRequest\x12>\n\x19remote_multicast_group_id\x18\x01 \x01(\tR\x1bremoteMulticastDeploymentID\x12\x17\n\x07\x64\x65v_eui\x18\x02 \x01(\tR\x06\x64\x65vEUI\"\xb8\x01\n ListRemoteMulticastDeviceRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12>\n\x19remote_multicast_group_id\x18\x03 \x01(\tR\x1bremoteMulticastDeploymentID\x12%\n\x0e\x61pplication_id\x18\x04 \x01(\x03R\rapplicationID\x12\x0e\n\x06search\x18\x05 \x01(\t\"]\n!ListRemoteMulticastDeviceResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12#\n\x06result\x18\x02 \x03(\x0b\x32\x13.api.DeviceListItem\"|\n!ResetRemoteMulticastDeviceRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\x12>\n\x19remote_multicast_group_id\x18\x02 \x01(\tR\x1bremoteMulticastDeploymentID\"o\n\"ListRemoteMulticastDevicesResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12\x34\n\x06result\x18\x02 \x03(\x0b\x32$.api.RemoteMulticastDeploymentDevice\"\x84\x01\n)GetRemoteMulticastDeploymentDeviceRequest\x12>\n\x19remote_multicast_group_id\x18\x01 \x01(\tR\x1bremoteMulticastDeploymentID\x12\x17\n\x07\x64\x65v_eui\x18\x02 \x01(\tR\x06\x64\x65vEUI\"m\n*GetRemoteMulticastDeploymentDeviceResponse\x12?\n\x11\x64\x65ployment_device\x18\x01 \x01(\x0b\x32$.api.RemoteMulticastDeploymentDevice\"\x82\x01\n\x18RemoteMulticastQueueItem\x12\x39\n\x19remote_multicast_group_id\x18\x01 \x01(\tR\x16remoteMulticastGroupID\x12\r\n\x05\x66_cnt\x18\x02 \x01(\r\x12\x0e\n\x06\x66_port\x18\x03 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"l\n&EnqueueRemoteMulticastQueueItemRequest\x12\x42\n\x1bremote_multicast_queue_item\x18\x01 \x01(\x0b\x32\x1d.api.RemoteMulticastQueueItem\"8\n\'EnqueueRemoteMulticastQueueItemResponse\x12\r\n\x05\x66_cnt\x18\x01 \x01(\r\"g\n*FlushRemoteMulticastGroupQueueItemsRequest\x12\x39\n\x19remote_multicast_group_id\x18\x01 \x01(\tR\x16remoteMulticastGroupID\"f\n)ListRemoteMulticastGroupQueueItemsRequest\x12\x39\n\x19remote_multicast_group_id\x18\x01 \x01(\tR\x16remoteMulticastGroupID\"q\n*ListRemoteMulticastGroupQueueItemsResponse\x12\x43\n\x1cremote_multicast_queue_items\x18\x01 \x03(\x0b\x32\x1d.api.RemoteMulticastQueueItem2\x8f\x12\n\x1bRemoteMulticastGroupService\x12\x82\x01\n\x06\x43reate\x12&.api.CreateRemoteMulticastGroupRequest\x1a\'.api.CreateRemoteMulticastGroupResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1c/api/remote-multicast-groups:\x01*\x12{\n\x03Get\x12#.api.GetRemoteMulticastGroupRequest\x1a$.api.GetRemoteMulticastGroupResponse\")\x82\xd3\xe4\x93\x02#\x12!/api/remote-multicast-groups/{id}\x12\x8d\x01\n\x06Update\x12&.api.UpdateRemoteMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"C\x82\xd3\xe4\x93\x02=\x1a\x38/api/remote-multicast-groups/{remote_multicast_group.id}:\x01*\x12s\n\x06\x44\x65lete\x12&.api.DeleteRemoteMulticastGroupRequest\x1a\x16.google.protobuf.Empty\")\x82\xd3\xe4\x93\x02#*!/api/remote-multicast-groups/{id}\x12y\n\x04List\x12$.api.ListRemoteMulticastGroupRequest\x1a%.api.ListRemoteMulticastGroupResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/api/remote-multicast-groups\x12\x9d\x01\n\tAddDevice\x12+.api.AddDeviceToRemoteMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"K\x82\xd3\xe4\x93\x02\x45\"@/api/remote-multicast-groups/{remote_multicast_group_id}/devices:\x01*\x12\xa7\x01\n\x0bResetDevice\x12&.api.ResetRemoteMulticastDeviceRequest\x1a\x16.google.protobuf.Empty\"X\x82\xd3\xe4\x93\x02R\x1aP/api/remote-multicast-groups/{remote_multicast_group_id}/devices/{dev_eui}/reset\x12\xac\x01\n\x0cRemoveDevice\x12\x30.api.RemoveDeviceFromRemoteMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"R\x82\xd3\xe4\x93\x02L*J/api/remote-multicast-groups/{remote_multicast_group_id}/devices/{dev_eui}\x12\xd5\x01\n\x1dListDevicesForRemoteMulticast\x12%.api.ListRemoteMulticastDeviceRequest\x1a&.api.ListRemoteMulticastDeviceResponse\"e\x82\xd3\xe4\x93\x02_\x12]/api/remote-multicast-groups/{remote_multicast_group_id}/application/{application_id}/devices\x12\xaa\x01\n\x0eGetDevicesList\x12%.api.ListRemoteMulticastDeviceRequest\x1a\'.api.ListRemoteMulticastDevicesResponse\"H\x82\xd3\xe4\x93\x02\x42\x12@/api/remote-multicast-groups/{remote_multicast_group_id}/devices\x12\xca\x01\n\x13GetDeploymentDevice\x12..api.GetRemoteMulticastDeploymentDeviceRequest\x1a/.api.GetRemoteMulticastDeploymentDeviceResponse\"R\x82\xd3\xe4\x93\x02L\x12J/api/remote-multicast-groups/{remote_multicast_group_id}/devices/{dev_eui}\x12\xcb\x01\n\x07\x45nqueue\x12+.api.EnqueueRemoteMulticastQueueItemRequest\x1a,.api.EnqueueRemoteMulticastQueueItemResponse\"e\x82\xd3\xe4\x93\x02_\"Z/api/remote-multicast-groups/{remote_multicast_queue_item.remote_multicast_group_id}/queue:\x01*\x12\x9d\x01\n\nFlushQueue\x12/.api.FlushRemoteMulticastGroupQueueItemsRequest\x1a\x16.google.protobuf.Empty\"F\x82\xd3\xe4\x93\x02@*>/api/remote-multicast-groups/{remote_multicast_group_id}/queue\x12\xb4\x01\n\tListQueue\x12..api.ListRemoteMulticastGroupQueueItemsRequest\x1a/.api.ListRemoteMulticastGroupQueueItemsResponse\"F\x82\xd3\xe4\x93\x02@\x12>/api/remote-multicast-groups/{remote_multicast_group_id}/queueB\x81\x01\n!io.chirpstack.api.as.external.apiB\x19RemoteMulticastGroupProtoP\x01Z?github.com/sagar-patel-sls/chirpstack-api/go/v3/as/external/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.as_pb.external.api.remoteMulticastGroup_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.chirpstack.api.as.external.apiB\031RemoteMulticastGroupProtoP\001Z?github.com/sagar-patel-sls/chirpstack-api/go/v3/as/external/api'
  _REMOTEMULTICASTDEPLOYMENTDEVICE_ERRORENTRY._options = None
  _REMOTEMULTICASTDEPLOYMENTDEVICE_ERRORENTRY._serialized_options = b'8\001'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['Create']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002!\"\034/api/remote-multicast-groups:\001*'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['Get']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002#\022!/api/remote-multicast-groups/{id}'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['Update']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002=\0328/api/remote-multicast-groups/{remote_multicast_group.id}:\001*'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['Delete']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002#*!/api/remote-multicast-groups/{id}'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['List']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\036\022\034/api/remote-multicast-groups'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['AddDevice']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['AddDevice']._serialized_options = b'\202\323\344\223\002E\"@/api/remote-multicast-groups/{remote_multicast_group_id}/devices:\001*'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['ResetDevice']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['ResetDevice']._serialized_options = b'\202\323\344\223\002R\032P/api/remote-multicast-groups/{remote_multicast_group_id}/devices/{dev_eui}/reset'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['RemoveDevice']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['RemoveDevice']._serialized_options = b'\202\323\344\223\002L*J/api/remote-multicast-groups/{remote_multicast_group_id}/devices/{dev_eui}'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['ListDevicesForRemoteMulticast']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['ListDevicesForRemoteMulticast']._serialized_options = b'\202\323\344\223\002_\022]/api/remote-multicast-groups/{remote_multicast_group_id}/application/{application_id}/devices'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['GetDevicesList']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['GetDevicesList']._serialized_options = b'\202\323\344\223\002B\022@/api/remote-multicast-groups/{remote_multicast_group_id}/devices'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['GetDeploymentDevice']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['GetDeploymentDevice']._serialized_options = b'\202\323\344\223\002L\022J/api/remote-multicast-groups/{remote_multicast_group_id}/devices/{dev_eui}'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['Enqueue']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['Enqueue']._serialized_options = b'\202\323\344\223\002_\"Z/api/remote-multicast-groups/{remote_multicast_queue_item.remote_multicast_group_id}/queue:\001*'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['FlushQueue']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['FlushQueue']._serialized_options = b'\202\323\344\223\002@*>/api/remote-multicast-groups/{remote_multicast_group_id}/queue'
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['ListQueue']._options = None
  _REMOTEMULTICASTGROUPSERVICE.methods_by_name['ListQueue']._serialized_options = b'\202\323\344\223\002@\022>/api/remote-multicast-groups/{remote_multicast_group_id}/queue'
  _REMOTEMULTICASTGROUP._serialized_start=355
  _REMOTEMULTICASTGROUP._serialized_end=747
  _REMOTEMULTICASTDEPLOYMENTDEVICE._serialized_start=750
  _REMOTEMULTICASTDEPLOYMENTDEVICE._serialized_end=1266
  _REMOTEMULTICASTDEPLOYMENTDEVICE_ERRORENTRY._serialized_start=1222
  _REMOTEMULTICASTDEPLOYMENTDEVICE_ERRORENTRY._serialized_end=1266
  _REMOTEMULTICASTGROUPLISTITEM._serialized_start=1269
  _REMOTEMULTICASTGROUPLISTITEM._serialized_end=1416
  _CREATEREMOTEMULTICASTGROUPREQUEST._serialized_start=1418
  _CREATEREMOTEMULTICASTGROUPREQUEST._serialized_end=1512
  _CREATEREMOTEMULTICASTGROUPRESPONSE._serialized_start=1514
  _CREATEREMOTEMULTICASTGROUPRESPONSE._serialized_end=1562
  _GETREMOTEMULTICASTGROUPREQUEST._serialized_start=1564
  _GETREMOTEMULTICASTGROUPREQUEST._serialized_end=1608
  _GETREMOTEMULTICASTGROUPRESPONSE._serialized_start=1611
  _GETREMOTEMULTICASTGROUPRESPONSE._serialized_end=1799
  _LISTREMOTEMULTICASTGROUPREQUEST._serialized_start=1802
  _LISTREMOTEMULTICASTGROUPREQUEST._serialized_end=1969
  _LISTREMOTEMULTICASTGROUPRESPONSE._serialized_start=1971
  _LISTREMOTEMULTICASTGROUPRESPONSE._serialized_end=2077
  _UPDATEREMOTEMULTICASTGROUPREQUEST._serialized_start=2079
  _UPDATEREMOTEMULTICASTGROUPREQUEST._serialized_end=2173
  _DELETEREMOTEMULTICASTGROUPREQUEST._serialized_start=2175
  _DELETEREMOTEMULTICASTGROUPREQUEST._serialized_end=2222
  _ADDDEVICETOREMOTEMULTICASTGROUPREQUEST._serialized_start=2225
  _ADDDEVICETOREMOTEMULTICASTGROUPREQUEST._serialized_end=2356
  _REMOVEDEVICEFROMREMOTEMULTICASTGROUPREQUEST._serialized_start=2359
  _REMOVEDEVICEFROMREMOTEMULTICASTGROUPREQUEST._serialized_end=2493
  _LISTREMOTEMULTICASTDEVICEREQUEST._serialized_start=2496
  _LISTREMOTEMULTICASTDEVICEREQUEST._serialized_end=2680
  _LISTREMOTEMULTICASTDEVICERESPONSE._serialized_start=2682
  _LISTREMOTEMULTICASTDEVICERESPONSE._serialized_end=2775
  _RESETREMOTEMULTICASTDEVICEREQUEST._serialized_start=2777
  _RESETREMOTEMULTICASTDEVICEREQUEST._serialized_end=2901
  _LISTREMOTEMULTICASTDEVICESRESPONSE._serialized_start=2903
  _LISTREMOTEMULTICASTDEVICESRESPONSE._serialized_end=3014
  _GETREMOTEMULTICASTDEPLOYMENTDEVICEREQUEST._serialized_start=3017
  _GETREMOTEMULTICASTDEPLOYMENTDEVICEREQUEST._serialized_end=3149
  _GETREMOTEMULTICASTDEPLOYMENTDEVICERESPONSE._serialized_start=3151
  _GETREMOTEMULTICASTDEPLOYMENTDEVICERESPONSE._serialized_end=3260
  _REMOTEMULTICASTQUEUEITEM._serialized_start=3263
  _REMOTEMULTICASTQUEUEITEM._serialized_end=3393
  _ENQUEUEREMOTEMULTICASTQUEUEITEMREQUEST._serialized_start=3395
  _ENQUEUEREMOTEMULTICASTQUEUEITEMREQUEST._serialized_end=3503
  _ENQUEUEREMOTEMULTICASTQUEUEITEMRESPONSE._serialized_start=3505
  _ENQUEUEREMOTEMULTICASTQUEUEITEMRESPONSE._serialized_end=3561
  _FLUSHREMOTEMULTICASTGROUPQUEUEITEMSREQUEST._serialized_start=3563
  _FLUSHREMOTEMULTICASTGROUPQUEUEITEMSREQUEST._serialized_end=3666
  _LISTREMOTEMULTICASTGROUPQUEUEITEMSREQUEST._serialized_start=3668
  _LISTREMOTEMULTICASTGROUPQUEUEITEMSREQUEST._serialized_end=3770
  _LISTREMOTEMULTICASTGROUPQUEUEITEMSRESPONSE._serialized_start=3772
  _LISTREMOTEMULTICASTGROUPQUEUEITEMSRESPONSE._serialized_end=3885
  _REMOTEMULTICASTGROUPSERVICE._serialized_start=3888
  _REMOTEMULTICASTGROUPSERVICE._serialized_end=6207
# @@protoc_insertion_point(module_scope)
