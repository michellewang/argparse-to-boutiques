import argdump
from .parser import _build_parser

parser = _build_parser()

json_str = argdump.dumps(parser) 
print(json_str)
