import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Function to summarize text
def summarize_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)

    # Create a frequency table to keep the score of each word
    freq_table = {}
    for word in word_tokens:
        word = word.lower()
        if word not in stop_words:
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1

    # Tokenize the sentences
    sentences = sent_tokenize(text)
    sentence_value = {}

    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq

    # Calculate the average value of a sentence
    sum_values = sum(sentence_value.values())
    average_value = int(sum_values / len(sentence_value))

    # Create the summary
    summary = ''
    for sentence in sentences:
        if sentence in sentence_value and sentence_value[sentence] > 1.5 * average_value:
            summary += " " + sentence

    return summary

# Example usage
if __name__ == "__main__":
    input_text ="Your lengthy article goes here. You can replace this text with the content you want to summarize. Make sure that you have more than one sentence to get a good summary."
    summary = summarize_text(input_text)
    print("Original Text:\n", input_text)
    print("\nSummary:\n", summary)