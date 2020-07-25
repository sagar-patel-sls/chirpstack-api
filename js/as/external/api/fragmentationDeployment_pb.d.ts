// package: api
// file: as/external/api/fragmentationDeployment.proto

import * as jspb from "google-protobuf";
import * as google_api_annotations_pb from "../../../google/api/annotations_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
import * as google_protobuf_duration_pb from "google-protobuf/google/protobuf/duration_pb";
import * as google_protobuf_empty_pb from "google-protobuf/google/protobuf/empty_pb";

export class FragmentationDeployment extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  getName(): string;
  setName(value: string): void;

  getDevEui(): string;
  setDevEui(value: string): void;

  getPayload(): Uint8Array | string;
  getPayload_asU8(): Uint8Array;
  getPayload_asB64(): string;
  setPayload(value: Uint8Array | string): void;

  getGroupType(): FragmentationDeploymentGroupTypeMap[keyof FragmentationDeploymentGroupTypeMap];
  setGroupType(value: FragmentationDeploymentGroupTypeMap[keyof FragmentationDeploymentGroupTypeMap]): void;

  getPingSlotPeriod(): number;
  setPingSlotPeriod(value: number): void;

  getRedundancy(): number;
  setRedundancy(value: number): void;

  hasUnicastTimeout(): boolean;
  clearUnicastTimeout(): void;
  getUnicastTimeout(): google_protobuf_duration_pb.Duration | undefined;
  setUnicastTimeout(value?: google_protobuf_duration_pb.Duration): void;

  getState(): string;
  setState(value: string): void;

  hasNextStepAfter(): boolean;
  clearNextStepAfter(): void;
  getNextStepAfter(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setNextStepAfter(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FragmentationDeployment.AsObject;
  static toObject(includeInstance: boolean, msg: FragmentationDeployment): FragmentationDeployment.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FragmentationDeployment, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FragmentationDeployment;
  static deserializeBinaryFromReader(message: FragmentationDeployment, reader: jspb.BinaryReader): FragmentationDeployment;
}

export namespace FragmentationDeployment {
  export type AsObject = {
    id: string,
    name: string,
    devEui: string,
    payload: Uint8Array | string,
    groupType: FragmentationDeploymentGroupTypeMap[keyof FragmentationDeploymentGroupTypeMap],
    pingSlotPeriod: number,
    redundancy: number,
    unicastTimeout?: google_protobuf_duration_pb.Duration.AsObject,
    state: string,
    nextStepAfter?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetFragmentationDeployment extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  getName(): string;
  setName(value: string): void;

  getDevEui(): string;
  setDevEui(value: string): void;

  getPayload(): Uint8Array | string;
  getPayload_asU8(): Uint8Array;
  getPayload_asB64(): string;
  setPayload(value: Uint8Array | string): void;

  getPayloadSize(): number;
  setPayloadSize(value: number): void;

  getGroupType(): FragmentationDeploymentGroupTypeMap[keyof FragmentationDeploymentGroupTypeMap];
  setGroupType(value: FragmentationDeploymentGroupTypeMap[keyof FragmentationDeploymentGroupTypeMap]): void;

  getPingSlotPeriod(): number;
  setPingSlotPeriod(value: number): void;

  getFragSize(): number;
  setFragSize(value: number): void;

  getRedundancy(): number;
  setRedundancy(value: number): void;

  hasUnicastTimeout(): boolean;
  clearUnicastTimeout(): void;
  getUnicastTimeout(): google_protobuf_duration_pb.Duration | undefined;
  setUnicastTimeout(value?: google_protobuf_duration_pb.Duration): void;

  getState(): string;
  setState(value: string): void;

  getDeviceState(): string;
  setDeviceState(value: string): void;

  getErrorMessage(): string;
  setErrorMessage(value: string): void;

  hasNextStepAfter(): boolean;
  clearNextStepAfter(): void;
  getNextStepAfter(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setNextStepAfter(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFragmentationDeployment.AsObject;
  static toObject(includeInstance: boolean, msg: GetFragmentationDeployment): GetFragmentationDeployment.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFragmentationDeployment, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFragmentationDeployment;
  static deserializeBinaryFromReader(message: GetFragmentationDeployment, reader: jspb.BinaryReader): GetFragmentationDeployment;
}

export namespace GetFragmentationDeployment {
  export type AsObject = {
    id: string,
    name: string,
    devEui: string,
    payload: Uint8Array | string,
    payloadSize: number,
    groupType: FragmentationDeploymentGroupTypeMap[keyof FragmentationDeploymentGroupTypeMap],
    pingSlotPeriod: number,
    fragSize: number,
    redundancy: number,
    unicastTimeout?: google_protobuf_duration_pb.Duration.AsObject,
    state: string,
    deviceState: string,
    errorMessage: string,
    nextStepAfter?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class FragmentationDeploymentRequest extends jspb.Message {
  hasFragmentationdeployment(): boolean;
  clearFragmentationdeployment(): void;
  getFragmentationdeployment(): FragmentationDeployment | undefined;
  setFragmentationdeployment(value?: FragmentationDeployment): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FragmentationDeploymentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: FragmentationDeploymentRequest): FragmentationDeploymentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FragmentationDeploymentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FragmentationDeploymentRequest;
  static deserializeBinaryFromReader(message: FragmentationDeploymentRequest, reader: jspb.BinaryReader): FragmentationDeploymentRequest;
}

export namespace FragmentationDeploymentRequest {
  export type AsObject = {
    fragmentationdeployment?: FragmentationDeployment.AsObject,
  }
}

export class FragmentationDeploymentResponse extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FragmentationDeploymentResponse.AsObject;
  static toObject(includeInstance: boolean, msg: FragmentationDeploymentResponse): FragmentationDeploymentResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FragmentationDeploymentResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FragmentationDeploymentResponse;
  static deserializeBinaryFromReader(message: FragmentationDeploymentResponse, reader: jspb.BinaryReader): FragmentationDeploymentResponse;
}

export namespace FragmentationDeploymentResponse {
  export type AsObject = {
    id: string,
  }
}

export class GetFragmentationDeploymentRequest extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFragmentationDeploymentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFragmentationDeploymentRequest): GetFragmentationDeploymentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFragmentationDeploymentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFragmentationDeploymentRequest;
  static deserializeBinaryFromReader(message: GetFragmentationDeploymentRequest, reader: jspb.BinaryReader): GetFragmentationDeploymentRequest;
}

export namespace GetFragmentationDeploymentRequest {
  export type AsObject = {
    id: string,
  }
}

export class GetFragmentationDeploymentResponse extends jspb.Message {
  hasFragmentationdeployment(): boolean;
  clearFragmentationdeployment(): void;
  getFragmentationdeployment(): GetFragmentationDeployment | undefined;
  setFragmentationdeployment(value?: GetFragmentationDeployment): void;

  hasCreatedAt(): boolean;
  clearCreatedAt(): void;
  getCreatedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setCreatedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasUpdatedAt(): boolean;
  clearUpdatedAt(): void;
  getUpdatedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setUpdatedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFragmentationDeploymentResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetFragmentationDeploymentResponse): GetFragmentationDeploymentResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetFragmentationDeploymentResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFragmentationDeploymentResponse;
  static deserializeBinaryFromReader(message: GetFragmentationDeploymentResponse, reader: jspb.BinaryReader): GetFragmentationDeploymentResponse;
}

export namespace GetFragmentationDeploymentResponse {
  export type AsObject = {
    fragmentationdeployment?: GetFragmentationDeployment.AsObject,
    createdAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    updatedAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class UpdateFragmentationDeploymentRequest extends jspb.Message {
  hasFragmentationDeployment(): boolean;
  clearFragmentationDeployment(): void;
  getFragmentationDeployment(): FragmentationDeployment | undefined;
  setFragmentationDeployment(value?: FragmentationDeployment): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateFragmentationDeploymentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateFragmentationDeploymentRequest): UpdateFragmentationDeploymentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateFragmentationDeploymentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateFragmentationDeploymentRequest;
  static deserializeBinaryFromReader(message: UpdateFragmentationDeploymentRequest, reader: jspb.BinaryReader): UpdateFragmentationDeploymentRequest;
}

export namespace UpdateFragmentationDeploymentRequest {
  export type AsObject = {
    fragmentationDeployment?: FragmentationDeployment.AsObject,
  }
}

export class DeleteFragmentationDeploymentRequest extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteFragmentationDeploymentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteFragmentationDeploymentRequest): DeleteFragmentationDeploymentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteFragmentationDeploymentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteFragmentationDeploymentRequest;
  static deserializeBinaryFromReader(message: DeleteFragmentationDeploymentRequest, reader: jspb.BinaryReader): DeleteFragmentationDeploymentRequest;
}

export namespace DeleteFragmentationDeploymentRequest {
  export type AsObject = {
    id: string,
  }
}

export class ListFragmentationDeploymentRequest extends jspb.Message {
  getLimit(): number;
  setLimit(value: number): void;

  getOffset(): number;
  setOffset(value: number): void;

  getSearch(): string;
  setSearch(value: string): void;

  getDevEui(): string;
  setDevEui(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListFragmentationDeploymentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ListFragmentationDeploymentRequest): ListFragmentationDeploymentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ListFragmentationDeploymentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListFragmentationDeploymentRequest;
  static deserializeBinaryFromReader(message: ListFragmentationDeploymentRequest, reader: jspb.BinaryReader): ListFragmentationDeploymentRequest;
}

export namespace ListFragmentationDeploymentRequest {
  export type AsObject = {
    limit: number,
    offset: number,
    search: string,
    devEui: string,
  }
}

export class ListFragmentationDeploymentResponse extends jspb.Message {
  getTotalCount(): number;
  setTotalCount(value: number): void;

  clearResultList(): void;
  getResultList(): Array<GetFragmentationDeployment>;
  setResultList(value: Array<GetFragmentationDeployment>): void;
  addResult(value?: GetFragmentationDeployment, index?: number): GetFragmentationDeployment;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListFragmentationDeploymentResponse.AsObject;
  static toObject(includeInstance: boolean, msg: ListFragmentationDeploymentResponse): ListFragmentationDeploymentResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ListFragmentationDeploymentResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListFragmentationDeploymentResponse;
  static deserializeBinaryFromReader(message: ListFragmentationDeploymentResponse, reader: jspb.BinaryReader): ListFragmentationDeploymentResponse;
}

export namespace ListFragmentationDeploymentResponse {
  export type AsObject = {
    totalCount: number,
    resultList: Array<GetFragmentationDeployment.AsObject>,
  }
}

export interface FragmentationDeploymentGroupTypeMap {
  CLASS_C: 0;
  CLASS_B: 1;
}

export const FragmentationDeploymentGroupType: FragmentationDeploymentGroupTypeMap;

