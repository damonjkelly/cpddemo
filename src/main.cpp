#include <iostream>
#include <string>
#include <fstream>

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

    // load contour 1
    cout << "loading contour 1" << endl;
    string fname1 = data_dir + "contour1.txt";
    cpd::Matrix mat1 = cpd::matrix_from_path(fname1);

    // load contour 2
    cout << "loading contour 2" << endl;
    string fname2 = data_dir + "contour2.txt";
    cpd::Matrix mat2 = cpd::matrix_from_path(fname2);

    // perform registration
    //auto result = cpd::nonrigid(mat1, mat2);
    auto result = cpd::affine(mat1, mat2);

    // save result to text file
    ofstream result_file(data_dir + "result.txt");
    result_file << result.points;
    result_file.close();
}
