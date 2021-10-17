#!/bin/bash
ARG=$(python generate_numbers.py $1)
echo $ARG > nums$3
../push_swap $ARG | tee >(../checker_linux $ARG > ok_ko$3)| wc -l > test$3
for i in $(eval echo {1..$2})
do
  ARG=$(python generate_numbers.py $1)
  echo $ARG >> nums
  ../push_swap $ARG | tee >(../checker_linux $ARG >> ok_ko$3) | wc -l >> test$3
done
python average.py