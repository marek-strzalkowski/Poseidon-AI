import pandas as pd
import time

# Not found infections related to death count monitor and processing time

start_time = time.time()
not_found = 0

# Get data sets from deaths and infections

data_deaths = pd.read_csv('data/deaths.csv', sep=',')
data_infections = pd.read_csv('data/infections.csv', sep=',')

# For each death case trying to match infection case (searching death date down to second month prior to) if not found add new case

for i in range(0, len(data_deaths)):
    row = 0
    del row
    search_fail = False
    
    woj = data_deaths.iloc[i,0]
    pow = data_deaths.iloc[i,1]
    plec = data_deaths.iloc[i,2]
    wiek = data_deaths.iloc[i,3]
    prod = data_deaths.iloc[i,5]
    daw = data_deaths.iloc[i,6]
    odp = data_deaths.iloc[i,7]
    year = data_deaths.iloc[i,8]
    mon = data_deaths.iloc[i,9]
    day = data_deaths.iloc[i,10]

    # Securing search month limit going to December below January

    if mon > 1:
        minmon = mon - 1
    else:
        minmon = 12

    row = data_infections.loc[(data_infections['teryt_woj'] == woj) & (data_infections['teryt_pow'] == pow) & (data_infections['plec'] == plec) & (data_infections['wiek'] == wiek) & (data_infections['producent'] == prod) & (data_infections['dawka_ost'] == daw) & (data_infections['obniz_odpornosc'] == odp) & (data_infections['year'] == year) & (data_infections['month'] == mon) & (data_infections['day'] == day) & (data_infections['zgon'] == 0)]
    
    while(len(row) == 0):        
        del row
        if(day > 1):
            day = day - 1
        elif(mon > minmon):
            mon = mon -1
            day = 31
        elif((minmon == 12) & (year == data_deaths['year'])):
            mon = 12
            day = 31
            year = year - 1
        else:
            search_fail = True
            not_found = not_found + 1
            break
        
        row = data_infections.loc[(data_infections['teryt_woj'] == woj) & (data_infections['teryt_pow'] == pow) & (data_infections['plec'] == plec) & (data_infections['wiek'] == wiek) & (data_infections['producent'] == prod) & (data_infections['dawka_ost'] == daw) & (data_infections['obniz_odpornosc'] == odp) & (data_infections['year'] == year) & (data_infections['month'] == mon) & (data_infections['day'] == day) & (data_infections['zgon'] == 0)]
        
    
    if search_fail == False:        
        index = row.index[0]        
        data_infections.loc[data_infections.index == index,'zgon'] = 1
    else:        
        new_case = {'teryt_woj': woj, 'teryt_pow': pow, 'plec': plec, 'wiek': wiek, 'producent': prod, 'dawka_ost': daw, 'obniz_odpornosc': odp, 'year': year, 'month': mon, 'day': day, 'zgon': 1}
        data_infections = data_infections.append(new_case, ignore_index = True)        
                

data_infections.to_csv('data/combined_data.csv', index=False)

# Final control data: not found count and processing time

print(not_found)
print("-- %s seconds --" % (time.time() - start_time))