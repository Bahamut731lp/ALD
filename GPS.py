from math import inf
import sys


def dijkstra(matrix, start, end=-1):
    n = len(matrix)

    dist = [inf]*n
    dist[start] = matrix[start][start]

    spVertex = [False]*n
    parent = [-1]*n

    path = [{}]*n

    for count in range(n-1):
        minix = inf
        u = 0

        for v in range(len(spVertex)):
            if spVertex[v] == False and dist[v] <= minix:
                minix = dist[v]
                u = v

        spVertex[u] = True
        for v in range(n):
            if not (spVertex[v]) and matrix[u][v] != 0 and dist[u] + matrix[u][v] < dist[v]:
                parent[v] = u
                dist[v] = dist[u] + matrix[u][v]

    for i in range(n):
        j = i
        s = []
        while parent[j] != -1:
            s.append(j)
            j = parent[j]
        s.append(start)
        path[i] = s[::-1]

    return (dist[end]-0, path[end]) if end >= 0 else (dist, path)


if __name__ == "__main__":
    places = ["liberec", "ceska-lipa", "chrastava",
              "new-york", "turnov", "jablonec-nad-nisou"]

    graf_m = [[0, 0, 12, 24, 22, 20],
              [0, 0, 40, 10, 52, 0],
              [12, 40, 0, 20, 0, 0],
              [24, 10, 20, 0, 15, 30],
              [22, 52, 0, 15, 0, 22],
              [20, 0, 0, 30, 22, 0]]

    graf_km = [[0, 0, 10, 35, 26, 20],
               [0, 0, 47, 30, 67, 0],
               [10, 47, 0, 14, 0, 0],
               [35, 30, 14, 0, 40, 30],
               [26, 67, 0, 40, 0, 24],
               [20, 0, 0, 30, 24, 0]]

    for line in sys.stdin:
        if 'q' == line.rstrip():
            break
        string = line.split()
        start = places.index(string[0])
        end = places.index(string[1])

        dist_m, path_m = dijkstra(graf_m, start, end)
        dist_km, path_km = dijkstra(graf_km, start, end)
        summ = 0;

        if string[2] == "nejkratsi":
            path = " -> ".join(list(map(lambda x: places[x], path_km)))

            for x in range(0, len(path_km) - 1):
                summ += graf_m[path_km[x]][path_km[x + 1]];

            print("({} min, {} km) {}".format(summ, dist_km, path))
        elif string[2] == "nejlepsi":
            path = " -> ".join(list(map(lambda x: places[x], path_m)))
            
            for x in range(0, len(path_m) - 1):
                summ += graf_km[path_m[x]][path_m[x + 1]];

            print("({} min, {} km) {}".format(dist_m, summ, path))
