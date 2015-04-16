#include "roommapgenerator.h"
#include <QApplication>
#include <iostream>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    RoomMapGenerator w;
    w.show();

    return a.exec();
}
