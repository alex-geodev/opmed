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

line_numbers = {1:'location', 2:'freq', 3:'patient_precedence', 4:'equipment',
             5:'mobility', 6:'site_security', 7:'pickup_mark', 8:'nationality',
             9:'cbrn'}

digits = {
    "one":1,"won":1,
    "two":2,"too":2,"to":2,
    "three":3,
    "four":4,"for":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8, "ate":8,
    "nine":9, "niner":9
    }

phonetic_alphabet = ["alpha", "bravo", "charlie","charley","delta", "echo", "foxtrot", "golf", 
"hotel","india", "juliet","kilo" ,"lima", "mike", "november", "oscar", 
"papa", "quebec", "ray","romeo" ,"sierra", "tango", "uniform", "victor", "whiskey", 
"x-ray","xray","yankee", "zulu"]