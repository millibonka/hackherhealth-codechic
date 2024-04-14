import csv
import requests
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
import numpy as np


api_key = ""
api_secret = ""
url = f'https://api.flickr.com/services/rest/'
data_file = 'flickr_data1.csv'
labels_file = "coco.names"
weights = "yolov4.weights"
config = "yolov4.cfg"
model = cv2.dnn.readNetFromDarknet(config,weights)
classes = open(labels_file).read().strip().split("\n")



def fetch_and_save_data(tag, total_photos):
    url = 'https://api.flickr.com/services/rest/'
    per_page = 100  # Number of results per page
    photos_collected = 0
    page = 1
    iterations = 0
    # Open CSV file for writing
    with open(data_file, mode='a', newline='') as csv_file:
        fieldnames = ['Photo URL', 'Date Taken', 'Latitude', 'Longitude', 'tag']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write header row only if the file is empty
        if csv_file.tell() == 0:
            writer.writeheader()

        while photos_collected < total_photos:
            iterations +=1
            print(f"Photos collected vs total photos: {photos_collected} : {total_photos}, iteration {iterations}")
            params = {
                'method': 'flickr.photos.search',
                'api_key': api_key,
                'tags': tag,
                'extras': 'url_o,date_taken,geo', 
                'format': 'json',
                'nojsoncallback': 1,
                'per_page': per_page,
                'page': page
            }

            response = requests.get(url, params=params)
            data = response.json()


            if data['stat'] == 'ok':
                photos = data['photos']['photo']
                num_photos = min(total_photos - photos_collected, len(photos))
                for i in range(num_photos):
                    photo = photos[i]
                    # get photo data
                    if 'url_o' in photo:
                        photo_url = photo['url_o']
                        photo_date = photo['datetaken']
                        photo_lat = photo['latitude'] if 'latitude' in photo else ''
                        photo_lon = photo['longitude'] if 'longitude' in photo else ''
                        # write photo data to CSV
                        writer.writerow({'Photo URL': photo_url, 'Date Taken': photo_date, 'Latitude': photo_lat, 'Longitude': photo_lon, 'tag': tag})
                        photos_collected += 1

                    if photos_collected == total_photos:
                        break  

                page += 1
            if iterations > 200:
                break
            else:
                print("Error:", data)
                break
    
def fetch_photo_from_path(img_path):
    with urllib.request.urlopen(img_path) as response:
        img_array = np.array(bytearray(response.read()), dtype=np.uint8)

    # Decode the image
    image = cv2.imdecode(img_array, -1)
    return image

def detect_humans(image):
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (608, 608), swapRB=True, crop=False)
    model.setInput(blob)
    ln = model.getLayerNames()
    ln = [ln[i-1] for i in model.getUnconnectedOutLayers()]
    layer_output = model.forward(ln)

    height, width, _ = image.shape
    detected_images = []
    confidence_scores = []
    classIDs = []

    for output in layer_output:
        #print(output)
        for detected in output:
            # print(detected)
            scores = detected[5:]
            classID = np.argmax(scores)
            confidence = scores[classID] # I found the confidence
            if confidence > 0.1 : 
                box = detected[0:4] * np.array([width,height,width,height])
                (center_x , center_y , box_width,box_height) = box.astype("int")
                # get (x,y) for top_left corner
                x = int((center_x - box_width/2))
                y = int((center_y - box_height/2))
                boxes.append([x , y , int(box_width) , int(box_height)])
                confidence_scores.append(float(confidence))
                classIDs.append(classID)
                print(classID)

                score_threshold = 0.9
        non_max_suppression_threshold = 0.9

        found_boxes = cv2.dnn.NMSBoxes(boxes,
                                    confidence_scores,
                                    score_threshold,
                                    non_max_suppression_threshold)

        return detected_images


def display(img,cmap=None):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)


