from sympy import symbols, Eq, solve
from math import *

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = symbols('a b c d e f g h i j k l m n o p')

symps = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]

vals = []

varz = []

print("Please type in all variables. End with 'done'.")
i = 0
while True:
    if i > len(symps):
        print("Reached max var length of", len(symps))
        break
    inp = input("var: ")
    if inp == "done":
        break
    else:
        varz.append(str(inp))
    i += 1



print("Please enter all values. If unknown, type '?'.")
for var in varz:
    inp = input(var + ": ")
    if inp == "?":
        vals.append(None)
    else:
        try:
            inp = int(inp)
            vals.append(inp)
        except:
            print("Failed: try to input a number please!")

print("Please give your equation in the form where z=x+y is x+y,z")
strEq = str(input())
i = 0
for var in varz:
    strEq = strEq.replace(var, str(symps[i]))
    i += 1
func = eval("Eq(" + strEq + ")")

unknown = None
for i in range(len(varz)):
    if vals[i] == None:
        unknown = symps[i]
    else:
        func = func.subs(symps[i], vals[i])

assert unknown is not None, "No unknown"

answer = solve(func, unknown)

if type(answer) == list:
    if len(answer) > 1:
        answer = answer[len(answer) - 1]
    else:
        answer = answer[0]

print("Answer:", eval(str(answer)))
