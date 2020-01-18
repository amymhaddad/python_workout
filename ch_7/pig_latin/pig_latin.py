

words = "air python"

new_words = ''
for word in words.split(" "):
    if word.startswith(("a", "e", "i", "o", "u")):
        
        new_words += word +"way " 
    else:
        new_words += word[1:] + word[0] + "ay" + " "


