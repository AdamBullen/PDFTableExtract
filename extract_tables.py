import os
import tabula

def pull_tables(file_name, file_path):
    tables = tabula.io.read_pdf(file_path, pages='all', multiple_tables=True)

    for i, table in enumerate(tables):
        fname=f"""{file_name}_T{i}.csv"""
        table.to_csv(fname, index='False')

def process_dir(dir_path):
    for file_name in os.listdir(dir_path):
        if file_name.lower().endswith('.pdf'):
            file_path = os.path.join(dir_path, file_name)
            print(file_path)
            pull_tables(file_name, file_path)

def process_file(file_path):
    file_name = os.path.basename(file_path)
    pull_tables(file_name, file_path)