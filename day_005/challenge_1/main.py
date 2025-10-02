# 100 Days of code by Angela Yu
# Day 5 - Challenge 1 - Highest score

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]


# sum of scores ---------------------------------------------------------------
total_sum = sum(student_scores)
print(f"Built in: {total_sum}")

total_sum_function = 0
for score in student_scores:
    total_sum_function += score

print(f"Coded: {total_sum_function}")


# max score -------------------------------------------------------------------
max_score = max(student_scores)
print(max_score)

max_score_function = 0
for score in student_scores:
    if score > max_score_function:
        max_score_function = score

print(f"Coded: {max_score_function}")
