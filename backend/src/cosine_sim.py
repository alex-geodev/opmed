# Program to measure the similarity between  
# two sentences using cosine similarity. 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

# X = input("Enter first string: ").lower() 
# Y = input("Enter second string: ").lower() 
X ="I love horror movies"
Y ="Lights out is a horror movie"

# Line 3: Pxt by precedence
# A: Urgent
# B: Urgent Surgical
# C: Priority
# D: Routine

# Line 4: Special Equipment
# A: None
# B: Hoist
# C: Extraction Equipment
# D: Ventilator

# Line 5: PXT by Type 
# L + #: litter
# A + #: ambulatory

# Line 7: Method of Marking 
# A: Panels
# B: Pyrotechnic Signal
# C: Smoke Signal
# D: None
# E: Other


status = ['urgent','urgent surgical', 'priority','routine','convenience']
spec_eqt = ['']
mobility = ['litter','ambulatory']
nationality = ['us military','us civilian', 'non us military','non us civilian','enemy prisoner of war']
test_str = 'urgent'
test_list_token = []
for word in status: 
    token_word = word_tokenize(word)
    test_list_token.append(token_word)

# tokenization 
test_str_token = word_tokenize(test_str)  
# test_list = word_tokenize(Y) 
  
# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[];l2 =[] 
  
# remove stop words from the string 
test_str_set = {w for w in test_str_token if not w in sw}  
set_list = []
for test_word in test_list_token:    
    Y_set = {w for w in test_word if not w in sw} 
    set_list.append(Y_set)
  
# form a set containing keywords of both strings  
for test_set in set_list: 
    l1 =[];l2 =[] 
    rvector = test_str_set.union(test_set)  
    for w in rvector: 
        if w in test_str_set: l1.append(1) # create a vector 
        else: l1.append(0) 
        if w in test_set: l2.append(1) 
        else: l2.append(0) 
    c = 0
      
    # cosine formula  
    for i in range(len(rvector)): 
            c+= l1[i]*l2[i] 
    cosine = c / float((sum(l1)*sum(l2))**0.5) 
    
    print(f"Similarity of {test_set} and {test_str_set}: ", cosine) 
    