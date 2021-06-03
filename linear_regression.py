
class linearRegression:
    def __init__(self, rate, i, j, xlist, ylist, testvalue):
        self.rate = rate #learning rate for gradient descent
        self.i = i #weight 1
        self.j = j #weight 2
        self.xlist = xlist #input lsit
        self.ylist = ylist #output list
        self.testvalue = testvalue #value for testing the output

    def sumi(self, i, j): #sum of derivative function values for the 1st parameter
        result = 0
        for k in range(len(self.xlist)):
            result = result + ((i+self.xlist[k]*j)-self.ylist[k])

        return result

    def sumj(self, i, j): #sum of derivative function for the 2nd parameter
        result = 0
        for k in range(len(self.xlist)):
            result = result + (((i + self.xlist[k] * j) - self.ylist[k])*self.xlist[k])
        return result

    def costfunction(self, parameter0, parameter1): #computing the error
        sum = 0
        for k in range(len(self.xlist)):
            sum = sum + ((parameter0+self.xlist[k]*parameter1)-self.ylist[k])**2

        return (1/(len(self.xlist)))*sum


    def minimize(self): #minimizing the error function using gradient descent
        k = 0
        init1 = 0
        init2 = 0
        result1 = 99999999
        result2 = 99999999

        while True:
            if k==0:
                result1 = init1 - (self.rate * (1 / (len(self.xlist)))) * self.sumi(0, 0)
                result2 = init2 - (self.rate * (1 / (len(self.xlist)))) * self.sumj(0, 0)
                k = k+1
                if((abs(self.costfunction(init1, init2) - self.costfunction(result1, result2)) < (0.0001))):
                    break
                else:
                    continue
            else:

                init1 = result1
                init2 = result2
                result1 = init1 - (self.rate*(1/(len(self.xlist)))*self.sumi(init1, init2))
                result2 = init2 - (self.rate*(1/(len(self.xlist))))*self.sumj(init1, init2)
                k = k+1
                if((abs(self.costfunction(init1, init2) - self.costfunction(result1, result2)) < 0.0001)):
                   break
        print(k)
        print([result1, result2])

        return [result1, result2]

    def test(self):
        return self.minimize()[0]+self.minimize()[1]*self.testvalue




#this part is for creating a training and testing data
#I generate a list1 of numbers from 0 to 100 as an input. The output is list1[i] * 2
#Basically the algorithm needs to learn to multiply a number by 2

def makedata():
    list1 = []
    i = 2

    for i in range(100):
        list1.append(i)
    return list1


def makedata2():
    list2 = []

    list1 = makedata()
    for i in list1:
        list2.append(i * 2)

    return list2

#running the linear regression with generated data:
reg = linearRegression(0.00001, 0, 0, makedata(), makedata2(), 600)
print(reg.test())






