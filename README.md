# 3D-MRI-CNN-Super-Resolution
## CNN-based Super-resolution in all 3 directions of 3D MRI scans from IXI dataset 

This is a modified version of the CNN-IL method proposed in the paper [1]. The modified network has different architecture with different skip connections, position of upsampling layer, ELU activations and different no. of layers. It is explained in detail in the report. As shown in the report, our modified network performs better than the one in the paper.

### Dataset Used: IXI Dataset

### References:
[1] M. I. Georgescu, R. T. Ionescu and N. Verga, ”Convolutional Neural Networks With Intermediate Loss for 3D Super-Resolution of CT and MRI Scans,” in IEEE Access, vol. 8, pp. 49112-49124, 2020, doi: 10.1109/ACCESS.2020.2980266.

### Output of original model in the paper:

![original_d_visualization](https://user-images.githubusercontent.com/34472717/209449889-3cff5a6a-d82a-479e-8f07-c7387d54b018.jpeg)

### Output of Our Model:

![custom_d_visualization](https://user-images.githubusercontent.com/34472717/209449872-b591b522-8a3a-48f2-a248-8978d37454f8.jpeg)
