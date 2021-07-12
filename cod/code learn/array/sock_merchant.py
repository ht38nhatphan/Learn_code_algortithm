MORSE_CODE_DICT = { 'a':'.-', 'b':'-...', 
                    'c':'-.-.', 'd':'-..', 'e':'.', 
                    'f':'..-.', 'g':'--.', 'h':'....', 
                    'i':'..', 'j':'.---', 'k':'-.-', 
                    'l':'.-..', 'm':'--', 'n':'-.', 
                    'o':'---', 'p':'.--.', 'q':'--.-', 
                    'r':'.-.', 's':'...', 't':'-', 
                    'u':'..-', 'v':'...-', 'w':'.--', 
                    'x':'-..-', 'y':'-.--', 'z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----'} 
def decodeMorseCode(message):
    message += ' '
    decipher = '' 
    citext = '' 
    for letter in message:
        if(letter in '/'):
           decipher+=" "
           continue
        if (letter != ' '): 
            i = 0
            citext += letter 
        else: 
            i += 1
            if i == 2 : 
                decipher += ' '
            else: 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 
    return decipher 



a=".... . .-.. .-.. --- /"
print(decodeMorseCode(a))