#!/usr/bin/env bash
set -o errexit

# Update and install dependencies
apt-get update && apt-get install -y wget unzip

# Download Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Install Chrome
dpkg -i google-chrome-stable_current_amd64.deb || apt-get -fy install
