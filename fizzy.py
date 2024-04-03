import random
import pandas as pd
import numpy as np

# Generate 50 data
data = []

for _ in range(50):
    intensitas_aktivitas = random.randint(1, 10)  # Intensitas aktivitas (misalnya, dalam skala 1-10)
    durasi_istirahat = random.randint(1, 10)  # Durasi istirahat dalam jam
    kalori_yang_masuk = random.randint(100, 1000)  # Kalori yang masuk
    
    data.append((intensitas_aktivitas, durasi_istirahat, kalori_yang_masuk))

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Intensitas Aktivitas', 'Durasi Istirahat (jam)', 'Kalori yang Masuk'])

# Save to Excel file
df.to_excel('data_kalori.xlsx', index=False)

print("Data telah disimpan dalam file Excel 'data_kalori.xlsx'.")
