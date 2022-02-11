{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "25fcc8e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d1abb6b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'D:\\\\Data_Science\\\\Python\\\\Training'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "da9b16d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "os.chdir(\"D:\\\\Data_Science\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "012c605a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'D:\\\\Data_Science'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "dd62c672",
   "metadata": {},
   "outputs": [],
   "source": [
    "var1=\"name\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "62b3b5bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name\n"
     ]
    }
   ],
   "source": [
    "print(var1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7ec539b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "del var1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "78315d00",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'var1' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4528/2529670587.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvar1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'var1' is not defined"
     ]
    }
   ],
   "source": [
    "print(var1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7bd0e061",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_4528/3524746678.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\Admin\\AppData\\Local\\Temp/ipykernel_4528/3524746678.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    def= 5\u001b[0m\n\u001b[1;37m       ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def= 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f87a4b98",
   "metadata": {},
   "outputs": [],
   "source": [
    "var1 = \"\"\"this is first line\n",
    "        this is second line\n",
    "        this is third line\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "96786cdb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is first line\n",
      "        this is second line\n",
      "        this is third line\n"
     ]
    }
   ],
   "source": [
    "print(var1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "40b1cae1",
   "metadata": {},
   "outputs": [],
   "source": [
    "a=list(range(100,999,8))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "837e6531",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100, 108, 116, 124, 132, 140, 148, 156, 164, 172, 180, 188, 196, 204, 212, 220, 228, 236, 244, 252, 260, 268, 276, 284, 292, 300, 308, 316, 324, 332, 340, 348, 356, 364, 372, 380, 388, 396, 404, 412, 420, 428, 436, 444, 452, 460, 468, 476, 484, 492, 500, 508, 516, 524, 532, 540, 548, 556, 564, 572, 580, 588, 596, 604, 612, 620, 628, 636, 644, 652, 660, 668, 676, 684, 692, 700, 708, 716, 724, 732, 740, 748, 756, 764, 772, 780, 788, 796, 804, 812, 820, 828, 836, 844, 852, 860, 868, 876, 884, 892, 900, 908, 916, 924, 932, 940, 948, 956, 964, 972, 980, 988, 996]\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c3dc0aae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,10):\n",
    "    print(i)\n",
    "    if(i==5):\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "902a5dc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def function1(a,b):\n",
    "    \"\"\"This is my docstring for my function which is adding 2 numbers\"\"\"\n",
    "    c=a+b\n",
    "    print(c)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "5cc93a4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is my docstring for my function which is adding 2 numbers\n"
     ]
    }
   ],
   "source": [
    "print(function1.__doc__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "fd21c6cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n"
     ]
    }
   ],
   "source": [
    "function1(10,15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "c8142872",
   "metadata": {},
   "outputs": [],
   "source": [
    "from my_package import assignment_package"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "63114e1e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'function5' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4528/2334160806.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mfunction5\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'function5' is not defined"
     ]
    }
   ],
   "source": [
    "function5()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "61c804ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "list1 = [a for a in range(0,100) if a%2!=0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "fcfeb13f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]\n"
     ]
    }
   ],
   "source": [
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "c4086374",
   "metadata": {},
   "outputs": [],
   "source": [
    "name = 'sudhakaran'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "ec0d35b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sudhakaran\n"
     ]
    }
   ],
   "source": [
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "201aff27",
   "metadata": {},
   "outputs": [],
   "source": [
    "def rem_vowels(string):\n",
    "    vowels = ['a','e','i','o','u']\n",
    "    name2 = [i for i in string if i.lower() not in vowels]\n",
    "    print(name2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "002260e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['s', 'd', 'h', 'k', 'r', 'n']\n"
     ]
    }
   ],
   "source": [
    "rem_vowels(name)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
