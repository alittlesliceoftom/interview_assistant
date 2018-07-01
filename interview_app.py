from flask import Flask
import json
import random
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


class Questions():
    """

    """
    def __init__(self):
        self.questions = None

    def get_questions(self, filename='questions.json'):
        qs = json.load(open(filename, 'r'))
        self.questions = qs
        return qs

    def ask_question(self, question=None):
        """
        Ask a question to the user and collect the answer. If questions specified ask that, else ask a random unasked
        question
        :return:
        """
        if not question:
            key = random.choice(tuple(self.questions.keys()))
        else:
            key = question
        print(key)
        q = self.questions[key]
        print(q)
        ans = input(q['Question'])
        return ans


if __name__ == '__main__':
    ###Section 1 get input data from the user
    userQuestions = Questions()
    userQuestions.get_questions()
    print(userQuestions.questions)
    ans = userQuestions.ask_question()
    print(ans)

    ##Section 2, show questions to the user for them to choose from, retain selections.
    interviewQuestions = Questions()
    interviewQuestions.get_questions(filename='interview_questions.json')
    for k, v in interviewQuestions.questions.items():
        print("The questions is: " + v['Question'])
        print("The answer is: " + str(v['Answer']) )
    ##Section 3, output to the user a PDF to interview the person with.
