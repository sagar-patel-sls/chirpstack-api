// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: as/external/api/deviceQueue.proto
// </auto-generated>
#pragma warning disable 0414, 1591, 8981
#region Designer generated code

using grpc = global::Grpc.Core;

namespace chirpstack.as.external.api {
  /// <summary>
  /// DeviceQueueService is the service managing the downlink data queue.
  /// </summary>
  public static partial class DeviceQueueService
  {
    static readonly string __ServiceName = "api.DeviceQueueService";

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static void __Helper_SerializeMessage(global::Google.Protobuf.IMessage message, grpc::SerializationContext context)
    {
      #if !GRPC_DISABLE_PROTOBUF_BUFFER_SERIALIZATION
      if (message is global::Google.Protobuf.IBufferMessage)
      {
        context.SetPayloadLength(message.CalculateSize());
        global::Google.Protobuf.MessageExtensions.WriteTo(message, context.GetBufferWriter());
        context.Complete();
        return;
      }
      #endif
      context.Complete(global::Google.Protobuf.MessageExtensions.ToByteArray(message));
    }

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static class __Helper_MessageCache<T>
    {
      public static readonly bool IsBufferMessage = global::System.Reflection.IntrospectionExtensions.GetTypeInfo(typeof(global::Google.Protobuf.IBufferMessage)).IsAssignableFrom(typeof(T));
    }

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static T __Helper_DeserializeMessage<T>(grpc::DeserializationContext context, global::Google.Protobuf.MessageParser<T> parser) where T : global::Google.Protobuf.IMessage<T>
    {
      #if !GRPC_DISABLE_PROTOBUF_BUFFER_SERIALIZATION
      if (__Helper_MessageCache<T>.IsBufferMessage)
      {
        return parser.ParseFrom(context.PayloadAsReadOnlySequence());
      }
      #endif
      return parser.ParseFrom(context.PayloadAsNewBuffer());
    }

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::chirpstack.as.external.api.EnqueueDeviceQueueItemRequest> __Marshaller_api_EnqueueDeviceQueueItemRequest = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::chirpstack.as.external.api.EnqueueDeviceQueueItemRequest.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::chirpstack.as.external.api.EnqueueDeviceQueueItemResponse> __Marshaller_api_EnqueueDeviceQueueItemResponse = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::chirpstack.as.external.api.EnqueueDeviceQueueItemResponse.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::chirpstack.as.external.api.FlushDeviceQueueRequest> __Marshaller_api_FlushDeviceQueueRequest = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::chirpstack.as.external.api.FlushDeviceQueueRequest.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Google.Protobuf.WellKnownTypes.Empty> __Marshaller_google_protobuf_Empty = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Google.Protobuf.WellKnownTypes.Empty.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::chirpstack.as.external.api.ListDeviceQueueItemsRequest> __Marshaller_api_ListDeviceQueueItemsRequest = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::chirpstack.as.external.api.ListDeviceQueueItemsRequest.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::chirpstack.as.external.api.ListDeviceQueueItemsResponse> __Marshaller_api_ListDeviceQueueItemsResponse = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::chirpstack.as.external.api.ListDeviceQueueItemsResponse.Parser));

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::chirpstack.as.external.api.EnqueueDeviceQueueItemRequest, global::chirpstack.as.external.api.EnqueueDeviceQueueItemResponse> __Method_Enqueue = new grpc::Method<global::chirpstack.as.external.api.EnqueueDeviceQueueItemRequest, global::chirpstack.as.external.api.EnqueueDeviceQueueItemResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "Enqueue",
        __Marshaller_api_EnqueueDeviceQueueItemRequest,
        __Marshaller_api_EnqueueDeviceQueueItemResponse);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::chirpstack.as.external.api.FlushDeviceQueueRequest, global::Google.Protobuf.WellKnownTypes.Empty> __Method_Flush = new grpc::Method<global::chirpstack.as.external.api.FlushDeviceQueueRequest, global::Google.Protobuf.WellKnownTypes.Empty>(
        grpc::MethodType.Unary,
        __ServiceName,
        "Flush",
        __Marshaller_api_FlushDeviceQueueRequest,
        __Marshaller_google_protobuf_Empty);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::chirpstack.as.external.api.ListDeviceQueueItemsRequest, global::chirpstack.as.external.api.ListDeviceQueueItemsResponse> __Method_List = new grpc::Method<global::chirpstack.as.external.api.ListDeviceQueueItemsRequest, global::chirpstack.as.external.api.ListDeviceQueueItemsResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "List",
        __Marshaller_api_ListDeviceQueueItemsRequest,
        __Marshaller_api_ListDeviceQueueItemsResponse);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::chirpstack.as.external.api.DeviceQueueReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of DeviceQueueService</summary>
    [grpc::BindServiceMethod(typeof(DeviceQueueService), "BindService")]
    public abstract partial class DeviceQueueServiceBase
    {
      /// <summary>
      /// Enqueue adds the given item to the device-queue.
      /// </summary>
      /// <param name="request">The request received from the client.</param>
      /// <param name="context">The context of the server-side call handler being invoked.</param>
      /// <returns>The response to send back to the client (wrapped by a task).</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::chirpstack.as.external.api.EnqueueDeviceQueueItemResponse> Enqueue(global::chirpstack.as.external.api.EnqueueDeviceQueueItemRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      /// <summary>
      /// Flush flushes the downlink device-queue.
      /// </summary>
      /// <param name="request">The request received from the client.</param>
      /// <param name="context">The context of the server-side call handler being invoked.</param>
      /// <returns>The response to send back to the client (wrapped by a task).</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Google.Protobuf.WellKnownTypes.Empty> Flush(global::chirpstack.as.external.api.FlushDeviceQueueRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      /// <summary>
      /// List lists the items in the device-queue.
      /// </summary>
      /// <param name="request">The request received from the client.</param>
      /// <param name="context">The context of the server-side call handler being invoked.</param>
      /// <returns>The response to send back to the client (wrapped by a task).</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::chirpstack.as.external.api.ListDeviceQueueItemsResponse> List(global::chirpstack.as.external.api.ListDeviceQueueItemsRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for DeviceQueueService</summary>
    public partial class DeviceQueueServiceClient : grpc::ClientBase<DeviceQueueServiceClient>
    {
      /// <summary>Creates a new client for DeviceQueueService</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public DeviceQueueServiceClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for DeviceQueueService that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public DeviceQueueServiceClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected DeviceQueueServiceClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected DeviceQueueServiceClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      /// <summary>
      /// Enqueue adds the given item to the device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::chirpstack.as.external.api.EnqueueDeviceQueueItemResponse Enqueue(global::chirpstack.as.external.api.EnqueueDeviceQueueItemRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return Enqueue(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      /// Enqueue adds the given item to the device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::chirpstack.as.external.api.EnqueueDeviceQueueItemResponse Enqueue(global::chirpstack.as.external.api.EnqueueDeviceQueueItemRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_Enqueue, null, options, request);
      }
      /// <summary>
      /// Enqueue adds the given item to the device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::chirpstack.as.external.api.EnqueueDeviceQueueItemResponse> EnqueueAsync(global::chirpstack.as.external.api.EnqueueDeviceQueueItemRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return EnqueueAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      /// Enqueue adds the given item to the device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::chirpstack.as.external.api.EnqueueDeviceQueueItemResponse> EnqueueAsync(global::chirpstack.as.external.api.EnqueueDeviceQueueItemRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_Enqueue, null, options, request);
      }
      /// <summary>
      /// Flush flushes the downlink device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Google.Protobuf.WellKnownTypes.Empty Flush(global::chirpstack.as.external.api.FlushDeviceQueueRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return Flush(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      /// Flush flushes the downlink device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Google.Protobuf.WellKnownTypes.Empty Flush(global::chirpstack.as.external.api.FlushDeviceQueueRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_Flush, null, options, request);
      }
      /// <summary>
      /// Flush flushes the downlink device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Google.Protobuf.WellKnownTypes.Empty> FlushAsync(global::chirpstack.as.external.api.FlushDeviceQueueRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return FlushAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      /// Flush flushes the downlink device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Google.Protobuf.WellKnownTypes.Empty> FlushAsync(global::chirpstack.as.external.api.FlushDeviceQueueRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_Flush, null, options, request);
      }
      /// <summary>
      /// List lists the items in the device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::chirpstack.as.external.api.ListDeviceQueueItemsResponse List(global::chirpstack.as.external.api.ListDeviceQueueItemsRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return List(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      /// List lists the items in the device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::chirpstack.as.external.api.ListDeviceQueueItemsResponse List(global::chirpstack.as.external.api.ListDeviceQueueItemsRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_List, null, options, request);
      }
      /// <summary>
      /// List lists the items in the device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::chirpstack.as.external.api.ListDeviceQueueItemsResponse> ListAsync(global::chirpstack.as.external.api.ListDeviceQueueItemsRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return ListAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      /// List lists the items in the device-queue.
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::chirpstack.as.external.api.ListDeviceQueueItemsResponse> ListAsync(global::chirpstack.as.external.api.ListDeviceQueueItemsRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_List, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected override DeviceQueueServiceClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new DeviceQueueServiceClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    public static grpc::ServerServiceDefinition BindService(DeviceQueueServiceBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_Enqueue, serviceImpl.Enqueue)
          .AddMethod(__Method_Flush, serviceImpl.Flush)
          .AddMethod(__Method_List, serviceImpl.List).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    public static void BindService(grpc::ServiceBinderBase serviceBinder, DeviceQueueServiceBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_Enqueue, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::chirpstack.as.external.api.EnqueueDeviceQueueItemRequest, global::chirpstack.as.external.api.EnqueueDeviceQueueItemResponse>(serviceImpl.Enqueue));
      serviceBinder.AddMethod(__Method_Flush, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::chirpstack.as.external.api.FlushDeviceQueueRequest, global::Google.Protobuf.WellKnownTypes.Empty>(serviceImpl.Flush));
      serviceBinder.AddMethod(__Method_List, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::chirpstack.as.external.api.ListDeviceQueueItemsRequest, global::chirpstack.as.external.api.ListDeviceQueueItemsResponse>(serviceImpl.List));
    }

  }
}
#endregion
