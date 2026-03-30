# The 'with' statement automatically closes the file for you

with open('example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # .strip() removes the newline character (\n) from the end
        list.append(line.strip())
        
