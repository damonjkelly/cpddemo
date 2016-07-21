#include <iostream>
#include <string>
#include <fstream>

#include <cpd/nonrigid.hpp>
#include <cpd/affine.hpp>
#include <cpd/matrix.hpp>

using namespace std;

template <class T>
void save_to_file(string filename, T result)
{
    ofstream file(filename);
    file << result.points;
    file.close();
}

string result_filename(string registration_type, int iteration)
{
    return registration_type + to_string(iteration) + ".txt";
}

int
main (int argc, char** argv)
{
    cout << "Starting CPD Demo ..." << endl;

    // set data directory
    string data_dir = "/home/damon/gcubed/repos/cpdexample/data/";
    int max_iterations = 10;

    // load contour 1
    cout << "loading contour 1" << endl;
    string fname1 = data_dir + "contour1.txt";
    cpd::Matrix mat1 = cpd::matrix_from_path(fname1);

    // load contour 2
    cout << "loading contour 2" << endl;
    string fname2 = data_dir + "contour2.txt";
    cpd::Matrix mat2 = cpd::matrix_from_path(fname2);

    // perform registrations
    //auto nonrigid_result = cpd::nonrigid(mat1, mat2);
    //auto affine_result = cpd::affine(mat1, mat2);

    cpd::Affine affine;
    cpd::Nonrigid nonrigid;
    cpd::RigidResult affine_result;
    cpd::NonrigidResult nonrigid_result;

    for(int iteration = 1; iteration < max_iterations; ++iteration)
    {
        // set max iterations
        affine.set_max_iterations(iteration);
        nonrigid.set_max_iterations(iteration);

        // perform registration
        affine_result = affine.compute(mat1, mat2);
        nonrigid_result = nonrigid.compute(mat1, mat2);

        // save registration results
        {
            save_to_file(data_dir + result_filename("nonrigid", iteration), nonrigid_result);
            save_to_file(data_dir + result_filename("affine",   iteration), affine_result);
        }

    }



}
