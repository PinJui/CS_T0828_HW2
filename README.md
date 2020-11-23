# CS_T0828_HW2

Digit Detection on SVHN(Street View House Numbers) Dataset

## Content

- [Introduction](#introduction)
- [Methodology](#methodology)
- [Results](#results)
- [Reference](#reference)

## Introduction

This homework requires to train a digit detector to detect the digits inside a given image.

The given dataset is a subset of SVHN<a href="#[1]"> [1] </a>dataset, which has 33042 training images and 13068 test image of Format 1 in the SVHN.

Image Example:

<img src="https://raw.githubusercontent.com/PinJui/CS_T0828_HW2/main/assets/train_1.png" width="200" height="100">

The desired result is the detected digits recorded as a list of dictionary, which each dictionary corresponds to one test image.

The dictionary has three keys:
- "bbox": List of bounding boxes in (y1, x1, y2, x2). (top,left,right,bottom)
- "score": List of probability for the class of the detected digit
- "label": List of class of the detected digit, use class '10' for digit 0

Result Example(for test image 1.png):

```
{
 "bbox": [[6, 40, 39, 59]],
 "score": [0.9932959675788879],
 "label": [5]
}
```

## Methodology

Here I use the mmdetection toolbox<a href="#[2]"> [2] </a> to train the model.

#### Step 1: Dataset preprocessing

Use the file [load_data](https://github.com/PinJui/CS_T0828_HW2/blob/main/load_data.py)<a href="#[3]"> [3] </a> to generate the annotation file in pascal VOC xml format.

The example xml file is [here](https://github.com/PinJui/CS_T0828_HW2/blob/main/assets/1.xml)

Then reorganize the dataset as follow
```
├── dataset
│   ├── VOC2007
│   │   ├── Annotations
│   │   ├── JPEGImages
│   │   ├── ImageSets
│   │   │   ├── Main
│   │   │   │   ├── valid.txt
│   │   │   │   ├── train.txt
```
to fit the VOC training procedure in the mmdetection toolbox.

Put all the xml annotation file inside `Annotations` folder.

Then put all training and validation images inside `JPEGImages`

And also generate `train.txt` and `valid.txt` which writes the pure filename **(no path names)** of the trainging images and validation images

#### Step 2: Install mmdetection

Suppose the python enviroment is set(including installation of pytorch, cython and cuda etc. Then `cd` to your working directory and run `git clone https://github.com/open-mmlab/mmdetection.git` to install the mmdetection.

Then run command
```
pip install -r requirements.txt
pip install "git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI"
pip install -v -e .
mkdir data
cd data
ln -s /your path/dataset VOCdevkit
```

#### Step 3: Modify config file

Modify the file in `mmdetection/mmdet/core/evaluation/class_names.py` and change the names in `voc_classes()` to your class name('1' to '10' in this homework)

Modify the file in `mmdetection/mmdet/datasets/voc.py` and change the names in `CLASSES` to your class name('1' to '10' in this homework)

Modify the model config file(faster rcnn r50 in this homework) in `configs/_base_/models/faster_rcnn_r50_fpn.py`
- change all the `num_classes` to the number of your classes(10 in this hw) **In the version of this hw is written, there's no need to add the background class**
- change `dataset_type`,`data_root`,`img_scale`,`ann_file`,`img_prefix`,`img_scale` as image<a href="#[4]"> [4] </a> below
<img src="https://img-blog.csdnimg.cn/20200212112033538.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xhaXppX2xhaXpp,size_16,color_FFFFFF,t_70" width="576" height="480">
<img src="https://img-blog.csdnimg.cn/20200212112302685.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xhaXppX2xhaXpp,size_16,color_FFFFFF,t_70" width="576" height="480">

Modify the desired runtime and schedule(epochs, step) setting in `configs/_base_/default_runtime.py` and `configs/_base_/schedules/schedule_1x.py`

Modify the `mmdet/datasets/xml_style.py`
- change all the `.jpg` to `.png` if your images are png file
- change the line `difficult = int(obj.find('difficult').text)` to block below if your xml file doesn't have difficult annotation.
```
if obj.find('difficult'):
    difficult = int(obj.find('difficult').text)
else:
    difficult = 0
```

> **If found the changes did not apply when you train, you can pip install e . again to update the change, but remember to check all the file is modified after update**

#### Step 4: Start training
`cd` to mmdetection directory and run `python3 ./tools/train.py ./configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py`

Then the training process should have begun.
#### Step 5: Inferencing
After training has completed, run the file [inference2txt](https://github.com/PinJui/CS_T0828_HW2/blob/main/inference2txt.py) to get the prediction txt file and by adjusting the threshold in **txt2json file** you can choose the confidence of bbox to write into the result json file.

Then you can upload the json file to TA for mAP calculation!

## Results 
After training for 10 epochs(nearly 10 hours on a RTX 2080 Ti GPU), some of the inference result in the json file is as below:

<img src="https://raw.githubusercontent.com/PinJui/CS_T0828_HW2/main/assets/1.png">
<img src="https://raw.githubusercontent.com/PinJui/CS_T0828_HW2/main/assets/2.png">

```
[
{"bbox": [[6, 40, 39, 59]], "score": [0.9932959675788879], "label": [5]},
{"bbox": [[7, 112, 28, 123], [6, 98, 29, 112], [7, 121, 28, 134]], "score": [0.908193051815033, 0.9809567928314209, 0.9090336561203003], "label": [1, 2, 10]}
...
]
```

## Reference
<a name="[1]"> [1] [Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Bo Wu, Andrew Y. Ng Reading Digits in Natural Images with Unsupervised Feature Learning NIPS Workshop on Deep Learning and Unsupervised Feature Learning 2011.](http://ufldl.stanford.edu/housenumbers/) </a>

<a name="[2]"> [2] [MMDetection: Open MMLab Detection Toolbox and Benchmark](https://github.com/open-mmlab/mmdetection.git) </a>

<a name="[3]"> [3] [RetinaNET Object Detector for SVHN Dataset](https://github.com/AlessandroSaviolo/RetinaNET-Object-Detector.git) </a>

<a name="[4]"> [4] [mmdetection实战，训练扑克牌数据集（VOC格式）并测试计算mAP](https://blog.csdn.net/laizi_laizi/article/details/104256781) </a>
