from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__)

@app.route('/')
def welcome():
    # Render a welcome page with a download link
    html_content = '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Narayanpall</title>
      </head>
      <body>
        <h1>Arduino for Android</h1>
        <p><a href="/download-apk">Download ArduinoDroid</a></p>
      </body>
      </body>
      	<h1>Basic codes of Arduino</h1>
      	<p><a href="/download-codes">Download codes</a></p>
    </html>
    '''
    return render_template_string(html_content)

    
@app.route('/download-apk')
def download_apk():
	return send_from_directory('static', 'arduinodroid-6-3-1.apk', as_attachment=True)
@app.route('/download-codes')
def download_codes():	
    return send_from_directory('static', 'ide.zip', as_attachment=True)	

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
