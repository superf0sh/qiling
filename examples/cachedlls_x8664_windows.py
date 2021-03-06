#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org) 
import sys
sys.path.append("..")
from qiling import *

if __name__ == "__main__":
    ql = Qiling(
        ["rootfs/x8664_windows/bin/x8664_hello.exe"],
        "rootfs/x8664_reactos",
        libcache=True,
        output="default"
    )
    ql.run()
