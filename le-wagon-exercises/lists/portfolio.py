# pylint: disable=missing-docstring

# Lists from Slides
# Create, Read, Update, Delete
# append, [], =, del()
beatles = ['paul','john','ringo']
print(type(beatles))
print(beatles[1:3])
print(beatles)
beatles.append('george')
print(beatles)
beatles[0]="PAUL"
print(beatles)
del(beatles[1])
print(beatles)
for index, beatle in enumerate(beatles):
    print(f'{index+1}. {beatle.capitalize()}')

fruits=['orange','banana']
fruits.append('pear')
print(fruits)

students = [ "george" ]
students.append("jose")
students.append("steven")
print(len(students))

cities = [ "paris", "london", "lisbon" ]
print(cities[0])
print(",".join([ "paris", "london", "lisbon" ]))
# Lists
aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]
for file in portfolio:
    print(file)
# Facebook stock count
print(portfolio[3][0])
#            AAPL     GOOG    TSLA      FB
market = [ 198.84, 1217.93, 267.66, 179.06 ]
# Calculate the P&L Computation
sum=0
for i in range(0, len(market)):
    sum+= portfolio[i][0]*(portfolio[i][1]-market[i])
print(sum)

