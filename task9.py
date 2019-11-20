#-*- coding: utf8 -*-
#4523

# 40 / 2 = 20
# 40 / 4 = 10
from multiprocessing import Pool, TimeoutError
import time
import os
from datetime import datetime

def primers(num):
    for i in range(2, num/2):
        if num % i == 0:
            return num, False
        else:
            pass
    return num, True

if __name__ == '__main__':
    pool = Pool(processes=4)
    """
    si volem que hi hagi més o meys processos actius només tenim que modificar
    el process per augmentar o disminuir els processos. Depen del número de nuclis
    del processador, no val la pena posar-ne més processos del número de nuclis que tenim
    per ex si tenim 4 nuclis no fer més de 4 processos a l'hora.
    """
    l = range(40000000, 40000100)#[45445535, 56534563, 43566487, 43635453, 52346557, 53454433, 43546453, 26847357, 54577647]
    start = datetime.now()

    for i in pool.map(primers, l):
        print i
    print datetime.now() - start
