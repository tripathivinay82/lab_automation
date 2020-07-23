# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import flexible_tunnel_service_pb2 as flexible__tunnel__service__pb2


class FlexibleTunnelStub(object):
    """*
    JET RPC service providing operations to manage flexible tunnel profiles
    as independent objects decopuled from routes that may use them.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FlexibleTunnelAdd = channel.unary_unary(
                '/routing.FlexibleTunnel/FlexibleTunnelAdd',
                request_serializer=flexible__tunnel__service__pb2.FlexibleTunnelAddRequest.SerializeToString,
                response_deserializer=flexible__tunnel__service__pb2.FlexibleTunnelAddResponse.FromString,
                )
        self.FlexibleTunnelUpdate = channel.unary_unary(
                '/routing.FlexibleTunnel/FlexibleTunnelUpdate',
                request_serializer=flexible__tunnel__service__pb2.FlexibleTunnelUpdateRequest.SerializeToString,
                response_deserializer=flexible__tunnel__service__pb2.FlexibleTunnelUpdateResponse.FromString,
                )
        self.FlexibleTunnelDelete = channel.unary_unary(
                '/routing.FlexibleTunnel/FlexibleTunnelDelete',
                request_serializer=flexible__tunnel__service__pb2.FlexibleTunnelDeleteRequest.SerializeToString,
                response_deserializer=flexible__tunnel__service__pb2.FlexibleTunnelDeleteResponse.FromString,
                )
        self.FlexibleTunnelGet = channel.unary_unary(
                '/routing.FlexibleTunnel/FlexibleTunnelGet',
                request_serializer=flexible__tunnel__service__pb2.FlexibleTunnelGetRequest.SerializeToString,
                response_deserializer=flexible__tunnel__service__pb2.FlexibleTunnelGetResponse.FromString,
                )


class FlexibleTunnelServicer(object):
    """*
    JET RPC service providing operations to manage flexible tunnel profiles
    as independent objects decopuled from routes that may use them.
    """

    def FlexibleTunnelAdd(self, request, context):
        """*
        Request to add new flexible tunnel profiles.
        An error will be returned if either a profile with the given name
        or a profile with conflicting tunnel attributes already exists.
        See the specific tunnel attributes for the description of conflicting
        attributes for that tunnel type.

        The request may contain from one to 1000 tunnel profiles.
        If the request contains multiple tunnel profiles, the profiles will
        be processed in the order given and the first error encountered will
        cause the request to abort.
        The API always returns the final status (success or first error
        encountered) and the number of profiles that were successfully
        updated prior to any error or full completion of the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FlexibleTunnelUpdate(self, request, context):
        """*
        Request to add new flexible tunnel profiles, or update the profile(s)
        if profiles matching the given name already exists. An error will be
        returned if a different profile with conflicting tunnel attributes
        already exists. See the specific tunnel attributes for the description
        of conflicting attributes for that tunnel type..

        The request may contain from one to 1000 tunnel profiles.

        If the request contains multiple tunnel profiles, the profiles will
        be processed in the order given and the first error encountered will
        cause the request to abort.
        The API always returns the final status (success or first error
        encountered) and the number of profiles that were successfully
        updated prior to any error or full completion of the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FlexibleTunnelDelete(self, request, context):
        """*
        Request to delete existing flexible tunnel profiles by name.

        The request may contain from one to 1000 tunnel profiles.

        If the request contains multiple tunnel profiles, the profiles will
        be processed in the order given and the first error encountered will
        cause the request to abort.
        The API always returns the final status (success or first error
        encountered) and the number of profiles that were successfully
        deleted prior to any error or full completion of the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FlexibleTunnelGet(self, request, context):
        """*
        Request to query the paramaters of an existing flexible tunnel
        profile with the given name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FlexibleTunnelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FlexibleTunnelAdd': grpc.unary_unary_rpc_method_handler(
                    servicer.FlexibleTunnelAdd,
                    request_deserializer=flexible__tunnel__service__pb2.FlexibleTunnelAddRequest.FromString,
                    response_serializer=flexible__tunnel__service__pb2.FlexibleTunnelAddResponse.SerializeToString,
            ),
            'FlexibleTunnelUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.FlexibleTunnelUpdate,
                    request_deserializer=flexible__tunnel__service__pb2.FlexibleTunnelUpdateRequest.FromString,
                    response_serializer=flexible__tunnel__service__pb2.FlexibleTunnelUpdateResponse.SerializeToString,
            ),
            'FlexibleTunnelDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.FlexibleTunnelDelete,
                    request_deserializer=flexible__tunnel__service__pb2.FlexibleTunnelDeleteRequest.FromString,
                    response_serializer=flexible__tunnel__service__pb2.FlexibleTunnelDeleteResponse.SerializeToString,
            ),
            'FlexibleTunnelGet': grpc.unary_unary_rpc_method_handler(
                    servicer.FlexibleTunnelGet,
                    request_deserializer=flexible__tunnel__service__pb2.FlexibleTunnelGetRequest.FromString,
                    response_serializer=flexible__tunnel__service__pb2.FlexibleTunnelGetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'routing.FlexibleTunnel', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FlexibleTunnel(object):
    """*
    JET RPC service providing operations to manage flexible tunnel profiles
    as independent objects decopuled from routes that may use them.
    """

    @staticmethod
    def FlexibleTunnelAdd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routing.FlexibleTunnel/FlexibleTunnelAdd',
            flexible__tunnel__service__pb2.FlexibleTunnelAddRequest.SerializeToString,
            flexible__tunnel__service__pb2.FlexibleTunnelAddResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FlexibleTunnelUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routing.FlexibleTunnel/FlexibleTunnelUpdate',
            flexible__tunnel__service__pb2.FlexibleTunnelUpdateRequest.SerializeToString,
            flexible__tunnel__service__pb2.FlexibleTunnelUpdateResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FlexibleTunnelDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routing.FlexibleTunnel/FlexibleTunnelDelete',
            flexible__tunnel__service__pb2.FlexibleTunnelDeleteRequest.SerializeToString,
            flexible__tunnel__service__pb2.FlexibleTunnelDeleteResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FlexibleTunnelGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routing.FlexibleTunnel/FlexibleTunnelGet',
            flexible__tunnel__service__pb2.FlexibleTunnelGetRequest.SerializeToString,
            flexible__tunnel__service__pb2.FlexibleTunnelGetResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
