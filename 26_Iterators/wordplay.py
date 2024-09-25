class WordPlay:
    def __init__(self, l):
        self.l = l

    def words_with_length(self, length):
        return [w for w in self.l if len(w) == length]

    def starts_with(self, s):
        return [w for w in self.l if w[:len(s)] == s]

    def ends_with(self, s):
        return [w for w in self.l if w[-len(s):] == s]

    def palindromes(self):
        return [w for w in self.l if w == w[::-1]]

    def only(self, L):
        return [w for w in self.l if set(w).issuperset(set(L))]

    def avoids(self, L):
        return [w for w in self.l if not set(w).intersection(set(L))]


words = ['this', 'is', 'a', 'test', 'of', 'class', 'level']
wordplay = WordPlay(words)
print(wordplay.words_with_length(2))
print(wordplay.starts_with('t'))
print(wordplay.ends_with('vel'))
print(wordplay.palindromes())
print(wordplay.only(['t', 's']))    # -> ['this', 'test']
print(wordplay.avoids(['t', 's']))  # -> ['a', 'of']