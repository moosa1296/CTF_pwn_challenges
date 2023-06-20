#include <iostream>
#include <cstring>
#include <cstdlib>

void print_flag() {
  // Function to print the flag
  std::cout << "Congratulations! Here is the flag: FLAG{example_flag}" << std::endl;
}

void init_visualize(char* buff, int bufferSize) {
  // Function to initialize stack visualization
  std::cout << "==== Stack Visualization ====" << std::endl;
  std::cout << "Buffer Address: " << static_cast<void*>(buff) << std::endl;
  std::cout << "Buffer Size: " << bufferSize << " bytes" << std::endl;
  std::cout << "----------------------------" << std::endl;
}

void visualize(char* buff, int bufferSize) {
  // Function to visualize the stack
  std::cout << "Buffer Contents: ";
  for (int i = 0; i < bufferSize; ++i) {
    std::cout << buff[i];
  }
  std::cout << std::endl;
  std::cout << "----------------------------" << std::endl;
}

void vuln() {
  const int bufferSize = 32;
  const int paddingSize = 16;
  char padding[paddingSize];
  char buff[bufferSize];
  int notsecret = 0xffffff00;
  int secret = 0xdeadbeef;

  std::memset(buff, 0, sizeof(buff)); // Zero-out the buffer.
  std::memset(padding, 0xFF, sizeof(padding)); // Zero-out the padding.

  init_visualize(buff, bufferSize); // Initializes the stack visualization

  visualize(buff, bufferSize); // Prints out the stack before modification
  std::cout << "Input some text: ";
  std::cin.getline(buff, sizeof(buff)); // This is a vulnerable call!
  
  visualize(buff, bufferSize); // Prints out the stack after modification

  // Check if secret has changed.
  if (secret == 0x67616c66) {
    std::cout << "You did it! Congratulations!" << std::endl;
    print_flag(); // Print out the flag. You deserve it.
    return;
  } else if (notsecret != 0xffffff00) {
    std::cout << "Uhmm... maybe you overflowed too much. Try deleting a few characters." << std::endl;
  } else if (secret != 0xdeadbeef) {
    std::cout << "Wow you overflowed the secret value! Now try controlling the value of it!" << std::endl;
  } else {
    std::cout << "Maybe you haven't overflowed enough characters? Try again?" << std::endl;
  }

  std::exit(0);
}

int main() {
  std::setbuf(stdout, NULL);
  std::setbuf(stdin, NULL);
  vuln();
}
