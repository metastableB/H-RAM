#ifndef ROOMMAPGENERATOR_H
#define ROOMMAPGENERATOR_H

#include <QMainWindow>
#include <QFileDialog>
#include <QFile>
#include <QTextStream>
#include <QDebug>

namespace Ui {
class RoomMapGenerator;
}

class RoomMapGenerator : public QMainWindow {
    Q_OBJECT
public:
    QString imageMapFile;
    QString roomListFile;
    QString destinationFile;

public:
    explicit RoomMapGenerator(QWidget *parent = 0);
    void updateImageMapFileText(QString imageMapFile);
    void updateRoomListFileText(QString roomListFile);
    ~RoomMapGenerator();

private:
    Ui::RoomMapGenerator *ui;
private slots :
    bool selectRoomListFile();
    bool selectImageMapFile();
    bool selectDestinationFile();
    void enablePushButtonGenerate();
    void createImageMapFile();

};

#endif // ROOMMAPGENERATOR_H
