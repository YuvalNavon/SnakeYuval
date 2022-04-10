def print_hi(name):
    print("Hi", name)

def recursive_distance(num1, num2):
    if (num1==0 and num2==0): return 0;
    if (num1==0 and num2>0): return 1 + recursive_distance(num1,num2//10);
    if (num2==0 and num1>0): return 1 + recursive_distance(num1//10,num2);
    else: return recursive_distance(num1//10,num2//10)

print (recursive_distance(0, 10))


