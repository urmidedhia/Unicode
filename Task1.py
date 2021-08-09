number = int(input("Enter number of words : "))
words = []
print("Enter the words : ")
for i in range(number):                            # Taking input in a list words
    element = input()
    words.append(element)

dist = []
for word in words:                                 # Adding distinct words to a list dist
    if word not in dist:
        dist.append(word)
distinct = len(dist)                               # Number of distinct words is length of list dist
print("Number of distinct words is", distinct)

occur = []
for word in dist:                                  # Adding number of occurrences of each distinct word in a list occur
    count = 0
    for item in words:
        if word == item:
            count += 1
    occur.append(count)
    print(count)                                   # Printing number of occurrences of each distinct word
