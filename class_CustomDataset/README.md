## 问题描述

生成的数据集需要读取csv，而deepsort代码是使用imagefolder读取路径获得label，需要进行改动。

##  目录结构

├── CustomDataset.py ：基于torchvision.datasets.ImageFolder 类进行改写，完成了相似的功能，同样继承自torch.utils.data.Dataset ，但把读取标签的步骤从路径中抽取 - > 改为了读取csv

├── Loader_API.py：调用了torch.utils.data.Dataloader，torch.utils.data.Dataset 作为参数传入

└── dataset：用取出上一步生成的数据集作为demo-dataset

  ├── img/

  └── label.csv

1. 借鉴思路 [pytorch.org](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html)
2. pytorch-doc


