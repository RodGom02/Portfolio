def compute_grade(score):
    try: 
        score = float(input("Enter score: "))

        if score > 1.0 or score < 0.0:
            print ('Liar')
        elif score <= 1.0 and score >= 0.90:
            print('A')
        elif score < 0.90 and score >= 0.80:
            print('B')
        elif score < 0.80 and score >= 0.70:
            print('C')
        elif score < 0.70 and score >= 0.60:
            print('D')
        elif score < 0.60 and score >= 0.00:  
            print('F')
    except ValueError:
        return "Enter a valid score"

score = input("Enter Score: ")
print(compute_grade(score))

