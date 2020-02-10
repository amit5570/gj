def LCS_length(X,Y):
    if not X or not Y:
        return ""
    x,m,y,n =X[0],X[1:],Y[0],Y[1:]
    if x == y:
        return x+LCS_length(m,n)
    else:
        return max(LCS_length(X,n),LCS_length(m,Y),key=len)
print(LCS_length('thisisatest','testingLCS123testing'))    
    
