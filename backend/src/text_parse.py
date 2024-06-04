
def parse_str(audio_string):
    nine_line_dict = {}
    audio_string = audio_string.lower()
    audio_string = audio_string.replace(",", "")
    audio_string = audio_string.replace(":", '')
    receiver = audio_string[:audio_string.find(" ")] 
    caller = audio_string[audio_string.find("this is")+8:audio_string.find("over")-2]
    nine_line_str = audio_string[audio_string.find("nine line as follows"):]
    nine_line_list = nine_line_str.split("break ")
    # print(nine_line_list)
    nine_line_dict = {
        "caller"  : caller,
        "receiver": receiver,
        "one"     : nine_line_list[1].replace("one ", "").replace("line ", "").replace("1", ''),
        "two"     : nine_line_list[2].replace("two ", "").replace("line ", "").replace("2", ''),
        "three"   : nine_line_list[3].replace("three ", "").replace("line ", "").replace("3", ''),
        "four"    : nine_line_list[4].replace("four ", "").replace("line ", "").replace("4", ''),
        "five"    : nine_line_list[5].replace("five ", "").replace("line ", "").replace("5", ''),
        "six"     : nine_line_list[6].replace("six ", "").replace("line ", "").replace("6", ''),
        "seven"   : nine_line_list[7].replace("seven ", "").replace("line ", "").replace("7", ''),
        "eight"   : nine_line_list[8].replace("eight ", "").replace("line ", "").replace("8", ''),
        "nine"    : nine_line_list[9].replace("nine ", "").replace("line ", "").replace("9", ''),
        }
 
    return nine_line_dict

test_case1 = "CharlieMed, this is Echo-2-Niner, over Echo-2-Niner, this is Charlie-Med, send over This is Echo-2-Niner, request medevac, over Echo-2-Niner this is Charlie-Med, authenticate Yankee, over Charlie-Med, this is Echo-2-Niner, I authenticate Champion, over Roger Echo-2-Niner, send request over Roger, nine line as follows, break ONE, Tango-alpha 6577, break TWO, 39.39,E-7-Romeo, break THREE, 1-Charlie, 2-Delta, break FOUR, Alpha, break FIVE, Lima-1, Alpha-2, break SIX, November, break SEVEN, Green smoke, break EIGHT, US military, break NINE, Large raising hills to the north, and south with wires to the north running east to west, over."
test_case2 = 'BravoMed, this is mike-4-foxtrot, over mike-7-foxtrot, this is BravoMed, standing by, this is mike-4-foxtrot, requesting medevac, nine line as follows break, Line one: We gave coordinates in Upper Kandahar where the extraction was needed. break Line two: We changed comms three times and ended up doing our route call to CDC at Bastion because it was closest to us. We comm-checked the frequency and continued our 9 line. break Line three : 2 urgent and 1 was deceased. break Line four We needed two IV suspensions. I needed a body splint for the 1 marine because he had multiple breaks in his upper and lower extremities and his bones were pretty much mush. I had already put 1 King in and bagging him. I needed a special ventilator. break Line five: 2 non-ambulatory (litters needed) and 1 body bag. break Line six : E – Hostiles in the area. We had not yet secured the single sniper we were receiving fire from, and we were requesting definite escort. break Line seven: Green smoke can. We requested immediate River City status. break Line eight: A – All three patients were U.S. Marines. break Line nine: No detected NBC at this time.'
test_case3 = 'MedCIP, this is unit 805, over, unit 805, this is MedCIP standing by, MedCIP this is unit 805 requesting medevac support, nine line as follows break, We called in an aerial lift for Afghan National Police that rolled their MRAP, severely injuring three and killing the driver. The mechanism of destruction was unknown at that time. Line 1: Coordinates were given outside Camp Jackson on a push. break Line 2: Comms for the day were separate. We used both to call in for the Afghan Nationals and the CDC was being run by the Geneva Forces—part of our joint alliance out of Camp Dwyer. break Line 3: 3 urgent and 1 was left at site for National pick-up (deceased). break Line 4: None was requested. All supplies were already on hand because we had a well-stocked medical MRAP at the scene. break Line 5: 2 non-ambulatory, 1 ambulatory for pick-up extraction. break Line 6: No escort requested at this time. break Line 7: Urgent evacuation site Afghanistan coordinates and national flag. break Line 8: C – local national militia. break Line 9: No NBC detected at this time. Stand by for possible deviation.'

test1 = parse_str(test_case1)
test2 = parse_str(test_case2)
test3 = parse_str(test_case3)














