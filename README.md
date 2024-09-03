# Projeto de Roteamento de Drone

Este projeto implementa um sistema de roteamento para um drone, utilizando algoritmos de grafos para encontrar o caminho mais curto entre pontos de interesse e verificar a viabilidade da rota com base na autonomia do drone.

## Estrutura do Projeto

- `Main.py`: Script principal que executa o fluxo do programa.
- `Drone.py`: Classe que representa o drone e suas funcionalidades.
- `Grafo.py`: Classe que representa o grafo e implementa o algoritmo de Dijkstra.
- `GrafoVisual.py`: Classe que visualiza o grafo e destaca o caminho encontrado.

## Dependências

- Python 3.x
- NetworkX
- Matplotlib

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/ArthurPaganoti/projeto-drone.git
    cd projeto-drone
    ```

2. Instale as dependências:
    ```sh
    pip install networkx matplotlib
    ```

## Uso

1. Execute o script principal:
    ```sh
    python Main.py
    ```

2. Insira a autonomia do drone em metros quando solicitado.

3. O programa exibirá as distâncias calculadas, o caminho mais curto do heliporto ao destino, e verificará se a autonomia do drone é suficiente para a rota de ida e volta.

4. O grafo será visualizado com o caminho destacado.

## Exemplo de Grafo

```python
grafo_dados = {
    'heliporto': {'zona1': 300, 'zona2': 200, 'destino': 950},
    'zona1': {'heliporto': 300, 'zona2': 1200, 'destino': 600},
    'zona2': {'heliporto': 200, 'zona1': 1200, 'destino': 500},
    'destino': {'heliporto': 950, 'zona2': 500, 'zona1': 600},
}
