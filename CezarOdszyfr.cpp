#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const int ile = 36;
const char alph[ile] = { 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U', 'V', 'W', 'X', 'Y', 'Z',
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };

int main()
{
    int liczba_wystapien[ile];
    for (int i = 0; i < ile; i++)
    {
        liczba_wystapien[i] = 0; //zerowanie
    }

    int licznik_znakow = 0;
    char tmp_char;
    int tmp_int = 0;

    ifstream zaszyfrowany;
    zaszyfrowany.open("zaszyfrowany.txt");


    while (true)
    {
        zaszyfrowany >> tmp_char;
        if (zaszyfrowany.eof()) goto koniec;
        tmp_char = toupper((int)tmp_char);

        if (((int)tmp_char >= 48 && (int)tmp_char <= 57) || ((int)tmp_char >= 65 && (int)tmp_char <= 90))
        {
            licznik_znakow += 1;
            for (size_t i = 0; i < ile; i++)
            {
                if (tmp_char == alph[i])
                {
                    liczba_wystapien[i] += 1;
                }
            }
        }
    }

koniec:
    std::cout << "Tekst ma " << licznik_znakow << " znakow \n\n";
    /*for (size_t i = 0; i < ile; i++)
    {
        std::cout << alph[i] << " - " << ((float)liczba_wystapien[i]/(float)licznik_znakow)*100.0 << "%   --> " << liczba_wystapien[i] << "\n";
    }
    std::cout << "\n\n\n\n";*/

    char znaki[ile];
    for (size_t i = 0; i < ile; i++)
    {
        znaki[i] = alph[i];
    }
    
    for (size_t i = 0; i < ile; i++)
    {
        for (size_t j = i+1; j < ile; j++)
        {
            if (liczba_wystapien[j] > liczba_wystapien[i])
            {
                tmp_int = liczba_wystapien[i];
                liczba_wystapien[i] = liczba_wystapien[j];
                liczba_wystapien[j] = tmp_int;

                tmp_char = znaki[i];
                znaki[i] = znaki[j];
                znaki[j] = tmp_char;
            }
        }
    }


    for (size_t i = 0; i < ile; i++)
    {
        std::cout << znaki[i] << " - " << ((float)liczba_wystapien[i] / (float)licznik_znakow) * 100.0 << "%   --> " << liczba_wystapien[i] << "\n";
    }

    zaszyfrowany.close();
    return 0;
}
