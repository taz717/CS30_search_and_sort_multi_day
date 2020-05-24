'''
Moataz Khallaf A.K.A Hackerman
main
2/20/2019
'''
###___imports___###
import csv, time, random

###___vars/arrays/dicts___###

#useless and overcomplicated. I'm just too proud to take it out
DvM = { #Disney vs Marvel ....
	"D" : 1,
	"M" : 2
}

char = 1


###___Subs___###
###input
def menu():
    x = int(input('''
    yo yo yo... gang gang you tryna search for some heroes???
    if you tryna do it fast and you are in a rush to get something done
    please type 1 and press enter.
    
    If you want to do it the slow and boring way please type 2 and press
    enter.
    >:(
    
    '''))

    return x


def getRawData(fileName):
	import csv
	tempLi = []
	fil = open(fileName) #thanks for the code boss
	text = csv.reader(fil)
	for line in text:
		tempLi.append(line)
	var = tempLi.pop(0)
	return tempLi, var

###proc
def binSearch(li, val): #this is just the code you gave us for bin search I'm pretty sure, slightly changed to fit 2D
    start = 0 #Lowest index value to calc midpoint
    end = len(li) - 1 #highest index value to calc midpoint

    while start <= end:
        midP = (start + end) // 2 #midpoint calc

        if li[midP][0] == val: #found test
            return li[midP]

        elif val > li[midP][0]: #if value is greater than the midpoint, redefine the lowest index value to be one higher
            #than the midpoint index value
            start = midP + 1

        else: #if value is less than the midpoint, redefine so it's 1 lower than midpoint index value
            end = midP - 1

    return False

def insertSort(li): #view insertion sort manual for in depth explanation, however; the gist is just that
    for i in range(len(li)): #its the fastest sorting method by inserting the smallest num in the list at the front
        for j in range(i, len(li)): #everytime as it goes through the list from the right. explanation in read.md
            if li[j][0] < li[i][0]:
                li.insert(i, li.pop(j))
    return li


###output
def charDisplay(char):
    print(", ".join(char))

###___main___###
###input
searchPick = menu()
if searchPick == 1: #inputs required to start the searches eg: name or id

    super = input('''
    ello mate, you ready to search and sort through some heroes????
    Well boi oh boi do I have the program for you partner.
    Just need you to enter the her's universe
        eg. D or M (doesn't even need to be capital letters ;))
    ''')

    ID = input('''
    Now you need the ID
        eg. 001
    ''')

    super = super[0].upper()

    superID = super + ID

if searchPick == 2:
    print('''
    wow... you must be crazy this will take a minute but at least you get to search by name.
    ''')

    name = input('''
    Please enter the character's name I guess...
    ''')


###proc
rawArr, headers = getRawData('comicBookCharData_mixed.csv')

if searchPick == 1:

    startTime = time.perf_counter()
    rawArr = insertSort(rawArr)
    char = (binSearch(rawArr, superID))
    endTime = time.perf_counter()

if searchPick == 2: #This uses linSearch to figure out if the name of the char is in the list

    startTime = time.perf_counter()
    for i in range(len(rawArr)): #I would split it into two separate lists beforehand to make it faster
        if name == rawArr[i][1]: #but that would take too much effort when you can just use the way faster method
            char = rawArr[i]
            endTime = time.perf_counter()

        else:
            print(name, "is not in the list sorry chief")

###output

charDisplay(char)
print(endTime - startTime)
print("was the time it took to finish the search")