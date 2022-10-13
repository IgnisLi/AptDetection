from scapy.all import *
from pcap_splitter.splitter import PcapSplitter

def analyzePcap(filepath):
    # s1 = PcapReader(filepath)

    # data = s1.read_packet()

    # ip_packet = data.payload
    # icmp_packet = ip_packet.payload
    # payload = icmp_packet
    pkt = rdpcap(filepath)
    return pkt


pcappath = "APT\\8202_tbd_ 6D2C12085F0018DAEB9C1A53E53FD4D1.pcap"
syspath = "C:\\QiLi\\Cyberattack\\"
folder_path = "dest_pcaps_folder"
ps = PcapSplitter(pcappath)
print(ps.split_by_session("dest_pcaps_folder"))

pkt = analyzePcap(syspath+pcappath)
number_packets = len(pkt.res)
for i in range(0,number_packets):
    pkt=pkt[i]
    IP = pkt['IP']
pkt[0].show()
#a = 1