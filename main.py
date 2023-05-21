input_filename = 'input.txt'

def read_file():
    edges = []
    with open(input_filename, 'r') as file:
        for line in file:
            edges.append(line.replace('\n', '').split(' '))
        for i in range(len(edges)):
            for j in 0, 1:
                try:
                    edges[i][j] = int(edges[i][j])
                except:
                    raise Exception('Invalid input')
    return edges


def count_degree(edges):
    degrees = {}
    for i in range(len(edges)):
        for j in 0, 1:
            this_edge = edges[i][j]
            if this_edge not in degrees.keys():
                degrees[this_edge] = 1
            else:
                degrees[this_edge] += 1


    even_degrees = {}
    for i in degrees.keys():
        if degrees[i] % 2 == 0:
            even_degrees[i] = degrees[i]
    return even_degrees


def sort_degrees(degrees):
    arr = []
    for i in degrees.keys():
        arr.append(i)

    for i in range(1, len(arr)):
        elem = arr[i]  # The current element to be inserted into the sorted part
        value = degrees[arr[i]]
        j = i - 1  # Index of the previous element

        # Moving elements larger than value one position to the right
        while j >= 0 and degrees[arr[j]] > value:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert element to correct position
        arr[j + 1] = elem

    return arr


if '__main__' == __name__:
    edges = read_file()
    degrees = count_degree(edges)
    sorted_vertexes = sort_degrees(degrees)
    for i in sorted_vertexes:
        print('Vertex ', i, ':\t', degrees[i], sep='')
