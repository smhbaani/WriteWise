from utils.readability import ReadabilityAnalyzer

analyzer = ReadabilityAnalyzer()

text = """
Artificial Intelligence is changing the world.
It helps automate repetitive tasks and improve productivity.
"""

result = analyzer.analyze(text)

print(result)