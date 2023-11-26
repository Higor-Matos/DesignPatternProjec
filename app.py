from flask import Flask, render_template, request
from article_fetchers import FetcherFactory

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    search_type = None

    if request.method == 'POST':
        query = request.form.get('query')
        search_type = request.form.get('search_type')
        factory = FetcherFactory()
        fetcher = factory.get_fetcher(search_type)  # Uso do Factory Method
        result = fetcher.fetch(query)

    return render_template('index.html', result=result, search_type=search_type)


if __name__ == '__main__':
    app.run(debug=True)
