import subprocess


weights = "runs/train/yolov7-v1/weights/best.pt"
source = "videos/chole1small.mp4"
cmd = "python yolov7/detect.py --weights " + weights +  " --conf 0.25 --img-size 640 --source " + source

args = cmd.split(" ")
result = subprocess.run(args, stdout=subprocess.PIPE)

