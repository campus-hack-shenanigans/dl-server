"""Main file of the server implementation."""
import subprocess
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def run_model(word,temp,poems_count):
    module_path = "'../dl-model/cv/model.p'"
    sample_path = "../dl-model/sample.py"
    args = ['python2.7',sample_path ,'-m',str(module_path),'-t',str(temp),'-s',str(word),'-n',str(poems_count),'-o',"0"]
    result = subprocess.run(args, stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')
    return result

@app.route('/lyrics', methods=["POST"])
def post_lyrics():
    word = request.form["word"]
    temp = request.form["temp"]
    poems_count =  request.form["poems_count"]
    model_output = run_model(word,temp,poems_count)
    return model_output


if __name__ == '__main__':
    app.run()



