import mgrs 
import json
import re

def mgrs_to_lat_long(mgrs_grid):

    m = mgrs.MGRS()
    d = m.toLatLon(mgrs_grid)

    return d

fields = {'patient_precedence': {'a':'urgent','b':'urgent surgical', 'c':'priority','d':'routine','e':'convenience'},
          'equipment':{'a':'None','b':'hoist','c':'extraction equipment','d':'ventilator'},
          'mobility' : {'l':'litter','a':'ambulatory'},
          'site_security' : {'n':'No enemy troops in area', 'p':'Possible enemy troops in area', 'e':'Enemy troops in area - no escort',
                        'x':'Enemy troops in area - escort'},
          'pickup_mark':{'a':'Panels','b':'Pyrotechnic Signal','c': 'Smoke Signal','d':'None','e':'Other'},            
          'nationality' : {'a':'us military','b':'us civilian', 'c':'non us military',
                           'd':'non us civilian','e':'enemy prisoner of war'},
           'cbrn':{'c':'chemical','b':'biological','r':'radioactive','n':'nuclear'}
            }

line_num = {1:'location', 2:'freq', 3:'patient_precedence', 4:'equipment',
             5:'mobility', 6:'site_security', 7:'pickup_mark', 8:'nationality',
             9:'cbrn'}


with open('../data/lookup_tables/numbers.json') as f:
    number_dict = json.load(f)

with open('../data/lookup_tables/phonetic.json') as f:
    phonetic = json.load(f)   


def generate_dict(nine_line_output: dict):
    nine_line_dict = {}

    i=1


    #find line one start
    line_one_start = re.search('line one',nine_line_output.get('audio_translation'))
    line_one_start = line_one_start.start()

    for line in nine_line_output.get('audio_translation')[line_one_start:].split('line'):
        if line:
            nine_line_dict[line_num[i]] = ' '.join(line.split()[1:])
            i+=1
    return nine_line_dict