#include <bits/stdc++.h>
using namespace std;
map<string, pair<int, int>> m = {
	{"ADD", make_pair(0,0)},
	{"ADDC", make_pair(0,1)},
	{"SUB", make_pair(1,0)},
	{"SUBC", make_pair(1,1)},
	{"MOV", make_pair(2,0)},
	{"MOVC", make_pair(2,1)},
	{"AND", make_pair(3,0)},
	{"ANDC", make_pair(3,1)},
	{"OR", make_pair(4,0)},
	{"ORC", make_pair(4,1)},
	{"NOT", make_pair(5,0)},
	{"MULT", make_pair(6,0)},
	{"MULTC", make_pair(6,1)},
	{"LSFTL", make_pair(7,0)},
	{"LSFTLC", make_pair(7,1)},
	{"LSFTR", make_pair(8,0)},
	{"LSFTRC", make_pair(8,1)},
	{"ASFTR", make_pair(9,0)},
	{"ASFTRC", make_pair(9,1)},
	{"RL", make_pair(10,0)},
	{"RLC", make_pair(10,1)},
	{"RR", make_pair(11,0)},
	{"RRC", make_pair(11,1)},
};

vector<string> split(string input, char target){
	vector<string> answer;
	stringstream ss(input);
	string temp;
	
	while(getline(ss, temp, target)){
		answer.push_back(temp);
	}
	return answer;
}

string threeBitCreate(int num){
	string result ="";
	bitset<3> bs(num);
	return result = bs.to_string();
}

string fourBitCreate(int num){
	string result ="";
	bitset<4> bs(num);
	return result = bs.to_string();	
}

void MachineLanguage(string s){
	string zero = "0";
	vector<string> v = split(s, ' ');
	vector<string> result;
	auto opcode = m.find(v[0]);
	
	// 4bit
	result.push_back(fourBitCreate(opcode->second.first));

	// 1bit	
	int isC = opcode->second.second;
	result.push_back(to_string(isC));

	// 1bit	
	result.push_back(zero);
	
	// 3bit
	result.push_back(threeBitCreate(stoi(v[1])));
	
	// 3bit
	result.push_back(threeBitCreate(stoi(v[2])));
	
	if(isC == 0){
		// 3bit
		result.push_back(threeBitCreate(stoi(v[3])));
		// 1bit
		result.push_back(zero);
	}else{
		// 4bit
		result.push_back(fourBitCreate(stoi(v[3])));
	}
	
	string resultString = "";
	for(int i=0; i<result.size(); i++){
		resultString += result[i];
	}
	cout<<resultString<<endl;
}


int main(){
	int n;
	cin>>n;
	cin.ignore();
	for(int i=0; i<n; i++){
		string s;
		getline(cin, s);
		MachineLanguage(s);
	}
	
	return 0;
}
