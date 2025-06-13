# python

|Operator |	Name |	Description |
|---------|-------|----------------|
|a + b |	Addition |	Sum of a and b |
|a - b	| Subtraction |	Difference of a and b |
|a * b |	Multiplication |	Product of a and b |
|a / b	| True division |	Quotient of a and b |
|a // b | Floor division |	Quotient of a and b, removing fractional parts|
|a % b |	Modulus	Integer | remainder after division of a by b|
|a ** b |	Exponentiation |	a raised to the power of b|
|-a	| Negation |	The negative of a|


**Order of operations**
The arithmetic we learned in primary school has conventions about the order in which operations are evaluated. Some remember these by a mnemonic such as PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.


**Comparison Operations**
| Operation |	Description |	Operation	Description |
|-----------|-------------|----------------|
|a == b |	a equal to b	|	a != b	a not equal to b |
|a < b |	a less than b	|	a > b	a greater than b |
|a <= b |	a less than or equal to b	|	a >= b	a greater than or equal to b |

| Operator | Description  |
|------------- |--------------- |
(expressions...),
[expressions...], 
{key: value...}, {expressions...}  | Binding or parenthesized expression, list display, dictionary display, set display  |
| x[index], x[index:index], x(arguments...), x.attribute  | Subscription, slicing, call, attribute reference  |
| await x | Await expression |
| ** | Exponentiation | 
|+x, -x, ~x | Positive, negative, bitwise NOT |
| *, @, /, //, % | Multiplication, matrix multiplication, division, floor division, remainder |
| +, - | Addition and subtraction | 
| <<, >> | Shifts | 
| & | Bitwise AND |
| ^ | Bitwise XOR |
| | | Bitwise OR | 
| in, not in, is, is not, <, <=, >, >=, !=, == | Comparisons, including membership tests and identity tests| 
| not x | Boolean NOT| 
| and | Boolean AND |
| or | Boolean OR |
| if – else | Conditional expression |
| lambda | Lambda expression |
| := | Assignment expression |


**String**
| What you type... |	What you get |	example |	print(example)|
|------------------|---------------|----------|--------------|
|\' |	'|	'What\'s up?'	What's up?
|\" |	"	| "That's \"cool\""	That's "cool"
|\\ |	\	| "Look, a mountain: /\\" |	Look, a mountain: /\ |
|\n	| | "1\n2 3" |	1 nextline-> 2 3|

**set**
|Method	| Shortcut	| Description|
|-------|-----------|------------|
|add()  |	        |Adds an element to the set|
|clear()|	 	    |Removes all the elements from the set|
|copy()	|	        |Returns a copy of the set|
|difference()|	-	|Returns a set containing the difference between two or more sets|
|difference_update()|	-= |Removes the items in this set that are also included in another, specified set|
|discard()|	 	    |Remove the specified item|
|intersection()|	&	 | Returns a set, that is the intersection of two other sets|
|intersection_update()|	&=	|Removes the items in this set that are not present in other, specified set(s)|
|isdisjoint()|	 	|Returns whether two sets have a intersection or not|
|issubset()| <=	, <	|Returns whether another set contains this set or not,
Returns whether all items in this set is present in other, specified set(s)|
|issuperset()| >= ,> | Returns whether this set contains another set or not, Returns whether all items in other, specified set(s) is present in this set
|pop()|	 	|Removes an element from the set|
|remove()|	 	|Removes the specified element|
|symmetric_difference()|	^	|Returns a set with the symmetric differences of two sets|
|symmetric_difference_update()|	^=	|Inserts the symmetric differences from this set and another|
|union()|	|	|Return a set containing the union of sets|
|update()|	| =	|Update the set with the union of this set and others|

**Dictionary Methods**
|Method |	Description|
|-------|--------------|
|clear() |	Removes all the elements from the dictionary|
|copy() |	Returns a copy of the dictionary|
|fromkeys()	| Returns a dictionary with the specified keys and value|
|get()	| Returns the value of the specified key|
|items()|	Returns a list containing a tuple for each key value pair|
|keys()|	Returns a list containing the dictionary's keys|
|pop()	|Removes the element with the specified key|
|popitem()|	Removes the last inserted key-value pair|
|setdefault()	|Returns the value of the specified key. If the key does not exist: insert the key, with the specified value|
|update()	|Updates the dictionary with the specified key-value pairs|
|values()	|Returns a list of all the values in the dictionary|

**File**
A file is a contiguous set of bytes used to store data. 
This data is organized in a specific format and can be anything as 
simple as a text file or as complicated as a program executable.
In the end, these byte files are then translated into binary 1 and 
0 for easier processing by the computer.

Files on most modern file systems are composed of three main parts:
Header: metadata about the contents of the file (file name, size, type, and so on)
Data: contents of the file as written by the creator or editor
End of file (EOF): special character that indicates the end of the file

**File Paths**
When you access a file on an operating system, a file path is required. 
The file path is a string that represents the location of a file. 
It’s broken up into three major parts:
Folder Path: the file folder location on the file system where subsequent 
folders are separated by a forward slash / (Unix) or backslash \ (Windows)
File Name: the actual name of the file
Extension: the end of the file path pre-pended with a period (.) used to 
indicate the file type

/
│
├── path/
|   │
│   ├── to/
│   │   └── cats.gif
│   │
│   └── dog_breeds.txt
|
└── animals.csv

The Folder Path is path/to/. The File Name is cats. The File Extension is .gif. So the full path is path/to/cats.gif.



/
│
├── path/  ← Referencing this parent folder
|   │
|   ├── to/  ← Current working directory (cwd)
|   │   └── cats.gif
|   │
|   └── dog_breeds.txt  ← Accessing this file
|
└── animals.csv

The double-dot (..) can be chained together to traverse multiple directories above the current directory. For example, to access animals.csv from the to folder, you would use ../../animals.csv.

**Line Endings**
ASA standard states that line endings should use the sequence of the Carriage Return (CR or \r) and the Line Feed (LF or \n) characters (CR+LF or \r\n). The ISO standard however allowed for either the CR+LF characters or just the LF character.

**Character Encodings**
An encoding is a translation from byte data to human readable characters. This is typically done by assigning a numerical value to represent a character. The two most common encodings are the ASCII and UNICODE Formats. ASCII can only store 128 characters, while Unicode can contain up to 1,114,112 characters.

**Opening and Closing a File in Python**
file = open('dog_breeds.txt')

The first way to close a file is to use the try-finally block:
reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
finally:
    reader.close()

The second way to close a file is to use the with statement:
with open('dog_breeds.txt') as reader:
    # Further file processing goes here

 represents opening the file in read-only mode as a text file:
 with open('dog_breeds.txt', 'r') as reader:
    # Further file processing goes here

|Character	   |Meaning|
|--------------|-------|
|'r'	       |Open for reading (default)|
|'w'	       |Open for writing, truncating (overwriting) the file first|
|'rb' or 'wb'  |Open in binary mode (read/write using byte data)|



There are three different categories of file objects:
1.Text files:
   A text file is the most common file that you’ll encounter.
   open('abc.txt')
   open('abc.txt', 'r')
   open('abc.txt', 'w')
   With these types of files, open() will return a TextIOWrapper file object:
   >>> file = open('dog_breeds.txt')
   >>> type(file)
   <class '_io.TextIOWrapper'>   
2.Buffered binary files:
    A buffered binary file type is used for reading and writing binary files.
    open('abc.txt', 'rb')
    open('abc.txt', 'wb')
    With these types of files, open() will return either a BufferedReader or BufferedWriter file object:
    >>> file = open('dog_breeds.txt', 'rb')
    >>> type(file)
    <class '_io.BufferedReader'>
    >>> file = open('dog_breeds.txt', 'wb')
    >>> type(file)
    <class '_io.BufferedWriter'>
3.Raw binary files:
    generally used as a low-level building-block for binary and text streams.
    open('abc.txt', 'rb', buffering=0)
    With these types of files, open() will return a FileIO file object:
    >>> file = open('dog_breeds.txt', 'rb', buffering=0)
    >>> type(file)
    <class '_io.FileIO'>

|Method	|What It Does|
|-------|------------|
|read(size=-1)	|This reads from the file based on the number of size bytes. If no argument is passed or None or -1 is passed, then the entire file is read |
|readline(size=-1)	|This reads at most size number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read |
|readlines()|This reads the remaining lines from the file object and returns them as a list |

|Method	       |What It Does|
|-------|------------|
|write(string)	| This writes the string to the file.|
|writelines(seq) |	This writes the sequence to the file. No line endings are appended to each sequence item. It’s up to you to add the appropriate line ending(s).|

|Value |	Interpretation|
|-------|------------|
|0x89|	A “magic” number to indicate that this is the start of a PNG|
|0x50 0x4E 0x47	| PNG in ASCII|
|0x0D 0x0A	| A DOS style line ending \r\n|
|0x1A	| A DOS style EOF character|
|0x0A |	A Unix style line ending \n|

Working With Two Files at the Same Time:
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))

Additionally, there are built-in libraries out there that you can use to help you:
wave: read and write WAV files (audio)
aifc: read and write AIFF and AIFC files (audio)
sunau: read and write Sun AU files
tarfile: read and write tar archive files
zipfile: work with ZIP archives
configparser: easily create and parse configuration files
xml.etree.ElementTree: create or read XML based files
msilib: read and write Microsoft Installer files
plistlib: generate and parse Mac OS X .plist files

There are plenty more out there. Additionally there are even more third party tools available on PyPI. Some popular ones are the following:
PyPDF2: PDF toolkit
xlwings: read and write Excel files
Pillow: image reading and manipulation
