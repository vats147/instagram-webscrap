# Import necessary libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import pandas as pd





# Define the web driver
# driver = webdriver.Chrome()


websites= [ "https://www.instagram.com/virat.kohli"]

#path of your webdriver c:path\to\your\webdriver\chromedriver.exe 
driver = webdriver.Chrome(executable_path=r'C:\Users\username\Downloads\chromedriver_win32 (1)\chromedriver.exe')

# Replace with your own Instagram username and password
username = 'your_username'
password = 'your_password'

#promt login 
driver.get('https://www.instagram.com/accounts/login')

# Wait for the login page to load
time.sleep(5)

# Enter username and password and click on the login button
username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')

# username_field = driver.find_element_by_name('username')
# password_field = driver.find_element_by_name('password')
username_field.send_keys(username)
password_field.send_keys(password)

# submit the login form
password_field.submit()


# Wait for the page to load and verify that you're logged in
time.sleep(5)


# List to store the results
results = []

#temp list
temp =[]
for website in websites:
    # Open the website in the web driver
    driver.get(website)

    # Wait for the page to load
    time.sleep(5)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find all <h2> tags with the specified class
    h2_tags = soup.find_all("h2")

     # Find all <li> tags with the specified class inside the <ul> tag
    ul_tag = soup.find("ul", class_="x78zum5")
    li_tags = ul_tag.find_all("li", class_="xl565be")


    # print name of website
    print("Current Website: " + website)
    
    # Loop through each <h2> tag and extract the text
    for h2_tag in h2_tags:
        # Extract the text from the <h2> tag
        h2_text = h2_tag.text.strip()

        # Print the text
        print(f"{website}: {h2_text}")
              # Store the website name and the <h2> text in the results list
        #results.append((website, h2_text))
    temp=[]
    for li_tag in li_tags:
        # Extract the text from the <li> tag
        li_text = li_tag.text.strip()
       
        # Print the text
        print(f"{website}: {li_text}")

        #append result in temp
        temp.append(li_text)
        
        # Store the website name and the <li> text in the results list
        #results.append((website, li_text))

    results.append((website,h2_text,tuple(temp)))    
    # print name of website
    print("Finished scraping " + website)
    print(results)

# Close the web driver
driver.quit()


# Define the filename for your CSV file
filename="result.csv"


# Create a DataFrame with columns 'url', 'username', 'stats'
df = pd.DataFrame(results, columns=['url', 'username', 'stats']) 

# Split the stats tuple into separate columns
df[['posts', 'followers', 'following']] = pd.DataFrame(df.stats.tolist(), index=df.index)

# extract numeric values from stats tuple and store them in separate columns
df['posts'] = df['stats'].apply(lambda x: int(''.join(filter(str.isdigit, x[0])))) 
df['followers'] = df['stats'].apply(lambda x: int(''.join(filter(str.isdigit, x[1])))) 
df['following'] = df['stats'].apply(lambda x: int(''.join(filter(str.isdigit, x[2]))))  

# Drop the original 'stats' column
df.drop('stats', axis=1, inplace=True) 

# Write DataFrame to CSV file
df.to_csv(filename, index=False)
