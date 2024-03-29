// package: api
// file: as/external/api/frameLog.proto

import * as jspb from "google-protobuf";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
import * as gw_gw_pb from "../../../gw/gw_pb";
import * as common_common_pb from "../../../common/common_pb";

export class UplinkFrameLog extends jspb.Message {
  hasTxInfo(): boolean;
  clearTxInfo(): void;
  getTxInfo(): gw_gw_pb.UplinkTXInfo | undefined;
  setTxInfo(value?: gw_gw_pb.UplinkTXInfo): void;

  clearRxInfoList(): void;
  getRxInfoList(): Array<gw_gw_pb.UplinkRXInfo>;
  setRxInfoList(value: Array<gw_gw_pb.UplinkRXInfo>): void;
  addRxInfo(value?: gw_gw_pb.UplinkRXInfo, index?: number): gw_gw_pb.UplinkRXInfo;

  getPhyPayloadJson(): string;
  setPhyPayloadJson(value: string): void;

  hasPublishedAt(): boolean;
  clearPublishedAt(): void;
  getPublishedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setPublishedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UplinkFrameLog.AsObject;
  static toObject(includeInstance: boolean, msg: UplinkFrameLog): UplinkFrameLog.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UplinkFrameLog, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UplinkFrameLog;
  static deserializeBinaryFromReader(message: UplinkFrameLog, reader: jspb.BinaryReader): UplinkFrameLog;
}

export namespace UplinkFrameLog {
  export type AsObject = {
    txInfo?: gw_gw_pb.UplinkTXInfo.AsObject,
    rxInfoList: Array<gw_gw_pb.UplinkRXInfo.AsObject>,
    phyPayloadJson: string,
    publishedAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class DownlinkFrameLog extends jspb.Message {
  hasTxInfo(): boolean;
  clearTxInfo(): void;
  getTxInfo(): gw_gw_pb.DownlinkTXInfo | undefined;
  setTxInfo(value?: gw_gw_pb.DownlinkTXInfo): void;

  getPhyPayloadJson(): string;
  setPhyPayloadJson(value: string): void;

  getGatewayId(): string;
  setGatewayId(value: string): void;

  hasPublishedAt(): boolean;
  clearPublishedAt(): void;
  getPublishedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setPublishedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DownlinkFrameLog.AsObject;
  static toObject(includeInstance: boolean, msg: DownlinkFrameLog): DownlinkFrameLog.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DownlinkFrameLog, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DownlinkFrameLog;
  static deserializeBinaryFromReader(message: DownlinkFrameLog, reader: jspb.BinaryReader): DownlinkFrameLog;
}

export namespace DownlinkFrameLog {
  export type AsObject = {
    txInfo?: gw_gw_pb.DownlinkTXInfo.AsObject,
    phyPayloadJson: string,
    gatewayId: string,
    publishedAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GatewayStatsFrameLog extends jspb.Message {
  getGatewayId(): Uint8Array | string;
  getGatewayId_asU8(): Uint8Array;
  getGatewayId_asB64(): string;
  setGatewayId(value: Uint8Array | string): void;

  getIp(): string;
  setIp(value: string): void;

  hasTime(): boolean;
  clearTime(): void;
  getTime(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTime(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasLocation(): boolean;
  clearLocation(): void;
  getLocation(): common_common_pb.Location | undefined;
  setLocation(value?: common_common_pb.Location): void;

  getConfigVersion(): string;
  setConfigVersion(value: string): void;

  getRxPacketsReceived(): number;
  setRxPacketsReceived(value: number): void;

  getRxPacketsReceivedOk(): number;
  setRxPacketsReceivedOk(value: number): void;

  getTxPacketsReceived(): number;
  setTxPacketsReceived(value: number): void;

  getTxPacketsEmitted(): number;
  setTxPacketsEmitted(value: number): void;

  getMetaDataMap(): jspb.Map<string, string>;
  clearMetaDataMap(): void;
  getStatsId(): Uint8Array | string;
  getStatsId_asU8(): Uint8Array;
  getStatsId_asB64(): string;
  setStatsId(value: Uint8Array | string): void;

  hasPublishedAt(): boolean;
  clearPublishedAt(): void;
  getPublishedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setPublishedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  getAckRate(): number;
  setAckRate(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GatewayStatsFrameLog.AsObject;
  static toObject(includeInstance: boolean, msg: GatewayStatsFrameLog): GatewayStatsFrameLog.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GatewayStatsFrameLog, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GatewayStatsFrameLog;
  static deserializeBinaryFromReader(message: GatewayStatsFrameLog, reader: jspb.BinaryReader): GatewayStatsFrameLog;
}

export namespace GatewayStatsFrameLog {
  export type AsObject = {
    gatewayId: Uint8Array | string,
    ip: string,
    time?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    location?: common_common_pb.Location.AsObject,
    configVersion: string,
    rxPacketsReceived: number,
    rxPacketsReceivedOk: number,
    txPacketsReceived: number,
    txPacketsEmitted: number,
    metaDataMap: Array<[string, string]>,
    statsId: Uint8Array | string,
    publishedAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    ackRate: number,
  }
}

export interface RXWindowMap {
  RX1: 0;
  RX2: 1;
}

export const RXWindow: RXWindowMap;

