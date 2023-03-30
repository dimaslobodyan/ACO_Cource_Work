import numpy as np
from scipy import spatial

# num_points = 12 # количество вершин
# # points_coordinate = np.random.rand(num_points, 2)
# # print(points_coordinate)
# points_coordinate=np.array([[2.,1.],
#                            [3.,4.],
#                            [5.,2.],
#                            [7.,5.],
#                            [4.,7.],
#                            [10.,5.],
#                            [10.,2.],
#                            [14.,3.],
#                            [17.,6.],
#                            [9.,9.],
#                            [13.,8.],
#                            [16.,9.]])


with open("data.txt", "r") as file:
    contents = file.readlines()
    time_to_fly=float(contents[0])
    speed=float(contents[1])
    start = np.asfarray(contents[2].split(' '))
    points_coordinate = np.array([start])
    end = np.array([np.asfarray(contents[3].split(' '))])
    num_points= int(contents[4])
    for i in range(num_points):
        points_coordinate=np.append(points_coordinate, np.array([np.asfarray(contents[6+2*i].split(' '))]), axis=0)
    points_coordinate = np.append(points_coordinate, end, axis=0)
    num_points+=2

distance=time_to_fly*speed

# print("Координаты вершин:\n", points_coordinate, "\n")

# вычисление матрицы расстояний между вершин
distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')
# print("Матрица расстояний:\n", distance_matrix)