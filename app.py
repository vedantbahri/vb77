from flask import Flask, request, render_template
from gensim.models import Word2Vec

# Load the trained Word2Vec model
model = Word2Vec.load("word2vec.model")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    opposite_word = None
    if request.method == 'POST':
        # Get the input word from the form
        word = request.form['word']
        # Using the model to find the most similar word (this example assumes the first result is the antonym)
        similar_words = model.wv.most_similar(positive=[], negative=[word], topn=1)
        opposite_word = similar_words[0][0] if similar_words else "Not found"
    return render_template('index.html', word=request.form.get('word'), opposite_word=opposite_word)

if __name__ == '__main__':
    app.run(debug=True)
