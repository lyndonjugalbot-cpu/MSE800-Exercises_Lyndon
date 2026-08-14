from getdata import GetData

def main():
    get_data = GetData()

    #open file and read
    lines = get_data.read_data("junk.txt")

    # 1. Total number of lines
    get_data.get_lines(lines)

    # 2. Add a new line at the end of the file
    get_data.append_lines(lines)

    # 3. Convert all text in the file to lowercase
    lines = get_data.convert_lines(lines)

    data = open("junk.txt", "w")
    data.writelines(lines)
    data.close()

if __name__ == "__main__":
    main()