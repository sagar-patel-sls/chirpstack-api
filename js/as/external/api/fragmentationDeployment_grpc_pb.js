// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var as_external_api_fragmentationDeployment_pb = require('../../../as/external/api/fragmentationDeployment_pb.js');
var google_api_annotations_pb = require('../../../google/api/annotations_pb.js');
var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');
var google_protobuf_duration_pb = require('google-protobuf/google/protobuf/duration_pb.js');
var google_protobuf_empty_pb = require('google-protobuf/google/protobuf/empty_pb.js');
var as_external_api_multicastGroup_pb = require('../../../as/external/api/multicastGroup_pb.js');

function serialize_api_DeleteFragmentationDeploymentRequest(arg) {
  if (!(arg instanceof as_external_api_fragmentationDeployment_pb.DeleteFragmentationDeploymentRequest)) {
    throw new Error('Expected argument of type api.DeleteFragmentationDeploymentRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_DeleteFragmentationDeploymentRequest(buffer_arg) {
  return as_external_api_fragmentationDeployment_pb.DeleteFragmentationDeploymentRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_FragmentationDeploymentRequest(arg) {
  if (!(arg instanceof as_external_api_fragmentationDeployment_pb.FragmentationDeploymentRequest)) {
    throw new Error('Expected argument of type api.FragmentationDeploymentRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_FragmentationDeploymentRequest(buffer_arg) {
  return as_external_api_fragmentationDeployment_pb.FragmentationDeploymentRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_FragmentationDeploymentResponse(arg) {
  if (!(arg instanceof as_external_api_fragmentationDeployment_pb.FragmentationDeploymentResponse)) {
    throw new Error('Expected argument of type api.FragmentationDeploymentResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_FragmentationDeploymentResponse(buffer_arg) {
  return as_external_api_fragmentationDeployment_pb.FragmentationDeploymentResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetFragmentationDeploymentRequest(arg) {
  if (!(arg instanceof as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentRequest)) {
    throw new Error('Expected argument of type api.GetFragmentationDeploymentRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetFragmentationDeploymentRequest(buffer_arg) {
  return as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_GetFragmentationDeploymentResponse(arg) {
  if (!(arg instanceof as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentResponse)) {
    throw new Error('Expected argument of type api.GetFragmentationDeploymentResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_GetFragmentationDeploymentResponse(buffer_arg) {
  return as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ListFragmentationDeploymentRequest(arg) {
  if (!(arg instanceof as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentRequest)) {
    throw new Error('Expected argument of type api.ListFragmentationDeploymentRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ListFragmentationDeploymentRequest(buffer_arg) {
  return as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_ListFragmentationDeploymentResponse(arg) {
  if (!(arg instanceof as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentResponse)) {
    throw new Error('Expected argument of type api.ListFragmentationDeploymentResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_ListFragmentationDeploymentResponse(buffer_arg) {
  return as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_UpdateFragmentationDeploymentRequest(arg) {
  if (!(arg instanceof as_external_api_fragmentationDeployment_pb.UpdateFragmentationDeploymentRequest)) {
    throw new Error('Expected argument of type api.UpdateFragmentationDeploymentRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_UpdateFragmentationDeploymentRequest(buffer_arg) {
  return as_external_api_fragmentationDeployment_pb.UpdateFragmentationDeploymentRequest.deserializeBinary(new Uint8Array(buffer_arg));
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


// FragmentationDeploymentService is the service managing fragmentation.
var FragmentationDeploymentServiceService = exports.FragmentationDeploymentServiceService = {
  // Create creates the given fragmentation deployment for given DevEUI.
create: {
    path: '/api.FragmentationDeploymentService/Create',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_fragmentationDeployment_pb.FragmentationDeploymentRequest,
    responseType: as_external_api_fragmentationDeployment_pb.FragmentationDeploymentResponse,
    requestSerialize: serialize_api_FragmentationDeploymentRequest,
    requestDeserialize: deserialize_api_FragmentationDeploymentRequest,
    responseSerialize: serialize_api_FragmentationDeploymentResponse,
    responseDeserialize: deserialize_api_FragmentationDeploymentResponse,
  },
  // Get returns a fragmentation deployment given an ID.
get: {
    path: '/api.FragmentationDeploymentService/Get',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentRequest,
    responseType: as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentResponse,
    requestSerialize: serialize_api_GetFragmentationDeploymentRequest,
    requestDeserialize: deserialize_api_GetFragmentationDeploymentRequest,
    responseSerialize: serialize_api_GetFragmentationDeploymentResponse,
    responseDeserialize: deserialize_api_GetFragmentationDeploymentResponse,
  },
  // Update updates the given fragmentation deployment.
update: {
    path: '/api.FragmentationDeploymentService/Update',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_fragmentationDeployment_pb.UpdateFragmentationDeploymentRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_api_UpdateFragmentationDeploymentRequest,
    requestDeserialize: deserialize_api_UpdateFragmentationDeploymentRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // Delete deletes a fragmentation deployment given an ID.
delete: {
    path: '/api.FragmentationDeploymentService/Delete',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_fragmentationDeployment_pb.DeleteFragmentationDeploymentRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_api_DeleteFragmentationDeploymentRequest,
    requestDeserialize: deserialize_api_DeleteFragmentationDeploymentRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // List lists the available fragmentation deployment.
list: {
    path: '/api.FragmentationDeploymentService/List',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentRequest,
    responseType: as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentResponse,
    requestSerialize: serialize_api_ListFragmentationDeploymentRequest,
    requestDeserialize: deserialize_api_ListFragmentationDeploymentRequest,
    responseSerialize: serialize_api_ListFragmentationDeploymentResponse,
    responseDeserialize: deserialize_api_ListFragmentationDeploymentResponse,
  },
};

exports.FragmentationDeploymentServiceClient = grpc.makeGenericClientConstructor(FragmentationDeploymentServiceService);
