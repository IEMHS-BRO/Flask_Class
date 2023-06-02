import os
import uuid
from werkzeug.utils import secure_filename
from flask import current_app, url_for

'''
이미지 저장
'''
def save_image(file):
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # 랜덤한 파일명 생성
    random_filename = str(uuid.uuid4())
    filename = secure_filename(file.filename)
    _, ext = os.path.splitext(filename)
    saved_filename = random_filename + ext

    file_path = os.path.join(upload_folder, saved_filename)
    file.save(file_path)
    return url_for('static', filename=saved_filename)

'''
이미지 삭제
'''
def delete_image(file_url):
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    filename = os.path.basename(file_url)
    file_path = os.path.join(upload_folder, filename)
    
    if os.path.exists(file_path):
        os.remove(file_path)