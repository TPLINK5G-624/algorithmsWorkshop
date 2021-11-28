class Solution:
    def translateNum(self, num: int) -> int:
        #加法原理
        '''
        alphabete = "abcdefghijklmnopqrstuvwxyz"
        di = {}
        for i in range(0,len(alphabete)):
            di[i]= alphabete[i]
        print(di)
        '''
        codes = str(num)    
        consecutive = 0
        kl = [1] + [None]* (len(codes)-1)
        for i in range(1,len(codes)):
            if 0 <= int(codes[i-1:i+1]) and 25 >= int(codes[i-1:i+1]) and codes[i-1] != '0':
                if consecutive:
                    kl[i]= kl[i-1]+consecutive
                else:
                    kl[i]= kl[i-1]*2
                consecutive = kl[i-1] 
            else:
                consecutive = 0
                kl[i]= kl[i-1]+0
        return kl[-1]