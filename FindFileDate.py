import os

matches = []
for root, dirnames, filenames in os.walk('H'):
    print(dirnames)
    for filename in fnmatch.filter(filenames, '*'):
        matches.append(os.path.join(root, filename))
        print(filename)

'''for filename in glob.glob(os.path.join(os.getcwd(), '*.*')):
    filename1="D:\Hash\REP"+filename
	print("last modified: %s" % time.ctime(os.path.getmtime(filename1)))
	print("created: %s" % time.ctime(os.path.getctime(filename1)))'''
