#!/usr/bin/env bash

SRVPORT=4499
export PATH="/usr/games:$PATH"  # <-- add this line

prerequisites() {
    command -v cowsay >/dev/null 2>&1 &&
    command -v fortune >/dev/null 2>&1 &&
    command -v nc >/dev/null 2>&1 ||
    { echo "Install prerequisites."; exit 1; }
}

main() {
    prerequisites
    echo "Wisdom server running on port $SRVPORT..."

    while true; do
        nc -l -p $SRVPORT -q 1 | (
            while read line; do
                [[ "$line" == $'\r' ]] && break
            done

            output=$(fortune | cowsay)

            echo -e "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<pre>$output</pre>"
        )
    done
}

main

