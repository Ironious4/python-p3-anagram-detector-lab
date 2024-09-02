class Anagram:
    def __init__(self,word):
        self.word=word.lower()

    def match(self, possible_anagrams):
        sorted_word= sorted(self.word)
        return[w for w in possible_anagrams if sorted(w.lower())==sorted_word]
        