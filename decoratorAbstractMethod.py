#decorator @abstractmethod works in P2 but not in P3


from abc import ABCMeta,abstractmethod

class baseKnowledgeBase:
    __metaclass__ = ABCMeta
    #@abstractmethod    
    def getKnowledgeBaseVer(self):
        return "version BaseKnowledgeBase"

class extendedByMathKnowledge(baseKnowledgeBase):
    def getKnowledgeBaseVer2(self):
        return "extended by Programming Knowledge Module"

obMathKnowledge=extendedByMathKnowledge()
obMathKnowledge.getKnowledgeBaseVer()
