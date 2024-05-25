import re
from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, id = "", email = "", telefone = "", endereco = ""):
        self._email= email
        self._telefone = telefone
        self._endereco = endereco
        self._id = id

    @abstractmethod
    def validaFaturamento(self, valor=0):
        pass

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self.id = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        self._telefone = value

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        self._endreco = value

"""
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self._email = value
        else:
            raise ValueError(f'Invalid email address: {value}')
"""