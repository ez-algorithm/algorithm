#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;

int main() {
    vector<string> answer, state, record;
    map<string, string> user;

    std::ifstream a("user");
    std::string s;
    string line("");

    if (a.is_open()) {
        while (!a.eof()) {
            getline(a, line);
            record.push_back(line);
        }
    } else {
        std::cout << "file::input::error" << std::endl;
    }

    for (int i=0; i<record.size(); i++) {
        //std::cout << record[i] << std::endl;
        string keyword[3];
        string token;
        stringstream ss(record[i]);
        int tkn = 0;

        while (ss >> token) {
            keyword[tkn++] = token;
        }

        if (keyword[0] == "Enter") {
            state.push_back("님이 들어왔습니다.");
            answer.push_back(keyword[1]);
            user[keyword[1]] = keyword[2];
        }
        else if (keyword[0] == "Leave") {
            state.push_back("님이 나갔습니다.");
            answer.push_back(keyword[1]);
        }
        else {
            user[keyword[1]] = keyword[2];
        }
    }

    for (int i=0; i<answer.size(); i++) {
        answer[i] = user[answer[i]] + state[i];
        std::cout << answer[i] << std::endl;
    }
    std::cout << std::endl;
    
    return 0;    
}
