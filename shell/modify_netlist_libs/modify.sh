#!/bin/bash
unalias -a

orig_f="A_TOTAL_LVS_NCSIM_test.net"
output_f="A_TOTAL_LVS_NCSIM_REP.txt"

log_f="A_TOTAL_LVS_NCSIM.log"

#----

var=$(cat A_TOTAL_LVS_NCSIM.log | grep "ERROR" | awk -F: '{print $NF}' | tr -d ")")

content=$(cat -n $orig_f)

for i in $var; do
      # sed -i -E "$i s/^X/M/" A_TOTAL_LVS_NCSIM_test.net
      content=$(echo "$content" | sed -E "/^\s*$i\s+/ s/M/X/")
      # if [ i -eq $var ]
      # then
      echo "----"
      # fi
done

# echo "$content" >output
# while true; do
#       sed -i 's/X/M/g' A_TOTAL_LVS_NCSIM.net
# done