#!/bin/bash

PASSWORD_FILE="passwords.txt"
MYSQL_USER="root"
MYSQL_HOST="localhost"

echo "开始尝试密码列表中的密码..."

while read -r password; do
    echo -n "尝试密码: $password ... "

    # 使用 -pPASSWORD 的形式避免交互
    mysql -u"$MYSQL_USER" -p"$password" -h "$MYSQL_HOST" -e "SELECT 1;" &>/dev/null

    if [ $? -eq 0 ]; then
        echo "✅ 成功！密码是：$password"
        exit 0
    else
        echo "失败"
    fi
done < "$PASSWORD_FILE"

echo "❌ 所有密码都尝试完了，未找到正确密码。"