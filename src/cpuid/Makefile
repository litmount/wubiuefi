export SHELL = sh
PROGRAM = pylauncher
LDFLAGS = -shared -dll
MINGW_PREFIX ?= i686-w64-mingw32
CC = $(MINGW_PREFIX)-gcc
STRIP = $(MINGW_PREFIX)-strip

all: cpuid.dll

cpuid.dll: cpuid.c
	$(CC) -o $@ $(LDFLAGS) $^
	$(STRIP) $@
