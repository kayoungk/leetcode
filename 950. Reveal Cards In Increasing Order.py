# 950. Reveal Cards In Increasing Order

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort(reverse = True)
        newDeck = []
        for number in deck:
            if newDeck:
                newFirst = newDeck.pop(0)
                newDeck.append(newFirst)
            newDeck.append(number)
        newDeck.reverse()
        return newDeck