from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Initialize the camera
camera = cv2.VideoCapture(0)

def gen_frames():
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # Read a frame from the camera
        if not success:
            break
        else:
            # Convert the frame to JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                break
            # Convert the buffer to bytes and yield it for the video stream
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
