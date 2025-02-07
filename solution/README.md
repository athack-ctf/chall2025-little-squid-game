# Solution

- Make sure you're using the same python version as the one used in the game otherwise, the RNGs might behave
  differently.

  ![](./screenshots/screenshot1.png)
  
  **IMPORTANT: USE THE PYTHON VERSION THAT THE RUNNING CHALLENGE GIVES YOU, NOT THE ONE ON THE SCREENSHOT.** 

- Fail 2 times (or more), and collect the generated numbers (for instance, `33368` and `17680`)
  ![](./screenshots/screenshot2.png)

- In [solution.py](./solution.py), populate `generated_numbers` with the collected numbers:

  ```
  generated_numbers = [
      33368,
      17680
  ]
  ```
- Execute `solution.py`. It should give you the next number.
    ```
    Next number to guess is 35482
    ```
- Enter the number to the game, and get the flag.
