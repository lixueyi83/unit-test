# makefile for sample cpputest

CPPUTEST_HOME = /usr/include/CppUTest

CC      := gcc
CFLAGS  := -g -Wall
CFLAGS  += -std=c99
CFLAGS  += -D CPPUTEST      #Compile the test file, ignore the main function of sample.c, the sample.c code with the CPPUTEST macro

# CPPUTest is C++Write, so using g++ To compile the test file
CPP     	:= g++
CPPFLAGS	:= -g -Wall
CPPFLAGS	+= -I$(CPPUTEST_HOME)/include

LDFLAGS := -L$(CPPUTEST_HOME)/lib -lCppUTest


sample: sample.o

sample.o: sample.h sample.c
	$(CC) -c -o sample.o sample.c $(CFLAGS)

# Additional compiled test program
test: test.o sample.o
	$(CPP) -o $@ test.o sample.o $(LDFLAGS)

test.o: sample.h test.c
	$(CPP) -c -o test.o test.c $(CPPFLAGS)


.PHONY: clean
clean:
	@echo "clean..."
	rm -f test sample
	rm -f sample.o test.o
