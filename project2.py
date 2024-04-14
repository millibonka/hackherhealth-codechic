# Image Classification class using YOLO
# Milena Miernik 
# project for course in Applied AI @ Teknikhögskolan, Göteborg

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime
import urllib.request

class ImageClassification:
    def __init__(self, image_path:str = None, image_url:str = None, video_path:str = None, idnr:str=None):
        self.idnr = idnr
        try:
            self.classes = open(r"coco.names").read().strip().split("\n")
            weights = r"yolov4.weights"
            config = r"yolov4.cfg"       
            self.model = cv2.dnn.readNetFromDarknet(config,weights)
            print("Model loaded successfully.")     
        except FileNotFoundError:
            print("YOLO config files could not be loaded.")
        else:
            self.detected_images = {}    
            if image_path:
                self.image = cv2.imread(image_path)
                if self.image is None:
                    print(f"Error loading the image. Incorrect path {image_path}.")
                else:
                    print("Image loaded successfully.")
                    self.height, self.width, self.colors = self.image.shape
                    self.detect_objects()
            elif video_path:
                self.cap = cv2.VideoCapture(video_path)
                if self.cap.isOpened():
                    print("Video loaded successfully.")
                    self.video_processing()
                else:
                    print(f"Video path '{video_path} is incorrect.")
            elif image_url:
                self.image = ImageClassification.fetch_photo_from_path(image_url)
                self.height, self.width, self.colors = self.image.shape
                self.detect_objects()
            else:
                print("You must provide either image_path or video_path.")
    @staticmethod
    def fetch_photo_from_path(img_path):
        with urllib.request.urlopen(img_path) as response:
            img_array = np.array(bytearray(response.read()), dtype=np.uint8)

        # Decode the image
        image = cv2.imdecode(img_array, -1)
        return image

    def detect_objects(self, video:bool=False):
        self.blob_conversion()
        self.define_output_layer()
        self.prepare_output_boxes()
        self.generate_found_boxes()
        if video:
            self.save_cropped_images(video=True)

        else:
            self.save_cropped_images()
            print(f"{len(self.detected_images)} images have been saved to {os.getcwd()}\output_folder.")
            
    def blob_conversion(self):
        self.blob = cv2.dnn.blobFromImage(self.image, 
                         1/255.0, 
                         (608,608), 
                         swapRB = True, 
                         crop = False) 

    def define_output_layer(self):
        ln = self.model.getLayerNames()
        ln = [ln[i-1] for i in self.model.getUnconnectedOutLayers()]
        self.model.setInput(self.blob) 
        self.layer_output = self.model.forward(ln)
    
    def prepare_output_boxes(self):
        self.boxes = []
        self.confidence_scores = []
        self.classIDs = []
        for output in self.layer_output:
            for detected in output:
                scores = detected[5:]
                classID = np.argmax(scores)
                confidence = scores[classID] 
        
                if confidence > 0.1 : 
                    box = detected[0:4] * np.array([self.width,self.height,
                                                    self.width,self.height])
                    (center_x , center_y , box_width,box_height) = box.astype("int")
                    # get (x,y) for top_left corner
                    x = int((center_x - box_width/2))
                    y = int((center_y - box_height/2))
                    self.boxes.append([x , y , int(box_width) , int(box_height)])
                    self.confidence_scores.append(float(confidence))
                    self.classIDs.append(classID)
    
    def generate_found_boxes(self):
        score_threshold = 0.9
        non_max_suppression_threshold = 0.9

        self.found_boxes = cv2.dnn.NMSBoxes(self.boxes,
                                    self.confidence_scores,
                                    score_threshold,
                                    non_max_suppression_threshold)
    
    def choose_folder(self,label):
        categories = {
            'Human': ['person'],
            'Vehicles': ['bicycle', 'car', 'motorbike', 'aeroplane', 'bus',
                         'train', 'truck', 'boat'],
            'Animal': ['bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
                       'elephant', 'bear', 'zebra', 'giraffe'],
            'Sport and Lifestyle': ['backpack', 'umbrella', 'handbag',
                                    'tie', 'suitcase', 'frisbee', 'skis',
                                    'snowboard', 'sports ball', 'kite',
                                    'baseball bat', 'baseball glove', 
                                    'skateboard', 'surfboard', 'tennis racket'],
            'Kitchen Stuff': ['bottle', 'wine glass', 'cup', 'fork', 'knife', 
                              'spoon', 'bowl'],
            'Food': ['banana', 'apple', 'sandwich', 'orange', 'broccoli', 
                     'carrot', 'hot dog', 'pizza', 'donut', 'cake'],
            'In House Things': ['chair', 'sofa', 'pottedplant', 'bed', 
                                'diningtable', 'toilet', 'tvmonitor', 'laptop',
                                'mouse', 'remote', 'keyboard', 'cell phone',
                                'microwave', 'oven', 'toaster', 'sink',
                                'refrigerator', 'book', 'clock', 'vase', 
                                'scissors', 'teddy bear', 'hair drier', 
                                'toothbrush']
            
        }
        
        for category, labels in categories.items():
            if label in labels:
                return os.path.join(os.getcwd(), f"output_folder\{category}")
        # if no label found in dictionary, returns MISC category
        return os.path.join(os.getcwd(), f"output_folder\MISC")
        
    def save_cropped_images(self, video:bool=False):
        if len(self.found_boxes) > 0: 
            for index in self.found_boxes.flatten():
                (x, y, width, height) = (self.boxes[index][0], self.boxes[index][1], 
                                        self.boxes[index][2], self.boxes[index][3])

                if width > 0 and height > 0 and x > 0 and y > 0:
                    image_copy = self.image.copy()
                    cropped_image = image_copy[y:y+height, x:x+width]
                    cropped_image_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
                    label = self.classes[self.classIDs[index]]

                    if label == "person":
                        print("Saving a human")
                        # create a folder for the label if it doesn't exist
                        folder_path = self.choose_folder(label)
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)    
                        if video:
                            filename = f"{label}_{index}_frame{self.current_frame}.jpg"
                            output_path = os.path.join(folder_path, filename)
                            cv2.imwrite(output_path, cropped_image)
                        else: 
                            filename = f"{self.idnr}_{index}.jpg"
                            output_path = os.path.join(folder_path, filename)
                            cv2.imwrite(output_path, cropped_image)

                        # appending it to the dictionary
                        self.detected_images[index] = (cropped_image_rgb, label)

            if video: # clearing the dictionary for the next frame to be processed
                self.detected_images = dict()
                
    def show_saved_images(self):
        if len(self.detected_images) > 0:
            for img in self.detected_images.values():
                fig = plt.figure(figsize=(2, 2))
                plt.imshow(img[0])
                plt.title(img[1])
                plt.axis("off")
                plt.show()
    
    def video_processing(self):
        self.current_frame = 0
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            self.image = frame
            self.current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            self.height, self.width, self.colors = self.image.shape
            self.detect_objects(video=True)
        print(f"Your images have been saved to {os.getcwd()}\output_folder.")
        self.cap.release()
