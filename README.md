# CCPS109 - Computer Science I
* The language used in the projects is python.
* This Course was taken in summer 2021 at chang school by ilkka kokkarinen.

# 109 Python Problems for CCPS 109

This repository contains the problem specifications, the automated tester and the necessary data files for the graded lab problems for the course *CCPS 109 Computer Science I*, as taught by [Ilkka Kokkarinen](http://www.scs.ryerson.ca/~ikokkari/) for the Chang School of Continuing Education, Ryerson University, Toronto, Canada.

Write all your functions one by one into the same file `labs109.py` so that the acceptance tester script `tester109.py` can find them. This tester will execute the automated acceptance tests for the functions implemented in `labs109.py`. The acceptance tester gives each implemented function a large number of pseudorandomly generated test cases, and computes a checksum from the answers returned by your function. This checksum is compared to the checksum computed from the instructor's private model solution and hardcoded from there into the tester. The function passes the acceptance test if and only if these two checksums are identical, and the time taken by the test is under 20 seconds. The test case generators have been designe to complete in at most a second or two on a modern desktop computer, provided that the student solution is reasonable to begin with, and does not try to achieve with two nested loops something that could be achieved with just one loop.

This setup allows students to work at home at their convenience. They know whether the functions written so far are correct simply by running the acceptance test script. This automation eliminates basically the additional labour needed from the the human instructor or the TA's to run the basic bureaucracy and grading of the lab assignments, so they can rather concentrate on helping students debug their solutions that fail the acceptance tests. Once students have given each problem a good old "college try" (including once sleeping over it to have another look at the problem with fresh eyes the following day) but still haven't been able to untangle that particular knot, they can contact the course personnel for help to get them loose again. 

In addition to the precomputed checksums that serve as definitive acceptance tests for each function, the file `expected_answers` contains the expected results for the first 400 test cases for each problem. The acceptance tester will compare these in lockstep to the results produced by the student solution. At the first discrepancy, the test for that function is immediately terminated, and the test case arguments, the expected correct result and the returned incorrect result are displayed as a valuable debugging aid. Having a reasonably short but explicit test case available is an invaluable aid in debugging a function that does not pass the automated test.

Everyone teaching or learning Python is welcome to use, adapt and distribute these problems and the associated acceptance tester for their own purposes as they see fit. The author welcomes feedback by email at `ilkka.kokkarinen@gmail.com` from computer science instructors who use these problems in their courses.

The lab specification document and the automated tester software `tester109.py` are released under the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.txt), with no warranties implied by the author.

Wordlist `words_sorted.txt` adapted from [dwyl/english-words](https://github.com/dwyl/english-words).
