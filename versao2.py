import numpy as np
import time
import os
import networkx as nx
import matplotlib.pyplot as plt

def carregando():
    for i in "Carregando arquivo...":
        print(i, end=' ', flush=True)
        time.sleep(0.16)
carregando()
os.system('cls') 
print('Grafo representado através da Lista de Adjacência: ')

def imprime_lista(num_v, lista):
    for i in range(num_v):
        print(f'Vértice {i+1} : {lista[i]}')
        
lista = []
def carrega_lista_adj():
    arquivo = open('grafo2.txt', 'r')
    linhas_arquivo = arquivo.readlines()
    
    for i in range(len(linhas_arquivo)):
        linha = linhas_arquivo[i].split()

        if i == 0:
            num_v = int(linha[0])
            lista_adj = [[] for _ in range(num_v)]
            lista_vertices=[i+1 for i in range((len(lista_adj)))]

        else:
            v1 = int(linha[0])
            v2 = int(linha[1])
            lista_adj[v1].append(v2 + 1)  
            
            par = (v1 + 1, v2 + 1)
            lista.append(par)

    arquivo.close()
    imprime_lista(num_v, lista_adj)

    return (lista, lista_vertices, lista_adj)

lista1, vertices_lista, lista_adj = carrega_lista_adj()

print(f'lista de adjacencia: {lista_adj}')

def DFS(G, vertices):
    cor = {u: 'B' for u in vertices} 
    pi = {u: None for u in vertices} 
    d = {}  
    f = {} 
 #   s = {u: None for u in vertices}
    lista = []
    tempo = [0]  
    
    for u in vertices:
        if cor[u] == 'B':  
            DFS_VISIT(G, u, cor, pi, d, f, lista, tempo)
    
    return lista

ordem_vertices=[]
def DFS_VISIT(G, u, cor, pi, d, f, lista, tempo):
    print(f'printando u no dfsvisit {u}')
   # sucessor = u
    cor[u] = 'C' 
    tempo[0] += 1
    d[u] = tempo[0]  
    ordem_vertices.append(u)
    
    
    for v in G[u - 1]:  
        v_list = []
        print(f'printando v {v}')
        v_list.append(v)
       # print(f'v_list antes do if {v_list}')
        if cor[v] == 'B':  
            pi[v] = u 
            DFS_VISIT(G, v, cor, pi, d, f, lista,tempo)
        if cor[v] == 'C':
            pi[v] = u
            print(f'ha um ciclo no vertice: {v} \nseu antecessor é: {pi[v]}\n')
        print(f'v_list depois do if {v_list}')
    
    cor[u] = 'P'  
    tempo[0] += 1
    f[u] = tempo[0]  
    lista.insert(0,u)
    
    
lista = DFS(lista_adj, vertices_lista)

print(f'\n\nOrdem topológica do grafo: {lista}')
