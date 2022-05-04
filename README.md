<h1>Django Restfull API</h1>

This is Django Restfull API for Person Identification based on Aadhar Number. <br>
Basically, this api helps in creating Aadhar card and Related details. <br>
Ontop of that it also has feature to filter and sort Personal Details based on Aadhar number and its active status.

<h2>REQUIREMENTS: Person Identification System</h2>

<h3>Workflow:</h3>
  ➢ Person Detailed Information can be retrieved using AADHAR <br>
  Number [E.g. Enter a Persons AADHAR Number and get all the details related to that AADHAR Number.].<br>
  ➢ Basic User Sign in/Signup <br>
  ➢ Only Token Authenticated User is Able to 
    Create/Read/Update/Delete Information. <br>
  ➢ Filter/Sort Person Details according to the following Tables. <br>
  ➢ Person Active Status using AADHAR Number. <br>
  ➢ Fetch/Sort Active / Inactive AADHAR Number. <br>
  ➢ Create Individual Endpoints According to the following Tables.<br>
    [E.g. https://example.com/Aadhar/Address , https://example.com/Aadhar/Bank ]
    
<h3>Type of User:</h3>
    ▪ Manager - Create/View /Update/Delete <br>
    ▪ Staff - View <br>
    
<h3>TABLES:</h3>
    1. AADHAR <br>
      &emsp;• Aadhar Number (Primary Key) <br>
      &emsp;• Is_Active (Boolean Field) <br>
    2. ADDRESS (Person can have Multiple Address) <br>
      &emsp;• Street <br>
      &emsp;• City <br>
      &emsp;• State <br>
      &emsp;• Postal Code <br>
    3. QUALIFICATION <br>
      &emsp;• Name of College / School <br>
      &emsp;• Year of Passing <br>
      &emsp;• Percentage <br>
    4. BANK <br>
      &emsp;• Account Number <br>
      &emsp;• Bank Name <br>
      &emsp;• IFSC Code <br>
    5. Personal Details <br>
      &emsp;• Full Name <br>
      &emsp;• Date of Birth <br>
      &emsp;• Blood Group <br>
      &emsp;• Contact Number (Person/ Individual can Have Multiple contact Number) <br>
      &emsp;• Email (Person/ Individual can have Multiple email id’s) <br>
    6. Past Job Experience <br>
      &emsp;• Company name <br>
      &emsp;• Job Role <br>
      &emsp;• Year of Work Experience <br>
      
      
<h2>ASSUMPTIONS: </h2>
      - SQLite Database <br>
      - Non Browsable API <br>
      
<h2>Requirements.txt</h2>
  &emsp;- python-3.8.10 <br>
  &emsp;- django-4.0.4 <br>
  &emsp;- rest_framework-3.13.1 <br>
  &emsp;- django-crispy-forms <br>
  
  
<h2>Run API</h2>
  &emsp; 1. Install Requirement.txt <br>
  &emsp; 2. Run this Django API via ```python manage.py runserver```
  &emsp; 3. Open POSTman (Used for request and response analysis)

<h2>Endoints</h2>
&emsp; /api/users/user_id/ <br>
&emsp; /api/signup/ <br>
&emsp; /api/signin/ <br>
&emsp; /api/signout/ <br>
&emsp; /api/aadhar/ <br>
&emsp; /api/aadhar/aadhar_no/ <br>
&emsp; /api/aadhar/aadhar_no/address/ <br>
&emsp; /api/aadhar/aadhar_no/address/<int:address_id>/ <br>
&emsp; /api/aadhar/aadhar_no/qualification/ <br>
&emsp; /api/aadhar/aadhar_no/bank/ <br>
&emsp; /api/aadhar/aadhar_no/personal_detail/ <br>
&emsp; /api/aadhar/aadhar_no/personal_detail/contact/ <br>
&emsp; /api/aadhar/aadhar_no/personal_detail/contact/contact_id/ <br>
&emsp; /api/aadhar/aadhar_no/personal_detail/email/ <br>
&emsp; /api/aadhar/aadhar_no/personal_detail/email/email_id/ <br>
&emsp; /api/aadhar/aadhar_no/past_job_experience/ <br>
&emsp; /api/personal_details/ <br>
  
  
