#!/bin/sh

# Force to supply an argument
if [ -z "$1" ]
  then
    echo "❗ No argument supplied"
fi


# Parsing -e and -u arguments
while getopts "u:e:" opt; do
  case $opt in

    # ==== Local server ===== #
    e)
      if [ $OPTARG = "dev" ]; then
      echo " 🔰 Environment: $OPTARG 🔰" >&2
      rm -rf ./db/mysql_data
      rm -rf ./db/logs
      docker system prune -a -f ;
      docker-compose stop;
      docker-compose down --remove-orphans ;
      docker-compose build ;
      docker-compose up ;
      
      elif [ $OPTARG = "prod" ]; then
      echo "📛 Environment: $OPTARG 📛" >&2
      docker-compose stop ;
      docker-compose down --remove-orphans ;
      docker-compose build;
      docker-compose up;

      else
        echo "Invalid option: -$OPTARG" >&2
      fi
      ;;
    

    # ==== HEROKU Deploy ===== #
    u)    
      if [ $OPTARG = "prod" ]; then
      echo "⏫  Pushing $OPTARG container to Heroku ⏫ " >&2
      heroku container:push web -a mycovidreporter ;
      heroku container:release web -a mycovidreporter ;
      heroku logs --tail -a mycovidreporter
      else
        echo "Invalid option: -$OPTARG" >&2
      fi
      ;;

    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done