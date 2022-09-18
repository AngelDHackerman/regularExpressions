# Regular Expressions

#### The (.)"dot" pattern:

- In the search patterns you can put a "dot" and it will find a character.


Find __one characterj__: (it will match every single character in the document)
`.`

Find __a set of 3 consecutive characters__:
`...`

Find __a set of 3 consecutive characters followed by a space__:
`... `


### Predefined and built classes


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


#### Asterisk (*):

It is a __greedy__ selector, the __asterick will match zero or more__.


`.*` Look for __all the characters, not one by one.__

`\d*` Look for __all the digits__ in the document.

