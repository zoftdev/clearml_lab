import clearml

from clearml import Task,Dataset

#load dataset

data= Dataset.get(dataset_id="68a52540085345c7b7f50ab47781e9b7")
local_path=data.get_local_copy()

print(local_path)
task=Task.init(project_name="titanic_demo", task_name="train the featurestore", reuse_last_task_id=False )

#list file in directory
import os
 
 
print(os.listdir(local_path))



import pandas as pd

train_df=pd.read_csv( f'{local_path}/train.csv')

print(train_df.head())


def mytrain( train_df,**kwargs):
    print("training")
    return 0.8
    
fs_artifact=task.get_task(data.id).artifacts 
key_category_to_title=fs_artifact['key_category_to_title'].get()
print(key_category_to_title)
task.logger.report_table("debug","head", table_plot=train_df.head())

mytrain(train_df)
task.close()