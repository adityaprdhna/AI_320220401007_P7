import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# Baca data dari file Excel
df = pd.read_excel('data_kalori.xlsx')

# Generate fuzzy input variables
intensitas_aktivitas = ctrl.Antecedent(np.arange(1, 11, 1), 'Intensitas Aktivitas')
durasi_istirahat = ctrl.Antecedent(np.arange(0, 4, 1), 'Durasi Istirahat')
kalori_yang_masuk = ctrl.Consequent(np.arange(0, 1001, 1), 'Kalori yang Masuk')

# Generate fuzzy membership functions for each input variable
intensitas_aktivitas['rendah'] = fuzz.trimf(intensitas_aktivitas.universe, [1, 1, 5])
intensitas_aktivitas['sedang'] = fuzz.trimf(intensitas_aktivitas.universe, [1, 5, 10])
intensitas_aktivitas['tinggi'] = fuzz.trimf(intensitas_aktivitas.universe, [5, 10, 10])

durasi_istirahat['singkat'] = fuzz.trimf(durasi_istirahat.universe, [0, 0, 2])
durasi_istirahat['sedang'] = fuzz.trimf(durasi_istirahat.universe, [0, 2, 3])
durasi_istirahat['panjang'] = fuzz.trimf(durasi_istirahat.universe, [2, 3, 3])

kalori_yang_masuk['sedikit'] = fuzz.trimf(kalori_yang_masuk.universe, [0, 0, 500])
kalori_yang_masuk['sedang'] = fuzz.trimf(kalori_yang_masuk.universe, [0, 500, 1000])
kalori_yang_masuk['banyak'] = fuzz.trimf(kalori_yang_masuk.universe, [500, 1000, 1000])

# Generate fuzzy rules
rule1 = ctrl.Rule(intensitas_aktivitas['rendah'] & durasi_istirahat['sedang'], kalori_yang_masuk['sedikit'])
rule2 = ctrl.Rule(intensitas_aktivitas['rendah'] & durasi_istirahat['panjang'], kalori_yang_masuk['sedikit'])
rule3 = ctrl.Rule(intensitas_aktivitas['sedang'] & durasi_istirahat['singkat'], kalori_yang_masuk['sedang'])
rule4 = ctrl.Rule(intensitas_aktivitas['sedang'] & durasi_istirahat['sedang'], kalori_yang_masuk['sedang'])
rule5 = ctrl.Rule(intensitas_aktivitas['sedang'] & durasi_istirahat['panjang'], kalori_yang_masuk['sedang'])
rule6 = ctrl.Rule(intensitas_aktivitas['tinggi'] & durasi_istirahat['singkat'], kalori_yang_masuk['banyak'])
rule7 = ctrl.Rule(intensitas_aktivitas['tinggi'] & durasi_istirahat['sedang'], kalori_yang_masuk['banyak'])
rule8 = ctrl.Rule(intensitas_aktivitas['tinggi'] & durasi_istirahat['panjang'], kalori_yang_masuk['banyak'])

# Generate fuzzy control system
kalori_terbakar_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
kalori_terbakar_simulator = ctrl.ControlSystemSimulation(kalori_terbakar_ctrl)

# Fuzzy inference for each row of data
hasil_kalori_terbakar = []

for index, row in df.iterrows():
    kalori_terbakar_simulator.input['Intensitas Aktivitas'] = row['Intensitas Aktivitas']
    kalori_terbakar_simulator.input['Durasi Istirahat'] = row['Durasi Istirahat (jam)']
    kalori_terbakar_simulator.compute()
    hasil_kalori_terbakar.append(kalori_terbakar_simulator.output['Kalori yang Masuk'])

# Tambahkan hasil fuzzy inference ke dalam DataFrame
df['Jumlah Kalori Terbakar (fuzzy)'] = hasil_kalori_terbakar

# Simpan DataFrame ke dalam file Excel
df.to_excel('data_kalori_with_fuzzy0.xlsx', index=False)

print("Data dengan hasil fuzzy inference telah disimpan dalam file Excel 'data_kalori_with_fuzzy0.xlsx'.")
