from flask import Flask
import json
import random
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


class Questions:
    """

    """
    def __init__(self):
        self.questions = self.get_questions()

    @staticmethod
    def get_questions():
        qs = json.load(open("questions.json", 'r'))
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
        ans = input(q['question'])
        return ans

class InterviewQuestions():
    

if __name__ == '__main__':
    ###Section 1 get input data from the user
    q = Questions
    print(q.Questions)
    ans = q.ask_question()
    print(ans)

    ##Section 2, show questions to the user for them to choose from, retain selections.


    ##Section 3, output to the user a PDF to interview the person with.
