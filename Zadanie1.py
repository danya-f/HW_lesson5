class Magaziny :
    def __init__(self,nazvanie,razmer,viruchka):
        self.nazvanie = nazvanie
        self.razmer  = razmer
        self.__viruchka = viruchka

    def privet(self):
        return f'Prixodi k nam v {self.nazvanie}'


    def set_new_razmer(self, new_razmer):
        self.razmer = new_razmer


mag1 = Magaziny('5ka','mini','40000000')
mag2 = Magaziny('Lerua','Super','345345')



class ProduktMag(Magaziny):

    def_vid = 'Produktoviy'

    def __init__(self,nazvanie,razmer,viruchka):
        super().__init__(nazvanie,razmer,viruchka)




mag3 = ProduktMag('1ka','big','4000')

print(mag1.privet())
print(mag3.def_vid)



class Stritel(Magaziny):

    def_vid = 'Stroitelniy'


    def __init__(self,nazvanie,razmer,viruchka):
        super().__init__(nazvanie,razmer,viruchka)

mag4 = Stritel('Lerua','rly_big','400')


print(mag4.def_vid)


print(mag4.razmer)
mag4.set_new_razmer('malish(')
print(mag4.razmer)

print(mag4.razmer+mag4.nazvanie)