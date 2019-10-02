class EquacioPrimerGrau:
    def __init__(self, s):
        self.seq = s

    def calcula(self):
        p = self.seq.split()
        a = p[0]
        a = a[1-1]
        b = p[2]
        operador = p[1]
        c = p[4]
        r = ""
        if operador == "+":
            r = (int(c)-int(b))/int(a)
        elif operador == "-":
            r = (int(c)+int(b))/int(a)
        print(self.seq)
        print("x = "+str(r))

equacio = EquacioPrimerGrau("2x + 3 = 7")
equacio.calcula()
