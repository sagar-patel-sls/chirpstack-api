# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from chirpstack_api.geo import geo_pb2 as chirpstack__api_dot_geo_dot_geo__pb2


class GeolocationServerServiceStub(object):
    """GeolocationServerService implements a geolocation-server service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ResolveTDOA = channel.unary_unary(
                '/geo.GeolocationServerService/ResolveTDOA',
                request_serializer=chirpstack__api_dot_geo_dot_geo__pb2.ResolveTDOARequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_geo_dot_geo__pb2.ResolveTDOAResponse.FromString,
                )
        self.ResolveMultiFrameTDOA = channel.unary_unary(
                '/geo.GeolocationServerService/ResolveMultiFrameTDOA',
                request_serializer=chirpstack__api_dot_geo_dot_geo__pb2.ResolveMultiFrameTDOARequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_geo_dot_geo__pb2.ResolveMultiFrameTDOAResponse.FromString,
                )


class GeolocationServerServiceServicer(object):
    """GeolocationServerService implements a geolocation-server service.
    """

    def ResolveTDOA(self, request, context):
        """ResolveTDOA resolves the location based on TDOA.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResolveMultiFrameTDOA(self, request, context):
        """ResolveMultiFrameTDOA resolves the location using TDOA, based on
        multiple frames.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GeolocationServerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ResolveTDOA': grpc.unary_unary_rpc_method_handler(
                    servicer.ResolveTDOA,
                    request_deserializer=chirpstack__api_dot_geo_dot_geo__pb2.ResolveTDOARequest.FromString,
                    response_serializer=chirpstack__api_dot_geo_dot_geo__pb2.ResolveTDOAResponse.SerializeToString,
            ),
            'ResolveMultiFrameTDOA': grpc.unary_unary_rpc_method_handler(
                    servicer.ResolveMultiFrameTDOA,
                    request_deserializer=chirpstack__api_dot_geo_dot_geo__pb2.ResolveMultiFrameTDOARequest.FromString,
                    response_serializer=chirpstack__api_dot_geo_dot_geo__pb2.ResolveMultiFrameTDOAResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'geo.GeolocationServerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GeolocationServerService(object):
    """GeolocationServerService implements a geolocation-server service.
    """

    @staticmethod
    def ResolveTDOA(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/geo.GeolocationServerService/ResolveTDOA',
            chirpstack__api_dot_geo_dot_geo__pb2.ResolveTDOARequest.SerializeToString,
            chirpstack__api_dot_geo_dot_geo__pb2.ResolveTDOAResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResolveMultiFrameTDOA(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/geo.GeolocationServerService/ResolveMultiFrameTDOA',
            chirpstack__api_dot_geo_dot_geo__pb2.ResolveMultiFrameTDOARequest.SerializeToString,
            chirpstack__api_dot_geo_dot_geo__pb2.ResolveMultiFrameTDOAResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
