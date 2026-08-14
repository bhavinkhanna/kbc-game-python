questions=[ 
    ["What is the capital of India?", "New Delhi", "Mumbai", "Kolkata", "Chennai", 1],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Who is known as the Father of the Indian Constitution?", "Mahatma Gandhi", "Jawaharlal Nehru", "B. R. Ambedkar", "Sardar Patel", 3],
    ["How many continents are there in the world?", "5", "6", "7", "8", 3],
    ["Which is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", 3],
    ["What is the chemical symbol of Gold?", "Ag", "Au", "Fe", "Go", 2],
    ["Who wrote the Indian National Anthem?", "Bankim Chandra Chattopadhyay", "Rabindranath Tagore", "Sarojini Naidu", "Subhash Chandra Bose", 2],
    ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],
    ["How many players are there in a cricket team?", "9", "10", "11", "12", 3],
    ["Which programming language is known for the statement 'print(\"Hello, World!\")'?", "C", "Java", "Python", "C++", 3]
]
levels=[1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for Rs {levels[i]}: {question[0]}\n")
    print(f"1. {question [1]}")
    print(f"2. {question [2]}")
    print(f"3. {question [3]}")
    print(f"4. {question [4]}")
    answer=int(input("Enter your answer (1-4) or press 0 to quit: "))
    if answer==0:
        print(f"You have chosen to quit. You have won Rs {levels[i-1]}")
        break
    money=0
    if answer==question[5]:
        print(f"Correct! You have won rs {levels[i]}\n")
        money=levels[i]

        

        if i==4:
            print("Congratulations! You have won Rs 10,000")
        elif i==9:
            print("Congratulations! You have won Rs 3,20,000")
        elif i==14:
            print("Congratulations! You have won Rs 1,00,00,000")  
  
    else:
        print(f"Wrong answer! The correct answer is option {question[5]}.")
        break          

print(f"Your take home money is Rs {money}")    