# CS_T0828_HW2

Digit Detection on SVHN(Street View House Numbers) Dataset

## Content

## Introduction
This homework requires to train a digit detector to detect the digits inside a given image.

The given dataset is a subset of SVHN[1]dataset, which has 33042 training images and 13068 test image of Format 1 in the SVHN.

Image Example:
[Training Image Example](**img_link**)

The desired result is the detected digits recorded as a list of dictionary, which each dictionary corresponds to one test image.

The dictionary has three keys:
- "bbox": List of bounding boxes in (y1, x1, y2, x2). (top,left,right,bottom)
- "score": List of probability for the class of the detected digit
- "label": List of class of the detected digit

Result Example(for test image 1.png):
```
{
 "bbox": [[6, 40, 39, 59]],
 "score": [0.9932959675788879],
 "label": [5]
}
```

## Methodology

## Results

## Reference
- [1] [Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Bo Wu, Andrew Y. Ng Reading Digits in Natural Images with Unsupervised Feature Learning NIPS Workshop on Deep Learning and Unsupervised Feature Learning 2011.](http://ufldl.stanford.edu/housenumbers/)
