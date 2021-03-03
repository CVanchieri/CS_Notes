''' OpenCV face detection notes '''

### command line ###
# file to run ################# image for detecion #### deployment model text ############ which model to run # 
python3 detect_faces_image.py --image assets/groupclass_jump.jpg --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

### video facial detection, command line ###
# file to run ###################### deployment model text ############ which model to run # 
python3 detect_faces_video.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

