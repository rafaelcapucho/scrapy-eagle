import sys

from time import sleep

# When the dashboard receives a KeyboardInterrupt
# the subprocess also receive a KeyboardInterrupt
# you could catch or not.

try:
    n = 1
    while True:

        print(n)

        n += 1

        #sys.stdout.flush()

        sleep(1)

        if n % 20 == 0: break

    print(' ')

except (KeyboardInterrupt, SystemExit):
    print('fechou')