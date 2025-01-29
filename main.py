import filedocumantation 

filedic=filedocumantation.FileDocumantation()


filedic.write_file(
    path_file='./doc/deneme.txt',
    data='write data\n'
)

filedic.append_file(
    path_file='./doc/deneme.txt',
    data='add data'
)

reading=filedic.read_file(
    path_file='./doc/deneme.txt'
)

print('old : '+reading+'\n')

filedic.bottom_line(
    path_file='./doc/deneme.txt'
)

filedic.change_file(
    path_file='./doc/deneme.txt',
    change_data='add',
    new_data='change'
)

reading=filedic.read_file(
    path_file='./doc/deneme.txt'
)

print('new : '+reading)