#import class to get grade details
from grades import GetGrades


def main():
    #get scores from user input
    scores = GetGrades().raw_scores(scores=[])

    #initialize list to store results
    results = []

    #loop through the scores and get the corresponding grades
    for score in scores:
        grade = GetGrades.get_grade(score)
        results.append((score, grade))

    #loop through the results and print the score and grade
    print("-" * 30)
    for score, grade in results:
        print(f"Score: {score:.1f} - Grade: {grade}")


if __name__ == "__main__":
    main()
