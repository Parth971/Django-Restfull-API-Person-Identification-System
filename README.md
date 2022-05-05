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
  
  
<h2>Run API</h2>
  &emsp; 1. Install Requirement.txt <br>
  &emsp; 2. Run this Django API via <code>python manage.py runserver</code> <br> 
  &emsp;(Default superuser username: <strong>admin</strong>, pass: <strong>admin123</strong>) <br>
  &emsp; 3. Open POSTman (Used for request and response analysis) <br>

<h2>Endoints</h2>
&emsp; [POST] Reqires: token | [user_id] in url, [role] in request body <br>
&emsp; <code>/api/users/user_id/ </code> <br> 
&emsp; [POST] Reqires: [username, email, password1, password2] in request body <br>
&emsp; <code>/api/signup/ </code> <br> 
&emsp; [POST] Reqires: [username, password] in request body <br>
&emsp; <code>/api/signin/ </code> <br> 
&emsp; [GET] Reqires: token <br>
&emsp; <code>/api/signout/ </code> <br> 
&emsp; [GET] Reqires: token <br>
&emsp; <code>/api/aadhar/ </code> <br> 
&emsp; [POST] Reqires: token | [aadhar_no, is_active] in request body <br>
&emsp; <code>/api/aadhar/ </code> <br> 
&emsp; [GET] Reqires: token | [aadhar_no] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/ </code> <br> 
&emsp; [PATCH] Reqires: token | [aadhar_no] in url, [is_active] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/ </code> <br> 
&emsp; [DELETE] Reqires: token | [aadhar_no] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/ </code> <br> 
&emsp; [GET] Reqires: token | [aadhar_no] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/address/ </code> <br> 
&emsp; [POST] Reqires: token | [aadhar_no] in url, [street, city, state, postal_code] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/address/ </code> <br> 
&emsp; [GET] Reqires: token | [aadhar_no, address_id] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/address/address_id/</code> <br> 
&emsp; [PATCH] Reqires: token | [aadhar_no, address_id] in url, [street, city, state, postal_code] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/address/address_id/</code> <br> 
&emsp; [DELETE] Reqires: token | [aadhar_no, address_id] in url<br>
&emsp; <code>/api/aadhar/aadhar_no/address/address_id/</code> <br> 
&emsp; [GET] Reqires: token | [aadhar_no] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/qualification/ </code> <br> 
&emsp; [POST] Reqires: token | [aadhar_no] in url, [institute_name, passing_year, percentage] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/qualification/ </code> <br> 
&emsp; [PATCH] Reqires: token | [aadhar_no] in url, [institute_name, passing_year, percentage] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/qualification/ </code> <br> 
&emsp; [DELETE] Reqires: token | [aadhar_no] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/qualification/ </code> <br> 
&emsp; [GET] Reqires: token | [aadhar_no] in url<br>
&emsp; <code>/api/aadhar/aadhar_no/bank/ </code> <br> 
&emsp; [POST] Reqires: token | [aadhar_no] in url, [account_number, bank_name, ifsc_code] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/bank/ </code> <br> 
&emsp; [PATCH] Reqires: token | [aadhar_no] in url, [account_number, bank_name, ifsc_code] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/bank/ </code> <br> 
&emsp; [DELETE] Reqires: token | [aadhar_no] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/bank/ </code> <br> 
&emsp; [GET] Reqires: token | [aadhar_no] in url<br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/ </code> <br> 
&emsp; [POST] Reqires: token | [aadhar_no] in url, [full_name, dob, blood_group] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/ </code> <br> 
&emsp; [PATCH] Reqires: token | [aadhar_no] in url, [full_name, dob, blood_group] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/ </code> <br> 
&emsp; [DELETE] Reqires: token | [aadhar_no] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/ </code> <br> 
&emsp; [GET] Reqires: token | [aadhar_no] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/contact/ </code> <br> 
&emsp; [POST] Reqires: token | [aadhar_no] in url, [contact] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/contact/ </code> <br> 
&emsp; [GET] Reqires: token | [aadhar_no, contact_id] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/contact/contact_id/ </code> <br> 
&emsp; [PATCH] Reqires: token | [aadhar_no, contact_id] in url, [contact] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/contact/contact_id/ </code> <br> 
&emsp; [DELETE] Reqires: token | [aadhar_no, contact_id] in url<br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/contact/contact_id/ </code> <br> 
&emsp; [GET] Reqires: token | [aadhar_no] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/email/ </code> <br> 
&emsp; [POST] Reqires: token | [aadhar_no] in url, [email] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/email/ </code> <br> 
&emsp; [GET] Reqires: token | [aadhar_no, email_id] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/email/email_id/ </code> <br> 
&emsp; [PATCH] Reqires: token | [aadhar_no, email_id] in url, [email] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/email/email_id/ </code> <br> 
&emsp; [DELETE] Reqires: token | [aadhar_no, email_id] in url<br>
&emsp; <code>/api/aadhar/aadhar_no/personal_detail/email/email_id/ </code> <br> 
&emsp; [GET] Reqires: token | [aadhar_no] in url<br>
&emsp; <code>/api/aadhar/aadhar_no/past_job_experience/ </code> <br> 
&emsp; [POST] Reqires: token | [aadhar_no] in url, [company_name, job_role, year_of_work_experience] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/past_job_experience/ </code> <br> 
&emsp; [PATCH] Reqires: token | [aadhar_no] in url, [company_name, job_role, year_of_work_experience] in request body <br>
&emsp; <code>/api/aadhar/aadhar_no/past_job_experience/ </code> <br> 
&emsp; [DELETE] Reqires: token | [aadhar_no] in url <br>
&emsp; <code>/api/aadhar/aadhar_no/past_job_experience/ </code> <br> 
&emsp; [GET] Reqires: token | [is_active(True, False), aadhar_no, sort(descending, default=ascending)] in url <br>
&emsp; <code>/api/personal_details/ </code> <br> 
&emsp; [POST] Reqires: [username, password] in body <br>
&emsp; <code>/api-token-auth/ </code> <br> 
