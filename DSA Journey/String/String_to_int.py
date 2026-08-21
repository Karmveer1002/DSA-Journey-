class Solution:
    def myAtoi(self, input):
        i = 0
        sign = 1
        ans = 0
        while i < len(input) and input[i]==" ":
            i+=1
        if i < len(input) and input[i]=="-":
            sign = -1
            i+=1
        elif i < len(input) and input[i]=="+":
            i+=1
        while i < len(input) and input[i].isdigit():
            digit = int(input[i])
            ans = ans * 10 + digit
            i += 1

        ans = ans * sign

        if ans < -2147483648:
            return -2147483648

        if ans > 2147483647:
            return 2147483647

        return ans