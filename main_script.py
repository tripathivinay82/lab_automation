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
import numpy as np
import pandas as pd
from jnpr.junos.utils.scp import SCP

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
    print(f'Final VMM Config Command: {vmmCmd}')
    
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
                print('Neighbor IP: ' + result['ospf-neighbor-information']['ospf-neighbor']['neighbor-address'] + ' ' + result['ospf-neighbor-information']['ospf-neighbor']['interface-name'] + ' ' + result['ospf-neighbor-information']['ospf-neighbor']['ospf-neighbor-state'])
            elif retVal['hostname'] == 'DCGW': 
                print(f"**** Checking Protocols for Device: {retVal['hostname']} ****")
                rpc = dev.rpc.get_ospf_neighbor_information()
                rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
                result = jxmlease.parse(rpc_xml)
                print('Neighbor IP: ' + result['ospf-neighbor-information']['ospf-neighbor']['neighbor-address'] + ' ' + result['ospf-neighbor-information']['ospf-neighbor']['interface-name'] + ' ' + result['ospf-neighbor-information']['ospf-neighbor']['ospf-neighbor-state'])
                rpc = dev.rpc.get_bgp_summary_information()
                rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
                result = jxmlease.parse(rpc_xml)
                for neighbor in result['bgp-information']['bgp-peer']:
                    print('Neighbor IP: ' + neighbor['peer-address'] + ' ' + neighbor['peer-as'] + ' ' + neighbor['peer-state'] + ' ' + neighbor['elapsed-time'])
            elif retVal['hostname'] == 'exr02.chg':
                print(f"*** Checking Protocols for Device: {retVal['hostname']} ****")
                rpc = dev.rpc.get_ospf_neighbor_information()
                rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
                result = jxmlease.parse(rpc_xml)
                for neighbor in result['ospf-neighbor-information']['ospf-neighbor']:
                    print('Neighbor IP: ' + neighbor['neighbor-address'] + ' ' + neighbor['interface-name'] + ' ' + neighbor['ospf-neighbor-state'])
                rpc = dev.rpc.get_bgp_summary_information()
                rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
                result = jxmlease.parse(rpc_xml)
                for neighbor in result['bgp-information']['bgp-peer']:
                    print('Neighbor IP: ' + neighbor['peer-address'] + ' ' + neighbor['peer-as'] + ' ' + neighbor['peer-state'] + ' ' + neighbor['elapsed-time'])
            elif retVal['hostname'] == 'IER':
                print(f"****Checking Protocols for Device: {retVal['hostname']}****")
                rpc = dev.rpc.get_ospf_neighbor_information()
                rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
                result = jxmlease.parse(rpc_xml)
                for neighbor in result['ospf-neighbor-information']['ospf-neighbor']:
                    print('Neighbor IP: ' + neighbor['neighbor-address'] + ' ' + neighbor['interface-name'] + ' ' + neighbor['ospf-neighbor-state'])
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
                retVal1 = subprocess.run([sys.executable, "route_inject_p3.py", "-H", hostname, "-P", "50051", "-U", username, "-W", password, "-F", "encap_tunnel_profile-ipv4-vxlanv6_exr.json"], stdout=subprocess.DEVNULL, timeout=5)
                retVal2 = subprocess.run([sys.executable, "decap_inject.py", "-H", hostname, "-P", "50051", "-U", username, "-W", password, "-F", "decap_tunnel_profile_v6_exr.json"], stdout=subprocess.DEVNULL, timeout=5)
                if retVal1.returncode is not 0 or retVal2.returncode is not 0:
                    print(f"Oops!!Subprocess returned unexpected value...retVal1: {retVal1.returncode}, retVal2:{retVal2.returncode}")
                    return False
            elif retVal['hostname'] == 'DCGW':
                retVal1 = subprocess.run([sys.executable, "route_inject_p3.py", "-H", hostname, "-P", "50051", "-U", username, "-W", password, "-F", "encap_tunnel_profile-ipv4-vxlanv6_dcgw.json"], stdout=subprocess.DEVNULL, timeout=5)
                retVal2 = subprocess.run([sys.executable, "decap_inject.py", "-H", hostname, "-P", "50051", "-U", username, "-W", password, "-F", "decap_tunnel_profile_v6_dcgw.json"], stdout=subprocess.DEVNULL, timeout=5)
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


def ecmp_over_flex_route(hostname):
    '''
    This function will perform following tasks: 
    1) Check if the route is unicast/unilist 
    3) verify the route programming in RE and PFE
    '''
 
    print(f"Hostname: {hostname}")

    username = 'regress'
    password = 'MaRtInI'

    dev = Device(host=hostname, user=username, password=password, normalize=True)
    dev.open()

    rpc=dev.rpc.get_config()
    rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
    result = jxmlease.parse(rpc_xml)

    static_route = re.findall(r'\d+.\d+.\d+.\d+',str(result['configuration']['routing-instances']['instance']['routing-options']['static']['route']['name']))
    next_hops = re.findall(r'\d+.\d+.\d+.\d+',str(result['configuration']['routing-instances']['instance']['routing-options']['static']['route']['next-hop']))

    # Collect data related to static route and their NH
    rpc=dev.rpc.get_route_information(destination=static_route,table='vpnA.inet',extensive=True,active_path=True,)
    sroute_dict = {}

    for ip in next_hops:
        inh =rpc.xpath('.//rt-entry/protocol-nh[to=\'' + ip + '\'][1]/indirect-nh[1]')[0].text.split(' ')[1]
        rtype=rpc.xpath('.//rt-entry/protocol-nh[to=\'' + ip + '\']/protocol-nh/nh-type[1]')[0].text
        nhindex=rpc.xpath('.//rt-entry/protocol-nh[to=\'' + ip + '\']/protocol-nh/nh-index[1]')[0].text
        rib=rpc.xpath('.//rt-entry/protocol-nh[to=\'' + ip + '\']/protocol-nh/originating-rib[1]')[0].text
        ifl=rpc.xpath('.//rt-entry/protocol-nh[to=\'' + ip + '\']/protocol-nh/nh/via[1]')[0].text
        sroute_dict[ip] = [inh, ifl, rtype, nhindex, rib]
    
    df = pd.DataFrame(sroute_dict, index=['Indirect NH', 'IFL', 'Route Type', 'NH Index', 'RT'])
    print()
    print(f'Data Collected from Static Route [RE]:')
    print(df)
    print()
    print()

    # Collect data related to static route next-hops
    ucast_dict = {}
    re_dict = {}
    for ip in next_hops:

        rpc=dev.rpc.get_route_information(destination=ip,table='vpnA.inet',extensive=True,active_path=True,)
        rtTable = rpc.xpath('.//route-table/table-name')[0].text
        nhType = rpc.xpath('.//rt-entry/nh-type')[0].text
        nhIndex = rpc.xpath('.//rt-entry/nh-index')[0].text
        ifl = rpc.xpath('.//rt-entry/nh/via')[0].text
        encap = rpc.xpath('.//rt-entry/rt-entry-opaque-data')[0].text.split(' ')[2]
        action = rpc.xpath('.//rt-entry/rt-entry-opaque-data')[0].text.split(' ')[6]
        vni = rpc.xpath('.//rt-entry/rt-entry-opaque-data')[0].text.split(' ')[12]
        spfx = rpc.xpath('.//rt-entry/rt-entry-opaque-data')[0].text.split(' ')[15].split('/')[0]
        smac = rpc.xpath('.//rt-entry/rt-entry-opaque-data')[0].text.split(' ')[26]
        dpfx = rpc.xpath('.//rt-entry/rt-entry-opaque-data')[0].text.split(' ')[29]
        dport = rpc.xpath('.//rt-entry/rt-entry-opaque-data')[0].text.split(' ')[33]
        dmac = rpc.xpath('.//rt-entry/rt-entry-opaque-data')[0].text.split(' ')[37]
        ucast_dict[ip] = [rtTable, nhType, nhIndex, ifl, encap, action, vni, spfx, smac, dpfx, dport, dmac]
        re_dict[ip] = [nhIndex, ifl, encap, vni, smac, dport, dmac] #Not able to add Src and Dst Prefi because of format diff in RE & PFE

    print(f"RE Data Captured for Comparision: {re_dict}")
    df = pd.DataFrame(ucast_dict, index=['RT', 'NH Type', 'NH Index', 'IFL', 'ENCAP', 'ACTION', 'VNI', 'Source Prefix', 'Src MAC', 'Dest Prefix', 'Dest UDP Port', 'Dest MAC'])
    print(f'Data Collected from Static Route Next-Hops [RE]:')
    print(df)
    print()
    print()

    # Collect data related to static route from Kernel
    rpc=dev.rpc.get_forwarding_table_information(destination=static_route,table='vpnA')

    destIp = rpc.xpath('.//rt-entry/rt-destination')[0].text
    destType = rpc.xpath('.//rt-entry/destination-type')[0].text

    nhType1 = rpc.xpath('.//rt-entry/nh[1]/nh-type')[0].text
    nhIndex1 = rpc.xpath('.//rt-entry/nh[1]/nh-index')[0].text

    nhType2 = rpc.xpath('.//rt-entry/nh[2]/nh-type')[0].text
    nhIndex2 = rpc.xpath('.//rt-entry/nh[2]/nh-index')[0].text
    
    nhType3 = rpc.xpath('.//rt-entry/nh[3]/nh-type')[0].text
    nhIndex3 = rpc.xpath('.//rt-entry/nh[3]/nh-index')[0].text    
    nhIfl3 = rpc.xpath('.//rt-entry/nh[3]/via')[0].text 
    
    nhType4 = rpc.xpath('.//rt-entry/nh[4]/nh-type')[0].text
    nhIndex4 = rpc.xpath('.//rt-entry/nh[4]/nh-index')[0].text
    
    nhType5 = rpc.xpath('.//rt-entry/nh[5]/nh-type')[0].text
    nhIndex5 = rpc.xpath('.//rt-entry/nh[5]/nh-index')[0].text    
    nhIfl5 = rpc.xpath('.//rt-entry/nh[5]/via')[0].text
    
    nhType6 = rpc.xpath('.//rt-entry/nh[6]/nh-type')[0].text
    nhIndex6 = rpc.xpath('.//rt-entry/nh[6]/nh-index')[0].text
    
    nhType7 = rpc.xpath('.//rt-entry/nh[7]/nh-type')[0].text
    nhIndex7 = rpc.xpath('.//rt-entry/nh[7]/nh-index')[0].text    
    nhIfl7 = rpc.xpath('.//rt-entry/nh[7]/via')[0].text

    print("Static Route: Kernel View")
    print(f'{"Destination":<10}{"Dest Type":>15}{"NH Type":>15}{"NH Index":>15}{"NH IFL":>15}')   
    print(f'{destIp:<10}{destType:>13}{nhType1:>15}{nhIndex1:>15}') 
    print(f'{nhType2:>25}{nhIndex2:>15}')
    print(f'{nhType3:>25}{nhIndex3:>15}{nhIfl3:>15}')
    print(f'{nhType4:>25}{nhIndex4:>15}')
    print(f'{nhType5:>25}{nhIndex5:>15}{nhIfl5:>15}')
    print(f'{nhType6:>25}{nhIndex6:>15}')
    print(f'{nhType7:>25}{nhIndex7:>15}{nhIfl7:>15}')
    print()
    print()

    # Get the IP route table index from PFE
    rpc=dev.rpc.request_pfe_execute(target='fpc0',command='show route table proto ip', timeout='5')
    for line in str.splitlines(rpc.text):
        if '__flexible_tunnel_profiles__' in line:
            pat = line.strip().split()[1]
            print(f'PFE Route Table Index for Flex Tunnel Profile (DECAP): {pat}')
            print()
        elif 'vpnA' in line:
            tableIndex = line.strip().split()[1]
            print(f'PFE Route Table Index for RI: {tableIndex}')
            print()

    # Collect static route details from PFE
    cmd = 'show route prefix proto ip table-index ' + tableIndex + ' ' + static_route[0] + ' detail'
    rpc=dev.rpc.request_pfe_execute(target='fpc0',command=cmd, timeout='15')

    print("Static route: PFE View")
    print(f'{"Destination":<10}{"NH Type":>15}{"NH Index":>15}{"NH IFL":>15}{"NH IFL Index":>15}')

    for line in str.splitlines(rpc.text):
        if str(static_route) in line:
            dstIp = line.strip().split()[0]
            nhType = line.strip().split()[1]
            nhId = line.strip().split()[2]
            print(f'{destIp:<10}{nhType:>15}{nhId:>15}') 
        elif 'pfe' in line and 'Indirect' in line:
            inhIndex=line.split()[0].split('(')[0]
            inhType=line.split()[0].split('(')[1].split(',')[0]
            inhIflInx=line.split()[2].split(':')[1]
            inhIfl=line.split()[2].split(':')[2].split(',')[0]
            print(f'{inhType:>25}{inhIndex:>15}{inhIfl:>15}{inhIflInx:>15}')
        elif 'pfe' in line and 'Unicast' in line:
            uIndex=line.split()[0].split('(')[0]
            uType=line.split()[0].split('(')[1].split(',')[0]
            uIflInx=line.split()[2].split(':')[1]
            uIfl=line.split()[2].split(':')[2].split(',')[0]
            print(f'{uType:>25}{uIndex:>15}{uIfl:>15}{uIflInx:>15}')

    print()
    print()

    # Collect Flex Route NH details from PFE
    pfe_ucast = {}
    pfe_dict = {}
    for ip in next_hops:

        cmd = 'show route prefix proto ip table-index ' + tableIndex + ' ' + ip + ' detail'
        rpc=dev.rpc.request_pfe_execute(target='fpc0',command=cmd)

        for line in str.splitlines(rpc.text):
            if 'pfe' in line and 'Unicast' in line:
                pfe_ucast[ip] = [line.split()[0].split('(')[1].split(',')[0]]
                pfe_dict[ip] = [line.split()[0].split('(')[0]]
                pfe_ucast[ip].append(line.split()[0].split('(')[0])
                pfe_ucast[ip].append(line.split()[2].split(':')[2].split(',')[0])
                pfe_dict[ip].append(line.split()[2].split(':')[2].split(',')[0])
                pfe_ucast[ip].append(line.split()[2].split(':')[1])
            elif 'Type:' in line:
                pfe_ucast[ip].append(line.split()[1])
                pfe_dict[ip].append(line.split()[1].upper())
            elif 'params' in line:
                pfe_ucast[ip].append(line.split()[1])
            elif 'Destination IP:' in line:
                pfe_ucast[ip].append(line.split()[2])
                #pfe_dict[ip].append(line.split()[2])
            elif 'VNI:' in line:
                pfe_ucast[ip].append(line.split()[1])
                pfe_dict[ip].append(line.split()[1])
            elif 'Dest MAC:' in line:
                pfe_ucast[ip].append(line.split()[2])
                pfe_dict[ip].append(line.split()[2])
            elif 'Source IP:' in line:
                pfe_ucast[ip].append(line.split()[2])
                #pfe_dict[ip].append(line.split()[2])
            elif 'Destination Port:' in line:
                pfe_ucast[ip].append(line.split()[2])
                pfe_dict[ip].append(line.split()[2])
            elif 'Src MAC:' in line:
                pfe_ucast[ip].append(line.split()[2])
                pfe_dict[ip].append(line.split()[2])

    print(f"PFE Data Captured for Comparision: {pfe_dict}")
    df = pd.DataFrame(pfe_ucast, index=['NH Type', 'NH Index', 'IFL', 'IFL Index', 'ENCAP', 'ACTION','Dest IP', 'VNI', 'Dest MAC','Src IP', 'Dst Port','Src MAC'])
    print(f'Data Collected from Flex Route Next-Hops [PFE]:')
    print(df)
    print()

    dev.close()

    # Compare RE and PFE data
    flag = 0
    for key,value in re_dict.items():
        for ret in value:
            if ret in pfe_dict[key]:
                #print('match')
                continue
            else:
                print(f'Difference bw RE and PFE Data: {ret}')
                flag=1
                
    if flag == 0:
        print('Flex Route: RE and PFE are in Sync')
        return True
    else:
        print('Opps!! Flex Route: RE & PFE are out of Sync!')
        return False


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
    '''
    isVm = str(input("Is VM setup creation needed? [Yes/No]: ")) or "No"
 
    if isVm == 'Yes':
        #Run and configure VMM
        retVal = vmm_start_config()
        print(f"Return Vale: {retVal}")
        print(f"Return Vale Type: {type(retVal)}")

        if retVal is False and isinstance(retVal, bool):
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
    else:
        print('VM creation skipped as per User Input')

    router_dict={'r1_re0': '10.49.103.61', 'r2_re0': '10.49.103.42', 'r3_re0': '10.49.103.184', 'r4_re0': '10.49.103.182', 'r5_re0': '10.49.103.150'}

    #Verify Router State and configuration 
    # Router list for D24.11
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

    # Verify Flex Route
    if ecmp_over_flex_route(router_dict['r2_re0']):
        print("R2: RE/Kernel/PFE: Flex Route Verification Successful!!")
    else:
        print("Oops!!R2: Flex Route verification failed!..")

if __name__ == "__main__":
    main()    

