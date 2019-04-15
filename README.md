# Onportrait - Online face detection and Gallery

Simple API to process an image using OpenCV and return the face detections

## Install and Run
> - requisits: Python3.7
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python db_config.py
python run.py
```

## API
### Upload a image
Returns json data with image id and face coordinate.

- *URL*
```
POST /api/upload
```
- *Data Params*

> - Image file with extension {jpg, jpeg, png}

- *Success Response*:

> - Code: 200
> - Content: {data: {id: 1, faces: [{x: 100, y:11, width: 28, height: 28},]}}

- *Error Response*:
> - Code: 422 Unprocessable Entity
> - Content: {file_error: "file format not allowed"}

OR

> - Code: 500 SERVER ERROR
> - Content: {'errors': {'internal_error':'<message>'}

- *Exemple*:
```bash
curl -i -X POST -H "Content-Type: multipart/form-data" 
-F "file=/path/to/image" http://0.0.0.0/api/upload/
```

### Get an image tagged
Send a image binnary with the face identified.

- *URL*
```
GET /api/get/portrait/image/<int:image_id>
```
- *Data Params*

> - url image id

- *Success Response*:

> - Code: 200
> - Content: ""

- *Error Response*:
> - Code: 500 SERVER ERROR
> - Content: {'errors': {'internal_error':'<message>'}
