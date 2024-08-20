graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E', 'D', 'A']
graph['C']= ['A', 'G', 'F']
graph['D'] = ['B']
graph['E'] = ['H', 'B']
graph['F'] = ['E', 'C', 'G']
graph['G'] = ['F', 'C']
graph['H'] = ['E']

print('A :',graph['A'])
print('B :',graph['B'])
print('C :',graph['C'])
print('D :',graph['D'])
print('E :',graph['E'])
print('F :',graph['F'])
print('G :',graph['G'])
print('H :',graph['H'])

matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)

adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
edges_list = []

for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key, neighbor))

for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

print("\nAdjacency Matrix : ")
for i in range(rows):
    print(adjacency_matrix[i])
