num = int(input("Enter number: "))


flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
    if(num%2 == 0):
        #print(num, "Even")
        for x in range(num-1, 5, -2):
            while x>23:
                if (x%2 ==0 or x%3 ==0 or x%4 ==0 or x%5 ==0 or x%6 ==0 or x%7==0 or x%8==0 or x%9==0 or x%10==0 or x%11==0 or x%12==0 or x%13 ==0 or x%14 ==0 or x%15 ==0 or x%16 ==0 or x%17 ==0 or x%18==0 or x%19==0 or x%20==0 or x%21==0 or x%22==0 or x%23==0):
                    print(x)
                    break
                else:
                    print(x, "is a prime number")
                    break 
    else:
        for x in range(num, 5, -2):
            while x>23:
                if (x%2 ==0 or x%3 ==0 or x%4 ==0 or x%5 ==0 or x%6 ==0 or x%7==0 or x%8==0 or x%9==0 or x%10==0 or x%11==0 or x%12==0 or x%13 ==0 or x%14 ==0 or x%15 ==0 or x%16 ==0 or x%17 ==0 or x%18==0 or x%19==0 or x%20==0 or x%21==0 or x%22==0 or x%23==0):
                    print(x)
                    break
                else:
                    print(x, "is a prime number")
                    break
    
else:
    print(num, "is a prime number")
