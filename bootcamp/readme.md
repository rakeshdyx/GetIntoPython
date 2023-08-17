## Covered Topics

<b>Loop</b>
- Loop using list
- Itirate over `range()`
- While Loop

<b>Functions</b>
- Parameter and Argumnets
- Positional vs. Keyword Arguments
- Functions with Return type
- Multiple return
- Docstrings
- Print vs Return
- Recursion

<b>Data Structure</b>
- List
- Dictionaries
- Nesting
   - Nesting a List in a Dictionary
   - Nesting a Dictionary in a Dictionary
   - Nesting a Dictionary in a List
- List Comprehension
- Dict Comprehension


<b>Scope</b>
- Namespace: Local and Global scope
- Modify Global scope
- Constant



<b>OOPs</b>
- Class And Objects
- Construction of Object and Accessing Attribute and Methods
- Attributes, Class Constructors, `__init__()` Function

<b>Files, Directories and Paths</b>
- Open, Read and Close File with
- Work with CSV
- Work with JSON

<b>Debugging Techniques</b>
- Describe the problem
- Reproduce the bug
- 




 >Notes
- List comprehension syntax `new_list = [new_item for item in list]`
- `title()` function to convert to title case in python
- Python don't follow the balock scope
- `global varname` syntax to use a global variable as a local however its not recomended as it make your code more failable.
- `global` can be use as constant and the constant always use upper case.

**OOPs**
- The `self` keyword is used to represent an instance (object) of the given class.
- When a function ties to an object is called as method
- What the object `has` is called `attributes` and What the object does is called `method`
- Object can help you to access attributes and methods
- `Constructor` allows us to specify what should happen when the object being constructed.

**Files, Directories and Paths**
- `with open(file.txt) as file` can take care of both open, read and close a file. No need to explicitily invoke `file.close()` function
- By default the file mode is readonly. To make it RW,mode should be spesificed inside `with open("file.txt", mode="rwa") as file`

<b>Play with the Challenge</b>
 - FizzBuzz
 - HANGMAN
 - Make a calclulator
