from preloaded import MORSE_CODE

def decode_morse(morse_code):    
    message = ""
    morse_code_words = morse_code.strip().split("   ")
    for i, w in enumerate(morse_code_words):
        morse_code_letters = w.split(" ")
        for l in morse_code_letters:
            message += MORSE_CODE[l]
        if i != len(morse_code_words) - 1:
            message += " "
        
    return message