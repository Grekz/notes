import json
import torch
import time

import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt

from torch import nn, optim
from torchvision import datasets, transforms, models
from PIL import Image


alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)
vgg13 = models.vgg13(pretrained=True)

models_available = {'alexnet': alexnet, 'vgg16': vgg16, 'vgg13': vgg13}

def get_models_available():
    return models_available

def get_device(is_gpu=False):
    if is_gpu:
        if torch.cuda.is_available():
            return "cuda"
        else: 
            print("============================================")
            print("WARNING: GPU is disabled, going back to CPU.")
            print("============================================")
    else:
        print("============================================")
        print("WARNING: You are running it in CPU.")
        print("============================================")
    return "cpu"
    
        
def crop_center(image, size):
    width = image.width
    height = image.height
    return image.crop(((width-size)//2, (height-size)//2, (width+size)//2, (height+size)//2))

def convert_image(image):
    return np.array(image)/255

def normalize(image_arr):
    return (image_arr - np.array([0.485, 0.456, 0.406])) / np.array([0.229, 0.224, 0.225])

def process_image(img_path):
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''
    im = Image.open(img_path)
    size = (256, 10000) if im.size[0] < im.size[1] else (10000, 256)
    im.thumbnail(size)
    im = crop_center(im, 224)
    im = convert_image(im)
    im = normalize(im)
    im = im.transpose((2,0,1))
    return torch.from_numpy(im)

def predict(image_path, model, cat_to_name, topk=5):
    ''' Predict the class (or classes) of an image using a trained deep learning model.
    '''
    model.eval()
    model.to(device)
    image = process_image(image_path)
    image = torch.from_numpy(image).type(torch.cuda.FloatTensor)
    image = image.unsqueeze(0)
    
    with torch.no_grad():
        logps = model.forward(image)

    ps = torch.exp(logps)
    top_p, top_class = ps.topk(topk, dim=1)
    top_class = [ cat_to_name[str(tc)] for tc in (top_class[0]+1).tolist()]
    return top_p[0].tolist(), top_class

def save_checkpoint(model, optimizer):
    # Save the checkpoint 
    checkpoint = {'arch': model.arch,
                  'epochs': model.epochs,
                  'optimizer_algo': 'SGD',
                  'optimazer_state_dict': optimizer.state_dict(),
                  'hidden_units': model.hidden_units,
                  'output_units': model.output_units,
                  'data_dir': model.data_dir,
                  'device': model.device,
                  'save_dir': model.save_dir,
                  'state_dict': model.state_dict()}

    torch.save(checkpoint, model.save_dir + "/cp_tmp.pth")

def load_checkpoint(filepath, device, debug=False):
    checkpoint = torch.load(filepath)
    if debug:
        print(checkpoint)
    arch = checkpoint['arch']
    state_dict = checkpoint['state_dict']
    output_units = checkpoint['output_units']
    hidden_units = checkpoint['hidden_units']
    model = models_available[arch]
    
    for param in model.parameters():
        param.requires_grad = False
        
    model.classifier = nn.Sequential(
        nn.Linear(25088, hidden_units),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(hidden_units, output_units),
        nn.LogSoftmax(dim=1)
    )
    model.load_state_dict(state_dict)
    model.to(device)
    if debug:
        print(model)
        print("Model successfully loaded from: {}. \nInfo about the model: {}".format(filepath, list(checkpoint.keys())))
    return model

def load_names(category_names):
    try:
        with open(category_names, 'r') as f:
            cat_to_name = json.load(f)
        return cat_to_name
    except:
        print("ERROR: category files with name '{}' cannot be found".format(category_names))
        raise

def predict(image_path, model, cat_to_name, device, topk=5):
    ''' Predict the class (or classes) of an image using a trained deep learning model.
    '''
    model.eval()
    image = process_image(image_path)
    image = image.type(torch.cuda.FloatTensor if device == "cuda" else torch.FloatTensor)
    image = image.unsqueeze(0)
    
    with torch.no_grad():
        logps = model.forward(image)

    ps = torch.exp(logps)
    top_p, top_class = ps.topk(topk, dim=1)
    top_class = [ cat_to_name[str(tc)] for tc in (top_class[0]+1).tolist()]
    return top_p[0].tolist(), top_class