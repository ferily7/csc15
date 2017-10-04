def gradeExam(answerKey, studentAnswer):
    correct, incorrect = 0, 0
    for i in range(len(answerKey)):
        if answerKey[i] == studentAnswer[i]:
            correct +=1
        else:
            incorrect += 1

    print("Correct =", correct)
    print("Incorrect =", incorrect)

    if (correct/len(answerKey))*100 > 60:
        print("Pass")
    else:
        print("Fail")

def main():

    answerList = ['A','D','E','B','B','C','A','E']
    studentAnswer = ['A','D','E','B','B','C','A','E']
    studentAnswer2 = ['B','E','A','B','B','D','B','A']
    gradeExam(answerList, studentAnswer)
    gradeExam(answerList, studentAnswer2)
    
main()
