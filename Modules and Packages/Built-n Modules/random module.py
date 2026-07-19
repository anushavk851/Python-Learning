import random
#random module is used to generate random numbers and make random selections

#(random()--return a random float between 0.0 and 1.0)
print(random.random())           # 0.0 to 1.0

#(randint(a, b)--Returns a random integer between a and b (inclusive))(each time running program we get different output)
print(random.randint(1, 10))     # 1 to 10

#randrange(start, stop, step)--Returns a random number from the specified range
print(random.randrange(1, 20, 2)) # Odd number between 1 and 19

#uniform(a, b)--Returns a random float between a and b
a=int(input("enter a lower value: "))
b=int(input("enter a upper  value: "))
print(random.uniform(a, b))     # Float between 1 and 10

names = ["Anusha", "Anilkumar", "Bindu", "Anusree"]
#choice(sequence)--Returns a random element from a sequence
print(random.choice(names))   # One random name

#choices(sequence, k=n)--Returns n random elements (with replacement) but wont be unique(may return duplicate values)
ran_choices=int(input("enter number of random elements: "))
print(random.choices(names, k=ran_choices)) 

#sample(sequence, k)--Returns k unique random elements
unique=int(input("enter number of unique choices: "))
print(random.sample(names, unique))  

#shuffle(sequence)--Shuffles a list in place
random.shuffle(names)
print(names)

#seed(value)--Initializes the random number generator for reproducible results(that is result will be same always in all run)
seed_no=int(input("enter a start point: "))
random.seed(seed_no) #here 10 is a starting point (eg when seed_no is 10 it could mean start from page 10) 
print(random.randint(1, 100))

# getrandbits(k)--Returns an integer with k random bits(if bit_no is k-Total possible values is 2^k,so ouput will be any value between 0-2^k)
bit_no=int(input("enter a number of bits: "))
print(random.getrandbits(bit_no))   

#if bit_no is 1 ,output value range from 0 to 1
#if 2-output value range (0-3)
#if 3- output value range(0-7)
#if 4- output value range(0-15)......

#if k-Total possible values is 2^k
