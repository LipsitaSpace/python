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

