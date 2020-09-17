from colorama import Fore, Back, Style

class polynome_class:
    def __init__(self, chaine):
        self.chaine = chaine
        self.expressions = []
        self.flag_egal = 0
        self.tab = []
        self.parse_elem()

    class Expression():
        def __init__(self, chaine, prev_expr = None):
            self.prev_expr = prev_expr
            self.chaine = chaine
            self.flag_egal = 0
            self.signe = 1 # 1: pos, -1:neg
            self.power = 0
            self.value = 0

        def get_sign(self):
            if not self.chaine[0] in "+-":
                self.signe = 1
                if self.chaine[0] == "=":
                    self.signe = -1
                    return 0

            else:
                self.signe = 1 if self.chaine[0] == "+" else -1
                tmp = self.prev_expr
                while tmp.chaine == "-" or tmp.chaine == "+":
                    if self.signe == 1:
                        self.signe = 1 if tmp.chaine == "+" else -1
                    else:
                        self.signe = -1 if tmp.chaine == "+" else 1
                    tmp = tmp.prev_expr
                    if tmp == None:
                        break
                    
            if self.flag_egal == 1:
                self.signe *= -1
            
            return 1

        def get_power(self):
            i = len(self.chaine) - 1
            while self.chaine[i] not in "X^" and i > 0:
                i -= 1
            if "X" not in self.chaine:
                self.power = 0
            elif self.chaine[i:] == "X":
                self.power = 1
            else:
                self.power = self.chaine[i+1:]

        def get_value(self):
            start = 0
            for indice, char in enumerate(self.chaine):
                if char in "X*":
                    self.value = self.chaine[start:indice] if self.chaine[start:indice].strip() != "" else "1"
                    break
                if char not in ".0123456789 ":
                    start += 1
            if "X" not in self.chaine:
                self.value = self.chaine[start:]              

    def get_expressions(self):
        tmp = 0
        for indice, char in enumerate(self.chaine):
            if char in "-+=":
                self.expressions.append(self.Expression(self.chaine[tmp:indice].strip()))
                tmp = indice
            if indice == len(self.chaine) - 1:
                self.expressions.append(self.Expression(self.chaine[tmp:].strip()))
        # debug
        for indice, expression in enumerate(self.expressions):
            if indice > 0:
                expression.prev_expr = self.expressions[indice - 1]

    def parse_elem(self):
        self.get_expressions()
        for expression in self.expressions:
            # print("expression : ", expression.chaine)
            if expression.chaine == "+" or expression.chaine == "-" or expression.chaine == "=" or expression.chaine == "":
                if expression.chaine == "=":
                    self.flag_egal = 1
            else:
                expression.flag_egal = 1 if self.flag_egal == 1 else 0
                if expression.get_sign() == 0:
                    self.flag_egal = 1
                expression.get_power()
                expression.get_value()
                # print("signe : ", expression.signe, ", puissance : ", expression.power, ", value : ", expression.value)

                while len(self.tab) <= int(expression.power):
                    self.tab.append(0)
                try:
                    self.tab[int(expression.power)] += float(expression.value) * expression.signe
                except:
                    print(Fore.RED + "Verifier le format de l'element \"", expression.chaine, "\" de l'equation svp")
                    exit()