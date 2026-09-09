// C++ program to demonstrate how to use 
// unordered_map::find() function
#include <bits/stdc++.h>
using namespace std;

void checkKey(unordered_map<int, string>& um, int key) {
  	 // Searching for element with key
    if (um.find(key) == um.end())
        cout << "Key " << key <<
          " Not Present\n";
    else
        cout << "Key " << key << 
          " Present\n";
}

int main() {
    unordered_map<int, string> um = {{12, "Geeks"},
                  {678, "Geeksfor"}, {88, "Gfg"}};

    // Key1 and key2 which have to search
    int key1 = 678;
    int key2 = 456;
	
  	checkKey(um, key1);
  	checkKey(um, key2);
	return 0;
}