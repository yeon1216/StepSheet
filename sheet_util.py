import gspread
from oauth2client.service_account import ServiceAccountCredentials

ALL_MEMBER_SHEET = '전체인원'
RANGE = 'A2:F'
KEY = '1RaeBPtK6bWFeDC6Ngz5GMrswvIuSQK-XKIgs1u6YiOE'
SCOPE = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]
JSON_FILE_NAME = 'res/platinum-chain-377308-8a26cc2d906e.json'

def getSheet(sheet_name):
    doc = getDoc()
    return doc.worksheet(sheet_name)

def getCred():
    return ServiceAccountCredentials.from_json_keyfile_name(JSON_FILE_NAME, SCOPE)

def getGC():
    return gspread.authorize(getCred())


def getDoc():
    gc = gspread.authorize(getCred())
    return gc.open_by_key(KEY)

def addSheet(sheet_name, rows, cols):
    doc = getDoc()
    doc.add_worksheet(title=sheet_name, rows=rows, cols=cols)