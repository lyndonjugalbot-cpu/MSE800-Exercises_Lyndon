data = open("junk.txt", "r")
lines = data.readlines()
data.close()

# 1. Total number of lines
total_lines = len(lines)
print(f"Total number of lines: {total_lines}")

# 2. Add a new line at the end of the file
lines.append("text file nanalyssis\n")

# 3. Convert all text in the file to lowercase
lines = [line.lower() for line in lines]

data = open("junk.txt", "w")
data.writelines(lines)
data.close()
