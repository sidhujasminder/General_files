function test(){
    echo "JAMMYY"
#    newman run API_SERVER_EXTENSIVE_TESTING.postman_collection.json
}

function test1(){
    echo "JAMMYYiKIZZZYY"
#    newman run API_SERVER_EXTENSIVE_TESTING.postman_collection.json
}

function kill(){

#   kill $PID
    ps -ef | grep api_server | grep -v grep | awk '{print $2}' | xargs kill
}

if [ -z "$1" ]
then
  test
else
if declare -f "$1" > /dev/null
then
  "$@"
else
  echo "WRONG FUNCTION NAME"
  exit 1
fi
fi

#setup
#sleep 10 &&
#kill
