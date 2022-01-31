from datasets import init_dataloaders
import torch as tc
import numpy as np
from matplotlib import pyplot as plt


def print_dataset():
    # train, test = init_dataloaders('lv')
    # train, test = init_dataloaders('gs')
    train, test = init_dataloaders('ns')
    for _, data in enumerate(train, 0):
        print(len(train))
        print(data['state'].shape)
        break
    for _, data in enumerate(test, 0):
        print(len(test))
        print(data['state'].shape)
        break


def save_datasets():
    dataset_abbr = 'gs'
    train, test = init_dataloaders(dataset_abbr)
    all_data = []
    for _, data in enumerate(train, 0):
        all_data.append(data['state'])
        print(data['state'].shape)
    all = tc.stack(all_data)
    print(all.shape)
    tc.save(all, '{}.pt'.format(dataset_abbr))



if __name__ == '__main__':
    # save_datasets()
    data = tc.load('ns.pt')
    print(data.shape)
    data = tc.load('gs.pt')
    print(data.shape)
    data = tc.load('lv.pt')
    print(data.shape)

