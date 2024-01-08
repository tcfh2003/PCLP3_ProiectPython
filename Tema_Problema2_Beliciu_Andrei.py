"X = 7 ( Beliciu ) Y = 6 ( Andrei ) "
import pandas as pd
import matplotlib.pyplot as plt
file_path = r'C:\Users\Andrei Beliciu\Desktop\data.csv'
# Citirea datelor din fisierul CSV
data = pd.read_csv(file_path)

# Plotează toate valorile de pe fiecare coloană
data.plot(subplots=True, layout=(2, 2), figsize=(12, 8), title="Toate valorile")
plt.show()

# Plotează primele 7 valori de pe fiecare coloană
data.head(7).plot(subplots=True, layout=(2, 2), figsize=(12, 8), title="Primele 7 valori")
plt.show()

# Plotează ultimele 6 valori pentru coloanele Durata și Puls
data.tail(6)[['Durata', 'Puls']].plot(figsize=(12, 4), title="Ultimele 6 valori pentru Durata și Puls")
plt.show()
