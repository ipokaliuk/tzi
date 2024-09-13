def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_phi(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count

numbers = [210, 80, 164, 346, 184]
results = {num: euler_phi(num) for num in numbers}

for num, phi in results.items():
    print(f"Функція Ейлера для {num} = {phi}")
