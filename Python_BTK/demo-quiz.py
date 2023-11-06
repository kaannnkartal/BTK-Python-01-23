
# Question

class Question:

    def __init__(self,text,choices,answer) -> None:
        pass
        self.text = text
        self.choices = choices
        self.answer = answer
        
    def checkAnswer(self,answer):
        return self.answer == answer





# Quiz


class Quiz:

    def __init__(self,questions) -> None:
        pass
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex +1 } : {question.text}")

        for q in question.choices:
            print("-" + q)


        answer = input("Cevap : ")
        
        self.guess(answer)
        self.loadQuestion()

    
    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex +=1


    def loadQuestion(self):

        if len(self.questions) == self.questionIndex:
            self.showScore()

        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("Score : ", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        if questionNumber > totalQuestion:
            print("Quiz bitti")

        else:
            pass




q1 = Question("En iyi programlama dili hangisidir?", ["C#","Python","JS","java"],"Python")
q2 = Question("En popüler programlama dili hangisidir?", ["Python","JS","C#","java"],"Python")
q3 = Question("En çok kazandıran programlama dili hangisidir?", ["C#","JS","java","Python"],"Python")

questions = [q1,q2,q3]

quiz = Quiz(questions)

##question = quiz.questions[quiz.questionIndex]

#question = quiz.getQuestion()

#print(question.text)
quiz.displayQuestion()
##print(q1.checkAnswer("Python"))
##print(q2.checkAnswer("C#"))