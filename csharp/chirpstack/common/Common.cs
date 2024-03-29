// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: common/common.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace chirpstack.common {

  /// <summary>Holder for reflection information generated from common/common.proto</summary>
  public static partial class CommonReflection {

    #region Descriptor
    /// <summary>File descriptor for common/common.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static CommonReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChNjb21tb24vY29tbW9uLnByb3RvEgZjb21tb24iMQoLS2V5RW52ZWxvcGUS",
            "EQoJa2VrX2xhYmVsGAEgASgJEg8KB2Flc19rZXkYAiABKAwiewoITG9jYXRp",
            "b24SEAoIbGF0aXR1ZGUYASABKAESEQoJbG9uZ2l0dWRlGAIgASgBEhAKCGFs",
            "dGl0dWRlGAMgASgBEiYKBnNvdXJjZRgEIAEoDjIWLmNvbW1vbi5Mb2NhdGlv",
            "blNvdXJjZRIQCghhY2N1cmFjeRgFIAEoDSosCgpNb2R1bGF0aW9uEggKBExP",
            "UkEQABIHCgNGU0sQARILCgdMUl9GSFNTEAIqqgEKBlJlZ2lvbhIJCgVFVTg2",
            "OBAAEgkKBVVTOTE1EAISCQoFQ043NzkQAxIJCgVFVTQzMxAEEgkKBUFVOTE1",
            "EAUSCQoFQ040NzAQBhIJCgVBUzkyMxAHEgsKB0FTOTIzXzIQDBILCgdBUzky",
            "M18zEA0SCwoHQVM5MjNfNBAOEgkKBUtSOTIwEAgSCQoFSU44NjUQCRIJCgVS",
            "VTg2NBAKEgsKB0lTTTI0MDAQCyqoAQoFTVR5cGUSDwoLSm9pblJlcXVlc3QQ",
            "ABIOCgpKb2luQWNjZXB0EAESFQoRVW5jb25maXJtZWREYXRhVXAQAhIXChNV",
            "bmNvbmZpcm1lZERhdGFEb3duEAMSEwoPQ29uZmlybWVkRGF0YVVwEAQSFQoR",
            "Q29uZmlybWVkRGF0YURvd24QBRIRCg1SZWpvaW5SZXF1ZXN0EAYSDwoLUHJv",
            "cHJpZXRhcnkQByqOAQoOTG9jYXRpb25Tb3VyY2USCwoHVU5LTk9XThAAEgcK",
            "A0dQUxABEgoKBkNPTkZJRxACEhUKEUdFT19SRVNPTFZFUl9URE9BEAMSFQoR",
            "R0VPX1JFU09MVkVSX1JTU0kQBBIVChFHRU9fUkVTT0xWRVJfR05TUxAFEhUK",
            "EUdFT19SRVNPTFZFUl9XSUZJEAZCdQoYaW8uY2hpcnBzdGFjay5hcGkuY29t",
            "bW9uQgtDb21tb25Qcm90b1ABWjZnaXRodWIuY29tL3NhZ2FyLXBhdGVsLXNs",
            "cy9jaGlycHN0YWNrLWFwaS9nby92My9jb21tb26qAhFjaGlycHN0YWNrLmNv",
            "bW1vbmIGcHJvdG8z"));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(new[] {typeof(global::chirpstack.common.Modulation), typeof(global::chirpstack.common.Region), typeof(global::chirpstack.common.MType), typeof(global::chirpstack.common.LocationSource), }, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::chirpstack.common.KeyEnvelope), global::chirpstack.common.KeyEnvelope.Parser, new[]{ "KekLabel", "AesKey" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::chirpstack.common.Location), global::chirpstack.common.Location.Parser, new[]{ "Latitude", "Longitude", "Altitude", "Source", "Accuracy" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Enums
  public enum Modulation {
    /// <summary>
    /// LoRa
    /// </summary>
    [pbr::OriginalName("LORA")] Lora = 0,
    /// <summary>
    /// FSK
    /// </summary>
    [pbr::OriginalName("FSK")] Fsk = 1,
    /// <summary>
    /// LR-FHSS
    /// </summary>
    [pbr::OriginalName("LR_FHSS")] LrFhss = 2,
  }

  public enum Region {
    /// <summary>
    /// EU868
    /// </summary>
    [pbr::OriginalName("EU868")] Eu868 = 0,
    /// <summary>
    /// US915
    /// </summary>
    [pbr::OriginalName("US915")] Us915 = 2,
    /// <summary>
    /// CN779
    /// </summary>
    [pbr::OriginalName("CN779")] Cn779 = 3,
    /// <summary>
    /// EU433
    /// </summary>
    [pbr::OriginalName("EU433")] Eu433 = 4,
    /// <summary>
    /// AU915
    /// </summary>
    [pbr::OriginalName("AU915")] Au915 = 5,
    /// <summary>
    /// CN470
    /// </summary>
    [pbr::OriginalName("CN470")] Cn470 = 6,
    /// <summary>
    /// AS923
    /// </summary>
    [pbr::OriginalName("AS923")] As923 = 7,
    /// <summary>
    /// AS923 with -1.80 MHz frequency offset
    /// </summary>
    [pbr::OriginalName("AS923_2")] As9232 = 12,
    /// <summary>
    /// AS923 with -6.60 MHz frequency offset
    /// </summary>
    [pbr::OriginalName("AS923_3")] As9233 = 13,
    /// <summary>
    /// AS923 with -5.90 MHz frequency offset
    /// </summary>
    [pbr::OriginalName("AS923_4")] As9234 = 14,
    /// <summary>
    /// KR920
    /// </summary>
    [pbr::OriginalName("KR920")] Kr920 = 8,
    /// <summary>
    /// IN865
    /// </summary>
    [pbr::OriginalName("IN865")] In865 = 9,
    /// <summary>
    /// RU864
    /// </summary>
    [pbr::OriginalName("RU864")] Ru864 = 10,
    /// <summary>
    /// ISM2400 (LoRaWAN 2.4 GHz)
    /// </summary>
    [pbr::OriginalName("ISM2400")] Ism2400 = 11,
  }

  public enum MType {
    /// <summary>
    /// JoinRequest.
    /// </summary>
    [pbr::OriginalName("JoinRequest")] JoinRequest = 0,
    /// <summary>
    /// JoinAccept.
    /// </summary>
    [pbr::OriginalName("JoinAccept")] JoinAccept = 1,
    /// <summary>
    /// UnconfirmedDataUp.
    /// </summary>
    [pbr::OriginalName("UnconfirmedDataUp")] UnconfirmedDataUp = 2,
    /// <summary>
    /// UnconfirmedDataDown.
    /// </summary>
    [pbr::OriginalName("UnconfirmedDataDown")] UnconfirmedDataDown = 3,
    /// <summary>
    /// ConfirmedDataUp.
    /// </summary>
    [pbr::OriginalName("ConfirmedDataUp")] ConfirmedDataUp = 4,
    /// <summary>
    /// ConfirmedDataDown.
    /// </summary>
    [pbr::OriginalName("ConfirmedDataDown")] ConfirmedDataDown = 5,
    /// <summary>
    /// RejoinRequest.
    /// </summary>
    [pbr::OriginalName("RejoinRequest")] RejoinRequest = 6,
    /// <summary>
    /// Proprietary.
    /// </summary>
    [pbr::OriginalName("Proprietary")] Proprietary = 7,
  }

  public enum LocationSource {
    /// <summary>
    /// Unknown.
    /// </summary>
    [pbr::OriginalName("UNKNOWN")] Unknown = 0,
    /// <summary>
    /// GPS.
    /// </summary>
    [pbr::OriginalName("GPS")] Gps = 1,
    /// <summary>
    /// Manually configured.
    /// </summary>
    [pbr::OriginalName("CONFIG")] Config = 2,
    /// <summary>
    /// Geo resolver (TDOA).
    /// </summary>
    [pbr::OriginalName("GEO_RESOLVER_TDOA")] GeoResolverTdoa = 3,
    /// <summary>
    /// Geo resolver (RSSI).
    /// </summary>
    [pbr::OriginalName("GEO_RESOLVER_RSSI")] GeoResolverRssi = 4,
    /// <summary>
    /// Geo resolver (GNSS).
    /// </summary>
    [pbr::OriginalName("GEO_RESOLVER_GNSS")] GeoResolverGnss = 5,
    /// <summary>
    /// Geo resolver (WIFI).
    /// </summary>
    [pbr::OriginalName("GEO_RESOLVER_WIFI")] GeoResolverWifi = 6,
  }

  #endregion

  #region Messages
  public sealed partial class KeyEnvelope : pb::IMessage<KeyEnvelope>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<KeyEnvelope> _parser = new pb::MessageParser<KeyEnvelope>(() => new KeyEnvelope());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<KeyEnvelope> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::chirpstack.common.CommonReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public KeyEnvelope() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public KeyEnvelope(KeyEnvelope other) : this() {
      kekLabel_ = other.kekLabel_;
      aesKey_ = other.aesKey_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public KeyEnvelope Clone() {
      return new KeyEnvelope(this);
    }

    /// <summary>Field number for the "kek_label" field.</summary>
    public const int KekLabelFieldNumber = 1;
    private string kekLabel_ = "";
    /// <summary>
    /// KEK label.
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string KekLabel {
      get { return kekLabel_; }
      set {
        kekLabel_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "aes_key" field.</summary>
    public const int AesKeyFieldNumber = 2;
    private pb::ByteString aesKey_ = pb::ByteString.Empty;
    /// <summary>
    /// AES key (when the kek_label is set, this key is encrypted using a key
    /// known to the join-server and application-server.
    /// For more information please refer to the LoRaWAN Backend Interface
    /// 'Key Transport Security' section.
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pb::ByteString AesKey {
      get { return aesKey_; }
      set {
        aesKey_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as KeyEnvelope);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(KeyEnvelope other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (KekLabel != other.KekLabel) return false;
      if (AesKey != other.AesKey) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (KekLabel.Length != 0) hash ^= KekLabel.GetHashCode();
      if (AesKey.Length != 0) hash ^= AesKey.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (KekLabel.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(KekLabel);
      }
      if (AesKey.Length != 0) {
        output.WriteRawTag(18);
        output.WriteBytes(AesKey);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (KekLabel.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(KekLabel);
      }
      if (AesKey.Length != 0) {
        output.WriteRawTag(18);
        output.WriteBytes(AesKey);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (KekLabel.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(KekLabel);
      }
      if (AesKey.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeBytesSize(AesKey);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(KeyEnvelope other) {
      if (other == null) {
        return;
      }
      if (other.KekLabel.Length != 0) {
        KekLabel = other.KekLabel;
      }
      if (other.AesKey.Length != 0) {
        AesKey = other.AesKey;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            KekLabel = input.ReadString();
            break;
          }
          case 18: {
            AesKey = input.ReadBytes();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            KekLabel = input.ReadString();
            break;
          }
          case 18: {
            AesKey = input.ReadBytes();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class Location : pb::IMessage<Location>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<Location> _parser = new pb::MessageParser<Location>(() => new Location());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<Location> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::chirpstack.common.CommonReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Location() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Location(Location other) : this() {
      latitude_ = other.latitude_;
      longitude_ = other.longitude_;
      altitude_ = other.altitude_;
      source_ = other.source_;
      accuracy_ = other.accuracy_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Location Clone() {
      return new Location(this);
    }

    /// <summary>Field number for the "latitude" field.</summary>
    public const int LatitudeFieldNumber = 1;
    private double latitude_;
    /// <summary>
    /// Latitude.
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public double Latitude {
      get { return latitude_; }
      set {
        latitude_ = value;
      }
    }

    /// <summary>Field number for the "longitude" field.</summary>
    public const int LongitudeFieldNumber = 2;
    private double longitude_;
    /// <summary>
    /// Longitude.
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public double Longitude {
      get { return longitude_; }
      set {
        longitude_ = value;
      }
    }

    /// <summary>Field number for the "altitude" field.</summary>
    public const int AltitudeFieldNumber = 3;
    private double altitude_;
    /// <summary>
    /// Altitude.
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public double Altitude {
      get { return altitude_; }
      set {
        altitude_ = value;
      }
    }

    /// <summary>Field number for the "source" field.</summary>
    public const int SourceFieldNumber = 4;
    private global::chirpstack.common.LocationSource source_ = global::chirpstack.common.LocationSource.Unknown;
    /// <summary>
    /// Location source.
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::chirpstack.common.LocationSource Source {
      get { return source_; }
      set {
        source_ = value;
      }
    }

    /// <summary>Field number for the "accuracy" field.</summary>
    public const int AccuracyFieldNumber = 5;
    private uint accuracy_;
    /// <summary>
    /// Accuracy (in meters).
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public uint Accuracy {
      get { return accuracy_; }
      set {
        accuracy_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as Location);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(Location other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(Latitude, other.Latitude)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(Longitude, other.Longitude)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(Altitude, other.Altitude)) return false;
      if (Source != other.Source) return false;
      if (Accuracy != other.Accuracy) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (Latitude != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(Latitude);
      if (Longitude != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(Longitude);
      if (Altitude != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(Altitude);
      if (Source != global::chirpstack.common.LocationSource.Unknown) hash ^= Source.GetHashCode();
      if (Accuracy != 0) hash ^= Accuracy.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (Latitude != 0D) {
        output.WriteRawTag(9);
        output.WriteDouble(Latitude);
      }
      if (Longitude != 0D) {
        output.WriteRawTag(17);
        output.WriteDouble(Longitude);
      }
      if (Altitude != 0D) {
        output.WriteRawTag(25);
        output.WriteDouble(Altitude);
      }
      if (Source != global::chirpstack.common.LocationSource.Unknown) {
        output.WriteRawTag(32);
        output.WriteEnum((int) Source);
      }
      if (Accuracy != 0) {
        output.WriteRawTag(40);
        output.WriteUInt32(Accuracy);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Latitude != 0D) {
        output.WriteRawTag(9);
        output.WriteDouble(Latitude);
      }
      if (Longitude != 0D) {
        output.WriteRawTag(17);
        output.WriteDouble(Longitude);
      }
      if (Altitude != 0D) {
        output.WriteRawTag(25);
        output.WriteDouble(Altitude);
      }
      if (Source != global::chirpstack.common.LocationSource.Unknown) {
        output.WriteRawTag(32);
        output.WriteEnum((int) Source);
      }
      if (Accuracy != 0) {
        output.WriteRawTag(40);
        output.WriteUInt32(Accuracy);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (Latitude != 0D) {
        size += 1 + 8;
      }
      if (Longitude != 0D) {
        size += 1 + 8;
      }
      if (Altitude != 0D) {
        size += 1 + 8;
      }
      if (Source != global::chirpstack.common.LocationSource.Unknown) {
        size += 1 + pb::CodedOutputStream.ComputeEnumSize((int) Source);
      }
      if (Accuracy != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(Accuracy);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(Location other) {
      if (other == null) {
        return;
      }
      if (other.Latitude != 0D) {
        Latitude = other.Latitude;
      }
      if (other.Longitude != 0D) {
        Longitude = other.Longitude;
      }
      if (other.Altitude != 0D) {
        Altitude = other.Altitude;
      }
      if (other.Source != global::chirpstack.common.LocationSource.Unknown) {
        Source = other.Source;
      }
      if (other.Accuracy != 0) {
        Accuracy = other.Accuracy;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 9: {
            Latitude = input.ReadDouble();
            break;
          }
          case 17: {
            Longitude = input.ReadDouble();
            break;
          }
          case 25: {
            Altitude = input.ReadDouble();
            break;
          }
          case 32: {
            Source = (global::chirpstack.common.LocationSource) input.ReadEnum();
            break;
          }
          case 40: {
            Accuracy = input.ReadUInt32();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 9: {
            Latitude = input.ReadDouble();
            break;
          }
          case 17: {
            Longitude = input.ReadDouble();
            break;
          }
          case 25: {
            Altitude = input.ReadDouble();
            break;
          }
          case 32: {
            Source = (global::chirpstack.common.LocationSource) input.ReadEnum();
            break;
          }
          case 40: {
            Accuracy = input.ReadUInt32();
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code
