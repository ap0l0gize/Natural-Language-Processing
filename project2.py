import streamlit as st

st.set_page_config(page_title="Grammar Trainer")

st.title("Grammar Trainer")

# przymiotnik + rzeczownik
st.header("Step 1: Subject (S)")

number = st.radio("Choose number:", ["singular", "plural"], horizontal=True)

adjectives = [
    "tall", "strong", "happy", "young", "beautiful", "smart", "small", "round", "fast",
    "brave", "calm", "charming", "cheerful", "clever", "clumsy", "cool", "curious", "cute",
    "dark", "delightful", "eager", "elegant", "energetic", "enthusiastic", "friendly", "funny",
    "gentle", "glamorous", "graceful", "handsome", "happy-go-lucky", "honest", "innocent",
    "intelligent", "kind", "lazy", "light", "lively", "lonely", "lucky", "mature", "modern",
    "neat", "nervous", "nice", "obedient", "optimistic", "organized", "outgoing", "polite",
    "pretty", "proud", "quiet", "quick", "rare", "realistic", "reliable", "responsible",
    "rich", "romantic", "silly", "simple", "smart", "soft", "strong-willed", "stubborn",
    "stylish", "successful", "sweet", "talented", "tough", "trustworthy", "unique", "unusual",
    "upbeat", "useful", "victorious", "warm", "weak", "wise", "witty", "wonderful", "young-at-heart",
    "zealous", "adorable", "affectionate", "agile", "alert", "ambitious", "ancient", "angry",
    "anxious", "arrogant", "astonishing", "attractive", "average", "awesome", "awkward", "beautifully"
]

nouns = {
    "singular": ["man", "boy", "father", "teacher", "woman", "student", "girl", "mother", "cat", "dog"],
    "plural": ["men", "boys", "fathers", "teachers", "women", "students", "girls", "mothers", "cats", "dogs"],
}

# should we use adjective
use_adj = st.radio("Add an adjective?", ["yes", "no"], horizontal=True)

# display adjectives
selected_adj = None
if use_adj == "yes":
    selected_adj = st.selectbox("Choose an adjective:", adjectives)

# wybor przymiotnika w zaleznosci czy l poj czy mnoga
selected_noun = st.selectbox("Choose a noun:", nouns[number])

st.divider()

# wybor czasownika
st.header("Step 2: Verb (V)")

# czasowniki regularne (dla nieregularnych jest duzo ciezej)
verbs = [
    "accept", "add", "admire", "agree", "allow", "answer", "arrive", "ask", "bake", "balance",
    "bathe", "believe", "bless", "borrow", "brush", "build", "call", "camp", "change", "check",
    "clean", "climb", "close", "collect", "color", "compare", "complete", "connect", "copy",
    "count", "create", "dance", "deliver", "describe", "destroy", "develop", "divide", "dream",
    "drop", "enjoy", "examine", "exist", "explain", "fill", "follow", "form", "help", "hope",
    "identify", "imagine", "improve", "include", "inform", "insert", "invite", "join", "jump",
    "keep", "laugh", "learn", "listen", "look", "love", "manage", "match", "measure", "move",
    "need", "notice", "observe", "offer", "open", "order", "paint", "participate", "pass",
    "play", "practice", "prepare", "present", "protect", "prove", "push", "receive", "recognize",
    "release", "repair", "replace", "reply", "return", "save", "search", "share", "start",
    "study", "talk", "test", "train", "travel", "try", "turn", "use", "wait", "walk", "watch",
    "work", "write"
]

selected_verb = st.selectbox("Choose a verb:", verbs)
tense = st.selectbox("Choose tense:", ["present", "past", "future"])

st.divider()

# czy zdanie ma byc oznajmujace, pytajace, rozkazujace czy przypuszczajace
st.header("Step 3: Sentence Type")

sentence_type = st.radio(
    "Choose sentence type:",
    ["declarative", "interrogative", "imperative", "conditional"],
    horizontal=True
)

st.divider()

# budowanie zdania
if st.button("Build Sentence"):
    subject_text = ""
    if selected_adj:
        subject_text += f"{selected_adj} "
    subject_text += selected_noun

    verb_form = selected_verb

    if tense == "present":
        if number == "singular":
            if selected_verb.endswith("y"):
                verb_form = selected_verb[:-1] + "ies"
            elif selected_verb.endswith(("s", "sh", "ch", "x", "z")):
                verb_form = selected_verb + "es"
            else:
                verb_form = selected_verb + "s"
        else:
            verb_form = selected_verb
    elif tense == "past":
        if selected_verb.endswith("e"):
            verb_form = selected_verb + "d"
        else:
            verb_form = selected_verb + "ed"
    elif tense == "future":
        verb_form = "will " + selected_verb

    # budowanie zdania na podstawie typu
    sentence = ""
    if sentence_type == "declarative":
        sentence = f"The {subject_text} {verb_form}."
    elif sentence_type == "interrogative":
        if tense == "present":
            aux = "Does" if number == "singular" else "Do"
            sentence = f"{aux} the {subject_text} {selected_verb}?"
        elif tense == "past":
            sentence = f"Did the {subject_text} {selected_verb}?"
        elif tense == "future":
            sentence = f"Will the {subject_text} {selected_verb}?"
    elif sentence_type == "imperative":
        sentence = f"{selected_verb.capitalize()} the {subject_text}!"
    elif sentence_type == "conditional":
        if tense == "present":
            sentence = f"If the {subject_text} {verb_form}, it will be fine."  # Type 1
        elif tense == "past":
            sentence = f"If the {subject_text} {verb_form}, it would be fine."  # Type 2
        elif tense == "future":
            sentence = f"If the {subject_text} will {selected_verb}, it will be fine."

    st.success("Sentence built!")
    st.subheader(sentence)
