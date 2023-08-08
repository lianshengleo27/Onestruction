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

def get_data_ascending(infile:str)->List[float]:
    L = []
    Q = []
  
    _p = pathlib.Path(infile)

    with open(_p) as file:
        csvfile = csv.reader(file)
        for row in csvfile:
            L.append(int(row[0]))
            Q.append(int(row[1]))
        lst = list(zip(Q,L))
        #sort quanlity in ascending order first, and then length in descending order
        lst.sort(key=lambda x: (int(x[0]), -int(x[1])))
        return lst
    

def get_data_descending(infile:str)->List[float]:
    L = []
    Q = []
  
    _p = pathlib.Path(infile)

    with open(_p) as file:
        csvfile = csv.reader(file)
        for row in csvfile:
            L.append(int(row[0]))
            Q.append(int(row[1]))
        lst = list(zip(Q,L))
        #sort quanlity in descending order first, and then length in ascending order
        lst.sort(key=lambda x: (-int(x[0]), int(x[1])))
        return lst

