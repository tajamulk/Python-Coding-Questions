# Deleting files on condition based

for file in os.listdir(): # First have a dry run 
    if file.endswith('.txt'):
        print(file)

for file in os.listdir(): # Then delete files
    if file.endswith('.txt'):
        os.unlink(file)
