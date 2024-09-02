class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        totalChalkNeeded = sum(chalk)
        remainingChalk = k % totalChalkNeeded
        
        for studentIndex, studentChalkUse in enumerate(chalk):
            if remainingChalk < studentChalkUse:
                return studentIndex
            remainingChalk -= studentChalkUse
        
        return 0