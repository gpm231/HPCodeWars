import re

string  = "Hello how are you doing"

print(re.search("^H.*ing$", string))