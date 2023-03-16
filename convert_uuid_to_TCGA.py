# Developer: Apiwat Sangphukieo , email: sangphukieo@gmail.com
import os,sys
import pandas as pd
import requests
import json

path=sys.argv[1]
fields = ["disease_type"]
params = {"fields": fields}
print('file_id', 'case_id','case_submitter_id','access','primary_site','disease_type','file_name','submitter_id', 'md5sum','experimental_strategy', sep ='\t')
for fileID in open(path):
    fileID = fileID.rstrip()
    if "id\tfilename" not in fileID:
        col = fileID.split()
        #fileID="fe341468-3b2e-48d6-b90a-a66da6a84083"
        response = requests.get(('https://api.gdc.cancer.gov/files/' + col[0] + '?expand=cases'), params = params)
        json_data = json.loads(response.text)
        tempdtype = json_data['data']
        casedatalist = tempdtype['cases']
        casedata = casedatalist[0]  

        print(col[0], casedata['case_id'],casedata['submitter_id'],tempdtype['access'],casedata['primary_site'],casedata['disease_type'],tempdtype['file_name'],tempdtype['submitter_id'], tempdtype['md5sum'],tempdtype['experimental_strategy'], sep ='\t')
