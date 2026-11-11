import threading
import time

# Servidores simulados

principal = {
    "online": True,
    "estoque": 10
}

replica = {
    "online": True,
    "estoque": 10
}

# Controle de concorrência

MAXIMO_SIMULTANEO = 2

semaforo = threading.Semaphore(
    MAXIMO_SIMULTANEO
)

trava = threading.Lock()
pedidos_confirmados = []

def processar_pedido(numero):
    with semaforo:
        time.sleep(0.1)
        
        with trava:
            if principal["estoque"] > 0:
                principal["estoque"] -= 1
                pedidos_confirmados.append(
                    numero
                )

def sincronizar():
    replica["estoque"] = principal["estoque"]

def consultar_estoque():
    if principal["online"]:
        return (
            "PRINCIPAL",
            principal["estoque"]
        )

    if replica["online"]:
        return (
            "REPLICA",
            replica["estoque"]
        )

    return "Disponivel", None

print("=== CENTRAL DE PEDIDOS ===")
print(
    "Limite simultâneo:",
    MAXIMO_SIMULTANEO
)

print(
    "Estoque inicial:",
    principal["estoque"]
)

trabalhadores = [
    threading.Thread(
        target=processar_pedido,
        args=(numero,)
    )   
    for numero in [101, 102]
]

for trabalhador in trabalhadores:
    trabalhador.start()

for trabalhador in trabalhadores:
    trabalhador.join()

print(
    "Pedidos confirmados:",
    sorted(pedidos_confirmados)
)

print(
    "Estoque principal:",
    principal["estoque"]
)

print(
    "Réplica antes:",
    replica["estoque"]
)

sincronizar()

print(
    "Réplica depois:",
    replica["estoque"]
)

# Simulação de falha

principal["online"] = False

nome, estoque = consultar_estoque()

print(
    "Consulta após falha:",
    nome,
    estoque
)
