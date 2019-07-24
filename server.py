#install these 
import json
import http.server
import socketserver
# run pip install --upgrade "ibm-watson>=3.0.3"
from ibm_watson import ToneAnalyzerV3

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    #call file and function 
    #Sentiment asnalysis using watson
    #FILL BELOW OUT
    service = tone_analyzer = ToneAnalyzerV3(
        version='{version}',
        username='{username}',
        password='{password}',
        url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )

    text = 'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    print(json.dumps(tone_analysis, indent=2))
        

    httpd.serve_forever() 
