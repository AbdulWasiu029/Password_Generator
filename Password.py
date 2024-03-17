import random
import string
def main():
    pass_length = int(input("Enter Length of Password: "))
    password = generate_pass(pass_length)
    print("The Password Can be: ",password)
def generate_pass(pass_length):
    password_m = string.ascii_letters + string.digits + string.punctuation
    for i in range(pass_length):
        password = "".join(random.choice(password_m)for i in range(pass_length))
    return password
if __name__ == "__main__":
    main()