class Tier():

    def __init__(self,rufname,farbe,alter):
        self.rufname= rufname
        self.farbe= farbe
        self.alter = alter
        self.schlafdauer = 0

    def tut_schlafen(self,dauer):
        print(self.rufname,"schläft jetzt ",dauer,"Min")
        self.schlafdauer += dauer
        print(self.rufname,"Hat insgesamt.. ",self.schlafdauer,"Minuten")


    def tut_reden(self,anzahl=1):
        print(self.rufname,"sagt..", anzahl*"miau ")

class BauplanKatze(Tier):

    def __init__(self,rufname,farbe,alter):
        super().__init__(rufname,farbe,alter)


class Hund(Tier):

    def __init__(self,rufname,farbe,alter):
        super().__init__(rufname,farbe,alter)

    def tut_reden(self,anzahl=1):
        print(self.rufname,"sagt..",anzahl*"Wuff!")

katze1= BauplanKatze("Sammy","orange",2)
Hund1=Hund("Garry","braun",6)

print(katze1.alter)
print("\n")
print(Hund1.rufname)
Hund1.tut_schlafen(2)
Hund1.tut_schlafen(20)
Hund1.tut_reden(2)
print("\n")
katze1.tut_reden(2)
Hund1.tut_reden(4)