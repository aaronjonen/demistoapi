from __future__ import unicode_literals
from __future__ import print_function
# DemistoClient
# Python client that shows how to invoke API calls on the Demisto server.
# To use the client, you should generate an API key under Settings->Integrations->API Keys
#
# Author:       Lior
# Version:      1.1
#
import json
from requests import Session
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)


class DemistoClient:
    XSRF_TOKEN_KEY = "X-XSRF-TOKEN"
    XSRF_COOKIE_KEY = "XSRF-TOKEN"
    AUTHORIZATION = "Authorization"

    # New client that does not do anything yet
    def __init__(self, apiKey, server, username=None, password=None):
        if not ((apiKey or (username and password)) and server):
            raise ValueError("You must provide server argument and key or user & password")
        if not server.find('https://') == 0 and not server.find('http://') == 0:
            raise ValueError("Server must be a url (e.g. 'https://<server>' or 'http://<server>')")
        if not server[-1] == '/':
            server += '/'

        self.server = server
        self.session = Session()
        if not apiKey:
            self.xsrf = True
            try:
                r = self.session.get(server, verify=False)
            except InsecureRequestWarning:
                pass
            self.token = r.cookies[DemistoClient.XSRF_COOKIE_KEY]
            self.username = username
            self.password = password
        else:
            self.xsrf = False
            self.apiKey = apiKey

    def req(self,method,url,data,ok_codes):
        h = {"Accept": "application/json",
             "Content-type": "application/json"}

        if self.xsrf:
            h[DemistoClient.XSRF_TOKEN_KEY] = self.token
        else:
            h[DemistoClient.AUTHORIZATION] = self.apiKey
        r=None
        try:
            if self.session:
                r = self.session.request(method, url, headers=h, verify=False, json=data)
                if r.status_code not in ok_codes:
                    raise RuntimeError('Error searching incidents - %d (%s)' % (r.status_code, r.reason))

            else:
                raise RuntimeError("Session not initialized!")
        except InsecureRequestWarning:
            pass
        return r

