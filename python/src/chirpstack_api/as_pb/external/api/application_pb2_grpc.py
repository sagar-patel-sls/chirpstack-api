# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from chirpstack_api.as_pb.external.api import application_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ApplicationServiceStub(object):
  """ApplicationService is the service managing applications.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/api.ApplicationService/Create',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateApplicationRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateApplicationResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/api.ApplicationService/Get',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetApplicationRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetApplicationResponse.FromString,
        )
    self.Update = channel.unary_unary(
        '/api.ApplicationService/Update',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.UpdateApplicationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Delete = channel.unary_unary(
        '/api.ApplicationService/Delete',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.DeleteApplicationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.List = channel.unary_unary(
        '/api.ApplicationService/List',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.ListApplicationRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.ListApplicationResponse.FromString,
        )
    self.CreateHTTPIntegration = channel.unary_unary(
        '/api.ApplicationService/CreateHTTPIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateHTTPIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetHTTPIntegration = channel.unary_unary(
        '/api.ApplicationService/GetHTTPIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetHTTPIntegrationRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetHTTPIntegrationResponse.FromString,
        )
    self.UpdateHTTPIntegration = channel.unary_unary(
        '/api.ApplicationService/UpdateHTTPIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.UpdateHTTPIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteHTTPIntegration = channel.unary_unary(
        '/api.ApplicationService/DeleteHTTPIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.DeleteHTTPIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CreateInfluxDBIntegration = channel.unary_unary(
        '/api.ApplicationService/CreateInfluxDBIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateInfluxDBIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetInfluxDBIntegration = channel.unary_unary(
        '/api.ApplicationService/GetInfluxDBIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetInfluxDBIntegrationRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetInfluxDBIntegrationResponse.FromString,
        )
    self.UpdateInfluxDBIntegration = channel.unary_unary(
        '/api.ApplicationService/UpdateInfluxDBIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.UpdateInfluxDBIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteInfluxDBIntegration = channel.unary_unary(
        '/api.ApplicationService/DeleteInfluxDBIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.DeleteInfluxDBIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CreateThingsBoardIntegration = channel.unary_unary(
        '/api.ApplicationService/CreateThingsBoardIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateThingsBoardIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetThingsBoardIntegration = channel.unary_unary(
        '/api.ApplicationService/GetThingsBoardIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetThingsBoardIntegrationRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetThingsBoardIntegrationResponse.FromString,
        )
    self.UpdateThingsBoardIntegration = channel.unary_unary(
        '/api.ApplicationService/UpdateThingsBoardIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.UpdateThingsBoardIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteThingsBoardIntegration = channel.unary_unary(
        '/api.ApplicationService/DeleteThingsBoardIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.DeleteThingsBoardIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CreateMyDevicesIntegration = channel.unary_unary(
        '/api.ApplicationService/CreateMyDevicesIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateMyDevicesIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetMyDevicesIntegration = channel.unary_unary(
        '/api.ApplicationService/GetMyDevicesIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetMyDevicesIntegrationRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetMyDevicesIntegrationResponse.FromString,
        )
    self.UpdateMyDevicesIntegration = channel.unary_unary(
        '/api.ApplicationService/UpdateMyDevicesIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.UpdateMyDevicesIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteMyDevicesIntegration = channel.unary_unary(
        '/api.ApplicationService/DeleteMyDevicesIntegration',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.DeleteMyDevicesIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListIntegrations = channel.unary_unary(
        '/api.ApplicationService/ListIntegrations',
        request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.ListIntegrationRequest.SerializeToString,
        response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.ListIntegrationResponse.FromString,
        )


class ApplicationServiceServicer(object):
  """ApplicationService is the service managing applications.
  """

  def Create(self, request, context):
    """Create creates the given application.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get returns the requested application.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Update updates the given application.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Delete deletes the given application.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """List lists the available applications.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateHTTPIntegration(self, request, context):
    """CreateHTTPIntegration creates a HTTP application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHTTPIntegration(self, request, context):
    """GetHTTPIntegration returns the HTTP application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateHTTPIntegration(self, request, context):
    """UpdateHTTPIntegration updates the HTTP application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteHTTPIntegration(self, request, context):
    """DeleteIntegration deletes the HTTP application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateInfluxDBIntegration(self, request, context):
    """CreateInfluxDBIntegration create an InfluxDB application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetInfluxDBIntegration(self, request, context):
    """GetInfluxDBIntegration returns the InfluxDB application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateInfluxDBIntegration(self, request, context):
    """UpdateInfluxDBIntegration updates the InfluxDB application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteInfluxDBIntegration(self, request, context):
    """DeleteInfluxDBIntegration deletes the InfluxDB application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateThingsBoardIntegration(self, request, context):
    """CreateThingsBoardIntegration creates a ThingsBoard application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetThingsBoardIntegration(self, request, context):
    """GetThingsBoardIntegration returns the ThingsBoard application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateThingsBoardIntegration(self, request, context):
    """UpdateThingsBoardIntegration updates the ThingsBoard application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteThingsBoardIntegration(self, request, context):
    """DeleteThingsBoardIntegration deletes the ThingsBoard application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateMyDevicesIntegration(self, request, context):
    """CreateMyDevicesIntegration creates a MyDevices application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMyDevicesIntegration(self, request, context):
    """GetMyDevicesIntegration returns the MyDevices application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateMyDevicesIntegration(self, request, context):
    """UpdateMyDevicesIntegration updates the MyDevices application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteMyDevicesIntegration(self, request, context):
    """DeleteMyDevicesIntegration deletes the MyDevices application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListIntegrations(self, request, context):
    """ListIntegrations lists all configured integrations.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ApplicationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateApplicationRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateApplicationResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetApplicationRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetApplicationResponse.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.UpdateApplicationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.DeleteApplicationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.ListApplicationRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.ListApplicationResponse.SerializeToString,
      ),
      'CreateHTTPIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.CreateHTTPIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateHTTPIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetHTTPIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.GetHTTPIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetHTTPIntegrationRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetHTTPIntegrationResponse.SerializeToString,
      ),
      'UpdateHTTPIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateHTTPIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.UpdateHTTPIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteHTTPIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteHTTPIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.DeleteHTTPIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CreateInfluxDBIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.CreateInfluxDBIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateInfluxDBIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetInfluxDBIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.GetInfluxDBIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetInfluxDBIntegrationRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetInfluxDBIntegrationResponse.SerializeToString,
      ),
      'UpdateInfluxDBIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateInfluxDBIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.UpdateInfluxDBIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteInfluxDBIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteInfluxDBIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.DeleteInfluxDBIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CreateThingsBoardIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.CreateThingsBoardIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateThingsBoardIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetThingsBoardIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.GetThingsBoardIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetThingsBoardIntegrationRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetThingsBoardIntegrationResponse.SerializeToString,
      ),
      'UpdateThingsBoardIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateThingsBoardIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.UpdateThingsBoardIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteThingsBoardIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteThingsBoardIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.DeleteThingsBoardIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CreateMyDevicesIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.CreateMyDevicesIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.CreateMyDevicesIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetMyDevicesIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.GetMyDevicesIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetMyDevicesIntegrationRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.GetMyDevicesIntegrationResponse.SerializeToString,
      ),
      'UpdateMyDevicesIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateMyDevicesIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.UpdateMyDevicesIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteMyDevicesIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteMyDevicesIntegration,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.DeleteMyDevicesIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListIntegrations': grpc.unary_unary_rpc_method_handler(
          servicer.ListIntegrations,
          request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.ListIntegrationRequest.FromString,
          response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_application__pb2.ListIntegrationResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.ApplicationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))