import heapq
import time
from collections import defaultdict


class RoadNetwork:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = {}
        self.average_speed = 60  # Средняя скорость по умолчанию 60 км/ч

    def update_average_speed(self, speed):
        self.average_speed = speed

    def calculate_travel_time(self, distance):
        hours = distance / self.average_speed
        minutes = int(hours * 60)
        return f"{minutes // 60} ч {minutes % 60} мин"


    def add_node(self, node_id, lat, lon, address):
        self.nodes[node_id] = {'lat': lat, 'lon': lon, 'address': address}
        print(f"Точка {address} добавлена!")

    def add_edge(self, src, dest, base_distance, road_type):
        self.graph[src].append((dest, base_distance, road_type))
        self.graph[dest].append((src, base_distance, road_type))

    def adjust_weight(self, base_distance, road_type, traffic_factor, use_toll):
        multipliers = {
            0: 1.0,
            1: 1.3,
            2: traffic_factor,
            3: 0.7 if use_toll else float('inf'),
        }
        return base_distance * multipliers.get(road_type, 1.0)

    def find_optimal_route(self, start, end, traffic_factor=2.0, use_toll=True, truck_type="medium"):
        distances = {node: float('inf') for node in self.nodes}
        prev = {node: None for node in self.nodes}
        distances[start] = 0

        truck_multiplier = 1.2 if truck_type == "large" else 1.0

        heap = [(0, start)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_distance > distances[current_node]:
                continue

            if current_node == end:
                break

            for neighbor, base_distance, road_type in self.graph[current_node]:
                adjusted_distance = self.adjust_weight(base_distance, road_type, traffic_factor, use_toll)
                new_distance = current_distance + adjusted_distance * truck_multiplier

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    prev[neighbor] = current_node
                    heapq.heappush(heap, (new_distance, neighbor))

        route = []
        current = end

        while current:
            route.append({
                'node': current,
                'address': self.nodes[current]['address'],
                'coords': (self.nodes[current]['lat'], self.nodes[current]['lon'])
            })
            current = prev[current]
        route.reverse()

        total_distance = round(distances[end], 1)
        travel_time = self.calculate_travel_time(total_distance)

        return {
            'total_distance': total_distance,
            'travel_time': travel_time,
            'route': route
        }


network = RoadNetwork()

network.add_node(node_id=1, lat=48.706556, lon=44.518889, address="Волгоград, Мамаев курган")
network.add_node(node_id=2, lat=48.716667, lon=44.503333, address="Волгоград, Площадь Павших Борцов")
network.add_node(node_id=3, lat=48.708333, lon=44.516667, address="Волгоград, Центральный парк культуры и отдыха")
network.add_node(node_id=4, lat=48.713333, lon=44.523333, address="Волгоград, Музей-панорама 'Сталинградская битва'")
network.add_node(node_id=5, lat=48.705, lon=44.515, address="Волгоград, Аллея Героев")

network.add_edge(src=1, dest=2, base_distance=15.0, road_type=1)  # Городская дорога
network.add_edge(src=2, dest=3, base_distance=8.0, road_type=2)  # Дорога с пробками
network.add_edge(src=3, dest=4, base_distance=20.0, road_type=0)  # Трасса
network.add_edge(src=4, dest=5, base_distance=6.0, road_type=3)  # Платная дорога
network.add_edge(src=1, dest=5, base_distance=10.0, road_type=1)  # Городская дорога

result = network.find_optimal_route(start=1, end=3, traffic_factor=1.8, use_toll=True, truck_type='large')

print(f'Общее расстояние: {result["total_distance"]} км')
print(f'Примерное время в пути: {result["travel_time"]}')
print('Маршрут:')
for i, point in enumerate(result['route'], start=1):
    print(f'{i}. {point["address"]}')

