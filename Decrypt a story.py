#### Edx exercise ####

### Problem set 5 ###

## Problem 4 - Decrypt a story ##

def decrypt_story():
    joke_code = CiphertextMessage(get_story_string())
    return joke_code.decrypt_message()
