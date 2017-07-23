/* file: test.c */

#include <CppUTest/CommandLineTestRunner.h>
#include <CppUTest/TestHarness.h>

/* To test .c files*/
extern "C"
{
#include "sample.h"
}

/* The definition of a TEST_GROUP, the name is sample */
TEST_GROUP(sample)
{};

/* The definition of a belonging to the TEST_GROUP TEST, the name is ret_int_success */
TEST(sample, ret_int_success)
{
    int sum = ret_int(1, 2);
    CHECK_EQUAL(sum, 3);
}

/* The definition of a belonging to the TEST_GROUP TEST, the name is ret_int_failed */
TEST(sample, ret_int_failed)
{
    int sum = ret_int(1, 2);
    CHECK_EQUAL(sum, 4);
}

int main(int argc, char *argv[])
{
    CommandLineTestRunner::RunAllTests(argc, argv);
    return 0;
}