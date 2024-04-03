from address_function import address_selection
from banking_function import banking_selection
from ssn_function import ssn_selection
from phone_number_function import phone_number_selection
from login_function import login_selection
from email_function import email_selection
from password_function import password_selection
from birth_function import birth_selection
from gender_function import gender_selection
from nationality_function import nationality_selection
from occupation_function import occupation_selection
from education_function import education_selection
from medical_function import medical_selection
from insurance_function import insurance_selection
from passport_function import passport_selection
from legal_function import legal_selection
from ethnicity_function import ethnicity_selection

    
user_choices = {    
    'address_choices' : ['1', 'one', 'One', 'Address Information', 'Address information', 'address information', 'Address Info', 'Address info', 'address info', 'Address', 'address'],
    'banking_choices' : ['2', 'two', 'Two', 'Banking Information', 'Banking information', 'banking information', 'Bank Information', 'Banking information', 'banking information', 'Banking Info', 'Banking info', 'banking info', 'Bank Info', 'Bank info', 'bank info'],
    'ssn_choices' : ['3', 'three', 'Three', 'Social Security Number Information', 'Social security number information', 'social security number information', 'Social Security Information', 'Social security information', 'social security information', 'Social Security Number Info', 'Social security number info', 'social security number info', 'Social Securtiy Info', 'Social security info', 'social security info', 'SSN Information', 'SSN information', 'ssn information', 'SSN Info', 'SSN info', 'ssn info', 'Social Security Number', 'Social security number', 'social security number', 'Social Security', 'Social security', 'social security', 'SSN', 'ssn'],
    'phone_number_choices' : ['4', 'four', 'Four', 'Phone Number Information', 'Phone number information', 'phone number information', 'Phone Number Info', 'Phone number info', 'phone number info', 'Phone Number', 'Phone number', 'phone number'],
    'login_choices' : ['5', 'five', 'Five', 'Login Information', 'Login information', 'login information', 'Login Info', 'Login info', 'login infop', 'Login', 'login'],
    'email_choices' : ['6', 'six', 'Six', 'Email Information', 'Email information', 'email information', 'Email Info', 'Email info', 'email info', 'Email', 'email'],
    'password_choices' : ['7', 'seven', 'Seven', 'Password', 'password', 'Password Information', 'Password information', 'password information', 'Password Info', 'Password info', 'password info'],
    'birth_choices' : ['', 'Birthday Information', 'Birthday information', 'birthday information', 'Birthday Info', 'Birthday info', 'birthday info', 'Birthday', 'birthday', 'Date of Birth', 'Date of birth', 'date of birth', 'Birth', 'birth'],
    'gender_choices' : ['', 'Gender Information', 'Gender information', 'gender information', 'Gender Info', 'Gender info', 'gender info', 'Gender', 'gender'],
    'nationality_choices' : ['', 'Nationality Information', 'Nationality information', 'nationality information', 'Nationality Info', 'Nationality info', 'nationality info', 'Nationality', 'nationality'],               
    'occupation_choices' : ['', 'Occupation Information', 'Occupation information', 'occupation information', 'Occupation Info', 'Occupation info', 'occupation info', 'Job Information', 'Job information', 'job information', 'Job Info', 'Job info', 'job info', 'Occupation', 'occupation', 'Job', 'job'],
    'education_choices' : ['', 'Education Information', 'Education information', 'education information', 'Education Info', 'Education info', 'education info', 'Education', 'education'],
    'medical_choices' : ['', 'Medical Information', 'Medical information', 'medical information', 'Medical Info', 'Medical info', 'medical info', 'Medical', 'medical'],
    'insurance_choices' : ['', 'Insurance Information', 'Insurance information', 'insurance information', 'Insurance Info', 'Insurance info', 'insurance info', 'Insurance', 'insurance'], 
    'driving_choices' : ['', 'Drivers License', 'Drivers license', 'drivers license', 'Driving Information', 'Driving information', 'driving information', 'Driving Info', 'Driving info', 'driving info', 'Driving', 'driving'],
    'passport_choices' : ['', 'Passport Information', 'Passport information', 'passport information', 'Passport Info', 'Passport info', 'passport info', 'Passport', 'passport'],
    'legal_choices' : ['', 'Legal Information', 'Legal information', 'legal information', 'Legal Info', 'Legal info', 'legal info', 'Legal', 'legal'],
    'ethnicity_choices' : ['', 'Ethnicity Information', 'Ethnicity information', 'ethnicity information', 'Ethnicity Info', 'Ethnicity info', 'ethnicity info', 'Ethnicity', 'ethnicity'],

    'save_address_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Address', 'Save address', 'save address', 'Save Billing Address', 'Save billing address', 'save billing address'],
    'save_banking_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Banking Information', 'Save banking information', 'save banking information', 'Save Banking Info', 'Save banking info', 'save banking info'],
    'save_ssn_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Social Security Number', 'Save social security number', 'save social security number', 'Save Social Security', 'Save social security', 'save social security', 'Save SSN', 'Save ssn', 'save SSN', 'save ssn'],
    'save_phone_number_choices' : ['1', 'one', 'Save', 'save', 'One', 'Save Phone Number', 'Save phone number', 'save phone number', 'Save Number', 'Save number', 'save number'],
    'save_login_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Login', 'Save login', 'save login'],
    'save_email_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Email', 'Save email', 'save email'],  
    'save_password_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Password', 'Save password', 'save password'],
    'save_birth_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Birthday', 'Save birthday', 'save birthday', 'Save Date of Birth', 'Save date of birth', 'save date of birth'],
    'save_gender_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Gender', 'Save gender', 'save gender'],
    'save_nationality_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Nationality', 'Save nationality', 'save nationality'],
    'save_occupation_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Occupation', 'Save occupation', 'save occupation', 'Save Job', 'Save job', 'save job'],
    'save_education_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Education', 'Save education', 'save education'],
    'save_medical_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Medical Information', 'Save medical information', 'save medical information', 'Save Medica Info', 'Save medical info', 'save medical info'],
    'save_insurance_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Insurance', 'Save insurance', 'save insurance'],
    'save_driving_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Drivers License', 'Save drivers license', 'save drivers license'],
    'save_passport_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Passport', 'Save passport', 'save passport'],
    'save_legal_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Legal Information', 'Save legal information', 'save legal information'],
    'save_ethnicity_choices' : ['1', 'one', 'One', 'Save', 'save', 'Save Ethnicity', 'Save ethincity', 'save ethnicity'],

    'see_banking_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See saved banking information', 'see saved banking information', 'See saved banking info', 'see saved banking info', 'See Banking Information', 'See banking information', 'See Banking Info', 'See banking info', 'see banking info', 'View saved banking information', 'view saved banking information', 'View saved banking info', 'view saved banking info', 'View Banking Information', 'View banking information', 'View Banking Info', 'View banking info', 'view banking info'],
    'see_address_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Address', 'See saved address', 'see saved address', 'See Address', 'See address', 'see address', 'View Saved Address', 'View saved address', 'view saved address', 'View Address', 'View address', 'view address'],
    'see_ssn_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See saved social security number', 'see saved social security number', 'See saved social security', 'see saved social security', 'See saved SSN', 'See saved ssn', 'See saved ssn', 'see saved ssn', 'see saved SSN', 'See social security number', 'see saved security number', 'See social security', 'see social security', 'See SSN', 'see SSN', 'See ssn', 'see ssn', 'View saved social security number', 'view saved social security number', 'View saved social security', 'sview saved social security', 'View saved SSN', 'View saved ssn', 'View saved ssn', 'view saved ssn', 'view saved SSN', 'View social security number', 'view saved security number', 'View social security', 'view social security', 'View SSN', 'view SSN', 'View ssn', 'view ssn'],
    'see_phone_number_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view','See Saved Phone Number', 'See saved phone number', 'see saved phone number', 'See Phone Number', 'See phone number', 'see phone number', 'See Saved Number', 'See saved number', 'see saved number', 'See Number', 'See number', 'see number', 'View Saved Phone Number', 'View saved phone number', 'view saved phone number', 'View Saved Number', 'View saved number', 'view saved number', 'View Phone Number', 'View phone number', 'view phone number', 'View Number', 'View number', 'view number'],
    'see_login_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Login', 'See saved login', 'see saved login', 'See Saved logins', 'See saved logins', 'see saved logins', 'See Login', 'See login', 'see login', 'See Logins', 'See logins', 'see logins', 'View Saved Login', 'View saved login', 'view saved login', 'View Saved Logins', 'View saved logins', 'view saved logins', 'View Login', 'View login', 'view login', 'View Logins', 'View logins', 'view logins'],
    'see_email_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Email', 'See saved email', 'see saved email', 'See Email', 'See email', 'see email', 'View Saved Email', 'View saved email', 'view saved email', 'View Email', 'View email', 'view email'],
    'see_password-Choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Password', 'See saved password', 'see saved password', 'See Password', 'See password', 'see password', 'View Saved Password', 'View saved password', 'view saved password', 'View Password', 'View password', 'view password'],
    'see_birth_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Birthday', 'See saved birthday', 'see saved birthday', 'See Saved Date of Birth', 'See saved date of birth', 'see saved date of birth', 'See Birthday', 'See birthday', 'see birthday', 'See Date of Birth', 'See date of birth', 'see date of birth', 'View Saved Birthday', 'View saved birthday', 'view saved birthday', 'View Saved Date of Birth', 'View saved date of birth', 'view saved date of birth', 'View Birthday', 'View birthday', 'view birthday', 'View Date of Birth', 'View date of birth', 'view date of birth'],
    'see_gender_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Gender', 'See saved gender', 'see saved gender', 'See Gender', 'See gender', 'see gender', 'View Saved Gender', 'View saved gender', 'view saved gender', 'View Gender', 'View gender', 'view gender'],
    'see_nationality_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Nationality', 'See saved nationality', 'see saved nationality', 'See Nationality', 'See nationality', 'see nationality', 'View Saved Nationality', 'View saved nationality', 'view saved nationality', 'View Nationality', 'View nationality', 'view nationality'],
    'see_occupation_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Occupation', 'See saved occupation', 'see saved occupation', 'See Saved Job', 'See saved job', 'see saved job', 'See Occupation', 'See occupation', 'see occupation', 'See Job', 'See job', 'see job', 'View Saved Occupation', 'View saved occupation', 'view saved occupation', 'View Saved Job', 'View saved job', 'view saved job', 'View Occupation', 'View occupation', 'view occupation', 'View Job', 'View job', 'view job'],
    'see_education_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Educations', 'See saved education', 'see saved education', 'See Education', 'See education', 'see education', 'View Saved Education', 'View saved education', 'view saved education', 'View Education', 'View education', 'view education'],
    'see_medical_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Medical Information', 'See saved medical information', 'see saved medical information', 'See Saved Medical Info', 'See saved medical info', 'see saved medical info', 'See Medical Information', 'See medical information', 'see medical information', 'See Medical Info', 'See medical info', 'see medical info', 'View Saved Medical Information', 'View saved medical information', 'view saved medical information', 'View Saved Medical Info', 'View saved medical info', 'view saved medical info'],
    'see_insurance_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Insurance', 'See saved insurance', 'see saved insurance', 'See Insurance', 'See insurance', 'see insurance', 'View Saved Insurance', 'View saved insurance', 'view saved insurance', 'View Insurance', 'View insurance', 'view insurance'],
    'see_driving_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Drivers License', 'See saved drivers license', 'see saved drivers license', 'See Drivers Lisence', 'See drivers license', 'see drivers license', 'See Drivers License', 'See drivers license', 'see drivers license', 'View Saved Drivers License', 'View saved drivers license', 'view saved drivers license', 'View Drivers License', 'View drivers license', 'view saved drivers license'],
    'see_passport_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Passport', 'See saved passport', 'see saved passport', 'See Passport', 'See passport', 'see passport', 'View Saved Passport', 'View saved passport', 'view saved passport', 'View Passport', 'View passport', 'view passport'],
    'see_legal_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Legal Information', 'See saved legal information', 'see saved legal information', 'See Saved legal Info', 'See saved legal info', 'see saved legal info', 'See Legal Information', 'See legal information', 'see legal information', 'See Legal Info', 'See legal info', 'see legal info', 'View Saved Legal Information', 'View saved legal information', 'view saved legal information', 'View Saved Legal Info', 'View saved legal info', 'view saved legal info', 'View Legal Information', 'View legal information', 'view legal information', 'View Legal Info', 'View legal info', 'view legal info'],
    'see_ethnicity_choices' : ['2', 'two', 'Two', 'See', 'see', 'View', 'view', 'See Saved Ethnicity', 'See saved ethnicity', 'see saved ethnicity', 'See Ethnicity', 'See ethnicity', 'see ethnicity', 'View Saved Ethnicity', 'View saved ethnicity', 'view saved ethnicity', 'View Ethnicity', 'View ethnicity', 'view ethnicity'],

    'delete_bannking_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Banking Information', 'Delete banking information', 'delete banking information', 'Delete Saved Banking Information', 'Delete saved banking information', 'delete saved banking information'],
    'delete_address_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Address', 'Delete address', 'delete address', 'Delete Saved Address', 'Delete saved address', 'delete saved address'],
    'delete_ssn_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Social Security Number', 'Delete social security number', 'delete social security number', 'Delete Saved Social Security Number', 'Delete saved social security number', 'delete saved social security number', 'Delete Social Security', 'Delete social security', 'delete social security', 'Delete Saved Social Security', 'Delete saved social security', 'delete saved social security', 'Delete SSN', 'Delete ssn', 'delete ssn', 'Delete saved SSN', 'Delete saved ssn', 'delete saved ssn'],
    'delete_phone_number_choices' : ['3', 'three', 'Three', 'Delete Phone Number', 'Delete phone number', 'delete phone number', 'Delete Saved Phone Number', 'Delete saved phone number', 'delete saved phone number', 'Delete Number', 'Delete number', 'delete number', 'Delete Saved Number', 'Delete saved number', 'delete saved number'],
    'delete_login_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Login', 'Delete login', 'delete login', 'Delete Saved Login', 'Delete saved login', 'delete saved login', 'Delete Logins', 'Delete logins', 'delete logins', 'Delete Saved Logins', 'Delete saved logins', 'delete saved logins'],
    'delete_email_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Email', 'Delete email', 'delete email', 'Delete Saved Email', 'Delete saved email', 'delete saved email', ''],
    'delet_password_choices' : ['3', 'three', 'Three', 'Delete', 'delete', 'Delete Password', 'Delete password', 'delete password', 'Delete Saved Password', 'Delete saved password', 'delete saved password'],
    'delete_birth_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Birthday', 'Delete birthday' 'delete birthday', 'Delete Date of Birth', 'Delete date of birth', 'delete date of birth', 'Delete Saved Birthday', 'Delete saved birthday', 'delete saved birthday', 'Delete Saved Date of Birth', 'Delete saved date of birth', 'delete saved date of birth'],
    'delete_gender_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Gender', 'Delete gender', 'delete gender', 'Delete Saved Gender', 'Delete saved gender', 'delete saved gender'],
    'delete_nationality_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Nationality', 'Delete nationality', 'delete nationality', 'Delete Saved Nationality', 'Delete saved nationality', 'delete saved nationality'],
    'delete_occupation_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Occupation', 'Delete occupation', 'delete occupation', 'Delete Job', 'Delete job', 'delete job', 'Delete Saved Job', 'Delete saved job', 'delete saved job'],
    'delete_education_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Education', 'Delete education', 'delete education', 'Delete Saved Education', 'Delete saved education', 'delete saved education'],
    'delete_medical_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Medical Information', 'Delete medical information', 'delete medical information', 'Delete Medical Info', 'Delete medical info', 'delete medical info', 'Delete Saved Medical Information', 'Delete saved medical information', 'delete saved medical information', 'Delete Saved Medical Info', 'Delete saved medical info', 'delete saved medical info'],
    'delete_insurance_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Edit Insurance', 'Edit insurance', 'edit insurance', 'Delete Insurance Information', 'Delete insurance information', 'delete insurance information', 'Delete Insurance Info', 'Delete insurance info', 'delete insurance info', 'Delete Insurance', 'Delete insurance', 'delete insurance', 'Delete Saved Insurance Information', 'Delete saved insurance information', 'delete saved insurance information', 'Delete Saved Insurance Info', 'Delete saved insurance info', 'delete saved insurance info', 'Delete Saved Insurance', 'Delete saved insurance', 'delete saved insurance'],
    'delete_driving_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Drivers Lisence', 'Delete drivers lisence', 'delete drivers lisence', 'Delete Driving Information', 'Delete driving information', 'delete driving information', 'Delete Driving Info', 'Delete driving info' , 'delete driving info', 'Delete Saved Drivers Lisence', 'Delete saved drivers lisence', 'delete saved drivers lisence', 'Delete Saved Driving Information', 'Delete saved driving information', 'delete saved driving information', 'Delete Saved Driving Info', 'Delete saved driving info', 'delete saved driving info'],
    'delete_passport_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Passport', 'Delete passport', 'delete passport', 'Delete Saved Passport', 'Delete saved passport', 'delete saved passport'],
    'delete_legal_choices' : ['3', 'three', 'Three', 'delete', 'Delete', 'Delete Legal Information', 'Delete legal information', 'delete legal information', 'Delete Legal Info', 'Delete legal info', 'delete legal info', 'Delete Saved Legal Information', 'Delete saved legal information', 'delete saved legal information', 'Delete Saved Legal Info', 'Delete saved legal info', 'delete saved legal info'],
    'delete_ethnicity_choices' : ['3', 'three', 'Three', 'Delete Ethnicity', 'Delete ethnicity', 'delete ethnicity', 'Delete Saved Ethnicity', 'Delete saved ethnicity', 'delete saved ethnicity'],
    
    'edit_address_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Adress', 'Edit address', 'edit address', 'Edit Saved Address', 'Edit saved address', 'edit saved address'],
    'edit_banking_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Banking Information', 'Edit banking information', 'edit banking information', 'Edit Saved Banking Information', 'Edit saved banking information', 'edit saved banking information', 'Edit Banking Info', 'Edit banking info', 'edit banking info', 'Edit Saved Banking Info', 'Edit saved banking info', 'edit saved banking info'],
    'edit_ssn_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Social Security Number', 'Edit social security number', 'edit social security number', 'Edit SSN', 'Edit ssn', 'edit ssn', 'Edit Saved Social Security Number', 'Edit saved social security number', 'edit social security number', 'Edit Saved SSN', 'Edit saved SSN', 'Edit saved ssn', 'edit saved ssn'],
    'edit_phone_number_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Phone Number', 'Edit phone number', 'edit phone number', 'Edit Saved Phone Number', 'Edit saved phone number'],
    'edit_login_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Login', 'Edit login', 'edit login', 'Edit Saved Login', 'Edit saved login', 'edit saved login'],
    'edit_email_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Email', 'Edit email', 'edit email', 'Edit Saved Email', 'Edit saved email', 'edit saved email'],
    'edit_password_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Password', 'Edit password', 'edit password', 'Edit Saved Password', 'Edit saved password', 'edit saved password'],
    'edit_birth_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Birthday', 'Edit birthday', 'edit birthday', 'Edit Date Of Birth', 'Edit Date of Birth', 'EDit date of birth', 'Edit Saved Birthday', 'Edit saved birthday', 'edit saved birthday', 'Edit Saved Date Of Birth', 'Edit Saved Date of Birth', 'Edit saved date of birth', 'edit saved date of birth'],
    'edit_gender_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Gender', 'Edit gender', 'edit gender', 'Edit Saved Gender', 'Edit saved gender', 'edit saved gender'],
    'edit_nationality_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Nationality', 'Edit nationality', 'edit nationality', 'Edit Saved Nationality', 'Edit saved nationality', 'edit saved nationality'],
    'edit_occupation_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Occupation', 'Edit occupation', 'edit occupation', 'Edit Saved Occupation', 'Edit saved occupation', 'edit saved occupation'],
    'edit_education_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Education', 'Edit education', 'edit education', 'Edit Saved Education', 'Edit saved education', 'edit saved education'],
    'edit_medical_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Medical Information', 'Edit medical information', 'edit medical information', 'Edit Medical Info', 'Edit medical info', 'edit medical info', 'Edit Saved Medical Information', 'Edit saved medical information', 'edit saved medical information', 'Edit Saved Medical Info', 'Edit saved medical info', 'edit saved medical info'],
    'edit_insurance_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Insurance', 'Edit insurance', 'edit insurance', 'Edit Insurance Information', 'Edit insurance information', 'edit insurance information', 'Edit Insurance Info', 'Edit insurance info', 'edit insurance info', 'Edit Saved Insurance', 'Edit saved insurance', 'edit saved insurance', 'Edit Saved Insurance Information', 'Edit saved insurance information', 'edit saved insurance information', 'Edit Saved Insurance Info', 'Edit saved insurance info', 'edit saved insurance info'],
    'edit_driving_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Drivers License', 'Edit drivers license', 'edit drivers license', 'Edit Driving Information', 'Edit driving information', 'edit driving information', 'Edit Driving Info', 'Edit driving info', 'edit driving info', 'Edit Saved Drivers License', 'Edit saved drivers license', 'edit saved drivers license', 'Edit Saved Driving Info', 'Edit saved driving info', 'edit saved driving info'],
    'edit_passport_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Passport', 'Edit passport', 'edit passport', 'Edit Saved Passport', 'Edit saved passport', 'edit saved passport'],
    'edit_legal_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Legal', 'Edit legal', 'edit legal', 'Edit Legal Information', 'Edit legal information', 'edit legal information', 'Edit Legal Info', 'Edit legal info', 'edit legal info', 'Edit Saved Legal', 'Edit saved legal', 'edit saved legal', 'Edit Saved Legal Information', 'Edit saved legal information', 'edit saved legal information', 'Edit Saved Legal Info', 'Edit saved legal info', 'edit saved legal info'],
    'edit_ethnicity_choices' : ['4', 'four', 'Four', 'edit', 'Edit', 'Edit Ethnicity', 'Edit ethnicity', 'edit ethnicity', 'Edit Saved Ethnicity', 'Edit saved ethnicity', 'edit saved ethnicity'],
}
        
error_handling_positive = {
    'save_address_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_address_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_banking_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_banking_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_ssn_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_ssn_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_phone_number_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_phone_number_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_login_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_login_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_email_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_email_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_password_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_password_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_birth_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_birth_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_gender_choices' : ['Yes', 'yes', 'Y', 'y',],
    'dont_delete_gender_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_nationality_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_nationality_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_occupation_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_occupation_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_education_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_education_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_medical_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_medical_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_insurance_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_insurance_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_driving_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_driving_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_passport_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_passport_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_legal_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_legal_choices' : ['Yes', 'yes', 'Y', 'y'],
    'save_ethnicity_choices' : ['Yes', 'yes', 'Y', 'y'],
    'dont_delete_ethnicity_choices' : ['Yes', 'yes', 'Y', 'y'],
}

error_handling_negative = {
    'dont_save_address_choices' : ['No', 'no', 'N', 'n'],
    'delete_address_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_banking_choices' : ['No', 'no', 'N', 'n'],
    'delete_banking_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_ssn_choices' : ['No', 'no', 'N', 'n'],
    'delete_ssn_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_phone_number_choices' : ['No', 'no', 'N', 'n'],
    'delete_phone_number_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_login_choices' : ['No', 'no', 'N', 'n'],
    'delete_login_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_email_choices' : ['No', 'no', 'N', 'n'],
    'delete_email_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_password_choices' : ['No', 'no', 'N', 'n'],
    'delete_password_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_birth_choices' : ['No', 'no', 'N', 'n'],
    'delete_birth_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_gender_choices' : ['No', 'no', 'N', 'n'],
    'delete_gender_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_nationality_choices' : ['No', 'no', 'N', 'n'],
    'delete_nationality_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_occupation_choices' : ['No', 'no', 'N', 'n'],
    'delete_occupation_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_education_choices' : ['No', 'no', 'N', 'n'],
    'delete_education_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_medical_choices' : ['No', 'no', 'N', 'n'],
    'delete_medical_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_insurance_choices' : ['No', 'no', 'N', 'n'],
    'delete_insurance_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_driving_choices' : ['No', 'no', 'N', 'n'],
    'delete_driving_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_passport_choices' : ['No', 'no', 'N', 'n'],
    'delete_passport_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_legal_choices' : ['No', 'no', 'N', 'n'],
    'delete_legal_choices' : ['No', 'no', 'N', 'n'],
    'dont_save_ethnicity_choices' : ['No', 'no', 'N', 'n'],
    'delete_ethnicity_choices' : ['No', 'no', 'N', 'n'],
}

def personal_information_selection():
    print('Address\'s')
    print('Banking Information')
    print('Social Security Number')
    print('Phone Number')
    print('Login')
    print('Email')
    print('Password')
    print('Date of Birth')
    print('Gender')
    print('Nationality')
    print('Occupation')
    print('Education')
    print('Medical Information')
    print('Insurance Information')
    print('legal Information')
    print('Ethnicity')

    user_selection = input('Choose one of the following options: ')
    
    selection_functions = {
    'address_choices' : address_selection,
    'banking_choices' : banking_selection,
    'ssn_choices' : ssn_selection,
    'phone_number_choices' : phone_number_selection,
    'login_choices' : login_selection,
    'email_choices' : email_selection,
    'password_choices' : password_selection,
    'birth_choices' : birth_selection,
    'gender_choices' : gender_selection,
    'nationality_choices' : nationality_selection,
    'occupation_choices' : occupation_selection,
    'education_choices' : education_selection,
    'medical_choices' : medical_selection,
    'insurance_choices' : insurance_selection,
    'passport_choices' : passport_selection,
    'legal_choices' : legal_selection,
    'ethnicity_choices' : ethnicity_selection, 
}
    if user_selection in selection_functions:
        selection_functions[user_selection]()
    else:
        print("Invalid choice. Please try again.")
        personal_information_selection()

    if user_selection in selection_functions['address_choices']:
        address_selection()
    elif user_selection in selection_functions['banking_choices']:
        banking_selection()
    elif user_selection in selection_functions['ssn_choices']:
        ssn_selection()
    elif user_selection in selection_functions['phone_number_choices']:
        phone_number_selection()
    elif user_selection in selection_functions['login_choices']:
        login_selection()
    elif user_selection in selection_functions['email_choices']:
        email_selection()
    elif user_selection in selection_functions['password_choices']:
        password_selection()
    elif user_selection in selection_functions['birth_choices']:
        birth_selection()
    elif user_selection in selection_functions['gender_choices']:
        gender_selection()
    elif user_selection in selection_functions['nationality_choices']:
        nationality_selection()
    elif user_selection in selection_functions['occupation_choices']:
        occupation_selection()
    elif user_selection in selection_functions['education_choices']:
        education_selection()
    elif user_selection in selection_functions['medical_choices']:
        medical_selection()
    elif user_selection in selection_functions['insurance_choices']:
        insurance_selection()
    elif user_selection in selection_functions['passport_choices']:
        passport_selection()
    elif user_selection in selection_functions['legal_choices']:
        legal_selection()
    elif user_selection in selection_functions['ethnicity_choices']:
        ethnicity_selection()
    
    for key, value in user_choices.items():
        if user_selection.lower() in value:
            selection_functions[key]()
            break
    else:
        print("Invalid choice. Please try again.")
        personal_information_selection() 
        
def main():
    personal_information_selection()
    
if __name__ == "__main__":
    main()                                                                                                                                    