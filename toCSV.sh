input="$1"
output="$2"
tr -s '\t' < $input | tr '\t' ',' > $output
