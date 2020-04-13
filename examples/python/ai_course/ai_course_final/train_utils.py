import torch

from time import time
from torchvision import datasets, transforms, models
from torch import nn, optim
from helpers import get_models_available, save_checkpoint

def get_valid_loss_and_accuracy(model, loader, device, criterion):
    loader_size = len(loader)
    valid_loss = 0
    accuracy = 0
    model.eval()
    with torch.no_grad():
        for inputs, labels in loader:
            inputs, labels = inputs.to(device), labels.to(device)
            logps = model.forward(inputs)
            ps = torch.exp(logps)
            top_p, top_class = ps.topk(1, dim=1)
            equals = top_class == labels.view(*top_class.shape)
            accuracy += torch.mean(equals.type(torch.FloatTensor)).item()
            valid_loss += criterion(logps, labels).item()
            
    model.train()
    valid_loss /= loader_size
    accuracy /= loader_size
    return valid_loss, accuracy

def get_model(device="cpu", arch="vgg13", hidden_units=512, dropout=0.5, output_units=103, data_dir=None, save_dir=None):
    models = get_models_available()
    model = models[arch]
    for param in model.parameters():
        param.requires_grad = False
    model.hidden_units = hidden_units
    model.arch = arch
    model.device = device
    model.dropout = dropout
    model.output_units = output_units
    model.data_dir = data_dir
    model.save_dir = save_dir
    model.classifier = nn.Sequential(
        nn.Linear(25088, hidden_units),
        nn.ReLU(),
        nn.Dropout(dropout),
        nn.Linear(hidden_units, output_units),
        nn.LogSoftmax(dim=1)
    )
    model.to(device)
    return model

def get_criterion():
    return nn.NLLLoss()

def get_optimizer(model, lr):
    return optim.SGD(model.classifier.parameters(), lr=lr)

def get_transformers():
    training_transformer = transforms.Compose([
        transforms.RandomRotation(20),
        transforms.Resize(255),
        transforms.CenterCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    default_transformer = transforms.Compose([
        transforms.Resize(255),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    return default_transformer, training_transformer

def get_dataset(path, transformer):
    try:
        return datasets.ImageFolder(path, transform=transformer)
    except FileNotFoundError:
        print(f"Folder {path} doesn't exist.")

def get_datasets(path, default_transformer, training_transformer=None):
    if not training_transformer:
        training_transformer = default_transformer
    return {
        'train': get_dataset(path + "/train", training_transformer),
        'valid': get_dataset(path + "/valid", default_transformer),
        'test': get_dataset(path + "/test", default_transformer),
    }

def get_dataloaders_from_datasets(datasets):
    return {
        'train': torch.utils.data.DataLoader(datasets['train'], batch_size=64, shuffle=True),
        'valid': torch.utils.data.DataLoader(datasets['valid'], batch_size=32),
        'test': torch.utils.data.DataLoader(datasets['test'], batch_size=32)
    }

def get_dataloaders(path):
    default_transformer, training_transformer = get_transformers()
    datasets = get_datasets(path, default_transformer, training_transformer)
    return get_dataloaders_from_datasets(datasets)


def train(model, criterion, optimizer, epochs, device, train_loader, valid_loader, print_every=60, step_track_every=30):
    total_start = time()
    model.epochs = epochs
    save_checkpoint(model, optimizer)
    train_losses, valid_losses = [], []
    steps = 0
    running_loss = 0
    valid_loader_size = len(valid_loader)
    print("==========================")
    print("Starting training of NN...")
    for epoch in range(epochs):
        print("==========================")
        print(f"Starting epoch #{epoch}...")
        start_epoch = start_step = time()
        for inputs, labels in train_loader:
            steps += 1
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            logps = model.forward(inputs)
            loss = criterion(logps, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            
            if steps % step_track_every == 0:
                print(f"Time in step #{steps}: {(time() - start_step):.3f} seconds") 
                start_step = time()
            if steps % print_every == 0:
                start_test = time()
                valid_loss, accuracy = get_valid_loss_and_accuracy(model, valid_loader, device, criterion) 
                cur_train_loss = running_loss/valid_loader_size
                running_loss = 0
                train_losses.append(cur_train_loss)
                valid_losses.append(valid_loss)
                print(f"Epoch {epoch}/{epochs}..."
                      f"Training loss: {cur_train_loss:.4f}..."
                      f"Validation loss: {valid_loss:.4f}..."
                      f"Test accuracy: {accuracy:.4f}\n")
                print(f"Time taken to test losses in epoch #{epoch}: {(time() - start_test):.3f} seconds") 
        print(f"Time per epoch: {(time() - start_epoch):.3f} seconds")    
    print(f"Total training time: {(time() - total_start):.3f} seconds")
    save_checkpoint(model, optimizer)