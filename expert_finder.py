# Code to return a list of names of who in the team knows a certain skill.
import pandas as pd

def return_expert (skill):
	'''Function which searches skills matrix for experts, returning their names.'''

	skills_df = pd.read_csv('/Users/admin/Documents/Away_Days/acebot/skills_matrix.csv')

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
