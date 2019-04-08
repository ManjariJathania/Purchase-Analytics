import re
import os
import sys

def csvLineToArray(x):
    line=[]
    regex = r",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"
    matches = re.finditer(regex, x, re.MULTILINE)
    startPoint=0
    for matchNum, match in enumerate(matches, start=1):
        line.append(x[startPoint:match.start()])
        startPoint=match.end()
    line.append(x[startPoint:len(x)-1])
    return line

class Products:
    def __init__(self, product_id=None,product_name=None,aisle_id=None,department_id=None):
        self.product_id=product_id
        self.product_name = product_name
        self.aisle_id = aisle_id
        self.department_id = department_id

    def printData(self):
        print(self.product_id,", ",self.product_name)

class Department_Data:
    number_of_orders=1;
    number_of_first_orders=0;
    percentage=0.0

    def __init__(self,department_id=None):
        self.department_id=department_id

    def addOrder(self):
        self.number_of_orders=self.number_of_orders+1

    def addFirstOrder(self):
        self.number_of_first_orders=self.number_of_first_orders+1

    def printData(self):
        print(self.getPrintData())

    def getPrintData(self):
        return str(self.department_id)+", "+str(self.number_of_orders)+", "+str(self.number_of_first_orders)+", "+str(self.getPercentage())

    def getPercentage(self):
        return round(self.number_of_first_orders/self.number_of_orders,2)


#Main Program
product_list={}
dept_list={}
iteration=0
direct = ''
productFileName=''
orderFileName=''

print("1. Run with original (/input) data.")
print("2. Run with test1 (/insight_testsuite/tests/test1/input) data.")
print("3. Run with your-own-test_1 (/insight_testsuite/tests/your-own-test_1/input)  data.")
runType=int(input("Select the input data folder : "))

if runType==1:
    print('in 1')
    direct = './input/'
    productFileName='products.csv'
    orderFileName='order_products.csv'
elif runType==2:
    direct = './tests/test_1/input/'
    productFileName='products.csv'
    orderFileName='order_products.csv'
elif runType==3:
    direct = './tests/your-own-test_1/input/'
    productFileName='products.csv'
    orderFileName='order_products_test.csv'

assert os.path.exists(direct), "I did not find the file at, "+str(direct)

#Get the details of the Products as they are less in size.
try:
    f = open(direct+"products.csv", 'r',encoding='utf8', errors='ignore')
except:
    f = open(direct+productFileName, 'r',encoding='utf8', errors='ignore')

f.readline()
for x in f:
    iteration=iteration+1
    x=csvLineToArray(x)
    x[0]=int(x[0])
    x[2]=int(x[2])
    x[3]=int(x[3])

    try:
    	dept_list[x[3]].addOrder()
    except KeyError:
    	dept_list[x[3]]=Department_Data(x[3])

    product_list[x[0]]=Products(x[0],x[1],x[2],x[3])
f.close()

print(product_list[46894].printData())

iteration=0

try:
    f = open(direct+"order_products.csv", 'r',encoding='utf8', errors='ignore')
except:
    f = open(direct+orderFileName, 'r',encoding='utf8', errors='ignore')

f.readline()
for x in f:
    iteration=iteration+1
    x=csvLineToArray(x)
    x[1]=int(x[1])
    x[3]=int(x[3])
    #print(x)
    if x[3]==0:
        print("First Order : ",product_list[x[1]].department_id)
        dept_list[product_list[x[1]].department_id].addFirstOrder()

f.close()

print(dept_list.keys())

keyList=list(dept_list.keys())
list.sort(keyList)
print(keyList)

f = open(direct+"../output/report.csv", 'w+',encoding='utf8', errors='ignore')
f.write('department_id,number_of_orders,number_of_first_orders,percentage\n')
for x in keyList:
    dept_list[x].printData()
    f.write(dept_list[x].getPrintData()+'\n');
f.close();

name = input("")