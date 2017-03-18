import sys
from flask import Flask, session
from github import Github

app = Flask(__name__)

def main_pr():
    global gitUser
    global gitRepo
    inputURL=sys.argv[1]
    myList=inputURL.rsplit('/',2)
    # session['github_user']=myList[1]
    # session['github_rep']=myList[2]
    gitUser = myList[1]
    gitRepo = myList[2]
@app.route('/v1/<getfilecontent>')
def index(getfilecontent):
    output_file = None
    global gitRepo
    global gitUser
    github = Github() 
    getUser = github.get_user(gitUser)
    getRepo = getUser.get_repo(gitRepo)
    rawFile = getRepo.get_file_contents(getfilecontent)
    output_file= rawFile.decoded_content
    return output_file


if __name__ == "__main__":
    main_pr()
    app.run(debug=True,host='0.0.0.0')