#1.i
L = [10, 20, 30, 40, 50, 60, 70, 80]
L.append(200)
L.append(300)
print(L)

#1.ii
L = [10, 20, 30, 40, 50, 60, 70, 80]
L.remove(10)
L.remove(30)
print(L)

#1.iii
L = [10, 20, 30, 40, 50, 60, 70, 80]
L.sort()
print(L)

#1.iv
L = [10, 20, 30, 40, 50, 60, 70, 80]
L.sort(reverse=True)
print(L)

#2.i
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
max_score = max(scores)
print(max_score, scores.index(max_score))

#2.ii
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
min_score = min(scores)
print(min_score, scores.count(min_score))

#2.iii
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
reversed_scores = list(scores[::-1])
print(reversed_scores)

#2.iv
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
num = int(input("Enter a score to check: "))
if num in scores:
    print(scores.index(num))
else:
    print("Not present")

#3.i
import random
numbers = [random.randint(100, 900) for _ in range(100)]
odds = []
evens = []
primes = []
for num in numbers:
    if num % 2 != 0:
        odds.append(num)
    else:
        evens.append(num)
    is_prime = True
    if num < 2:
        is_prime = False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print("Odd numbers:", odds)
print("Even numbers:", evens)
print("Prime numbers:", primes)

#4.i
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
print(A.union(B))

#4.ii
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
print(A.intersection(B))

#4.iii
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
print(A.symmetric_difference(B))

#4.iv
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
print(A.issubset(B))
print(B.issuperset(A))

#4.v
A = {34, 56, 78, 90}
X = int(input("Enter a score to remove from A: "))
if X in A:
    A.remove(X)
    print(A)
else:
    print("Not present in A")

#5
locations = {"name" : "kelly", "age": 25,"salary": 8000, "city": "New York"}
locations["location"] = locations.pop["city"]
print(locations)

