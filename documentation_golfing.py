"""
Lambda is a function that can be used to create a function without a name ex : lambda x: x+1 = def f(x): return x+1
regex is a function that can be used to search for a pattern in a string ex : re.search(r"\d",s) = search for a digit in the string s
map is a function that can be used to apply a function to all the elements of a list ex : map(lambda x:x+1,[1,2,3]) = [2,3,4]
for condition in [] can be use to fill a list with the condition ex : [i for i in range(10) if i%2==0] = [0,2,4,6,8]
filter is a function that can be used to filter a list  ex : filter(lambda x:x%2==0,[1,2,3]) = [2]
reduce is a function that can be used to reduce a list to a single value  ex : reduce(lambda x,y:x+y,[1,2,3]) = 6
zip() is a function that can be used to merge two lists ex : zip([1,2,3],[4,5,6]) = [(1,4),(2,5),(3,6)]
ternary condition is a trick to write a condition in one line ex : "palindrome" if w==w[::-1] else "not palindrome"
join is a function that can be used to join a list of strings ex : "-".join(["a","b","c"]) = "a-b-c"
any  is a function that can be used to check if one of the conditions is true ex : any([1==1,2==3]) = True
translate is a function that can be used to replace a character in a string ex : "abc".translate(str.maketrans("abc","def")) = "def"
maketrans is a function that can be used to create a translation table ex : str.maketrans("abc","def") = {97:100,98:101,99:102}
"""


###lambda exemple:
f=lambda:sum(map(int,input().split()))
print(-f()+f())

#---------------------------------------------------------------------------------------------#

print(sum(filter(lambda n:n%3*n%5*n%7==0,range(int(input())))))

#---------------------------------------------------------------------------------------------#

f=lambda:int(input())
print(min(min((f()+f(),"A"),(f(),"B")),(f(),"no delivery"))[1])

#---------------------------------------------------------------------------------------------#

f= lambda x, y: x * y
print(f(2, 3))

#---------------------------------------------------------------------------------------------#

###regex exemple:
import re
t=re.findall("1+|0+","".join([format(ord(h),"07b")for h in input()]))
#nbr="10001110"
#t = ["1", "000", "111", "0"]

#---------------------------------------------------------------------------------------------#

s = input().lower()
print(
    [["not palindrome", "palindrome"][s == s[::-1]], "invalid"][
        bool(re.search(r"\d", s)) 
    ]
)
#search for a digit in the string s
#re.search(r"\d","abc") = None
#re.search(r"\d","abc1") = <re.Match object; span=(3, 4), match='1'>

#---------------------------------------------------------------------------------------------#

###map exemple:

s = [*map(int, [*open(0)][1].split())]
print(max(s) + min(s))

#---------------------------------------------------------------------------------------------#

print(round(sum(map(ord, s)) / len(s), 1))

#---------------------------------------------------------------------------------------------#

print(" ".join(map(str,reversed(sorted(int(input()) for _ in range(int(input())))))))

#---------------------------------------------------------------------------------------------#

print(sum(map(str.isupper,input())))

#---------------------------------------------------------------------------------------------#

for i in range(int(input())):
    s,t=list(map(int,input().split()))
    print(int((s*(t*60)/100)))

#---------------------------------------------------------------------------------------------#

###List comprehension exemple:

x=[int(input())for _ in range(4)]
print(max(x)-min(x))

#---------------------------------------------------------------------------------------------#

l = [int(i) for i in input().split()]
print(sum(l) / len(l))

#---------------------------------------------------------------------------------------------#

###filter exemple:

print(sum(filter(lambda x:x%2==0,map(int,input().split()))))

#---------------------------------------------------------------------------------------------#

print(len(list(filter(str.isupper,input()))))

#---------------------------------------------------------------------------------------------#

print(sum(filter(lambda n:n%3*n%5*n%7==0,range(int(input())))))

#---------------------------------------------------------------------------------------------#

###reduce exemple:

from functools import reduce
print(reduce(lambda x,y:x+y,map(int,input().split())))

#---------------------------------------------------------------------------------------------#

###zip exemple:

s=input()
for a in zip(s,s[::-1]):
    print(*a)
#zip("abc","cba") = [("a","c"),("b","b"),("c","a")]

#---------------------------------------------------------------------------------------------#

###ternary condition exemple:

import time
f=lambda:time.strptime(input(),'%H:%M:%S')
l,r=f(),f()
print("EARLY"if l>r else"DELAYED"if l<r else"ON TIME")

#---------------------------------------------------------------------------------------------#

t=[int(input())for _ in range(4)]
u=t[0]+t[1]
print("A"if u<t[2]and u<=t[3]else"B"if u>t[2]and t[2]<=t[3]else"no delivery")

#---------------------------------------------------------------------------------------------#

n1, n2 = map(int, input().split())
if n1 == 0 and n2 == 0:
    print(0)
n = int(input())

def f(n):
    # ternary condition with 2 conditions
    return n1 if n == 1 else n2 if n == 2 else f(n - 1) + f(n - 2)

#---------------------------------------------------------------------------------------------#

###join exemple:

print("-".join([str(i) for i in range(1,int(input())+1)]))

#---------------------------------------------------------------------------------------------#

print(" ".join([s.capitalize()for s in input().split(' ')]))

#---------------------------------------------------------------------------------------------#

print(" ".join(map(str,reversed(sorted(int(input()) for _ in range(int(input())))))))

#---------------------------------------------------------------------------------------------#

I = input
a = I()
m = I()
w = I()
while w not in m:
    m = "".join(map(lambda x: a[(a.index(x) - 1) % len(a)], m))
print(m)

#---------------------------------------------------------------------------------------------#

###any exemple:

print("".join([i for i in input()if any([i==j for j in"aeiouy"])]))

#---------------------------------------------------------------------------------------------#

print(
    sum(
        1
        for w in input().lower().split()
        if any(w[i] == w[i + 1] for i in range(len(w) - 1))
    )
)
#any : check if one of the conditions is true,
#here we check if one of the letters is the same as the next one

#---------------------------------------------------------------------------------------------#

###translate/maketrans exemple:

print(input().translate(str.maketrans("abc","def")))
#translate is a function that can be used to replace a character in a string
#maketrans is a function that can be used to create a translation table
#ex : str.maketrans("abc","def") = {97:100,98:101,99:102}

#---------------------------------------------------------------------------------------------#

###OTHER TIPS:

#reverse a string:
s="abc"
print(s[::-1]) #cba

#---------------------------------------------------------------------------------------------#

#reverse a list:
l=[1,2,3]
print(l[::-1]) #[3,2,1]

#---------------------------------------------------------------------------------------------#

#get longer string in a list:
l=["abc","def","ghij"]
print(max(l,key=len)) #ghij

#---------------------------------------------------------------------------------------------#

#sort a list of strings by length:
l=["abc","def","ghij"]
print(sorted(l,key=len)) #["abc","def","ghij"]

#---------------------------------------------------------------------------------------------#

#sort a list of strings by length and then alphabetically:
l=["abc","def","ghij"]
print(sorted(l,key=lambda x:(len(x),x))) #["abc","def","ghij"]

#---------------------------------------------------------------------------------------------#

##CONDITIONS:

#classic:
X,Y,A,B,Z,L=map(int,input().split())

if X and Y:
  print(B)
else:
  print(A)

#clubbed:
print([A,B][X and Y])
print([A,B][X&Y])

print([A,B][X<5 and Y<5])
print([A,B][X<5>Y])

print([A,B][X>0 and X<10])
print([A,B][0<X<10])

print([A,B][X>0 and Z>0 and Y<X])
print([A,B][Z>0<X>Y])

#---------------------------------------------------------------------------------------------#

#classic:
"return X==5 and Y==6"

#clubbed:
"return(X,Y)==(5,6)"

#---------------------------------------------------------------------------------------------#

#classic:
print(['much','code','wow'][X])

#clubbed:
print('mcwuoocdwhe'[X::3])

#---------------------------------------------------------------------------------------------#

#classic:
print(', '.join(['A','B']))

#clubbed:
print(*['A','B'],sep=', ')

#---------------------------------------------------------------------------------------------#

#classic:
for a in range(3):
  for b in range(5):
    print(a,b)

#clubbed:
for a in range(3):
 for b in range(5):print(a,b)

#---------------------------------------------------------------------------------------------#

def foo():
   pass
#classic:
for a in range(10):foo()

#clubbed:
for a in[1]*10:foo()

exec("foo();"*10)

#---------------------------------------------------------------------------------------------#

#classic:
for a in range(4):print(a)

#clubbed:
for a in 0,1,2,3:print(a)

#---------------------------------------------------------------------------------------------#

#classic:
import math
x=math.floor(A/B)
x=math.ceil(A/B)

#clubbed:
x=A//B
x=-(-A//B)

#---------------------------------------------------------------------------------------------#

#classic:
A=list(range(10))
B=list('abc')

#clubbed:
*A,=range(10)
*B,='abc'

#---------------------------------------------------------------------------------------------#

#classic:
A,B,C='a','b','c'

#clubbed:
A,B,C='abc'

#---------------------------------------------------------------------------------------------#

#classic:
a,b,c=input(),input(),input()

#clubbed:
i=input;a,b,c=i(),i(),i()

#---------------------------------------------------------------------------------------------#

#LISTS:

#classic:
A,B=4,[] #8 Chars

#clubbed:
A,*B=4, #7 Chars

#---------------------------------------------------------------------------------------------#

#Getting first item
#classic:
A=L[0]

#clubbed:
A,*_=L

#---------------------------------------------------------------------------------------------#

#Getting last item
#classic:
A=L[-1]

#clubbed:
*_,A=L

#---------------------------------------------------------------------------------------------#

#Removing first item
#classic:
L.pop(0)

#clubbed:
L=L[1:]
_,*L=L

#---------------------------------------------------------------------------------------------#

#Removing last item
#classic:
L=L[:-1]

#clubbed:
L.pop()
*L,_=L

#---------------------------------------------------------------------------------------------#

#Appending an item
#classic:
L.append(A)
#clubbed:
L+=[A]

#---------------------------------------------------------------------------------------------#

#Extending a list
#classic:
A.extend(B) 
#clubbed:
A+=B

#---------------------------------------------------------------------------------------------#

#Inserting items into a list
#classic:
L.insert(i,A)
#clubbed:
L[:i]+=A,

#---------------------------------------------------------------------------------------------#

#Reversing a list
#classic:
L=L.reverse()
#clubbed:
L=L[::-1]

#---------------------------------------------------------------------------------------------#

#classic:
L[::-1][A]
#get the Ath item from the end of the list, ex: L=[1,2,3,4,5] A=4 => 2

#clubbed:
L[~A]

#---------------------------------------------------------------------------------------------#

#classic:
A = [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(len(list(A)))

#clubbed:
print(len([*A]))

#---------------------------------------------------------------------------------------------#

#find most common element in a list:
#classic:
A=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7]
for i in A:
  if A.count(i)>A.count(A[0]):
    A[0]=i
print(A[0])

#clubbed:
print(max(set(A),key=A.count))

#---------------------------------------------------------------------------------------------#

#quickly create a list of numbers:
#classic:
A=list(range(10))

#clubbed:
A=[*range(10)]

#---------------------------------------------------------------------------------------------#

#quickly create a list of numbers in reverse order:
#classic:
A=list(range(10))[::-1]

#clubbed:
A=[*range(9,-1,-1)]

#---------------------------------------------------------------------------------------------#

#transpose a matrix:
#classic:
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
print(B)
#ex: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

#clubbed:
print(list(zip(*A)))

#---------------------------------------------------------------------------------------------#