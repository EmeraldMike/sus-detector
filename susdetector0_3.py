#imports
#Made by Emerald Mike
import sys
import time
import random
from colorama import init
from colorama import Fore, Back, Style
#code (;
init()
print(Fore.RED + 'Open SUS Program opensus.wtf')
time.sleep(1)
print('SUS DETECTOR 0.3')
time.sleep(1)
foofoo = 0;
while foofoo < 101:
    print('LAUNCHING SUS DETECTORS ' + str(foofoo) + '%')
    time.sleep(0.1)
    foofoo = foofoo + 1;
foo = 1;
while foo == 1:
    man = input("who do you think is sus: ")
    if man == "quit":
        foofoobar = 0;
        while foofoobar < 101:
            print('DEACTIVATING SUS DETECTORS ' + str(foofoobar) + '%')
            time.sleep(0.05)
            foofoobar = foofoobar + 1;
        sys.exit()
    else:
        print('Scanning ' + man + ' for sus . . .')
        foobar = 0;
        while foobar < 101:
            print('Scanning ' + man + ' for sus ' + str(foobar) + '%')
            time.sleep(0.01)
            foobar = foobar + 1;
        sus = random.randint(0,100);
        print(man + ' is ' + str(sus) + '% sus')