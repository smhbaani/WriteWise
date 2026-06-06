from textblob import TextBlob


class SentimentAnalyzer:

    def analyze(self, text):

        blob = TextBlob(text)

        polarity = blob.sentiment.polarity

        confidence = round(abs(polarity) * 100)

        if polarity > 0.1:

            sentiment = "Positive"

            reason = (
                "The text contains mostly optimistic, "
                "encouraging, or favorable language."
            )

        elif polarity < -0.1:

            sentiment = "Negative"

            reason = (
                "The text contains mostly critical, "
                "unhappy, or unfavorable language."
            )

        else:

            sentiment = "Neutral"

            reason = (
                "The text is mostly factual and "
                "emotionally balanced."
            )

        return {
            "sentiment": sentiment,
            "polarity": round(polarity, 2),
            "confidence": confidence,
            "reason": reason
        }