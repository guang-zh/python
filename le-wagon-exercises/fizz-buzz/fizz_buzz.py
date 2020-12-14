# Start with some pseudo-code!

# For n from 1 to 100
#     if n is divisible by 3
#         print 'fizz'
#     else if n is divisble by 5
#         print 'buzz'
#     else if n is divisible by 3 and by 5
#         print 'fizzbuzz'
#     else
#         print n
# Bug with the orders. 15 will be displayed to fizz, not to the 3rd block

for n in range(1,100+1):
    if (n%3==0 and n%5==0):
        print('fizzbuzz')
    elif (n%3==0):
        print('fizz')
    elif(n%5==0):
        print('buzz')
    else:
        print(n)

print("The Wagon"!="The Wagon")