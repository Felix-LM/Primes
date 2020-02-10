import csv

primeList = []

def isolate(x): #returns the value as a single integer instead of a list of a single string
    return int(x[0])

def init(): #copies contents of csv file to list and formats it to include one integer at each position
    with open('primes.csv', 'r') as r:
        reader = csv.reader(r)

        returnList = list(reader)

        returnList = list(map(isolate, returnList)) #converts list into a list of integers

        return returnList

def graphDifference(val1, val2):
    entry = ''
    maxLength = int((val1 - val2) / 2)
    for i in range(0, maxLength):
        entry += '-'
    print(entry)

primeList = init()

with open('ranked_primes.csv', 'w') as w:
    writer = csv.writer(w)

    for i, n in enumerate(primeList):
        writer.writerow({str(i+1)+': '+str(n)})
        graphDifference(primeList[i], primeList[i-1])
    
    print(str(len(primeList))+' primes found')
