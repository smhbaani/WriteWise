import re


class WritingSuggestions:

    def analyze(self, text):

        suggestions = []

        # --------------------------------------------------
        # LONG SENTENCES
        # --------------------------------------------------

        sentences = re.split(r'[.!?]+', text)

        for sentence in sentences:

            words = sentence.split()

            if len(words) > 25:

                suggestions.append({
                    "type": "Long Sentence",
                    "message": (
                        "This sentence is quite long. "
                        "Consider splitting it into shorter sentences."
                    ),
                    "text": sentence.strip()
                })

        # --------------------------------------------------
        # REPEATED WORDS
        # --------------------------------------------------

        words = text.lower().split()

        for i in range(len(words) - 1):

            if words[i] == words[i + 1]:

                suggestions.append({
                    "type": "Repeated Word",
                    "message": (
                        f"The word '{words[i]}' appears consecutively."
                    ),
                    "text": f"{words[i]} {words[i + 1]}"
                })

        # --------------------------------------------------
        # WEAK WORDS
        # --------------------------------------------------

        weak_words = [
            "very",
            "really",
            "quite",
            "just",
            "nice",
            "good",
            "bad",
            "thing",
            "stuff"
        ]

        for word in weak_words:

            if f" {word} " in f" {text.lower()} ":

                suggestions.append({
                    "type": "Weak Vocabulary",
                    "message": (
                        f"Consider replacing '{word}' "
                        "with a stronger word."
                    ),
                    "text": word
                })

        # --------------------------------------------------
        # EXCESSIVE ADVERBS
        # --------------------------------------------------

        adverbs = re.findall(
            r"\b\w+ly\b",
            text.lower()
        )

        if len(adverbs) >= 5:

            suggestions.append({
                "type": "Too Many Adverbs",
                "message": (
                    "Your writing contains many adverbs. "
                    "Consider using stronger verbs instead."
                ),
                "text": ", ".join(adverbs[:10])
            })

        # --------------------------------------------------
        # PASSIVE VOICE INDICATOR
        # --------------------------------------------------

        passive_patterns = [
            "was",
            "were",
            "been",
            "being"
        ]

        for word in passive_patterns:

            if f" {word} " in f" {text.lower()} ":

                suggestions.append({
                    "type": "Possible Passive Voice",
                    "message": (
                        "This text may contain passive voice. "
                        "Consider making it more direct."
                    ),
                    "text": word
                })

                break

        # --------------------------------------------------
        # NO ISSUES FOUND
        # --------------------------------------------------

        if not suggestions:

            suggestions.append({
                "type": "Excellent Writing",
                "message": (
                    "No major writing issues detected."
                ),
                "text": ""
            })

        return suggestions