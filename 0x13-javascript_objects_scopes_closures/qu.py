class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        res = [0]*len(deck)
        q = deque(range(len(deck)))
        for n in deck:
            i = q.popleft()
            res[i] = n
            if n:
                res.append(q.popleft())
        return deck
mysol = Solution()
deck = list(map(int, input().split(',')))
print(mysol.deckRevealedIncreasing(deck))