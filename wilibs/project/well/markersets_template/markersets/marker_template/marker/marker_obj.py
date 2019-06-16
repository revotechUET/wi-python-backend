from  .marker_api import *

class Marker:
    def __init__(self, token, markerInfo):
        self.token = token
        self.markerInfo = {
            'idMarker' : markerInfo['idMarker']
            'idMarkerTemplate': markerInfo['idMarkerTemplate'],
        }
        self.markerId =  markerInfo['idMarker']
        

    def __repr__(self):
        obj = dict(self.imagesetInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()
    
    def deleteMarker(self):
        check, content = deleteMarker(self.token, self.markerId)
        if check:
            return True
        else:
            print(content)
        return False
    