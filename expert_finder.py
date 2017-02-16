# Code to return a list of names of who in the team knows a certain skill.
import pandas as pd

def return_expert (command):
    '''Function which searches skills matrix for experts, returning their names.'''
    
    command_array = str.lower(command).split(' ')
    if len(command_array) < 3:
        response = "Who knows what?..."
    else:    
        skill = command_array[2]
        skills_df = pd.read_csv('./csv_inputs/skills_matrix.csv')

        for column in skills_df.columns.tolist():
            if str.lower(column) == skill:
                skill = column

        try:
            experts = skills_df[skill].dropna().tolist()
            if len(experts) == 0:
                response = 'Nobody has recorded knowledge in ' + skill + ', try Robin.'
            elif len(experts) == 1:
                response = experts[0]
            else:
                response = ', '.join(experts) + ' know ' + skill
        except:
            response = "acebot hasn't heard of " + skill

    return response

def df_to_dictionary (df):
    '''Changes a dataframe to a dictionary and removes any NaNs'''

    dictionary = {}
    
    for column in df.columns.tolist():
        values = [x for x in df[column].tolist() if str(x) != 'nan']
        dictionary[column] = values
        
    return dictionary

def add_expert (command, user):
    '''Function that adds user to skills matrix.
    Works by converting the dataframe to a dictionary and updating the values in that dictionary.'''

    forename = user.profile.first_name
    surname = user.profile.last_name
    full_name = str(forename) + str(surname)

    command_array = str.lower(command).split(' ')
    if len(command_array) < 3:
        response = "You know what?..."
    else:
        skill = command_array[2]
        
        skills_df = pd.read_csv('./csv_inputs/skills_matrix.csv')
        skills_dictionary = df_to_dictionary(skills_df)
    
        try:
            experts = skills_dictionary[skill]
            experts.append(full_name)
            skills_dictionary[skill] = experts
        except:
            skills_dictionary[skill] = [full_name]
        
        skills_df = pd.DataFrame.from_dict(skills_dictionary, orient='index').transpose()
        skills_df.to_csv('./csv_inputs/skills_matrix.csv', index=False)
        
        response = 'Okay, acebot has updated the skills matrix.'

    return response


