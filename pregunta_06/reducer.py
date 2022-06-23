#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from curses import keyname


if __name__ == '__main__':

    keyname = None
    max = 0
    min = 0

    for line in sys.stdin:

        key, val = line.split('\t')
        val = float(val)


        if key == keyname:
            if val > max:
                max = val
            else:
                val = max
            
            if val < min:
                min = val
            else:
                val = min 
                                 
        else:
            if keyname is not None:
                sys.stdout.write('{}\t{}\t{}\n'.format(keyname, max, min))

                keyname = key
                max = val
                min = val

    sys.stdout.write("{}\t{}\t{}\n".format(keyname, max, min))