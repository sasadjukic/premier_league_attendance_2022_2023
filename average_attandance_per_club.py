
# import necessary libraries and modules
import pandas as pd
from pl_data import (
                      aston_villa, arsenal, bournemouth, brentford, brighton,
                      chelsea, crystal_palace, everton, fulham, leeds,
                      leicester, liverpool, manchester_united, manchester_city, newcastle,
                      nott_forest, southampton, tottenham, west_ham, wolves
                    ) 

#  get average attendance per club
villa_avg = round(aston_villa['attendance'].mean())
arsenal_avg = round(arsenal['attendance'].mean())
bournemouth_avg = round(bournemouth['attendance'].mean())
brentford_avg = round(brentford['attendance'].mean())
brighton_avg = round(brighton['attendance'].mean())
chelsea_avg = round(chelsea['attendance'].mean())
crystal_palace_avg = round(crystal_palace['attendance'].mean())
everton_avg = round(everton['attendance'].mean())
fulham_avg = round(fulham['attendance'].mean())
leeds_avg = round(leeds['attendance'].mean())
leicester_avg = round(leicester['attendance'].mean())
liverpool_avg = round(liverpool['attendance'].mean())
man_utd_avg = round(manchester_united['attendance'].mean())
man_city_avg = round(manchester_city['attendance'].mean())
newcastle_avg = round(newcastle['attendance'].mean())
nott_forest_avg = round(nott_forest['attendance'].mean())
southampton_avg = round(southampton['attendance'].mean())
tottenham_avg = round(tottenham['attendance'].mean())
west_ham_avg = round(west_ham['attendance'].mean())
wolves_avg = round(wolves['attendance'].mean())
