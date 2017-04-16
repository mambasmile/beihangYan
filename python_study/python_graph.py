#coding=utf-8
'''
Created on 2017年2月24日

@author: Administrator
'''



def find_path(graph,start,end,path=[]):
    path = path+[start]
    if end == start:
        return path
    if not graph.has_key(start):
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

graph={'A':['B','C'],
       'B':['C','D'],
       'C':['D'],
       'D':['C'],
       'E':['F'],
       'F':['C']}
path=[]
path = find_path(graph, 'A', 'D', path)
print path

def find_all_paths(graph,start,end,path=[]):
    path = path+[start]
    if start==end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for newNode in graph[start]:
        if newNode not in path:
            newpaths = find_all_paths(graph, newNode, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

path = []
paths =  find_all_paths(graph, 'A', 'D', path)
print paths

def find_shortest_path(graph,start,end,path=[]):
    path = path+[start]
    if start==end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for newNode in graph[start]:
        if newNode not in path:
            newpath = find_shortest_path(graph, newNode, end, path)
            if newpath:
                if not shortest or len(newpath)<len(shortest):
                    shortest=newpath
    return shortest

path = []
path =  find_shortest_path(graph, 'A', 'D', path)
print path