from statemachine import StateMachine, State, Transition

# create a generator class
class Generator(StateMachine):
    def __init__(self, states, transitions, form_to):

        # creating each new object needs clearing its variables (otherwise they're duplicated)
        self.states = []
        self.transitions = []
        self.states_map = {}

        # create fields of states and transitions using setattr()
        # create lists of states and transitions
        # create states map - needed by StateMachine to map states and its values
        for s in states:
            setattr(self, s.value, s)
            self.states.append(s)
            self.states_map[s.value] = s

        for ind, tran in enumerate(form_to):
            transition = Transition(self.states[tran[0]], self.states[tran[1]],
                                    identifier=transitions[ind]['identifier'])
            setattr(self, transition.identifier, transition)
            self.transitions.append(transition)
            self.states[tran[0]].transitions.append(transition)

        # super() - allows us to use methods of StateMachine in our Generator object
        super(Generator, self).__init__()