import subprocess

train_weights = "runs/train/yolov7-v1/weights/best.pt"
#train_aux_weights = "runs/train/yolov7-custom2/weights/best.pt"


test_cmd = "python yolov7/test.py --data yolov7/data/m2cai16toollocations.yaml --img 596 --task test --batch 16 --conf 0.001 --iou 0.65 --device 0 --weights " +train_weights + " --name yolov7_v1"


test_args = test_cmd.split(" ")
result = subprocess.run(test_args, stdout=subprocess.PIPE)

print(result.stdout.decode())

