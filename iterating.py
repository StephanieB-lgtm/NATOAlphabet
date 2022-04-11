student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas
dataframe=pandas.DataFrame(student_dict)
new_dic = {row.student:row.score for (index, row) in dataframe.iterrows()}
print(new_dic)
