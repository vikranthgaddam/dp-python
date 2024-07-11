
def basicRecursion(text1,text2,m,n)->int:
    if m ==0 or n==0:
        return 0
    elif text1[m-1]==text2[n-1]:
        return 1+basicRecursion(text1,text2,m-1,n-1)
    else:
        return max(basicRecursion(string1,string2,m-1,n),basicRecursion(string1,string2,m,n-1))

#if an empty string the max is 0 
#To accomodate it we initialize with n+1,m+1
def optimizedSolution(text1,text2,m,n)->int:
    dp =[None*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif text1[i-1]==text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

    
if __name__=='__main__':
    string1=""
    string2=""
    print("Length",basicRecursion(string1,string2,len(string1),len(string2)))