from flask import Flask, render_template, request
import os
import cv2
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# Directory to store uploaded files
UPLOAD_FOLDER = '/home/akhildasyam/thesis/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

#if upload folder doesnt exists, then create it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Simulate image transfer to localhost (your PC)
def upload_to_localhost(image_path):
    # Simulate the transfer process
    # In a real scenario, you would implement the transfer logic here
    print(f"Transferring image from {image_path} to localhost")
    return True

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Use ThreadPoolExecutor to simulate image transfer in the background
            with ThreadPoolExecutor() as executor:
                future = executor.submit(upload_to_localhost, filepath)
                success = future.result()

            if success:
                result = "Image uploaded and transfer simulation completed successfully."
            else:
                result = "Image uploaded, but there was an issue during the transfer simulation."

            return render_template('result.html', result=result)

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
