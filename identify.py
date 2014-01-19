from chain import *
import sys
import os

def load_definitions(directory):
    files = os.listdir(directory)
    defs = {}
    for fname in files:
        f = open(os.path.join(directory, fname), 'r')
        c = Chain.deserialize(f.read())
        f.close()
        
        defs[fname] = c
    return defs

def main():
    defs = load_definitions("references")
    fname = sys.argv[1]
    data = None
    with open(fname) as f:
        data = f.read()

    results = {}
    for name, chain in defs.iteritems():
        results[name] = chain.compare(data)
    # Sort by the value, not the key.
    sorted_results = [(v,k) for k, v in results.iteritems()]
    sorted_results.sort(reverse=True)
    for value, name in sorted_results:
        print name + ": " + str(value)


if __name__ == "__main__":
    main()
