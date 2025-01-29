
class FileDocumantation:
    def __init__(self):
        pass
    
    def create_file(self,path_file:str,name_file:str,type_file)->None:
        file=open(f'{path_file}/{name_file}.{type_file}','x',encoding='utf-8')
        file.close()
        
    def append_file(self,path_file:str,data:dict)->None:
        file=open(path_file,'a',encoding='utf-8')
        file.write(data)
        file.close()
    
    def write_file(self,path_file:str,data:dict)->None:
        file=open(path_file,'w',encoding='utf-8')
        file.write(data)
        file.close()
        
    def read_file(self,path_file:str)-> dict:
        file=open(path_file,'r',encoding='utf-8')
        doc=file.read()
        file.close()
        return doc