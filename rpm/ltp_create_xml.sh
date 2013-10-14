#!/bin/sh

echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
echo "<testdefinition version=\"1.0\">"
echo "  <suite name=\"ltp-tests\" domain=\"Kernel\">"
echo "    <set name=\"Linux Kernel LTP\" description=\"LTP Validates the reliability, robustness, and stability of Linux\" feature=\"Linux Kernel\">"
echo "      <pre_steps timeout=\"3600\">"
echo "        <!-- Run all ltplite test cases, timeout set to one hour -->"
echo "        <step>/usr/sbin/run-blts-root rm -rf /opt/ltp/results/ltplite_results.log</step>"
echo "        <step>/usr/sbin/run-blts-root /opt/ltp/runltplite.sh -p -l ltplite_results.log</step>"
echo "      </pre_steps>"

for  var1 in ` awk '/^[a-z]/ {print $1}' <  $1 `
do
    echo "      <case name=\"$var1\">"
    echo "        <step>grep $var1 /opt/ltp/results/ltplite_results.log |grep PASS</step>"
    echo "      </case>"
done

echo "      <get>"
echo "        <file>/opt/ltp/results/ltplite_results.log</file>"
echo "      </get>"
echo "    </set>"
echo "  </suite>"
echo "</testdefinition>"
