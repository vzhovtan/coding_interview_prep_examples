"""
Suppose that there are radio stations that need to be paid below, as well as the areas covered by the station signals.
How to select the fewest stations so that all regions can receive signals 
Given set of states where coverage is needed and array providing station's coverage
"""

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
  best_station = None
  states_covered = set()
  for station, states_for_station in stations.items():
      print(station, states_for_station)
      covered = states_needed & states_for_station
      print ("covered", covered)
      if len(covered) > len(states_covered):
          best_station = station
          states_covered = covered

  states_needed -= states_covered
  final_stations.add(best_station)

print(final_stations)
