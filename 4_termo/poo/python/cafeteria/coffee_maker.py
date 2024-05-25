class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.materia_prima = {
            "agua": 300,
            "leite": 200,
            "cafe": 100,
        }

    def status(self):
        materia = ""
        for nom, sta in self.materia_prima.items():
            materia += f"{nom} - {sta} | "
        return materia

    def report(self):
        """Prints a report of all resources."""
        print(f"Água: {self.materia_prima['agua']}ml")
        print(f"Leite: {self.materia_prima['leite']}ml")
        print(f"Cafe: {self.materia_prima['cafe']}g")

    def recursso_e_suficiente(self, bebida):
        """Returns True when order can be made, False if ingredients are insufficient."""
        pode_fazer = True
        for item in bebida.ingredientes:
            if bebida.ingredientes[item] > self.materia_prima[item]:
                print(f"Desculpe, não há suficiente {item}.")
                pode_fazer = False
        return pode_fazer

    def fazer_cafe(self, pedido):
        """Deducts the required ingredients from the resources."""
        for item in pedido.ingredientes:
            self.materia_prima[item] -= pedido.ingredientes[item]
        print(f"Aqui está o seu {pedido.nome} ☕. Aproveite!\n")
