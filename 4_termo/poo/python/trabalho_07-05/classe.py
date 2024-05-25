class Estado:
    def __init__(self, sig, cap):
        self.sigla = sig
        self.capital = cap

    def __repr__(self):
     return str(self.sigla)