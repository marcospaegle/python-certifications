"""1.2.1 - Keywords, statements vs expressions, indentation, comments."""
import keyword

print(len(keyword.kwlist))         # -> 35
print(keyword.iskeyword("if"))     # -> True
print(keyword.iskeyword("print"))  # -> False
print(keyword.iskeyword("True"))   # -> True

# Code after a dedent always runs: it is not part of the block.
temperature = 20
if temperature > 30:
    print("hot")
print("done")                      # -> done

# A '#' inside a string is not a comment.
print("#1")                        # -> #1

# Implicit line joining inside parentheses
total = (1 +
         2 +
         3)
print(total)                       # -> 6

# pass as an empty-block placeholder
if total:
    pass
print("after pass")                # -> after pass
