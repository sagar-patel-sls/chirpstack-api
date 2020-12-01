// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var as_external_api_remoteMulticastGroup_pb = require('../../../as/external/api/remoteMulticastGroup_pb.js');
var google_api_annotations_pb = require('../../../google/api/annotations_pb.js');
var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');
var google_protobuf_duration_pb = require('google-protobuf/google/protobuf/duration_pb.js');
var google_protobuf_empty_pb = require('google-protobuf/google/protobuf/empty_pb.js');
var as_external_api_device_pb = require('../../../as/external/api/device_pb.js');
var as_external_api_multicastGroup_pb = require('../../../as/external/api/multicastGroup_pb.js');
var as_external_api_fuotaDeployment_pb = require('../../../as/external/api/fuotaDeployment_pb.js');

function serialize_api_AddDeviceToRemoteMulticastGroupRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.AddDeviceToRemoteMulticastGroupRequest)) {
    throw new Error('Expected argument of type api.AddDeviceToRemoteMulticastGroupRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_AddDeviceToRemoteMulticastGroupRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.AddDeviceToRemoteMulticastGroupRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_CreateRemoteMulticastGroupRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupRequest)) {
    throw new Error('Expected argument of type api.CreateRemoteMulticastGroupRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_CreateRemoteMulticastGroupRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_CreateRemoteMulticastGroupResponse(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupResponse)) {
    throw new Error('Expected argument of type api.CreateRemoteMulticastGroupResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_CreateRemoteMulticastGroupResponse(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_DeleteRemoteMulticastGroupRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.DeleteRemoteMulticastGroupRequest)) {
    throw new Error('Expected argument of type api.DeleteRemoteMulticastGroupRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_DeleteRemoteMulticastGroupRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.DeleteRemoteMulticastGroupRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_EnqueueRemoteMulticastQueueItemRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemRequest)) {
    throw new Error('Expected argument of type api.EnqueueRemoteMulticastQueueItemRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_EnqueueRemoteMulticastQueueItemRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_EnqueueRemoteMulticastQueueItemResponse(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemResponse)) {
    throw new Error('Expected argument of type api.EnqueueRemoteMulticastQueueItemResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_EnqueueRemoteMulticastQueueItemResponse(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_FlushRemoteMulticastGroupQueueItemsRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.FlushRemoteMulticastGroupQueueItemsRequest)) {
    throw new Error('Expected argument of type api.FlushRemoteMulticastGroupQueueItemsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_FlushRemoteMulticastGroupQueueItemsRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.FlushRemoteMulticastGroupQueueItemsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetRemoteMulticastDeploymentDeviceRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceRequest)) {
    throw new Error('Expected argument of type api.GetRemoteMulticastDeploymentDeviceRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetRemoteMulticastDeploymentDeviceRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetRemoteMulticastDeploymentDeviceResponse(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceResponse)) {
    throw new Error('Expected argument of type api.GetRemoteMulticastDeploymentDeviceResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetRemoteMulticastDeploymentDeviceResponse(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetRemoteMulticastGroupRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupRequest)) {
    throw new Error('Expected argument of type api.GetRemoteMulticastGroupRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetRemoteMulticastGroupRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetRemoteMulticastGroupResponse(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupResponse)) {
    throw new Error('Expected argument of type api.GetRemoteMulticastGroupResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetRemoteMulticastGroupResponse(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ListRemoteMulticastDeviceRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest)) {
    throw new Error('Expected argument of type api.ListRemoteMulticastDeviceRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ListRemoteMulticastDeviceRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ListRemoteMulticastDeviceResponse(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceResponse)) {
    throw new Error('Expected argument of type api.ListRemoteMulticastDeviceResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ListRemoteMulticastDeviceResponse(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ListRemoteMulticastDevicesResponse(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDevicesResponse)) {
    throw new Error('Expected argument of type api.ListRemoteMulticastDevicesResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ListRemoteMulticastDevicesResponse(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDevicesResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ListRemoteMulticastGroupQueueItemsRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsRequest)) {
    throw new Error('Expected argument of type api.ListRemoteMulticastGroupQueueItemsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ListRemoteMulticastGroupQueueItemsRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ListRemoteMulticastGroupQueueItemsResponse(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsResponse)) {
    throw new Error('Expected argument of type api.ListRemoteMulticastGroupQueueItemsResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ListRemoteMulticastGroupQueueItemsResponse(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ListRemoteMulticastGroupRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupRequest)) {
    throw new Error('Expected argument of type api.ListRemoteMulticastGroupRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ListRemoteMulticastGroupRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ListRemoteMulticastGroupResponse(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupResponse)) {
    throw new Error('Expected argument of type api.ListRemoteMulticastGroupResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ListRemoteMulticastGroupResponse(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_RemoveDeviceFromRemoteMulticastGroupRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.RemoveDeviceFromRemoteMulticastGroupRequest)) {
    throw new Error('Expected argument of type api.RemoveDeviceFromRemoteMulticastGroupRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_RemoveDeviceFromRemoteMulticastGroupRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.RemoveDeviceFromRemoteMulticastGroupRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ResetRemoteMulticastDeviceRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.ResetRemoteMulticastDeviceRequest)) {
    throw new Error('Expected argument of type api.ResetRemoteMulticastDeviceRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ResetRemoteMulticastDeviceRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.ResetRemoteMulticastDeviceRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_UpdateRemoteMulticastGroupRequest(arg) {
  if (!(arg instanceof as_external_api_remoteMulticastGroup_pb.UpdateRemoteMulticastGroupRequest)) {
    throw new Error('Expected argument of type api.UpdateRemoteMulticastGroupRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_UpdateRemoteMulticastGroupRequest(buffer_arg) {
  return as_external_api_remoteMulticastGroup_pb.UpdateRemoteMulticastGroupRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_google_protobuf_Empty(arg) {
  if (!(arg instanceof google_protobuf_empty_pb.Empty)) {
    throw new Error('Expected argument of type google.protobuf.Empty');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_google_protobuf_Empty(buffer_arg) {
  return google_protobuf_empty_pb.Empty.deserializeBinary(new Uint8Array(buffer_arg));
}


// RemoteMulticastGroupService is the service managing multicast-groups.
var RemoteMulticastGroupServiceService = exports.RemoteMulticastGroupServiceService = {
  // Create creates the given remote multicast-group.
  create: {
    path: '/api.RemoteMulticastGroupService/Create',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupRequest,
    responseType: as_external_api_remoteMulticastGroup_pb.CreateRemoteMulticastGroupResponse,
    requestSerialize: serialize_api_CreateRemoteMulticastGroupRequest,
    requestDeserialize: deserialize_api_CreateRemoteMulticastGroupRequest,
    responseSerialize: serialize_api_CreateRemoteMulticastGroupResponse,
    responseDeserialize: deserialize_api_CreateRemoteMulticastGroupResponse,
  },
  // Get returns a remote multicast-group given an ID.
  get: {
    path: '/api.RemoteMulticastGroupService/Get',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupRequest,
    responseType: as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastGroupResponse,
    requestSerialize: serialize_api_GetRemoteMulticastGroupRequest,
    requestDeserialize: deserialize_api_GetRemoteMulticastGroupRequest,
    responseSerialize: serialize_api_GetRemoteMulticastGroupResponse,
    responseDeserialize: deserialize_api_GetRemoteMulticastGroupResponse,
  },
  // Update updates the given remote multicast-group.
  update: {
    path: '/api.RemoteMulticastGroupService/Update',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.UpdateRemoteMulticastGroupRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_api_UpdateRemoteMulticastGroupRequest,
    requestDeserialize: deserialize_api_UpdateRemoteMulticastGroupRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // Delete deletes a remote multicast-group given an ID.
  delete: {
    path: '/api.RemoteMulticastGroupService/Delete',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.DeleteRemoteMulticastGroupRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_api_DeleteRemoteMulticastGroupRequest,
    requestDeserialize: deserialize_api_DeleteRemoteMulticastGroupRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // List lists the available remote multicast-groups.
  list: {
    path: '/api.RemoteMulticastGroupService/List',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupRequest,
    responseType: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupResponse,
    requestSerialize: serialize_api_ListRemoteMulticastGroupRequest,
    requestDeserialize: deserialize_api_ListRemoteMulticastGroupRequest,
    responseSerialize: serialize_api_ListRemoteMulticastGroupResponse,
    responseDeserialize: deserialize_api_ListRemoteMulticastGroupResponse,
  },
  // AddDevice adds the given devices to the remote multicast-group.
  addDevice: {
    path: '/api.RemoteMulticastGroupService/AddDevice',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.AddDeviceToRemoteMulticastGroupRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_api_AddDeviceToRemoteMulticastGroupRequest,
    requestDeserialize: deserialize_api_AddDeviceToRemoteMulticastGroupRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // ResetDevice Restart the remote multicast process of given device.
  resetDevice: {
    path: '/api.RemoteMulticastGroupService/ResetDevice',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.ResetRemoteMulticastDeviceRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_api_ResetRemoteMulticastDeviceRequest,
    requestDeserialize: deserialize_api_ResetRemoteMulticastDeviceRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // RemoveDevice removes the given device from the remote multicast-group.
  removeDevice: {
    path: '/api.RemoteMulticastGroupService/RemoveDevice',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.RemoveDeviceFromRemoteMulticastGroupRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_api_RemoveDeviceFromRemoteMulticastGroupRequest,
    requestDeserialize: deserialize_api_RemoveDeviceFromRemoteMulticastGroupRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // ListDevicesForRemoteMulticast Lists the available pending devices for joining to
  // remote multicast-group for given application id.
  listDevicesForRemoteMulticast: {
    path: '/api.RemoteMulticastGroupService/ListDevicesForRemoteMulticast',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest,
    responseType: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceResponse,
    requestSerialize: serialize_api_ListRemoteMulticastDeviceRequest,
    requestDeserialize: deserialize_api_ListRemoteMulticastDeviceRequest,
    responseSerialize: serialize_api_ListRemoteMulticastDeviceResponse,
    responseDeserialize: deserialize_api_ListRemoteMulticastDeviceResponse,
  },
  // GetDevicesList Lists the available devices in remote multicast-groups.
  getDevicesList: {
    path: '/api.RemoteMulticastGroupService/GetDevicesList',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDeviceRequest,
    responseType: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastDevicesResponse,
    requestSerialize: serialize_api_ListRemoteMulticastDeviceRequest,
    requestDeserialize: deserialize_api_ListRemoteMulticastDeviceRequest,
    responseSerialize: serialize_api_ListRemoteMulticastDevicesResponse,
    responseDeserialize: deserialize_api_ListRemoteMulticastDevicesResponse,
  },
  // GetDeploymentDevice returns the deployment device.
  getDeploymentDevice: {
    path: '/api.RemoteMulticastGroupService/GetDeploymentDevice',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceRequest,
    responseType: as_external_api_remoteMulticastGroup_pb.GetRemoteMulticastDeploymentDeviceResponse,
    requestSerialize: serialize_api_GetRemoteMulticastDeploymentDeviceRequest,
    requestDeserialize: deserialize_api_GetRemoteMulticastDeploymentDeviceRequest,
    responseSerialize: serialize_api_GetRemoteMulticastDeploymentDeviceResponse,
    responseDeserialize: deserialize_api_GetRemoteMulticastDeploymentDeviceResponse,
  },
  // Enqueue adds the given item to the remote multicast-queue.
  enqueue: {
    path: '/api.RemoteMulticastGroupService/Enqueue',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemRequest,
    responseType: as_external_api_remoteMulticastGroup_pb.EnqueueRemoteMulticastQueueItemResponse,
    requestSerialize: serialize_api_EnqueueRemoteMulticastQueueItemRequest,
    requestDeserialize: deserialize_api_EnqueueRemoteMulticastQueueItemRequest,
    responseSerialize: serialize_api_EnqueueRemoteMulticastQueueItemResponse,
    responseDeserialize: deserialize_api_EnqueueRemoteMulticastQueueItemResponse,
  },
  // FlushQueue flushes the remote multicast-group queue.
  flushQueue: {
    path: '/api.RemoteMulticastGroupService/FlushQueue',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.FlushRemoteMulticastGroupQueueItemsRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_api_FlushRemoteMulticastGroupQueueItemsRequest,
    requestDeserialize: deserialize_api_FlushRemoteMulticastGroupQueueItemsRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // ListQueue lists the items in the remote multicast-group queue.
  listQueue: {
    path: '/api.RemoteMulticastGroupService/ListQueue',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsRequest,
    responseType: as_external_api_remoteMulticastGroup_pb.ListRemoteMulticastGroupQueueItemsResponse,
    requestSerialize: serialize_api_ListRemoteMulticastGroupQueueItemsRequest,
    requestDeserialize: deserialize_api_ListRemoteMulticastGroupQueueItemsRequest,
    responseSerialize: serialize_api_ListRemoteMulticastGroupQueueItemsResponse,
    responseDeserialize: deserialize_api_ListRemoteMulticastGroupQueueItemsResponse,
  },
};

exports.RemoteMulticastGroupServiceClient = grpc.makeGenericClientConstructor(RemoteMulticastGroupServiceService);
