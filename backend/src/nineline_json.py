import json


with open('./lookup_tables/phonetic.json') as f:
    phonetic_dict = json.load(f)

with open('../data/nine_line_test.json') as f:
    nine_line_outpout = json.load(f)



def text_to_alpha(text_str: str)->str:
    pass


