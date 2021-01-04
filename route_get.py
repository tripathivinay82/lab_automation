#!/usr/bin/python
#
# Copyright (c) 2020 Juniper Networks, Inc.
# All rights reserved.
#

import time, sys, glob
import os, random
import optparse
import netaddr
import socket
import grpc

from google.protobuf import json_format as jsonf

import authentication_service_pb2 as auth_svc
import authentication_service_pb2_grpc
import rib_service_pb2 as rib_svc
import rib_service_pb2_grpc
import flexible_tunnel_profile_pb2 as flex_tnl
import prpd_common_pb2 as prpd
import jnx_addr_pb2 as jnx_addr

TIMEOUT = 60
BATCH_SIZE = 1000

#
# Command line options parsing
#
parser = optparse.OptionParser()
parser.add_option('-H', '--host', action="store", dest="HOST", 
                  help="Server host address", default="localhost")
parser.add_option('-P', '--port', action="store", dest="PORT", 
                  help="Server GRPC port", default="50051")
parser.add_option('-U', '--user', action="store", dest="USER", 
                  help="JET username", default="user")
parser.add_option('-W', '--password', action="store", dest="PASSWORD", 
                  help="JET password", default="password")
parser.add_option('-C', '--client', action="store", dest="CLIENT_ID", 
                  help="JET client ID", default="app1")
parser.add_option('-F', '--file', action="store", dest="FILE", 
                  help="JSON output file", default="config.json")
parser.add_option('-T', '--tag', action="store", dest="TAG", 
                  help="Tag to match", default=None)
parser.add_option('-R', '--table', action="store", dest="TABLE", 
                  help="RIB Table to read", default="inet.0")

(options, args) = parser.parse_args()

def Main():

    # Connect and Authenticate
    conn = grpc.insecure_channel('%s:%d' % (options.HOST, int(options.PORT)))
    auth_stub = authentication_service_pb2_grpc.LoginStub(conn)
    login = auth_stub.LoginCheck(
            auth_svc.LoginRequest(user_name=options.USER,
                                  password=options.PASSWORD,
                                  client_id=options.CLIENT_ID), 
            TIMEOUT)
    if login:
        print "Successfully connected to server %s:%s as %s" % (
            options.HOST, options.PORT, options.USER)
    else:
        print "ERROR: Login to server server %s:%s as %s FAILED" % (
            options.HOST, options.PORT, options.USER)
        sys.exit(1)

    # Create the RIB service stub
    rib = rib_service_pb2_grpc.RibStub(conn)

    # Open the output file
    f = open(options.FILE, "wb")

    # Make the request for all IPv4 routes in the given table
    
    match = rib_svc.RouteMatchFields(
            dest_prefix = prpd.NetworkAddress(
                    inet = jnx_addr.IpAddress(addr_string = "0.0.0.0")),
            dest_prefix_len = 0,
            table = prpd.RouteTable(
                rtt_name = prpd.RouteTableName(name = options.TABLE)))
    if (options.TAG):
        match_tags = {}
        match_tags[0] = rib_svc.RouteAttributeUint32(value = int(options.TAG))
        ext_match = rib_svc.RouteExtendedMatchFields(tags = match_tags)
    else:
        ext_match = None
    this_req = rib_svc.RouteGetRequest(key = match,
                                       extended_match = ext_match,
                                       match_type = rib_svc.EXACT_OR_LONGER,
                                       route_count = 1000)
    getStream = rib.RouteGet(this_req, TIMEOUT)

    rt_count = 0
    cummulative_reply = rib_svc.RouteGetReply()
    for i in getStream:
        #print "Read reply with %d routes" % len(i.routes)
        #print i
        cummulative_reply.status = i.status
        cummulative_reply.routes.extend(i.routes)
        rt_count += len(i.routes)
            
    f.write(jsonf.MessageToJson(cummulative_reply))
    f.close()
    print "Wrote %d JSON routes to %s" % (rt_count, options.FILE)

    
if __name__ == '__main__':
    Main()


