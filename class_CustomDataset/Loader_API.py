from torch.utils.data import DataLoader
import CustomDataset
import matplotlib.pyplot as plt
import torchvision
from PIL import Image

transform_train = torchvision.transforms.Compose([
    torchvision.transforms.RandomCrop((128, 64), padding=4),
    torchvision.transforms.RandomHorizontalFlip(),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(
        [0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
training_data=CustomDataset.CustomImageDataset('dataset/label.csv','',transform=transform_train)
train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
    # print(f"Label: {label}")