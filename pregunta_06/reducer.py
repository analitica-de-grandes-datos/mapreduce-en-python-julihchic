#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    Keyname = None
    max = 0
    min = 0

    for line in sys.stdin:

        key, val = line.split('\t')
        val = float(val)


        if key == Keyname:
            if val > max:
                max = val
            else:
                val = max
            
            if val < min:
                min = val
            else:
                val = min 
                                 
        else:
            if Keyname is not None:
                sys.stdout.write('{}\t{}\t{}\n'.format(Keyname, max, min))

                Keyname = key
                max = val
                min = val

    sys.stdout.write("{}\t{}\t{}\n".format(Keyname, max, min))