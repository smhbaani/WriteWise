from utils.statistics import TextStatistics

stats = TextStatistics()

text = """
Artificial Intelligence is transforming industries.

It helps automate repetitive tasks.

Many companies use AI every day.
"""

result = stats.get_statistics(text)

print(result)