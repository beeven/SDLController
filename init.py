import platform

system = platform.system()
machine = platform.machine()

if system == "Windows":
    platform.os.environ["PYSDL2_DLL_PATH"] = "./lib_win"
elif system == "Darwin":
    platform.os.environ["PYSDL2_DLL_PATH"] = "./lib_darwin"
elif system == "Linux":
    if machine == "armv6l":
        import ctypes
        ctypes.CDLL("/opt/vc/lib/libbcm_host.so",mode=ctypes.RTLD_GLOBAL)
        platform.os.environ["PYSDL2_DLL_PATH"] = "./lib_rpi"
