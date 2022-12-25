import itertools

def weeklyExpenses(inp):
# Mapping weekly cost of newspaper to its name in a dictionary
    myDict = {
    26:"TOI",
    20.5:"Hindu",
    34: "ET",
    10.5:"BM",
    16.4:"HT",
    };
    val=[26,20.5,34,10.5,16.4]
    newspaper=[]
# storing all possible combinations to a variable
    combination=list(itertools.combinations(val, 2))
    for i in combination:
        if sum(i)<=inp: #Fitering out the combinations based on the weekly budget
            newspaper.append(i)
    
    np=[]
    for i in range(len(newspaper)):
        val1=newspaper[i][0]
        val2=newspaper[i][1]
        np.append((myDict[val1],myDict[val2])) # Getting values for keys
    print(np)


inp=int(input())
weeklyExpenses(inp)



