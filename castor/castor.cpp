#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char hackme[16];
    char buff[32];

    cout << "Hello everyone, say your name: ";
    cin.getline(buff, sizeof(buff));

    if (strcmp("CyberCastors", hackme) == 0)
        // get_flag();
        cout<< "flag[1234abcd]";

    std::cout << "I caught an old tire! I sure am tired of that!" << std::endl;
    return 0;
}
