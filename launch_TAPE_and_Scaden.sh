#!/bash 

source tape_scaden_env/bin/activate

set -e 

python3 launch_TAPE_and_Scaden.py $1 $2 $3 $4

wait

