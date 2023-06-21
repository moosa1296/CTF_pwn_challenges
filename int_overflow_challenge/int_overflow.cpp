#include <iostream>
#include <fstream>
#include <limits>
#include <string>


int main() {
    std::cout << std::unitbuf; // Enable automatic flushing for output

    int acc = 0;
    int n;

    std::cout << "Hello welcome to this program\n";
    while (acc >= 0) {
        std::cout << "acc = " << acc << '\n';
        std::cout << "Enter a number: ";

        if (!(std::cin >> n)) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Error reading integer\n";
        } else {
            if (n < 0) {
                std::cout << "You can't enter a negative number!\n";
            } else {
                acc += n;
            }
        }
    }

    std::cout << "You win! acc = " << acc << '\n';
   std::ifstream file("./flag.txt");
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            // Do whatever you want with each line of the file
            // For example, process the line or store it in a variable
        }
        file.close();
    } else {
        std::cout << "Could not open the flag file! Contact an admin.\n";
    }
    return 0;
}
