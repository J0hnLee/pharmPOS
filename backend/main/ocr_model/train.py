import argparse
import tqdm
import pickle
import torch
import torch.nn.functional as F
import torch.nn as nn
from DataLoader import *
from model import *
from torch.utils.data.sampler import SubsetRandomSampler
from sklearn.model_selection import StratifiedKFold
from torch.autograd import Variable
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from split_string import *

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epoch', type=int, default=0)
    parser.add_argument('--n_epochs', type=int, default=100)
    parser.add_argument('--batch', type=int, default=1024)
    parser.add_argument('--beta', type=float, default=5e-2)
    parser.add_argument('--lr', type=float, default=0.001)
    parser.add_argument('--weight_decay', type=float, default=1e-5)
    parser.add_argument('--momentum', type=float, default=.9)
    parser.add_argument('--scheduler_step', type=int, default=5)
    parser.add_argument('--gamma', type=float, default=.98)
    parser.add_argument('--n_cpu', type=int, default=4)
    parser.add_argument('--gpu_num', type=str, default='1')
    opt = parser.parse_args()
    print(opt)

    return opt


def train(opt):
    os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpu_num
    model = LeNet().cuda()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
    # scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=opt.scheduler_setp, gamma=opt.gamma)
    loss = nn.CrossEntropyLoss()
    trans = transforms.Compose([
        transforms.Resize(size=(30, 30)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[.5], std=[.4])
    ])
    train_data = Data('./dataset', transforms_=trans, mode='train')
    test_data = Data('./dataset', mode='test')
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=opt.batch, num_workers=opt.n_cpu)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=opt.batch, num_workers=opt.n_cpu)
    test_min = float('inf')
    with tqdm.tqdm(total=opt.epoch, miniters=1, mininterval=0) as progress:
        for epoch in range(1, opt.n_epochs+1):
            total_correct = 0
            model.train()
            for i, batch in enumerate(train_loader, 1):
                img = Variable(batch['X']).cuda()
                lbl = Variable(batch['Y']).cuda()
                optimizer.zero_grad()
                output = model(img)
                batch_loss = loss(output, lbl)
                batch_loss.backward()
                optimizer.step()
                _, predict = torch.max(output, 1)
                total_correct += (predict == lbl).sum()
                des = "epoch: {epoch}, Iter: {iter:.1f}%, Loss: {loss:.8f}, Correct_rate: {rate:.2f}%, " \
                      "Corr/total: {corr}/{total}".format(
                        epoch=epoch,
                        iter=100*i/len(train_loader),
                        loss=batch_loss,
                        rate=100*total_correct/len(train_data),
                        corr=total_correct,
                        total=len(train_data)
                )
                progress.set_description(des)
            model.eval()
            test_loss = 0
            test_correct = 0
            for i, batch in enumerate(test_loader, 1):
                img = Variable(batch['X']).cuda()
                lbl = Variable(batch['Y']).cuda()
                with torch.no_grad():
                    output = model(img)
                    test_loss += loss(output, lbl)
                    _, predict = torch.max(output, 1)
                    test_correct += (predict == lbl).sum()
            print("\n---TEST--- Loss : {loss:.8f}, Correct_rate: {rate:.2f}%, Corr/total: {corr}/{total}".format(
                loss=test_loss,
                rate=(100*test_correct)/len(test_data),
                corr=test_correct,
                total=len(test_data)
            ))
            if test_loss < test_min:
                test_min = test_loss
                torch.save(model, 'model2.pth')
                print('Model Saved')

def test(opt):
    os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpu_num
    test_data = Data('./dataset', mode='test')
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=25, num_workers=opt.n_cpu, shuffle=True)
    model = torch.load('model2.pth').cuda()
    model.eval()
    chinese_lbl = {}

    with open('chinese_labels', 'rb') as _dict:
        chinese_lbl = pickle.load(_dict)

    for i, batch in enumerate(test_loader):
        img = Variable(batch['X']).cuda()
        print(img.shape)
        lbl = Variable(batch['Y']).cuda()
        with torch.no_grad():
            output = model(img)
            _, predict = torch.max(output, 1)
        fig = plt.figure(figsize=(10, 10))
        font = FontProperties(fname="./msj.ttf", size=14)
        for j in range(25):
            plt.subplot(5, 5, j+1)
            plt.tight_layout()
            plt.imshow(img[j][0].cpu(), cmap='gray', interpolation='none')
            plt.title("Prediction: {}".format(
                chinese_lbl[predict[j].cpu().item()]
            ), fontproperties=font)
            plt.xticks([])
            plt.yticks([])
        fig.savefig('predict2.png')
        break

def predict(opt, input_file):
    os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpu_num
    model = torch.load('model2.pth')
    model.cpu()
    model.eval()
    s = Split(input_file)
    img_list = s.split()
    test_data = TestData(img_list)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=1)
    with open('chinese_labels', 'rb') as _dict:
        chinese_lbl = pickle.load(_dict)

    fig = plt.figure(figsize=(10, 10))
    font = FontProperties(fname="./msj.ttf", size=14)
    for i, batch in enumerate(test_loader):
        img = Variable(batch)
        with torch.no_grad():
            output = model(img)
            _, predict = torch.max(output, 1)
            print(chinese_lbl[predict.item()])
            plt.subplot(1, len(test_data), i + 1)
            plt.tight_layout()
            plt.imshow(img[0][0], cmap='gray', interpolation='none')
            plt.title("Prediction: {}".format(
                chinese_lbl[predict.item()]
            ), fontproperties=font)
            plt.xticks([])
            plt.yticks([])
        fig.savefig('predict.png')

if __name__ == '__main__':
    opt = parse()
    # train(opt)
    # test(opt)
    predict(opt, './input/test7.png')
