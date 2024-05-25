from pessoa import Medico, Funcionario, Cliente
from animal import Animal
from agendamento import Agendamento

med = Medico("Marcos", "15 975-605", "Marc@gmail.com", "Rua: vasto, 2-14", "459761-20", "5460-50", "Vascular", 250)

func = Funcionario("Carlos", "14 9850-580", "Carl@gmail.com", "Rua: Carlos, 250", "4562840-00", 300, "***", "Faxina")

anim = Animal("Mario", "Masculino", 250.00, "Pangaré", "Quarto de milha", "10/05/2002")

client = Cliente("Robert", "18 246-5132", "Rober@gmail.com", "Rua: girus, 480", "46801156-20", anim, False)

agend = Agendamento("20/02/2300", med, client, func, "", "", 250.00, "")

print(f"\n>> {agend.agendar()}")
print(f"Compareceu: {agend.compar}\n")

print(f">> {agend.finalizar()}")
print(f"Compareceu: {agend.compar}\n")

print(f"O animal {agend.cliente.animal.nome}, do dono {agend.cliente.nome}, concluiu uma consulta com o médico {agend.medico.nome}, conforme registrado pelo funcionário {agend.funcionario.nome}.\n")