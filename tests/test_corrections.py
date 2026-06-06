from utils.corrections import TextCorrector

corrector = TextCorrector()

sample_text = """
i am studing machne learnng.
"""

errors = corrector.get_all_errors(sample_text)

print(errors)

print()

corrected = corrector.get_corrected_text(
    sample_text
)

print(corrected)