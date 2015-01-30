#!/usr/bin/env python
from app.generate import *
import sys

gen = OutputGenerator("template")
out = gen.generate(sys.argv[1])
print(out)
