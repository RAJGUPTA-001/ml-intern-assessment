import random
import numpy as np
from collections import defaultdict
from src.utils import preprocess , make_dict , getcounts
from nltk.tokenize import word_tokenize
class NgramModel:
    def __init__(self, n = 3 ):
        """
        Initializes the TrigramModel.
        """
        if n <= 1:
           raise ValueError("n must be greater than 1 for an n-gram model.")
        # TODO: Initialize any data structures you need to store the n-gram counts.
        self.n = n
        # Nested dictionary: counts[w1][w2][w3] = count of trigram (w1, w2, w3)
        self.counts = make_dict(n)
        # Context counts: context_counts[w1][w2] = total count of context (w1, w2)
        self.context_counts = make_dict(n-1)
        self.vocab = set()
        self.vocab_size = 0
        self.start_token = "__start__"
        self.unk_token = "__UNK__"
        self.end_token = "__end__"
        

    def fit(self, text):
        """
        Trains the trigram model on the given text.

        Args:
            text (str): The text to train the model on.
        """
        text = f"{self.start_token} " * (self.n - 1) + text + f" {self.end_token}"
        text = preprocess(text)
        words = word_tokenize(text)
        # self.vocab.update(words)
        # self.vocab_size=len(self.vocab)
        getcounts(words,self.n,self.counts,self.context_counts)
        # print(self.counts)
        # print(self.context_counts)


    def sample_next_word(self, context):
        """
        Given a context tuple, sample the next word based on empirical probabilities
        from self.counts and self.context_counts.

        Args:
            context (tuple): The (n-1)-gram context

        Returns:
            str: Sampled next word (from the model's vocabulary)
        """
        # print(context)
        # Get the counts for all possible next words for this context
        next_word_counts = self.counts.get(context)
        # print(next_word_counts)
        if not next_word_counts:
            # If context not in model, could return random word or <UNK>
            return "__UNK__"

        words = []
        probs = []
        total = self.context_counts.get(context, 0)
        for word, count in next_word_counts.items():
            words.append(word)
            probs.append(count / total)
        probs = np.array(probs)
        probs = probs / probs.sum() 
        # Sample using numpy:
        return np.random.choice(words, p=probs)

    def generate(self, min = 0  ,text="",max=50):
        """
        Generates new text using the trained trigram model.

        Args:
            max_length (int): The maximum length of the generated text.

        Returns:
            str: The generated text.
        """
        # TODO: Implement the generation logic.
        # This will involve:
        # 1. Starting with the start tokens.
        # 2. Probabilistically choosing the next word based on the current context.
        # 3. Repeating until the end token is generated or the maximum length is reached.
       
        text = word_tokenize(preprocess(text)) if text else []
        
        if len(text) < self.n - 1:
            text = [self.start_token] * (self.n - 1 - len(text)) + text
        text = text[-2:]
        if min == 0: 
            for _ in range(max):
                context = tuple(text[-(self.n - 1):])
                next_word = self.sample_next_word(context)
                if next_word == self.end_token:
                    
                    return " ".join(text[2:])
                text.append(next_word)
            return " ".join(text[2:])
        else:
            word_count = 0
            for _ in range(1000):  # safety to prevent infinite loop
                context = tuple(text[-(self.n - 1):])
                next_word = self.sample_next_word(context)
                text.append(next_word)
                if next_word != self.end_token:
                    word_count += 1
                if word_count >= min and next_word == self.end_token or word_count >= max:
                    break
            return " ".join(text[2:])





