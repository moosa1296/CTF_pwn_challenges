#include <iostream>
#include <cstdlib>
#include <string>
#include <sstream>

std::string sanitize(const std::string& input) {
    // Sanitization function to prevent command injection
    std::stringstream sanitized;
    for (char ch : input) {
        if (ch == '|' || ch == ';' || ch == '`' || ch == '$' || ch == '(' || ch == ')' || ch == '\\' || ch == '<' || ch == '>') {
            sanitized << '_'; // Replace dangerous characters with underscores
        } else {
            sanitized << ch;
        }
    }
    return sanitized.str();
}

int main() {
    std::string command;

    std::cout << "Enter a command: ";
    std::getline(std::cin, command);

    // Command injection vulnerability
    std::string sanitizedCommand = sanitize(command);
    std::string fullCommand = "ls -l " + sanitizedCommand;

    std::cout << "Executing command: " << fullCommand << "\n";
    std::system(fullCommand.c_str());

    return 0;
}
