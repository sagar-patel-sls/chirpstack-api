// Code generated by protoc-gen-go. DO NOT EDIT.
// source: as/external/api/frameLog.proto

package api

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	common "github.com/sagar-patel-sls/chirpstack-api/go/v3/common"
	gw "github.com/sagar-patel-sls/chirpstack-api/go/v3/gw"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type RXWindow int32

const (
	RXWindow_RX1 RXWindow = 0
	RXWindow_RX2 RXWindow = 1
)

var RXWindow_name = map[int32]string{
	0: "RX1",
	1: "RX2",
}

var RXWindow_value = map[string]int32{
	"RX1": 0,
	"RX2": 1,
}

func (x RXWindow) String() string {
	return proto.EnumName(RXWindow_name, int32(x))
}

func (RXWindow) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_d215818867a60801, []int{0}
}

type UplinkFrameLog struct {
	// TX information of the uplink.
	TxInfo *gw.UplinkTXInfo `protobuf:"bytes,1,opt,name=tx_info,json=txInfo,proto3" json:"tx_info,omitempty"`
	// RX information of the uplink.
	RxInfo []*gw.UplinkRXInfo `protobuf:"bytes,2,rep,name=rx_info,json=rxInfo,proto3" json:"rx_info,omitempty"`
	// LoRaWAN PHYPayload.
	PhyPayloadJson string `protobuf:"bytes,3,opt,name=phy_payload_json,json=phyPayloadJSON,proto3" json:"phy_payload_json,omitempty"`
	// Published at timestamp.
	PublishedAt          *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=published_at,json=publishedAt,proto3" json:"published_at,omitempty"`
	XXX_NoUnkeyedLiteral struct{}               `json:"-"`
	XXX_unrecognized     []byte                 `json:"-"`
	XXX_sizecache        int32                  `json:"-"`
}

func (m *UplinkFrameLog) Reset()         { *m = UplinkFrameLog{} }
func (m *UplinkFrameLog) String() string { return proto.CompactTextString(m) }
func (*UplinkFrameLog) ProtoMessage()    {}
func (*UplinkFrameLog) Descriptor() ([]byte, []int) {
	return fileDescriptor_d215818867a60801, []int{0}
}

func (m *UplinkFrameLog) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_UplinkFrameLog.Unmarshal(m, b)
}
func (m *UplinkFrameLog) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_UplinkFrameLog.Marshal(b, m, deterministic)
}
func (m *UplinkFrameLog) XXX_Merge(src proto.Message) {
	xxx_messageInfo_UplinkFrameLog.Merge(m, src)
}
func (m *UplinkFrameLog) XXX_Size() int {
	return xxx_messageInfo_UplinkFrameLog.Size(m)
}
func (m *UplinkFrameLog) XXX_DiscardUnknown() {
	xxx_messageInfo_UplinkFrameLog.DiscardUnknown(m)
}

var xxx_messageInfo_UplinkFrameLog proto.InternalMessageInfo

func (m *UplinkFrameLog) GetTxInfo() *gw.UplinkTXInfo {
	if m != nil {
		return m.TxInfo
	}
	return nil
}

func (m *UplinkFrameLog) GetRxInfo() []*gw.UplinkRXInfo {
	if m != nil {
		return m.RxInfo
	}
	return nil
}

func (m *UplinkFrameLog) GetPhyPayloadJson() string {
	if m != nil {
		return m.PhyPayloadJson
	}
	return ""
}

func (m *UplinkFrameLog) GetPublishedAt() *timestamppb.Timestamp {
	if m != nil {
		return m.PublishedAt
	}
	return nil
}

type DownlinkFrameLog struct {
	// TX information of the downlink.
	TxInfo *gw.DownlinkTXInfo `protobuf:"bytes,1,opt,name=tx_info,json=txInfo,proto3" json:"tx_info,omitempty"`
	// LoRaWAN PHYPayload.
	PhyPayloadJson string `protobuf:"bytes,2,opt,name=phy_payload_json,json=phyPayloadJSON,proto3" json:"phy_payload_json,omitempty"`
	// Gateway ID.
	GatewayId string `protobuf:"bytes,3,opt,name=gateway_id,json=gatewayID,proto3" json:"gateway_id,omitempty"`
	// Published at timestamp.
	PublishedAt          *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=published_at,json=publishedAt,proto3" json:"published_at,omitempty"`
	XXX_NoUnkeyedLiteral struct{}               `json:"-"`
	XXX_unrecognized     []byte                 `json:"-"`
	XXX_sizecache        int32                  `json:"-"`
}

func (m *DownlinkFrameLog) Reset()         { *m = DownlinkFrameLog{} }
func (m *DownlinkFrameLog) String() string { return proto.CompactTextString(m) }
func (*DownlinkFrameLog) ProtoMessage()    {}
func (*DownlinkFrameLog) Descriptor() ([]byte, []int) {
	return fileDescriptor_d215818867a60801, []int{1}
}

func (m *DownlinkFrameLog) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DownlinkFrameLog.Unmarshal(m, b)
}
func (m *DownlinkFrameLog) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DownlinkFrameLog.Marshal(b, m, deterministic)
}
func (m *DownlinkFrameLog) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DownlinkFrameLog.Merge(m, src)
}
func (m *DownlinkFrameLog) XXX_Size() int {
	return xxx_messageInfo_DownlinkFrameLog.Size(m)
}
func (m *DownlinkFrameLog) XXX_DiscardUnknown() {
	xxx_messageInfo_DownlinkFrameLog.DiscardUnknown(m)
}

var xxx_messageInfo_DownlinkFrameLog proto.InternalMessageInfo

func (m *DownlinkFrameLog) GetTxInfo() *gw.DownlinkTXInfo {
	if m != nil {
		return m.TxInfo
	}
	return nil
}

func (m *DownlinkFrameLog) GetPhyPayloadJson() string {
	if m != nil {
		return m.PhyPayloadJson
	}
	return ""
}

func (m *DownlinkFrameLog) GetGatewayId() string {
	if m != nil {
		return m.GatewayId
	}
	return ""
}

func (m *DownlinkFrameLog) GetPublishedAt() *timestamppb.Timestamp {
	if m != nil {
		return m.PublishedAt
	}
	return nil
}

type GatewayStatsFrameLog struct {
	// Gateway ID.
	GatewayId []byte `protobuf:"bytes,1,opt,name=gateway_id,json=gatewayID,proto3" json:"gateway_id,omitempty"`
	// Gateway IP.
	Ip string `protobuf:"bytes,9,opt,name=ip,proto3" json:"ip,omitempty"`
	// Gateway time.
	Time *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=time,proto3" json:"time,omitempty"`
	// Gateway location.
	Location *common.Location `protobuf:"bytes,3,opt,name=location,proto3" json:"location,omitempty"`
	// Gateway configuration version (this maps to the config_version sent
	// by LoRa Server to the gateway).
	ConfigVersion string `protobuf:"bytes,4,opt,name=config_version,json=configVersion,proto3" json:"config_version,omitempty"`
	// Number of radio packets received.
	RxPacketsReceived uint32 `protobuf:"varint,5,opt,name=rx_packets_received,json=rxPacketsReceived,proto3" json:"rx_packets_received,omitempty"`
	// Number of radio packets received with valid PHY CRC.
	RxPacketsReceivedOk uint32 `protobuf:"varint,6,opt,name=rx_packets_received_ok,json=rxPacketsReceivedOK,proto3" json:"rx_packets_received_ok,omitempty"`
	// Number of downlink packets received for transmission.
	TxPacketsReceived uint32 `protobuf:"varint,7,opt,name=tx_packets_received,json=txPacketsReceived,proto3" json:"tx_packets_received,omitempty"`
	// Number of downlink packets emitted.
	TxPacketsEmitted uint32 `protobuf:"varint,8,opt,name=tx_packets_emitted,json=txPacketsEmitted,proto3" json:"tx_packets_emitted,omitempty"`
	// Additional gateway meta-data.
	MetaData map[string]string `protobuf:"bytes,10,rep,name=meta_data,json=metaData,proto3" json:"meta_data,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	// Stats ID (UUID).
	// Unique identifier for the gateway stats.
	StatsId []byte `protobuf:"bytes,11,opt,name=stats_id,json=statsID,proto3" json:"stats_id,omitempty"`
	// Published at timestamp.
	PublishedAt *timestamppb.Timestamp `protobuf:"bytes,12,opt,name=published_at,json=publishedAt,proto3" json:"published_at,omitempty"`
	// As the exposed ack-rate represents the last reported ack-rate by the GW,
	// it is also important to monitor the ack-rate count. If this value does
	// not increment, it could mean that the GW is no longer reporting the
	// ack-rate and thus the exposed ack-rate is stale.
	AckRate              float32  `protobuf:"fixed32,13,opt,name=ack_rate,json=ackRate,proto3" json:"ack_rate,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *GatewayStatsFrameLog) Reset()         { *m = GatewayStatsFrameLog{} }
func (m *GatewayStatsFrameLog) String() string { return proto.CompactTextString(m) }
func (*GatewayStatsFrameLog) ProtoMessage()    {}
func (*GatewayStatsFrameLog) Descriptor() ([]byte, []int) {
	return fileDescriptor_d215818867a60801, []int{2}
}

func (m *GatewayStatsFrameLog) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GatewayStatsFrameLog.Unmarshal(m, b)
}
func (m *GatewayStatsFrameLog) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GatewayStatsFrameLog.Marshal(b, m, deterministic)
}
func (m *GatewayStatsFrameLog) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GatewayStatsFrameLog.Merge(m, src)
}
func (m *GatewayStatsFrameLog) XXX_Size() int {
	return xxx_messageInfo_GatewayStatsFrameLog.Size(m)
}
func (m *GatewayStatsFrameLog) XXX_DiscardUnknown() {
	xxx_messageInfo_GatewayStatsFrameLog.DiscardUnknown(m)
}

var xxx_messageInfo_GatewayStatsFrameLog proto.InternalMessageInfo

func (m *GatewayStatsFrameLog) GetGatewayId() []byte {
	if m != nil {
		return m.GatewayId
	}
	return nil
}

func (m *GatewayStatsFrameLog) GetIp() string {
	if m != nil {
		return m.Ip
	}
	return ""
}

func (m *GatewayStatsFrameLog) GetTime() *timestamppb.Timestamp {
	if m != nil {
		return m.Time
	}
	return nil
}

func (m *GatewayStatsFrameLog) GetLocation() *common.Location {
	if m != nil {
		return m.Location
	}
	return nil
}

func (m *GatewayStatsFrameLog) GetConfigVersion() string {
	if m != nil {
		return m.ConfigVersion
	}
	return ""
}

func (m *GatewayStatsFrameLog) GetRxPacketsReceived() uint32 {
	if m != nil {
		return m.RxPacketsReceived
	}
	return 0
}

func (m *GatewayStatsFrameLog) GetRxPacketsReceivedOk() uint32 {
	if m != nil {
		return m.RxPacketsReceivedOk
	}
	return 0
}

func (m *GatewayStatsFrameLog) GetTxPacketsReceived() uint32 {
	if m != nil {
		return m.TxPacketsReceived
	}
	return 0
}

func (m *GatewayStatsFrameLog) GetTxPacketsEmitted() uint32 {
	if m != nil {
		return m.TxPacketsEmitted
	}
	return 0
}

func (m *GatewayStatsFrameLog) GetMetaData() map[string]string {
	if m != nil {
		return m.MetaData
	}
	return nil
}

func (m *GatewayStatsFrameLog) GetStatsId() []byte {
	if m != nil {
		return m.StatsId
	}
	return nil
}

func (m *GatewayStatsFrameLog) GetPublishedAt() *timestamppb.Timestamp {
	if m != nil {
		return m.PublishedAt
	}
	return nil
}

func (m *GatewayStatsFrameLog) GetAckRate() float32 {
	if m != nil {
		return m.AckRate
	}
	return 0
}

func init() {
	proto.RegisterEnum("api.RXWindow", RXWindow_name, RXWindow_value)
	proto.RegisterType((*UplinkFrameLog)(nil), "api.UplinkFrameLog")
	proto.RegisterType((*DownlinkFrameLog)(nil), "api.DownlinkFrameLog")
	proto.RegisterType((*GatewayStatsFrameLog)(nil), "api.GatewayStatsFrameLog")
	proto.RegisterMapType((map[string]string)(nil), "api.GatewayStatsFrameLog.MetaDataEntry")
}

func init() {
	proto.RegisterFile("as/external/api/frameLog.proto", fileDescriptor_d215818867a60801)
}

var fileDescriptor_d215818867a60801 = []byte{
	// 671 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xa4, 0x94, 0xed, 0x6e, 0xd3, 0x3c,
	0x14, 0xc7, 0x9f, 0xb4, 0xdb, 0xda, 0xba, 0x6b, 0x95, 0xc7, 0x9b, 0x1e, 0xe5, 0xa9, 0x78, 0x29,
	0x93, 0x10, 0x05, 0xb6, 0x44, 0x6c, 0x5f, 0x10, 0x08, 0x21, 0xa6, 0x0e, 0x34, 0x18, 0xac, 0xca,
	0x06, 0x4c, 0x7c, 0x89, 0x4e, 0x13, 0x37, 0x35, 0x79, 0xb1, 0x95, 0xb8, 0x6f, 0x17, 0xc0, 0x0d,
	0x70, 0x19, 0xdc, 0x08, 0x1f, 0xb9, 0x25, 0x64, 0x3b, 0x2d, 0xeb, 0x56, 0x21, 0x21, 0x3e, 0x25,
	0xe7, 0xf8, 0x67, 0xff, 0xcf, 0xdf, 0xe7, 0xc8, 0xe8, 0x16, 0xe4, 0x0e, 0x99, 0x0a, 0x92, 0xa5,
	0x10, 0x3b, 0xc0, 0xa9, 0x33, 0xc8, 0x20, 0x21, 0x27, 0x2c, 0xb4, 0x79, 0xc6, 0x04, 0xc3, 0x65,
	0xe0, 0xb4, 0x75, 0x3b, 0x64, 0x2c, 0x8c, 0x89, 0xa3, 0x52, 0xfd, 0xd1, 0xc0, 0x11, 0x34, 0x21,
	0xb9, 0x80, 0x84, 0x6b, 0xaa, 0x55, 0x0f, 0x27, 0x4e, 0x38, 0x29, 0x82, 0x2d, 0x9f, 0x25, 0x09,
	0x4b, 0x1d, 0xfd, 0xd1, 0xc9, 0x9d, 0x1f, 0x06, 0x6a, 0xbe, 0xe7, 0x31, 0x4d, 0xa3, 0x97, 0x85,
	0x00, 0xbe, 0x8f, 0x2a, 0x62, 0xea, 0xd1, 0x74, 0xc0, 0x2c, 0xa3, 0x6d, 0x74, 0xea, 0xfb, 0xa6,
	0x1d, 0x4e, 0x6c, 0x0d, 0x9d, 0x5f, 0x1c, 0xa7, 0x03, 0xe6, 0x6e, 0x88, 0xa9, 0xfc, 0x4a, 0x34,
	0x2b, 0xd0, 0x52, 0xbb, 0xbc, 0x8c, 0xba, 0x05, 0x9a, 0x69, 0xb4, 0x83, 0x4c, 0x3e, 0x9c, 0x79,
	0x1c, 0x66, 0x31, 0x83, 0xc0, 0xfb, 0x9c, 0xb3, 0xd4, 0x2a, 0xb7, 0x8d, 0x4e, 0xcd, 0x6d, 0xf2,
	0xe1, 0xac, 0xa7, 0xd3, 0xaf, 0xcf, 0x4e, 0xdf, 0xe1, 0x67, 0x68, 0x93, 0x8f, 0xfa, 0x31, 0xcd,
	0x87, 0x24, 0xf0, 0x40, 0x58, 0x6b, 0xaa, 0x88, 0x96, 0xad, 0xcd, 0xda, 0x73, 0xb3, 0xf6, 0xf9,
	0xdc, 0xac, 0x5b, 0x5f, 0xf0, 0x2f, 0xc4, 0xce, 0x77, 0x03, 0x99, 0x5d, 0x36, 0x49, 0x97, 0x3c,
	0x3d, 0xbc, 0xea, 0x09, 0xcb, 0x42, 0xe7, 0xd8, 0x15, 0x57, 0xab, 0x4a, 0x2d, 0xad, 0x2c, 0xf5,
	0x26, 0x42, 0x21, 0x08, 0x32, 0x81, 0x99, 0x47, 0x83, 0xc2, 0x4e, 0xad, 0xc8, 0x1c, 0x77, 0xff,
	0xd6, 0xc9, 0x97, 0x75, 0xb4, 0xfd, 0x4a, 0x1f, 0x76, 0x26, 0x40, 0xe4, 0x0b, 0x37, 0xcb, 0xb2,
	0xd2, 0xd0, 0xe6, 0x65, 0xd9, 0x26, 0x2a, 0x51, 0x6e, 0xd5, 0x54, 0x35, 0x25, 0xca, 0xb1, 0x8d,
	0xd6, 0xe4, 0x60, 0x28, 0x0f, 0xbf, 0x97, 0x57, 0x1c, 0xde, 0x45, 0xd5, 0x98, 0xf9, 0x20, 0x68,
	0xd1, 0x22, 0xd9, 0xd6, 0x62, 0x68, 0x4e, 0x8a, 0xbc, 0xbb, 0x20, 0xf0, 0x5d, 0xd4, 0xf4, 0x59,
	0x3a, 0xa0, 0xa1, 0x37, 0x26, 0x59, 0x2e, 0xf7, 0xac, 0x29, 0xe5, 0x86, 0xce, 0x7e, 0xd0, 0x49,
	0x6c, 0xa3, 0xad, 0x6c, 0xea, 0x71, 0xf0, 0x23, 0x22, 0x72, 0x2f, 0x23, 0x3e, 0xa1, 0x63, 0x12,
	0x58, 0xeb, 0x6d, 0xa3, 0xd3, 0x70, 0xff, 0xcd, 0xa6, 0x3d, 0xbd, 0xe2, 0x16, 0x0b, 0xf8, 0x00,
	0xfd, 0xb7, 0x82, 0xf7, 0x58, 0x64, 0x6d, 0xa8, 0x2d, 0x5b, 0xd7, 0xb6, 0x9c, 0xbe, 0x91, 0x22,
	0x62, 0x85, 0x48, 0x45, 0x8b, 0x88, 0x6b, 0x22, 0xbb, 0x08, 0x5f, 0xe2, 0x49, 0x42, 0x85, 0x20,
	0x81, 0x55, 0x55, 0xb8, 0xb9, 0xc0, 0x8f, 0x74, 0x1e, 0x77, 0x51, 0x2d, 0x21, 0x02, 0xbc, 0x00,
	0x04, 0x58, 0x48, 0xcd, 0xfb, 0x3d, 0x1b, 0x38, 0xb5, 0x57, 0x35, 0xc9, 0x7e, 0x4b, 0x04, 0x74,
	0x41, 0xc0, 0x51, 0x2a, 0xb2, 0x99, 0x5b, 0x4d, 0x8a, 0x10, 0xff, 0x8f, 0xaa, 0xb9, 0x04, 0x65,
	0xeb, 0xea, 0xaa, 0x75, 0x15, 0x15, 0xaf, 0x98, 0x97, 0xcd, 0x3f, 0x9a, 0x17, 0x79, 0x32, 0xf8,
	0x91, 0x97, 0x81, 0x20, 0x56, 0xa3, 0x6d, 0x74, 0x4a, 0x6e, 0x05, 0xfc, 0xc8, 0x05, 0x41, 0x5a,
	0x4f, 0x51, 0x63, 0xa9, 0x1e, 0x6c, 0xa2, 0x72, 0x44, 0x66, 0x6a, 0x76, 0x6a, 0xae, 0xfc, 0xc5,
	0xdb, 0x68, 0x7d, 0x0c, 0xf1, 0x88, 0x14, 0xa3, 0xae, 0x83, 0x27, 0xa5, 0xc7, 0xc6, 0x83, 0x1b,
	0xa8, 0xea, 0x5e, 0x7c, 0xa4, 0x69, 0xc0, 0x26, 0xb8, 0x82, 0xca, 0xee, 0xc5, 0x23, 0xf3, 0x1f,
	0xfd, 0xb3, 0x6f, 0x1a, 0x87, 0x5f, 0x0d, 0x74, 0x87, 0x32, 0xdb, 0x1f, 0xd2, 0x8c, 0xe7, 0x02,
	0xfc, 0x48, 0x5d, 0x09, 0xe4, 0xf6, 0xfc, 0xf9, 0x92, 0xf1, 0x61, 0x63, 0x7e, 0x2f, 0x3d, 0x69,
	0xa2, 0x67, 0x7c, 0x7a, 0x1e, 0x52, 0x31, 0x1c, 0xf5, 0xe5, 0x60, 0x39, 0x39, 0x84, 0x90, 0xed,
	0x71, 0x10, 0x24, 0xde, 0xcb, 0xe3, 0xdc, 0xf9, 0x75, 0xd6, 0x9e, 0x7c, 0xfa, 0x42, 0xe6, 0x8c,
	0x0f, 0x9c, 0x2b, 0x0f, 0xe2, 0xb7, 0x52, 0xeb, 0xb2, 0xe4, 0xb2, 0x5c, 0x7f, 0x43, 0xdd, 0xd5,
	0xc1, 0xcf, 0x00, 0x00, 0x00, 0xff, 0xff, 0xef, 0xb9, 0xd6, 0xfe, 0x47, 0x05, 0x00, 0x00,
}
