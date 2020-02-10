import csv

primeList = []
value = 0 #will be checked to see if prime. If it is, it will be added to the csv file and then increased by 1

def isolate(x): #returns the value as a single integer instead of a list of a single string
    return int(x[0])

def init(): #copies contents of csv file to list and formats it to include one integer at each position
    with open('primes.csv', 'r') as r:
        reader = csv.reader(r)

        returnList = list(reader)

        returnList = list(map(isolate, returnList)) #converts list into a list of integers

        return returnList

def isPrime(n): #checks whether input value is prime
    prime = True
    for x in primeList: #finds if value is prime by finding the remainder of it and every integer below it
        if n % x == 0:
            prime = False

    return prime #returns True if prime, False if not

def addPrime(value): #adds prime to csv file and to primeList
    primeList.append(value)

    with open('primes.csv', 'a') as f:
        editor = csv.writer(f)

        editor.writerow({value})

primeList = init()
value = primeList[len(primeList)-1] #sets value to last value on primeList
print('Starting value:', value)


while 1:
    if isPrime(value):
        addPrime(value)
    value += 2
