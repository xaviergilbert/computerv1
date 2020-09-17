import sys
from colorama import Fore, Back, Style
from polynome_class import polynome_class

def SquareRoot(x):
    if x == 0.0:
        return 0.0
    else:
        m = 1.0
    while x >= 2.0:
        x = 0.25 * x
        m = 2.0 * m
    while x < 0.5:
        x = 4.0 * x
        m = 0.5 * m
    a = x
    b = 1.0 - x
    while 1 == 1: 
        a = a * (1.0 + 0.5 * b)
        b = 0.25 * (3.0 + b) * b ** 2
        if b < 1.0E-15:
            return a * m

def calculerDelta(a, b, c):
   return b*b-4*a*c

def resoudreEquationSecondDegre(a, b, c):
    delta = calculerDelta(a, b, c)
    if delta > 0:
        print(Fore.GREEN + "Discriminant is strictly positive, the two solutions are :")
        racineDeDelta = SquareRoot(delta)
        retour = [(-b - racineDeDelta) / (2 * a), (-b + racineDeDelta) / (2 * a)]
    elif delta < 0:
        print(Fore.RED + "Discriminant is strictly negative, there is no solution")
        exit(0)
    else:
        print(Fore.GREEN + "The solution is :")
        retour = [-b / (2 * a)]
    return retour

def frac_irreductible(x):
    x = float(x)
    if not x.is_integer():
        denominateur = 100000
        x = int(x * 100000)
    else:
        return (int(x))
    flag = 1
    if x < 0:
        x *= -1
        flag = -1
    nb = 2
    while nb < denominateur:
        if (x / nb).is_integer() and (denominateur / nb).is_integer():
            x /= nb
            denominateur /= nb
            nb = 1
        nb += 1
    if denominateur == 1:
        return (int(x))
    else:
        return (str(int(x * flag)) + " / " + str(int(denominateur)))

def clean_tab(classe):
    while (len(classe.tab) > 1 and classe.tab[-1] == 0):
        del classe.tab[-1]

def main():
    ma_classe = polynome_class(sys.argv[1])
    clean_tab(ma_classe)
    # print("tab : ", ma_classe.tab)
    print(Fore.BLUE + "Reduced form :", end = ' ')
    i = 0
    for arg in ma_classe.tab:
        if i > 2:
            print(Fore.RED, end = '')
        if len(sys.argv) == 3 and sys.argv[2].find('z') != -1 and arg == 0 and len(ma_classe.tab) != 1:
            pass
        else:
            if i != 0:
                if arg >= 0:
                    print("+",end = ' ')
                else:
                    arg = arg * -1
                    print("-",end = ' ')
            print(str(arg) + " * X^" + str(i), end = ' ')
        i += 1
    print(Fore.BLUE + "= 0")
    print(Fore.YELLOW + "Polynomial degree:", len(ma_classe.tab) - 1)
    if len(ma_classe.tab) == 3:
        ret = resoudreEquationSecondDegre(ma_classe.tab[2], ma_classe.tab[1], ma_classe.tab[0])
    elif len(ma_classe.tab) == 2:
        print(Fore.GREEN + "The solution is :", end = ' ')
        if ma_classe.tab[0] == 0:
            ret = 0
        else:
            ret = ma_classe.tab[0] / (ma_classe.tab[1]) * - 1
    elif len(ma_classe.tab) == 1:
        print(Fore.RED + "There is no solution to this polynomial")
        exit(0)
    else:
        print(Fore.RED + "The polynomial degree is stricly greater than 2, I can't solve.")
        exit(0)
    if ret == 0:
        print ("")
    if len(sys.argv) == 3 and sys.argv[2].find('f') != -1:
        if len(ma_classe.tab) == 2:
            print(frac_irreductible(ret))
        else:
            for arg in ret:
                print(frac_irreductible(arg))
    else:
        print(ret)

if __name__ == "__main__":
    main()

