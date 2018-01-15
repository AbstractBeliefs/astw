#!/bin/sh

# create build tree
mkdir -p aseba/build-dashel aseba/build-enki aseba/build-aseba
cd aseba
# fetch and compile dashel
git clone https://github.com/aseba-community/dashel.git
cd build-dashel
cmake ../dashel -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_SHARED_LIBS=OFF
make
cd ..
# fetch and compile enki
git clone https://github.com/enki-community/enki.git
cd build-enki
cmake ../enki -DCMAKE_BUILD_TYPE=RelWithDebInfo
make
cd ..
# fetch and compile aseba, telling it where to find dashel and enki
git clone --recursive https://github.com/aseba-community/aseba.git
cd aseba && git checkout release-1.5.x && cd ..
cd build-aseba
cmake ../aseba -DCMAKE_BUILD_TYPE=RelWithDebInfo -Ddashel_DIR=../build-dashel -Denki_DIR=../build-enki
make
