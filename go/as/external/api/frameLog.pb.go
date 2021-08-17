// Code generated by protoc-gen-go. DO NOT EDIT.
// source: as/external/api/frameLog.proto

package api

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "github.com/golang/protobuf/ptypes/duration"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
	_ "github.com/sagar-patel-sls/chirpstack-api/go/v3/common"
	gw "github.com/sagar-patel-sls/chirpstack-api/go/v3/gw"
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
	PublishedAt          *timestamp.Timestamp `protobuf:"bytes,4,opt,name=published_at,json=publishedAt,proto3" json:"published_at,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
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

func (m *UplinkFrameLog) GetPublishedAt() *timestamp.Timestamp {
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
	PublishedAt          *timestamp.Timestamp `protobuf:"bytes,4,opt,name=published_at,json=publishedAt,proto3" json:"published_at,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
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

func (m *DownlinkFrameLog) GetPublishedAt() *timestamp.Timestamp {
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
	// 400 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xa4, 0x92, 0xc1, 0x6f, 0xd3, 0x30,
	0x14, 0xc6, 0xc9, 0x8a, 0x36, 0xe6, 0xc2, 0x14, 0x85, 0x4b, 0x55, 0xc1, 0x28, 0x3b, 0x15, 0x50,
	0x6d, 0xb1, 0x9d, 0x11, 0x62, 0x9a, 0x90, 0x86, 0x10, 0x54, 0x61, 0x88, 0x8a, 0x4b, 0xf4, 0xda,
	0x38, 0x8e, 0x59, 0xe2, 0x67, 0xd9, 0x0e, 0x69, 0xfe, 0x42, 0x8e, 0xfc, 0x4b, 0x28, 0x75, 0x02,
	0x5a, 0xd4, 0x1b, 0xa7, 0xe7, 0xf7, 0xf9, 0x27, 0xfb, 0xfb, 0x9e, 0x1e, 0x39, 0x05, 0xcb, 0xf8,
	0xd6, 0x71, 0xa3, 0xa0, 0x60, 0xa0, 0x25, 0xcb, 0x0c, 0x94, 0xfc, 0x23, 0x0a, 0xaa, 0x0d, 0x3a,
	0x8c, 0x46, 0xa0, 0xe5, 0xf4, 0x99, 0x40, 0x14, 0x05, 0x67, 0x3b, 0x69, 0x5d, 0x65, 0xcc, 0xc9,
	0x92, 0x5b, 0x07, 0xa5, 0xf6, 0xd4, 0xf4, 0x74, 0x08, 0xa4, 0x95, 0x01, 0x27, 0x51, 0x75, 0xf7,
	0x8f, 0x37, 0x58, 0x96, 0xa8, 0x98, 0x2f, 0x9d, 0x38, 0x16, 0x35, 0x13, 0xb5, 0x6f, 0xce, 0x7e,
	0x07, 0xe4, 0xe4, 0xab, 0x2e, 0xa4, 0xba, 0x7d, 0xdf, 0x19, 0x88, 0x5e, 0x90, 0x23, 0xb7, 0x4d,
	0xa4, 0xca, 0x70, 0x12, 0xcc, 0x82, 0xf9, 0xf8, 0x3c, 0xa4, 0xa2, 0xa6, 0x1e, 0xba, 0x59, 0x5d,
	0xab, 0x0c, 0xe3, 0x43, 0xb7, 0x6d, 0x6b, 0x8b, 0x9a, 0x0e, 0x3d, 0x98, 0x8d, 0xee, 0xa2, 0x71,
	0x87, 0x1a, 0x8f, 0xce, 0x49, 0xa8, 0xf3, 0x26, 0xd1, 0xd0, 0x14, 0x08, 0x69, 0xf2, 0xc3, 0xa2,
	0x9a, 0x8c, 0x66, 0xc1, 0xfc, 0x38, 0x3e, 0xd1, 0x79, 0xb3, 0xf4, 0xf2, 0x87, 0x2f, 0x9f, 0x3f,
	0x45, 0x6f, 0xc8, 0x43, 0x5d, 0xad, 0x0b, 0x69, 0x73, 0x9e, 0x26, 0xe0, 0x26, 0xf7, 0x77, 0x26,
	0xa6, 0xd4, 0x67, 0xa5, 0x7d, 0x56, 0x7a, 0xd3, 0x0f, 0x23, 0x1e, 0xff, 0xe5, 0xdf, 0xb9, 0xb3,
	0x5f, 0x01, 0x09, 0xaf, 0xb0, 0x56, 0x77, 0x32, 0xbd, 0x1a, 0x66, 0x8a, 0x5a, 0xa3, 0x3d, 0x36,
	0x48, 0xb5, 0xcf, 0xea, 0xc1, 0x5e, 0xab, 0x4f, 0x09, 0x11, 0xe0, 0x78, 0x0d, 0x4d, 0x22, 0xd3,
	0x2e, 0xce, 0x71, 0xa7, 0x5c, 0x5f, 0xfd, 0x67, 0x92, 0x97, 0x4f, 0xc8, 0x83, 0x78, 0xf5, 0x4d,
	0xaa, 0x14, 0xeb, 0xe8, 0x88, 0x8c, 0xe2, 0xd5, 0xeb, 0xf0, 0x9e, 0x3f, 0x9c, 0x87, 0xc1, 0x65,
	0x45, 0x9e, 0x4b, 0xa4, 0x9b, 0x5c, 0x1a, 0x6d, 0x1d, 0x6c, 0x6e, 0x29, 0x68, 0x49, 0xc1, 0xd2,
	0x7e, 0xab, 0xda, 0xfe, 0xf2, 0x51, 0x3f, 0x81, 0x65, 0xfb, 0xd7, 0x32, 0xf8, 0xfe, 0x56, 0x48,
	0x97, 0x57, 0x6b, 0xba, 0xc1, 0x92, 0x59, 0x10, 0x60, 0x16, 0x1a, 0x1c, 0x2f, 0x16, 0xb6, 0xb0,
	0xec, 0xdf, 0x5b, 0x8b, 0x76, 0x23, 0x05, 0xb2, 0x9f, 0x17, 0x6c, 0xb0, 0xa7, 0xeb, 0xc3, 0x9d,
	0xeb, 0x8b, 0x3f, 0x01, 0x00, 0x00, 0xff, 0xff, 0xe0, 0x88, 0x1c, 0x28, 0xc1, 0x02, 0x00, 0x00,
}
