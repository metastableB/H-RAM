#include "roommapgenerator.h"
#include "ui_roommapgenerator.h"

RoomMapGenerator::RoomMapGenerator(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::RoomMapGenerator) {
    ui->setupUi(this);
}

RoomMapGenerator::~RoomMapGenerator(){
    delete ui;
}

bool RoomMapGenerator::selectImageMapFile() {
    imageMapFile = QFileDialog::getOpenFileName(this,
            tr("Open Image Map File"), "./", tr("MapFiles (*.map);;HTML Files (*.html)"));
    this->ui->lineEditImageMap->setText(imageMapFile);
    return true;
}

bool RoomMapGenerator::selectRoomListFile() {
    roomListFile = QFileDialog::getOpenFileName(this,
            tr("Open Room List File"), "./", tr("Text Files (*.txt);;md Files (*..md)"));
    this->ui->lineEditRoomList->setText(roomListFile);
    return true;
}
bool RoomMapGenerator::selectDestinationFile() {
    destinationFile = QFileDialog::getOpenFileName(this,
            tr("Open Destination"), "./", tr("HTML files (*.html)"));
    this->ui->lineEditDestination->setText(destinationFile);
    return true;
}

void RoomMapGenerator::enablePushButtonGenerate(){
    QString tempImageFile,tempRoomFile,tempDestinationFile;
    tempImageFile = this->ui->lineEditImageMap->text();
    tempRoomFile = this->ui->lineEditRoomList->text();
    tempDestinationFile = this->ui->lineEditDestination->text();
    if(tempImageFile.isEmpty() || tempRoomFile.isEmpty() || tempDestinationFile.isEmpty())
        this->ui->pushButtonGenerate->setEnabled(false);
    else
        this->ui->pushButtonGenerate->setEnabled(true);
}

void RoomMapGenerator::createImageMapFile(){

   QFile openFileRoomList(roomListFile);
   QFile openFileImageMap(imageMapFile);
   QFile openFileGenerate(destinationFile);
   QString readMap;
   QString readRoom;
   QString id;
   int posId;
   int posNoHref;
   int noOfLines = 0;

   if( !openFileImageMap.open((QIODevice::ReadOnly | QIODevice::Text)) ||
           !openFileRoomList.open(QIODevice::ReadOnly | QIODevice::Text)) {
       // ERROR HANDLER : COULD NOT READ FILES
   }
   if( !openFileGenerate.open(QIODevice::WriteOnly | QIODevice::Text) ) {
       // ERROR HANDLER : no write permissions ?
   }
   QTextStream outStream(&openFileGenerate);

   while (!(openFileImageMap.atEnd())){
       readMap = openFileImageMap.readLine();
       noOfLines++;
   }
   this->ui->progressBar->reset();
   this->ui->progressBar->setMinimum(0);
   this->ui->progressBar->setMaximum(noOfLines);

   noOfLines = 0;
   openFileImageMap.seek(0);
   while (!(openFileImageMap.atEnd())) {
           readMap = openFileImageMap.readLine();
           readMap.remove("\n");
           if((posId = readMap.indexOf("shape")) != -1) {
               if( !(readRoom = openFileRoomList.readLine()).isEmpty() ||
                       !(readRoom = openFileRoomList.readLine()).isNull()) {
                      //ERROR HANDLER : unexpected end of file
               }
               readRoom.remove("\n");
               id = readRoom;
               readRoom.insert(0,QString("id=\""));
               readRoom.insert(readRoom.size(),"\" onclick=\"toggle('");
               readRoom.insert(readRoom.size(),id);
               readRoom.insert(readRoom.size(),"')\" ");
               readMap.insert(posId,readRoom);

               if((posNoHref = readMap.indexOf("nohref=\"nohref\"")) != -1){
                   readMap.replace("nohref=\"nohref\"","href=\"#\"");
               }
               else if((posNoHref = readMap.indexOf("nohref")) != -1){
                   readMap.replace("nohref","href=\"#\"");
               }
               outStream << readMap<<"\n";
           }

           else outStream << readMap<<"\n";
           noOfLines++;
           this->ui->progressBar->setValue(noOfLines);
   }
   openFileGenerate.close();
   openFileImageMap.close();
   openFileRoomList.close();
}
