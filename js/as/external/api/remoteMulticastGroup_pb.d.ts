// package: api
// file: as/external/api/remoteMulticastGroup.proto

import * as jspb from "google-protobuf";
import * as google_api_annotations_pb from "../../../google/api/annotations_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
import * as google_protobuf_duration_pb from "google-protobuf/google/protobuf/duration_pb";
import * as google_protobuf_empty_pb from "google-protobuf/google/protobuf/empty_pb";
import * as as_external_api_device_pb from "../../../as/external/api/device_pb";
import * as as_external_api_multicastGroup_pb from "../../../as/external/api/multicastGroup_pb";
import * as as_external_api_fuotaDeployment_pb from "../../../as/external/api/fuotaDeployment_pb";

export class RemoteMulticastGroup extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  getName(): string;
  setName(value: string): void;

  getServiceProfileId(): string;
  setServiceProfileId(value: string): void;

  getGroupType(): as_external_api_multicastGroup_pb.MulticastGroupTypeMap[keyof as_external_api_multicastGroup_pb.MulticastGroupTypeMap];
  setGroupType(value: as_external_api_multicastGroup_pb.MulticastGroupTypeMap[keyof as_external_api_multicastGroup_pb.MulticastGroupTypeMap]): void;

  getDr(): number;
  setDr(value: number): void;

  getFrequency(): number;
  setFrequency(value: number): void;

  getPingSlotPeriod(): number;
  setPingSlotPeriod(value: number): void;

  getMcAddr(): string;
  setMcAddr(value: string): void;

  getMcNwkSKey(): string;
  setMcNwkSKey(value: string): void;

  getMcAppSKey(): string;
  setMcAppSKey(value: string): void;

  getFCnt(): number;
  setFCnt(value: number): void;

  getState(): string;
  setState(value: string): void;

  hasUnicastTimeout(): boolean;
  clearUnicastTimeout(): void;
  getUnicastTimeout(): google_protobuf_duration_pb.Duration | undefined;
  setUnicastTimeout(value?: google_protobuf_duration_pb.Duration): void;

  hasNextStepAfter(): boolean;
  clearNextStepAfter(): void;
  getNextStepAfter(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setNextStepAfter(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoteMulticastGroup.AsObject;
  static toObject(includeInstance: boolean, msg: RemoteMulticastGroup): RemoteMulticastGroup.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoteMulticastGroup, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoteMulticastGroup;
  static deserializeBinaryFromReader(message: RemoteMulticastGroup, reader: jspb.BinaryReader): RemoteMulticastGroup;
}

export namespace RemoteMulticastGroup {
  export type AsObject = {
    id: string,
    name: string,
    serviceProfileId: string,
    groupType: as_external_api_multicastGroup_pb.MulticastGroupTypeMap[keyof as_external_api_multicastGroup_pb.MulticastGroupTypeMap],
    dr: number,
    frequency: number,
    pingSlotPeriod: number,
    mcAddr: string,
    mcNwkSKey: string,
    mcAppSKey: string,
    fCnt: number,
    state: string,
    unicastTimeout?: google_protobuf_duration_pb.Duration.AsObject,
    nextStepAfter?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class RemoteMulticastDeploymentDevice extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  getDevEui(): string;
  setDevEui(value: string): void;

  getDeviceName(): string;
  setDeviceName(value: string): void;

  getApplicationId(): number;
  setApplicationId(value: number): void;

  getApplicationName(): string;
  setApplicationName(value: string): void;

  hasLastSeenAt(): boolean;
  clearLastSeenAt(): void;
  getLastSeenAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setLastSeenAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  getMcGroupId(): number;
  setMcGroupId(value: number): void;

  hasCreatedAt(): boolean;
  clearCreatedAt(): void;
  getCreatedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setCreatedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasUpdatedAt(): boolean;
  clearUpdatedAt(): void;
  getUpdatedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setUpdatedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  getState(): as_external_api_fuotaDeployment_pb.FUOTADeploymentDeviceStateMap[keyof as_external_api_fuotaDeployment_pb.FUOTADeploymentDeviceStateMap];
  setState(value: as_external_api_fuotaDeployment_pb.FUOTADeploymentDeviceStateMap[keyof as_external_api_fuotaDeployment_pb.FUOTADeploymentDeviceStateMap]): void;

  getErrorMessage(): string;
  setErrorMessage(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoteMulticastDeploymentDevice.AsObject;
  static toObject(includeInstance: boolean, msg: RemoteMulticastDeploymentDevice): RemoteMulticastDeploymentDevice.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoteMulticastDeploymentDevice, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoteMulticastDeploymentDevice;
  static deserializeBinaryFromReader(message: RemoteMulticastDeploymentDevice, reader: jspb.BinaryReader): RemoteMulticastDeploymentDevice;
}

export namespace RemoteMulticastDeploymentDevice {
  export type AsObject = {
    id: string,
    devEui: string,
    deviceName: string,
    applicationId: number,
    applicationName: string,
    lastSeenAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    mcGroupId: number,
    createdAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    updatedAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    state: as_external_api_fuotaDeployment_pb.FUOTADeploymentDeviceStateMap[keyof as_external_api_fuotaDeployment_pb.FUOTADeploymentDeviceStateMap],
    errorMessage: string,
  }
}

export class RemoteMulticastGroupListItem extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  getName(): string;
  setName(value: string): void;

  getServiceProfileId(): string;
  setServiceProfileId(value: string): void;

  getServiceProfileName(): string;
  setServiceProfileName(value: string): void;

  getState(): string;
  setState(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoteMulticastGroupListItem.AsObject;
  static toObject(includeInstance: boolean, msg: RemoteMulticastGroupListItem): RemoteMulticastGroupListItem.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoteMulticastGroupListItem, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoteMulticastGroupListItem;
  static deserializeBinaryFromReader(message: RemoteMulticastGroupListItem, reader: jspb.BinaryReader): RemoteMulticastGroupListItem;
}

export namespace RemoteMulticastGroupListItem {
  export type AsObject = {
    id: string,
    name: string,
    serviceProfileId: string,
    serviceProfileName: string,
    state: string,
  }
}

export class CreateRemoteMulticastGroupRequest extends jspb.Message {
  hasRemoteMulticastGroup(): boolean;
  clearRemoteMulticastGroup(): void;
  getRemoteMulticastGroup(): RemoteMulticastGroup | undefined;
  setRemoteMulticastGroup(value?: RemoteMulticastGroup): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateRemoteMulticastGroupRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateRemoteMulticastGroupRequest): CreateRemoteMulticastGroupRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateRemoteMulticastGroupRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateRemoteMulticastGroupRequest;
  static deserializeBinaryFromReader(message: CreateRemoteMulticastGroupRequest, reader: jspb.BinaryReader): CreateRemoteMulticastGroupRequest;
}

export namespace CreateRemoteMulticastGroupRequest {
  export type AsObject = {
    remoteMulticastGroup?: RemoteMulticastGroup.AsObject,
  }
}

export class CreateRemoteMulticastGroupResponse extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateRemoteMulticastGroupResponse.AsObject;
  static toObject(includeInstance: boolean, msg: CreateRemoteMulticastGroupResponse): CreateRemoteMulticastGroupResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateRemoteMulticastGroupResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateRemoteMulticastGroupResponse;
  static deserializeBinaryFromReader(message: CreateRemoteMulticastGroupResponse, reader: jspb.BinaryReader): CreateRemoteMulticastGroupResponse;
}

export namespace CreateRemoteMulticastGroupResponse {
  export type AsObject = {
    id: string,
  }
}

export class GetRemoteMulticastGroupRequest extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRemoteMulticastGroupRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRemoteMulticastGroupRequest): GetRemoteMulticastGroupRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRemoteMulticastGroupRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRemoteMulticastGroupRequest;
  static deserializeBinaryFromReader(message: GetRemoteMulticastGroupRequest, reader: jspb.BinaryReader): GetRemoteMulticastGroupRequest;
}

export namespace GetRemoteMulticastGroupRequest {
  export type AsObject = {
    id: string,
  }
}

export class GetRemoteMulticastGroupResponse extends jspb.Message {
  hasRemoteMulticastGroup(): boolean;
  clearRemoteMulticastGroup(): void;
  getRemoteMulticastGroup(): RemoteMulticastGroup | undefined;
  setRemoteMulticastGroup(value?: RemoteMulticastGroup): void;

  hasCreatedAt(): boolean;
  clearCreatedAt(): void;
  getCreatedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setCreatedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasUpdatedAt(): boolean;
  clearUpdatedAt(): void;
  getUpdatedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setUpdatedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRemoteMulticastGroupResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetRemoteMulticastGroupResponse): GetRemoteMulticastGroupResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRemoteMulticastGroupResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRemoteMulticastGroupResponse;
  static deserializeBinaryFromReader(message: GetRemoteMulticastGroupResponse, reader: jspb.BinaryReader): GetRemoteMulticastGroupResponse;
}

export namespace GetRemoteMulticastGroupResponse {
  export type AsObject = {
    remoteMulticastGroup?: RemoteMulticastGroup.AsObject,
    createdAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    updatedAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class ListRemoteMulticastGroupRequest extends jspb.Message {
  getLimit(): number;
  setLimit(value: number): void;

  getOffset(): number;
  setOffset(value: number): void;

  getOrganizationId(): number;
  setOrganizationId(value: number): void;

  getServiceProfileId(): string;
  setServiceProfileId(value: string): void;

  getSearch(): string;
  setSearch(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListRemoteMulticastGroupRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ListRemoteMulticastGroupRequest): ListRemoteMulticastGroupRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ListRemoteMulticastGroupRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListRemoteMulticastGroupRequest;
  static deserializeBinaryFromReader(message: ListRemoteMulticastGroupRequest, reader: jspb.BinaryReader): ListRemoteMulticastGroupRequest;
}

export namespace ListRemoteMulticastGroupRequest {
  export type AsObject = {
    limit: number,
    offset: number,
    organizationId: number,
    serviceProfileId: string,
    search: string,
  }
}

export class ListRemoteMulticastGroupResponse extends jspb.Message {
  getTotalCount(): number;
  setTotalCount(value: number): void;

  clearResultList(): void;
  getResultList(): Array<RemoteMulticastGroupListItem>;
  setResultList(value: Array<RemoteMulticastGroupListItem>): void;
  addResult(value?: RemoteMulticastGroupListItem, index?: number): RemoteMulticastGroupListItem;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListRemoteMulticastGroupResponse.AsObject;
  static toObject(includeInstance: boolean, msg: ListRemoteMulticastGroupResponse): ListRemoteMulticastGroupResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ListRemoteMulticastGroupResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListRemoteMulticastGroupResponse;
  static deserializeBinaryFromReader(message: ListRemoteMulticastGroupResponse, reader: jspb.BinaryReader): ListRemoteMulticastGroupResponse;
}

export namespace ListRemoteMulticastGroupResponse {
  export type AsObject = {
    totalCount: number,
    resultList: Array<RemoteMulticastGroupListItem.AsObject>,
  }
}

export class UpdateRemoteMulticastGroupRequest extends jspb.Message {
  hasRemoteMulticastGroup(): boolean;
  clearRemoteMulticastGroup(): void;
  getRemoteMulticastGroup(): RemoteMulticastGroup | undefined;
  setRemoteMulticastGroup(value?: RemoteMulticastGroup): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateRemoteMulticastGroupRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateRemoteMulticastGroupRequest): UpdateRemoteMulticastGroupRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateRemoteMulticastGroupRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateRemoteMulticastGroupRequest;
  static deserializeBinaryFromReader(message: UpdateRemoteMulticastGroupRequest, reader: jspb.BinaryReader): UpdateRemoteMulticastGroupRequest;
}

export namespace UpdateRemoteMulticastGroupRequest {
  export type AsObject = {
    remoteMulticastGroup?: RemoteMulticastGroup.AsObject,
  }
}

export class DeleteRemoteMulticastGroupRequest extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteRemoteMulticastGroupRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteRemoteMulticastGroupRequest): DeleteRemoteMulticastGroupRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteRemoteMulticastGroupRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteRemoteMulticastGroupRequest;
  static deserializeBinaryFromReader(message: DeleteRemoteMulticastGroupRequest, reader: jspb.BinaryReader): DeleteRemoteMulticastGroupRequest;
}

export namespace DeleteRemoteMulticastGroupRequest {
  export type AsObject = {
    id: string,
  }
}

export class AddDeviceToRemoteMulticastGroupRequest extends jspb.Message {
  getRemoteMulticastGroupId(): string;
  setRemoteMulticastGroupId(value: string): void;

  clearDevEuisList(): void;
  getDevEuisList(): Array<string>;
  setDevEuisList(value: Array<string>): void;
  addDevEuis(value: string, index?: number): string;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddDeviceToRemoteMulticastGroupRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddDeviceToRemoteMulticastGroupRequest): AddDeviceToRemoteMulticastGroupRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddDeviceToRemoteMulticastGroupRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddDeviceToRemoteMulticastGroupRequest;
  static deserializeBinaryFromReader(message: AddDeviceToRemoteMulticastGroupRequest, reader: jspb.BinaryReader): AddDeviceToRemoteMulticastGroupRequest;
}

export namespace AddDeviceToRemoteMulticastGroupRequest {
  export type AsObject = {
    remoteMulticastGroupId: string,
    devEuisList: Array<string>,
  }
}

export class RemoveDeviceFromRemoteMulticastGroupRequest extends jspb.Message {
  getRemoteMulticastGroupId(): string;
  setRemoteMulticastGroupId(value: string): void;

  getDevEui(): string;
  setDevEui(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveDeviceFromRemoteMulticastGroupRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveDeviceFromRemoteMulticastGroupRequest): RemoveDeviceFromRemoteMulticastGroupRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveDeviceFromRemoteMulticastGroupRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveDeviceFromRemoteMulticastGroupRequest;
  static deserializeBinaryFromReader(message: RemoveDeviceFromRemoteMulticastGroupRequest, reader: jspb.BinaryReader): RemoveDeviceFromRemoteMulticastGroupRequest;
}

export namespace RemoveDeviceFromRemoteMulticastGroupRequest {
  export type AsObject = {
    remoteMulticastGroupId: string,
    devEui: string,
  }
}

export class ListRemoteMulticastDeviceRequest extends jspb.Message {
  getLimit(): number;
  setLimit(value: number): void;

  getOffset(): number;
  setOffset(value: number): void;

  getRemoteMulticastGroupId(): string;
  setRemoteMulticastGroupId(value: string): void;

  getApplicationId(): number;
  setApplicationId(value: number): void;

  getSearch(): string;
  setSearch(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListRemoteMulticastDeviceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ListRemoteMulticastDeviceRequest): ListRemoteMulticastDeviceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ListRemoteMulticastDeviceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListRemoteMulticastDeviceRequest;
  static deserializeBinaryFromReader(message: ListRemoteMulticastDeviceRequest, reader: jspb.BinaryReader): ListRemoteMulticastDeviceRequest;
}

export namespace ListRemoteMulticastDeviceRequest {
  export type AsObject = {
    limit: number,
    offset: number,
    remoteMulticastGroupId: string,
    applicationId: number,
    search: string,
  }
}

export class ListRemoteMulticastDeviceResponse extends jspb.Message {
  getTotalCount(): number;
  setTotalCount(value: number): void;

  clearResultList(): void;
  getResultList(): Array<as_external_api_device_pb.DeviceListItem>;
  setResultList(value: Array<as_external_api_device_pb.DeviceListItem>): void;
  addResult(value?: as_external_api_device_pb.DeviceListItem, index?: number): as_external_api_device_pb.DeviceListItem;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListRemoteMulticastDeviceResponse.AsObject;
  static toObject(includeInstance: boolean, msg: ListRemoteMulticastDeviceResponse): ListRemoteMulticastDeviceResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ListRemoteMulticastDeviceResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListRemoteMulticastDeviceResponse;
  static deserializeBinaryFromReader(message: ListRemoteMulticastDeviceResponse, reader: jspb.BinaryReader): ListRemoteMulticastDeviceResponse;
}

export namespace ListRemoteMulticastDeviceResponse {
  export type AsObject = {
    totalCount: number,
    resultList: Array<as_external_api_device_pb.DeviceListItem.AsObject>,
  }
}

export class ResetRemoteMulticastDeviceRequest extends jspb.Message {
  getDevEui(): string;
  setDevEui(value: string): void;

  getRemoteMulticastGroupId(): string;
  setRemoteMulticastGroupId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResetRemoteMulticastDeviceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ResetRemoteMulticastDeviceRequest): ResetRemoteMulticastDeviceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ResetRemoteMulticastDeviceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResetRemoteMulticastDeviceRequest;
  static deserializeBinaryFromReader(message: ResetRemoteMulticastDeviceRequest, reader: jspb.BinaryReader): ResetRemoteMulticastDeviceRequest;
}

export namespace ResetRemoteMulticastDeviceRequest {
  export type AsObject = {
    devEui: string,
    remoteMulticastGroupId: string,
  }
}

export class ListRemoteMulticastDevicesResponse extends jspb.Message {
  getTotalCount(): number;
  setTotalCount(value: number): void;

  clearResultList(): void;
  getResultList(): Array<RemoteMulticastDeploymentDevice>;
  setResultList(value: Array<RemoteMulticastDeploymentDevice>): void;
  addResult(value?: RemoteMulticastDeploymentDevice, index?: number): RemoteMulticastDeploymentDevice;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListRemoteMulticastDevicesResponse.AsObject;
  static toObject(includeInstance: boolean, msg: ListRemoteMulticastDevicesResponse): ListRemoteMulticastDevicesResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ListRemoteMulticastDevicesResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListRemoteMulticastDevicesResponse;
  static deserializeBinaryFromReader(message: ListRemoteMulticastDevicesResponse, reader: jspb.BinaryReader): ListRemoteMulticastDevicesResponse;
}

export namespace ListRemoteMulticastDevicesResponse {
  export type AsObject = {
    totalCount: number,
    resultList: Array<RemoteMulticastDeploymentDevice.AsObject>,
  }
}

export class GetRemoteMulticastDeploymentDeviceRequest extends jspb.Message {
  getRemoteMulticastGroupId(): string;
  setRemoteMulticastGroupId(value: string): void;

  getDevEui(): string;
  setDevEui(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRemoteMulticastDeploymentDeviceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRemoteMulticastDeploymentDeviceRequest): GetRemoteMulticastDeploymentDeviceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRemoteMulticastDeploymentDeviceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRemoteMulticastDeploymentDeviceRequest;
  static deserializeBinaryFromReader(message: GetRemoteMulticastDeploymentDeviceRequest, reader: jspb.BinaryReader): GetRemoteMulticastDeploymentDeviceRequest;
}

export namespace GetRemoteMulticastDeploymentDeviceRequest {
  export type AsObject = {
    remoteMulticastGroupId: string,
    devEui: string,
  }
}

export class GetRemoteMulticastDeploymentDeviceResponse extends jspb.Message {
  hasDeploymentDevice(): boolean;
  clearDeploymentDevice(): void;
  getDeploymentDevice(): RemoteMulticastDeploymentDevice | undefined;
  setDeploymentDevice(value?: RemoteMulticastDeploymentDevice): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRemoteMulticastDeploymentDeviceResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetRemoteMulticastDeploymentDeviceResponse): GetRemoteMulticastDeploymentDeviceResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRemoteMulticastDeploymentDeviceResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRemoteMulticastDeploymentDeviceResponse;
  static deserializeBinaryFromReader(message: GetRemoteMulticastDeploymentDeviceResponse, reader: jspb.BinaryReader): GetRemoteMulticastDeploymentDeviceResponse;
}

export namespace GetRemoteMulticastDeploymentDeviceResponse {
  export type AsObject = {
    deploymentDevice?: RemoteMulticastDeploymentDevice.AsObject,
  }
}

export class RemoteMulticastQueueItem extends jspb.Message {
  getRemoteMulticastGroupId(): string;
  setRemoteMulticastGroupId(value: string): void;

  getFCnt(): number;
  setFCnt(value: number): void;

  getFPort(): number;
  setFPort(value: number): void;

  getData(): Uint8Array | string;
  getData_asU8(): Uint8Array;
  getData_asB64(): string;
  setData(value: Uint8Array | string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoteMulticastQueueItem.AsObject;
  static toObject(includeInstance: boolean, msg: RemoteMulticastQueueItem): RemoteMulticastQueueItem.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoteMulticastQueueItem, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoteMulticastQueueItem;
  static deserializeBinaryFromReader(message: RemoteMulticastQueueItem, reader: jspb.BinaryReader): RemoteMulticastQueueItem;
}

export namespace RemoteMulticastQueueItem {
  export type AsObject = {
    remoteMulticastGroupId: string,
    fCnt: number,
    fPort: number,
    data: Uint8Array | string,
  }
}

export class EnqueueRemoteMulticastQueueItemRequest extends jspb.Message {
  hasRemoteMulticastQueueItem(): boolean;
  clearRemoteMulticastQueueItem(): void;
  getRemoteMulticastQueueItem(): RemoteMulticastQueueItem | undefined;
  setRemoteMulticastQueueItem(value?: RemoteMulticastQueueItem): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EnqueueRemoteMulticastQueueItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: EnqueueRemoteMulticastQueueItemRequest): EnqueueRemoteMulticastQueueItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EnqueueRemoteMulticastQueueItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EnqueueRemoteMulticastQueueItemRequest;
  static deserializeBinaryFromReader(message: EnqueueRemoteMulticastQueueItemRequest, reader: jspb.BinaryReader): EnqueueRemoteMulticastQueueItemRequest;
}

export namespace EnqueueRemoteMulticastQueueItemRequest {
  export type AsObject = {
    remoteMulticastQueueItem?: RemoteMulticastQueueItem.AsObject,
  }
}

export class EnqueueRemoteMulticastQueueItemResponse extends jspb.Message {
  getFCnt(): number;
  setFCnt(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EnqueueRemoteMulticastQueueItemResponse.AsObject;
  static toObject(includeInstance: boolean, msg: EnqueueRemoteMulticastQueueItemResponse): EnqueueRemoteMulticastQueueItemResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EnqueueRemoteMulticastQueueItemResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EnqueueRemoteMulticastQueueItemResponse;
  static deserializeBinaryFromReader(message: EnqueueRemoteMulticastQueueItemResponse, reader: jspb.BinaryReader): EnqueueRemoteMulticastQueueItemResponse;
}

export namespace EnqueueRemoteMulticastQueueItemResponse {
  export type AsObject = {
    fCnt: number,
  }
}

export class FlushRemoteMulticastGroupQueueItemsRequest extends jspb.Message {
  getRemoteMulticastGroupId(): string;
  setRemoteMulticastGroupId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): FlushRemoteMulticastGroupQueueItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: FlushRemoteMulticastGroupQueueItemsRequest): FlushRemoteMulticastGroupQueueItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: FlushRemoteMulticastGroupQueueItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): FlushRemoteMulticastGroupQueueItemsRequest;
  static deserializeBinaryFromReader(message: FlushRemoteMulticastGroupQueueItemsRequest, reader: jspb.BinaryReader): FlushRemoteMulticastGroupQueueItemsRequest;
}

export namespace FlushRemoteMulticastGroupQueueItemsRequest {
  export type AsObject = {
    remoteMulticastGroupId: string,
  }
}

export class ListRemoteMulticastGroupQueueItemsRequest extends jspb.Message {
  getRemoteMulticastGroupId(): string;
  setRemoteMulticastGroupId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListRemoteMulticastGroupQueueItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ListRemoteMulticastGroupQueueItemsRequest): ListRemoteMulticastGroupQueueItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ListRemoteMulticastGroupQueueItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListRemoteMulticastGroupQueueItemsRequest;
  static deserializeBinaryFromReader(message: ListRemoteMulticastGroupQueueItemsRequest, reader: jspb.BinaryReader): ListRemoteMulticastGroupQueueItemsRequest;
}

export namespace ListRemoteMulticastGroupQueueItemsRequest {
  export type AsObject = {
    remoteMulticastGroupId: string,
  }
}

export class ListRemoteMulticastGroupQueueItemsResponse extends jspb.Message {
  clearRemoteMulticastQueueItemsList(): void;
  getRemoteMulticastQueueItemsList(): Array<RemoteMulticastQueueItem>;
  setRemoteMulticastQueueItemsList(value: Array<RemoteMulticastQueueItem>): void;
  addRemoteMulticastQueueItems(value?: RemoteMulticastQueueItem, index?: number): RemoteMulticastQueueItem;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListRemoteMulticastGroupQueueItemsResponse.AsObject;
  static toObject(includeInstance: boolean, msg: ListRemoteMulticastGroupQueueItemsResponse): ListRemoteMulticastGroupQueueItemsResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ListRemoteMulticastGroupQueueItemsResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListRemoteMulticastGroupQueueItemsResponse;
  static deserializeBinaryFromReader(message: ListRemoteMulticastGroupQueueItemsResponse, reader: jspb.BinaryReader): ListRemoteMulticastGroupQueueItemsResponse;
}

export namespace ListRemoteMulticastGroupQueueItemsResponse {
  export type AsObject = {
    remoteMulticastQueueItemsList: Array<RemoteMulticastQueueItem.AsObject>,
  }
}

