# GCD ( Greatest Common Divisor) using Euclidian Algorithm
#Recursive---->gcd(a,b)=gcd(b,a%b)
#Base Case---->gcd(a,0)
def Euclid_gcd(a,b):
    if b==0:
        return a
    else:
        return Euclid_gcd(b,a%b)
a,b=input("Enter two numbwers : ").split()
result=Euclid_gcd(int(a),int(b))
print("GCD value : ",result)
