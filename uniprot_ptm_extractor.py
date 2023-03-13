from bioservices import UniProt
import pprint
import csv

###################

# Prints all the results from the UniProt search
def print_detailed_results(res):

    for key in res:
        print('\n')
        print('//////////////')
        print(key)
        print(type(res[key]))
        print('//////////////')
        print('\n')
        pprint.pprint(res[key])

# res is a dictionary of results from the UniProt page. One of the keys is 'comments'. 
# 'comments' is a list of dictionaries. One of these keys is 'commentType', which can have
# the value 'PTM.'  
def get_ptms(res):

    l = list()
    for dict_item in (res['comments']):
        if dict_item.get('commentType') == 'PTM':
            info, evidence = get_info_and_evidence(dict_item.get('texts'))
            primary_accession = res['primaryAccession']
            uniprot_id = res['uniProtkbId']
            row = (primary_accession, uniprot_id, info, evidence)
            l.append(row)
    return l

# 'ptm_details' is a list of dicts. It always contains 'value' which describes the PTM.
# It can also have 'evidences' which cites relevant literature. Returns information and
# related evidence as a tuple.
def get_info_and_evidence(ptm_details):

    for dict_item in ptm_details:
        info = dict_item.get('value')
        if dict_item.get('evidences'):
            ev = get_evidence(dict_item.get('evidences'))
            #print(ev)
        else: 
            ev = 'NONE'
    return(info, ev)

def get_evidence(input):

    #print('\n')
    evidence = list()

    for dict_item in input:
        pprint.pprint(dict_item)
        if dict_item.get('id') and dict_item.get('source'): 
            evidence.append(dict_item.get('source') + ' ' + dict_item.get('id'))
        elif dict_item.get('id') and not dict_item.get('source'):
            evidence.append(dict_item.get('id'))
        elif not dict_item.get('id') and dict_item.get('source'): 
            evidence.append(dict_item.get('source'))
        else:
            evidence.append('no source no id')
    return evidence

###################

# Read protein list from proteins.txt
with open('proteins.txt', 'r') as file:
    protein_list = file.readlines()
    # Strip any whitespace characters (including newline characters) from each line
    protein_list = [line.strip() for line in protein_list]
file.close

# Headers for tsv file
data = [('Accession Number', 'Primary ID', 'PTM Info', 'Evidence')]

# Search for each protein on Uniprot. Expand data for each PTM found
u = UniProt()
for protein in protein_list:
    res = u.retrieve(protein, database='uniprot') # Database search
    ptm_info = get_ptms(res) # Getting relevant PTM info for each search
    data.extend(ptm_info) # Add PTM info to data

# Output data in psm_output.tsv
# Open a file for writing with 'w' mode and newline='' to avoid line ending issues
with open('psm_output.tsv', 'w', newline='') as f:
    # Create a CSV writer object with tab as delimiter
    writer = csv.writer(f, delimiter='\t')
    for row in data:
        writer.writerow(row)
f.close()

#print_detailed_results(res)