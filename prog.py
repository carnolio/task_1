vowelsCount = {"a": 0, "o": 0, "u": 0, "i": 0, "e": 0, "y": 0}
text = input("input your text: ")
for letter in text:
    if letter in vowelsCount.keys():
        for key in vowelsCount.keys():
            if letter == key:
                vowelsCount[letter] += 1
printVowels = ""
for key in vowelsCount.keys():
    printVowels= printVowels+key+" "+str(vowelsCount[key])+","
printVowels=printVowels[0:len(printVowels)-1]
print(printVowels)