"""
    Skript pro úlohu 11 z ALD
    @author matej.hampl
    @refactor kevin.danek
"""
from math import inf
import sys

PLACES = ["liberec", "ceska-lipa", "chrastava",
            "new-york", "turnov", "jablonec-nad-nisou"]

GRAPH_TIME = [[0, 0, 12, 24, 22, 20],
            [0, 0, 40, 10, 52, 0],
            [12, 40, 0, 20, 0, 0],
            [24, 10, 20, 0, 15, 30],
            [22, 52, 0, 15, 0, 22],
            [20, 0, 0, 30, 22, 0]]

GRAPH_DISTANCE = [[0, 0, 10, 35, 26, 20],
            [0, 0, 47, 30, 67, 0],
            [10, 47, 0, 14, 0, 0],
            [35, 30, 14, 0, 40, 30],
            [26, 67, 0, 40, 0, 24],
            [20, 0, 0, 30, 24, 0]]

def dijkstra(matrix, start, end=-1):
    """Funkce realizující dijkstrův algoritmus

    Args:
        matrix (list[list[int]]): Matice sousednosti
        start (int): Počáteční vrchol
        end (int, optional): Koncový vrchol. Defaults to -1.

    Returns:
        tuple[list[float]]: Cesta
    """
    dimension = len(matrix)
    distance = [inf]*dimension
    distance[start] = matrix[start][start]

    shortest_path_vertices = [False]*dimension
    parent = [-1]*dimension
    path = [{}]*dimension

    for _ in range(dimension-1):
        minimum_distance = inf
        shortest = 0

        vertex_index = -1
        for _ in enumerate(shortest_path_vertices):
            vertex_index += 1

            if shortest_path_vertices[vertex_index]:
                continue

            if distance[vertex_index] > minimum_distance:
                continue

            minimum_distance = distance[vertex_index]
            shortest = vertex_index

        shortest_path_vertices[shortest] = True
        for vertex_index in range(dimension):
            if shortest_path_vertices[vertex_index]:
                continue

            if matrix[shortest][vertex_index] == 0:
                continue

            if distance[shortest] + matrix[shortest][vertex_index] >= distance[vertex_index]:
                continue

            parent[vertex_index] = shortest
            distance[vertex_index] = distance[shortest] + matrix[shortest][vertex_index]

    for index in range(dimension):
        j = index
        result = []

        while parent[j] != -1:
            result.append(j)
            j = parent[j]

        result.append(start)
        path[index] = result[::-1]

    return (distance[end]-0, path[end]) if end >= 0 else (distance, path)

def process_line(input_str: str):
    """Metoda vykonávající hlavní funkci programu

    Args:
        input_str (str): Vstup z testu

    Returns:
        str: Výsledek
    """
    if 'q' == input_str.rstrip():
        return ""

    (start, end, optimisation) = input_str.split()
    origin = PLACES.index(start)
    destination = PLACES.index(end)
    summ = 0

    results = {
        "nejkratsi": dijkstra(GRAPH_DISTANCE, origin, destination),
        "nejlepsi": dijkstra(GRAPH_TIME, origin, destination)
    }

    graphs = {
        "nejkratsi": GRAPH_TIME,
        "nejlepsi": GRAPH_DISTANCE
    }

    (distance, path_to_destination) = results[optimisation]

    path = " -> ".join(list(map(lambda x: PLACES[x], path_to_destination)))

    for index in range(0, len(path_to_destination) - 1):
        summ += graphs[optimisation][path_to_destination[index]][path_to_destination[index + 1]]

    messages = {
        "nejkratsi": f"({summ} min, {distance} km) {path}",
        "nejlepsi": f"({distance} min, {summ} km) {path}"
    }

    return messages[optimisation]

def main(input_str: list[str]):
    """Metoda vykonávající hlavní funkci programu

    Args:
        input_str (str): Vstup z testu

    Returns:
        str: Výsledek
    """
    results = [process_line(x) for x in input_str]
    return "\n".join(results).strip()

if __name__ == "__main__":
    for line in sys.stdin:
        print(main(line))
