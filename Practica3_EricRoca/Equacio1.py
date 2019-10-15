class EquacioPrimerGrau:
    def __init__(self, s):
        self.eq = s

    def calcula(self):
        self.p = self.eq.split()

        if "x" in self.p[0]:
            self.a = self.p[0]
            self.a = self.a[:-1]
            self.b = self.p[2]
            self.operador = self.p[1]
            self.c = self.p[4]
            self.r = ""
        else:
            return "l'equacio no segueix el format: ax + b = c"

        try:
            float(self.p[2])
        except:
            return "l'equacio conte caracter no calculables: "+self.eq

        if self.operador == "+":
            self.r = (float(self.c)-float(self.b))/float(self.a)
        elif self.operador == "-":
            self.r = (float(self.c)+float(self.b))/float(self.a)
        else:
            self.r = "Operador no valid: "+self.b

        return self.r
