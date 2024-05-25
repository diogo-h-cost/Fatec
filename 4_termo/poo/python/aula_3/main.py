from mei import MEI
from fisica import PessoaFisica
from juridica import PessoaJuridica

mei1 = MEI( 1, '444444444-44', 'José Silva', '1111111111-0001', '',
            'MEI', 'JOsé Lanches','Rua XXX, 123', '11 1234-1234', 'jose@jose.com')

print(mei1.razao_social)

print("-" * 30)

fis1 = PessoaFisica(2, "661840249-87", "carlitos", "Rua: Casa, 520", "11 5481-2681", 
                    "Carlito@gmail.com")
print(fis1.endereco)

print("-" * 30)

jur1 = PessoaJuridica(3, "1111111111-0002", "", "Juridica", "Fanta", "Rua: Bahia, 300", 
                      "11 1670-8056", "Fanta@gmail.com")
print(jur1.nome_fantasia)