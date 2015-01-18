#!/usr/bin/env python
from app.generate import *

gen = OutputGenerator("template")
out = gen.generate("input.txt")
print(out)
