#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import operator
import sys

if __name__ == '__main__':

    list = []
    

    for line in sys.stdin:

        key, fecha, val = line.split('\t')
        val = int(val)
        mi_t = key, fecha, val
        list.append(mi_t)

    sortedDict = sorted(list, key = operator.itemgetter(0, 2))
    for line in sortedDict:
              

        sys.stdout.write('{}  {}  {}\n'.format(line[0], line[1], line[2]))
