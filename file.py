
class FileDocumantation:
    def __init__(self):
        pass
    
    def create_file(self,path_file:str,name_file:str,type_file):
        file=open(f'{path_file}/{name_file}.{type_file}','w',encoding='utf')
        file.close()
        
    