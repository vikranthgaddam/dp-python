#You are climbing a staircase. It takes n steps to reach the top.
#each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution:
    def climbStairs(self,n:int)->int:
        if n==1:
            return 1
        
        no_of_ways_one=1 #if one step
        no_of_ways_two=2 #if two steps
        # we need the no of ways of N
        for n in range(3,n+1):
            next_number_of_ways=no_of_ways_one+no_of_ways_two
            no_of_ways_one=no_of_ways_two
            no_of_ways_two=next_number_of_ways
        
        return no_of_ways_two
    
    def climbStairs_binet(self,n:int)->int:
        #fibonacci type series started from 0,1,1,2,3,5 here 1,2,3,5
        n+=1
        a=5**1/2
        final_ways_n=(((1+a)/2)**n -((1-a)/2)**n)/a
        return int(round(final_ways_n))
    
    

    