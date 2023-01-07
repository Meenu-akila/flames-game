name1=input("Enter the first name :")
name2=input("Enter the second name :")
unique_characters1=set(name1)
unique_characters2=set(name2)

def uniquecharacter_count(uniq,name):
    dict1={}
    for i in uniq:
        dict1[i]=name.count(i)
    return dict1

res1=uniquecharacter_count(unique_characters1,name1)
res2=uniquecharacter_count(unique_characters2,name2)
	
def difference_samecharacter(dic1,dic2):
    newdic={}
    for key in dic1:
        if key in dic2:
            newdic[key]=abs(dic1[key]-dic2[key])
    return newdic

a=difference_samecharacter(res1,res2)
	
def remove_commonkeys(a,b,c):
    for key in a:
        del b[key]
        del c[key]
    return {**a,**b,**c}

final=remove_commonkeys(a,res1,res2)

#print(final)
#print(a)
#print(res1)
#print(res2)

ans=list(final.values())
sum1=sum(ans)
res = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]  
while len(res) > 1 :  
    strikeAt = (sum1 % len(res) - 1)  
    if strikeAt >= 0 :  
        right = res[strikeAt + 1 : ]  
        left = res[ : strikeAt]  
        res = right + left  
    else :  
        res = res[ : len(res) - 1]       
print("Relationship :", res[0])  
