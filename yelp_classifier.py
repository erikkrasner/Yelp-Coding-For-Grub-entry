import json

def analyze_review_sentiment(review, sentiments):
    average = None
    sentiment=0
    word_count=0
    for word in tweet_words:
        if word in sentiments:
            sentiment += sentiments[word]
            word_count+=1
    if word_count>0:
        average=sentiment/word_count
    return average

def make_sentiments_table():
    sentiments_table = {}
    for line in open('sentiments.csv'):
	word, sentiment = line.split(',')
	sentiment = float(sentiment)
	sentiments_table[word] = sentiment
    return sentiments_table
        

def train_and_predict(training_filename, test_filename):
    with open(training_filename) as training_file:
        user_averages, business_averages = generate_model(training_file)

    with open(test_filename) as test_file:
        predict_reviews(test_file, user_averages, business_averages)

if __name__ == '__main__':
    if len(argv) != 3:
        print("usage: %s training-data.json test-data.json" % argv[0])
    training_filename = argv[1]
    test_filename = argv[2]

    
    train_and_predict(training_filename, test_filename)
