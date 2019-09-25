import os
import glob
#import docx
##
##   print(filename)
##   f = open(filename, 'r')
##   content = f.read()
##   if content=="PII":
##       print(filename)
##     doc = docx.Document(filename)
##     for para in doc.paragraphs:
##         if "PII" in para.text:
##             print("HEYA")
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'
s=['secure flag not set in cookie','application is vulnerable to back refresh','application timeout not set','webserver fingerprinting']
temp_list=[]
freq_data={}
temp_list=[]
for filename in glob.glob(os.path.join(os.getcwd(), '*.docx')):
    document = zipfile.ZipFile(filename)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)
    a=""
    cnt=0
    rt=0
    #print(filename)
    
    for paragraph in tree.getiterator(PARA):
        if cnt!=1:
            texts = [node.text for node in paragraph.getiterator(TEXT) if node.text]
            
            for a in texts:
            #print(a.lower())
                if "dynamic analysis" in a.lower():
                    rt=1
                
                if "web service assessment" in a.lower():
                    cnt=1
                if rt==1:
                    if a.lower() not in ['dynamic analysis','web service assessment']:
                        #print(a.lower())
                        temp_list.append(a.lower())
                if a.lower() in s:
                
                    if a.lower() not in temp_list:
                        temp_list.append(a.lower())
                        if a.lower() in freq_data.keys():         
                            freq_data[a.lower()]+=1
                        else:
                            freq_data[a.lower()]=1
                #print(s)
                #print("--------")
                #print(a)
print("---------------------------------------")
temp_list1=[x for x in temp_list if not(x.isdigit())]
temp_list2=[]
for t in temp_list1:
    try:
        float(t)
    except ValueError:
        if "web service assessment" not in t:
            temp_list2.append(t)
        continue
    #print(t)
#print(temp_list2)
temp_list3=[]
for t in temp_list2:
    result = ''.join(i for i in t if not i.isdigit())    
    temp_list3.append(result)
    result=''
print(temp_list3)

##for filename in glob.glob('*.txt'):
##   # do your stuff

##path = '/some/path/to/file'
##
##for filename in os.listdir(path):
##    # do your stuff
##
##for filename in glob.glob(os.path.join(path, '*.txt')):
