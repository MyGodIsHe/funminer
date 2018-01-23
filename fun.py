#!/usr/bin/env python

import sys
import string
import itertools
import hashlib
import random
import binascii
import optparse
import multiprocessing
import time


SYNC_INTERVAL = 0.1


def to_str(data):
    return data.decode('utf-8')


def to_bytes(data):
    return data.encode('utf-8')


def alph_iter(alph, start=1):
    n = start
    itr = itertools.product(alph, repeat=n)
    while True:
        value = next(itr, None)
        if value is None:
            n += 1
            itr = itertools.product(alph, repeat=n)
        else:
            yield b''.join(value)


def mine(nonce_iter, words, start, step, cmp):
    last_sync = time.time() - start * SYNC_INTERVAL
    nonce_iter = itertools.islice(nonce_iter, start, None, step)
    for nonce in nonce_iter:
        if time.time() - last_sync > SYNC_INTERVAL * step:
            last_sync = time.time()
            sys.stdout.write('\r{} '.format(to_str(nonce)))
            sys.stdout.flush()
        h = hashlib.sha256(nonce).digest()
        for word in words:
            if cmp(h, word):
                sys.stdout.write('\r{} => {} | {}\n'.format(
                    to_str(nonce),
                    to_str(word),
                    to_str(binascii.hexlify(h)),
                ))
                sys.stdout.flush()


def main():
    usage = "Usage: %prog [OPTIONS] WORDS"
    parser = optparse.OptionParser(usage)
    parser.add_option("-s", "--start", dest="start",
                      help="start from this nonce")
    parser.add_option("-a", "--alph", dest="alph",
                      help="alphabet")
    parser.add_option("-c", "--cmp", dest="cmp",
                      help="method of comparison", choices=('startswith', 'find'),
                      default='startswith')


    options, args = parser.parse_args()

    if len(args) < 1:
        parser.error("incorrect number of arguments")

    if options.alph:
        options.alph = [to_bytes(c) for c in options.alph]
    else:
        options.alph = [to_bytes(c) for c in (string.ascii_letters + string.digits)]
        random.shuffle(options.alph)

    print("Alphabet:", to_str(b''.join(options.alph)))

    if options.start:
        options.start = to_bytes(options.start)
        nonce_iter = alph_iter(options.alph, len(options.start))
        last_sync = time.time()
        for nonce in nonce_iter:
            if time.time() - last_sync > SYNC_INTERVAL:
                last_sync = time.time()
                sys.stdout.write('\r{} '.format(to_str(nonce)))
                sys.stdout.flush()
            if nonce == options.start:
                break
    else:
        nonce_iter = alph_iter(options.alph)

    options.cmp = {
        'startswith': lambda h, word: h.startswith(word),
        'find': lambda h, word: h.find(word) != -1,
    }[options.cmp]

    words = tuple([to_bytes(w) for w in args])
    p_count = multiprocessing.cpu_count() + 1
    ps = []
    for start in range(p_count):
        p = multiprocessing.Process(target=mine,
                                args=(nonce_iter,
                                      words,
                                      start,
                                      p_count,
                                      options.cmp,
                                      )
                                )
        p.start()
        ps.append(p)
    return ps


if __name__ == '__main__':
    ps = []
    try:
        ps = main()
        for p in ps:
            p.join()
    except KeyboardInterrupt:
        for p in ps:
            p.terminate()
