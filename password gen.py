import time

seconds = time.time()
print(seconds)

x = float(7)
y = seconds

print(y % x)

savage = (y % x)
print(str(savage), type(savage))


list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','0','1','2','3','4','5','6','7','8','9']

new = str(list).join(str(savage))

print(new)

print("List index-value are : ")
for savage in range(len(list)):


        print(savage, end = "")
        print(list[int(savage)])



