# Regular Expressions

#### The (.)"dot" pattern:

- In the search patterns you can put a "dot" and it will find a character.


Find __one characterj__: (it will match every single character in the document)
`.`

Find __a set of 3 consecutive characters__:
`...`

Find __a set of 3 consecutive characters followed by a space__:
`... `


## Predefined and built classes


#### Digits (\d):

It will __find all the digits__ in the document.

`\d` 

Find __a set of 3 consecutive digits__:

`\d\d\d` 


#### Words (\w):

It can __include numbers, words, but NOT characters:__

`\w`

#### Spaces (\s):

It will select just the spaces in the document (it can also include the "new line" character)

`\s`


#### Classes ([]):

You can use it to look for ranges.

`[]`

`[6-9]` It will look for __numbers between the 6 and the 9__.

`[a-f]` It will look for __lower case letters between the "a" and the "f"__.

`[a-fA-F]` It will look for __lower case and UPPER case letters__ between the "a" and the "f".

`[a-fA-F0-5_\.]` It will look foor __lower case and UPPER case letters from A to F, the character "_" and the dot character "."__


## Delimiters

#### Asterisk (*):

It is a __greedy__ selector, the __asterick will match zero or more__.


`.*` Look for __all the characters, not one by one.__

`\d*` Look for __all the digits__ in the document.

`\d*[a-z]` It will match if there is __zero or more digits followed by letter from a to z.__


#### Plus (+):

It will look for __one or more matches__.

`\d+`  A digit that has __one or more digit beside it__.

`\d+[a-z]` It will look for __one or more digits followed by the letters form a to z__. 


#### Question Mark (?):

It will match for __zero or one occurrences__. 


## Counters {}

It is use to stablish how many times a character must appear. 

`\d{2,7}` It will match a __set of digits from 2 up to 7 numbers together__. 

`\d{4,}` It will match a __set of 4 or more digits together__.

`\w{5,}` It iwll match a __set of characters (number/words) of 5 or more__.

`\d{2,2}\-?\d{2,2}\-?\d{2,2}\-?` It will __match a set of 2 digits (3 times)__ together and __it migth or might not be followed by a "-"__. 
- the "?" indicates that the "-" could be appear or not. 

###### Creating a class with counters and escaped characters:

`\d{2,2}[\-\.\ ]?` __match a set of 2 digits__, and they __could or could not be followed by a "-", "." or " "__.

`\d{2,2}[\-\.\ ]?\d{2,2}[\-\.\ ]?\d{2,2}[\-\.\ ]?` Same has above but it will find 3 sets of 2 digits together.


## (?) As a Delimiter.

It will match the __set of any characters delimited by a ","__.

`.+?,` "." = any character, "+" = one or more characters, "?" = delimited by a: ","


## NOT (^), negate a match or a class. 

`\D` This match everything __else than a Digit__.

`\W` This match everything __else than a Digit/Letter__.

`\S` This match everything __else than a Space__.

`[^0-5a-c]` It matches everything __else than the numbers 0 to 5 and a to c__.

`\d\d\D?\d\d\D?` It will __match something like this : 44-55- or 44.55. or 44a55b__, etc.


## Start (^) and End ($) of a line.

`^\d$` It will find a line that __starts with a digit and ends with a digit__.

`^\d{3,6}$` It matches a line that __starts with 3 digits and ends UP TO 6 digits__.

`^[^\d].*$` It matches a line that __starts with something that is NOT a digit__ and ends with any other characters.

`^\w+,\w+,\w+$` This match something like this: csv1,csv2,csv3 | 1234,5430,2304 | 123,432,566. It must have exactly 3 columns.


## Searching Logs.

`^\[LOG.*\[WARN\].*$`  With this Regex you can __find all the warnings__ in the "liners.txt" file

`^[LOG.*\[LOG\].*user:celismx\] .*$`


## Searching Phone numbers.

`^\+?\d+[#pe]?\d*$`  The pattern to match will look for:

1) it might start with a "+" signe.  (^\\+?)
2) it must have one or more digits.  (\d+)
3) digits might be followed by a: "#" "p" or "e".  ([#pe]?)
4) and lastly bring all the digits (if there are) after all the preceeded match.  (\d*)


`^\+?\d{2,3}[^\da-zA-Z]?\d{2,3}[^\da-zA-Z]?\d{2,3}[#pe]?\d*$`  This stands for:

1) It might start with a "+" signe. (^\\+?)
2) Look from 2 up to 3 digits together. (\d{2,3}).
3) And those digits __migth be followed__ by something __that is not__ a digit or letters. ([^\da-zA-Z]?)
4) lastly they might be followed by "#" "p" or "e". ([#pe])
5) And the some of the previous steps are repited in order to match our pattern.


## Searching URL. 

`https?:\/\/[\w\-\.]+\.\w{2,5}\/?\S*`

1) https, it might have a "s" at the end or not. (https?)
2) it has to be followed by two slashed.  (\\/\\/)
3) the slash could be followed by __one or more__: letters, "-" or ".".  ([\w\\-\\.]+)
4) then followed from 2 up to 5 dots, digits or letters.  (\\.\w{2,5})
5) also it could have a "/" and a non-space at the end. (\\/?\S*)


## Searching for emails.

`[\w\._]{5,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}`

1) It starts with a digit/word or "." or "_" from 5 up to 30 characters.
2) migth be a "+"
3) after the "+" a letter or digit from 0 up to 10 characters.
4) this is separated by a "@"
5) from 3 up to infitive letters/digits or "." or "-"
6) followed by from 2 up to 5 "." or letters/digits.  __(this can be a regional TLD like: .gt .mx .jp)__


## Searching Names.

`^[A-Z][a-z]{3,}\s?[A-Z]?[a-z]{0,}`


