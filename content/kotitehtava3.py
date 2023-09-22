'''
Käytetään alla olevaa demonstroimaan Google CoLabissa pandas interactive table ominaisuutta.
Jätetään tämä tähän, jotta opiskelijat voivat itsekin helposti kokeilla miten se
toimi Colabissa.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import data_table
from vega_datasets import data

'''

'''
Viikkotehtävä 3


Alla olevan esimerkkikoodin avulla saat luettua world-data-2023.csv tiedostosta
195 riviä ja 35 saraketta tietoa eri maiden tilanteesta. Tehtävät ovat seuraavat:

1. Muokkaa Pandas data framea siten, että valitset sieltä mielenkiintoisimmat sarakkeet, 
   jotka ovat:
   Country,Land Area, Armed Forces size,Co2-Emissions,GDP,Life expectancy,Population, Total tax rate, Unemployment rate
   Vinkki: Kysy chatGPT:ltä neuvoa, tehtävän eri vaiheissa. Sieltä saat hyviä toimivia esimerkkikoodeja käyttöösi.

2. Taulukossa on NaN lukuja, jotka ovat ongelmiallisia maksimi arvoja haettaessa. Muuta kaikki Nan => 0.
   Taulukossa on myös $ ja % merkkejä, jotka kannattaa muuttaa tyhjiksi merkeiksi ennen laskuoperaatioita.
   Taulukon numerot on esitetty muodossa 3,003,000 eli pilkut pitää muuttaa tyhjiksi merkeiksi.

3. Laske/selvitä sen jälkeen taulukosta
   a) Millä maalla on suurimmat asejoukot
   b) Millä maalla on eniten sotilaita maan kokoon verrattuna.
   c) Millä maalla on eniten sotilaita maan väestöön verrattuna.
   d) Luettele 5 suurinta Co2 päästäjää
   e) Selvitä, mihin maahan sinun kannattaisi mennä töihin valmistuttuasi (saat itse perustella GDP:n Life expectancy, Total tax rate ja Unemployment
      rate lukujen perusteella.)

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('world-data-2023.csv')

print(df)
for columns in df:
    print(columns)






