import datetime
from flask import Flask, render_template, request
import database
import database1
import database2
import getYoutubeVideoLinks as getYT

import os
os.environ["EAI_USERNAME"] = 'pitabi1360@pashter.com'
os.environ["EAI_PASSWORD"] = 'Testqwerty1!'

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

# Output overall sentiment


app = Flask(__name__)

database.create_tables()
database1.create_table()
database2.create_tablee()

language= 'en'

videos = []

@app.route("/", methods=["GET", "POST"])
def home():
    
    if request.method == "POST":
        entry_content = request.form.get("content")
        output = client.specific_resource_analysis(body={"document": {"text":  entry_content}}, params={'language': language, 'resource': 'relevants'})
        database2.create_entryss(entry_content, datetime.datetime.today().strftime("%b %d"))
        for lemma in output.main_lemmas:
            print(lemma.value)
            video = getYT.searchVideoForKeyword(lemma.value)
            for indivvideo in video:
                database.create_entry(entry_content, datetime.datetime.today().strftime("%b %d"), indivvideo)
                videos.append(f'{indivvideo}')
 
    return render_template("home.html")



@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
          entry_contents = request.form.get("contents")
          output = client.specific_resource_analysis(body={"document": {"text": entry_contents}},params={'language': language, 'resource': 'sentiment'})
          
          database1.create_entrys(entry_contents, datetime.datetime.today().strftime("%b %d"), output.sentiment.overall)
          print(output.sentiment.overall)

    return render_template("feedback.html")




@app.route("/recommendation", methods=["GET", "POST"])
def recommendation():         
    return render_template('index.html', videos=videos, entries=database.retrieve_entries(), entrie=database2.retrieve_entriee())


@app.route('/negative', methods=["GET", "POST"])
def negative():
    return render_template("negative.html", entries=database1.retrieve_entrie())


@app.route('/positive', methods=["GET", "POST"])
def positive():
    return render_template("positive.html", entries=database1.retrieve_entrie())



