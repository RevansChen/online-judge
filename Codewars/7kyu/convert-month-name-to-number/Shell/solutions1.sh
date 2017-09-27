# Shell - bash

# 將輸入轉成小寫英文
month="${1,,}"

# 取前面三個字做判斷
case ${month:0:3} in
    "jan") echo "01" ;;
    "feb") echo "02" ;;
    "mar") echo "03" ;;
    "apr") echo "04" ;;
    "may") echo "05" ;;
    "jun") echo "06" ;;
    "jul") echo "07" ;;
    "aug") echo "08" ;;
    "sep") echo "09" ;;
    "oct") echo "10" ;;
    "nov") echo "11" ;;
    "dec") echo "12" ;;
esac