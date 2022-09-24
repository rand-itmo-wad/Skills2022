
# Skills 2022 test

## Task1:
### Task name: 
Manage GitHub scripts and documents
### Task preparation: 
create `Skills2022` directory inside the home directory using `mkdir` 
### Task implementation 
 1. Create `Skills2022` directory![enter image description here](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/1.png)
 2. Initialize the local repository, Create `README.md` file and add it to the repo. ![enter image description here](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/2.png)
 3. Create remote repo and add remote origin ![enter image description here](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/3.png)
 4. Had the error  `Password support removed` and solve it using the following commands after create personal access token (explained in details in task troubleshooting).
 5. push the commits to the remote repo using `push` command ![enter image description here](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/4.png)
### Task troubleshooting 
We can create access token from your GitHub account, go to **Settings** => **Developer Settings** => **Personal Access Token** => **Generate New Token** (Give your password) => **Fillup the form** => click **Generate token** => **Copy the generated Token**![enter image description here](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/problem-solve-1.png)
then use the following commands as in the step5 screenshot 
```
$ git config --global user.name "your_github_username"
$ git config --global user.email "your_github_email"
$ git config -l
```
### Task verification 
![](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task1/screenshots/4.png)

## Task5:
### Task name: 
Unit testing
### Task preparation: 
create `task5` directory inside the `Skills2022` directory using `mkdir` 
### Task implementation 
 1. Create `task.py` file contains the functions which we need to test:
  ```python
def factors(n):
    p = 2
    f = list()
    while n >= p*p :
        if n % p == 0:
            f.append(p)
            n = int(n / p)
        else:
           p = p + 1
    f.append(n)
    return f

def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
        else:
            return True

def vowels(text):
    v = list()
    for i in text:
        if i in 'aeiouAEIOU':
            v.append(i)
    return v
```
 2. import `unittest` 
```python
import  unittest
```
 3. Add test class which inherits unittest.TestCase
 4. Convert the test functions into methods by adding `self` as the first argument
```python
class TestTask5(unittest.TestCase):
    def test_factors(self):
        self.assertCountEqual(factors(1), [1], "Should be [1]")
        self.assertCountEqual(factors(4), [2, 2], "Should be [2,2]")
        self.assertCountEqual(factors(5), [5], "Should be [5]")
        self.assertCountEqual(factors(6), [2,3], "Should be [2,3]")

    def test_is_prime(self):
        self.assertEqual(is_prime(-1), False, "Should be False")
        self.assertEqual(is_prime(1), False, "Should be False")
        self.assertEqual(is_prime(4), False, "Should be False")
        self.assertEqual(is_prime(5), True, "Should be True")
        self.assertEqual(is_prime(6), False, "Should be False")

    def test_vowels(self):
        self.assertCountEqual(vowels("ok"), ["o"], 'Should be ["o"]')
        self.assertCountEqual(vowels("test"), ["e"], 'Should be ["e"]')
        self.assertCountEqual(vowels("aeiouAEIOU"), ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"], 'Should be ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]')
        self.assertCountEqual(vowels(""), [], "Should be []")

    def test_len(self):
        self.assertEqual(len(""), 0, "Should be 0")
        self.assertEqual(len("test"), 4, "Should be 4")
        self.assertEqual(len("test "), 5, "Should be 5")
        self.assertEqual(len([1, 2]), 2, "Should be 2")

if __name__ == '__main__':
    unittest.main()
```
### Task troubleshooting 
N/A
### Task verification 
![](https://raw.githubusercontent.com/rand-itmo-wad/Skills2022/main/task5/screenshots/1.png)
