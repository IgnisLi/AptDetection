import unittest

import feature_extraction
pcappath = "APT\\8202_tbd_ 6D2C12085F0018DAEB9C1A53E53FD4D1.pcap"
syspath = "C:\\QiLi\\Cyberattack\\"
class TestFeatureExtraction(unittest.TestCase):

    def test_cicflowmeter_feature_extraction(self):
        result = feature_extraction.feature_extraction(syspath+pcappath)#)
        print(result)
