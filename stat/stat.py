import pandas
from scipy import stats
experiments_data = pandas.read_csv("experiments.csv")
df11 = pandas.DataFrame(data ={
    'df1': pandas.read_csv("experiments.csv")['experiments']
    })
print(stats.kstest(df11['df1'],'norm'))
