import time
import string

for _ in range(10):
        y = time.time()
        savage = y % 7
        savage = str(savage).replace('.','')
        
        lis = string.ascii_letters + str(savage)

        pw = ''
        n = len(savage)
        for i in range(n):
                if int(savage[i]) <= 5 and i < n-1 :
                        idx = int(savage[i])*10 + i
                        pw += lis[idx]
                else:
                        idx = (int(savage[i])-5)*10 + i
                        pw += lis[idx]
        print(n, pw)


