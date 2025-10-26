# 100 Days of code by Angela Yu
# Day 12 - Challenge 1 - Prime number checker

def is_prime(num: int) -> bool:
    is_prime_num = True
    i = 2

    while i < num:
        if num % i == 0:
            is_prime_num = False
            break
        else:
            is_prime_num = True

        i += 1

    return is_prime_num

def input_num() -> int:
    try:
        num_str = input("Type a number: ")
        num_int = int(num_str)
        return num_int
    except ValueError:
        print("Value Error")
        return 0

def main():
    num = 0
    print("Test if a number is a prime number.")
    
    while num == 0:
        num = input_num()

    if is_prime(num):
        print(f"{num} is a prime number!")
    else:
        print(f"{num} is not a prime number!")
    
if __name__ == "__main__":
    main()
