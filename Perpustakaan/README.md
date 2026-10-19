# REST API mini project: 📚 Perpustakaan(Flask & SQLAlchemy)
## 💻 System Requierement
     - Pyhton 3.10+(make sure to click the "Add Python to PATH" button befor download)
     - MySQL Database Server(you can use XAMPP or Laragon, but i use Laragon)
     - Postman(for API testing)
## 🗄  Database Configuration
1. Start Laragon. After installing Laragon, open the Laragon Control Panel and click Start All to start the required services.
2. Open phpMyAdmin. In the Laragon Control Panel, click Menu, select MySQL, and then click phpMyAdmin.
3. Log in to phpMyAdmin. Your browser will open the phpMyAdmin login page. By default, Laragon uses the following credentials:
    - Username: root
    - Password: Leave this field empty.
4. Enter root as the username, leave the password field blank, and click Log in.
5. When you finally login to the phpMyAdmin page, you will see this page:
   <img src="images/laragon.png" alt="Laragon Control Panel" width="600">
7. In the navigation bar above, pick the "SQL" button, and it will lead you to the SQL Query Editor

    <img src="images/navigation_bar.png" alt="navigation_bar" width="600">
    
    <img src="images/sql_button.png" alt="sql_button" width="600">
    
    <img src="images/SQLQueryEditor.png" alt="SQLQueryEditor" width="600">
8.In the the SQL Query Editor Create the database name "perpustakaan" with the following Query:

     CREATE DATABASE perpustakaan;
    
## 🚀 To run the application

### 1. Make a folder to make 
Create a new folder on your Desktop where you want to store your project.

For example, you can create a folder named ```Github project```.

### 2. Clone the Repository
Open your terminal (Command Prompt, PowerShell, or VS Code terminal) and run


For example, if you created GitHub Projects on your Desktop, run:
```
cd Desktop
cd "GitHub Projects"
```
Next, run the following command to clone the repository from GitHub:

```
git clone https://github.com/Anya10032004/RestAPIMiniProject_Perpustakaan
```
Git will download the repository and create a new folder containing the project files.

### 3. Open the Project Folder
Next, enter the downloaded folder by running:

```
cd "<Folder_location>\RestAPIMiniProject_Perpustakaan"
```
### 4. Make a virtual enviroment
After that, we will make a virtual enviroment with a name perpustakaan, we will need to the following commands:

```
python -m venv perpustakaan
```

### 5. Activate the virtual enviroment
Commands to  activate the virtual enviroment is based on terminal you will use:

- Windows PowerShell:

   ```
   .\perpustakaan\Scripts\Activate.ps1
   ```
   
- Windows Command Prompt (CMD):
  
   ```
   .\perpustakaan\Scripts\Activate.ps1
   ```
   
- Git Bash / Linux / macOS:
  
  ```
  source perpustakaan/Scripts/activate
  ```
You can tell that the virtual environment is active when you see the prefix (perpustakaan) at the beginning of your terminal prompt.

### 6. Install the Required Libraries

### 7. Configure the Database Connection
  Open main.py and find the database connection configuration. Set it to the following URL:
        ```
        mysql+pymysql://root:@localhost:3306/perpustakaan
        ```
   | Component       | Value           | Description                                                                                                                                    |
   |-----------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
   | Database Driver | `mysql+pymysql` | Specifies MySQL as the database and PyMySQL as the Python driver.                                                                              |
   | Username        | `root`          | The MySQL username used to connect to the database.                                                                                            |
   | Password        | Empty           | No password is configured for this setup.                                                                                                      |
   | Host            | `localhost`     | Connects to MySQL running on your own computer. If MySQL runs on another server, replace `localhost` with the server's IP address or hostname. |
   | Port            | `3306`          | The default MySQL port. Change it if your MySQL server uses a different port.                                                                  |
   | Database Name   | `perpustakaan`  | The name of the database created in Step 8.                                                                                                    |
   
   **Important**: Make sure the username, password, host, port, and database name match your MySQL configuration. If you use a password, add it after root: in the connection URL.
   
   **Note**: This configuration assumes MySQL is running locally and the root account has no password. For production environments, use a dedicated database user with a strong password instead of the root account.



```   
pip install -r requirements.txt
```
This installs the Python libraries required by the project.
### 8. Run the app

Run the ```app.py```:

    python main.py
    
If it works the output will be:

```
 * Serving Flask app 'main'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 
```
The ```penulis```, ```kategori```, and ```buku``` tabbles will be automattically made when we run the app 
    
## ⚙️ API testing
