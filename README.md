This is a personal project in making a very simple Python interpreter for my very simple language.

FEATURES:
- simple scanner
- simple AST for use in a descent tree parser
- expressions will use reverse-polish notation
- the memory is made with a simple stack and heap system:
  - the stack will hold all of the working data
  - the heap is a map between the identifier and the value it represents, which can be updated using code
- the language is procedural
- there are only three native data types: String, Bool, Integer
- the list of keywords is very small:
    - if
    - else
    - elif
    - while
    - int
    - bool
    - string
    - return
    - fn
- the list of literals is also small:
    - true
    - false
    - any integer
    - any word (for identifiers)
- there are operators for each type of literal:
    - strings:
        - +: this concatenates two strings together
    - bool:
        - and: this is true if two bools are equal to eachother
        - or: this is false if two bools are not equal to eachother
        - not: this negates a bool
    - int:
        - binary operators:
            - +: adds two integers
            - -: takes away two integers
            - *: multiplies two integers
            - /: divides two integers
            - <: returns true if a number is less than another
            - ">": returns true if a number is greater than another
            - =: retuns true if two numbers are equal to eachother
        - unary operators:
            - -: this turns a positive integer negative and vice-versa
- the language has syntax inspired by c:
    - a semi-colon identifies the end of the statement
    - if, elif and while take a bool expressive argument in () brackets
    - after a function or control flow a {} will identify the next block of code
- there are some simple changes though:
    - arguments passed into functions will follow reverse-Polish notation style, e.g.: instead of add_two_numbers(a, b); we will use a b addd_two_numbers;
    - reassigning a variable will not use the = sign, it will instead use a colon, e.g.: instead of x = x * 4; we will use x: x 4 *;
- at the moment the standard library will be able to print to the console, however the idea is to be able to expand this in the future to make this into a more useful language

