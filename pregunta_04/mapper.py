#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    for row in sys.stdin:
        data= row.split('\t')

        sys.stdout.write(f'{row}\n')