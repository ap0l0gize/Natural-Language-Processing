import nltk
import language_processing_functions as lpf
from nltk.probability import FreqDist

if __name__ == '__main__':

    nltk.download('punkt')
    nltk.download('punkt_tab')

    words = lpf.read_and_decode()

    words_no_punc = lpf.remove_punctuation(words)
    total_words_in_text = len(words_no_punc)

    f_words_no_punc = FreqDist(words_no_punc)
    frequencies = sorted(f_words_no_punc.values(), reverse=True)
    ranks = range(1, len(frequencies) + 1)

    num_of_words = lpf.num_words_for_knowing_fraction_of_language(frequencies, total_words_in_text)
    most_common_words = f_words_no_punc.most_common(num_of_words)

    lpf.plot_zipf_law(ranks, frequencies)

    print(f"Number of words in the text (with punctuation): {len(words)}")
    print(f"Number of words without punctuation: {total_words_in_text}")
    print(f"Number of words needed to learn 90% of language: {num_of_words}")


    most_connected_words_graph = lpf.draw_word_graph(words_no_punc, 20)