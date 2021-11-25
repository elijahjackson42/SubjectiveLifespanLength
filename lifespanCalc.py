##How long do you live?
totalSpan=24
#Calculations will be based on how subjectively long this year felt
compareYear=24
##What percentage of your total life will have subjectively passed
percentageYear=35


percentageLeft=0;


def calcLifespan (totalSpan, compareYear):
    subjectiveYear=1.0/compareYear
    total=0.0
    totalAtPercentageYear=0.0
    i=1
    while i < totalSpan+1:
        total+=1/i
        print('Year ',i,' feels like ',(1/i))
        if(i==percentageYear):
            totalAtPercentageYear=total
        i+=1
    
    print(total)
    print(totalAtPercentageYear/total)
    print(total/subjectiveYear)
    return (total/subjectiveYear)


calcLifespan(totalSpan,compareYear)