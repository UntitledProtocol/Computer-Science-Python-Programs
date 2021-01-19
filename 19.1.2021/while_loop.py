import random as random_lib
random = random_lib.randint

class question():
    def __init__(self):
        self.n0 = random(1, 100)
        self.n1 = random(1, 100)
    
    def is_ans(self, num):
        if num == self.n0 + self.n1:
            return True

def main():
    while True:
        my_question = question()
        print(f'{my_question.n0} + {my_question.n1} = ?')
        ans = int(input("> "))

        if my_question.is_ans(ans):
            print("You got it right.")
            return
        else:
            print("Can't do simple addition? You suck. \n")
main()
    