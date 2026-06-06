from utils.suggestions import WritingSuggestions

checker = WritingSuggestions()

text = """
This is a very very good paragraph.
It was written really carefully and
extremely beautifully.
"""

results = checker.analyze(text)

for item in results:
    print(item)