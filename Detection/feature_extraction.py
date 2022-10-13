import os
import subprocess

import scapy.all
from typing import List
#import cicflowmeter.utils
import myutil

def change_client_port_with_DNS_ID():
    # pcap名称
    old_pcap_file_path: str = './2018.pcap'
    packet_list: List = scapy.all.rdpcap(old_pcap_file_path)
    server_ip: str = ''
    client_ip: str = ''

    # 判断哪个ip为客户端，则另一个为服务端
    if packet_list[0]['UDP'].sport == 53:
        server_ip = packet_list[0]['IP'].src
        client_ip = packet_list[0]['IP'].dst
    else:
        client_ip = packet_list[0]['IP'].src
        server_ip = packet_list[0]['IP'].dst

    for each_packet in packet_list:
        if each_packet['IP'].src == client_ip:
            each_packet['UDP'].sport = each_packet['DNS'].id
        elif each_packet['IP'].src == server_ip:
            each_packet['UDP'].dport = each_packet['DNS'].id
    # 保存为新的pcap
    scapy.all.wrpcap('20181.pcap', packet_list)


def feature_extraction(pcap_file_path, exp_type='statistical'):
    temp_feature_csv_folder_path: str = 'Feature/temp'
    temp_feature_csv_file_name: str = 'temp.csv'
    temp_feature_csv_file_path: str = os.path.join(temp_feature_csv_folder_path, temp_feature_csv_file_name)

    # statistical 2
    if exp_type == 'statistical':
        commond = 'cicflowmeter -f {} -c {}'.format(pcap_file_path, temp_feature_csv_file_path)
        # print(commond)
        p = subprocess.call(commond, shell=True)
        csv_data = myutil.read_with_pandas(temp_feature_csv_file_path)
        return csv_data

    # payload_1
    if exp_type == 'payload':
        pass
        # commond = 'python /home/119project/DNS_Evade/Feature/payload_parse.py ' + \
        #     pcap + ' '+feature_path+feature_name

    # packet_3
    if exp_type == 'packet':
        pass