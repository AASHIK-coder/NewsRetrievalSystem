from .preprocess import preprocess_text

def retrieve_articles(graph, query):
    query_words = set(preprocess_text(query))
    articles_found = []
    
    for node in graph.graph.nodes(data=True):  # to access the graph attribute of the ArticleGraph instance
        if 'category' in node[1]:  # Checking if node is an article
            # Assuming node[0] (the title) is representative of the article's content.
            content_words = set(preprocess_text(" ".join(graph.graph[node[0]])))  
            if query_words.issubset(content_words):
                articles_found.append(node[0])
    
    return articles_found
