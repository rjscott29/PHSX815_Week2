#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np

# import our Random class from python/Random.py file
sys.path.append(".")
from Random import Random

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -seed [number]      change seed")
        print ("   -prob [number]      name of file for H1 data")
        print ("   -Ntoss [number]     number of tosses in Nexp")
        print ("   -Nexp [number]      number of experiments for Ntoss")
        print ("   -output [text]      name of file for output data")
        print ("   -b                  run Bernoulli (default)")
        print ("   -e                  run Exponential")
        print ("   -d                  run Diceroll")
        sys.exit(1)

    # default seed
    seed = 5555

    # default single coin-toss probability for "1"
    prob = 0.5

    # default number of coin tosses (per experiment)
    Ntoss = 1

    # default number of experiments
    Nexp = 1
    
    # default number of sides
    sides = 20

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-prob' in sys.argv:
        p = sys.argv.index('-prob')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            prob = ptemp
    if '-Ntoss' in sys.argv:
        p = sys.argv.index('-Ntoss')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Ntoss = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-sides' in sys.argv:
        p = sys.argv.index('-sides')
        stemp = int(sys.argv[p+1])
        if stemp > 0 and stemp % 1 == 0:
            sides = stemp
    # assigns distribution from sys.argv
    Bern = '-b' in sys.argv
    Exp = '-e' in sys.argv
    Dice = '-d' in sys.argv
    # default distribution
    Bern = not (Exp or Dice)
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True



    # class instance of our Random class using seed
    random = Random(seed)

    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        if Bern:
            for e in range(0,Nexp):
                for t in range(0,Ntoss):
                    outfile.write(str(random.Bernoulli(prob))+" ")
                outfile.write(" \n")
        if Exp:
            for e in range(0,Nexp):
                for t in range(0,Ntoss):
                    outfile.write(str(random.Exponential())+" ")
                outfile.write(" \n")
        if Dice:
            for e in range(0,Nexp):
                for t in range(0,Ntoss):
                    outfile.write(str(random.Diceroll(sides))+" ")
                outfile.write(" \n")
        outfile.close()
    else:
        if Bern:
            print("---Bernoulli---\n")
            for e in range(0,Nexp):
                for t in range(0,Ntoss):
                    print(str(random.Bernoulli(prob))+" ")
                print(" \n")
        if Exp:
            print("---Exponential---\n")
            for e in range(0,Nexp):
                for t in range(0,Ntoss):
                    print(str(random.Exponential())+" ")
                print(" \n")
        if Dice:
            print("---Diceroll---\n")
            for e in range(0,Nexp):
                for t in range(0,Ntoss):
                    print(str(random.Diceroll(sides))+" ")
                print(" \n") 
