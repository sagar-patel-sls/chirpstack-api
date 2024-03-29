// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var as_external_api_gateway_pb = require('../../../as/external/api/gateway_pb.js');
var google_api_annotations_pb = require('../../../google/api/annotations_pb.js');
var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');
var google_protobuf_empty_pb = require('google-protobuf/google/protobuf/empty_pb.js');
var common_common_pb = require('../../../common/common_pb.js');
var as_external_api_frameLog_pb = require('../../../as/external/api/frameLog_pb.js');

function serialize_api_CreateGatewayRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.CreateGatewayRequest)) {
    throw new Error('Expected argument of type api.CreateGatewayRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_CreateGatewayRequest(buffer_arg) {
  return as_external_api_gateway_pb.CreateGatewayRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_DeleteGatewayRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.DeleteGatewayRequest)) {
    throw new Error('Expected argument of type api.DeleteGatewayRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_DeleteGatewayRequest(buffer_arg) {
  return as_external_api_gateway_pb.DeleteGatewayRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GenerateGatewayClientCertificateRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.GenerateGatewayClientCertificateRequest)) {
    throw new Error('Expected argument of type api.GenerateGatewayClientCertificateRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GenerateGatewayClientCertificateRequest(buffer_arg) {
  return as_external_api_gateway_pb.GenerateGatewayClientCertificateRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GenerateGatewayClientCertificateResponse(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.GenerateGatewayClientCertificateResponse)) {
    throw new Error('Expected argument of type api.GenerateGatewayClientCertificateResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GenerateGatewayClientCertificateResponse(buffer_arg) {
  return as_external_api_gateway_pb.GenerateGatewayClientCertificateResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetGatewayRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.GetGatewayRequest)) {
    throw new Error('Expected argument of type api.GetGatewayRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetGatewayRequest(buffer_arg) {
  return as_external_api_gateway_pb.GetGatewayRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetGatewayResponse(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.GetGatewayResponse)) {
    throw new Error('Expected argument of type api.GetGatewayResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetGatewayResponse(buffer_arg) {
  return as_external_api_gateway_pb.GetGatewayResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetGatewayStatsRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.GetGatewayStatsRequest)) {
    throw new Error('Expected argument of type api.GetGatewayStatsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetGatewayStatsRequest(buffer_arg) {
  return as_external_api_gateway_pb.GetGatewayStatsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetGatewayStatsResponse(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.GetGatewayStatsResponse)) {
    throw new Error('Expected argument of type api.GetGatewayStatsResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetGatewayStatsResponse(buffer_arg) {
  return as_external_api_gateway_pb.GetGatewayStatsResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetGatewayUptimeRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.GetGatewayUptimeRequest)) {
    throw new Error('Expected argument of type api.GetGatewayUptimeRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetGatewayUptimeRequest(buffer_arg) {
  return as_external_api_gateway_pb.GetGatewayUptimeRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetGatewayUptimeResponse(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.GetGatewayUptimeResponse)) {
    throw new Error('Expected argument of type api.GetGatewayUptimeResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetGatewayUptimeResponse(buffer_arg) {
  return as_external_api_gateway_pb.GetGatewayUptimeResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetLastPingRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.GetLastPingRequest)) {
    throw new Error('Expected argument of type api.GetLastPingRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetLastPingRequest(buffer_arg) {
  return as_external_api_gateway_pb.GetLastPingRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetLastPingResponse(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.GetLastPingResponse)) {
    throw new Error('Expected argument of type api.GetLastPingResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetLastPingResponse(buffer_arg) {
  return as_external_api_gateway_pb.GetLastPingResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ListGatewayRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.ListGatewayRequest)) {
    throw new Error('Expected argument of type api.ListGatewayRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ListGatewayRequest(buffer_arg) {
  return as_external_api_gateway_pb.ListGatewayRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ListGatewayResponse(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.ListGatewayResponse)) {
    throw new Error('Expected argument of type api.ListGatewayResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ListGatewayResponse(buffer_arg) {
  return as_external_api_gateway_pb.ListGatewayResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_StreamGatewayEventLogsRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.StreamGatewayEventLogsRequest)) {
    throw new Error('Expected argument of type api.StreamGatewayEventLogsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_StreamGatewayEventLogsRequest(buffer_arg) {
  return as_external_api_gateway_pb.StreamGatewayEventLogsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_StreamGatewayEventLogsResponse(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.StreamGatewayEventLogsResponse)) {
    throw new Error('Expected argument of type api.StreamGatewayEventLogsResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_StreamGatewayEventLogsResponse(buffer_arg) {
  return as_external_api_gateway_pb.StreamGatewayEventLogsResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_StreamGatewayFrameLogsRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.StreamGatewayFrameLogsRequest)) {
    throw new Error('Expected argument of type api.StreamGatewayFrameLogsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_StreamGatewayFrameLogsRequest(buffer_arg) {
  return as_external_api_gateway_pb.StreamGatewayFrameLogsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_StreamGatewayFrameLogsResponse(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.StreamGatewayFrameLogsResponse)) {
    throw new Error('Expected argument of type api.StreamGatewayFrameLogsResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_StreamGatewayFrameLogsResponse(buffer_arg) {
  return as_external_api_gateway_pb.StreamGatewayFrameLogsResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_StreamGlobalGatewayFrameLogsRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.StreamGlobalGatewayFrameLogsRequest)) {
    throw new Error('Expected argument of type api.StreamGlobalGatewayFrameLogsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_StreamGlobalGatewayFrameLogsRequest(buffer_arg) {
  return as_external_api_gateway_pb.StreamGlobalGatewayFrameLogsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_StreamGlobalGatewayFrameLogsResponse(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.StreamGlobalGatewayFrameLogsResponse)) {
    throw new Error('Expected argument of type api.StreamGlobalGatewayFrameLogsResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_StreamGlobalGatewayFrameLogsResponse(buffer_arg) {
  return as_external_api_gateway_pb.StreamGlobalGatewayFrameLogsResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_UpdateGatewayRequest(arg) {
  if (!(arg instanceof as_external_api_gateway_pb.UpdateGatewayRequest)) {
    throw new Error('Expected argument of type api.UpdateGatewayRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_UpdateGatewayRequest(buffer_arg) {
  return as_external_api_gateway_pb.UpdateGatewayRequest.deserializeBinary(new Uint8Array(buffer_arg));
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


// GatewayService is the service managing the gateways.
var GatewayServiceService = exports.GatewayServiceService = {
  // Create creates the given gateway.
create: {
    path: '/api.GatewayService/Create',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_gateway_pb.CreateGatewayRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_api_CreateGatewayRequest,
    requestDeserialize: deserialize_api_CreateGatewayRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // Get returns the gateway for the requested mac address.
get: {
    path: '/api.GatewayService/Get',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_gateway_pb.GetGatewayRequest,
    responseType: as_external_api_gateway_pb.GetGatewayResponse,
    requestSerialize: serialize_api_GetGatewayRequest,
    requestDeserialize: deserialize_api_GetGatewayRequest,
    responseSerialize: serialize_api_GetGatewayResponse,
    responseDeserialize: deserialize_api_GetGatewayResponse,
  },
  // Update updates the gateway matching the given mac address.
update: {
    path: '/api.GatewayService/Update',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_gateway_pb.UpdateGatewayRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_api_UpdateGatewayRequest,
    requestDeserialize: deserialize_api_UpdateGatewayRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // Delete deletes the gateway matching the given mac address.
delete: {
    path: '/api.GatewayService/Delete',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_gateway_pb.DeleteGatewayRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_api_DeleteGatewayRequest,
    requestDeserialize: deserialize_api_DeleteGatewayRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // List lists the gateways.
list: {
    path: '/api.GatewayService/List',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_gateway_pb.ListGatewayRequest,
    responseType: as_external_api_gateway_pb.ListGatewayResponse,
    requestSerialize: serialize_api_ListGatewayRequest,
    requestDeserialize: deserialize_api_ListGatewayRequest,
    responseSerialize: serialize_api_ListGatewayResponse,
    responseDeserialize: deserialize_api_ListGatewayResponse,
  },
  // GetStats lists the gateway stats given the query parameters.
getStats: {
    path: '/api.GatewayService/GetStats',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_gateway_pb.GetGatewayStatsRequest,
    responseType: as_external_api_gateway_pb.GetGatewayStatsResponse,
    requestSerialize: serialize_api_GetGatewayStatsRequest,
    requestDeserialize: deserialize_api_GetGatewayStatsRequest,
    responseSerialize: serialize_api_GetGatewayStatsResponse,
    responseDeserialize: deserialize_api_GetGatewayStatsResponse,
  },
  // GetLastPing returns the last emitted ping and gateways receiving this ping.
getLastPing: {
    path: '/api.GatewayService/GetLastPing',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_gateway_pb.GetLastPingRequest,
    responseType: as_external_api_gateway_pb.GetLastPingResponse,
    requestSerialize: serialize_api_GetLastPingRequest,
    requestDeserialize: deserialize_api_GetLastPingRequest,
    responseSerialize: serialize_api_GetLastPingResponse,
    responseDeserialize: deserialize_api_GetLastPingResponse,
  },
  // GenerateGatewayClientCertificate returns TLS certificate gateway authentication / authorization.
// This endpoint can ony be used when ChirpStack Network Server is configured with a gateway
// CA certificate and key, which is used for signing the TLS certificate. The returned TLS
// certificate will have the Gateway ID as Common Name.
generateGatewayClientCertificate: {
    path: '/api.GatewayService/GenerateGatewayClientCertificate',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_gateway_pb.GenerateGatewayClientCertificateRequest,
    responseType: as_external_api_gateway_pb.GenerateGatewayClientCertificateResponse,
    requestSerialize: serialize_api_GenerateGatewayClientCertificateRequest,
    requestDeserialize: deserialize_api_GenerateGatewayClientCertificateRequest,
    responseSerialize: serialize_api_GenerateGatewayClientCertificateResponse,
    responseDeserialize: deserialize_api_GenerateGatewayClientCertificateResponse,
  },
  // StreamFrameLogs streams the uplink and downlink frame-logs for the given gateway ID.
// Notes:
//   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.
//   * This endpoint does not work from a web-browser.
streamFrameLogs: {
    path: '/api.GatewayService/StreamFrameLogs',
    requestStream: false,
    responseStream: true,
    requestType: as_external_api_gateway_pb.StreamGatewayFrameLogsRequest,
    responseType: as_external_api_gateway_pb.StreamGatewayFrameLogsResponse,
    requestSerialize: serialize_api_StreamGatewayFrameLogsRequest,
    requestDeserialize: deserialize_api_StreamGatewayFrameLogsRequest,
    responseSerialize: serialize_api_StreamGatewayFrameLogsResponse,
    responseDeserialize: deserialize_api_StreamGatewayFrameLogsResponse,
  },
  // StreamGlobalFrameLogs streams the uplink and downlink frame-logs for all gateways of given organization.
// Notes:
//   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.
//   * This endpoint does not work from a web-browser.
streamGlobalFrameLogs: {
    path: '/api.GatewayService/StreamGlobalFrameLogs',
    requestStream: false,
    responseStream: true,
    requestType: as_external_api_gateway_pb.StreamGlobalGatewayFrameLogsRequest,
    responseType: as_external_api_gateway_pb.StreamGlobalGatewayFrameLogsResponse,
    requestSerialize: serialize_api_StreamGlobalGatewayFrameLogsRequest,
    requestDeserialize: deserialize_api_StreamGlobalGatewayFrameLogsRequest,
    responseSerialize: serialize_api_StreamGlobalGatewayFrameLogsResponse,
    responseDeserialize: deserialize_api_StreamGlobalGatewayFrameLogsResponse,
  },
  // StreamEventLogs streams the connection event logs given gateway ID.
// Notes:
//   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.
//   * This endpoint does not work from a web-browser.
streamEventLogs: {
    path: '/api.GatewayService/StreamEventLogs',
    requestStream: false,
    responseStream: true,
    requestType: as_external_api_gateway_pb.StreamGatewayEventLogsRequest,
    responseType: as_external_api_gateway_pb.StreamGatewayEventLogsResponse,
    requestSerialize: serialize_api_StreamGatewayEventLogsRequest,
    requestDeserialize: deserialize_api_StreamGatewayEventLogsRequest,
    responseSerialize: serialize_api_StreamGatewayEventLogsResponse,
    responseDeserialize: deserialize_api_StreamGatewayEventLogsResponse,
  },
  // GetUptime lists the gateway uptime stats given the query parameters.
getUptime: {
    path: '/api.GatewayService/GetUptime',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_gateway_pb.GetGatewayUptimeRequest,
    responseType: as_external_api_gateway_pb.GetGatewayUptimeResponse,
    requestSerialize: serialize_api_GetGatewayUptimeRequest,
    requestDeserialize: deserialize_api_GetGatewayUptimeRequest,
    responseSerialize: serialize_api_GetGatewayUptimeResponse,
    responseDeserialize: deserialize_api_GetGatewayUptimeResponse,
  },
};

exports.GatewayServiceClient = grpc.makeGenericClientConstructor(GatewayServiceService);
