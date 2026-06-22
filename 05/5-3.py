import time

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, models, transforms

transform = transforms.Compose(
    [
        transforms.Resize((32, 32)),
        transforms.Grayscale(num_output_channels=3),
        transforms.ToTensor(),
    ]
)

train_dataset = datasets.FashionMNIST(
    root="./data", train=True, download=True, transform=transform
)
test_dataset = datasets.FashionMNIST(
    root="./data", train=False, download=True, transform=transform
)

train_dataset = Subset(train_dataset, range(1000))
test_dataset = Subset(test_dataset, range(200))

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

resnet = models.resnet18(weights=None)
resnet.fc = nn.Linear(resnet.fc.in_features, 10)

vgg16 = models.vgg16(weights=None)
vgg16.classifier[6] = nn.Linear(vgg16.classifier[6].in_features, 10)

model_list = [
    ("ResNet18", resnet),
    ("VGG16", vgg16),
]

criterion = nn.CrossEntropyLoss()
num_epochs = 3
results = []

for model_name, model in model_list:
    optimizer = optim.Adam(model.parameters(), lr=0.0001)

    start_time = time.time()

    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0

        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        print(
            f"{model_name} Epoch {epoch + 1}/{num_epochs}, "
            f"Loss: {running_loss / len(train_loader):.4f}"
        )

    training_time = time.time() - start_time

    model.eval()
    test_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            loss = criterion(outputs, labels)
            predictions = outputs.argmax(dim=1)

            test_loss += loss.item()
            total += labels.size(0)
            correct += (predictions == labels).sum().item()

    test_loss = test_loss / len(test_loader)
    accuracy = correct / total * 100

    results.append([model_name, test_loss, accuracy, training_time])

print("\n모델 성능 비교")

for result in results:
    print("모델:", result[0])
    print(f"테스트 손실: {result[1]:.4f}")
    print(f"테스트 정확도: {result[2]:.2f}%")
    print(f"학습 시간: {result[3]:.2f}초")
    print()
