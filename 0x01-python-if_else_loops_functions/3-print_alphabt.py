#!/usr/bin/python3
for code in range(ord('a'), ord('z') + 1):
    if code == ord('e') or code == ord('q'):
        continue
    print("{:c}".format(code), sep='', end='')
