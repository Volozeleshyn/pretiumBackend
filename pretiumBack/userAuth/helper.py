import os
import time
from binascii import hexlify

"""" keep secret """
good_string = '#7p3e5j+0$cr&(jqx=kpk(-se(#%=hg^n!tpd_v-a=+gvd+=e2'


def create_hash():
    return str(hexlify(os.urandom(16)), 'ascii')


def caesar_cypher(str):
    ret = ''
    for i in range(len(str)):
        ret = ret + good_string[ord(str[i]) % 50]
    return ret


def time_stamp():
    return int(round(time.time()))
