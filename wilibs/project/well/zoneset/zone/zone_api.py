from wilibs.api_url import ROOT_API
import os as os
from wilibs.common import *
from wilibs.common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def createZone(token, payload):
    r = createZone_RAW(token, payload)
    return verifyAndReturn(r)


def deleteZone(token, ZoneId):
    r = deleteZone_RAW(token, ZoneId)
    return verifyAndReturn(r)


def editZoneTemplate(token, payload):
    r = editZone_RAW(token, payload)
    return verifyAndReturn(r)


def getListZone(token, ZoneSetId):
    r = getListZone_RAW(token, ZoneSetId)
    return verifyAndReturn(r)


def getZoneInfo(token, ZoneId):
    r = getZoneInfo_RAW(token, ZoneId)
    return verifyAndReturn(r)


# RAW
def createZone_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/well/zone-set/zone/new', payload, token)
    r = requests.post(url, json={payload}, headers=tokenHeader(token), verify=False)
    return r.json()


def deleteZone_RAW(token, ZoneId):
    url = genUrlWithWiId(ROOT_API + '/project/well/zone-set/zone/delete', {'idZone': ZoneId}, token)
    r = requests.delete(url, json={'idZone': ZoneId}, headers=tokenHeader(token), verify=False)
    return r.json()


def editZone_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/well/zone-set/zone/edit', {'idZone': payload}, token)
    r = requests.delete(url, json={'idZone': payload}, headers=tokenHeader(token), verify=False)
    return r.json()


def getListZone_RAW(token, ZoneSetId):
    url = genUrlWithWiId(ROOT_API + '/project/well/zone-set/zone/list', {'idZoneSet': ZoneSetId}, token)
    r = requests.post(url, json={'idZoneSet': ZoneSetId}, headers=tokenHeader(token), verify=False)
    return r.json()


def getZoneInfo_RAW(token, ZoneId):
    url = genUrlWithWiId(ROOT_API + '/project/well/zone-set/zone/info', {'idZone': ZoneId}, token)
    r = requests.post(url, json={'idZone': ZoneId}, headers=tokenHeader(token), verify=False)
    return r.json()
