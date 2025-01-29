
class FileDocumantation:
    '''
    File Operation
    '''
    def __init__(self):
        pass
    
    def create_file(self,path_file:str,name_file:str,type_file:str)->None:
        '''
        path_file : file save location
        name_file : file name
        type_file : file save type example txt,docx,json
        '''
        with open(f'{path_file}/{name_file}.{type_file}','x',encoding='utf-8') as file:
            file.close()
        
    def append_file(self,path_file:str,data:dict)->None:
        '''
        path_file : file save location
        name_file : file name
        data : add data type dictiniary or string 
        '''
        with open(path_file,'a',encoding='utf-8') as file:
            file.write(data)
    
    def write_file(self,path_file:str,data:dict)->None:
        '''
        path_file : file save location
        name_file : file name
        data : add data type dictiniary or string 
        '''
        with open(path_file,'w',encoding='utf-8') as file:
            file.write(data)
        
    def read_file(self,path_file:str)-> dict:
        '''
        path_file : file save location
        '''
        with open(path_file,'r',encoding='utf-8') as file:
            doc=file.read()
        return doc
    
    def bottom_line(self,path_file:str)->None:
        '''
        Within the text, the cursor moves to the bottom line.
        path_file : file save location
        '''
        with open(path_file,'a',encoding='utf-8') as file:
            file.write('\n')
            
    def update_file(self,path_file:str,data:str)->None:
        '''
        Within the text, the cursor is moved to the beginning and data is inserted at the beginning, 
        the previous text is not deleted.
        path_file : file save location
        '''
        with open(path_file,'r+',encoding='utf-8') as file:
            file.write(data)
            
    def change_file(self,path_file:str,change_data:str,new_data:str)->None:
        '''
        Within the text, the cursor is moved to the beginning and data is inserted at the beginning, 
        the previous text is not deleted.
        path_file : file save location
        change_data : The data to be changed in the text.
        new_data : New text to be written in its place.
        '''
        with open(path_file,'r+',encoding='utf-8') as file:
            doc=file.read()
            doc = doc.replace(change_data, new_data)
            file.seek(0)
            file.write(doc)
            file.truncate()