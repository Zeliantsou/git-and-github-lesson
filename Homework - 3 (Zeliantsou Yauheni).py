{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите массу человека (кг):70\n",
      "Введите рост человека (м):1.8\n",
      "Ваш индекс массы тела: 21.6\n",
      "10============|============================50\n",
      "цена деления равна 1\n"
     ]
    }
   ],
   "source": [
    "m=float(input(\"Введите массу человека (кг):\"))\n",
    "h=float(input(\"Введите рост человека (м):\"))\n",
    "BMI=m/h**2\n",
    "print(\"Ваш индекс массы тела:\", round (BMI,1))\n",
    "int_BMI=int(round(BMI))\n",
    "tochka_na_shkale=int_BMI-10\n",
    "znachenie_do_konca_shkali=40-tochka_na_shkale\n",
    "print(\"10\"+\"=\"*tochka_na_shkale+\"|\"+\"=\"*znachenie_do_konca_shkali+\"50\")\n",
    "print(\"цена деления равна 1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
