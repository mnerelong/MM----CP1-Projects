# Meika Milton, 1st period Programming I, Using the debugger notes.

# DEBUGGER - shows you what your code is doing while it runs.
#     It does not fix it.

grades = [85, 90, 78, 92, 88]

total = 0
count = 4 # needs to be changed to length of grades, so
count = len(grades)

for grade in grades:
    total += grade

average = total / count
print(f"The average grade is {average}.")

# EX 2
scores = [12, 45, 7, 68, 33, 90, 21]

running_total = 0
highest_score = 0

for score in scores:
        running_total += score
        #if score < highest_score: # score should be greater than.
        if score > highest_score:
            highest_score = score

print(f"Total: {running_total}")
print(f"Highest score: {highest_score}")

# Debugger is best for logic errors.