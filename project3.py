import spacy
import language_processing_functions as lpf
import os
from collections import Counter
import verb_noun_adjective_helper_functions as vhf
# from spacy.cli import download
# spacy.cli.download('en_core_web_sm') # if not downloaded

nlp = spacy.load("en_core_web_sm", disable=["ner", "parser"])
nlp.add_pipe("sentencizer")
nlp.max_length = 6_000_000

base_dir = os.path.dirname(__file__)
language_corpus = os.path.join(base_dir, 'language_data', 'englishCorpus.txt')

text = lpf.read_and_decode(language_corpus)

total_adj_noun_pairs = Counter()
total_verb_noun_pairs = Counter()

print("Starting ...")
for i, part in enumerate(vhf.chunk_text(text)):
    doc = nlp(part)
    adj_pairs, verb_pairs = vhf.extract_pairs(doc)
    total_adj_noun_pairs.update(adj_pairs)
    total_verb_noun_pairs.update(verb_pairs)
    print(f"Processed chunk {i + 1}")

print("===================")
print("Top 10 adjective-noun pairs:")
for pair, freq in total_adj_noun_pairs.most_common(10):
    print(f"{pair}: {freq}")
print("===================")
print("Top 10 verb-noun pairs:")
for pair, freq in total_verb_noun_pairs.most_common(10):
    print(f"{pair}: {freq}")


adj_graph = vhf.build_bipartite_graph(total_adj_noun_pairs)
verb_graph = vhf.build_bipartite_graph(total_verb_noun_pairs)

vhf.plot_bipartite_graph(adj_graph)
vhf.plot_bipartite_graph(verb_graph)
