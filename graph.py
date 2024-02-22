import networkx as nx
from .preprocess import preprocess_text

class ArticleGraph:
    def __init__(self):
        self.graph = nx.Graph()
    
    def add_article(self, title, content, category):
        self.graph.add_node(title, category=category)#category of the article is stored as an attribute of the node.
        for word in preprocess_text(content):
            self.graph.add_node(word)
            self.graph.add_edge(title, word)
