import os
import sys
import zlib
from chain import Chain

def main():
    fname = sys.argv[1]
    chain = Chain()
    with open(fname, "r") as f:
        print "Reading " + fname
        chain.record_string(f.read())

    with open("definitions/" + sys.argv[2], "w") as fout:
        print "Writing " + sys.argv[2]
        fout.write(zlib.compress(chain.serialize()))
    

if __name__ == "__main__":
    main()
