#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Juan Mendoza
# DATE CREATED: 12/04/2020  


import argparse
import os

def create_dir(name):
    path = os.getcwd() + "/"
    dir_name = path + name
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print("Directory {} created.".format(dir_name))   
        
def get_args_train():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_dir', type = str, help = 'Path to the folder of training images. Example: flowers') 
    parser.add_argument('--arch', type = str, default = 'vgg13', help = 'CNN Model Architecture')
    parser.add_argument('--save_dir', type = str, default = 'checkpoints', help = 'Set directory to save checkpoints.')
    parser.add_argument('--learning_rate', type = float, default = 0.01, help = 'Learning rate') 
    parser.add_argument('--hidden_units', type = int, default = 512, help = 'Units in hidden layer') 
    parser.add_argument('--epochs', type = int, default = 20, help = 'Epochs for training')
    parser.add_argument('--gpu', default = False, action='store_true', help = 'Should we use GPU')
    in_args = parser.parse_args()
    create_dir(in_args.save_dir)
    return in_args

def get_args_predict():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('image_path', type = str, help = 'path to the image to predict results. Example: flowers/train/1/image_06734.jpg') 
    parser.add_argument('checkpoint_path', type = str, help = 'path to the image to predict results. Example: checkpoints/my_checkpoint.pth') 
    parser.add_argument('--top_k', type = int, default = 3, help = 'Top number of results')
    parser.add_argument('--category_names', type = str, default = 'cat_to_name.json', help = 'Category JSON file. Example: cat_to_name.json')
    parser.add_argument('--gpu', default = False, action='store_true', help = 'Should we use GPU')
    
    in_args = parser.parse_args()
    return in_args