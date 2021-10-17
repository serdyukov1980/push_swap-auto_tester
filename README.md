# push_swap-auto_tester
automatic tester of push_swap project with randomly generated data-sets

create virtual environment:

python -m venv venv

activate new environment:

source venv/bin/activate

install additional python packages:

pip install numpy scipy matplotlib pyqt5

now run script with your push_swap executable:

./test_average.sh 5 100

first command line parameter is the quantity of numbers to sort, second parameter is
number of random data-sets

script stores generated numbers into file "nums", number of operations in the
file "test", and "OK" or "KO" for successful/unsuccessful sorting. those can be 
useful for debugging.

third optional parameter adds suffix to the "nums" and "test" file names, e.g.

./test_average.sh 5 100 1 

will produce "nums1" and "test1" files.
this can be useful for running multiple instances of script parallel in multiple
shell instances.
  
The shell script uses linux tester executable name, which should be changed if necessary.
