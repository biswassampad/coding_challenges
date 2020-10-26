import random
import operator


def main(n):
    print("Welcome to the quiz \nYou should answer floats upto 2 decimals")
    score = 0 
    for i in range(n):
        is_correct ,answer = question(i)
        if is_correct:
            score += 1
            print("Congratualtions, Your answer is correct")
        else:
            print(f'Incorrect Answer : {answer}')
    print(f'Total Score :{score}')

def question(n):

    answer = generating_question()
    user_answer = float(input('Your answer : '))
    return user_answer == answer,answer

def generating_question():
    operators   =   {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv,
        '//':operator.floordiv,
        '%':operator.mod
    }

    nums = [i for i in range(10)]
    _1,_2 = nums[random.randint(0,9)],nums[random.randint(0,9)]
    symbol = list(operators.keys())[random.randint(0,5)]
    answer = round(operators.get(symbol)(_1,_2),2)
    print(f'{_1} {symbol} {_2} ?')
    return answer


if __name__ =="__main__":
    number_of_questions = int(input("Enter the number of questions you want to answer : "))
    main(number_of_questions)