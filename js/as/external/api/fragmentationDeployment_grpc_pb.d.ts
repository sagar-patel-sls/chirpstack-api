// GENERATED CODE -- DO NOT EDIT!

// package: api
// file: as/external/api/fragmentationDeployment.proto

import * as as_external_api_fragmentationDeployment_pb from "../../../as/external/api/fragmentationDeployment_pb";
import * as google_protobuf_empty_pb from "google-protobuf/google/protobuf/empty_pb";
import * as grpc from "grpc";

interface IFragmentationDeploymentServiceService extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
  create: grpc.MethodDefinition<as_external_api_fragmentationDeployment_pb.FragmentationDeploymentRequest, as_external_api_fragmentationDeployment_pb.FragmentationDeploymentResponse>;
  get: grpc.MethodDefinition<as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentRequest, as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentResponse>;
  update: grpc.MethodDefinition<as_external_api_fragmentationDeployment_pb.UpdateFragmentationDeploymentRequest, google_protobuf_empty_pb.Empty>;
  delete: grpc.MethodDefinition<as_external_api_fragmentationDeployment_pb.DeleteFragmentationDeploymentRequest, google_protobuf_empty_pb.Empty>;
  list: grpc.MethodDefinition<as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentRequest, as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentResponse>;
}

export const FragmentationDeploymentServiceService: IFragmentationDeploymentServiceService;

export interface IFragmentationDeploymentServiceServer extends grpc.UntypedServiceImplementation {
  create: grpc.handleUnaryCall<as_external_api_fragmentationDeployment_pb.FragmentationDeploymentRequest, as_external_api_fragmentationDeployment_pb.FragmentationDeploymentResponse>;
  get: grpc.handleUnaryCall<as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentRequest, as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentResponse>;
  update: grpc.handleUnaryCall<as_external_api_fragmentationDeployment_pb.UpdateFragmentationDeploymentRequest, google_protobuf_empty_pb.Empty>;
  delete: grpc.handleUnaryCall<as_external_api_fragmentationDeployment_pb.DeleteFragmentationDeploymentRequest, google_protobuf_empty_pb.Empty>;
  list: grpc.handleUnaryCall<as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentRequest, as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentResponse>;
}

export class FragmentationDeploymentServiceClient extends grpc.Client {
  constructor(address: string, credentials: grpc.ChannelCredentials, options?: object);
  create(argument: as_external_api_fragmentationDeployment_pb.FragmentationDeploymentRequest, callback: grpc.requestCallback<as_external_api_fragmentationDeployment_pb.FragmentationDeploymentResponse>): grpc.ClientUnaryCall;
  create(argument: as_external_api_fragmentationDeployment_pb.FragmentationDeploymentRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_fragmentationDeployment_pb.FragmentationDeploymentResponse>): grpc.ClientUnaryCall;
  create(argument: as_external_api_fragmentationDeployment_pb.FragmentationDeploymentRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_fragmentationDeployment_pb.FragmentationDeploymentResponse>): grpc.ClientUnaryCall;
  get(argument: as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentRequest, callback: grpc.requestCallback<as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentResponse>): grpc.ClientUnaryCall;
  get(argument: as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentResponse>): grpc.ClientUnaryCall;
  get(argument: as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_fragmentationDeployment_pb.GetFragmentationDeploymentResponse>): grpc.ClientUnaryCall;
  update(argument: as_external_api_fragmentationDeployment_pb.UpdateFragmentationDeploymentRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  update(argument: as_external_api_fragmentationDeployment_pb.UpdateFragmentationDeploymentRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  update(argument: as_external_api_fragmentationDeployment_pb.UpdateFragmentationDeploymentRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  delete(argument: as_external_api_fragmentationDeployment_pb.DeleteFragmentationDeploymentRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  delete(argument: as_external_api_fragmentationDeployment_pb.DeleteFragmentationDeploymentRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  delete(argument: as_external_api_fragmentationDeployment_pb.DeleteFragmentationDeploymentRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  list(argument: as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentRequest, callback: grpc.requestCallback<as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentResponse>): grpc.ClientUnaryCall;
  list(argument: as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentResponse>): grpc.ClientUnaryCall;
  list(argument: as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_fragmentationDeployment_pb.ListFragmentationDeploymentResponse>): grpc.ClientUnaryCall;
}
