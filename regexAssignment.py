import re

def classtask():
    with open('data.txt', 'r') as file:
        text = file.read()

    pattern_a = r'\ba\w*\b'
    pattern_b = r'\bb\w*\b'

    words_starting_with_a = re.findall(pattern_a, text, re.IGNORECASE)
    words_starting_with_b = re.findall(pattern_b, text, re.IGNORECASE)

    with open('A.txt', 'w') as file_a:
        file_a.write('\n' + str(words_starting_with_a) )

    with open('B.txt', 'w') as file_b:
        file_b.write('\n' + str(words_starting_with_b) )

classtask()
print("Data Saved successfully to new file")


