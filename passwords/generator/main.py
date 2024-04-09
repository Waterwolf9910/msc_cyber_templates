import secrets # Crytographically Secure RNG
import string # String Constances

# Modifiable below
# The values in this grouping are strings
# String variables must start
password: str = ??


# The values in this grouping are integer numbers

# Here we insert the length of the password
length: int = ??

# Here 
start: int = ??


# The values in this grouping are booleans
# Booleans can only be True or False

# Here we set if we want letters
letter: bool = ??
# Here we set if we want uppercase letters
upper: bool = ??
# Here we set if we want numbers
num: bool = ??
# Here we set if we want special characters (i.e. !, @, ...etc)
special: bool = ??


# DO NOT TOUCH:

allowed: str = ''
if (letter):
    allowed += string.ascii_letters if upper else string.ascii_lowercase

if (num):
    allowed += string.digits

if (special):
    allowed += string.punctuation


while start - 1 < length + 1:
    password += allowed[secrets.randbelow(len(allowed))]
    start += 1

# Here we print out our password
print(??)

