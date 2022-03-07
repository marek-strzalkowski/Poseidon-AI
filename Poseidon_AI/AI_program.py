import pickle

# Load A.I. model

with open('data/ai_logistic_regression.pkl','rb') as f:
    model = pickle.load(f)

# Set data for specific person for specific day of infection

woj = 0         # region by TERYT data code
pow = 0         # area by TERYT data code
plec = 0        # gender ('Male': 1, 'Female': 2)
wiek = 0        # age
prod = 0        # vaccination ('Astra Zeneca': 1, 'Johnson&Johnson': 2, 'Moderna': 3, 'Pfizer': 4, None: 5)
daw = 0         # number of doses ('one': 1, 'full': 2, 'booster': 3, 'supplemental': 4, None: 5)
odp = 0         # decreased immunity ('no': 0, 'yes': 1)
year = 0        # year
mon = 0         # month
day = 0         # day of the month

# Results: 0-1 result and % probability

print('Result:')

result = model.predict([[woj,pow,plec,wiek,prod,daw,odp,year,mon,day]])

print(result)

print('Probability:')

result = model.predict_proba([[woj,pow,plec,wiek,prod,daw,odp,year,mon,day]])

print(result)