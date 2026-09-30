def likes(names):
    
    display_text = ""
    
    if not names:
        
        display_text = "no one likes this"
    
    elif len(names) == 1:
        display_text = names[0] + " likes this"
        
    elif len(names) < 4:
        for i in range(len(names)):
            if i == len(names) - 1:
                display_text = display_text + " and "
            elif i > 0:
                display_text = display_text + ", "
            display_text = display_text + names[i]
        display_text = display_text + " like this"
    
    else:
        display_text = names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"

    return display_text