
#!/bin/sh

DIRNAME=`dirname $0`

# Setup the JVM
if [ "x$JAVA_HOME" != "x" ]; then
    JAVA="$JAVA_HOME/bin/java"
else
    JAVA="java"
fi

if [ ! -f "$DIRNAME/kSar.jar" ] ; then
    echo "Unable to find kSar.jar"
    exit 1;
fi

exec $JAVA $JAVA_OPT -jar $DIRNAME/kSar.jar $@
#!/bin/sh

# Run the JMeter shutdown client

DIRNAME=`dirname $0`

java -cp ${DIRNAME}/ApacheJMeter.jar org.apache.jmeter.util.ShutdownClient Shutdown "$@"

#!/bin/sh


cd `dirname $0`

CP=../lib/ext/ApacheJMeter_http.jar;../lib/ext/ApacheJMeter_core.jar;../lib/jorphan.jar;../lib/logkit-1.2.jar
CP=${CP};;../lib/avalon-framework-4.1.4.jar;../lib/jakarta-oro-2.0.8.jar
java -cp $CP org.apache.jmeter.protocol.http.control.HttpMirrorServer $1
#! /bin/sh
java $JVM_ARGS -Dapple.laf.useScreenMenuBar=true -jar `dirname $0`/ApacheJMeter.jar "$@"
#!/bin/sh
DIRNAME=`dirname $0`

java -cp ${DIRNAME}/ApacheJMeter.jar org.apache.jmeter.util.ShutdownClient StopTestNow "$@"
#! /bin/sh
ID="@(#)multi.sh:3.4 -- 5/15/18 19:30:24";
instance=1
while [ $instance -le $1 ]; do
	/bin/sh "$UB_BINDIR/tst.sh" &
	instance=`expr $instance + 1`
done
wait

#!/bin/bash
VER=$(git tag -l v[0-9].[0-9]*.[0-9]* | tail -n 1)
echo "# ($(date +%Y-%m-%d))"
echo
git log $VER...HEAD --no-merges --topo-order --format=' * %s (%an)'
echo
echo "# $VER"
#!/bin/sh
DIR=$( cd $(dirname $0) ; pwd -P )

if [ -z "$JAVA_HOME" ] ; then
        JAVA_HOME=`readlink -f \`which java 2>/dev/null\` 2>/dev/null | \
        sed 's/\/bin\/java//'`
fi

TOOLSJAR="$JAVA_HOME/lib/tools.jar"

if [ ! -f "$TOOLSJAR" ] ; then
        echo "$JAVA_HOME seems to be no JDK!" >&2
        exit 1
fi

"$JAVA_HOME"/bin/java $JAVA_OPTS -cp "$DIR/jvmtop.jar:$TOOLSJAR" \
com.jvmtop.JvmTop "$@"
exit $?
#!/bin/sh

QT_SELECT=qt5 qmake qjournalctl.pro -r -spec linux-g++ CONFIG+=release

if [ -d ".git" ]; then
    sed -i -e 's/[[:xdigit:]]\{7\}/'$(git log --pretty=format:'%h' -n 1)'/' src/version.h
else
    sed -i -e 's/[[:xdigit:]]\{7\}/0000000/' src/version.h
fi


date
echo "$0 Started "

DATE=`date +%m%d%y`
tar -cvf /tmp/cdenzesham.tar /cygdrive/c/x/Netwoker_Documentation /cygdrive/c/x/BlackUSB/QA /cygdrive/c/cygwin/home/zesham /cygdrive/c/x/NMDA /cygdrive/c/x/*.doc* /cygdrive/c/x/*.xls* /cygdrive/c/x/*.pdf
mv /tmp/cdenzesham.tar /tmp/cdenzesham.$DATE.tar
openssl aes-256-cbc -salt -k 4545hammed678 -in /tmp/cdenzesham.$DATE.tar -out /tmp/cdenzesham.$DATE
mv /tmp/cdenzesham.$DATE /cygdrive/b
date
echo "$0 Done"
openssl aes-256-cbc -d -salt -in cdenzesham.033111 -out cdenzesham.033111.tar
enter aes-256-cbc decryption password:
namdosefer

#!/bin/sh
while true
do
echo "--------------------------------" 
date 
ps -efW |egrep -i "$1" 
sleep 2
done

#!/bin/bash
echo " find /cygdrive/b/cdenz* -type f -mtime +4 -exec rm {} \; "
find /cygdrive/b/cdenz* -type f -mtime +4 -exec rm {} \;
echo "find /tmp/cdenz* -type f -mtime +4 -exec rm {} \;"
find /tmp/cdenz* -type f -mtime +4 -exec rm {} \;
END=5
for ((i=1;i<=END;i++)); do
    echo $i
done
#!/bin/env bash

END=45
for ((i=1;i<=END;i++)); do
    echo $i
done
for ((i=1;i<=END;i++)); do
    echo $i
done
