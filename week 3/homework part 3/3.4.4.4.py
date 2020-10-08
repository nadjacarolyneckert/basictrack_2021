words = ["watery", "announce", "baseball", "sheet", "fruit", "measly", "maddening", "detect",
         "attack", "automatic", "hammer", "harbor"]
count_words_length5 = 0

for word in words:
    if len(word) == 5:
        count_words_length5 +=1

print("There are ", count_words_length5, "words with 5 letters in the sample")