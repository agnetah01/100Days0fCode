p= True
q= False
r=True
#question1(pv -q) and q
a=p or (not q)
b= a and q

print(f"ans to q 1: {b}")

#question2 (p or q) not(-q and -p)
c=p or q #(p or q) true
d=not(q and p)#(-q and -p) true
e=not d #not(-q and -p) false
f=c and e # false
print(f"ans to q 2: {f}")

#question3 (p v q) (p or -q)
g=p or q # true
h=p or(not q) # true
i=g and h # true
print(f"ans to q 3: {i}")


