from flask import Flask, render_template, render_template_string
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route('/test_report')
def test_report():
    html_path = '/html_test/linkseq-main-hboc-all.html'
    with open(html_path) as fid:
        source = fid.read()
        return render_template_string(source)
