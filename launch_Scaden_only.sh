#!/bash 

source tape_scaden_env/bin/activate

set -e 

python3 launch_Scaden_only.py $1 $2 $3 $4

wait

