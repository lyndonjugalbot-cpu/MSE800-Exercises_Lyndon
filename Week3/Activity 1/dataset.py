from ucimlrepo import fetch_ucirepo 

class GetIrisData:

    def get_data(self):
        # fetch dataset 
        iris = fetch_ucirepo(id=53) 
  
        # data (as pandas dataframes) 
        X = iris.data.features 
        y = iris.data.targets
  
        # metadata 
        print("__" *50)
        print(iris.metadata) 
        print("__" *50)
  
        # variable information
        print("__" *50)
        print(iris.variables)
        print("__" *50)

        return X, y

    def unique_flowers(self, y):
        # unique flower species
        flower_names = y.iloc[:, 0].unique()
        print("Total number of different flowers:", len(flower_names))
        print("Total number of different flowers:", list(flower_names))