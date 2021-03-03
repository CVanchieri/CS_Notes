### imports ### 
import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np

### encode all the face images ###
def encoded_faces():
#looks through the facee_iamges folder and encodes all the faces ###
# returns a dict of (name, image encoded)
    encoded = {}
    for dirpath, dnames, fnames in os.walk("./face_images"): # look through each image in face_iamges folder 
        for f in fnames: 
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("face_images/" + f) # load each file 
                encoding = fr.face_encodings(face)[0] # get the face encoding 
                encoded[f.split(".")[0]] = encoding # split encoding add to dict

    return encoded

### encode image from file name ### 
def unknown_image(img):
    face = fr.load_image_file("face_images/" + img) # load the image file 
    encoding = fr.face_encodings(face)[0] # get the face encoding 

    return encoding

### find the faces and label in known ###
def search_face(im):
# param 'im' is str of file path
# returns a list of face names
    face_names = [] # create a list for the face names found 
    faces = encoded_faces() # set the function
    faces_encoded = list(faces.values()) # create a list of the encoded faces values 
    known_face_names = list(faces.keys()) # creat a list of the faces key values 
    img = cv2.imread(im, 1) # read in the image
    face_locations = face_recognition.face_locations(img) # find the face locations from the image 
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations) # find the unkown face encodings

    for face_encoding in unknown_face_encodings: # loop through  unkown face encodings
        # See if the face is a match for the known face(s)
        match_list = face_recognition.compare_faces(faces_encoded, face_encoding) # see if the face is a match 
        name = "Unknown" 
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding) # find face distances 
        best_match = np.argmin(face_distances) # find the smallest distance from known face to new face 
        if match_list[best_match]: # if a match 
            name = known_face_names[best_match] # set the name 
        face_names.append(name) # add the name to the list 

        ### create the visual face boxes and text ### 
        for (top, right, bottom, left), name in zip(face_locations, face_names): # loop through face_locations and face_names
            # Draw a box around the face
            cv2.rectangle(img, (left-20, top-20), (right+20, bottom+40), (0, 255, 0), 1) # set the box parameters 
            font = cv2.FONT_HERSHEY_DUPLEX # set the font 
            cv2.putText(img, name, (left -20, bottom +75), font, 1.0, (0, 0, 255), 2) # set the text parameters 

    ### return the image with face names if found ###
    while True: 
        cv2.imshow('Face Recgonition Results', img) # show the title and image 
        if cv2.waitKey(1) & 0xFF == ord('q'): # set wait key and q exit command 
            return face_names 

### run the function on the image to search ### 
# print(search
#_face('Barak_Joe.jpg')) # alternative example 
print(search_face('test_images/Jumanji_Cast.jpg'))


