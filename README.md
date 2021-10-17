# push_swap-auto_tester
automatic tester of push_swap project with randomly generated data-sets

create virtual environment:

python -m venv <path-to-venv, e.g. 'venv'>

activate new environment:

source <path to environment>/bin/activate (e.g. venv/bin/activate)

install additional python packages:

pip install numpy scipy matplotlib pyqt5

now run script with your push_swap executable:

./test_average 5 100

first numeric parameter is the quantity of numbers to sort, second parameter is
number of random data-sets

script stores generated numbers into file "nums" and number of operations in the
file "test". those can be useful for debugging.

third optional parameter adds suffix to the "nums" and "test" file names, e.g.

./test_average 5 100 1 

will produce "nums1" and "test1" files.
this can be useful for running multiple instances of script parallel in multiple
shell instances.
  
The shell script uses linux executable name, which should be changed if necessary.
