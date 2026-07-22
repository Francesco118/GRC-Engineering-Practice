#READ
with open ("log-sample.txt", "r") as log_file: #Open the log file in read mode (r)
    log_contents = log_file.readlines() # Read the contents of the log file
    log_contents = [line.strip() for line in log_contents] #removes blank lines and whitespace from the beginning and end of each line
    for line in log_contents:
        print(line) #each line of the log file is printed to the console

#PARSE

#COUNT