def word_match(list):
    count = 0
    words = []
    for i in list:
        if len(i) >1 and i[0] == i[-1]:
            count += 1 
            words.append(i)
    print(words)
    print("the number of words that match are ", count)
        
word_match(['animal', 'ava', 'bee', 'dad', 'pop'])

