#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from collections import defaultdict
import sys
import operator
from traceback import StackSummary

if __name__ == '__main__':

    Dict = defaultdict(list)


    for line in sys.stdin:

        key, val = line.split('\t')
        val = float(val)
        Dict[key].append(val)

    for clave, lista in Dict.items():
        suma = round(sum(lista), 1)
        prom = sum(lista)/len(lista)

        values= [clave, suma, prom]

    sys.stdout.write("{}\t{}\t{}\n".format(values[0], values[1], values[2]))