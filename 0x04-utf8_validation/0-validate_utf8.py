#!/usr/bin/python3
"""UTF-8 Validation"""

def validUTF8(data):
    """Determines if a given data set
      represents a valid UTF-8 encoding"""
    bytes = 0
    for i in data:
        byte = format(i, '#010b')[-8:]
        if bytes == 0:
            if byte[0] == '1':
                bytes = len(byte.split('0')[0])
            if bytes > 4 or bytes == 1:
                return False
            if bytes == 0:
                continue
        else:
            if not byte.startswith('10'):
                return False
        bytes -= 1
    return bytes == 0