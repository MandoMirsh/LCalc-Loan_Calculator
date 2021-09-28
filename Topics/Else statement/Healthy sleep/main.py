low_bound = int(input())
up_bound = int(input())
slept = int(input())
print("Deficiency" if slept < low_bound else ("Excess" if slept > up_bound else "Normal"))
