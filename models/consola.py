from huron import Huron
from boaConstrictor import BoaConstrictor

boa = BoaConstrictor("Anabelle", 5, 2.1, "Argentina", 120.1)
huron = Huron("Pedro", 6, 5.2, "Egipto", 52.2)

boa.hacer_sonido()
huron.hacer_sonido()

boa.comer_raton()

print(boa.hacer_sonido())
print(huron.hacer_sonido())

print(boa.__dict__)
print(huron.__dict__)
