import random

def fix_me(num1, num2):
    return num1 + num2

# Yes this is overly cutesy. I love cinnamaroll man

if __name__ == "__main__":
    print("\n◦∘●∘◦❀◦∘●∘◦❀◦∘●∘◦❀◦∘●∘◦❀◦∘●∘◦")
    print("--! Running calculations !--\n")

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    print(f"Adding {num1} and {num2} together to get...")
    print(fix_me(num1, num2))
