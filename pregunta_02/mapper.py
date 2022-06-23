#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    for row in sys.stdin:
        campo = row.split(',')
        c2 = campo[3]
        c3 = campo[4]

        sys.stdout.write(f"{c2}\t{c3}\n")
