from cliente import Cliente

class PessoaJuridica(Cliente):
   def __init__(self, id = "", cnpj = "", razao_social = "", tipo = "", nome_fantasia = "", endereco = "", telefone = "", email = ""):
      super().__init__(id, email, telefone, endereco)
      self._cnpj = cnpj
      self._razao_social = razao_social
      self._tipo = tipo
      self._nome_fantasia= nome_fantasia

   def validaFaturamento(self, valor = 0):
      if valor > 300000000:
         self._tipo = 'Grande empresa'
      elif valor > 4800000:
         self._tipo= 'Média empresa'
      elif valor > 360000:
         self._tipo = 'Pequena empresa'
      else:
         self._tipo = 'Pequena empresa'

   @property
   def cnpj(self):
      return self._cnpj

   @cnpj.setter
   def cnpj(self, value):
      self._cnpj = value


   @property
   def razao_social(self):
      return self._razao_social

   @razao_social.setter
   def razao_social(self, value):
      self._razao_social = value

   @property
   def nome_fantasia(self):
      return self._nome_fantasia

   @nome_fantasia.setter
   def nome_fantasia(self, value):
      self._nome_fantasia = value

   @property
   def tipo(self):
      return self._tipo

   @nome_fantasia.setter
   def tipo(self, value):
      self._tipo = value