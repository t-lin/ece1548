#!/bin/bash -f
source /home/savitb/bin/functions
USER=$(whoami)
SLICE="$USER"-slice
PRIVATE_NETWORK="$USER"-net
green_desc_title "  Assigning a ($PRIVATE_NETWORK) to ($SLICE) for ($USER)"
command_desc "quantum net-list"
NET_ID_PRIVATE=`quantum net-list -c id -c name | grep $PRIVATE_NETWORK | awk '{print $2}'`
echo "NET_ID_PRIVATE=$NET_ID_PRIVATE"
command_desc "janus fv-assignnetwork -slicename $SLICE --network_id $NET_ID_PRIVATE"
janus fv-assignnetwork --slicename $SLICE --network_id $NET_ID_PRIVATE
