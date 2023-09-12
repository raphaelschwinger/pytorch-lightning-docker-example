# %%
import torch, torch.nn as nn
import lightning as L

class NeuralNetwork(L.LightningModule):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
    
    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = nn.functional.cross_entropy(logits, y)
        self.log('train_loss', loss)
        return loss
    
    def validation_step(self, batch, batch_idx):
        loss = self.training_step(batch, batch_idx)
        self.log('val_loss', loss)
        return loss
    
    def configure_optimizers(self):
        return torch.optim.SGD(self.parameters(), lr=1e-3)


# %%
from torchvision import datasets
from torchvision.transforms import ToTensor
# Download training data from open datasets.
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)

# Download test data from open datasets.
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

# %%
# get current path
import os

# change to directory of this file
os.chdir('/workspace')
path = os.getcwd()
print(path)


# %%
from torch.utils.data import DataLoader
batch_size = 64
model = NeuralNetwork()
# works on single GPU
# trainer = L.Trainer(max_epochs=5, accelerator='gpu', devices=[0])
trainer = L.Trainer(max_epochs=5, accelerator='gpu', devices=[0,1])
trainer.fit(model, DataLoader(training_data, batch_size=batch_size), DataLoader(test_data, batch_size=batch_size))

# %%
# get sample from validation set
x, y = next(iter(DataLoader(test_data, batch_size=1)))
# get prediction
pred = model(x)

classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]
predicted, actual = classes[pred[0].argmax(0)], classes[y]
print(f'Predicted: "{predicted}", Actual: "{actual}"')


