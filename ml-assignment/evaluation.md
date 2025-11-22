# Evaluation

Please provide a 1-page summary of your design choices for the Trigram Language Model.

This should include:

- How you chose to store the n-gram counts.

They are stored in a nested dictionary.
The module is designed to take input the number n for any ngram model , it dynamically adapts.
The object while initialization takes an argument n for the ngram model (defaults to 3 & not configured for 1).
To change any data you want to train on change the data\example_corpus.txt , by default it has two books data 
one from alice and one from the book by charles dickens.
 
- How you handled text cleaning, padding, and unknown words.

The preprocess function from the src/utils.py 
removes any extra dots spaces or urls if there are  and then sets __end__ token for the EOL and EOP.
then lowercase it.
Then in the src/ngram_model.py the fit function tokenize it then uses the getcounts function  to get the 
dict of counts for prediction (bigram and trigram or any general n gram counts)
 
- How you implemented the `generate` function and the probabilistic sampling.

generate function uses the   sample_next_words from same file to get the next word using the generated 
probabilities , as required , it doesnt choose the most possible words  , but uses numpy to get  words 
randomly based on the probability of that word . for example - if "next" comes 5/10 and "another" comes 3/10 and "second" comes 2/10 times 
then during generation this probabillity is maintained by choosing the words based on these probabilitys not by
max probability each time.


- Any other design decisions you made and why you made them.

Created it to work as a general ngram model not just 3.

Inserted end token after end of para to make it end on para and line (although it introduced new bug that makes it stop nuch early , CAN be improved).




 
