a=int(input("Saisir le première nombre  : "))
b=int(input("Saisir le deuxième nombre  : "))
ope=input("Saisir l'operation : ")
while(ope!='/' and ope!='*' and ope!='-' and ope!='+' ):
    ope=input("Saisir l'operation : ")
match ope:
    case '/':
        print(f"{a}/{b}={a/b}")
    case '*':
        print(f"{a}*{b}={a*b}")
    case '+':
        print(f"{a}+{b}={a+b}")
    case '-':
        print(f"{a}-{b}={a-b}")

