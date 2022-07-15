import gspread
from constant import creds


def getInput(sheet_name, tab_name):
    client = gspread.authorize(creds)
    masterSheet = client.open(sheet_name).worksheet(tab_name)
    return masterSheet.get_all_records(), masterSheet


def updateStatus(linkedin_url, sheet, col_count, msg):
    cell = sheet.find(linkedin_url)
    try:
        sheet.update_cell(cell.row, cell.col + col_count, msg)
        # sheet.update_cell(cell.row, cell.col + 3, str(datetime.now()))
    except:
        pass


def processData(data):
    li = []
    for each in data:
        if each['Request Sent To POC 1'] == '':
            li.append({'name': each['POC1'], 'linkedin': each['POC 1 LinkedIn Profile']})
        if each['Request Sent To POC 2'] == '':
            li.append({'name': each['POC2'], 'linkedin': each['POC 2 LinkedIn Profile']})
    return li
