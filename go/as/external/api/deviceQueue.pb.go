// Code generated by protoc-gen-go. DO NOT EDIT.
// source: as/external/api/deviceQueue.proto

package api

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	empty "github.com/golang/protobuf/ptypes/empty"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
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

type DeviceQueueItem struct {
	// Device EUI (HEX encoded).
	DevEui string `protobuf:"bytes,1,opt,name=dev_eui,json=devEUI,proto3" json:"dev_eui,omitempty"`
	// Set this to true when an acknowledgement from the device is required.
	// Please note that this must not be used to guarantee a delivery.
	Confirmed bool `protobuf:"varint,2,opt,name=confirmed,proto3" json:"confirmed,omitempty"`
	// Downlink frame-counter.
	// This will be automatically set on enquue.
	FCnt uint32 `protobuf:"varint,6,opt,name=f_cnt,json=fCnt,proto3" json:"f_cnt,omitempty"`
	// FPort used (must be > 0)
	FPort uint32 `protobuf:"varint,3,opt,name=f_port,json=fPort,proto3" json:"f_port,omitempty"`
	// Base64 encoded data.
	// Or use the json_object field when an application codec has been configured.
	Data []byte `protobuf:"bytes,4,opt,name=data,proto3" json:"data,omitempty"`
	// JSON object (string).
	// Only use this when an application codec has been configured that can convert
	// this object into binary form.
	JsonObject           string   `protobuf:"bytes,5,opt,name=json_object,json=jsonObject,proto3" json:"json_object,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DeviceQueueItem) Reset()         { *m = DeviceQueueItem{} }
func (m *DeviceQueueItem) String() string { return proto.CompactTextString(m) }
func (*DeviceQueueItem) ProtoMessage()    {}
func (*DeviceQueueItem) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{0}
}

func (m *DeviceQueueItem) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DeviceQueueItem.Unmarshal(m, b)
}
func (m *DeviceQueueItem) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DeviceQueueItem.Marshal(b, m, deterministic)
}
func (m *DeviceQueueItem) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DeviceQueueItem.Merge(m, src)
}
func (m *DeviceQueueItem) XXX_Size() int {
	return xxx_messageInfo_DeviceQueueItem.Size(m)
}
func (m *DeviceQueueItem) XXX_DiscardUnknown() {
	xxx_messageInfo_DeviceQueueItem.DiscardUnknown(m)
}

var xxx_messageInfo_DeviceQueueItem proto.InternalMessageInfo

func (m *DeviceQueueItem) GetDevEui() string {
	if m != nil {
		return m.DevEui
	}
	return ""
}

func (m *DeviceQueueItem) GetConfirmed() bool {
	if m != nil {
		return m.Confirmed
	}
	return false
}

func (m *DeviceQueueItem) GetFCnt() uint32 {
	if m != nil {
		return m.FCnt
	}
	return 0
}

func (m *DeviceQueueItem) GetFPort() uint32 {
	if m != nil {
		return m.FPort
	}
	return 0
}

func (m *DeviceQueueItem) GetData() []byte {
	if m != nil {
		return m.Data
	}
	return nil
}

func (m *DeviceQueueItem) GetJsonObject() string {
	if m != nil {
		return m.JsonObject
	}
	return ""
}

type EnqueueDeviceQueueItemRequest struct {
	// Queue-item object to enqueue.
	DeviceQueueItem      *DeviceQueueItem `protobuf:"bytes,1,opt,name=device_queue_item,json=deviceQueueItem,proto3" json:"device_queue_item,omitempty"`
	XXX_NoUnkeyedLiteral struct{}         `json:"-"`
	XXX_unrecognized     []byte           `json:"-"`
	XXX_sizecache        int32            `json:"-"`
}

func (m *EnqueueDeviceQueueItemRequest) Reset()         { *m = EnqueueDeviceQueueItemRequest{} }
func (m *EnqueueDeviceQueueItemRequest) String() string { return proto.CompactTextString(m) }
func (*EnqueueDeviceQueueItemRequest) ProtoMessage()    {}
func (*EnqueueDeviceQueueItemRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{1}
}

func (m *EnqueueDeviceQueueItemRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_EnqueueDeviceQueueItemRequest.Unmarshal(m, b)
}
func (m *EnqueueDeviceQueueItemRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_EnqueueDeviceQueueItemRequest.Marshal(b, m, deterministic)
}
func (m *EnqueueDeviceQueueItemRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_EnqueueDeviceQueueItemRequest.Merge(m, src)
}
func (m *EnqueueDeviceQueueItemRequest) XXX_Size() int {
	return xxx_messageInfo_EnqueueDeviceQueueItemRequest.Size(m)
}
func (m *EnqueueDeviceQueueItemRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_EnqueueDeviceQueueItemRequest.DiscardUnknown(m)
}

var xxx_messageInfo_EnqueueDeviceQueueItemRequest proto.InternalMessageInfo

func (m *EnqueueDeviceQueueItemRequest) GetDeviceQueueItem() *DeviceQueueItem {
	if m != nil {
		return m.DeviceQueueItem
	}
	return nil
}

type EnqueueDeviceQueueItemResponse struct {
	// Frame-counter for the enqueued payload.
	FCnt                 uint32   `protobuf:"varint,1,opt,name=f_cnt,json=fCnt,proto3" json:"f_cnt,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *EnqueueDeviceQueueItemResponse) Reset()         { *m = EnqueueDeviceQueueItemResponse{} }
func (m *EnqueueDeviceQueueItemResponse) String() string { return proto.CompactTextString(m) }
func (*EnqueueDeviceQueueItemResponse) ProtoMessage()    {}
func (*EnqueueDeviceQueueItemResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{2}
}

func (m *EnqueueDeviceQueueItemResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_EnqueueDeviceQueueItemResponse.Unmarshal(m, b)
}
func (m *EnqueueDeviceQueueItemResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_EnqueueDeviceQueueItemResponse.Marshal(b, m, deterministic)
}
func (m *EnqueueDeviceQueueItemResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_EnqueueDeviceQueueItemResponse.Merge(m, src)
}
func (m *EnqueueDeviceQueueItemResponse) XXX_Size() int {
	return xxx_messageInfo_EnqueueDeviceQueueItemResponse.Size(m)
}
func (m *EnqueueDeviceQueueItemResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_EnqueueDeviceQueueItemResponse.DiscardUnknown(m)
}

var xxx_messageInfo_EnqueueDeviceQueueItemResponse proto.InternalMessageInfo

func (m *EnqueueDeviceQueueItemResponse) GetFCnt() uint32 {
	if m != nil {
		return m.FCnt
	}
	return 0
}

type FlushDeviceQueueRequest struct {
	// Device EUI (HEX encoded).
	DevEui               string   `protobuf:"bytes,1,opt,name=dev_eui,json=devEUI,proto3" json:"dev_eui,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *FlushDeviceQueueRequest) Reset()         { *m = FlushDeviceQueueRequest{} }
func (m *FlushDeviceQueueRequest) String() string { return proto.CompactTextString(m) }
func (*FlushDeviceQueueRequest) ProtoMessage()    {}
func (*FlushDeviceQueueRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{3}
}

func (m *FlushDeviceQueueRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_FlushDeviceQueueRequest.Unmarshal(m, b)
}
func (m *FlushDeviceQueueRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_FlushDeviceQueueRequest.Marshal(b, m, deterministic)
}
func (m *FlushDeviceQueueRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_FlushDeviceQueueRequest.Merge(m, src)
}
func (m *FlushDeviceQueueRequest) XXX_Size() int {
	return xxx_messageInfo_FlushDeviceQueueRequest.Size(m)
}
func (m *FlushDeviceQueueRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_FlushDeviceQueueRequest.DiscardUnknown(m)
}

var xxx_messageInfo_FlushDeviceQueueRequest proto.InternalMessageInfo

func (m *FlushDeviceQueueRequest) GetDevEui() string {
	if m != nil {
		return m.DevEui
	}
	return ""
}

type ListDeviceQueueItemsRequest struct {
	// Device EUI (HEX encoded).
	DevEui string `protobuf:"bytes,1,opt,name=dev_eui,json=devEUI,proto3" json:"dev_eui,omitempty"`
	// Return only the count, not the result-set.
	CountOnly            bool     `protobuf:"varint,2,opt,name=count_only,json=countOnly,proto3" json:"count_only,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ListDeviceQueueItemsRequest) Reset()         { *m = ListDeviceQueueItemsRequest{} }
func (m *ListDeviceQueueItemsRequest) String() string { return proto.CompactTextString(m) }
func (*ListDeviceQueueItemsRequest) ProtoMessage()    {}
func (*ListDeviceQueueItemsRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{4}
}

func (m *ListDeviceQueueItemsRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ListDeviceQueueItemsRequest.Unmarshal(m, b)
}
func (m *ListDeviceQueueItemsRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ListDeviceQueueItemsRequest.Marshal(b, m, deterministic)
}
func (m *ListDeviceQueueItemsRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ListDeviceQueueItemsRequest.Merge(m, src)
}
func (m *ListDeviceQueueItemsRequest) XXX_Size() int {
	return xxx_messageInfo_ListDeviceQueueItemsRequest.Size(m)
}
func (m *ListDeviceQueueItemsRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_ListDeviceQueueItemsRequest.DiscardUnknown(m)
}

var xxx_messageInfo_ListDeviceQueueItemsRequest proto.InternalMessageInfo

func (m *ListDeviceQueueItemsRequest) GetDevEui() string {
	if m != nil {
		return m.DevEui
	}
	return ""
}

func (m *ListDeviceQueueItemsRequest) GetCountOnly() bool {
	if m != nil {
		return m.CountOnly
	}
	return false
}

type ListDeviceQueueItemsResponse struct {
	// The device queue items.
	DeviceQueueItems []*DeviceQueueItem `protobuf:"bytes,1,rep,name=device_queue_items,json=deviceQueueItems,proto3" json:"device_queue_items,omitempty"`
	// Total number of items in the queue.
	TotalCount           uint32   `protobuf:"varint,2,opt,name=total_count,json=totalCount,proto3" json:"total_count,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ListDeviceQueueItemsResponse) Reset()         { *m = ListDeviceQueueItemsResponse{} }
func (m *ListDeviceQueueItemsResponse) String() string { return proto.CompactTextString(m) }
func (*ListDeviceQueueItemsResponse) ProtoMessage()    {}
func (*ListDeviceQueueItemsResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{5}
}

func (m *ListDeviceQueueItemsResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ListDeviceQueueItemsResponse.Unmarshal(m, b)
}
func (m *ListDeviceQueueItemsResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ListDeviceQueueItemsResponse.Marshal(b, m, deterministic)
}
func (m *ListDeviceQueueItemsResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ListDeviceQueueItemsResponse.Merge(m, src)
}
func (m *ListDeviceQueueItemsResponse) XXX_Size() int {
	return xxx_messageInfo_ListDeviceQueueItemsResponse.Size(m)
}
func (m *ListDeviceQueueItemsResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ListDeviceQueueItemsResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ListDeviceQueueItemsResponse proto.InternalMessageInfo

func (m *ListDeviceQueueItemsResponse) GetDeviceQueueItems() []*DeviceQueueItem {
	if m != nil {
		return m.DeviceQueueItems
	}
	return nil
}

func (m *ListDeviceQueueItemsResponse) GetTotalCount() uint32 {
	if m != nil {
		return m.TotalCount
	}
	return 0
}

func init() {
	proto.RegisterType((*DeviceQueueItem)(nil), "api.DeviceQueueItem")
	proto.RegisterType((*EnqueueDeviceQueueItemRequest)(nil), "api.EnqueueDeviceQueueItemRequest")
	proto.RegisterType((*EnqueueDeviceQueueItemResponse)(nil), "api.EnqueueDeviceQueueItemResponse")
	proto.RegisterType((*FlushDeviceQueueRequest)(nil), "api.FlushDeviceQueueRequest")
	proto.RegisterType((*ListDeviceQueueItemsRequest)(nil), "api.ListDeviceQueueItemsRequest")
	proto.RegisterType((*ListDeviceQueueItemsResponse)(nil), "api.ListDeviceQueueItemsResponse")
}

func init() {
	proto.RegisterFile("as/external/api/deviceQueue.proto", fileDescriptor_6bc7c26115164240)
}

var fileDescriptor_6bc7c26115164240 = []byte{
	// 556 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x84, 0x54, 0x4d, 0x6f, 0xd3, 0x40,
	0x10, 0x95, 0xf3, 0x55, 0x3a, 0xa5, 0x2a, 0x2c, 0x85, 0x5a, 0x69, 0x5a, 0x5c, 0xc3, 0x21, 0xaa,
	0x84, 0x2d, 0x25, 0x42, 0x08, 0x4e, 0xa8, 0x25, 0x48, 0x95, 0x90, 0x02, 0x46, 0xbd, 0x70, 0xb1,
	0x36, 0xf6, 0x3a, 0xd9, 0xe2, 0xec, 0x3a, 0xde, 0x71, 0x44, 0x84, 0xb8, 0xc0, 0x99, 0x13, 0xbf,
	0x82, 0xdf, 0xc3, 0x5f, 0xe0, 0x67, 0x70, 0x40, 0xde, 0xb8, 0x72, 0x48, 0x48, 0x7a, 0x5b, 0xbf,
	0x9d, 0x9d, 0x37, 0xef, 0x3d, 0x8d, 0xe1, 0x84, 0x2a, 0x97, 0x7d, 0x42, 0x96, 0x0a, 0x1a, 0xbb,
	0x34, 0xe1, 0x6e, 0xc8, 0xa6, 0x3c, 0x60, 0xef, 0x32, 0x96, 0x31, 0x27, 0x49, 0x25, 0x4a, 0x52,
	0xa5, 0x09, 0x6f, 0xb6, 0x86, 0x52, 0x0e, 0x63, 0xa6, 0x4b, 0xa8, 0x10, 0x12, 0x29, 0x72, 0x29,
	0xd4, 0xbc, 0xa4, 0x79, 0x58, 0xdc, 0xea, 0xaf, 0x41, 0x16, 0xb9, 0x6c, 0x9c, 0xe0, 0x6c, 0x7e,
	0x69, 0xff, 0x34, 0x60, 0xef, 0x55, 0xd9, 0xf5, 0x02, 0xd9, 0x98, 0x1c, 0xc0, 0x56, 0xc8, 0xa6,
	0x3e, 0xcb, 0xb8, 0x69, 0x58, 0x46, 0x7b, 0xdb, 0x6b, 0x84, 0x6c, 0xda, 0xbb, 0xbc, 0x20, 0x2d,
	0xd8, 0x0e, 0xa4, 0x88, 0x78, 0x3a, 0x66, 0xa1, 0x59, 0xb1, 0x8c, 0xf6, 0x2d, 0xaf, 0x04, 0xc8,
	0x3d, 0xa8, 0x47, 0x7e, 0x20, 0xd0, 0x6c, 0x58, 0x46, 0x7b, 0xd7, 0xab, 0x45, 0xe7, 0x02, 0xc9,
	0x7d, 0x68, 0x44, 0x7e, 0x22, 0x53, 0x34, 0xab, 0x1a, 0xad, 0x47, 0x6f, 0x65, 0x8a, 0x84, 0x40,
	0x2d, 0xa4, 0x48, 0xcd, 0x9a, 0x65, 0xb4, 0x6f, 0x7b, 0xfa, 0x4c, 0x1e, 0xc2, 0xce, 0x95, 0x92,
	0xc2, 0x97, 0x83, 0x2b, 0x16, 0xa0, 0x59, 0xd7, 0xd4, 0x90, 0x43, 0x7d, 0x8d, 0xd8, 0x14, 0x8e,
	0x7a, 0x62, 0x92, 0x8f, 0xb9, 0x34, 0xb1, 0xc7, 0x26, 0x19, 0x53, 0x48, 0x5e, 0xc2, 0xdd, 0xb9,
	0x43, 0xbe, 0xae, 0xf2, 0x39, 0xb2, 0xb1, 0x96, 0xb0, 0xd3, 0xd9, 0x77, 0x68, 0xc2, 0x9d, 0xe5,
	0x77, 0x7b, 0xe1, 0xbf, 0x80, 0xfd, 0x14, 0x8e, 0xd7, 0x51, 0xa8, 0x44, 0x0a, 0xc5, 0x4a, 0x95,
	0x46, 0xa9, 0xd2, 0xee, 0xc0, 0xc1, 0xeb, 0x38, 0x53, 0xa3, 0x85, 0x47, 0xd7, 0x33, 0xad, 0x33,
	0xd3, 0xbe, 0x84, 0xc3, 0x37, 0x5c, 0xe1, 0x12, 0x8f, 0xba, 0xe9, 0x1d, 0x39, 0x02, 0x08, 0x64,
	0x26, 0xd0, 0x97, 0x22, 0x9e, 0x95, 0x29, 0x64, 0x02, 0xfb, 0x22, 0x9e, 0xd9, 0xdf, 0x0c, 0x68,
	0xfd, 0xbf, 0x6f, 0x21, 0xe0, 0x0c, 0xc8, 0x8a, 0x49, 0xca, 0x34, 0xac, 0xea, 0x5a, 0x97, 0xee,
	0x2c, 0xb9, 0xa4, 0xf2, 0xa8, 0x50, 0x22, 0x8d, 0x7d, 0xcd, 0xab, 0x87, 0xd8, 0xf5, 0x40, 0x43,
	0xe7, 0x39, 0xd2, 0xf9, 0x53, 0x01, 0xb2, 0xd0, 0xe6, 0x3d, 0x4b, 0xf3, 0x33, 0xf9, 0x6e, 0xc0,
	0x56, 0xe1, 0x2f, 0xb1, 0x35, 0xd7, 0xc6, 0x40, 0x9b, 0x8f, 0x36, 0xd6, 0xcc, 0x05, 0xd9, 0xcf,
	0xbf, 0xfe, 0xfa, 0xfd, 0xa3, 0xd2, 0xb5, 0x9d, 0x85, 0x15, 0x51, 0xee, 0xe7, 0x15, 0x91, 0x4e,
	0xe1, 0xe7, 0x17, 0x57, 0x63, 0x2f, 0x8c, 0x53, 0x12, 0x40, 0x5d, 0xe7, 0x46, 0x5a, 0x9a, 0x68,
	0x4d, 0x86, 0xcd, 0x07, 0xce, 0x7c, 0x85, 0x9c, 0xeb, 0x15, 0x72, 0x7a, 0xf9, 0x0a, 0xd9, 0x8f,
	0x35, 0xf3, 0xf1, 0x69, 0x6b, 0x85, 0x79, 0x81, 0x87, 0x4c, 0xa0, 0x96, 0x07, 0x42, 0x2c, 0xcd,
	0xb1, 0x21, 0xf3, 0xe6, 0xc9, 0x86, 0x8a, 0x42, 0x6c, 0x41, 0x49, 0x36, 0x52, 0x9e, 0xf5, 0x61,
	0x9f, 0x4b, 0x27, 0x18, 0xf1, 0x34, 0x51, 0x48, 0x83, 0x8f, 0xba, 0x2f, 0x55, 0x1f, 0x9e, 0x0d,
	0x39, 0x8e, 0xb2, 0x81, 0x13, 0xc8, 0xb1, 0x3b, 0x48, 0x65, 0x40, 0x69, 0xea, 0x96, 0x55, 0x4f,
	0xf2, 0x96, 0x43, 0xe9, 0x4e, 0xbb, 0xee, 0xd2, 0x8f, 0x67, 0xd0, 0xd0, 0xca, 0xbb, 0x7f, 0x03,
	0x00, 0x00, 0xff, 0xff, 0xb0, 0xf9, 0x32, 0x75, 0x92, 0x04, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// DeviceQueueServiceClient is the client API for DeviceQueueService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type DeviceQueueServiceClient interface {
	// Enqueue adds the given item to the device-queue.
	Enqueue(ctx context.Context, in *EnqueueDeviceQueueItemRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueItemResponse, error)
	// Flush flushes the downlink device-queue.
	Flush(ctx context.Context, in *FlushDeviceQueueRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	// List lists the items in the device-queue.
	List(ctx context.Context, in *ListDeviceQueueItemsRequest, opts ...grpc.CallOption) (*ListDeviceQueueItemsResponse, error)
}

type deviceQueueServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewDeviceQueueServiceClient(cc grpc.ClientConnInterface) DeviceQueueServiceClient {
	return &deviceQueueServiceClient{cc}
}

func (c *deviceQueueServiceClient) Enqueue(ctx context.Context, in *EnqueueDeviceQueueItemRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueItemResponse, error) {
	out := new(EnqueueDeviceQueueItemResponse)
	err := c.cc.Invoke(ctx, "/api.DeviceQueueService/Enqueue", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *deviceQueueServiceClient) Flush(ctx context.Context, in *FlushDeviceQueueRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, "/api.DeviceQueueService/Flush", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *deviceQueueServiceClient) List(ctx context.Context, in *ListDeviceQueueItemsRequest, opts ...grpc.CallOption) (*ListDeviceQueueItemsResponse, error) {
	out := new(ListDeviceQueueItemsResponse)
	err := c.cc.Invoke(ctx, "/api.DeviceQueueService/List", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DeviceQueueServiceServer is the server API for DeviceQueueService service.
type DeviceQueueServiceServer interface {
	// Enqueue adds the given item to the device-queue.
	Enqueue(context.Context, *EnqueueDeviceQueueItemRequest) (*EnqueueDeviceQueueItemResponse, error)
	// Flush flushes the downlink device-queue.
	Flush(context.Context, *FlushDeviceQueueRequest) (*empty.Empty, error)
	// List lists the items in the device-queue.
	List(context.Context, *ListDeviceQueueItemsRequest) (*ListDeviceQueueItemsResponse, error)
}

// UnimplementedDeviceQueueServiceServer can be embedded to have forward compatible implementations.
type UnimplementedDeviceQueueServiceServer struct {
}

func (*UnimplementedDeviceQueueServiceServer) Enqueue(ctx context.Context, req *EnqueueDeviceQueueItemRequest) (*EnqueueDeviceQueueItemResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Enqueue not implemented")
}
func (*UnimplementedDeviceQueueServiceServer) Flush(ctx context.Context, req *FlushDeviceQueueRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Flush not implemented")
}
func (*UnimplementedDeviceQueueServiceServer) List(ctx context.Context, req *ListDeviceQueueItemsRequest) (*ListDeviceQueueItemsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}

func RegisterDeviceQueueServiceServer(s *grpc.Server, srv DeviceQueueServiceServer) {
	s.RegisterService(&_DeviceQueueService_serviceDesc, srv)
}

func _DeviceQueueService_Enqueue_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EnqueueDeviceQueueItemRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DeviceQueueServiceServer).Enqueue(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/api.DeviceQueueService/Enqueue",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DeviceQueueServiceServer).Enqueue(ctx, req.(*EnqueueDeviceQueueItemRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DeviceQueueService_Flush_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FlushDeviceQueueRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DeviceQueueServiceServer).Flush(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/api.DeviceQueueService/Flush",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DeviceQueueServiceServer).Flush(ctx, req.(*FlushDeviceQueueRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DeviceQueueService_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListDeviceQueueItemsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DeviceQueueServiceServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/api.DeviceQueueService/List",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DeviceQueueServiceServer).List(ctx, req.(*ListDeviceQueueItemsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _DeviceQueueService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "api.DeviceQueueService",
	HandlerType: (*DeviceQueueServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Enqueue",
			Handler:    _DeviceQueueService_Enqueue_Handler,
		},
		{
			MethodName: "Flush",
			Handler:    _DeviceQueueService_Flush_Handler,
		},
		{
			MethodName: "List",
			Handler:    _DeviceQueueService_List_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "as/external/api/deviceQueue.proto",
}
