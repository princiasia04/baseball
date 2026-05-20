import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._teams = []

    def creaGrafo(self):
        self._grafo.add_nodes_from(self._teams) #tutti i miei nodi diventano team
        #creo gli archi
        #for u in self._grafo.nodes:
        #    for v in self._grafo.nodes:
        #        if u!=v:
        #            self._grafo.add_edge(u, v)

        myedges = itertools.combinations(self._teams, 2)
        self._grafo.add_edges_from(myedges)

    def getTeamsOfYear(self, year):
        self._teams = DAO.GetTeamsOfYear(year)
        return self._teams

    def getAllYears(self):
        return DAO.getAllYears()

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)