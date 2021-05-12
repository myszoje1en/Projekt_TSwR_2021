from kreator import Kreator
from diagram import diagram
from slave import slave

class ConsoleControl:
    def __init__(self):
        self.system = Kreator(diagram, slave)
        self.run = True
        self.curr_state = self.get_curr_state()
        self.curr_automat, self.curr_automat_str = self.get_curr_automat()
        self.automats_info = {'master': diagram, 'slave': slave}

    def get_curr_state(self):
        return self.system.curr_state

    def get_curr_automat(self):
        if self.system.to_run == self.system.diagram:
            return self.system.diagram, 'Master'
        elif self.system.to_run == self.system.slave:
            return self.system.slave, 'Slave'

    def get_allowed_trans(self):
        return self.system.allowed_trans

    def get_trans_name(self, transitions):
        names = []
        for tran in transitions:
            for aut in self.automats_info.values():
                for t in aut['transitions']:
                    if t['identifier'] == tran.identifier:
                        names.append(t['name'])
        return names

    def print_curr_state(self):
        print(f'###################################################################################################\n'
              f'Automat: {self.get_curr_automat()[1]}\nStan automatu: {self.get_curr_state().name}\n'
              f'---------------------------------------------------------------------------------------------------')

    def print_allowed_trans(self):
        allowed_trans = self.get_allowed_trans()
        trans_names = self.get_trans_name(allowed_trans)
        print('Dostępne akcje:\n\n'
              'q - Zakończenie działania programu\n')
        for ind, tran in enumerate(allowed_trans):
            print(f'{ind} - {trans_names[ind]} - Przejście pomiędzy stanami: '
                  f'"{tran.source.name}" >>> "{tran.destinations[0].name}"')

    def choose_tran(self):
        while True:
            inp = input('\nWybierz akcję: ')
            if inp == 'q':
                self.run = False
                choice = 'q'
                break
            else:
                try:
                    inp_int = int(inp)
                except:
                    inp_int = -1

                if inp_int <= len(self.get_allowed_trans()) - 1 and not inp_int < 0:
                    choice = self.get_allowed_trans()[int(inp)]
                    break
                else:
                    print('Podana akcja jest nieprawidłowa.')

        return choice

    def run_tran(self, tran):
        self.system.run(tran.identifier)


if __name__ == '__main__':
    con = ConsoleControl()
    while True:
        con.system.refresh()
        con.print_curr_state()
        con.print_allowed_trans()
        chosen_tran = con.choose_tran()
        if con.run:
            con.run_tran(chosen_tran)
        else:
            break