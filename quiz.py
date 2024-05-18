quiz = {
    "question1": {
        "question":"what is the capital of India?",
        "answer": "New Delhi"
    },
    "question2": {
        "question": "What is the capital of Germany",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of France",
        "answer": "Paris"
    },
    "question4": {
        "question": "What is the capital of Spain",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Austria",
        "answer": "Vienna"
    },

}

score = 0
for key,value in quiz.items():
    print(value['question'])
    answer = input("answer?")

    if answer.lower() == value['answer'].lower():
        print('correct')
        score = score+1
        print("Yours score is: " +str(score))
    else:
        print("Wrong!")
        print("The answer is : " +value['answer'])
        print("Your score is: "+ str(score))
print("You got "+ str(score)+ "out of 7 questions correctly")
print("Your percentage is " + str(score/7 * 100) + "%")