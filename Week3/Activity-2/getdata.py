class GetData:
    def read_data(self,filename):
        #open file and read
        data = open(filename, "r")
        lines = data.readlines()
        data.close()
        return lines

    def get_lines(self,total_lines):
        #get total number of lines
        total_lines = len(total_lines)
        print(f"Total number of lines: {total_lines}")

    def append_lines(self,lines):
        #append text to the file
        lines.append("text file nanalyssis\n")


    def convert_lines(self,lines):
        #Convert all text in the file to lowercase
        lines = [line.lower() for line in lines]
        return lines