# Simple Python3 practice scripts

* Python 3 Testing: [An intro to
  unittest](https://www.blog.pythonlibrary.org/2016/07/07/python-3-testing-an-intro-to-unittest/)
  The unittest module is actually a testing framework that was originally inspired by JUnit. It currently supports test automation, the sharing of setup and shutdown code, aggregating tests into collections and the independence of tests from the reporting framework.

  The unittest frameworks supports the following concepts:

      Test Fixture – A fixture is what is used to setup a test so it can be run and also tears down when the test is finished. For example, you might need to create a temporary database before the test can be run and destroy it once the test finishes.
      Test Case – The test case is your actual test. It will typically check (or assert) that a specific response comes from a specific set of inputs. The unittest frameworks provides a base class called **TestCase** that you can use to create new test cases.
      Test Suite – The test suite is a collection of test cases, test suites or both.
      Test Runner – A runner is what controls or orchestrates the running of the tests or suites. It will also provide the outcome to the user (i.e. did they pass or fail). A runner can use a graphical user interface or be a simple text interface.


## Set up
* Install and set-up [Git Version
  control](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
* Inatall and set-up [Python3](https://www.python.org/downloads/)
* Install and set-up [Pipenv &amp; virtual
  environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

* Clone the repo `$ git clone https://github.com/artorious/playground.git`
* Navigate to `playground` dir
* Install dependancies `pipenv shell`

Run `$ coverage run -m pytest -v; coverage report`
or `$  python -m unittest -v`
or ` pytest -v`

