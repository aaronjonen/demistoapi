from __future__ import unicode_literals
from __future__ import print_function
import json
class Label(dict):
    def __init__(self,type,value):
        super(Label,self).__init__()
        self["type"]=type
        self["value"]=value

class Resource(object):
    GET="GET"
    POST="POST"
    SEVERITY={"LOW":0,"MEDIUM":1,"HIGH":2}
    def __init__(self,client):
        self.client = client
        self.method = Resource.GET
        self.status_codes={}
        self.data={}
        self.url=self.client.server+"{0}"
        self.method=Resource.GET
        self.status_codes={}


    def __iter__(self):
        return self

    def __next__(self):
        return self.request()

    def request(self):
        #todo(aj) add debugging
        response = self.client.req(self.method,self.url,self.data,self.status_codes[self.method])
        status = response.status_code
        data = json.loads(response.content)
        if response.status_code in self.status_codes[self.method]:
            status='Success'
        return {
            'data': data,
            'response': response,
            'status': status
        }


class Incident(Resource):

    def __init__(self,client):
        super(Incident,self).__init__(client)
        self.url=self.url.format("incident")
        self.status_codes = {
            'DELETE': [200],
            'GET': [200],
            'POST': [200, 201],
            'PUT': [200]
        }

    def create(self, name , type, severity,create_investigation=False, **kwargs):
        """
        POST http://server/incident
         name: str,
         type: str,
         severity: str,
         labels:list of Label,

        :param kwargs:
         owner: str,
         details,
         custom_fields, ** kwargs
        """
        self.method=Resource.POST

        self.data = {"type": type,
                        "name": name,
                        "severity": severity,
                        "createInvestigation":True if create_investigation else False
                        }

        for e in kwargs:
            if e not in self.data:
                self.data[e] = kwargs[e]


class SearchIncident(Resource):
    def __init__(self,client):
        super(SearchIncident,self).__init__(client)
        self.url=self.url.format("incidents/search")

    def SearchIncidents(self, page, size, query):
        """
        POST http://server/incidents/search

        :param page:
        :param size:
        :param query:
        :return:
        """
        self.data = {'filter': {'page': page, 'size': size, 'query': query, 'sort': [{'field':'id', 'asc': False}]}}

