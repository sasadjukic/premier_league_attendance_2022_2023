
# import necessary libararies and modules
import pandas as pd 
from average_attandance_per_club import (
                                          villa_avg, arsenal_avg, bournemouth_avg, brentford_avg,
                                          brighton_avg, chelsea_avg, crystal_palace_avg, everton_avg,
                                          fulham_avg, leeds_avg, leicester_avg, liverpool_avg,
                                          man_utd_avg, man_city_avg, newcastle_avg, nott_forest_avg,
                                          southampton_avg, tottenham_avg, west_ham_avg, wolves_avg
                                        )

# get average attendance per club
villa_occ = round((villa_avg / 42657)*100, 2)
arsenal_occ = round((arsenal_avg / 60704)*100, 2)
bournemouth_occ = round((bournemouth_avg / 11307)*100, 2)
brentford_occ = round((brentford_avg / 17250)*100, 2)
brighton_occ = round((brighton_avg / 31708)*100, 2)
chelsea_occ = round((chelsea_avg / 40343)*100, 2)
crystal_palace_occ = round((crystal_palace_avg / 25486)*100, 2)
everton_occ = round((everton_avg / 39414)*100, 2)
fulham_occ = round((fulham_avg / 22384)*100, 2)
leeds_occ = round((leeds_avg / 37608)*100, 2)
leicester_occ = round((leicester_avg / 32262)*100, 2)
liverpool_occ = round((liverpool_avg / 53394)*100, 2)
man_utd_occ = round((man_utd_avg / 74310)*100, 2)
man_city_occ = round((man_city_avg / 53400)*100, 2)
newcastle_occ = round((newcastle_avg / 52305)*100, 2)
nott_forest_occ = round((nott_forest_avg / 30332)*100, 2)
southampton_occ = round((southampton_avg / 32384)*100, 2)
tottenham_occ = round((tottenham_avg / 62850)*100, 2)
west_ham_occ = round((west_ham_avg / 62500)*100, 2)
wolves_occ = round((wolves_avg / 31750)*100, 2)
