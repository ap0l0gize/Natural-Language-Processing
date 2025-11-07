from matplotlib import pyplot as plt
import networkx as nx


#read and decode text
def read_and_decode(filename, encoding="utf-8"):
    with open(filename, 'r', encoding=encoding) as f:
        text = f.read()
    return text

def remove_punctuation(language_corpus):
    return [word.lower() for word in language_corpus if word.isalpha()]

def plot_zipf_law(ranks, frequencies):
    plt.figure(figsize=(8,5))
    plt.loglog(ranks, frequencies)
    plt.xlabel("Rank (r)")
    plt.ylabel("Frequency (f)")
    plt.title("Zipf's Law - log-log plot")
    plt.grid(True)
    plt.show()

# How many words do you have to know in order to learn 90% of language?
def num_words_for_knowing_fraction_of_language(word_frequencies, total_words, fraction_of_knowledge=0.9):

    cumulative_coverage = 0
    word_count = 0

    for frequency in word_frequencies:
        cumulative_coverage += (frequency / total_words)
        word_count += 1
        if cumulative_coverage >= fraction_of_knowledge:
            break
    return word_count

def draw_word_graph(words_no_punc_in_text, amount_of_words_plotted = 10):
    neighbors_dict = {}

    for index, word in enumerate(words_no_punc_in_text):
        if word not in neighbors_dict:
            neighbors_dict[word] = []
        if index - 1 >= 0:
            neighbors_dict[word].append(words_no_punc_in_text[index - 1])
        if index + 1 < len(words_no_punc_in_text):
            neighbors_dict[word].append(words_no_punc_in_text[index + 1])

    # get rid of duplicates
    for word in neighbors_dict:
        neighbors_dict[word] = list(set(neighbors_dict[word]))

    # Create an empty graph
    neighbors_graph = nx.Graph()

    for word, word_neighbors in neighbors_dict.items():
        if word not in neighbors_graph:
            neighbors_graph.add_node(word)
        for neighbor in word_neighbors:
            if word != neighbor:
                neighbors_graph.add_edge(word, neighbor)

    # Draw the graph
    plt.figure(figsize=(15, 15))

    degrees = dict(neighbors_graph.degree())

    top_connected_words = sorted(degrees, key=degrees.get, reverse=True)[:amount_of_words_plotted]

    neighbors_subgraph = neighbors_graph.subgraph(top_connected_words)
    nx.draw(neighbors_subgraph, with_labels=True, node_size=50, alpha=0.5)
    plt.show()
    return neighbors_subgraph # if the graph would be needed at some point