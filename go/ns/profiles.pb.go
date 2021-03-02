// Code generated by protoc-gen-go. DO NOT EDIT.
// source: ns/profiles.proto

package ns

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
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

type RatePolicy int32

const (
	// Drop
	RatePolicy_DROP RatePolicy = 0
	// Mark
	RatePolicy_MARK RatePolicy = 1
)

var RatePolicy_name = map[int32]string{
	0: "DROP",
	1: "MARK",
}

var RatePolicy_value = map[string]int32{
	"DROP": 0,
	"MARK": 1,
}

func (x RatePolicy) String() string {
	return proto.EnumName(RatePolicy_name, int32(x))
}

func (RatePolicy) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_ee79be696a10f18b, []int{0}
}

type ServiceProfile struct {
	// Service-profile ID.
	Id []byte `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// Token bucket filling rate, including ACKs (packet/h).
	UlRate uint32 `protobuf:"varint,2,opt,name=ul_rate,json=ulRate,proto3" json:"ul_rate,omitempty"`
	// Token bucket burst size.
	UlBucketSize uint32 `protobuf:"varint,3,opt,name=ul_bucket_size,json=ulBucketSize,proto3" json:"ul_bucket_size,omitempty"`
	// Drop or mark when exceeding ULRate.
	UlRatePolicy RatePolicy `protobuf:"varint,4,opt,name=ul_rate_policy,json=ulRatePolicy,proto3,enum=ns.RatePolicy" json:"ul_rate_policy,omitempty"`
	// Token bucket filling rate, including ACKs (packet/h).
	DlRate uint32 `protobuf:"varint,5,opt,name=dl_rate,json=dlRate,proto3" json:"dl_rate,omitempty"`
	// Token bucket burst size.
	DlBucketSize uint32 `protobuf:"varint,6,opt,name=dl_bucket_size,json=dlBucketSize,proto3" json:"dl_bucket_size,omitempty"`
	// Drop or mark when exceeding DLRate.
	DlRatePolicy RatePolicy `protobuf:"varint,7,opt,name=dl_rate_policy,json=dlRatePolicy,proto3,enum=ns.RatePolicy" json:"dl_rate_policy,omitempty"`
	// GW metadata (RSSI, SNR, GW geoloc., etc.) are added to the packet sent to AS.
	AddGwMetadata bool `protobuf:"varint,8,opt,name=add_gw_metadata,json=addGwMetadata,proto3" json:"add_gw_metadata,omitempty"`
	// Frequency to initiate an End-Device status request (request/day).
	DevStatusReqFreq uint32 `protobuf:"varint,9,opt,name=dev_status_req_freq,json=devStatusReqFreq,proto3" json:"dev_status_req_freq,omitempty"`
	// Report End-Device battery level to AS.
	ReportDevStatusBattery bool `protobuf:"varint,10,opt,name=report_dev_status_battery,json=reportDevStatusBattery,proto3" json:"report_dev_status_battery,omitempty"`
	// Report End-Device margin to AS.
	ReportDevStatusMargin bool `protobuf:"varint,11,opt,name=report_dev_status_margin,json=reportDevStatusMargin,proto3" json:"report_dev_status_margin,omitempty"`
	// Minimum allowed data rate. Used for ADR.
	DrMin uint32 `protobuf:"varint,12,opt,name=dr_min,json=drMin,proto3" json:"dr_min,omitempty"`
	// Maximum allowed data rate. Used for ADR.
	DrMax uint32 `protobuf:"varint,13,opt,name=dr_max,json=drMax,proto3" json:"dr_max,omitempty"`
	// Channel mask. sNS does not have to obey (i.e., informative).
	ChannelMask []byte `protobuf:"bytes,14,opt,name=channel_mask,json=channelMask,proto3" json:"channel_mask,omitempty"`
	// Passive Roaming allowed.
	PrAllowed bool `protobuf:"varint,15,opt,name=pr_allowed,json=prAllowed,proto3" json:"pr_allowed,omitempty"`
	// Handover Roaming allowed.
	HrAllowed bool `protobuf:"varint,16,opt,name=hr_allowed,json=hrAllowed,proto3" json:"hr_allowed,omitempty"`
	// Roaming Activation allowed.
	RaAllowed bool `protobuf:"varint,17,opt,name=ra_allowed,json=raAllowed,proto3" json:"ra_allowed,omitempty"`
	// Enable network geolocation service.
	NwkGeoLoc bool `protobuf:"varint,18,opt,name=nwk_geo_loc,json=nwkGeoLoc,proto3" json:"nwk_geo_loc,omitempty"`
	// Target Packet Error Rate.
	TargetPer uint32 `protobuf:"varint,19,opt,name=target_per,json=targetPer,proto3" json:"target_per,omitempty"`
	// Minimum number of receiving GWs (informative).
	MinGwDiversity       uint32   `protobuf:"varint,20,opt,name=min_gw_diversity,json=minGwDiversity,proto3" json:"min_gw_diversity,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ServiceProfile) Reset()         { *m = ServiceProfile{} }
func (m *ServiceProfile) String() string { return proto.CompactTextString(m) }
func (*ServiceProfile) ProtoMessage()    {}
func (*ServiceProfile) Descriptor() ([]byte, []int) {
	return fileDescriptor_ee79be696a10f18b, []int{0}
}

func (m *ServiceProfile) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ServiceProfile.Unmarshal(m, b)
}
func (m *ServiceProfile) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ServiceProfile.Marshal(b, m, deterministic)
}
func (m *ServiceProfile) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ServiceProfile.Merge(m, src)
}
func (m *ServiceProfile) XXX_Size() int {
	return xxx_messageInfo_ServiceProfile.Size(m)
}
func (m *ServiceProfile) XXX_DiscardUnknown() {
	xxx_messageInfo_ServiceProfile.DiscardUnknown(m)
}

var xxx_messageInfo_ServiceProfile proto.InternalMessageInfo

func (m *ServiceProfile) GetId() []byte {
	if m != nil {
		return m.Id
	}
	return nil
}

func (m *ServiceProfile) GetUlRate() uint32 {
	if m != nil {
		return m.UlRate
	}
	return 0
}

func (m *ServiceProfile) GetUlBucketSize() uint32 {
	if m != nil {
		return m.UlBucketSize
	}
	return 0
}

func (m *ServiceProfile) GetUlRatePolicy() RatePolicy {
	if m != nil {
		return m.UlRatePolicy
	}
	return RatePolicy_DROP
}

func (m *ServiceProfile) GetDlRate() uint32 {
	if m != nil {
		return m.DlRate
	}
	return 0
}

func (m *ServiceProfile) GetDlBucketSize() uint32 {
	if m != nil {
		return m.DlBucketSize
	}
	return 0
}

func (m *ServiceProfile) GetDlRatePolicy() RatePolicy {
	if m != nil {
		return m.DlRatePolicy
	}
	return RatePolicy_DROP
}

func (m *ServiceProfile) GetAddGwMetadata() bool {
	if m != nil {
		return m.AddGwMetadata
	}
	return false
}

func (m *ServiceProfile) GetDevStatusReqFreq() uint32 {
	if m != nil {
		return m.DevStatusReqFreq
	}
	return 0
}

func (m *ServiceProfile) GetReportDevStatusBattery() bool {
	if m != nil {
		return m.ReportDevStatusBattery
	}
	return false
}

func (m *ServiceProfile) GetReportDevStatusMargin() bool {
	if m != nil {
		return m.ReportDevStatusMargin
	}
	return false
}

func (m *ServiceProfile) GetDrMin() uint32 {
	if m != nil {
		return m.DrMin
	}
	return 0
}

func (m *ServiceProfile) GetDrMax() uint32 {
	if m != nil {
		return m.DrMax
	}
	return 0
}

func (m *ServiceProfile) GetChannelMask() []byte {
	if m != nil {
		return m.ChannelMask
	}
	return nil
}

func (m *ServiceProfile) GetPrAllowed() bool {
	if m != nil {
		return m.PrAllowed
	}
	return false
}

func (m *ServiceProfile) GetHrAllowed() bool {
	if m != nil {
		return m.HrAllowed
	}
	return false
}

func (m *ServiceProfile) GetRaAllowed() bool {
	if m != nil {
		return m.RaAllowed
	}
	return false
}

func (m *ServiceProfile) GetNwkGeoLoc() bool {
	if m != nil {
		return m.NwkGeoLoc
	}
	return false
}

func (m *ServiceProfile) GetTargetPer() uint32 {
	if m != nil {
		return m.TargetPer
	}
	return 0
}

func (m *ServiceProfile) GetMinGwDiversity() uint32 {
	if m != nil {
		return m.MinGwDiversity
	}
	return 0
}

type DeviceProfile struct {
	// Device-profile ID.
	Id []byte `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// End-Device supports Class B.
	SupportsClassB bool `protobuf:"varint,2,opt,name=supports_class_b,json=supportsClassB,proto3" json:"supports_class_b,omitempty"`
	// Maximum delay for the End-Device to answer a MAC request or a confirmed DL frame (mandatory if class B mode supported).
	ClassBTimeout uint32 `protobuf:"varint,3,opt,name=class_b_timeout,json=classBTimeout,proto3" json:"class_b_timeout,omitempty"`
	// Mandatory if class B mode supported.
	PingSlotPeriod uint32 `protobuf:"varint,4,opt,name=ping_slot_period,json=pingSlotPeriod,proto3" json:"ping_slot_period,omitempty"`
	// Mandatory if class B mode supported.
	PingSlotDr uint32 `protobuf:"varint,5,opt,name=ping_slot_dr,json=pingSlotDr,proto3" json:"ping_slot_dr,omitempty"`
	// Mandatory if class B mode supported.
	PingSlotFreq uint32 `protobuf:"varint,6,opt,name=ping_slot_freq,json=pingSlotFreq,proto3" json:"ping_slot_freq,omitempty"`
	// End-Device supports Class C.
	SupportsClassC bool `protobuf:"varint,7,opt,name=supports_class_c,json=supportsClassC,proto3" json:"supports_class_c,omitempty"`
	// Maximum delay for the End-Device to answer a MAC request or a confirmed DL frame (mandatory if class C mode supported).
	ClassCTimeout uint32 `protobuf:"varint,8,opt,name=class_c_timeout,json=classCTimeout,proto3" json:"class_c_timeout,omitempty"`
	// Version of the LoRaWAN supported by the End-Device.
	MacVersion string `protobuf:"bytes,9,opt,name=mac_version,json=macVersion,proto3" json:"mac_version,omitempty"`
	// Revision of the Regional Parameters document supported by the End-Device.
	RegParamsRevision string `protobuf:"bytes,10,opt,name=reg_params_revision,json=regParamsRevision,proto3" json:"reg_params_revision,omitempty"`
	// Class A RX1 delay (mandatory for ABP).
	RxDelay_1 uint32 `protobuf:"varint,11,opt,name=rx_delay_1,json=rxDelay1,proto3" json:"rx_delay_1,omitempty"`
	// RX1 data rate offset (mandatory for ABP).
	RxDrOffset_1 uint32 `protobuf:"varint,12,opt,name=rx_dr_offset_1,json=rxDrOffset1,proto3" json:"rx_dr_offset_1,omitempty"`
	// RX2 data rate (mandatory for ABP).
	RxDatarate_2 uint32 `protobuf:"varint,13,opt,name=rx_datarate_2,json=rxDatarate2,proto3" json:"rx_datarate_2,omitempty"`
	// RX2 channel frequency (mandatory for ABP).
	RxFreq_2 uint32 `protobuf:"varint,14,opt,name=rx_freq_2,json=rxFreq2,proto3" json:"rx_freq_2,omitempty"`
	// List of factory-preset frequencies (mandatory for ABP).
	FactoryPresetFreqs []uint32 `protobuf:"varint,15,rep,packed,name=factory_preset_freqs,json=factoryPresetFreqs,proto3" json:"factory_preset_freqs,omitempty"`
	// Maximum EIRP supported by the End-Device.
	MaxEirp uint32 `protobuf:"varint,16,opt,name=max_eirp,json=maxEirp,proto3" json:"max_eirp,omitempty"`
	// Maximum duty cycle supported by the End-Device.
	MaxDutyCycle uint32 `protobuf:"varint,17,opt,name=max_duty_cycle,json=maxDutyCycle,proto3" json:"max_duty_cycle,omitempty"`
	// End-Device supports Join (OTAA) or not (ABP).
	SupportsJoin bool `protobuf:"varint,18,opt,name=supports_join,json=supportsJoin,proto3" json:"supports_join,omitempty"`
	// RF region name.
	RfRegion string `protobuf:"bytes,19,opt,name=rf_region,json=rfRegion,proto3" json:"rf_region,omitempty"`
	// End-Device uses 32bit FCnt (mandatory for LoRaWAN 1.0 End-Device).
	Supports_32BitFCnt   bool     `protobuf:"varint,20,opt,name=supports_32bit_f_cnt,json=supports32bitFCnt,proto3" json:"supports_32bit_f_cnt,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DeviceProfile) Reset()         { *m = DeviceProfile{} }
func (m *DeviceProfile) String() string { return proto.CompactTextString(m) }
func (*DeviceProfile) ProtoMessage()    {}
func (*DeviceProfile) Descriptor() ([]byte, []int) {
	return fileDescriptor_ee79be696a10f18b, []int{1}
}

func (m *DeviceProfile) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DeviceProfile.Unmarshal(m, b)
}
func (m *DeviceProfile) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DeviceProfile.Marshal(b, m, deterministic)
}
func (m *DeviceProfile) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DeviceProfile.Merge(m, src)
}
func (m *DeviceProfile) XXX_Size() int {
	return xxx_messageInfo_DeviceProfile.Size(m)
}
func (m *DeviceProfile) XXX_DiscardUnknown() {
	xxx_messageInfo_DeviceProfile.DiscardUnknown(m)
}

var xxx_messageInfo_DeviceProfile proto.InternalMessageInfo

func (m *DeviceProfile) GetId() []byte {
	if m != nil {
		return m.Id
	}
	return nil
}

func (m *DeviceProfile) GetSupportsClassB() bool {
	if m != nil {
		return m.SupportsClassB
	}
	return false
}

func (m *DeviceProfile) GetClassBTimeout() uint32 {
	if m != nil {
		return m.ClassBTimeout
	}
	return 0
}

func (m *DeviceProfile) GetPingSlotPeriod() uint32 {
	if m != nil {
		return m.PingSlotPeriod
	}
	return 0
}

func (m *DeviceProfile) GetPingSlotDr() uint32 {
	if m != nil {
		return m.PingSlotDr
	}
	return 0
}

func (m *DeviceProfile) GetPingSlotFreq() uint32 {
	if m != nil {
		return m.PingSlotFreq
	}
	return 0
}

func (m *DeviceProfile) GetSupportsClassC() bool {
	if m != nil {
		return m.SupportsClassC
	}
	return false
}

func (m *DeviceProfile) GetClassCTimeout() uint32 {
	if m != nil {
		return m.ClassCTimeout
	}
	return 0
}

func (m *DeviceProfile) GetMacVersion() string {
	if m != nil {
		return m.MacVersion
	}
	return ""
}

func (m *DeviceProfile) GetRegParamsRevision() string {
	if m != nil {
		return m.RegParamsRevision
	}
	return ""
}

func (m *DeviceProfile) GetRxDelay_1() uint32 {
	if m != nil {
		return m.RxDelay_1
	}
	return 0
}

func (m *DeviceProfile) GetRxDrOffset_1() uint32 {
	if m != nil {
		return m.RxDrOffset_1
	}
	return 0
}

func (m *DeviceProfile) GetRxDatarate_2() uint32 {
	if m != nil {
		return m.RxDatarate_2
	}
	return 0
}

func (m *DeviceProfile) GetRxFreq_2() uint32 {
	if m != nil {
		return m.RxFreq_2
	}
	return 0
}

func (m *DeviceProfile) GetFactoryPresetFreqs() []uint32 {
	if m != nil {
		return m.FactoryPresetFreqs
	}
	return nil
}

func (m *DeviceProfile) GetMaxEirp() uint32 {
	if m != nil {
		return m.MaxEirp
	}
	return 0
}

func (m *DeviceProfile) GetMaxDutyCycle() uint32 {
	if m != nil {
		return m.MaxDutyCycle
	}
	return 0
}

func (m *DeviceProfile) GetSupportsJoin() bool {
	if m != nil {
		return m.SupportsJoin
	}
	return false
}

func (m *DeviceProfile) GetRfRegion() string {
	if m != nil {
		return m.RfRegion
	}
	return ""
}

func (m *DeviceProfile) GetSupports_32BitFCnt() bool {
	if m != nil {
		return m.Supports_32BitFCnt
	}
	return false
}

type RoutingProfile struct {
	// ID of the routing profile.
	Id []byte `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// Application-server ID.
	AsId string `protobuf:"bytes,2,opt,name=as_id,json=asId,proto3" json:"as_id,omitempty"`
	// CA certificate for connecting to the AS.
	CaCert string `protobuf:"bytes,3,opt,name=ca_cert,json=caCert,proto3" json:"ca_cert,omitempty"`
	// TLS certificate for connecting to the AS.
	TlsCert string `protobuf:"bytes,4,opt,name=tls_cert,json=tlsCert,proto3" json:"tls_cert,omitempty"`
	// TLS key for connecting to the AS.
	// Note: when retrieving the routing-profile, the tls_key is not returned
	// for security reasons. When updating the routing-profile, an empty tls_key
	// does not clear the certificate, unless the tls_cert is also left blank.
	TlsKey               string   `protobuf:"bytes,5,opt,name=tls_key,json=tlsKey,proto3" json:"tls_key,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *RoutingProfile) Reset()         { *m = RoutingProfile{} }
func (m *RoutingProfile) String() string { return proto.CompactTextString(m) }
func (*RoutingProfile) ProtoMessage()    {}
func (*RoutingProfile) Descriptor() ([]byte, []int) {
	return fileDescriptor_ee79be696a10f18b, []int{2}
}

func (m *RoutingProfile) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_RoutingProfile.Unmarshal(m, b)
}
func (m *RoutingProfile) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_RoutingProfile.Marshal(b, m, deterministic)
}
func (m *RoutingProfile) XXX_Merge(src proto.Message) {
	xxx_messageInfo_RoutingProfile.Merge(m, src)
}
func (m *RoutingProfile) XXX_Size() int {
	return xxx_messageInfo_RoutingProfile.Size(m)
}
func (m *RoutingProfile) XXX_DiscardUnknown() {
	xxx_messageInfo_RoutingProfile.DiscardUnknown(m)
}

var xxx_messageInfo_RoutingProfile proto.InternalMessageInfo

func (m *RoutingProfile) GetId() []byte {
	if m != nil {
		return m.Id
	}
	return nil
}

func (m *RoutingProfile) GetAsId() string {
	if m != nil {
		return m.AsId
	}
	return ""
}

func (m *RoutingProfile) GetCaCert() string {
	if m != nil {
		return m.CaCert
	}
	return ""
}

func (m *RoutingProfile) GetTlsCert() string {
	if m != nil {
		return m.TlsCert
	}
	return ""
}

func (m *RoutingProfile) GetTlsKey() string {
	if m != nil {
		return m.TlsKey
	}
	return ""
}

func init() {
	proto.RegisterEnum("ns.RatePolicy", RatePolicy_name, RatePolicy_value)
	proto.RegisterType((*ServiceProfile)(nil), "ns.ServiceProfile")
	proto.RegisterType((*DeviceProfile)(nil), "ns.DeviceProfile")
	proto.RegisterType((*RoutingProfile)(nil), "ns.RoutingProfile")
}

func init() {
	proto.RegisterFile("ns/profiles.proto", fileDescriptor_ee79be696a10f18b)
}

var fileDescriptor_ee79be696a10f18b = []byte{
	// 969 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x7c, 0x55, 0x5d, 0x6f, 0xdb, 0x36,
	0x14, 0x9d, 0xd3, 0xc4, 0xb1, 0x19, 0x4b, 0x71, 0x98, 0x74, 0x55, 0xf7, 0xe9, 0xa5, 0xc5, 0x60,
	0x0c, 0xa8, 0xb3, 0xb8, 0x03, 0x86, 0x3d, 0xd6, 0xf6, 0x1a, 0x6c, 0x9d, 0x51, 0x43, 0x19, 0xf6,
	0xb0, 0x17, 0x82, 0x26, 0x69, 0x87, 0xb3, 0x24, 0x2a, 0x97, 0x54, 0x6c, 0xf7, 0x71, 0xbf, 0x77,
	0xc0, 0xfe, 0xc2, 0xc0, 0x2b, 0xd9, 0x4e, 0xd3, 0x6d, 0x6f, 0xd2, 0x39, 0xe7, 0xf2, 0xf0, 0x5e,
	0x1e, 0x4a, 0xe4, 0x24, 0xb3, 0x17, 0x39, 0x98, 0x99, 0x4e, 0x94, 0xed, 0xe5, 0x60, 0x9c, 0xa1,
	0x7b, 0x99, 0x3d, 0xff, 0xeb, 0x80, 0x84, 0xd7, 0x0a, 0xee, 0xb4, 0x50, 0x93, 0x92, 0xa5, 0x21,
	0xd9, 0xd3, 0x32, 0xaa, 0x75, 0x6a, 0xdd, 0x56, 0xbc, 0xa7, 0x25, 0x7d, 0x42, 0x0e, 0x8b, 0x84,
	0x01, 0x77, 0x2a, 0xda, 0xeb, 0xd4, 0xba, 0x41, 0x5c, 0x2f, 0x92, 0x98, 0x3b, 0x45, 0x9f, 0x93,
	0xb0, 0x48, 0xd8, 0xb4, 0x10, 0x0b, 0xe5, 0x98, 0xd5, 0xef, 0x54, 0xf4, 0x08, 0xf9, 0x56, 0x91,
	0x0c, 0x10, 0xbc, 0xd6, 0xef, 0x14, 0xfd, 0x0e, 0x55, 0xbe, 0x9c, 0xe5, 0x26, 0xd1, 0x62, 0x1d,
	0xed, 0x77, 0x6a, 0xdd, 0xb0, 0x1f, 0xf6, 0x32, 0xdb, 0xf3, 0xeb, 0x4c, 0x10, 0xf5, 0x55, 0xbb,
	0x37, 0x6f, 0x2a, 0x2b, 0xd3, 0x83, 0xd2, 0x54, 0x6e, 0x4d, 0xe5, 0xfb, 0xa6, 0xf5, 0xd2, 0x54,
	0x3e, 0x30, 0x95, 0xef, 0x9b, 0x1e, 0xfe, 0xbb, 0xa9, 0xbc, 0x6f, 0xfa, 0x35, 0x39, 0xe6, 0x52,
	0xb2, 0xf9, 0x92, 0xa5, 0xca, 0x71, 0xc9, 0x1d, 0x8f, 0x1a, 0x9d, 0x5a, 0xb7, 0x11, 0x07, 0x5c,
	0xca, 0xab, 0xe5, 0xb8, 0x02, 0xe9, 0x0b, 0x72, 0x2a, 0xd5, 0x1d, 0xb3, 0x8e, 0xbb, 0xc2, 0x32,
	0x50, 0xb7, 0x6c, 0x06, 0xea, 0x36, 0x6a, 0xe2, 0x46, 0xda, 0x52, 0xdd, 0x5d, 0x23, 0x13, 0xab,
	0xdb, 0xd7, 0xa0, 0x6e, 0xe9, 0x0f, 0xe4, 0x29, 0xa8, 0xdc, 0x80, 0x63, 0xf7, 0xaa, 0xa6, 0xdc,
	0x39, 0x05, 0xeb, 0x88, 0xa0, 0xc1, 0xc7, 0xa5, 0x60, 0xb4, 0x29, 0x1d, 0x94, 0x2c, 0xfd, 0x9e,
	0x44, 0x1f, 0x96, 0xa6, 0x1c, 0xe6, 0x3a, 0x8b, 0x8e, 0xb0, 0xf2, 0xf1, 0x83, 0xca, 0x31, 0x92,
	0xf4, 0x31, 0xa9, 0x4b, 0x60, 0xa9, 0xce, 0xa2, 0x16, 0xee, 0xea, 0x40, 0xc2, 0x78, 0x07, 0xf3,
	0x55, 0x14, 0x6c, 0x61, 0xbe, 0xa2, 0x5f, 0x91, 0x96, 0xb8, 0xe1, 0x59, 0xa6, 0x12, 0x96, 0x72,
	0xbb, 0x88, 0x42, 0x3c, 0xfc, 0xa3, 0x0a, 0x1b, 0x73, 0xbb, 0xa0, 0x9f, 0x13, 0x92, 0x03, 0xe3,
	0x49, 0x62, 0x96, 0x4a, 0x46, 0xc7, 0xe8, 0xdd, 0xcc, 0xe1, 0x55, 0x09, 0x78, 0xfa, 0x66, 0x47,
	0xb7, 0x4b, 0xfa, 0xe6, 0x3e, 0x0d, 0x7c, 0x4b, 0x9f, 0x94, 0x34, 0xf0, 0x0d, 0xfd, 0x05, 0x39,
	0xca, 0x96, 0x0b, 0x36, 0x57, 0x86, 0x25, 0x46, 0x44, 0xb4, 0xe4, 0xb3, 0xe5, 0xe2, 0x4a, 0x99,
	0x5f, 0x8c, 0xf0, 0xe5, 0x8e, 0xc3, 0x5c, 0x39, 0x96, 0x2b, 0x88, 0x4e, 0x71, 0xeb, 0xcd, 0x12,
	0x99, 0x28, 0xa0, 0x5d, 0xd2, 0x4e, 0x75, 0xe6, 0xcf, 0x4d, 0xea, 0x3b, 0x05, 0x56, 0xbb, 0x75,
	0x74, 0x86, 0xa2, 0x30, 0xd5, 0xd9, 0xd5, 0x72, 0xb4, 0x41, 0xcf, 0xff, 0x3e, 0x20, 0xc1, 0x48,
	0xfd, 0x5f, 0xda, 0xbb, 0xa4, 0x6d, 0x8b, 0xdc, 0x8f, 0xd4, 0x32, 0x91, 0x70, 0x6b, 0xd9, 0x14,
	0x63, 0xdf, 0x88, 0xc3, 0x0d, 0x3e, 0xf4, 0xf0, 0xc0, 0xa7, 0xa5, 0x12, 0x30, 0xa7, 0x53, 0x65,
	0x0a, 0x57, 0xe5, 0x3f, 0x40, 0x78, 0xf0, 0x6b, 0x09, 0xfa, 0x15, 0x73, 0x9d, 0xcd, 0x99, 0x4d,
	0x0c, 0xee, 0x5f, 0x1b, 0x89, 0x57, 0x20, 0x88, 0x43, 0x8f, 0x5f, 0x27, 0xc6, 0x37, 0xa1, 0x8d,
	0xa4, 0x1d, 0xd2, 0xda, 0x29, 0x25, 0x54, 0xc9, 0x27, 0x1b, 0xd5, 0x08, 0x7c, 0xfa, 0x77, 0x0a,
	0x0c, 0x5d, 0x95, 0xfe, 0x8d, 0x06, 0x03, 0xf7, 0x61, 0x0f, 0x02, 0xf3, 0xff, 0xb0, 0x87, 0xe1,
	0xae, 0x07, 0xb1, 0xed, 0xa1, 0x71, 0xaf, 0x87, 0xe1, 0xa6, 0x87, 0x2f, 0xc9, 0x51, 0xca, 0x05,
	0xc3, 0x31, 0x9a, 0x0c, 0x93, 0xde, 0x8c, 0x49, 0xca, 0xc5, 0x6f, 0x25, 0x42, 0x7b, 0xe4, 0x14,
	0xd4, 0x9c, 0xe5, 0x1c, 0x78, 0xea, 0xaf, 0xc4, 0x9d, 0x46, 0x21, 0x41, 0xe1, 0x09, 0xa8, 0xf9,
	0x04, 0x99, 0xb8, 0x22, 0xe8, 0x67, 0x84, 0xc0, 0x8a, 0x49, 0x95, 0xf0, 0x35, 0xbb, 0xc4, 0x28,
	0x07, 0x71, 0x03, 0x56, 0x23, 0x0f, 0x5c, 0xd2, 0x67, 0x24, 0xf4, 0x2c, 0x30, 0x33, 0x9b, 0x59,
	0xe5, 0xd8, 0x65, 0x95, 0xe2, 0x23, 0x58, 0x8d, 0xe0, 0x2d, 0x62, 0x97, 0xf4, 0x9c, 0x04, 0x5e,
	0xc4, 0x1d, 0xc7, 0x7b, 0xde, 0xaf, 0x22, 0xed, 0x35, 0x15, 0xd6, 0xa7, 0x9f, 0x90, 0x26, 0xac,
	0x70, 0x50, 0xac, 0x8f, 0xa9, 0x0e, 0xe2, 0x43, 0x58, 0xf9, 0x21, 0xf5, 0xe9, 0xb7, 0xe4, 0x6c,
	0xc6, 0x85, 0x33, 0xb0, 0x66, 0x39, 0x28, 0x6f, 0xe3, 0x75, 0x36, 0x3a, 0xee, 0x3c, 0xea, 0x06,
	0x31, 0xad, 0xb8, 0x09, 0x52, 0xbe, 0xc2, 0xd2, 0xa7, 0xa4, 0x91, 0xf2, 0x15, 0x53, 0x1a, 0x72,
	0x8c, 0x78, 0x10, 0x1f, 0xa6, 0x7c, 0xf5, 0xa3, 0x86, 0xdc, 0x1f, 0x8c, 0xa7, 0x64, 0xe1, 0xd6,
	0x4c, 0xac, 0x45, 0xa2, 0x30, 0xe4, 0x41, 0xdc, 0x4a, 0xf9, 0x6a, 0x54, 0xb8, 0xf5, 0xd0, 0x63,
	0xf4, 0x19, 0x09, 0xb6, 0x07, 0xf3, 0x87, 0xd1, 0x59, 0x95, 0xf4, 0xd6, 0x06, 0xfc, 0xd9, 0xe8,
	0x8c, 0x7e, 0x4a, 0x9a, 0x30, 0x63, 0xa0, 0xe6, 0x7e, 0x80, 0xa7, 0x38, 0xc0, 0x06, 0xcc, 0x62,
	0x7c, 0xa7, 0x17, 0xe4, 0x6c, 0xbb, 0xc2, 0xcb, 0xfe, 0x54, 0x3b, 0x36, 0x63, 0x22, 0x73, 0x18,
	0xf7, 0x46, 0x7c, 0xb2, 0xe1, 0x90, 0x7a, 0x3d, 0xcc, 0xdc, 0xf9, 0x9f, 0x35, 0x12, 0xc6, 0xa6,
	0x70, 0x3a, 0x9b, 0xff, 0x57, 0xe4, 0x4f, 0xc9, 0x01, 0xb7, 0x4c, 0x4b, 0xcc, 0x79, 0x33, 0xde,
	0xe7, 0xf6, 0x27, 0xfc, 0xea, 0x0b, 0xce, 0x84, 0x82, 0x32, 0xd5, 0xcd, 0xb8, 0x2e, 0xf8, 0x50,
	0x81, 0xf3, 0x43, 0x70, 0x89, 0x2d, 0x99, 0x7d, 0x64, 0x0e, 0x5d, 0x62, 0x91, 0x7a, 0x42, 0xfc,
	0x23, 0x5b, 0xa8, 0x35, 0x46, 0xb7, 0x19, 0xd7, 0x5d, 0x62, 0xdf, 0xa8, 0xf5, 0x37, 0x1d, 0x42,
	0xee, 0x7d, 0x66, 0x1b, 0x64, 0x7f, 0x14, 0xbf, 0x9d, 0xb4, 0x3f, 0xf2, 0x4f, 0xe3, 0x57, 0xf1,
	0x9b, 0x76, 0x6d, 0x30, 0x26, 0x67, 0xda, 0xf4, 0xc4, 0x8d, 0x86, 0xdc, 0x3a, 0x2e, 0x16, 0x3d,
	0x9e, 0xeb, 0x5e, 0x66, 0x07, 0x41, 0xb5, 0x69, 0x3b, 0xf1, 0xbf, 0xac, 0x49, 0xed, 0xf7, 0xe7,
	0x73, 0xed, 0x6e, 0x8a, 0x69, 0x4f, 0x98, 0xf4, 0x62, 0x0a, 0x46, 0x70, 0x0e, 0x17, 0xbb, 0xb2,
	0x17, 0x3c, 0xd7, 0x17, 0x99, 0x9d, 0xd6, 0xf1, 0x0f, 0xf7, 0xf2, 0x9f, 0x00, 0x00, 0x00, 0xff,
	0xff, 0x4a, 0xb3, 0x5f, 0x99, 0xf6, 0x06, 0x00, 0x00,
}
