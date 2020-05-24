# searchNsortMultiDay

Search and sort through DC and Marvel Chars

## dayOne
This project is meant to sort and search through a list of super
hero chars. It's designed in such a manner that the csv file
containing the data is put in the same directory as the main
file itself.

###intro
these notes were left to explain the code used in the program
in depth if anyone wishes to edit or use it but does not
understand the concepts or how they where used.

## Search Algorithms
### linear search
Linear search is finding information in an array item by item
(line by line). This is the easiest method to program however,
it's the least efficient.

```
li = [some number of values
for i range(len(li)):
    if li[i] == value:
        return true
```

Linear Search's time to process is directly proportional to
the length of the data set being processed. The bigger the set
the more time it will take.


### Binary search
Binary search followed the _divide-and-conquer_ technique of
finding a value. It takes an ordered set of data and tests
the middle number, then it cuts the set in half and reruns
the test if the midpoint is not the searched value.

##sorting
just like with search algorithms, sorting ones have varying
levels of effincy. There are several types of sort algorithms
including; bubble sort, selection sort, insertion sort and merge
sort. more complicated sorts algorithms like .sort()
for python arrays,use a combination of simpler sorts. python
uses timsort, which is a combination of merge and insertion
sorts designed by time peters

###insertionSort
Insertion sort goes through the list and inserts the lowest
value into the current testing position. As it progresses
through the list, more and more of the list is sorted
to the left of the testing position.

aside: there are to common sorting algorithms. One searches
to the left of the current testing position while the other;
to te right of the current resting position. In general the
right one is faster because it can arrange multiple values in
a single pass.

| 5 | 17 | 13 | 11 | 1 | 7 | 3 |
| --- | --- | --- | --- | --- | --- | --- |
| __1__ | 5 | 17 | 13 | 11 | 7 | 3 |
| 1 | __3__ | 5 | 17 | 13 | 11 | 7 |
| 1 | 3 | __5__ | 17 | 13 | 11 | 7 |
| 1 | 3 | 5 | __7__ | 11 | 13 | 17 |
| 1 | 3 | 5 | 7 | __11__ | 13 | 17 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 17 |
| 1 | 3 | 5 | 7 | 11 | 13 | __17__ |



##dayTwo
This project is legit the most annoying thing ever because all I
do is overcomplicate code and it makes a simple copy/past project
like ten times harder. It's done though using insertion sort and
binary search to figure whether they want dc or marvel. Will work
on adding a timer and another method of searching. like maybe
linear name search but I'd have to split it into 2 different
arrays to make the wait times somewhat short.

##dayThree
polish is all done. finished the search by name and added all
the needed comments to make sure that the basic concept is given.
added the notes from class to the top in case someone out of the
class wished to view the code but didn't understand how the
search and sort algorithms worked or why they were being used.
This is the last entry due to the program being completed.
Maybe some minor bug fixes could be introduced, however; the 
code is self explanatory to use and the inputs give you examples
of how to insert the text.