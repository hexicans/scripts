#!/usr/bin/env bash

ZPDIR="/usr/share/z-push"
TS="`date +%Y%m%d`"
TMPFILE="/tmp/zpdevices-$TS-temp.tmp"

if [ -e $TMPFILE ]
then
        echo -e "Cleaning up old temp file...\n"
        rm $TMPFILE
fi

mkfifo $TMPFILE

echo -e "Generating data...\n"

for user in `$ZPDIR/z-push-admin.php -a list|egrep -v "synchronized|id"|awk '{print $2}'|cut -d',' -f1`
do
        $ZPDIR/z-push-admin.php -a list -u $user|egrep "Device Model"|awk '{print $NF}' >> $TMPFILE &
done

cat $TMPFILE|sort|uniq -c

rm $TMPFILE
