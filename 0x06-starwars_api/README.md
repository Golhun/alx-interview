
# Star Wars Characters 🌌✨

## Overview 🚀  
The **Star Wars Characters** project is a Node.js-based application that interacts with the [Star Wars API](https://swapi.dev) to fetch and display information about Star Wars characters. By providing a movie ID as an argument, the program retrieves the names of all characters appearing in that movie and displays them in order. This project demonstrates the use of web programming, API interaction, and asynchronous JavaScript concepts.

---

## Features 🌟  
- Fetch character data from the Star Wars API 🌠  
- Retrieve and display character names based on the provided movie ID 🎥  
- Efficient handling of asynchronous API calls using `async/await` ⏳  
- Clean, semistandard-compliant code with no usage of `var` 🛠️  

---

## Getting Started 📖  

### Prerequisites 🛠️  
Ensure you have the following installed on your system:  
- **Node.js** (v10.14.x)  
- **npm** (Node Package Manager)  
- **semistandard** (Code linting tool)  

### Installation 🖥️  
1. Install Node.js:  
   ```bash
   $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   $ sudo apt-get install -y nodejs
   ```  

2. Install the `semistandard` linter globally:  
   ```bash
   $ sudo npm install semistandard --global
   ```  

3. Install the `request` module globally:  
   ```bash
   $ sudo npm install request --global
   $ export NODE_PATH=/usr/lib/node_modules
   ```  

---

## Usage 🖱️  
1. Clone this repository:  
   ```bash
   $ git clone <repository_url>
   $ cd <project_directory>
   ```  

2. Run the script with a movie ID:  
   ```bash
   $ ./<script_name>.js <movie_id>
   ```  
   Example:  
   ```bash
   $ ./0-star_wars_characters.js 1
   ```  

3. The output will display the names of all characters in the specified movie, in the order they appear.  

---

## Concepts Demonstrated 📚  

### HTTP Requests 🌐  
- Making API calls using the `request` module.  
- Parsing JSON responses.  

### Asynchronous Programming ⚡  
- Managing API calls with `async/await`.  
- Handling errors and managing asynchronous data flows.  

### Command-Line Arguments 🧩  
- Using `process.argv` to handle user input.  

### Array Manipulation 🌀  
- Iterating over data and formatting it for display.  

---

## Project Requirements ✅  
- **Ubuntu 20.04 LTS** compatibility.  
- Semistandard-compliant code.  
- No usage of `var`.  
- All files are executable and end with a new line.  

---

## Example Output 🎉  
Command:  
```bash
$ ./0-star_wars_characters.js 1
```  

Output:  
```text
Luke Skywalker  
Leia Organa  
Darth Vader  
Han Solo  
Obi-Wan Kenobi  
...  
```

---

## Author 👨‍💻  
**[Your Name]**  
- GitHub: [Your GitHub Profile](https://github.com/YourUsername)  
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/YourUsername)  

---

Enjoy coding, and may the Force be with you! 🌟
