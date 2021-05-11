from generator import Generator
import time

class Kreator(Generator):

    def __init__(self, diagram, slave):
        self.diagram = Generator(diagram['states'], diagram['transitions'], diagram['from_to'])
        self.slave = Generator(slave['states'], slave['transitions'], slave['from_to'])

        self.state_master_to_slave = self.diagram.states[2]
        self.states_slave_to_master = [self.slave.states[1], self.slave.states[2]]

        self.trans_after_slave = [self.diagram.transitions[3], self.diagram.transitions[2]]

        self.curr_state = self.diagram.states[0]
        self.allowed_trans = self.diagram.allowed_transitions
        self.to_run = self.diagram

    def refresh(self):
        if self.to_run.current_state == self.state_master_to_slave:
            self.to_run = self.slave
        elif self.to_run.current_state in self.states_slave_to_master:
            self.to_run = self.diagram
            if self.slave.current_state == self.states_slave_to_master[0]:
                self.trans_after_slave[0]._run(self.to_run)
            elif self.slave.current_state == self.states_slave_to_master[1]:
                self.trans_after_slave[1]._run(self.to_run)
            self.reset_slave()

        self.curr_state = self.to_run.current_state
        self.allowed_trans = self.to_run.allowed_transitions

    def reset_slave(self):

        self.slave.current_state = self.slave.states[0]

    @staticmethod
    def identifier_to_index(to_run, transition):

        for ind, tran in enumerate(to_run.transitions):
            if tran.identifier == transition:
                return ind

    def run(self, transition):

        tran_index = self.identifier_to_index(self.to_run, transition)

        self.to_run.transitions[tran_index]._run(self.to_run)
