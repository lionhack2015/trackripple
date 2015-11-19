from os import path

STOP_WORD_FILE = "stopwords"

#sample
text = open("sample.txt").read().strip()

# GLOBAL LIST OF WORDS IN LEARNING SET
# change these to class variables later
ALL_WORDS = {}
WORD_COUNT = 0

def read_stop_words(file):
	""" reads stop words from a file
	and returns a dictionary to enable efficient searching
	"""
	stop_words = {}
	sw_file = open(file)
	line = sw_file.readline()
	while line:
		word = line.strip()
		stop_words[word] = word
		line = sw_file.readline()
	return stop_words


def extract_bag_of_words_features(text, swd):
    """ ingests blog text and returns a boolean
    bag of words vector representation of the document
    Also populates ALL_WORDS in situ

    text: blog text
    swd: stop word dictionary
    """
    # change case to lower
    # remove stop words
    global WORD_COUNT
    global ALL_WORDS
    features = [0]*WORD_COUNT
    for line in text.split("."):
        line = line.strip()
        words = line.split(" ")
        for w in words:
            if len(w)==0 or w in swd:
                continue
            w = w.lower().rstrip(',')
            if w not in ALL_WORDS:
                WORD_COUNT = WORD_COUNT + 1
                ALL_WORDS[w] = WORD_COUNT
                features.append(1)
            else:
                index = ALL_WORDS[w]
                features[index] = 1     # think about using word counts instead of booleans here

    # stemming? (not always helpful ... think later)

    return features

swd = read_stop_words(STOP_WORD_FILE)
extract_bag_of_words_features(text, swd)


#def extract_echonext_features(signals):






