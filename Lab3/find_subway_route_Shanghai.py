import re
import math
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import requests
import json
import urllib
from urllib import request
#Build Graph
with open('E:\subway_txt\zuobiao.txt', 'r', encoding= "utf-8") as m_file:
    data=str(m_file.read())
m_file.close
#Get data from source using regular expression
def get_station_info(station_coordination):
    station_location = {}
    for line in station_coordination.split("\n"):
        if line.startswith("//"): continue
        if line.strip() == "":continue
        try:
            station = re.findall("(.+):",line)[0]#\w+ represents the chracter we are looking for;() means that I just need to return the things in parentheses
            x_y = re.findall(":(.+..+),(.+..+)",line)[0]#d represents number
            x_y = tuple(map(float,x_y))#Function is applied to the sequence to be traversed, but the final result is an object
            station_location[station] = x_y
        except:
            continue
    return station_location
station_info = get_station_info(data)
# print(station_info)
#Compute distance between stations
def geo_distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d
def get_station_distance(station1,station2):
    return geo_distance(station_info[station1],station_info[station2])
print("  The distance between 江杨北路 and 滴水湖: "+str(get_station_distance("江杨北路","滴水湖"))+" km")
print()
#Store all stations into a list
with open('E:\subway_txt\lines.txt', 'r', encoding= "utf-8") as m_file:
    data=str(m_file.read())
m_file.close
stations=[]
for line in data.split("\n"):
    stations+=re.findall("(\w+)",line)+['']

def clean_list(list_i,value):
    while value in list_i:
        list_i.remove(value)
# Build connection between notes
def build_connection_on_route(stations_info):
    stations_connection = defaultdict(list)
    data1=stations_info.copy()
    del data1[0]
    data2=stations_info.copy()
    data2.insert(0,stations_info[0]) 
    for c1 in stations_info:
        try:
            stations_connection[c1].append(data1[0])
            del data1[0]
            clean_list(stations_connection[c1],'')
        except:print
        if c1 == data2[0] : 
            del data2[0]
            continue 
        stations_connection[c1].append(data2[0])
        clean_list(stations_connection[c1],'')
        del data2[0]
    del stations_connection[''] 
    return stations_connection
build_connection_on_route=build_connection_on_route(stations)
# print(build_connection_on_route)
#Draw connection graph
stations_connection_graph = nx.Graph(build_connection_on_route)
nx.draw(stations_connection_graph, station_info,node_color= 'g',edge_color='b',with_labels=True,font_size=5,node_size=5)
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()
#Optimal search using variation of BFS based on a strategy
def bfs_search(graph,start,destination,search_strategy):
    pathes = [[start]] # list is used to store the path to be searched
    visited = set() # set is used to store the searched nodes
    while pathes:
        path = pathes.pop(0) #Extract the first path
        froniter = path[-1]  #Extract the node to be explored
        if froniter in visited : continue #Check if the point has already been explored, do not explore again
        if froniter == destination:  #Check if the destination is already searched
            return path# ！
        successsors = graph[froniter] #All child nodes join successsors
        for station in successsors:
            if station in path: continue  # check loop
            new_path = path+[station]  #New path
            pathes.append(new_path)  #bfs#Add new path to list
        pathes = search_strategy(pathes)
        visited.add(froniter) #All child nodes at this point have been traversed 

def get_distance_of_path(path):
    distance = 0
    for i,_ in enumerate(path[:-1]):
        distance += get_station_distance(path[i],path[i+1])
    return distance
def sort_by_distance(pathes):
    return sorted(pathes,key=get_distance_of_path)

def count_transfer(path):
    transfer_num = 0
    num_of_close_station=0
    # if(get_station_distance(path[-1],destination))<1.2:
    #     del(path[-1])
    for i in path:
        num_of_close_station=len(build_connection_on_route[i])
        if (num_of_close_station)==1:
            transfer_num +=1
    return transfer_num

def sort_by_num_of_transfer(pathes):
    return sorted(pathes,key=count_transfer)

inquiry_result=" --> ".join(bfs_search(build_connection_on_route,"曹杨路","龙阳路",search_strategy=sort_by_distance)) 
print("  1.Recommended shortest route: "+inquiry_result)
inquiry_result=" --> ".join(bfs_search(build_connection_on_route,"曹杨路","龙阳路",search_strategy=sort_by_num_of_transfer)) 
print("  2.The path that requires minimum transfers between two stations: "+inquiry_result)
