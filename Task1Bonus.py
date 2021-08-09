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

for j in range(distinct):                          # Arranging both the lists in descending order of occurrences
    for i in range(j + 1, distinct):               # Since length of dist is same as length of occur
        if occur[j] < occur[i]:
            temp = dist[j]                         # Swapping in dist list
            dist[j] = dist[i]
            dist[i] = temp

            temp = occur[j]                        # Swapping in occur list
            occur[j] = occur[i]
            occur[i] = temp

print("The input in descending order of occurrences is : ", dist)
print("The most repeated word is : ", dist[0])
print("The least repeated word is : ", dist[-1])
