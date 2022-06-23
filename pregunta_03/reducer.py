#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import operator
import sys

if __name__ == '__main__':

    dict = {}

    for line in sys.stdin:

        key, val = line.split('\t')
        val = int(val)
        dict[key] = val


        if key == curkey:
            if val > max:
                total = val
            else:
                val = max 
                total = val
        else:
            if curkey is not None:
                sys.stdout.write('{}\t{}\n'.format(curkey, total))

            curkey = key
            total = val
            max = val

    sys.stdout.write("{}\t{}\n".format(curkey, total))
