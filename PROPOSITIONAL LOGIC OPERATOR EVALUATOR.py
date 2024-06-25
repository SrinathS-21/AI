P = input("Enter truth value for P (True or False): ").strip()
Q = input("Enter truth value for Q (True or False): ").strip()
s = P and Q
f = P or Q
g = not P
print(f"P AND Q = {s}")
print(f"P OR Q = {f}")
print(f"NOT P = {g}")



#if above code doesnt work properly

P = input("Enter truth value for P (True or False): ").strip().capitalize()
Q = input("Enter truth value for Q (True or False): ").strip().capitalize()

# Convert input strings to Boolean values
P = True if P == "True" else False
Q = True if Q == "True" else False

# Perform logical operations
s = P and Q
f = P or Q
g = not P

# Print results
print(f"P AND Q = {s}")
print(f"P OR Q = {f}")
print(f"NOT P = {g}")
