import pandas as pd

#INFECTIONS

data = pd.read_csv('data/ewp_dsh_zakazenia_po_szczepieniu_20211222.csv', sep=';').iloc[::-1]

clean_data = data.drop(columns=['kat_wiek','liczba_zaraportowanych_zakazonych'])
clean_data[["year", "month", "day"]] = clean_data["data_rap_zakazenia"].str.split("-", expand = True)
clean_data['year'] = clean_data['year'].astype(int)
clean_data['month'] = clean_data['month'].astype(int)
clean_data['day'] = clean_data['day'].astype(int)
clean_data['wiek'] = clean_data['wiek'].astype(float)
clean_data['zgon'] = 0
clean_data = clean_data.drop(columns=['data_rap_zakazenia'])

mapping = {'M': 1, 'K': 2, 'nieznana' : 3}
clean_data = clean_data.replace({'plec': mapping})
mapping_producer = {'Astra Zeneca': 1, 'Johnson&Johnson': 2, 'Moderna': 3, 'Pfizer': 4, 'brak danych':5, None: 5}
clean_data = clean_data.replace({'producent': mapping_producer})
mapping_repeat = {'jedna_dawka': 1, 'pelna_dawka': 2, 'przypominajaca': 3, 'uzupełniająca': 4, None: 5}
clean_data = clean_data.replace({'dawka_ost': mapping_repeat})

clean_data = clean_data.dropna()

clean_data['teryt_woj'] = clean_data['teryt_woj'].astype(int)
clean_data['teryt_pow'] = clean_data['teryt_pow'].astype(int)

clean_data = clean_data.reset_index(drop=True)

clean_data.to_csv('data/infections.csv', index=False)


# DEATHS

data = pd.read_csv('data/ewp_dsh_zgony_po_szczep_20211222.csv', sep=';')

clean_data = data.drop(columns=['kat_wiek','liczba_zaraportowanych_zgonow'])
clean_data[["year", "month", "day"]] = clean_data["data_rap_zgonu"].str.split("-", expand = True)
clean_data['year'] = clean_data['year'].astype(int)
clean_data['month'] = clean_data['month'].astype(int)
clean_data['day'] = clean_data['day'].astype(int)
clean_data['wiek'] = clean_data['wiek'].astype(float)
clean_data = clean_data.drop(columns=['data_rap_zgonu'])

mapping = {'M': 1, 'K': 2, 'nieznana' : 3}
clean_data = clean_data.replace({'plec': mapping})
mapping_producer = {'Astra Zeneca': 1, 'Johnson&Johnson': 2, 'Moderna': 3, 'Pfizer': 4, None: 5}
clean_data = clean_data.replace({'producent': mapping_producer})
mapping_repeat = {'jedna_dawka': 1, 'pelna_dawka': 2, 'przypominajaca': 3, 'uzupełniająca': 4, None: 5}
clean_data = clean_data.replace({'dawka_ost': mapping_repeat})

clean_data = clean_data.dropna()

clean_data['teryt_woj'] = clean_data['teryt_woj'].astype(int)
clean_data['teryt_pow'] = clean_data['teryt_pow'].astype(int)

clean_data = clean_data.reset_index(drop=True)

clean_data.to_csv('data/deaths.csv', index=False)