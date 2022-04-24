<h1>Rock Paper Scissors "AI"</h1>

<p style="text-align:right">Revision for 0.0.1</p>

### List of contents:
1. Brief Introduction
2. Instructions
3. Console Example
4. Legal (MIT license)

<b><h2 style="text-align:center">Brief Introduction</h3></b>

---

A Rock Paper Scissors game application written in Python; competing against an “AI” (named <i>machine</i>), which produces predictions by generating a random choice from a binomial distribution of the user’s frequency of previous inputs. Interfaced by CLI.
With a player database to record statistics of performance over the duration of games.
* All usernames in the <i>CSV</i> (Comma-Seperated Values) database are represented as <i>hash_id</i>s, which are simply the output of the SHA256 function in hexadecimal (32 characters), with an input of the username.

<b><h2 style="text-align:center">Instructions</h3></b>

---

<h3>Packages</h3>

Prior to being interpreted the following <i>non-standard</i> packages must be installed to the enviroment:

```
numpy
keyboard
cursor
```

1. Clone (download) the repository locally.
2. Change the <i>pwd</i> directory to the <i>/src</i> subdirectory.
3. Enter `pip3 install -r requirements.txt` into a preferred CLI shell to download the necessary packages into the enviroment:

<h3>Play</h3>

1. Change the <i>pwd</i> directory (if not already) to the <i>/src</i> subdirectory.
2. Run <i>play.py</i> with the command `python3 play.py`
3. Follow the instructions printed on the CLI:
   * Input a username (case-sensitive).
   * Use the <i>left</i> and <i>right</i> arrow keys (or <i>a</i> and <i>d</i>) to change between rock, paper and scissors.
   * Press <i>enter</i> (or <i>e</i>) to confirm your choice.

<b><h2 style="text-align:center">Console Example</h3></b>

---

``` shell
username (case-sensitive): Ivan

Rock🪨, Paper📰, Scissors✂️

📰  Vs  📰  |  tie
✂️
```

``` shell
username (case-sensitive): Ivan

Rock🪨, Paper📰, Scissors✂️

📰  Vs  📰  |  tie
✂️  Vs  📰  |  user
🪨  Vs  📰  |  machine

Final Score:
user: 1
machine: 1

-----------

Statistics:
win streak:
  -current: 0
  -highest: 0
win rate: N/A

-----------
```

``` shell
Rock🪨, Paper📰, Scissors✂️

📰  Vs  🪨  |  user
🪨  Vs  🪨  |  tie
🪨  Vs  ✂️  |  user

Final Score:
user: 2
machine: 0

-----------

Statistics:
win streak:
  -current: 2
  -highest: 1
win rate: 0.5

-----------
```

<b><h2 style="text-align:center">License (MIT)</h3></b>

---
<br>

|Permissions|Conditions|Limitations|
|---|---|---|
|Commercial use|License and copyright notice|Liability|
|Distribution||Warranty|
|Modification|||
|Private use|||

```
MIT License

Copyright (c) 2022 Ivan (GitHub: ivanl-exe, E-Mail: ivan.exe@pm.me)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```