import os

from mmdet.apis import inference_detector, init_detector, show_result_pyplot
config = 'configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
checkpoint = 'work_dirs/faster_rcnn_r50_fpn_1x_coco/latest.pth'
device = 'cuda:0'
dataroot = '/home/aimmlab/Documents/hw2/mmdetection/data/VOCdevkit/VOC2007/test/'
model = init_detector(config, checkpoint, device)
with open('work_dirs/result_output10epochhw2.txt', 'w') as f:
    for i in range(1, 13069):
        result = inference_detector(model, dataroot+str(i)+'.png')
        for k in result:
            f.write(str(k.tolist())+'\n')

