import mgrs 
import re
from app.crud.lookup_tables.fields import fields, line_numbers, digits, phonetic_alphabet
import backend.src.nineline_entry as nineline_entry

class nineLineHelper():

    def __init__(self, id:str, filepath:str, transcription:str):

        self.id = id
        self.filepath = filepath
        self.transcription = transcription
        self.generate_dict(transcription)
        self.process_nine_line(self.nineLineInit)

    def generate_dict(self):
        nine_line_dict = {}

        #find line one start
        line_one_start = re.search('line one',self.transcription)
        line_one_start = line_one_start.start()
        
        #loop through each line of nine line and extract corresponding text
        idx=1
        for line in self.transcription[line_one_start:].split('line'):
            if line:
                nine_line_dict[line_numbers[idx]] = ' '.join(line.split()[1:])
                idx+=1

        self.nineLineInit = nine_line_dict

    def check_for_phonetic(word:str)->str:
        match = [item for item in phonetic_alphabet if item == word]
        return match[0][0] if match else ''

    def check_for_number(word:str)->str:
        match = [item for item in list(digits.keys()) if item == word]
        return  str(digits[match[0]]) if match else ''

    def get_field(letter:str,field_name:str)->str:
        match = [v for k,v in fields.get(field_name).items() if k == letter]
        return match[0] if match else 'None'
    
    def mgrs_to_lat_long(mgrs_grid):

        m = mgrs.MGRS()
        d = m.toLatLon(mgrs_grid)

        return d
    
    def process_nine_line(self):

        formatted_nine_liner = {'id': self.id,
                                'filepath':self.filepath,
                                'audio_transcription':self.transcription}
        
        for k,v in self.nineLineInit.items():
            output=''
            
            #get fields with associated values and process
            if k in ['patient_precedence','mobility','nationality']:
                for idx,word in enumerate(v.split()):
                    result = self.check_for_phonetic(word)
                    if result:
                        field = self.get_field(result,k)
                        try:
                            quantity = self.check_for_number(v.split()[idx-1])
                        except:
                            quantity = self.check_for_number(v.split()[idx+1])
                        formatted_nine_liner[field] = quantity
            
            #remaining fields have no quantity associations
            else:
                for idx,word in enumerate(v.split()):
                    result = self.check_for_phonetic(word)
                    if result:
                        output+=result
                    else:
                        output+=self.check_for_number(word)
                if k == 'location':
                    lat,lon = self.mgrs_to_lat_long(output)
                    formatted_nine_liner[k] = {'mgrs':output,'lat':lat,'lon':lon}
                elif k in ['equipment','site_security','pickup_mark']:
                    field = self.get_field(result,k)
                    formatted_nine_liner[k]=field
                else:
                    formatted_nine_liner[k]=output
        
        self.nineLineProcessed = formatted_nine_liner


def send_to_db(nineline:dict):
    id_ = nineline.get('id')
    audio_transcription = nineline.get('audio_transcription')
    audio_file = nineline.get('audio_path')
    mgrs = nineline.get('location')['mgrs']
    lat =  nineline.get('location')['lat']
    lon = nineline.get('location')['lon']
    frequency = nineline.get('freq')
    urgent = nineline.get('urgent')
    urgent_surgical = nineline.get('urgent surgical')
    priority= nineline.get('priority')
    routine = nineline.get('routine')
    convenience = nineline.get('convenience')
    litter = nineline.get('litter')
    ambulatory = nineline.get('ambulatory')
    us_military = nineline.get('us military')
    us_civilian = nineline.get('us civilian')
    non_us_military = nineline.get('non us military')
    non_us_civilian = nineline.get('non us civilian')
    enemy_prisoner_of_war = nineline.get('enemy prisoner of war')
    equipment = nineline.get('equipment')
    site_security = nineline.get('site_security')
    pickup_mark = nineline.get('pickup_mark')
    cbrn = nineline.get('cbrn')

    nineline_entry.insert(id_,audio_transcription,audio_file,mgrs,lat,lon,frequency,
                          urgent,urgent_surgical,priority,routine,convenience,litter,
                          ambulatory, us_military, us_civilian, non_us_military,
                          non_us_civilian, enemy_prisoner_of_war,equipment,site_security,pickup_mark,cbrn)