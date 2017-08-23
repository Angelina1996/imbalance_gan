#data.py
import os,sys
from PIL import Image
import scipy.misc
from glob import glob
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from tensorflow.examples.tutorials.mnist import input_data

folder = '/data/projects/yhliuzzb/'
def get_img(img_path, crop_h, resize_h):
    img=scipy.misc.imread(img_path).astype(np.float) # mode L for grayscale
    #print(img.shape)
    
    #print(img.shape)
    #crop resize  Original Use
    crop_w = crop_h
    resize_h = resize_h
    resize_w = resize_h
    h, w = img.shape[:2]
    j = int(round((h - crop_h)/2.))
    i = int(round((w - crop_w)/2.))
    #cropped_image = scipy.misc.imresize(img[j:j+crop_h, i:i+crop_w],[resize_h, resize_w])# cropp
    cropped_image = scipy.misc.imresize(img,[resize_h, resize_w])# no cropp
    #print(cropped_image.shape)
    #img = cropped_image#for defect grayscale data
    #img = np.dstack((cropped_image,cropped_image))[:,:,:1]
    if len(cropped_image.shape)==3:
        cropped_image = cropped_image[:,:,0]
    img = cropped_image.reshape((resize_h,resize_w,1))
    #print(img)
    #print(img.shape)
    return np.array(img)/255.0


class celebA():
    def __init__(self):
        datapath = prefix + 'celebA'
        self.z_dim = 100
        self.size = 64
        self.channel = 3
        self.data = glob(os.path.join(datapath, '*.jpg'))
        
        self.batch_count = 0
    
    def __call__(self,batch_size):
        batch_number = len(self.data)/batch_size
        if self.batch_count < batch_number-1:
            self.batch_count += 1
        else:
            self.batch_count = 0
        
        path_list = self.data[self.batch_count*batch_size:(self.batch_count+1)*batch_size]
        
        batch = [get_img(img_path, 128, self.size) for img_path in path_list]
        batch_imgs = np.array(batch).astype(np.float32)
        '''
            print self.batch_count
            fig = self.data2fig(batch_imgs[:16,:,:])
            plt.savefig('out_face/{}.png'.format(str(self.batch_count).zfill(3)), bbox_inches='tight')
            plt.close(fig)
            '''
        return batch_imgs
            
            def data2fig(self, samples):
        fig = plt.figure(figsize=(4, 4))
        gs = gridspec.GridSpec(4, 4)
        gs.update(wspace=0.05, hspace=0.05)
        
        for i, sample in enumerate(samples):
            ax = plt.subplot(gs[i])
            plt.axis('off')
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.set_aspect('equal')
            plt.imshow(sample)
return fig

class mydata():
    def __init__(self, size, defect, defect_num,test=False):
        
        data_list = []
        for i in range(defect_num):
            defect_sub = defect.split(',')[i]
            print(defect_sub)
            #datapath = '/data/projects/eyhsu/defect/images/PSD1_ASI/'+defect_sub+'/*.jpg'
            if test:
                datapath = '../defect/test'+defect_sub+'/*.jpg'
            else:
                datapath = '../defect/'+defect_sub+'/*.jpg'
            data_list.extend(glob(datapath))
        print(len(data_list))
        
        
        #datapath = folder+'data/'+defect+'/'
        self.z_dim = 512
        self.y_dim = defect_num
        self.size = size
        self.channel = 1 ##
        self.data = data_list
        #self.data = glob(os.path.join(datapath, '*.jpg'))
        #print(self.data)
        
        label = []
        check = []
        label_count = -1
        for path in self.data:
            defect_id = path.split('/')[2]#7,5
            if defect_id not in check:
                check.append(defect_id)
                label_count+=1
            label.append(label_count)
        
        #print(label)
        one_hot = np.zeros((len(label),self.y_dim))
        for i,val in enumerate(label):
            one_hot[i,val]=1
        self.label = one_hot
                self.batch_count = 0

def __call__(self,batch_size):
    
    batch_number = len(self.data)/batch_size
        if self.batch_count < batch_number-1:
            self.batch_count += 1
    else:
        list_zip = list(zip(self.data,self.label))
            np.random.shuffle(list_zip)
            self.data, self.label = zip(*list_zip)
            self.batch_count = 0
        
        path_list = self.data[self.batch_count*batch_size:(self.batch_count+1)*batch_size]
        label_list = self.label[self.batch_count*batch_size:(self.batch_count+1)*batch_size]
        #print(path_list)
        
        batch = [get_img(img_path, self.size*3, self.size) for img_path in path_list]
        batch_imgs = np.array(batch).astype(np.float32)



'''
    print self.batch_count
    fig = self.data2fig(batch_imgs[:16,:,:])
    plt.savefig('out_face/{}.png'.format(str(self.batch_count).zfill(3)), bbox_inches='tight')
    plt.close(fig)
    '''
        return batch_imgs, label_list

def data2fig(self, samples):
    fig = plt.figure(figsize=(4, 4))
        gs = gridspec.GridSpec(4, 4)
        gs.update(wspace=0.05, hspace=0.05)
        
        for i, sample in enumerate(samples):
            #print(sample)
            ax = plt.subplot(gs[i])
            plt.axis('off')
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.set_aspect('equal')
            #print(sample.shape)
            new_sample = np.concatenate((sample,sample),axis = 2)
            new_sample = np.concatenate((new_sample,sample),axis = 2)
            #print(new_sample.shape)
            sample = new_sample
            plt.imshow(sample)
        return fig

class mnist():
    def __init__(self, flag='conv', is_tanh = False):
        datapath = folder+'GAN_yhliu/MNIST_data'
        self.X_dim = 784 # for mlp
        self.z_dim = 100
        self.y_dim = 10
        self.size = 28 # for conv
        self.channel = 1 # for conv
        self.data = input_data.read_data_sets(datapath, one_hot=True)
        self.flag = flag
        self.is_tanh = is_tanh
    
    def __call__(self,batch_size):
        batch_imgs,y = self.data.train.next_batch(batch_size)
        if self.flag == 'conv':
            batch_imgs = np.reshape(batch_imgs, (batch_size, self.size, self.size, self.channel))
        if self.is_tanh:
            batch_imgs = batch_imgs*2 - 1
        return batch_imgs, y
    
    def data2fig(self, samples):
        if self.is_tanh:
            samples = (samples + 1)/2
        fig = plt.figure(figsize=(4, 4))
        gs = gridspec.GridSpec(4, 4)
        gs.update(wspace=0.05, hspace=0.05)
        
        for i, sample in enumerate(samples):
            ax = plt.subplot(gs[i])
            plt.axis('off')
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.set_aspect('equal')
            plt.imshow(sample.reshape(self.size,self.size), cmap='Greys_r')
return fig

if __name__ == '__main__':
    data = face3D()
    print(data(17).shape)
