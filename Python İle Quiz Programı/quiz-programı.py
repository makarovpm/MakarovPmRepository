class Question:
    def __init__(self,text,choices,answer):
        self.text= text
        self.choices= choices
        self.answer= answer
    def checkAnswer(self,answer):
        return self.answer == answer



class Quiz():
    def __init__(self,questios):
        self.questions = questios
        self.score= 0
        self.questionsIndex= 0
    def getQuestions(self):
        return self.questions[self.questionsIndex]

    def displayQuestion(self):
        question = self.getQuestions()
        print(f"Soru {self.questionsIndex + 1}: {question.text}")
        for q in question.choices:
            print('-'+ q)
        answer = input("Cevabınızı Giriniz: ")
        self.guess(answer)
        self.loadQuestion()
    def guess(self,answer):
        question = self.getQuestions()

        if question.checkAnswer(answer):
            self.score +=1
        self.questionsIndex += 1
    def showScore(self):
        print("Skor :",self.score)

    def displayProgress(self):
        totalQuestion =  len(self.questions)
        questionNumber = self.questionsIndex + 1
        if questionNumber > totalQuestion:
            print("Quiz Bitmiştir.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,'*'))

    def loadQuestion(self):
        if len(self.questions) == self.questionsIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
q1 = Question("En iyi Programlama Dili Hangisidir ?", ["Python","C#","C++","Java"], ("python"))
q2 = Question("En Popüler Programlama Dili Hangisidir ?", ["C","C#","C++","Python"], ("python"))
q3 = Question("En iyi Kazandıran Progamlama Dili Hangisidir ?", ["JavaScript","C#","C++","Python"], ("python"))
questions = [q1,q2,q3]

quiz = Quiz(questions)
question = quiz.getQuestions
quiz.loadQuestion()
