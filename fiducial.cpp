#include "opencv2/highgui/highgui.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char* argv[])
{
    VideoCapture cap(0);

    if(!cap.isOpened()) {
        cout << "Cannot open the video camera" << endl;
        return -1;
    }

    namedWindow("video capture", CV_WINDOW_AUTOSIZE);

    while(1) {
        Mat frame;
        bool ret = cap.read(frame);

        if(!ret) {
            cout << "Cannot read the frame" << endl;
            break;
        }

        imshow("video capture", frame);
       
        if (waitKey(30) != -1) {
            cout << "Stopping the camera" << endl;
            break;
        }
    }

    return 0;
}

double angle_cos(Point2f p0, Point2f p1, Point2f p2) {
//    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
//    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) 
}
