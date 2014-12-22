# -*- coding: utf-8 -*-
import sys
import requests
import easygui



def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


Mode = enum('PREVIEW', 'EDIT', 'REFRESH')
mode = 0
size = 0
params = ''
key = ''
i = 0


for i in range(len(sys.argv)):
    if str(sys.argv[i]).lower() == "-mode" and (i + 1) < len(sys.argv):
        if str(sys.argv[i + 1]).lower() == "preview":
            mode = Mode.PREVIEW
        elif str(sys.argv[i + 1]).lower() == "edit":
            mode = Mode.EDIT
        elif str(sys.argv[i + 1]).lower() == "refresh":
            mode = Mode.REFRESH
    elif str(sys.argv[i]).lower() == "-size":
        size = int(sys.argv[i + 1])
    elif str(sys.argv[i]).lower() == "-params":
        params = str(sys.argv[i + 1])
        paramslist = params.split(';')
        for i in range(len(paramslist)):
            if paramslist[i].split('=')[0].lower() == 'key':
                key = paramslist[i].split('=')[1]
            i += 1
    i += 1


def printData(key):
    if not key == '':
        proxies = []
        url = ''.join(['https://docs.google.com/spreadsheet/ccc?key=', key, '&output=csv'])
        csv = requests.get(url, proxies=proxies, verify=False)

        if csv.headers['Content-Type'] == 'text/csv':
            data = csv.content
        else:
            data = """Error
Error In Header"""

    else:
        data = """Error
Error In Key"""
    print "beginDSInfo"
    print """fileName;#;true
csv_first_row_has_column_names;true;true;
csv_separator;,;true
csv_number_grouping;,;true
csv_number_decimal;.;true
csv_date_format;d.M.yyyy;true"""
    print ''.join(['key;', key, ';true'])
    print "endDSInfo"

    print "beginData"
    print data
    print "endData"


if mode == Mode.PREVIEW:
    default = ''
    key = easygui.enterbox(msg="Enter GDocs Key", title="Google Docs Key", default=default)
    key = key or default
    printData(key=key)
elif mode == Mode.EDIT:
    default = key
    key = easygui.enterbox(msg="Edit GDocs Key", title="Google Docs Key", default=default)
    key = key or default
    printData(key)
elif mode == Mode.REFRESH:
    printData(key)
















