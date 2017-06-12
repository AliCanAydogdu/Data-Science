    #We've read story.txt into the string story_string, and used the replace() method to remove all periods (.) and commas (,). Next, add code that removes single quotes ('), semi-colons (;), and newline characters ("\n").
    f = open("story.txt", 'r')
    story_string = f.read()

    print(story_string)
    story_string = story_string.replace(".","")
    story_string = story_string.replace(",","")
    story_string = story_string.replace("'", "")
    story_string = story_string.replace(";", "")
    story_string = story_string.replace("\n", "")
    print(story_string)

    > Creating A Function That Cleans Text

    # Let's look at a simple function named clean_text() that replaces all commas (,) with blank spaces (""), and then returns the resulting string. Note that a blank space ("") is different from a single whitespace character (" "):

    f = open("story.txt", 'r')
    story_string = f.read()

    def clean_text(text_string):
        cleaned_string = text_string.replace(".","")

    cleaned_story = clean_text(story_string)
    # Solution code.
    def clean_text(text_string):
        cleaned_string = text_string.replace(".","")
        cleaned_string = cleaned_string.replace(",","")
        cleaned_string = cleaned_string.replace("'", "")
        cleaned_string = cleaned_string.replace(";", "")
        cleaned_string = cleaned_string.replace("\n", "")
        return(cleaned_string)
    cleaned_story = clean_text(story_string)

    > Changing Word Case

    # Modify the clean_text()function so that it converts cleaned_string to lowercase before returning it.

    def clean_text(text_string):
        cleaned_string = text_string.replace(",","")
        cleaned_string = cleaned_string.replace(".","")
        cleaned_string = cleaned_string.replace("'", "")
        cleaned_string = cleaned_string.replace(";", "")
        cleaned_string = cleaned_string.replace("\n", "")
        return(cleaned_string)
    cleaned_story = clean_text(story_string)
    def clean_text(text_string):
        cleaned_string = text_string.replace(",","")
        cleaned_string = cleaned_string.replace(".","")
        cleaned_string = cleaned_string.replace("'", "")
        cleaned_string = cleaned_string.replace(";", "")
        cleaned_string = cleaned_string.replace("\n", "")
        cleaned_string = cleaned_string.lower()
        return(cleaned_string)
    cleaned_story = clean_text(story_string)

    > Tokenizing The Story

    # Using functions to separate tasks spares us from having to write the same code in multiple places. It also makes it easier for others to understand our code. Doing this will become more important as our projects increase in complexity.

    def clean_text(text_string, special_characters):
        cleaned_string = text_string
        for string in special_characters:
            cleaned_string = cleaned_string.replace(string, "")
        cleaned_string = cleaned_string.lower()
        return(cleaned_string)

    clean_chars = [",", ".", "'", ";", "\n"]
    cleaned_story = clean_text(story_string, clean_chars)
    def tokenize(text_string, special_characters):
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)

    tokenized_story = tokenize(story_string, clean_chars)
    print(tokenized_story[0:10])

    > Finding Misspelled Words

    # Now that we have tokenized versions of both the story and the vocabulary, we can run our spell checker. Recall that we want to compare each word in the tokenized story with each word in the tokenized vocabulary, and return all tokens not found in the vocabulary.

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
