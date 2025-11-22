# Trigram Language Model

This directory contains the core assignment files for the Trigram Language Model.

## How to Run 

### Setup

Clone the repo

```bash
git clone copy_the_link_from_github
cd ml-intern-assessment
```

Create a venv ( Optional but recommended) 
```bash
python -m venv venv
venv/Scripts/activate
```

Install the requirements. 

```bash
pip install -r requirements.txt 
```
Now  you can test it using 

```bash
pytest ml-assignment/tests/test_ngram.py
```

Or use the Generate file to generate text.

```bash
cd ml-assignment
python -m src.generate
```

As it is expected to stop at an end token, and the eol and para endings are treated as an endtoken while 

preprocessing and model train so the end token is very much possible .

to get longer results try changing the generate function in the generate.py file , it takes as argument min 

and max to configure the output token. It is by default set to use max=50.



## Design Choices

Check the evaluation.md file

