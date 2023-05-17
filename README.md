# Surgical-Tool-Detection

# File Legend
`converter.py` converts the XML annotations to txt annotations
\
\
`Report.pdf` contains the Report
\
\
`yolov7` is the complete model details
\
\
`slides` contains the .ppt files used to present the updates

# Training
Clone/Download the github repo to your device and open the root in terminal. Run the below command in terminal
\
\
`python3 runner.py`

# Testing
When you train the model using above command, a weights-folder `best.pt` gets installed at `runs/train/yolov7-v1/weights`. Otherwise
download the weight folder [best.pt](https://github.com/Likhith-2914/Surgical-Tool-Detection/releases/download/weights/best.pt) directly from here and store
it in `runs/train/yolov7-v1/weights`.
\
Once you got the weights in the correct directory, run below command to test the model
`python3 tester.py`




