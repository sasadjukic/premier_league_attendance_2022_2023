
#  import necessary libararies and modules
import pandas as pd
from pl_data import (
                      aston_villa, arsenal, bournemouth, brentford, brighton,
                      chelsea, crystal_palace, everton, fulham, leeds,
                      leicester, liverpool, manchester_united, manchester_city, newcastle,
                      nott_forest, southampton, tottenham, west_ham, wolves
                    ) 


# getting max attendence per club
villa_max = aston_villa['attendance'].max()
arsenal_max = arsenal['attendance'].max()
bournemouth_max = bournemouth['attendance'].max()
brentford_max = brentford['attendance'].max()
brighton_max = brighton['attendance'].max()
chelsea_max = chelsea['attendance'].max()
crystal_palace_max = crystal_palace['attendance'].max()
everton_max = everton['attendance'].max()
fulham_max = fulham['attendance'].max()
leeds_max = leeds['attendance'].max()
leicester_max = leicester['attendance'].max()
liverpool_max = liverpool['attendance'].max()
man_utd_max = manchester_united['attendance'].max()
man_city_max = manchester_city['attendance'].max()
newcastle_max = newcastle['attendance'].max()
nott_forest_max = nott_forest['attendance'].max()
southampton_max = southampton['attendance'].max()
tottenham_max = tottenham['attendance'].max()
west_ham_max = west_ham['attendance'].max()
wolves_max = wolves['attendance'].max()
