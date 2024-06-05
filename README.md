# Innovation_hub_sys

This repository is about an Innovation Hub system craeted in Flask.
It stores the data about the hub in the MySQL database basically in 
Four tables for-starters 
## Mmembers table
    1.member_id
    2.member_name
    3.members_email
    4.faculty_id  
   
## Collaboration table
    1.collaboration_id
    2.project_id
    3.member_id

## Projects table
    1.project_id
    2.project_name
    3.project_description
    4.faculty_id
    

## Faculties table
    1.faculty_id
    2.faculty_name

##  We all the above information about the data that the database schema expects 
you can add the data basing on that which was added before. You need to run the 
flask application using this command 
"flask --app ihs.py run --debug"
then visit the browser at http://127.0.0.1:5000/


