import subprocess
import wandb

wandb.login(key="550c5ff8c6b0568f6e6f8f3255a9b03edaf889af")

train_cmd = "python3 yolov7/train.py --workers 8 --device 0 --epochs 20 --batch-size 16 --data yolov7/data/m2cai16toollocations.yaml --img 596 596 --cfg yolov7/cfg/training/yolov7-custom.yaml --weights '/home/kumar/riddhi/Likhith/PE/runs/train/yolov7-v1/weights/best.pt' --name yolov7-v2 --hyp yolov7/data/hyp.scratch.custom.yaml"

#train_aux_cmd = "python3 yolov7/train_aux.py --workers 8 --device 0 --epochs 30 --batch-size 8 --data yolov7/data/m2cai16toollocations.yaml --img 596 596 --cfg yolov7/cfg/training/yolov7-w6-custom.yaml --weights '' --name yolov7-custom --hyp yolov7/data/hyp.scratch.custom.yaml"

train_args = train_cmd.split(" ")
result = subprocess.run(train_args, stdout=subprocess.PIPE)

print(result.stdout.decode())

print("Trained normal model")


#train_aux_args = train_cmd.split(" ")
#result = subprocess.run(train_aux_args, stdout=subprocess.PIPE)

#print(result.stdout.decode())

#print("Trained aux model")
