import pandas as pd
import time
import skfuzzy as fuzz


def space():
    print("\n\n")
    print("-".center(100,"-"))
    print("\n\n")
    time.sleep(1)


def unique(data):
    print("The numerical data in the csv file contains the following parameters respectively: \n\n")
    print(data['Gender'].unique())
    print(data['family_history_with_overweight'].unique())
    print(data['FAVC'].unique())
    print(data['CAEC'].unique())
    print(data['SMOKE'].unique())
    print(data['SCC'].unique())
    print(data['CALC'].unique())
    print(data['MTRANS'].unique())
    

def main():
    print("\n\n")
    print("Welcome".center(100," "))
    space()

    # read the dataset
    data = pd.read_csv("ObesityDataSet.csv")

    # drop the last column
    data = data.drop(['NObeyesdad'], axis=1)

    # get the head of the dataset
    print(data.head())
    space()

    # get unique values from the dataset that we want to apply
    # one hot encoding on

    unique(data=data)
    space()

    # set columns as category
    datas = ["Gender","Age","Height","Weight","family_history_with_overweight","FAVC","FCVC","NCP","CAEC","SMOKE","CH2O","SCC","FAF","TUE","CALC","MTRANS"]
    print("ONE HOT ENCODED DATA")
    one_hot_encoded_data = pd.get_dummies(data, columns = ['Gender', 'family_history_with_overweight',"FAVC","CAEC","SMOKE","SCC","CALC","MTRANS"])
    print(one_hot_encoded_data)
    space()

    # removes missing/empty values
    one_hot_encoded_data = one_hot_encoded_data.dropna()

    # printing one hot encoded data
    print("ENCODED DATA")
    print(one_hot_encoded_data)
    print(one_hot_encoded_data.head())
    space()

    # converting to int and T/F values to 0 or 1
    print("INT DATA")
    df = one_hot_encoded_data*1
    df = df.astype('int')
    print(df)
    space()


    # this has clustering method taken with the help of AI but there are errors so we comment this out

    '''
    cntr, u, u0, d, jm, p, fpc = fuzz._cluster.cmeans(data.T, 7, 2, error=0.005, maxiter=1000)

    clusters = []
    for i in range(len(u.T)):
        cluster = u.T[i].argmax()
        clusters.append(cluster)

    weights = ['Insufficient Weight', 'Normal Weight', 'Overweight Level I', 'Overweight Level II', 'Obesity Type I', 'Obesity Type II', 'Obesity Type III']
    matrix = [[0 for x in range(7)] for y in range(7)]

    for i in range(1,len(clusters)):
        weight = weights.index(data.iloc[i]['FAF'])
        matrix[clusters[i]][weight] += 1
    print(pd.DataFrame(matrix, columns=weights, index=['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5', 'Cluster 6', 'Cluster 7']))
    '''


main()