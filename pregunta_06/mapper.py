#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    for row in sys.stdin:
        campo = row.strip().split('   ')
        ltr = campo[0]
        num = campo[2]

        sys.stdout.write(f'{ltr}\t{num}\n')