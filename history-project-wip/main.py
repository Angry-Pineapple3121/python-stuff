from questions import quiz
from rich import print
import time

# Quiz Configuration #
SHOW_ANSWER_KEY = False
ALLOW_SKIPS = False
QUIZ_ATTEMPTS = 3
MAX_BAR_LENGTH = 60
END_WAIT_TIME = 3

def check_ans(question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"\n[bright_black][ [bright_green] ✅ [/bright_green] ] [/bright_black][bright_green]Your answer was correct![/bright_green] \n[bold bright_yellow] ⭐ Total Score: {score + 1} ⭐[/bold bright_yellow]\n")
        return True
    else:
        print(f"\n[bright_black][  [bold bright_red]X[/bold bright_red]  ] [/bright_black][bright_red]Incorrect answer. You have {attempts - 1} attempts remaining.[/bright_red]")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])

def progressBar():
    for done in range(MAX_BAR_LENGTH):
        time.sleep(0.01)

        undone = MAX_BAR_LENGTH - 1 - done
        proc = (100 * done) // (MAX_BAR_LENGTH - 1)
        print(f"\rProgress: [{('█' * done) + ('░' * undone)}] ({proc}.0%)", end='\r')

    print("\n[bright_green]Finished loading your questionnaire![/bright_green]")

if __name__ == "__main__":
    while True:
        print('\n[bright_black][  [bold bright_cyan]#[/bold bright_cyan]  ] [/bright_black][bright_cyan]Setting up your questionnaire session...[/bright_cyan]')
        progressBar()
        score = 0
        for question in quiz:
            attempts = QUIZ_ATTEMPTS
            while attempts > 0:
                print(quiz[question]['question'])
                if ALLOW_SKIPS == True:
                    answer = input("\n[  !  ] Skips are enabled for this questionnaire! Type 'skip' to skip a question.\n[  >  ] Enter your answer # here --> ")
                answer = input("\n[  >  ] Enter your answer here --> ")
                if ALLOW_SKIPS == True:
                    if answer == "skip":
                        break
                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1

        break

print('[bold bright_cyan] Finishing up your session, please wait...[/bold bright_cyan]')
time.sleep(END_WAIT_TIME)

print(f"""[bright_green]
  +-------------------------------------------------+
  | Indianapolis Super Bowl Questionnaire Finished! |
  |                                                 |
  |         Your Total Score: {score} Points              |
  |              Thanks for playing!                |
  +-------------------------------------------------+
  [/bright_green]
""")
if SHOW_ANSWER_KEY == True:
    print("Answer Key:\n")
    print_dictionary()