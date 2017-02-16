def whos_on_what(input_text):    
    
    import xlrd
    import pandas as pd
    
    name_list = ["Hayden", "Jon", "Ross", "Robin", "Sam", "Karik", "Dan J", "Dan H", "George", "Andy", "Vicky", "Ben"]
    found_names = []

    for i in name_list:
        if i.lower() in input_text.lower():
            found_names.append(i)
        
    # Will need to update this link depending on where the doc is stored
    people_tracker = xlrd.open_workbook("/Users/dddteam/Documents/Python Projects/Ace_bot/acebot/People_tracker.xls")

    # Get the first worksheet
    people_sheet = people_tracker.sheet_by_name("People")

    # Find the location of the requested names 
    names = found_names

    loc_df = pd.DataFrame(columns=["Project Col", "Name", "Row", "Column"])

    for j in range(people_sheet.ncols):
        for i in range(people_sheet.nrows):
            if people_sheet.cell(i,j).value == "Projects":
                project_row_id = i
                project_column_id = j
                project = people_sheet.cell(i,j).value

    for j in range(people_sheet.ncols):
        for i in range(people_sheet.nrows):    
            if people_sheet.cell(i,j).value in names:
                    row_id = i
                    column_id = j
                    value = people_sheet.cell(i,j).value
                    search_dict = {"Project Col":[project_column_id], "Name":[value], "Row":[row_id], "Column":[column_id]}
                    name_df = pd.DataFrame(data=search_dict)
                    loc_df = loc_df.append(name_df)

    loc_df = loc_df.drop_duplicates("Name") 

    # Set up a dataframe of people and projects
    people_df = pd.DataFrame(columns=["Name", "Object", "Value"])

    for index, row in loc_df.iterrows():

        project_col = int(row["Project Col"])
        name = row["Name"]
        name_col = int(row["Column"])
        first_row = int(row["Row"])

        for i in range(first_row, people_sheet.nrows):
            if type(people_sheet.cell(i,name_col).value) == float:
                people_dict = {"Name":[name], "Object":[ people_sheet.cell(i,project_col).value], "Value":[people_sheet.cell(i,name_col).value]}
                temp_df = pd.DataFrame(people_dict)
                people_df = people_df.append(temp_df)


    unique_people = people_df.Name.unique()
    number_people = len(unique_people)
    final_return = []

    for i in range(number_people):
        current_person = unique_people[i]
        person_projects_string = []
        count_string = []
        fte_string = []
        person_projects_string.append(current_person + " is working on the projects: ")
        projects_count_pp = 0

        for index, row in people_df.iterrows():
            if row["Name"] == current_person:
                if row["Object"].strip() == "Count":
                    count_string.append(current_person + " is working on " + str(row["Value"]) + " different projects")
                elif row["Object"].strip() == "FTE":
                    if row["Value"] > 1.0:
                        fte_string.append(current_person + " has a FTE of: " + str(row["Value"]) + ". " + " They may be working too hard...")
                    else:
                        fte_string.append(current_person + " has a FTE of: " + str(row["Value"]))
                else:
                    person_projects_string.append(str(row["Object"]) + " for an FTE of: " + str(row["Value"]) + " ")


        print_projects = ",".join(person_projects_string)

        final_return.append(count_string)
        final_return.append(fte_string) 
        final_return.append(print_projects)

    return(final_return)