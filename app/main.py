#from azureml.deploy import DeployClient

from flask import Flask
from flask import render_template
#import cpudriver 
import tempDriver

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/testpage')
def test():
  return 'Hello from test route!'

#@app.route('/<string:page_name>/')
#def render_static(page_name):
#    return render_template('%s.html' % page_name)

@app.route('/helloworld')
@app.route('/helloworld/')
def render_static(pageName=None):
    #for runIndex in range(100):
    #  cpudriver.GenerateArrayAndHash()
    tempDriver.Drive()
    return render_template('helloworld.html', name=pageName)


if __name__ == '__main__':
      app.run()