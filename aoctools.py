import re

# Load today's file
def ld(filename):
  return [l.strip() for l in open("./" + filename + ".data", "r") if l != "\n"] 

# Return True if  `search_string` matches `regex_pattern`
def find(regex_pattern, search_string):
  return re.search(regex_pattern, search_string) != None

# Print the items of `lines` that match `regex_pattern`
def grep(regex_pattern, lines):
  [print(l) for l in lines if re.search(regex_pattern, l)]

# Extract the subset of elements from `lines` that match `regex_pattern`
def grepfilter(regex_pattern, lines):
  return [l for l in lines if find(regex_pattern, l)]

# Join a list of strings together into a single string with an optional delimiter between each element
def concat(elements, delimiter=''):
  return delimiter.join(elements)

# Accepts a list and a function, and returns a dict which maps the list elements by the result of func(element)
def groupby(elements, func):
  M = {}
  for e in elements:
    if not func(e) in M:
      M[func(e)] = []
    M[func(e)].append(e)
  return M