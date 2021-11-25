totalSpan=85
compareYear=14
percentageYear=35
percentageLeft=0;


def calcLifespan (totalSpan, compareYear):
    subjectiveYear=1.0/compareYear
    total=0.0
    totalAtPercentageYear=0.0
    i=1
    while i < totalSpan:
        total+=1/i
        print(1/i)
        if(i==percentageYear):
            totalAtPercentageYear=total
        i+=1
    
    print(total)
    print(totalAtPercentageYear/total)
    print(total/subjectiveYear)
    return (total/subjectiveYear)


calcLifespan(totalSpan,compareYear)