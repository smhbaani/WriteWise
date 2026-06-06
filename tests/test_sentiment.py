from utils.sentiment import SentimentAnalyzer

analyzer = SentimentAnalyzer()

text = """
I absolutely love this project.
It is amazing and very useful.
"""

result = analyzer.analyze(text)

print(result)