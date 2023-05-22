while 1:
    
    List1 = [('parent', 'abir', 'emon'),
                ('parent', 'abir', 'ashek'),
                ('parent', 'emon', 'remon'),
                ('parent', 'emon', 'nishi'),
                ('parent', 'ashek', 'tirtho'),
                ('parent', 'ashek', 'safi'),
                ('parent', 'nishi', 'nobel'),
                ('parent', 'nishi', 'shimanto'),
                ('parent', 'nishi', 'omor')]

    

    List2 = [('male', 'abir'),
                 ('female', 'emon'),
                 ('male', 'ashek'),
                 ('male', 'remon'),
                 ('male', 'nishi'),
                 ('male', 'tirtho'),
                 ('male', 'safi'),
                 ('male', 'nobel'),
                 ('male', 'shimanto'),
                 ('male', 'omor')]
    
    #Brother or Sister
    ch = int(input("Enter your choice to find relation of \n1-Brother\n2-Sister\n3-Uncle\n4-Aunt\nChoice: "))

    if ch == 1 or ch == 2:
        X = str(input("Enter the name: "))
        if ch == 1:
            print("Brother: ", end=' ')
        else:
            print("Sister: ", end=' ')
        for i in range(len(List1)):
            if List1[i][0] == 'parent' and List1[i][2] == X:
                for j in range(len(List1)):
                    if (
                        List1[j][0] == 'parent'
                        and List1[i][1] == List1[j][1]
                        and List1[j][2] != X
                    ):
                        for k in range(len(List2)):
                            if ch == 1:
                                if (
                                    List2[k][0] == 'male'
                                    and List2[k][1] == List1[j][2]
                                ):
                                    print(List1[j][2], end=' ')
                            else:
                                if (
                                    List2[k][0] == 'female'
                                    and List2[k][1] == List1[j][2]
                                ):
                                    print(List1[j][2], end=' ')
    #Uncle or Aunt
    elif ch == 3 or ch == 4:
        X = str(input("Enter the name: "))
        if ch == 3:
            print("Uncle: ", end=' ')
        else:
            print("Aunt: ", end=' ')
        for l in range(len(List1)):
            if List1[l][0] == 'parent' and List1[l][2] == X:
                for i in range(len(List1)):
                    if List1[i][0] == 'parent' and List1[i][2] == List1[l][1]:
                        for j in range(len(List1)):
                            if (
                                List1[j][0] == 'parent'
                                and List1[i][1] == List1[j][1]
                                and List1[j][2] != List1[l][1]
                            ):
                                for k in range(len(List2)):
                                    if ch == 3:
                                        if (
                                            List2[k][0] == 'male'
                                            and List2[k][1] == List1[j][2]
                                        ):
                                            print(List1[j][2], end=' ')
                                    else:
                                        if (
                                            List2[k][0] == 'female'
                                            and List2[k][1] == List1[j][2]
                                        ):
                                            print(List1[j][2], end=' ')
  
print("\n");