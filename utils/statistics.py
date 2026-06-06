import re


class TextStatistics:

    def get_statistics(self, text):

        # Remove extra spaces
        cleaned_text = text.strip()

        # Words
        words = cleaned_text.split()
        word_count = len(words)

        # Characters (including spaces)
        character_count = len(cleaned_text)

        # Characters (excluding spaces)
        character_no_spaces = len(
            cleaned_text.replace(" ", "")
        )

        # Sentences
        sentences = re.split(
            r'[.!?]+',
            cleaned_text
        )

        sentence_count = len(
            [s for s in sentences if s.strip()]
        )

        # Paragraphs
        paragraphs = [
            p for p in cleaned_text.split("\n")
            if p.strip()
        ]

        paragraph_count = len(paragraphs)

        # Reading Time
        # Average reading speed = 200 words/min

        reading_time = max(
            1,
            round(word_count / 200)
        )

        return {

            "word_count": word_count,

            "character_count": character_count,

            "character_no_spaces":
                character_no_spaces,

            "sentence_count":
                sentence_count,

            "paragraph_count":
                paragraph_count,

            "reading_time":
                f"{reading_time} min"
        }