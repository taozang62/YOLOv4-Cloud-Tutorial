import os

image_files = []
os.chdir('images_to_be_cleaned/')
filelist = os.listdir(os.getcwd())
# preprocess the filename list
filelist.sort()
filelist.pop(0)
length = len(filelist)
# print(length) ok
for i in range(length):
    curr_name = filelist[i]
    if i + 1 == length and curr_name.endswith(".jpg"):
        os.remove(curr_name)
        break
    if i + 1 < length:
        next_name = filelist[i + 1]
    if curr_name.endswith(".jpg") and next_name.endswith(".jpg"):
        os.remove(curr_name)
        continue
    if curr_name.endswith(".jpg") and next_name.endswith(".txt"):
        i = i + 1
        continue
newFileList = os.listdir(os.getcwd())
newFileList.sort()
newFileList.pop(0)
print(newFileList)

idx = -1
for i in range(len(newFileList)):
    if i % 2 == 0: idx += 1
    filename = newFileList[i]
    i1 = filename.index(':')
    i2 = filename.index(',')
    os.rename(filename, 'image-' + str(idx) + '_' + filename[i1+1:i2] + '_' + filename[i2+1:])
