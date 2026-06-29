class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())


analyzer = TextAnalyzer("Hey, how you doing.")
print(analyzer.word_count())