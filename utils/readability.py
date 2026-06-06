import textstat


class ReadabilityAnalyzer:

    def analyze(self, text):

        score = round(textstat.flesch_reading_ease(text), 2)

        if score >= 90:
            level = "Very Easy"

        elif score >= 80:
            level = "Easy"

        elif score >= 70:
            level = "Fairly Easy"

        elif score >= 60:
            level = "Standard"

        elif score >= 50:
            level = "Fairly Difficult"

        else:
            level = "Difficult"

        return {
            "score": score,
            "level": level,
            "description": f"The text has a readability score of {score} "
            f"which corresponds to '{level}'.",
        }
