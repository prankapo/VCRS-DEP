import re

bin_count = 31

command = input("Enter the command: ")
lst1 = list()
num_list = list()
set1 = list()
set2 = list()
if re.search(':', command) :
    lst1 = re.findall('(.*)\s*:', command)
    lst1.append(re.findall(':\s*(.*)', command)[0])
else :
    lst1 = re.findall('\s*(.*)', command.rstrip())
print(lst1)
if lst1[0] == '' :
    set1.append(lst1[0])
if lst1[0].strip() == 'Hydrogen' or lst1[0].strip() == 'Helium' :
    set1.append(lst1[0].strip())
else :
    index = 0
    for char in lst1[0] :
        if char.isdigit() :
            index = index + 1
            continue
        else : 
            if (char == '+') or (char == ' ') :
                index = index + 1
                continue
            else :
                print('\aINVALID CHARACTER: ', char, "'")
                quit()
    num_list = re.findall('[0-9]+', lst1[0])
    for number in num_list :
        if int(number) < 1 or int(number) > bin_count :
            print(number, 'IS OUT OF RANGE\a')
            quit()
        else :
            set1.append(int(number))
if lst1[1] == '' :
    set2.append(lst1[1])
elif lst1[1].strip() == 'Hydrogen' or lst1[1].strip() == 'Helium' :
    set2.append(lst1[1].strip())
else :
    index = 0
    for char in lst1[1] :
        if char.isdigit() :
            index = index + 1
            continue
        else : 
            if (char == '+') or (char == ' ') :
                index = index + 1
                continue
            else :
                print('\aINVALID CHARACTER: ', char, "'")
                quit()
    num_list = re.findall('[0-9]+', lst1[1])
    for number in num_list :
        if int(number) < 1 or int(number) > bin_count :
            print(number, 'IS OUT OF RANGE\a')
            quit()
        else :
            set2.append(int(number))
print(set1)
print(set2)