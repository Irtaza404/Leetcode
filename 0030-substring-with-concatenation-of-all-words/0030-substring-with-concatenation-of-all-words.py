from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or len(s) < len(words) * len(words[0]):
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        win_size = word_len * num_words
        freq = Counter(words)
        
        index = []
        i = 0
        while i <= len(s) - win_size:
            window = s[i:i + win_size]
            chunks = [window[j:j + word_len] for j in range(0, win_size, word_len)]
            chunk_count = Counter(chunks)
            if chunk_count == freq:
                index.append(i)
            i += 1
        
        return index