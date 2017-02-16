# Code to return a list of names of who in the team knows a certain skill.
import pandas as pd

def return_expert (command):
    '''Function which searches skills matrix for experts, returning their names.'''

    skill = str.lower(command).split(' ')[2]
    
    skills_df = pd.read_csv('./csv_inputs/skills_matrix.csv')

    for column in skills_df.columns.tolist():
        if str.lower(column) == skill:
            skill = column

    try:
        experts = skills_df[skill].dropna().tolist()
        if len(experts) == 0:
            answer = 'Nobody has recorded knowledge in ' + skill + ', try Robin.'
        elif len(experts) == 1:
            answer = experts[0]
        else:
            answer = ', '.join(experts)
    except:
        answer = "acebot hasn't heard of " + skill

    return answer
