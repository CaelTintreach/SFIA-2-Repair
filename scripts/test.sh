#! /bin/bash
cd lgen
pip3 install -r requirements.txt
python3 -m pytest pytest --cov=. term-missing
cd ..

cd ngen
pip3 install -r requirements.txt
python3 -m pytest pytest --cov=. term-missing
cd ..

cd ui1
pip3 install -r requirements.txt
python3 -m pytest pytest --cov=. term-missing
cd ..

cd pgen
pip3 install -r requirements.txt
python3 -m pytest pytest --cov=. term-missing
cd ..