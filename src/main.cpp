#include <iostream>
#include <string>

#include <cpd/nonrigid.hpp>
#include <cpd/matrix.hpp>

using namespace std;

int
main (int argc, char** argv)
{
    cout << "Starting CPD Example ..." << endl;

    // load matrix 1
    string fname1 = "/home/damon/gcubed/repos/cpdexample/fish.txt";
    cpd::Matrix mat1 = cpd::matrix_from_path(fname1);

    cout << mat1 << endl;


}
