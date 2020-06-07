def addition(x,y):
    z=x+y
    print('test')
    return(z)
    
#%%
import random    
random.randint(16,272)


# Simple addition %%
print(10+1)    


#%%
type(5)
print(3.0-1)

# Bindings %%
usa_gold = 46
uk_gold = 27
romania_gold = 1

total_gold = usa_gold + uk_gold + romania_gold
print(total_gold)

romania_gold += 1
print(total_gold)


# Branching and Iteration %%
hi = "hello there"
name = "ana"
greet = hi + name

print(greet)

greeting = hi + " " + name
print(greeting)

silly = hi + (" " + name)*3
print(silly)

#%%
x = 1
print(x)

x_str = str(x)
print("my fave number is", x, ".", "x=", x)
print("my fave number is", x_str + "." + "x=" + x_str)
print("my fave number is" + x_str + "." + "x=" + x_str)

# Input Casting %%
text = input("Type anything... ")
print(5*text)
num = int(input("Type a number... "))
print(5*num)

# While Loop - Using counter%%
n = input("You are in the Forest\n************")
while n == "right" or n == "Right":
    n = input("You are in the Forest\n************")
print("\nYou got out of the Lost Forest! \n\o/")


# For Loop - Using counter%%
mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2):
    mysum += i
print(mysum)

# Strings %%
once = "umbr"
repeat = "ella"
u = once + (repeat+" ")*4

# Strings Manipulation %%
s = "abcdefgiu"
len(s)

for char in s:
    if char == 'i' or char == 'u':
        print("There is  an i or u")


cube = 9
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)
        
# Write and Call/Invoke a function %%
def is_even (i):
    """
    Input: i, a postive int
    Returns True if i is even, otherwise False
    """
    print("inside is_even")
    return i%2 == 0

is_even(3)


def f (x):
    x = x + 1
    print('in f(x): x =', x)
    
x = 3
z = f (x)



print("All numbers between 0 and 20: even or not")

for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")
        

    

# Tuples %%
def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t [1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

test = ((1,"a"),(2,"b"),
        (1,"a"),(7,"b"))
(a, b, c) = get_data(test)
print("a:",a,"b:",b,"c:",c)

               
tswift = ((2014,"Katy"), 
          (2014,"Harry"), 
          (2012,"Jake"), 
          (2010,"Taylor"), 
          (2008,"Joe"))
(min_year, max_year, num_people) = get_data(tswift)
print("From", min_year, "to", max_year, \
      "Taylor  Swift wrote songs about", num_people, "peope!")




















