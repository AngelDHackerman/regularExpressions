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


## Counters {n,n}

It is use to stablish how many times a character must appear. 

`\d{2,7}` It will match a __set of digits from 2 up to 7 numbers together__. 

`\d{4,}` It will match a __set of 4 or more digits together__.

`\w{5,}` It iwll match a __set of characters (number/words) of 5 or more__.

`\d{2,2}\-?\d{2,2}\-?\d{2,2}\-?` It will __match a set of 2 digits (3 times)__ together and __it migth or might not be followed by a "-"__. 
- the "?" indicates that the "-" could be appear or not. 

###### Creating a class with counters and escaped characters:

`\d{2,2}[\-\.]?` __match a set of 2 digits__ (as many as the appear in the document), and they __could or could not be followed by a "-" or "."__.