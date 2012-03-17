import json

def analyze_review_sentiment(review, sentiments):
    average = 0
    sentiment=0
    word_count=0
    for word in review.split():
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

def star_from_sentiments(review, sentiments_table):
    return 3 + 2 * analyze_review_sentiment(review, sentiments_table)

def predict_reviews(review_data,sentiments_table):
    output = {}
    first_five_reviews = 50
    for raw_review in review_data:
        # Each line of the testing data is a JSON dictionary object containing a review record.6
        # Use simplejson's loads() function to parse this into a native Python dictionary.
        review = json.loads(raw_review)
        review_id = review.get('review_id', None)
        if review_id is None:
            continue
        review_text = review.get('text', None)
        guess = star_from_sentiments(review_text, sentiments_table)
        output[review_id] = guess
    print json.dumps(output)
    

    

def train_and_predict(training_filename, test_filename):
    sentiments_table = make_sentiments_table()

    with open(test_filename) as test_file:
        predict_reviews(test_file, sentiments_table)

if __name__ == '__main__':
    if len(argv) != 3:
        print("usage: %s training-data.json test-data.json" % argv[0])
    training_filename = argv[1]
    test_filename = argv[2]

    train_and_predict(training_filename, test_filename)
