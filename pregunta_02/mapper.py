#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
    campo = row.split(',')
    prop = campo[3]
    mont = campo[4]

    sys.stdout.write(f'{mont}\t{prop}\n')
