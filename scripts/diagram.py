from statemachine import State

# define states for a master (way of passing args to class)
master_options = [{"name": "Ramię w pozycji I", "initial": True, "value": "ramie_w_pozycji_I"},  # 0
                  {"name": "Element na linii I", "initial": False, "value": "element_na_linii_I"},  # 1
                  {"name": "Element rozpoznany - Master", "initial": False, "value": "element_rozpoznany_M"},  # 2
                  {"name": "Element na linii II", "initial": False, "value": "element_na_linii_II"},  # 3
                  {"name": "Ramię w pozycji II", "initial": False, "value": "ramie_w_pozycji_II"}]  # 4

# create State objects for a master
# ** -> unpack dict to args
master_states = [State(**opt) for opt in master_options]

# valid transitions for a master (indices of states from-to)
master_form_to = [[0, 1],
                  [1, 2],
                  [2, 0],
                  [2, 3],
                  [3, 4],
                  [4, 0]]

# create transitions for a master (as a dict)
master_transitions = [{'name': 'Czekanie na element', 'identifier': 'czekanie_na_el'},
                      {'name': 'Rozpoznanie elementu', 'identifier': 'rozpoznanie_el'},
                      {'name': 'Oczekiwanie na element', 'identifier': 'oczekiwanie_na_el'},
                      {'name': 'Transport elementu', 'identifier': 'transport_el'},
                      {'name': 'Odłożenie elementu', 'identifier': 'odl_el'},
                      {'name': 'Powrót do pozycji', 'identifier': 'pow'}]

diagram = {'states': master_states, 'transitions': master_transitions, 'form_to': master_form_to}
