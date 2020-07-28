#!/usr/bin/python3

import paramiko
import getpass
import sys
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from lxml import etree
import jxmlease
import re
from jnpr.junos.utils.fs import FS
from jnpr.junos.exception import *
import multiprocessing
import time
import os 
import subprocess

NUM_PROCESSES = 1 

def vmm_start_config():
    '''
    This function sill start the VMM and load the configuration
    '''

    hostname = str(input("Please Enter The VMM POD Server IP: ")) or "10.51.246.43"
    userName = str(input("Please Enter The VMM POD Server User Name: ")).strip() or "vinayt"
    userPass = getpass.getpass() 
    vmmConfig = str(input("Please Enter The VMM Config File Location and Name: ")) or "/vmm/data/user_disks/vinayt/msft/exr/vmx.conf"
    vmmCmd = "vmm config " + vmmConfig + " -g vmm-default"
    
    try:
        # initialize the SSH client
        client = paramiko.SSHClient()
        # add to known hosts
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Connect to server
        client.connect(hostname=hostname, username=userName, password=userPass)
    except:
        print("Cannot Connect to VMM Server")
        sys.exit()

    try: 
        stdin, stdout, stderr = client.exec_command('vmm unbind')                                    
        time.sleep(60)
        out = stdout.read().decode().split("\n")
        for line in out:
            if re.search('Warning|error|Fatal',line):
                print(f"Error During VMM Unbind Execution! Reason: {out}")
                return False
        stdin, stdout, stderr = client.exec_command(vmmCmd)
        time.sleep(60)
        out = stdout.read().decode().split("\n")
        for line in out:
            if re.search('error|Fatal|Warning',line):
                print(f"Error During VMM Config Execution! Reason: {out}")
                return False
        stdin, stdout, stderr = client.exec_command('vmm start')
        time.sleep(120)
        out = stdout.read().decode().split("\n")
        for line in out:
            if re.search('error|Fatal|Warning',line):
                print(f"Error During VMM Start! Reason: {out}")
                return False
    except:
        print(out)
        print(err)
        sys.exit()
    else:
        count = 1
        router_dict = {} 

        while count <= 30:

            vm_status_all = []
            stdin, stdout, stderr = client.exec_command('vmm ping')
            out = stdout.read().decode().split("\n")
            del out[-1] #Remove last empty element of list 'out' created after split 
            print(f'{"VM Name":<20}{"VM IP":<0}{"VM Status":>20}')
           
            for line in out:
                #print(f"Count {count} line: {line}")
                vm_name = line.split(" ")[0]
                vm_ip = line.split(" ")[1]
                vm_state = line.split(" ")[2]
                vm_status_all.append(vm_state)
                if count is 1 and '_re' in vm_name:
                    router_dict[vm_name] = vm_ip
                #print(f"Router List: {router_dict}")
                print(f"{vm_name:<20}{vm_ip:<10}{vm_state:>20}")

            if 'no-response' in vm_status_all:
                print("VMs are still coming up..lets wait..") 
            elif 'no-response' not in vm_status_all and vm_status_all:
                print("All VMs are alive")
                client.close()
                return router_dict            
            elif count is '30':
                print(f"VMs did not come up in {count} attempts! Stopping further checks..")
                client.exec_command('vmm unbind')
                client.close()
                return False
            else:
                print("Unintended Result..Please debug the script")
                client.exec_command('vmm unbind')
                client.close()
                return False

            time.sleep(60) 
            count += 1 
        

def check_router(hostname):
    '''
    Verify the router states
    '''

    username = 'regress'
    password = 'MaRtInI'

    print(f"Checking hostname {hostname}")

    try:
        with Device(host=hostname, user=username, password=password, normalize=True) as dev:
            dev.open()
            rpc = dev.rpc.get_fpc_information()
            rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
    except ConnectRefusedError: 
        print("%s: Error - Device connection refused!" % hostname)
    except ConnectTimeoutError:
        print("%s: Error - Device connection timed out!" % hostname)
    except ConnectAuthError:
        print("%s: Error - Authentication failure!" % hostname)

    result = jxmlease.parse(rpc_xml)

    state=[]
    for handle in result['fpc-information']['fpc']:
        state.extend([handle['state']])
        if handle['state'] == 'Empty':
           pass
        elif handle['state'] == 'Online' and handle['slot'] == '0' or handle['slot'] == '1':
           print(f"FPC state is {handle['state']} for slot {handle['slot']}")
        else:
           print("Unkown FPC state..please investigate")

    if 'Online' in state:
        return True 
    else:
        return False 

def check_protocols(hostname):
    '''
    Verify the protocols after initial setup bringup
    '''

    print(f"Hostname: {hostname}")

    username = 'regress'
    password = 'MaRtInI'

    try:
        with Device(host=hostname, user=username, password=password, normalize=True) as dev:
            dev.open()
            retVal=dev.facts
            if retVal['hostname'] == 'CE-Customer' or retVal['hostname'] == 'CE-Server':
                print(f"**** Checking Protocols for Device: {retVal['hostname']} ****")
                rpc = dev.rpc.get_ospf_neighbor_information()
                rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
                result = jxmlease.parse(rpc_xml)
                print('Checking neighbor with IP address: ' + result['ospf-neighbor-information']['ospf-neighbor']['neighbor-address'])
                print(result['ospf-neighbor-information']['ospf-neighbor']['interface-name'])
                print(result['ospf-neighbor-information']['ospf-neighbor']['ospf-neighbor-state'])
            elif retVal['hostname'] == 'DCGW': 
                print(f"**** Checking Protocols for Device: {retVal['hostname']} ****")
                rpc = dev.rpc.get_ospf_neighbor_information()
                rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
                result = jxmlease.parse(rpc_xml)
                print('Checking neighbor with IP address: ' + result['ospf-neighbor-information']['ospf-neighbor']['neighbor-address'])
                print(result['ospf-neighbor-information']['ospf-neighbor']['interface-name'])
                print(result['ospf-neighbor-information']['ospf-neighbor']['ospf-neighbor-state'])
                rpc = dev.rpc.get_bgp_summary_information()
                rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
                result = jxmlease.parse(rpc_xml)
                for neighbor in result['bgp-information']['bgp-peer']:
                    print('Checking peer with IP address: ' + neighbor['peer-address'])
                    print(neighbor['peer-as'])
                    print(neighbor['peer-state'])
                    print(neighbor['elapsed-time'])
            elif retVal['hostname'] == 'exr02.chg':
                print(f"*** Checking Protocols for Device: {retVal['hostname']} ****")
                rpc = dev.rpc.get_ospf_neighbor_information()
                rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
                result = jxmlease.parse(rpc_xml)
                for neighbor in result['ospf-neighbor-information']['ospf-neighbor']:
                    print('Checking neighbor with IP address: ' + neighbor['neighbor-address'])
                    print(neighbor['interface-name'])
                    print(neighbor['ospf-neighbor-state'])
                rpc = dev.rpc.get_bgp_summary_information()
                rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
                result = jxmlease.parse(rpc_xml)
                for neighbor in result['bgp-information']['bgp-peer']:
                    print('Checking peer with IP address: ' + neighbor['peer-address'])
                    print(neighbor['peer-as'])
                    print(neighbor['peer-state'])
                    print(neighbor['elapsed-time'])
            elif retVal['hostname'] == 'IER':
                print(f"****Checking Protocols for Device: {retVal['hostname']}****")
                rpc = dev.rpc.get_ospf_neighbor_information()
                rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
                result = jxmlease.parse(rpc_xml)
                for neighbor in result['ospf-neighbor-information']['ospf-neighbor']:
                    print('Checking neighbor with IP address: ' + neighbor['neighbor-address'])
                    print(neighbor['interface-name'])
                    print(neighbor['ospf-neighbor-state'])
            else:
                print(f"Incorrect Hostname {retVal['hostname']}" )
                return False
    except ConnectRefusedError:
        print("%s: Error - Device connection refused!" % hostname)
        return False
    except ConnectTimeoutError:
        print("%s: Error - Device connection timed out!" % hostname)
        return False
    except ConnectAuthError:
        print("%s: Error - Authentication failure!" % hostname)
        return False

    return True 

def config_flex_route(hostname):
    '''
    This function will configure encap and decap profile for flex route on EXR and DCGW
    '''
    
    print(f"Hostname: {hostname}")

    username = 'regress'
    password = 'MaRtInI'

    try:
        with Device(host=hostname, user=username, password=password, normalize=True) as dev:
            dev.open()
            retVal=dev.facts
            if retVal['hostname'] == 'exr02.chg':
                retVal1 = subprocess.run(["python", "route_inject_p3.py", "-H", hostname, "-P", "50051", "-U", username, "-W", password, "-F", "encap_tunnel_profile-ipv4-vxlanv6_exr.json"], stdout=subprocess.DEVNULL, timeout=5)
                retVal2 = subprocess.run(["python", "decap_inject.py", "-H", hostname, "-P", "50051", "-U", username, "-W", password, "-F", "decap_tunnel_profile_v6_exr.json"], stdout=subprocess.DEVNULL, timeout=5)
                if retVal1.returncode is not 0 or retVal2.returncode is not 0:
                    print(f"Oops!!Subprocess returned unexpected value...retVal1: {retVal1.returncode}, retVal2:{retVal2.returncode}")
                    return False
            elif retVal['hostname'] == 'DCGW':
                retVal1 = subprocess.run(["python", "route_inject_p3.py", "-H", hostname, "-P", "50051", "-U", username, "-W", password, "-F", "encap_tunnel_profile-ipv4-vxlanv6_dcgw.json"], stdout=subprocess.DEVNULL, timeout=5)
                retVal2 = subprocess.run(["python", "decap_inject.py", "-H", hostname, "-P", "50051", "-U", username, "-W", password, "-F", "decap_tunnel_profile_v6_dcgw.json"], stdout=subprocess.DEVNULL, timeout=5)
                if retVal1.returncode is not 0 or retVal2.returncode is not 0:
                    print(f"Oops!!Subprocess returned unexpected value...retVal1: {retVal1.returncode}, retVal2:{retVal2.returncode}")
                    return False
            else:
                print("Oops! Incorrect Hostname..Please investigate..")
                dev.close()
                return False
    except ConnectRefusedError:
        print("%s: Error - Device connection refused!" % hostname)
        return False
    except ConnectTimeoutError:
        print("%s: Error - Device connection timed out!" % hostname)
        return False
    except ConnectAuthError:
        print("%s: Error - Authentication failure!" % hostname)
        return False

    return True


def ucast_flex_route_checker(hostname):
    '''
    This function will perform following tasks: 
    1) check if route is a unicast flex route or not 
    2) if flex route, check programming at RE and PFE 
    '''


def ulist_flex_route_checker(hostname,static_route,next_hops):
    '''
    This function will perform following tasks: 

    1) check if route is a unlist pointing to flex route NH or not 
    2) if NH are flex route, check programming of all NHs at RE and PFE 
    '''

    print(f"Hostname: {hostname}")

    username = 'regress'
    password = 'MaRtInI'

    try:
        with Device(host=hostname, user=username, password=password, normalize=True) as dev:
            dev.open()
    except ConnectRefusedError:
        print("%s: Error - Device connection refused!" % hostname)
        return False
    except ConnectTimeoutError:
        print("%s: Error - Device connection timed out!" % hostname)
        return False
    except ConnectAuthError:
        print("%s: Error - Authentication failure!" % hostname)
        return False

    return True


def ecmp_over_flex_route_checker(hostname):
    '''
    This function will perform following tasks: 
    1) Check if the route is unicast/unilist 
    3) verify the route programming in RE and PFE
    '''
 
    print(f"ecmp_over_flex_route_checker: Hostname: {hostname}")

    username = 'regress'
    password = 'MaRtInI'

    #try:
    #    with Device(host=hostname, user=username, password=password, normalize=True) as dev:
    #        dev.open()

    #except ConnectRefusedError:
    #    print("%s: Error - Device connection refused!" % hostname)
    #    return False
    #except ConnectTimeoutError:
    #    print("%s: Error - Device connection timed out!" % hostname)
    #    return False
    #except ConnectAuthError:
    #    print("%s: Error - Authentication failure!" % hostname)
    #    return False

    dev = Device(host=hostname, user=username, password=password, normalize=True)
    dev.open()

    rpc=dev.rpc.get_config()
    rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
    result = jxmlease.parse(rpc_xml)

    static_route = re.findall(r'\d+.\d+.\d+.\d+',str(result['configuration']['routing-instances']['instance']['routing-options']['static']['route']['name']))
    next_hops = re.findall(r'\d+.\d+.\d+.\d+',str(result['configuration']['routing-instances']['instance']['routing-options']['static']['route']['next-hop']))

    # Collect data from indirect NH
    rpc=dev.rpc.get_route_information(destination=static_route,table='vpnA.inet',extensive=True,active_path=True)
    result=rpc.xpath(".//rt-entry/protocol-nh[nh-type]")
    #Generate a dictionary with all the values
    nested_dict = {}
    for count,value in enumerate(result):
        dict_count = {}
        for cnt,val in enumerate(value):
            dict_count[cnt] = val.text
        #print(f"New Dict Created; Name and Value: {dict_count}") 
        nested_dict[count] = dict_count
             
    print(f"Nested Dict {nested_dict}")
    #Generate a new dict with key value as NH IP 
    inh_dict = {}
    nh_col = []
    for key,value in nested_dict.items():
        print(value)
        nh_col.append(value[0])                                 # NH IP 
        nh_col.append(value[1].split()[1])                      # Indirect NHID 
        nh_col.append(value[3])                                 # NH Type
        nh_col.append(value[4])                                 # Unicast NH ID
        nh_col.append(value[6].split()[3])                     # RI Name
        nh_col.append(value[6].split()[13])                    # FTI Name
        inh_dict[value[0]] = nh_col                           # assign list as value of dict
        nh_col = []                                             # Empty the list

    print(inh_dict)        



    # Collect data from unicast NH
    ucast_dict = {} 
    for ip in next_hops:
        rpc=dev.rpc.get_route_information(destination=ip,table='vpnA.inet',extensive=True,active_path=True)
        ucast_dict[ip] = [rpc.xpath(".//table-name")[0].text]
        ucast_dict[ip].append(rpc.xpath(".//rt-destination")[0].text)
        ucast_dict[ip].append(rpc.xpath(".//nh-index")[0].text)
        ucast_dict[ip].append(rpc.xpath(".//via")[0].text)
        ucast_dict[ip].append(rpc.xpath(".//rt-entry-opaque-data")[0].text.split()[0])
        ucast_dict[ip].append(rpc.xpath(".//rt-entry-opaque-data")[0].text.split()[6])
        ucast_dict[ip].append(rpc.xpath(".//rt-entry-opaque-data")[0].text.split()[8])
        ucast_dict[ip].append(rpc.xpath(".//rt-entry-opaque-data")[0].text.split()[9])
        ucast_dict[ip].append(rpc.xpath(".//rt-entry-opaque-data")[0].text.split()[11])
        ucast_dict[ip].append(rpc.xpath(".//rt-entry-opaque-data")[0].text.split()[23])
        ucast_dict[ip].append(rpc.xpath(".//rt-entry-opaque-data")[0].text.split()[27])
        ucast_dict[ip].append(rpc.xpath(".//rt-entry-opaque-data")[0].text.split()[14])
        

    return True    



def config_change(hostname):
    '''
    Modify the gRPC connection configuration
    '''

    print(f"Hostname: {hostname}")

    username = 'regress'
    password = 'MaRtInI'

    try:
        with Device(host=hostname, user=username, password=password, normalize=True) as dev:
            dev.open()
            rpc=dev.rpc.get_interface_information(interface_name='fxp0')
            rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
            result = jxmlease.parse(rpc_xml)
            new_ip = result['interface-information']['physical-interface']['logical-interface']['address-family']['interface-address']['ifa-local']
            cmd='set system services extension-service request-response grpc clear-text address ' + str(new_ip)
            with Config(dev, mode='private') as cu:  
                cu.load(cmd, format='set')
                cu.pdiff()
                cu.commit()
            dev.close()
    except ConnectRefusedError:
        print("%s: Error - Device connection refused!" % hostname)
        return False
    except ConnectTimeoutError:
        print("%s: Error - Device connection timed out!" % hostname)
        return False
    except ConnectAuthError:
        print("%s: Error - Authentication failure!" % hostname)
        return False

    return True 
           
def main():
    '''
    This is the main function...More details to follow

    #Run and configure VMM
    retVal = vmm_start_config()
    print(f"Return Vale: {retVal}")
    print(f"Return Vale Type: {type(retVal)}")

    if retVal is False and isinstance(inp1, bool):
        print(f"VMM Start Failed! Reason: {retVal}")
        sys.exit()
    elif isinstance(retVal, dict) and retVal:
        router_dict = retVal
        print(f"List of VMM Routers: {router_dict}")
        print("VMM Setup and Configuration Was Successful!!")
    elif retVal:
        print(f"VMM Start Failed as Router List is Empty! Return Value: {retVal}")
        sys.exit()
    else:
        print("VMM Start Failed Because of Unkown Reason! Return Value: {retVal}")
        sys.exit()

    #Lets give VMs enough time to settle down
    print("Lets Wait for 5 minutes for VMs to get stablize..")
    time.sleep(300)

'''

    hostname='10.49.103.15'
    ecmp_over_flex_route_checker(hostname)
    print("********Funtcion completed**Sleeping now*********")
    time.sleep(500)
 
    #Verify Router State and configuration 
    # ROuter list for D24.11
    #router_dict={'r1_re0': '10.49.103.152', 'r2_re0': '10.49.103.15', 'r3_re0': '10.49.103.148', 'r4_re0': '10.49.101.64', 'r5_re0': '10.49.101.62'}
    time_start = time.time()
    with multiprocessing.Pool(processes=NUM_PROCESSES) as process_pool: 
        retVal=process_pool.map(check_router, router_dict.values()) 
        process_pool.close() 
        process_pool.join()
    print(f"retVal {retVal}")
    print("Multiprocessing Finished in %f sec." % (time.time() - time_start)) 

    if 'False' not in retVal:
        print("Router Check Passed..") 
    else:
        print("!!!Router Check Failed..Please debug")
        return False

    #Verify Protocols Stateonfiguration 
    time_start = time.time()
    with multiprocessing.Pool(processes=NUM_PROCESSES) as process_pool:
        retVal=process_pool.map(check_protocols, router_dict.values())
        process_pool.close()
        process_pool.join()
    print(f"retVal {retVal}")
    print("Multiprocessing Finished in %f sec." % (time.time() - time_start))

    if 'False' not in retVal:
        print("Protocols Check Passed..")
    else:
        print("!!!Protocols Check Failed..Please debug")
        return False

    #Modify the JET configuration change to reflect to new fxp0 IP
    if config_change(router_dict['r2_re0']) and config_change(router_dict['r4_re0']):
        print("Router Config Successful!!")
    else:
        print("Oops!!Router Config Failed..")

    # Configure Flex Route from controller
    if config_flex_route(router_dict['r2_re0']) and config_flex_route(router_dict['r4_re0']):
        print("Flex Route programming Successful!!")
    else:
        print("Oops!!Flex Route programming failed!..")

if __name__ == "__main__":
    main()    

