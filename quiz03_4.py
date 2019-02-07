s = """We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process.""".replace("," ,"").replace(".","")\
    .replace("\n","").upper()

words = s.split(" ")
frequency = {}
for word in words:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
for word in frequency_list:
    print(word, frequency[word])
