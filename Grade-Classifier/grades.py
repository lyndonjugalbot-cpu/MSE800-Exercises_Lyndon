class GetGrades:
    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def raw_scores(self, scores):
        raw_scores = input("Enter scores (format: [score1,score2,score3,...]): ")
        raw_scores = raw_scores.strip().strip("[]")
        self.scores = [float(value.strip()) for value in raw_scores.split(",")]
        return self.scores