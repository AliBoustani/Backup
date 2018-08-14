Pyntc is an open source multi-vendor Python library that establishes a common framework for working with different network APIs & device types.
more info:   https://github.com/networktocode/pyntc

Pyntc currently supports four device types:

cisco_ios_ssh
cisco_nxos_nxapi
arista_eos_eapi
juniper_junos_netconf




Before starting to use Pyntc you need to install some prerequisites:
This below procedure has completely tested on Debian/Ubuntu distributions.

"sudo pip install pyntc" or "sudo pip install pyntc --upgrade"

Complete installation guide is:
# apt-get update
# apt-get install python -y
# apt-get install build-essential libssl-dev libffi-dev -y
# pip install cryptography
# pip install netmiko
# pip install pyntc