#Random Number
import random
def generate_random_number(low,high):
    return random.randint(low,high)
def check_guess(secret_number,guess):
    if guess<secret_number:
        return "Too Low"
    elif guess>secret_number:
        return "Too high"
    else:
        return "Correct!"
    
def main():
    low=1
    high=100
    secret_number=generate_random_number(low,high)
    print("Welcome to the Number Guessing Game!")
    print(f"Guess the number betwenn {low} and {high}.")

    guesses=0
    while True:
        guess=int(input("Enter your guess:"))
        result=check_guess(secret_number,guess)
        print(result)
        guesses+=1
        if result=="Correct!":
            print(f"You guessed the number in {guesses} guesses")
if __name__=="__main__":
    main()