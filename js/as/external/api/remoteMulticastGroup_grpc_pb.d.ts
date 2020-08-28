// GENERATED CODE -- DO NOT EDIT!

// package: api
// file: as/external/api/remoteMulticastGroup.proto

import * as as_external_api_remoteMulticastGroup_pb from "../../../as/external/api/remoteMulticastGroup_pb";
import * as google_protobuf_empty_pb from "google-protobuf/google/protobuf/empty_pb";
import * as grpc from "grpc";

interface IRemoteMulticastGroupServiceService extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
  create: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupRequest, as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupResponse>;
  get: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupRequest, as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupResponse>;
  update: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.UpdateRemoteMulticastGroupRequest, google_protobuf_empty_pb.Empty>;
  delete: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.DeleteRemoteMulticastGroupRequest, google_protobuf_empty_pb.Empty>;
  list: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupRequest, as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupResponse>;
  addDevice: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.AddDeviceToRemoteMulticastGroupRequest, google_protobuf_empty_pb.Empty>;
  resetDevice: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.ResetRemoteMulticastDeviceRequest, google_protobuf_empty_pb.Empty>;
  removeDevice: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.RemoveDeviceFromRemoteMulticastGroupRequest, google_protobuf_empty_pb.Empty>;
  listDevicesForRemoteMulticast: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest, as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceResponse>;
  getDevicesList: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest, as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDevicesResponse>;
  getDeploymentDevice: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceRequest, as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceResponse>;
  enqueue: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemRequest, as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemResponse>;
  flushQueue: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.FlushRemoteMulticastGroupQueueItemsRequest, google_protobuf_empty_pb.Empty>;
  listQueue: grpc.MethodDefinition<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsRequest, as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsResponse>;
}

export const RemoteMulticastGroupServiceService: IRemoteMulticastGroupServiceService;

export class RemoteMulticastGroupServiceClient extends grpc.Client {
  constructor(address: string, credentials: grpc.ChannelCredentials, options?: object);
  create(argument: as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupRequest, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupResponse>): grpc.ClientUnaryCall;
  create(argument: as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupResponse>): grpc.ClientUnaryCall;
  create(argument: as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupResponse>): grpc.ClientUnaryCall;
  get(argument: as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupRequest, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupResponse>): grpc.ClientUnaryCall;
  get(argument: as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupResponse>): grpc.ClientUnaryCall;
  get(argument: as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupResponse>): grpc.ClientUnaryCall;
  update(argument: as_external_api_remoteMulticastGroup_pb.UpdateRemoteMulticastGroupRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  update(argument: as_external_api_remoteMulticastGroup_pb.UpdateRemoteMulticastGroupRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  update(argument: as_external_api_remoteMulticastGroup_pb.UpdateRemoteMulticastGroupRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  delete(argument: as_external_api_remoteMulticastGroup_pb.DeleteRemoteMulticastGroupRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  delete(argument: as_external_api_remoteMulticastGroup_pb.DeleteRemoteMulticastGroupRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  delete(argument: as_external_api_remoteMulticastGroup_pb.DeleteRemoteMulticastGroupRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  list(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupRequest, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupResponse>): grpc.ClientUnaryCall;
  list(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupResponse>): grpc.ClientUnaryCall;
  list(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupResponse>): grpc.ClientUnaryCall;
  addDevice(argument: as_external_api_remoteMulticastGroup_pb.AddDeviceToRemoteMulticastGroupRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  addDevice(argument: as_external_api_remoteMulticastGroup_pb.AddDeviceToRemoteMulticastGroupRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  addDevice(argument: as_external_api_remoteMulticastGroup_pb.AddDeviceToRemoteMulticastGroupRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  resetDevice(argument: as_external_api_remoteMulticastGroup_pb.ResetRemoteMulticastDeviceRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  resetDevice(argument: as_external_api_remoteMulticastGroup_pb.ResetRemoteMulticastDeviceRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  resetDevice(argument: as_external_api_remoteMulticastGroup_pb.ResetRemoteMulticastDeviceRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  removeDevice(argument: as_external_api_remoteMulticastGroup_pb.RemoveDeviceFromRemoteMulticastGroupRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  removeDevice(argument: as_external_api_remoteMulticastGroup_pb.RemoveDeviceFromRemoteMulticastGroupRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  removeDevice(argument: as_external_api_remoteMulticastGroup_pb.RemoveDeviceFromRemoteMulticastGroupRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  listDevicesForRemoteMulticast(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceResponse>): grpc.ClientUnaryCall;
  listDevicesForRemoteMulticast(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceResponse>): grpc.ClientUnaryCall;
  listDevicesForRemoteMulticast(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceResponse>): grpc.ClientUnaryCall;
  getDevicesList(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDevicesResponse>): grpc.ClientUnaryCall;
  getDevicesList(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDevicesResponse>): grpc.ClientUnaryCall;
  getDevicesList(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDevicesResponse>): grpc.ClientUnaryCall;
  getDeploymentDevice(argument: as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceRequest, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceResponse>): grpc.ClientUnaryCall;
  getDeploymentDevice(argument: as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceResponse>): grpc.ClientUnaryCall;
  getDeploymentDevice(argument: as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceResponse>): grpc.ClientUnaryCall;
  enqueue(argument: as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemRequest, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemResponse>): grpc.ClientUnaryCall;
  enqueue(argument: as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemResponse>): grpc.ClientUnaryCall;
  enqueue(argument: as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemResponse>): grpc.ClientUnaryCall;
  flushQueue(argument: as_external_api_remoteMulticastGroup_pb.FlushRemoteMulticastGroupQueueItemsRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  flushQueue(argument: as_external_api_remoteMulticastGroup_pb.FlushRemoteMulticastGroupQueueItemsRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  flushQueue(argument: as_external_api_remoteMulticastGroup_pb.FlushRemoteMulticastGroupQueueItemsRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  listQueue(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsRequest, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsResponse>): grpc.ClientUnaryCall;
  listQueue(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsResponse>): grpc.ClientUnaryCall;
  listQueue(argument: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsResponse>): grpc.ClientUnaryCall;
}
