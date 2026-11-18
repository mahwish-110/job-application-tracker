import streamlit as st
import requests
API_URL="http://127.0.0.1:5000"
st.set_page_config(
    page_title=" Job Application Tracker",
    page_icon="💼",
    layout="centered"
)
if "logged_in" not in st.session_state:
   st.session_state.logged_in=False

if "token" not in st.session_state:
    st.session_state.token=None   

st.title("💼 Job Application Tracker")
st.subheader("Welcome!")
st.write("Keep track of your job applications, interviews and progress")
st.divider()

if st.session_state.logged_in:
   st.title("📊 Dashboard")
   st.subheader("Welcome to job Application Tracker!")
   st.write("Manage and track all your job applications in one place.")
   st.divider()

   headers={
       "Authorization": f"Bearer {st.session_state.token}"
   }
   try:
       response=requests.get(
           API_URL+"/api/applications",
           headers=headers
       )
       if response.status_code==200:
           applications=response.json()

           total = len(applications)
           st.metric("Total Applications", total)
           applied_count = 0
           interview_count=0
           selected_count=0
           rejected_count=0

           for app in applications:
               if app["status"]=="Applied":
                   applied_count+=1
               elif app["status"]=="Interview":
                   interview_count+=1
               elif app["status"]=="Selected":
                   selected_count+=1
               elif app["status"]=="Rejected":
                   rejected_count+=1

           st.subheader("📊 Application Summary")

           summary = {
                "Status": ["Applied", "Interview", "Selected", "Rejected"],
                "Count": [
                    applied_count,
                    interview_count,
                    selected_count,
                    rejected_count
               ]
           }

           st.dataframe(summary,hide_index=True)
           st.dataframe(applications)

           st.divider()
           st.subheader("➕ Add New Applications")

           company_name=st.text_input("Company Name")
           job_role=st.text_input("job role")
           status=st.selectbox(
           "Application Status",
           ["Applied","Interview","Selected","Rejected"])
           if st.button("Add Application"):
               
               data={
                   "company_name":company_name,
                   "job_role":job_role,
                   "status":status
               }

               response=requests.post(
                   API_URL+"/api/applications",
                   json=data,
                   headers=headers
               )
               if response.status_code==201:
                   st.success("Appliction added successfully!")

               else:
                   st.error("Unable to add applicatio")

           st.divider()
           st.subheader("✏️ Update Applications") 

           application_options={}
           for app in applications:
               application_options[app["id"]]=(
                   app["company_name"]+"-"+app["job_role"]
               )
           selected_id=st.selectbox(
                "Select Application",
                options=list(application_options.keys()),
                format_func=lambda x:application_options[x]
            ) 
           new_status=st.selectbox(
               "Select New Status",
               ["Applied","Interview","Selected","Rejected"]
           ) 
           if st.button("Update Application"):
               data={
                   "status":new_status
               }
               response=requests.put(
                   API_URL+f"/api/applications/{selected_id}",
                   json=data,
                   headers=headers
               )
               if response.status_code==200:
                   st.success("Application updated successfully!")

               else:
                   st.error("unable to update application")
               
           st.divider()
           st.subheader("🗑️ Delete Applications")

           delete_id=st.selectbox(
               "select Application to delete",
               options=list(application_options.keys()),
               format_func=lambda x:application_options[x],
               key="delete_pplication"
           )
           if st.button("Delete Application"):
               response=requests.delete(
                   API_URL+f"/api/applications/{delete_id}",
                   headers=headers
               )
               if response.status_code==200:
                   st.success("Application deleted successfully!")
               else:
                   st.error("Unable to delete application")

       else:
           st.error("Unable to fetch applications")

   except requests.exceptions.ConnectionError:
       st.error("Cannot connect to Flask backend")

   if st.button("Logout"):
       st.session_state.logged_in=False
       st.session_state.token=None
       st.rerun()
else:
   with st.form("login_form"):

         email=st.text_input("Enter your Email")
         password=st.text_input("Enter your Password",type="password")
         login_button=st.form_submit_button("Login")

         if login_button:
            if email and password:
               try:
                   response=requests.post(
                       API_URL+"/api/login",
                       json={
                           "email":email,
                           'password':password
                       }
                   )
                   if response.status_code==200:
                       result=response.json()

                       st.session_state.token=result["token"]
                       st.session_state.logged_in=True

                       st.rerun()

                   else:
                       result=response.json()
                       st.error(result["error"])

               except requests.exceptions.ConnectionError:
                   st.error("Cannot connect to flask backend")

            else:
               st.warning("Please fill all fields")
            