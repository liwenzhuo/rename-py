import os
def rename(path, oriext, repext):
	#当前py文件的目录
	curdir = path #os.path.split(os.path.realpath(__file__))[0]
	allfile = os.listdir(curdir)
	for fi in allfile:
		fn  = os.path.splitext(fi)[0]
		ext = os.path.splitext(fi)[1][1:]
		if ext == oriext:
			ofi = fn + '.' + repext
			#print (os.path.join(curdir,fi))
			#print (os.path.join(curdir,ofi))
			os.rename(os.path.join(curdir,fi), os.path.join(curdir,ofi))

rename(os.path.split(os.path.realpath(__file__))[0], 'c', 'cpp')