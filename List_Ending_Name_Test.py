names = ["geetha", "sudha", "radha", "mani", "vaani", "raani", "ramu", "somu", "sesu"]

a = []
b = []
c = []


for i in names:
    if i.endswith("a"):
        a.append(i)
      
    if i.endswith("i"):
        b.append(i)
        
    if i.endswith("u"):
        c.append(i)
        
print (a)
print (b)
print (c)