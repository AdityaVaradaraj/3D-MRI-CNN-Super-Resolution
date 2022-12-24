import torch
import torch.nn as nn 
import torch.nn.functional as F 

class Net(nn.Module):

  def __init__(self,r=2):
    super(Net,self).__init__()
    self.conv1 = nn.Conv2d(1, 32,kernel_size = 3, padding = 'same')
    self.ELU1 = nn.ELU()
    
    self.conv2 = nn.Conv2d(32, 32, kernel_size = 3, padding = 'same')
    self.ELU2 = nn.ELU()

    self.conv3 = nn.Conv2d(32,32,kernel_size = 3 , padding = 'same')
    self.ELU3 = nn.ELU()
    
    self.conv4 = nn.Conv2d(32,32,kernel_size = 3 , padding = 'same')
    self.ELU4 = nn.ELU()

    self.conv5 = nn.Conv2d(32,32,kernel_size = 3 , padding = 'same')
    self.ELU5 = nn.ELU()

    self.conv6 = nn.Conv2d(32,32,kernel_size = 3 , padding = 'same')
    self.ELU6 = nn.ELU()

    self.conv7 = nn.Conv2d(32,32,kernel_size = 3 , padding = 'same')
    self.ELU7 = nn.ELU()

    self.conv8 = nn.Conv2d(32,32,kernel_size = 3 , padding = 'same')
    self.ELU8 = nn.ELU()

    self.conv9 = nn.Conv2d(32,4 , kernel_size = 3 , padding = 'same') 
    self.ELU9 = nn.ELU()

    self.depth2space = nn.PixelShuffle(r)

  def forward(self , x):
    x1 = self.conv1(x)
    x1 = self.ELU1(x1)

    x2 = self.conv2(x1)
    x2 = self.ELU2(x2)

    x3 = self.conv3(x2)
    x3 = self.ELU3(x3)
    x3 = x1 + x3 

    x4 = self.conv4(x3)
    x4 = self.ELU4(x4)
    x4 = x4 + x1 

    x5 = self.conv5(x4)
    x5 = self.ELU5(x5)

    x6 = self.conv6(x5)
    x6 = self.ELU6(x6)

    x7 = self.conv7(x6)
    x7 = self.ELU7(x7)
    x7 = x7 + x4 

    x8 = self.conv8(x7)
    x8 = self.ELU8(x8)
    x8 = x8 + x7
    
    x9 = self.conv9(x8)
    x9 = self.ELU9(x9)

    y = self.depth2space(x9)
    return y 





