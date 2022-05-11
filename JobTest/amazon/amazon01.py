import re


def findPasswordStrength(password):
    vowelList =['a','i','u','e','o']
    ct = 0
    vct = 0
    cct = 0
    for c in password:
        if c in vowelList:
            if cct > 0:
                ct += 1
                vct = 0
                cct = 0
            else:
                vct += 1
        else:
            if vct > 0:
                ct+=1
                vct = 0
                cct = 0
            else:
                cct += 1
    return ct

