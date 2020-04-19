#!/usr/bin/env python
# coding: utf-8

# In[1]:


def int_file(path):
    import os
    filename, file_extension = os.path.splitext(path)
    # Findind file or folder
    e = []
    if file_extension != '':
        print('You uploaded a File')
        e.append(path)

    if file_extension == '':
        print('It is Folder')
        p = os.listdir(path)
        #e = [path+'\\'+i for i in p]
        print('It contains following files',p)
        k = input('Which file you need to read from this folder : ')
        e = [path+'\\'+k]
        if k not in p:
            print('Your input is wrong!')
        exit()
        
    #Assigning Extension to check in input files
    xl_ext  = ['.json','.xls','.xlsx','.csv']
    doc_ext = ['.pdf','.txt','.docx']
    img_ext = ['.png','.jpg','.jpeg']
    def Filter(file,extensions):
        k=[]
        for i in range(len(file)):
            for j in extensions:
                if e[i].endswith(j):
                    a = e[i]
                    k.append(a)
        return k
    xl_file = Filter(e,xl_ext)
    doc_file = Filter(e,doc_ext)
    img_file = Filter(e,img_ext)
    xl_list  = []
    doc_list = []
    img_list = []
    # File Def function to read excel, csv files
   
    def file_all(file):
        import pandas as pd
        from tika import parser
        from PIL import Image
        if file.endswith('.json'):
            try:
                jsn_f = pd.read_json(file)
            except:
                jsn_f = pd.read_json(file, typ='series')
            file = jsn_f 

        elif file.endswith('.xls'):
            exl_f = pd.read_excel(file)
            file = exl_f
        elif file.endswith('.xlsx'):
            exls_f = pd.read_excel(file)
            file = exls_f

        elif file.endswith('.csv'):
            sep_dil = [',',':',';','\n', '\r','\r\n',' ','\r\t']
            # Getting Input
            k = str(input ("CSV File is Uploaded \nEnter Seperator :") or ',')
            # check it for input validity
            if k in sep_dil :
                print("Entered Seperator : ", k)
            else:
                print('Error, It is not a valid seperator')
            csv_f = pd.read_csv(file,sep=k)
            file = csv_f

        elif file.endswith('.pdf'):
            pdf_f = parser.from_file(file)['content']
            file = pdf_f
        elif file.endswith('.txt'):
            pdf_f = parser.from_file(file)['content']
            file = pdf_f        
        elif file.endswith('.docx'):
            pdf_f = parser.from_file(file)['content']
            file = pdf_f
    
        from PIL import Image
        if file.endswith('.jpg'):
            file = Image.open(file)
        if file.endswith('.jpeg'):
            file = Image.open(file)
        if file.endswith('.png'):
            file = Image.open(file)
        return file
    
    file = file_all(e[0])
    
    try: 
        return_file = file
    except:
        return_file = print('\n\nSorry can\'t read that file....!')
    
    return return_file

