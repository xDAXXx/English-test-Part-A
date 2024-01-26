import time

# Inicjalizacja zmiennych
correct_answers = 0
incorrect_answers = 0
total_questions = 4 

print("To jest test z języka angielskiego Part A.\
 \nPodczas wpisywania odpowiedzi wpisuj literę np. 'c' albo słowo np. 'My'.\
 \nPo prawidłowej odpowiedzi pojawi się słowo 'Correct', a przy błędnej 'Incorrect'." )
print ("Powodzenia!\n")


time.sleep(2)
    
print("1. _____ name is Robert.")
print ("a) Me b) I c) My")
A =input ()
if A == "My" or A == "c":
    print("Correct!\n")
    correct_answers += 1
else:
    print("Incorrect.")
    incorrect_answers += 1


print("2. They _____ from Spain.")
print ("a) is b) are c) do")
A =input ()
if A == "are" or A == "b":
    print("Correct!\n")
    correct_answers += 1
else:
    print("Incorrect.")
    incorrect_answers += 1


print("3. _____ are you from?")
print ("a) What b) Who c) Where")
A =input ()
if A == "Where" or A == "c":
    print("Correct!\n")
    correct_answers += 1
else:
    print("Incorrect.")
    incorrect_answers += 1


print("4. What do you do? I’m _____ student.")
print ("a) a b) an c) the")
A =input ()
if A == "a" or A == "a":
    print("Correct!\n")
    correct_answers += 1
else:
    print("Incorrect.")
    incorrect_answers += 1



# Obliczanie procentu poprawnych odpowiedzi
percentage_correct = (correct_answers / total_questions) * 100

# Wyświetlanie ilości poprawnych odpowiedzi
print(f"\nTotal correct answers: {correct_answers}")
print(f"\nTotal incorrect answers: {incorrect_answers}\n")
print(f"Percentage correct answers: {percentage_correct:.2f}%\n")

# Wyświetlanie poprawnych odpowiedzi
print("Answers Part A\
\n1 c / 2 b / 3 c / 4 a / 5 c / 6 c / 7 a / 8 a / 9 b / 10 c\
\n11 b / 12 c / 13 a / 14 a / 15 b / 16 c / 17 c / 18 a / 19 b /2 0 a\
\n21 c / 22 c / 23 a / 24 c / 25 a / 26 b / 27 c / 28 c / 29 c / 30 a\
\n31 b / 32 b / 33 c / 34 a / 35 c / 36 b / 37 b / 38 c / 39 c / 40 a\
\n41 c / 42 c / 43 a / 44 c / 45 c / 46 a / 47 c / 48 c / 49 b / 50 c")


