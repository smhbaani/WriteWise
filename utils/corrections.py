import language_tool_python


class TextCorrector:

    def __init__(self):

        self.tool = language_tool_python.LanguageTool("en-US")

    def get_all_errors(self, text):

        matches = self.tool.check(text)

        grammar_errors = []
        spelling_errors = []
        punctuation_errors = []

        for match in matches:

            error_text = text[match.offset : match.offset + match.error_length]

            suggestion = ""

            if match.replacements:

                suggestion = match.replacements[0]

            error_data = {
                "message": match.message,
                "error": error_text,
                "suggestion": suggestion,
                "all_suggestions": match.replacements[:5],
                "offset": match.offset,
                "length": match.error_length,
            }

            category = str(match.category).lower()

            if "typo" in category or "spelling" in category:

                spelling_errors.append(error_data)

            elif "punct" in category:

                punctuation_errors.append(error_data)

            else:

                grammar_errors.append(error_data)

        return {
            "grammar": grammar_errors,
            "spelling": spelling_errors,
            "punctuation": punctuation_errors,
        }

    def get_corrected_text(self, text):

        matches = self.tool.check(text)

        corrected_text = language_tool_python.utils.correct(text, matches)

        return corrected_text

    def get_error_statistics(self, text):

        errors = self.get_all_errors(text)

        grammar_count = len(errors["grammar"])

        spelling_count = len(errors["spelling"])

        punctuation_count = len(errors["punctuation"])

        return {
            "grammar_count": grammar_count,
            "spelling_count": spelling_count,
            "punctuation_count": punctuation_count,
            "total_errors": (grammar_count + spelling_count + punctuation_count),
        }

    def apply_single_correction(self, text, error, replacement):

        return text.replace(error, replacement, 1)

    def has_errors(self, text):

        matches = self.tool.check(text)

        return len(matches) > 0
