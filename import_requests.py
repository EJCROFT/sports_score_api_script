# Description: This code is used to make a request to the API and save the response as JSON and CSV files.
import requests
import pandas as pd
import os
import json
import csv

# make a request to the API

url = "https://sportscore1.p.rapidapi.com/sports/1/teams"

querystring = {"page":"1"}

headers = {
	"X-RapidAPI-Key": "api_key",
	"X-RapidAPI-Host": "sportscore1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# assign the response to a variable (api_data)

if response.status_code == 200:
    api_data=response.json()

    #In this code, the response from the API is saved as JSON using the json.dump() function. It opens a file named teams.json in write mode and writes the JSON data into it. Finally, it prints a success message if the file is generated successfully.

    with open('teams.json','w') as json_file:
        json.dump(api_data, json_file)
               

    print("teams.json file has been generated successfully.")


    #In this function, the response from the API is saved as CSV using the csv.writer() function. It opens a file named teams.csv in write mode and writes the CSV data into it. Finally, it prints a success message if the file is generated successfully.
    

    def get_teams(data):
            
            

        #create a file path to save the csv file

        file_path = "path/to/teams.csv"
        with open(file_path, 'w') as f:

            #write to the header of csv file
            writer =csv.writer(f)
            writer.writerow(['id', 'name', 'country', 'founded', 'national', 'logo_path', 'venue_id', 'venue_name', 'venue_surface', 'venue_address', 'venue_city', 'venue_capacity'])
    #           write the data from python dic (api response in json) to csv
            for team in data['data']:
                writer.writerow([team['id'],
                                team['name'],
                                team.get('country', ''),
                                team.get('founded', ''), 
                                team.get('national', ''), 
                                team.get('logo_path', ''), 
                                team.get('venue_id', ''), 
                                team.get('venue_name', ''), 
                                team.get('venue_surface', ''), 
                                team.get('venue_address', ''), 
                                team.get('venue_city', ''), 
                                team.get('venue_capacity', '')
                                ])
                
            #create an if statement to check if the file has been created successfully
        if os.path.exists(file_path):

            print("teams.csv file has been generated successfully.")
        else:
            print("Error occurred while fetching the data.")

    get_teams(api_data) # call the get_teams function 

else:
    print("Error occurred while fetching the data.")

                
            
               
            


        

        








    

