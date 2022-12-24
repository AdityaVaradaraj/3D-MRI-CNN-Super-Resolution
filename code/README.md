# ENPM809K Final Project - Group 6
## Convolutional Neural Networks with Intermediate Loss for 3D Super-Resolution of CT and MRI Scans

Code for training CNN for 3D medical images super resolution.

Set the ```folder_name``` and ```resize_factor``` according to your needs.

your dataset should have the following format:

path/to/your/data/set/subject_name/input_train_64_2/1.png

path/to/your/data/set/subject_name/input_train_64_2/2.png

.....

path/to/your/data/set/subject_name/gt_train_64_2/1.png

path/to/your/data/set/subject_name/gt_train_64_2/2.png

......

In order to train h and w model (on height and width),
- you first need to prepare your data (Convert from NIFTI or nii.gz to PNG format) (nibabel and imageio libraries can be used for this). Input for h and w network should be 128 PNG images of 256 x 256 per subject. 
- Then you will have to create patches using the code in "h and w/preprocessing.py" and giving appropriate paths, resize factor and patch dimensions. 
- Then use appropriate paths in the various .ipynb files. Change 'user' variable and corr. path according to your file storage structure. 
- Run all cells of custom_train_h_w.ipynb for training the height and width network
- New dataset for the d network must have been generated using the last few cells of code in the custom_train_h_w.ipynb with folders 'Subject_1', 'Subject_2', etc. each containing input_train_d_64_2, gt_train_d_64_2, etc.
- Also model checkpoints should be created if proper path changes and directories are made
- This may take a very long time. Alternatively, run the cells to np.save() the elements of 'subjects', i.e., the list of 3D numpy arrays as .npy files which might run and reflect much faster. Then run resize_train_d() on a list containing 3D array of 1 subject at a time to create the patches and resize to get data for depth. 

In order to test h and w model (on height and width),
- Run all the cells of custom_test_h_w.ipynb

In order to train the d (depth) model,
- Make appropriate path changes and user changes
- Run all cells of custom_train_d.ipynb
- Model Checkpoints will be generated
- Running the last few cells should help visualize the output images and compare with ground truth visually.
