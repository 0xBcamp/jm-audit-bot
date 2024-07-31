ARCH=$(uname -m)

if [ "$ARCH" = "x86_64" ]
then
  ARCH="amd"
fi

mkdir /aderyn
wget https://github.com/Cyfrin/aderyn/releases/download/v0.1.7/aderyn-linux-${ARCH}64.tar.gz -P /aderyn
tar -xzf /aderyn/aderyn-linux-${ARCH}64.tar.gz -C /aderyn 
mv /aderyn/aderyn-linux-${ARCH}64 /usr/bin/aderyn

# Binary should be called aderyn-linux-$(ARCH)64
