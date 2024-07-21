### This application demonstrates prime number checker ###
### Author: Sandro Zakaidze
### Version pro


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n ):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Please enter a natural number: "))

    if is_prime(n):
        print("The number is a prime number.")
    else:
        print("The number is not a prime number.")


if __name__ == "__main__":
    main()
