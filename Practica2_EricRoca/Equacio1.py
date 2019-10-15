class EquacioPrimerGrau:
    def __init__(self, s):
        self.seq = s

    def calcula(self):
        p = self.seq.split()
        a = p[0]
<<<<<<< HEAD
        a = a[:-1]
=======
        a = a[1-1]
>>>>>>> ed5e2b310b4b5ee287f45a9f0e6e684ec4c19d17
        b = p[2]
        operador = p[1]
        c = p[4]
        r = ""
        if operador == "+":
<<<<<<< HEAD
            r = (float(c)-float(b))/float(a)
        elif operador == "-":
            r = (float(c)+float(b))/float(a)
            
=======
            r = (int(c)-int(b))/int(a)
        elif operador == "-":
            r = (int(c)+int(b))/int(a)
>>>>>>> ed5e2b310b4b5ee287f45a9f0e6e684ec4c19d17
        print(self.seq)
        print("x = "+str(r))

equacio = EquacioPrimerGrau("2x + 3 = 7")
equacio.calcula()
