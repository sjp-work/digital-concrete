import shutil
from pathlib import Path
import random
import time

print ("Welcome to your digital muse.")

user_input = input("Write down your input.")
file_html = open("demo.html", "w")
file = open('UserInput.txt', 'w')
file.write(user_input)
file.close()
line_length = int(input("How many words per line do you want? "))
number_of_lines = int(input("How many lines do you want? "))
to_store = [] # stores final poem before writing to file
final_to_print =[] # the completed final poem!

# Read the Poem file

# open poem one and read
p1_lines = []

file = open('UserInput.txt', 'r')
for line in file:
    for word in line.split():
        p1_lines.append(word + "")
        #print (word)

file.close()

# open poem two and read

p2_lines = []

options = [
    'Shadowbook.txt',
    'Rupi Kaur.rtf',
    'RupiGlitch.txt',
    '1337SPEAK.txt',
    'ASCII.txt',
    'haiku.txt'

]

print('Which file should I merge?')
print('[0] Shadowbook')
print('[1] Rupi Kaur')
print('[2] Glitch')
print('[3] L33tspeak')
print('[4] ASCII')
print('[5] Haiky')

#otherfile = random.choice(options)
choice = int(input("Enter a number"))
otherfile = options[choice]

file2 = open(otherfile, 'r')

for line in file2:
    for word in line.split():
        p2_lines.append(word + " ")
        #print (word)

file2.close()

# Combines the two poem files

firstfile = p1_lines
secondfile = p2_lines

# copy first poem file to second poem file
for x in firstfile:
    secondfile.append(x)

# switch variable name
final_file = secondfile

# print (final_file) '''test print '''

print (len(final_file))
tw = (len(final_file)) # total words

for i in range (len(final_file)):
    random_word = random.randrange(len(final_file))
    #print (final_file[random_word])
    final_file.append(final_file[random_word])
    del final_file[random_word]

# how many words per line
for i in range (5, len(final_file), line_length):
    #print (final_file[i:i+line_length])
    to_store.append(final_file[i:i+line_length])

# # create the line breaks for the poem
# current_line = 0
# while current_line < len(to_store):
#     for i in range(current_line, min(current_line + number_of_lines, len(to_store))):
#         final_to_print.append(to_store[i]) # add poem lines to the file
#     final_to_print.append("")    
#     current_line += number_of_lines
    
final_to_print.extend(to_store[:number_of_lines])

# Write to a file

newfile = 'text.txt'
print()
print("The merged content of the 2 files will be in", newfile)


MyFile=open(newfile,'w')
for x in final_to_print:
    MyFile.writelines(x)
    MyFile.write('\n')
MyFile.close()

with open('start.html') as file:
   info1 = file.read()

# Reading information from the second file
with open(newfile) as file:
   info2 = file.read()

# Reading information from the third file
with open('end.html') as file:
   info3 = file.read()


title = input("Enter a title")

# Merge start.html, text.txt and end.html together
info1 += ""
info1 += "<h1>"+title+"</h1>"
info1 += info2
info1 += info3

with open ('result.html', 'w') as file:
   file.write(info1)


print("\nYour Poem is ready.!")




#Function_Name = open("My new poem","File_operation")

#Function_Name.write("Adding_Input_data_using_HTML_Synatx_separted_by_/n")

#Function_Name.close()