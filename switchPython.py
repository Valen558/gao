#should switch cases


def switchNumberToCity(i):
    allCases={
    1:'Rio',
    2:'Moscow',
    3:'London',
    4:'Brazil',
    5:'Tokyo',
    6:'SanMartin',
    7:'SanPaulo'
    }
    return allCases.get(i,'noData')


