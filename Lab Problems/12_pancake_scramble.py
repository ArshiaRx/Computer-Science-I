#12 - Try a spatula
def pancake_scramble(text):
    
    #loop through every element from 2 to the range of (lenght of text+1)
    for i in range(2, len(text)+1):
        
        text = text[:i][::-1] + text[i:]
        #^text = from beginning to i reversed + from i to the end
    return text

#SUCCESSFUL
# =============================================================================
print(pancake_scramble('hello world'))
print(pancake_scramble('ilkka'))
print(pancake_scramble('pancake'))
print(pancake_scramble('abcdefghijklmnopqrstuvwxyz'))
print(pancake_scramble('this is the best of the enterprising rear'))