// Code generated by protoc-gen-go. DO NOT EDIT.
// source: as/external/api/frameLog.proto

package api

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
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

func init() {
	proto.RegisterEnum("api.RXWindow", RXWindow_name, RXWindow_value)
	proto.RegisterType((*UplinkFrameLog)(nil), "api.UplinkFrameLog")
	proto.RegisterType((*DownlinkFrameLog)(nil), "api.DownlinkFrameLog")
}

func init() {
	proto.RegisterFile("as/external/api/frameLog.proto", fileDescriptor_d215818867a60801)
}

var fileDescriptor_d215818867a60801 = []byte{
	// 380 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xa4, 0x92, 0xcf, 0x8b, 0xda, 0x40,
	0x14, 0xc7, 0x1b, 0x53, 0xb4, 0x8e, 0xad, 0x84, 0x9c, 0x44, 0xfa, 0xc3, 0x7a, 0xb2, 0x2d, 0xce,
	0x50, 0x3d, 0x97, 0x52, 0x91, 0x82, 0xa5, 0xb4, 0x92, 0x5a, 0x56, 0xf6, 0x12, 0x5e, 0xcc, 0x64,
	0x32, 0x6b, 0x92, 0x19, 0x32, 0x93, 0x8d, 0xf9, 0x0b, 0xf7, 0xb8, 0xff, 0xd2, 0x12, 0x93, 0xec,
	0xa2, 0x78, 0xdb, 0xd3, 0xcc, 0x7b, 0x7c, 0x78, 0xf3, 0xfd, 0x0c, 0x0f, 0xbd, 0x07, 0x45, 0xe8,
	0x41, 0xd3, 0x34, 0x81, 0x88, 0x80, 0xe4, 0x24, 0x48, 0x21, 0xa6, 0xbf, 0x05, 0xc3, 0x32, 0x15,
	0x5a, 0xd8, 0x26, 0x48, 0x3e, 0xfc, 0xc0, 0x84, 0x60, 0x11, 0x25, 0xc7, 0x96, 0x97, 0x05, 0x44,
	0xf3, 0x98, 0x2a, 0x0d, 0xb1, 0xac, 0xa8, 0x61, 0x8f, 0xe5, 0x84, 0xe5, 0x55, 0x31, 0xbe, 0x37,
	0x50, 0xff, 0xbf, 0x8c, 0x78, 0xb2, 0xff, 0x59, 0xcf, 0xb2, 0x3f, 0xa1, 0x8e, 0x3e, 0xb8, 0x3c,
	0x09, 0xc4, 0xc0, 0x18, 0x19, 0x93, 0xde, 0xcc, 0xc2, 0x2c, 0xc7, 0x15, 0xb4, 0xd9, 0xae, 0x92,
	0x40, 0x38, 0x6d, 0x7d, 0x28, 0xcf, 0x12, 0x4d, 0x6b, 0xb4, 0x35, 0x32, 0x4f, 0x51, 0xa7, 0x46,
	0xd3, 0x0a, 0x9d, 0x20, 0x4b, 0x86, 0x85, 0x2b, 0xa1, 0x88, 0x04, 0xf8, 0xee, 0x8d, 0x12, 0xc9,
	0xc0, 0x1c, 0x19, 0x93, 0xae, 0xd3, 0x97, 0x61, 0xb1, 0xae, 0xda, 0xbf, 0xfe, 0xfd, 0xfd, 0x63,
	0x7f, 0x43, 0xaf, 0x65, 0xe6, 0x45, 0x5c, 0x85, 0xd4, 0x77, 0x41, 0x0f, 0x5e, 0x1e, 0x43, 0x0c,
	0x71, 0xe5, 0x85, 0x1b, 0x2f, 0xbc, 0x69, 0xbc, 0x9c, 0xde, 0x23, 0xff, 0x43, 0x8f, 0xef, 0x0c,
	0x64, 0x2d, 0x45, 0x9e, 0x9c, 0x38, 0x7d, 0x39, 0x77, 0xb2, 0xcb, 0xa0, 0x0d, 0x76, 0x66, 0x75,
	0x29, 0x6a, 0xeb, 0x62, 0xd4, 0x77, 0x08, 0x31, 0xd0, 0x34, 0x87, 0xc2, 0xe5, 0x7e, 0xad, 0xd3,
	0xad, 0x3b, 0xab, 0xe5, 0x33, 0x4d, 0x3e, 0xbf, 0x45, 0xaf, 0x9c, 0xed, 0x15, 0x4f, 0x7c, 0x91,
	0xdb, 0x1d, 0x64, 0x3a, 0xdb, 0xaf, 0xd6, 0x8b, 0xea, 0x32, 0xb3, 0x8c, 0x45, 0x86, 0x3e, 0x72,
	0x81, 0x77, 0x21, 0x4f, 0xa5, 0xd2, 0xb0, 0xdb, 0x63, 0x90, 0x1c, 0x83, 0xc2, 0xcd, 0x82, 0x94,
	0xf5, 0xe2, 0x4d, 0xf3, 0x03, 0xeb, 0xf2, 0xad, 0xb5, 0x71, 0xfd, 0x9d, 0x71, 0x1d, 0x66, 0x1e,
	0xde, 0x89, 0x98, 0x28, 0x60, 0x90, 0x4e, 0x25, 0x68, 0x1a, 0x4d, 0x55, 0xa4, 0xc8, 0xd3, 0xac,
	0x69, 0xb9, 0x5c, 0x4c, 0x90, 0xdb, 0x39, 0x39, 0x5b, 0x39, 0xaf, 0x7d, 0x4c, 0x3d, 0x7f, 0x08,
	0x00, 0x00, 0xff, 0xff, 0xa1, 0x97, 0x39, 0x6a, 0x8c, 0x02, 0x00, 0x00,
}
