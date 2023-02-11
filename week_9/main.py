from flask import Flask, render_template, Response
from camera import VideoCamera
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')                                                                     #render home.html

@app.route('/cool')
def index():
    return render_template('index.html')                                                                      #render index.html

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'                                                   
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_frame')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')       #mimetype is for the browser, we are basically letting browser know what type of file it is


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)