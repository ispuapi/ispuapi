#!/usr/bin/python
# data cleaner function

__author__ = 'vickydasta'

def tolatin1(data):
    return data.encode('latin-1')

# garbage tags remover
def removegarbage(data):
    return ' '.join(data.split(' '))

def tolist(data):
    return data.split(' ')

def cleaner(data):
    return tolist(removegarbage(tolatin1(data)))
