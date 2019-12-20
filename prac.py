def fun(lst2):
    for i in range(len(lst2)-1):
        for j in range(i+1,len(lst2)):
            if lst2[i] > lst2[j]:
                lst2[i],lst2[j]=lst2[j],lst2[i]
    return lst2
        

lst =[-23,-45,-456,-1,-567]
lst1=fun(lst)
print('largest number from list is :',lst1[len(lst1)-1])
print('second smallest number from list is  :',lst1[1])
