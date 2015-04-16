/*
 *
 * Thursday, 9th April 2015
 * Don K Dennis (metastableB)
 * As part of HRAM
 *
 *	This program takes a file containing room numbers
 *  and another containing the generated map areas,
 * 	then assosiates the area id tags with the room numbers
 *  and creates a new file.
 */

#include <iostream>
#include <fstream>
#include <string>

using namespace std;
void makeRoomNo(fstream &readMap,fstream &readRoomList, fstream &printMap);

int main(int argc, char* argv[]) {
	if(argc <3) 
		cout << "ERROR: Too few arguements\n
				Usage ./roomNoCreator {mapfile.map} {roomNumberListr.txt}\n";
	if(argc > 3)
		cout << "ERROR: Too many arguements\n
				Usage ./roomNoCreator {mapfile.map} {roomNumberListr.txt}\n"
	if(argc != 3)
		return 1;

	fstream readMap,readRoomList,printMap;
	readMap.open(argc[1],ios::in);
	readRoomList.open(arg[2],ios::in);
	writeMap.open("roomNumber.txt",ios::out);

	if(!readMap.is_open() || !writemap.is_open() || !readRoomList.is_open()) {
		cout << "ERROR: FileOpenFailed, verify your imput files exist and you have write permissions on the disk\n";
		return 0;
	}
	makeRoomNo(readMap,readRoomList,printMap);
	readMap.close();
	printMap.close();
	return 0;
}

void makeRoomNo(fstream &readMap,fstream &readRoomList, fstream &printMap) {
	string readAreaLine,readRoomListLine;
	size_t pos;
	while ( getline(readMap,readAreaLine) ) {
		if( (readAreaLine.find(size_t pos = "shape")) != string::npos ) {
			if (!getline(readRoomList,readRoomListLine)) {
				cout << "ERROR: unexpected end of RoomListFile");
				exit(1);
			}
			readRoomListLine.inert(0,"id=\"");
			readRoomListLine.append("\" ");
			readAreaLine.insert (size_t pos, readRoomListLine);		
			printMap << readAreaLine <<"\n";
		}
		else 
			printMap << readAreaLine<<"\n";
    }
}