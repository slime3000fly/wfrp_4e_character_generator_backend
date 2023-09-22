import random
from random import randint
from uzupelnienie_pdf import Uzupelnianie_pdf

rasy = ["człowiek","niziołek","elf","krasnolud"]
rasa = ""

random.seed(randint(1,100000))
x = randint (1,100)

if (1<=x<=60):
    rasa = rasy[0]
elif (61<=x<=70):
    rasa = rasy[1]
elif (71<=x<=80):
    rasa = rasy[2]
elif (81<=x<=100):
    rasa = rasy[3]

pdf = Uzupelnianie_pdf()
pdf.uzupelnienie_pola_tekstowego(key_name="Rasa",text=rasa)
pdf.tworzenie_pdf()

print(rasa)