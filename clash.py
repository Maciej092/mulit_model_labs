from typing import *
from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

temp = defaultdict(list)

for string in strs:
    temp[''.join(tuple(sorted((string))))].append(string)



