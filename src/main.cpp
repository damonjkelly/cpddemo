
#include <iostream>
#include <string>
#include <fstream>

#include <Eigen/Geometry>
#include <cpd/nonrigid.hpp>
#include <cpd/affine.hpp>
#include <cpd/matrix.hpp>

using namespace std;

int
main (int argc, char** argv)
{
    cout << "Starting CPD Example ..." << endl;

    // set data directory
    string data_dir = "/home/damon/gcubed/repos/cpdexample/";

    // load matrix 1
    cout << "loading matrix 1" << endl;
    //string fname1 = data_dir + "fish.txt";
    string fname1 = data_dir + "contour1.txt";
    cpd::Matrix mat1 = cpd::matrix_from_path(fname1);
    cout << "mat1" << endl << mat1 << endl;

    // load matrix 2
    cout << "loading matrix 2" << endl;
    string fname2 = data_dir + "contour2.txt";
    cpd::Matrix mat2 = cpd::matrix_from_path(fname2);
    //Eigen::Rotation2D<double> rotation(M_PI / 6);
    //Eigen::RowVector2d translation(1, 2);
    //cpd::Matrix mat2((mat1 + translation.replicate(mat1.rows(),1)) * rotation.matrix());

    // perform registration
    //auto result = cpd::nonrigid(mat1, mat2);
    auto result = cpd::affine(mat1, mat2);

    // save result to text file
    ofstream result_file(data_dir + "result.txt");
    result_file << result.points;
    result_file.close();


    //cout << "mat2" << endl << mat2 << endl;
    //cout << "result" << endl << result.points << endl;


}
