class PiPiChecker:
    wordDic=["pipi","皮皮"]
    def __init__(self):
        pass

    def checkContent(self,s):
        for word in self.wordDic:
            if word in s:
                return True
        return False
