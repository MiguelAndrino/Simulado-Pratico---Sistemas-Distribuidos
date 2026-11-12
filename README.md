# Simulado-Pratico---Sistemas-Distribuidos

# Central de Pedidos Distribuída

Simulado prático da disciplina de **Sistemas Distribuídos**, do curso de **Análise e Desenvolvimento de Sistemas** (Anhanguera Educacional).

- **Professora:** Prof.ª Dr.ª Simone Tatiane do Canto
- **Ambiente:** Visual Studio Code
- **Linguagem:** Python
- **Duração sugerida:** 60 minutos
- **Valor:** 1.000 pontos
- **Modalidade:** Individual

## Sobre o projeto

Uma empresa de comércio eletrônico usa um sistema para controlar o processamento de pedidos. Ele é composto por um **servidor principal** e uma **réplica**, que mantém uma cópia das informações de estoque.

O projeto simula esses dois nós por meio de estruturas em memória dentro do mesmo programa, e não por servidores reais conectados em rede. É uma simplificação didática, pensada para focar no diagnóstico dos mecanismos distribuídos.

O código já está praticamente completo. A tarefa é **analisar, identificar os problemas e fazer pequenas correções**, sem desenvolver o programa do zero.

## Conceitos abordados

- Concorrência e controle de acesso com **semáforo** (`threading.Semaphore`)
- Exclusão mútua com **lock** (`threading.Lock`)
- **Replicação** e consistência de dados
- **Tolerância a falhas** e failover
- Causalidade e ordem de eventos em sistemas distribuídos

## Problemas identificados pela equipe de TI

1. O sistema permite mais processamentos simultâneos do que o estabelecido.
2. O estoque da réplica não é atualizado corretamente.
3. Quando o servidor principal fica indisponível, o sistema não consegue utilizar a réplica.

## Como executar

1. Abra o Visual Studio Code.
2. Crie a pasta `simulado_distribuidos`.
3. Dentro dela, crie o arquivo `central_pedidos.py` e copie o código fornecido no enunciado.
4. Execute pelo terminal do VS Code:

```bash
python central_pedidos.py
```

Caso necessário, use:

```bash
py central_pedidos.py
```

> Execute primeiro o programa **sem alterações** e observe a saída antes de começar as correções.

## Desafios

### Problema A: Concorrência (200 pontos)
A empresa definiu que apenas **dois pedidos** podem ser processados simultaneamente, mas o código permite três. Localize a configuração responsável por esse limite e corrija-a.

### Problema B: Replicação e consistência (250 pontos)
Após o processamento, o estoque do servidor principal passa de 10 para 7 unidades, mas a réplica continua informando 10. Localize a função de sincronização e corrija-a para que a réplica receba o estoque atualizado do principal.

### Problema C: Tolerância a falhas (250 pontos)
O sistema deve continuar funcionando quando o servidor principal estiver indisponível. Hoje, após a simulação de falha, o programa exibe:

```
Consulta após falha: INDISPONIVEL None
```

Localize a condição incorreta na função de consulta e corrija-a para que o sistema utilize a réplica quando o principal estiver offline.

## Validação (150 pontos)

Após as três correções, execute o programa novamente. A saída esperada é:

```
=== CENTRAL DE PEDIDOS ===
Limite simultâneo: 2
Estoque inicial: 10
Pedidos confirmados: [101, 102, 103]
Estoque principal: 7
Réplica antes: 10
Réplica depois: 7
Consulta após falha: REPLICA 7
```

## Análise técnica (150 pontos)

Responda brevemente:

1. Qual é a função do semáforo no processamento dos pedidos?
2. Por que é necessário sincronizar os dados entre o servidor principal e a réplica?
3. O que significa tolerância a falhas e como ela aparece neste programa?
4. Para que serve o `Lock` no programa e como o controle de acesso aos recursos ajuda a prevenir problemas de concorrência?
5. Considerando a sequência de eventos, a sincronização do estoque deve acontecer antes ou depois do processamento dos pedidos? Explique a relação de causalidade.

## Critérios de avaliação

| Critério                          | Pontuação |
|-----------------------------------|----------:|
| Correção da concorrência          | 200       |
| Correção da sincronização         | 250       |
| Correção da tolerância a falhas   | 250       |
| Execução e validação              | 150       |
| Respostas técnicas                | 150       |
| **Total**                         | **1.000** |

## Entrega

- Arquivo `central_pedidos.py` corrigido
- Captura de tela do terminal demonstrando a execução
- Respostas às cinco questões técnicas

## Estrutura do repositório

```
simulado_distribuidos/
├── central_pedidos.py
└── README.md
```

## RESPOSTA

Durante o atividade, realizei a analise do codigo e identifique que para resolver o Problema A seria necessário realizar a mudança da
variavel MAXIMO_SIMULTANEO = 3 para MAXIMO_SIMULTANEO = 2. Assim conseguimos fazer com que somente 2 processos possam ser executado silmultaneamente.

Já para o Problema B, foi preciso realiza a mudar do nome da variavel dentro da função "consultar_estoque" alterando no segundo "if" a variavel "principal" para "replica". Dessa forma conseguimos fazer com que as informações se mantenham atualizadas em ambos os servidores. Tambem foi necessário erxcluir o processo 103 da linha "for numero in [101, 102, 103]" para que a informação aparecesse correta no terminal.

No Problema C, fazendo a alteralção do nome da varial citado no Problema B já resolvemos este problema.

Durante a validação da atividade foi identificado que o resultado esperado estava incorreto:
=== CENTRAL DE PEDIDOS ===
Limite simultâneo: 2
Estoque inicial: 10
Pedidos confirmados: [101, 102, 103]
Estoque principal: 7
Réplica antes: 10
Réplica depois: 7
Consulta após falha: REPLICA 7

Como podemos observar, o desafio pede que alteremos de 3 para 2 processos, ou seja, o estoque principal seria 8 após as operações e não 7 alem dos pedidos que deveriam retornar apenas dois numeros, 101 e 102.
=== CENTRAL DE PEDIDOS ===
Limite simultâneo: 2
Estoque inicial: 10
Pedidos confirmados: [101, 102]
Estoque principal: 8
Réplica antes: 10
Réplica depois: 8
Consulta após falha: REPLICA 8

Assim ficaria o resultado esperado de forma correta.



