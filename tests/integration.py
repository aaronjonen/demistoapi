import unittest
import argparse
import demistoapi.client as cli
import demistoapi.resource as resources

import os


class RequestError(Exception):
    def __init__(self,msg):
        super(RequestError,self)

API_KEY = os.environ["API_DEMISTO"]
SERVER = os.environ["SERVER"]

class IncidentCreate(unittest.TestCase):
    def test_incident(self):
        client = cli.DemistoClient(API_KEY,SERVER)
        incident_resource = resources.Incident(client)
        label = resources.Label("md5_hashes","00f538c3d410822e241486ca061a57ee,")
        incident_resource.create(name="Test integration",
                                          type="TC Intel Historical",
                                          severity=resources.Resource.SEVERITY["LOW"],
                                 labels=[label])
        result = incident_resource.request()
        if result["status"]!="Success":
            raise RuntimeError("Connection Failed")


if __name__ == "__main__":
    unittest.main()



