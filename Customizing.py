The file dictionary.txt contains a sequence of correctly spelled words, which we'll use to seed the vocabulary. The file story.txt contains a piece of text with some misspelled words. We added the current version of the spell checker as we wrote it in the previous mission to the following code cell.

f = open("story.txt", 'r')
story_string = f.read()
vocabulary = open("dictionary.txt", "r").read()

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

misspelled_words = []
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)

for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)
print(misspelled_words)

Tokenizing the Text

# Default code
def tokenize(text_string, special_characters, clean=False):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

tokenized_story = []
tokenized_vocabulary = []
misspelled_words = []
# Answer code
def tokenize(text_string, special_characters, clean=False):
    # If `clean` is `True`.
    if clean:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)
    # If `clean` not equal to `True`, no cleaning.
    story_tokens = text_string.split(" ")
    return(story_tokens)

clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars, True)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)

for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)

Creating A More Compact Spell Checker

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters, clean=False):
    cleaned_text = text_string
    if clean:
        cleaned_text = clean_text(text_string, special_characters)
    tokens = cleaned_text.split(" ")
    return(tokens)

final_misspelled_words = []
def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    text = open(text_file).read()

    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)

    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)
