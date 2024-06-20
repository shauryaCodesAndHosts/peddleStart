#! /bin/sh
echo "start virtualenv"
if [ -d "env" ];
then
    echo "enabling virtual env"
else
    echo "run setup.sh first"
    exit 0
fi

. env/bin/activate
export ENV=development
echo "hello"
python main.py
deactivate