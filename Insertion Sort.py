### Insertion Sort ###
import random

## The array being initisialised
Array = [random.randint(1,99) for i in range(20)]

print("Unsorted Array:",Array)

## This is the basic sort

for i in range(1,len(Array)):
    pos = i ## The position of sort
    CV = Array[i] ## The Value it is moving
    while pos > 0 and CV < Array[pos-1]:
        Array[pos] = Array[pos-1] ##moving the places 
        pos -= 1
    Array[pos] = CV ##places it in the correct location 

print("Sorted Array:",Array)


