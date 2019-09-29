def nestedList(Students, Scores):
    lowest = Scores[0][0]
    for x in range Students:
        if( lowest > Scores[x][0]):
        lowest = Scores[x][0]
        output = x
    print(Scores[output][1])
