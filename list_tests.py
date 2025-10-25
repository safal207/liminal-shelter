import unittest
import os
import sys

# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath('.'))

try:
    # Try to import the test module
    from tests.test_core import TestSeedlingModel, TestGuardianCore, TestLiminalShelter, TestIntegration
    
    # Create a test suite
    loader = unittest.TestLoader()
    
    # Add test cases to the suite
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestSeedlingModel))
    suite.addTests(loader.loadTestsFromTestCase(TestGuardianCore))
    suite.addTests(loader.loadTestsFromTestCase(TestLiminalShelter))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Print the number of tests found
    print(f"Found {suite.countTestCases()} test cases")
    
    # List all test cases
    for test in suite:
        print(f"Test: {test}")
    
    # Run the tests
    print("\nRunning tests...")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    print(f"\nTests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
