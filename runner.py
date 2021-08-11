import subprocess

def run():
    
    # open text.txt and readlines and store it in content
    with open('text.txt', 'r') as f:
        content = f.readlines()
        content = content[1:] # Removing the first line (```) from the code block
        # found that it is a list
        # print(type(content)) 
        content[-1] = content[-1].rstrip("```") # Removing the last ``` from the code block
        
        # opening another file test.py and writing to that file
        with open('test.py', 'w') as file:
            for line in content:
                file.write(line)
            file.close()
    f.close()
        #print(content[-1])

    command = f'python test.py'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output