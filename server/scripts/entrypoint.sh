#!/bin/sh

wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh ;

  bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 && rm -rf ~/miniconda3/miniconda.sh ;
  /root/miniconda3/bin/conda create -n wt_assessment python=3.10.4 -y ;
  /root/miniconda3/bin/conda init bash ;
  echo "conda activate wt_assessment" > ~/.bashrc ;
  pip install -r requirements/requirements.txt ;
  /root/miniconda3/bin/conda install pyodbc==4.0.32 ;



exec python manage.py runserver 0.0.0.0:${APP_PORT}