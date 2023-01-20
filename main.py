from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def search4letters(phrase: str, letters: str) -> set:
    res = set(letters).intersection(set(phrase))
    if len(res)==0:
        return 'Your phrase is empty!'

# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters =  request.form['letters']   
    return render_template('results.html',
        the_title='Here are your results',
        the_phrase=phrase,
        the_letters=letters,
        the_results=str(search4letters(phrase, letters)))

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title = 'Welcome to search4letters on the Web')


@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as  log:
        contents = log.read()
    return contents


app.run(debug=True)