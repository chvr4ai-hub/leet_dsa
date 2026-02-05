# print numbers 1 to N using recursion method

# print 1 to N using HEAD recursion
def printn_hr(i, n):
    if i>n:
        return

    print(i)
    printn_hr(i+1, n)

# print 1 to N using TAIL recursion (Back tracing)
def printn_tr(i, n):
    
    # backtracing (reverse order printing)
    # if i>n:
    #   return

    # printn_tr(i+1, n)
    # print(i)



    # forward printing using TAIL recursion
    if n==0:
        return

    printn_tr(i, n-1)
    print(n)






i = 1
n = 5

print("HEAD recursion output: ")
printn_hr(i, n)

print("TAIL recursion output: ")
printn_tr(i, n)


