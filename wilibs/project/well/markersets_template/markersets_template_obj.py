from ....api_url import ROOT_API
from ....api_url import EXPORT_PATH
import os as os
from ....common import *
import requests

class MarkerSetTemplate:
    def __init__(self, token, MarkerSetTempateInfo):
        self.token = token
        self.MarkerSetTempateInfo = {
            'idProject' : MarkerSetTempateInfo['idProject'],
            'idMarkerTemplate' : MarkerSetTempateInfo['idMarkerTemplate'],
            'name' : MarkerSetTempateInfo["name"]
        }
        self.markerSetTemplateId = MarkerSetTempateInfo['idMarkerTemplate']
        self.projectId = MarkerSetTempateInfo['idProject']
        self.markerSetTemplateName = MarkerSetTempateInfo['name']
   
    def __repr__(self):
        obj = dict(self.MarkerSetTempateInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()  

    def deleteMarkerSet(self):
        check, content = deleteMarkerSet(self.token, self.markerSetTemplateId)
        if check:
            return None
        return content