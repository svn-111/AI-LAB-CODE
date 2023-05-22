while 1:
    newTupleList =[('parent', 'Hasib', 'Rakib'),('parent', 'Rakib','Sohel'),('parent', 'Rakib', 'Rebeka'),('parent','Rashid', 'Hasib')]
    X = str(input("Enter the name to find someone's grandparent: "))
    print('Grandparent: ', end=' ')
    for i in range(len(newTupleList)):
        if newTupleList[i][0] == 'parent' and newTupleList[i][2] == X:
            for j in range(len(newTupleList)):
                if (newTupleList[j][0] == 'parent' and newTupleList[i][1] == newTupleList[j][2]):
                    print(newTupleList[j][1], end=' ')
    print("\n");