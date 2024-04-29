# operator = ['+','-','/','*']
# operand = []
# exp = input("Enter Postfix Expression: ")
# expression = exp.split(' ')
# for ele in expression:
#     if(ele not in operator):
#         operand.append(ele)
#     else:
#         num1 = eval(operand.pop())
#         num2 = eval(operand.pop())
#         if(ele == '+'):
#             ans=num2+num1
#         elif(ele == '-'):
#             ans=num2-num1
#         elif(ele == '/'):
#             ans=num2/num1
#         elif(ele == '*'):
#             ans=num2*num1
#         operand.append(str(ans))
# print('ans = ',operand[0])


class Evaluate:
 
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
         
        self.array = []
 
    def isEmpty(self):
        return True if self.top == -1 else False
 
    def peek(self):
        return self.array[-1]
 
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
 
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    def evaluatePostfix(self, exp):
 
        for i in exp:
 
        
            if i.isdigit():
                self.push(i)
 
           
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
 
        return int(self.pop())
 
if __name__ == '__main__':
    exp = input("Enter Postfix Expression: ")
    obj = Evaluate(len(exp))
     
    print("postfix evaluation: %d" % (obj.evaluatePostfix(exp)))
