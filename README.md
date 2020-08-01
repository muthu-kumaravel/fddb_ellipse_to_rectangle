# FDDB ELLIPSE TO RECTANGLE

This code is used to 
* Convert elliptical annotation of FDDB data set to rectangular
* Dump ground truth of each image seperately 
* Extract image specified in [FDDB_Fold](http://vis-www.cs.umass.edu/fddb/) from [face_in_the_wild](http://tamaraberg.com/faceDataset/index.html) and dump them seperately

### Example
__Input format__
FDDB-fold-01.txt
```
2002/08/11/big/img_591
2002/08/26/big/img_265
2002/07/19/big/img_423
.
.
.
```
FDDB-fold-01-ellipseList.txt
```
2002/08/11/big/img_591
1
123.583300 85.549500 1.265839 269.693400 161.781200  1
2002/08/26/big/img_265
3
67.363819 44.511485 -1.476417 105.249970 87.209036  1
41.936870 27.064477 1.471906 184.070915 129.345601  1
70.993052 43.355200 1.370217 340.894300 117.498951  1
2002/07/19/big/img_423
1
87.080955 59.379319 1.550861 255.383099 133.767857  1
.
.
.
```
__Output Folder__
* FDDB Images   : FDDB_DATASET_IMAGES_GROUND_TRUTH/fddb_images/
* Ground Truth  : FDDB_DATASET_IMAGES_GROUND_TRUTH/ground_truth_rect

### Prerequisite
* Download      : [Original, unannotated, set of images](http://tamaraberg.com/faceDataset/originalPics.tar.gz)
* Extract the file into __fddb_ellipse_to_rectangle/__, so that __2002__ and __2003__ will be there within the folder fddb_ellipse_to_rectangle
* follow thsi command to create the folder structure
```
$ mkdir FDDB_DATASET_IMAGES_GROUND_TRUTH
$ cd FDDB_DATASET_IMAGES_GROUND_TRUTH
$ mkdir fddb_images
$ mkdir ground_truth_rect
$ cd ..
```

### Execute
To run the script,
```
python3 eliptorect.py
```
(Use python or python3 as you always use in your system)

### Useful links
* [FDDB](http://vis-www.cs.umass.edu/fddb/)
* [Face in Wild](http://tamaraberg.com/faceDataset/index.html)
* [mAP calculation script](https://github.com/Cartucho/mAP)