# ColorText
A library for good color in Python!  
In Python while we are coding, we can need color in a String...  This library is the solution.

## How to use
Firstly, we have a file called hello.py with this:  
```python
print('I need some color :(')
```  
In this example, you have a print statement, who needs some cool color, let's give it.  
```python
from ColorText import ColorText

color = ColorText() # Give it a variable

print(color.red('Red Color!'))

print(color.green('Green Color!'))

print(color.yellow('Yellow Color!'))

# And more...
```
