#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

from curses import keyname
import sys

if __name__ == '__main__':

    Keyname = None
    ttl = 0


    for line in sys.stdin:

        key, val = line.split('\t')
        val = int(val)

        if key == Keyname:
            ttl += val
        else:
            if Keyname is not None:
                
                sys.stdout.write('{},{}\n'.format(Keyname, ttl))

            Keyname = key
            ttl = val     


    sys.stdout.write('{},{}\n'.format(Keyname, ttl))