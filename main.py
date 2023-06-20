from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Welcome to the API"}


@app.get("/api")
def get_c(funct : str):
    if(funct == 'calculator'):
         return """#include <iostream>
#include <cstring>

void calculator()
{
    char num1[8];
    char buffer1[8];
    char num2[8];
    char buffer2[8];
    char operation[2];
    char bufferOp[2];

    std::cout << "Calculator\n";

    while (true)
    {
        std::cout << "Enter the first number (or 'q' to quit): ";
        std::cin >> num1;

        // Check for exit condition
        if (strcmp(num1, "q") == 0)
            return;

        std::cout << "Enter the operation (+, -, *, /): ";
        std::cin >> operation;

        // Intentional buffer overflow vulnerabilities
        strcpy(buffer1, num1);
        strcpy(bufferOp, operation);

        std::cout << "Enter the second number: ";
        std::cin >> num2;

        // Intentional buffer overflow vulnerability
        strcpy(buffer2, num2);

        double result;
        switch (bufferOp[0])
        {
            case '+':
                result = atof(buffer1) + atof(buffer2);
                break;
            case '-':
                result = atof(buffer1) - atof(buffer2);
                break;
            case '*':
                result = atof(buffer1) * atof(buffer2);
                break;
            case '/':
                result = atof(buffer1) / atof(buffer2);
                break;
            default:
                std::cout << "Invalid operation\n";
                return;
        }

        std::cout << "Result: " << result << "\n";
    }
}

int main()
{
    calculator();
    return 0;
}
"""
    elif(funct == 'chatbot'):
        return """#include <iostream>
#include <string>
#include <cstring>

const int BUFFER_SIZE = 32;

void chatbot(const std::string& input, const std::string& userName) {
    char restricted_territory[] = "Area51";
    char responseBuffer[BUFFER_SIZE];

    std::string response;

    // Process user input and generate response
    if (input == "hello") {
        response = "Hi " + userName;
        strcpy(responseBuffer, response.c_str());
    } else if (input == "how are you") {
        response = "I'm good, thank you!";
    } else if (input == "bye") {
        response = "Goodbye!";
    } else {
        response = "Sorry, I didn't understand that.";
    }

    if (strcmp(restricted_territory, "Area00") == 0)
    {
        std::cout << "Access granted\n";
        std::cout << "FLAG{buffer_overflow_exploited}\n";
        return;
    }

    // Introduce buffer overflow vulnerability
    strcpy(responseBuffer, response.c_str());

    // Output the response
    std::cout << "Bot: " << responseBuffer << std::endl;
}

int main() {

    std::cout << "Please enter your name: ";
    std::string userName;
    std::getline(std::cin, userName); 

    std::string userInput;
    std::cout << "Bot: Hello " << userName<<  "! How can I help you?" << std::endl;


    // Start the conversation
    while (true) {
        // Get user input
        std::cout << "User: ";
        std::getline(std::cin, userInput);


        // Process user input with the chatbot
        chatbot(userInput, userName);

     // Check for an exit condition
        if (userInput == "bye") {
            break;
        }
    }

    return 0;
}
"""
    elif(funct == 'password'):
        return """#include <cstdio>
#include <cstring>
#include <iostream>

const char *PASSWORD_FILE = "rictro";

int main()
{
  char input[8];
  char password[8];

  std::sscanf(PASSWORD_FILE, "%s", password);

  std::cout << "Enter password: ";
  std::cin >> input;

//   Debug prints:
   std::cout << "Address of input: " << &input << "\n";
   std::cout << "Address of password: " << &password << "\n";
   std::cout << "Input: " << input << "\n";
   std::cout << "Password: " << password << "\n";

  if (std::strncmp(password, input, 8) == 0){
    std::cout << "Access granted\n";
    std::cout << "FLAG{buffer_overflow_exploited}\n";}
  else
    std::cout << "Access denied\n";

  return 0;
}
"""

# def perform_calculation():
    url = "http://localhost:8000/calculate"

    data = {
        "num1": "5",
        "operation": "+",
        "num2": "3"
    }

    response = requests.post(url, json=data)
    result = response.json()["result"]

    print("Result:", result)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

