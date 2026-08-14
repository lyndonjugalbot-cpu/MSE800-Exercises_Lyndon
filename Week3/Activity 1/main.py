from dataset import GetIrisData

def main():
    iris_data = GetIrisData()
    X, y = iris_data.get_data()
    iris_data.unique_flowers(y)

if __name__ == "__main__":
    main()