from flask import Flask, render_template, Response
import cv2
import Virtual_tryOn

app = Flask(__name__, template_folder="templates")z\

def generate_frames():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()


@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/video',methods=['GET', 'POST'])
def video():
    return Response(Virtual_tryOn.Tryon(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
