# %%
import pandas as pd
import torch
import torchvision.models as models
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import r2_score
from tqdm import tqdm
import matplotlib.pyplot as plt
import pandas as pd

from torch.utils.data import Dataset, DataLoader
from torchvision.io import decode_image
import torchvision.transforms as transforms

from PIL import Image

from peru_poverty_sat.config import PROCESSED_DATA_DIR

from torch.utils.data import Dataset, DataLoader
from torchvision.io import decode_image
from torchvision.transforms import ToTensor


from peru_poverty_sat.config import PROCESSED_DATA_DIR

# %%
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# %%
class ENAHOS2(Dataset):
    def __init__(self, dataset_dir, transform=None, target_transform=None):
        self.labels = pd.read_parquet(dataset_dir / 'index.parquet')
        self.imgs_dir = dataset_dir / 'imgs'
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        img_path = self.imgs_dir / f"{self.labels.iloc[idx]['filename']}.png"
        image = Image.open(img_path)
        label = self.labels.iloc[idx]['wealth_index']
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label

# %%
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

training_data = ENAHOS2(
    dataset_dir=PROCESSED_DATA_DIR / 'ENAHOS2',
    transform=transform,
)

# %%
training_data[5000]

# %%
# Load pre-trained ViT model
model = models.vit_b_16(pretrained=True)

# Modify the head for regression (output a single value)
num_ftrs = model.heads.head.in_features
model.heads.head = nn.Linear(num_ftrs, 1)

# Move model to device
model = model.to(device)

# %%
# Define DataLoader
batch_size = 32
train_dataloader = DataLoader(training_data, batch_size=batch_size, shuffle=True)

# Define loss function and optimizer
loss_fn = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-4)

# Training loop
num_epochs = 5  # You might want to adjust this based on your dataset size and desired training time

model.train() # Set the model to training mode
print("Starting training...")
for epoch in range(num_epochs):
    running_loss = 0.0
    for batch_idx, (images, labels) in enumerate(tqdm(train_dataloader, desc=f"Epoch {epoch+1}/{num_epochs}")):
        images = images.to(device)
        labels = labels.to(device).float().view(-1, 1) # Ensure labels are float and correct shape

        # Forward pass
        outputs = model(images)
        loss = loss_fn(outputs, labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)

    epoch_loss = running_loss / len(training_data)
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {epoch_loss:.4f}")

print("Training complete!")

# %%
# Evaluation
model.eval() # Set the model to evaluation mode
all_labels = []
all_predictions = []

with torch.no_grad():
    for images, labels in tqdm(train_dataloader, desc="Collecting predictions"):
        images = images.to(device)
        labels = labels.to(device).float().view(-1, 1)

        outputs = model(images)

        all_labels.extend(labels.cpu().numpy())
        all_predictions.extend(outputs.cpu().numpy())

# Calculate R^2 score
r2 = r2_score(all_labels, all_predictions)
print(f"R^2 Score: {r2:.4f}")

# Plotting actual vs predicted
plt.figure(figsize=(10, 6))
plt.scatter(all_labels, all_predictions, alpha=0.3)
plt.title('Actual vs. Predicted Wealth Index')
plt.xlabel('Actual Wealth Index')
plt.ylabel('Predicted Wealth Index')
plt.grid(True)
plt.plot([min(all_labels), max(all_labels)], [min(all_labels), max(all_labels)], 'r--') # Identity line
plt.show()

# %%

# %%
# Load pre-trained ViT model
model = models.vit_base_patch16_224(pretrained=True)

# Modify the head for regression (output a single value)
num_ftrs = model.heads.head.in_features
model.heads.head = nn.Linear(num_ftrs, 1)

# Move model to device
model = model.to(device)
