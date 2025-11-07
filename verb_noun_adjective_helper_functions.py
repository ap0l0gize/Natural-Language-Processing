from itertools import islice
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt


def chunk_text(language_text, chunk_size=500_000):
    for index in range(0, len(language_text), chunk_size):
        yield language_text[index:index + chunk_size]

def extract_pairs(doc):
    adj_noun_pairs = Counter()
    verb_noun_pairs = Counter()

    for sent in doc.sents:
        adjs = [t.lemma_.lower() for t in sent if t.pos_ == "ADJ" and t.is_alpha]
        nouns = [t.lemma_.lower() for t in sent if t.pos_ == "NOUN" and t.is_alpha]
        verbs = [t.lemma_.lower() for t in sent if t.pos_ == "VERB" and t.is_alpha]

        for adj in adjs:
            for noun in nouns:
                adj_noun_pairs[(adj, noun)] += 1
        for verb in verbs:
            for noun in nouns:
                verb_noun_pairs[(verb, noun)] += 1

    return adj_noun_pairs, verb_noun_pairs


def get_color_for_frequency(frequency):
    if frequency == 0:
        return "red"
    elif frequency == 1:
        return "yellow"
    elif frequency < 10:
        return "green"
    else:
        return "blue"

def build_bipartite_graph(pairs_counter, top_node_amount=50):
    bipartite_graph = nx.Graph()
    # islice for efficiency, could do [:top_node_amount] but that entails list construction
    for(left, right), frequency in islice(pairs_counter.most_common(top_node_amount), top_node_amount):
        # 0 means one side of the graph 1 means the other
        bipartite_graph.add_node(left, bipartite=0)
        bipartite_graph.add_node(right, bipartite=1)
        bipartite_graph.add_edge(left, right, weight=frequency, color=get_color_for_frequency(frequency))
    return bipartite_graph

def plot_bipartite_graph(bipartite_graph):
    pos = nx.spring_layout(bipartite_graph, iterations=50)
    edge_colors = [bipartite_graph[u][v]["color"] for u, v in bipartite_graph.edges()]

    plt.figure(figsize = (12,10))

    nx.draw(
        bipartite_graph,
        pos=pos,
        with_labels=True,
        node_color="lightgrey",
        edge_color=edge_colors,
        font_size=8,
        node_size=200,
        alpha=0.8
    )
    plt.show()