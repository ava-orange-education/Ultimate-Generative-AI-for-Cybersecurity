import torch
import torch.nn as nn

class Discriminator(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        return self.model(x)

# Usage in training
discriminator = Discriminator(input_dim=10)  # e.g., log features
real_data = torch.randn(32, 10)
output = discriminator(real_data)
