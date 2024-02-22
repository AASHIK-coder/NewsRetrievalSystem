import pandas as pd
from src.graph import ArticleGraph
from src.retrieval import retrieve_articles

def load_articles(filepath):
    df = pd.read_csv(filepath)
    return df.to_dict('records')

def main():
    articles = load_articles('data/articles.csv')
    graph = ArticleGraph()
    
    for article in articles:
        graph.add_article(article['title'], article['content'], article['category'])
    
    query = "elections"
    print("Articles found:", retrieve_articles(graph, query))

if __name__ == "__main__":
    main()
