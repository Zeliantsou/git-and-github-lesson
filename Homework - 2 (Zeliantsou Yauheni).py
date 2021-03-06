{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Шаг1 - Количество символов в строке - 107\n",
      "Шаг2 - Развернутая строка - !акеволеч гурд — модварпу сан у А .акеволеч гурд — акабос мат ,тежоМ .алыб ен я ,енодноЛ в мат как ,юанз еН\n",
      "Шаг3 - Каждое слово строки с большой буквы - Не Знаю, Как Там В Лондоне, Я Не Была. Может, Там Собака — Друг Человека. А У Нас Управдом — Друг Человека!\n",
      "Шаг4 - Весь текст в строке прописными буквами -  НЕ ЗНАЮ, КАК ТАМ В ЛОНДОНЕ, Я НЕ БЫЛА. МОЖЕТ, ТАМ СОБАКА — ДРУГ ЧЕЛОВЕКА. А У НАС УПРАВДОМ — ДРУГ ЧЕЛОВЕКА!\n",
      "Шаг5 - Число вхождений \"нд\" - 1\n",
      "       Число вхождений \"ам\" - 2\n",
      "       Число вхождений \"о\"  - 7\n",
      "Шаг6 - Только первое слово строки с прописной буквы -  Не знаю, как там в лондоне, я не была. может, там собака — друг человека. а у нас управдом — друг человека!\n",
      "       Наименьший индекс подстроки \"не\" в исходной строке - 24\n",
      "       Все строчные \"о\" заменены на прописные \"О\" - Не знаю, как там в ЛOндOне, я не была. МOжет, там сOбака — друг челOвека. А у нас управдOм — друг челOвека!\n",
      "       Все буквы строки преобразованы в строчные - не знаю, как там в лондоне, я не была. может, там собака — друг человека. а у нас управдом — друг человека!\n",
      "       Выведен список слов исходной строки. Разделителем служит запятая - ['Не знаю', ' как там в Лондоне', ' я не была. Может', ' там собака — друг человека. А у нас управдом — друг человека!']\n",
      "Шаг7 - Исходная строка -  Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!\n"
     ]
    }
   ],
   "source": [
    "stroka = \"Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!\"\n",
    "print (\"Шаг1 - Количество символов в строке -\", len(stroka))\n",
    "print (\"Шаг2 - Развернутая строка -\", stroka[::-1])\n",
    "print (\"Шаг3 - Каждое слово строки с большой буквы -\", stroka.title())\n",
    "print (\"Шаг4 - Весь текст в строке прописными буквами - \", stroka.upper())\n",
    "print (\"Шаг5 - Число вхождений \\\"нд\\\" -\", stroka.count(\"нд\"))\n",
    "print (\"       Число вхождений \\\"ам\\\" -\", stroka.count(\"ам\"))\n",
    "print (\"       Число вхождений \\\"о\\\"  -\", stroka.count(\"о\"))\n",
    "print (\"Шаг6 - Только первое слово строки с прописной буквы - \", stroka.capitalize())\n",
    "print (\"       Наименьший индекс подстроки \\\"не\\\" в исходной строке -\", stroka.find(\"не\"))\n",
    "print (\"       Все строчные \\\"о\\\" заменены на прописные \\\"О\\\" -\", stroka.replace(\"о\", \"O\"))\n",
    "print (\"       Все буквы строки преобразованы в строчные -\", stroka.lower())\n",
    "print (\"       Выведен список слов исходной строки. Разделителем служит запятая -\", stroka.rsplit(\",\"))\n",
    "print (\"Шаг7 - Исходная строка - \", stroka)"
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
