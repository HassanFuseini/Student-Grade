student_scores = []
for i in range(1, 17):
    scores = []
    print(f"Enter test scores for Student {i}: ")
    for j in range(1, 5):
        score = float(input(f"Test {j}: "))
        scores.append(score)
    student_scores.append(scores)
print("\nAverage Test Scores for Each Student: ")
for i, scores in enumerate(student_scores, start=1):
    average_score = sum(scores) / len(scores)
    print(f"Student {i}: Average Score = {average_score:.2f}")
