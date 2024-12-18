
class Project:
    
    def __init__(self, pid):
        self.pid = pid
        self.atoms = []

    def addAtomToProject(self, new_atom):
        self.atoms.append(new_atom)
    