#Excercise_4
#Quiz

def quiz():
    questions_quiz = [
        {"question": "1.What is the capital of France?", "answer": "Paris"},
        {"question": "2.What is the capital of Ukraine?", "answer": "Kyiv"},
        {"question": "3.What is the capital of Bosnia?", "answer": "Sarajevo"},
        {"question": "4.What is the capital of Croatia?", "answer": "Zagreb"},
        {"question": "5.What is the capital of Malta?", "answer": "Valetta"},
        {"question": "6.What is the capital of Slovenia?", "answer": "Ljubljana"},
        {"question": "7. What is the capital of Andora?", "answer": "Andorra la Vella"}, #Question and Answer Dictionary 
        {"question": "8. What is the capital of Greece?", "answer": "Athens"},
        {"question": "9. What is the capital of Poland?", "answer": "Warsaw"},
        {"question": "10. What is the capital of Montenegro?", "answer": "Podgorica"},
        
       ]
    
    for q in questions_quiz:
        user_answer = input(f"{q['question']} ").strip() #Removes whitespace
        
        if user_answer.lower() == q['answer'].lower(): #Disregards capitalization
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {q['answer']}.")#Code to give correct answer when wrong answer is entered

if __name__ == "__main__":
    quiz()
