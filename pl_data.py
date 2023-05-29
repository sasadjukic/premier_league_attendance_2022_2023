
import pandas as pd 

# getting the data from exfcel sheet
premier_league = pd.read_excel('premiere_league_attendance_2022_2023.xlsx')

# sorting clubs using stadium names
aston_villa = premier_league[premier_league['stadium'] == 'Villa Park']
arsenal = premier_league[premier_league['stadium'] == 'Emirates Stadium']
bournemouth = premier_league[premier_league['stadium'] == 'Vitality Stadium']
brentford = premier_league[premier_league['stadium'] == 'Gtech Community Stadium']
brighton = premier_league[premier_league['stadium'] == 'Amex Stadium']
chelsea = premier_league[premier_league['stadium'] == 'Stamford Bridge']
crystal_palace = premier_league[premier_league['stadium'] == 'Selhurst Park']
everton = premier_league[premier_league['stadium'] == 'Goodison Park']
fulham = premier_league[premier_league['stadium'] == 'Craven Cottage']
leeds = premier_league[premier_league['stadium'] == 'Elland Road']
leicester = premier_league[premier_league['stadium'] == 'King Power Stadium']
liverpool = premier_league[premier_league['stadium'] == 'Anfield']
manchester_united = premier_league[premier_league['stadium'] == 'Old Trafford']
manchester_city = premier_league[premier_league['stadium'] == 'Etihad Stadium']
newcastle = premier_league[premier_league['stadium'] == "St. James’ Park"]
nott_forest = premier_league[premier_league['stadium'] == 'City Ground']
southampton = premier_league[premier_league['stadium'] == 'St. Mary’s Stadium']
tottenham = premier_league[premier_league['stadium'] == 'Tottenham Hotspur Stadium']
west_ham = premier_league[premier_league['stadium'] == 'London Stadium']
wolves = premier_league[premier_league['stadium'] == 'Molineux']
