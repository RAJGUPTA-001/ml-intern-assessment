from src.ngram_model import NgramModel

def main():
    # Create a new TrigramModel
    model = NgramModel()

    # Train the model on the example corpus
    with open("data/example_corpus.txt", "r",encoding="utf-8") as f:
        text = f.read()
    model.fit(text)

    # Generate new text
    generated_text = model.generate()  # give min = number and max = number  to genereate minimum words even after end token  default max=50
    print("Generated Text:")
    print(generated_text)

if __name__ == "__main__":
    main()
