from statemachine import State

# define states for a slave (way of passing args to class)
slave_options = [{'name': 'Element rozpoznany - Slave', 'value': 'el_roz_S', 'initial': True},
                 {'name': 'Ciąg dalszy procesu', 'value': 'ciag_dal', 'initial': False},
                 {'name': 'Oczekiwanie na element', 'value': 'oczek_na_el', 'initial': False}]

# create State objects for a slave
# ** -> unpack dict to args
slave_states = [State(**opt) for opt in slave_options]

# valid transitions for a slave (indices of states from-to)
slave_form_to = [[0, 1],
                 [0, 2]]

# create transitions for a slave (as a dict)
slave_transitions = [{'name': 'Element prawidłowy', 'identifier': 'ele_pra'},
                     {'name': 'Element wadliwy', 'identifier': 'ele_wad'}]

slave = {'states': slave_states, 'transitions': slave_transitions, 'form_to': slave_form_to}
