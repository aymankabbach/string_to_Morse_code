latin_alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
,"1","2","3","4","5","6","7","8","9","0","&","é","è",'"',"'","(","-","_","ç","à","@","=","+",";",",","?"
,"!",":","."]
Morse_code=["·− ","−··· ","−·−· ","−·· ","·","··−·","−−·","····","··","·−−−","−·−","·−··","−−","−·","−−−","·−−· "
,"−−·−","·−· ","···","−","··−","···−","·−−","−··−","−·−−","−−·· ","·−−−−","··−−− ","···−−","····−","·····"
,"−····"," −−···","−−−··","−−−−·","−−−−−","·−···","··−··","·−··−","·−··−·","·−−−−·","−·−−·−","−····−"
,"··−−·−"," −·−··","·−−·−","·−−·−·","−···−","·−·−·","−·−·−·","−−··−−","··−−··","−·−·−−","−−−···","·−·−·−"] 
def read_the_text_from_the_user():
    user_input=input("enter a text\n")
    return user_input.lower()
def convert_input_To_List(user_word):
    letters_list=[]
    for letter in user_word:
        letters_list.append(letter)
    return letters_list
def coding_The_text(letters_list):
    global latin_alphabet
    coded_list=[]
    for letter in letters_list:
        if letter in latin_alphabet:
            coded_list.append(Morse_code[latin_alphabet.index(letter)])
        else:
            coded_list.append(letter)
    return coded_list
def convert_the_list_to_a_text(coded_list):
    converted_text=""
    for letter in coded_list:
        if letter in Morse_code:
            converted_text+=letter+" "
        else:
            converted_text+=letter
    return converted_text
def print_the_text():
    user_word=read_the_text_from_the_user()
    letters_list=convert_input_To_List(user_word)
    coded_list=coding_The_text(letters_list)
    converted_text=convert_the_list_to_a_text(coded_list)
    print(converted_text)
print_the_text()