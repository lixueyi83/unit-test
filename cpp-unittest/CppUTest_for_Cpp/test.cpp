/* file: test.c */

#include <CppUTest/CommandLineTestRunner.h>
#include <CppUTest/TestHarness.h>
#include "sample.h"


/* The definition of a TEST_GROUP, the name is sample */
TEST_GROUP(sample)
{};

/* The definition of a belonging to the TEST_GROUP TEST, the name is ret_int_success */
TEST(sample, add_success)
{
    int sum = add(1, 2);
    CHECK_EQUAL(sum, 3);
}

/* The definition of a belonging to the TEST_GROUP TEST, the name is ret_int_failed */
TEST(sample, mul_failed)
{
    int multiple = mul(5, 2);
    CHECK_EQUAL(multiple, 10);
}

/* The definition of a belonging to the TEST_GROUP TEST, the name is ret_int_failed */
TEST(sample, mode_success)
{
    int mod = mode(10, 8);
    CHECK_EQUAL(mod, 2);
}

int main(int argc, char *argv[])
{
    CommandLineTestRunner::RunAllTests(argc, argv);
    return 0;
}