import pathlib
from typing import List
import re
import csv
from math import ceil
def get_data(infile:str)->List[float]:
    """ Reads a file of numbers and returns a list of (count, number) pairs."""
    # _p = pathlib.Path(infile)
    # input_text = _p.read_text()
    # numbers = [ceil(float(n)) for n in re.findall(r'[0-9.]+', _p.read_text())]
    L = []
    Q = []
  
    _p = pathlib.Path(infile)

    with open(_p) as file:
        csvfile = csv.reader(file)
        for row in csvfile:
            L.append(int(row[0]))
            Q.append(int(row[1]))
        return list(zip(Q,L))
        #since the program only accept input as (Q,L)
        #when we input csv as (L,Q), we need to switch the order





    # for n in numbers:
    #     if n not in nr and n != 0:
    #         quan.append(numbers.count(n))
    #         nr.append(n)
    # return list(zip(quan,nr))

