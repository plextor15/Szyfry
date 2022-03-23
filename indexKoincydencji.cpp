#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const int ile = 36;
const char alph[ile] = { '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U', 'V', 'W', 'X', 'Y', 'Z' };

//const int ile = 3;
//const char alph[ile] = {'A','B','C'};


int main()
{
    ifstream zaszyfrowany;
    zaszyfrowany.open("zaszyfrowany.txt");
    
    const int max_dlugosc_hasla = 20 - 2;//int min_dlugosc_hasla = 2;
    //double kolejne_IC[max_dlugosc_hasla];
    //double* IC;

    bool koniec_pliku = false;
    //int* TabPrzesu;
    //int zapetlenie = 0;
    char tmp_char;
    string tmp_str = "";
    //int tmp_int;
    double tmp_double;
    
    int DlugoscHasla = 5;
    int DlugoscHaslaI = 0; //ktory znak hasla
    std::cout << "Dlugosc hasla: ";
    std::cin >> DlugoscHasla;
    
    double* licznik_znakow = new double[DlugoscHasla];
    for (int i = 0; i < DlugoscHasla; i++)
    {
        licznik_znakow[i] = 0;
    }

    double* IC = new double[DlugoscHasla];
    for (size_t i = 0; i < DlugoscHasla; i++)
    {
        IC[i] = 0;
    }
    
     //liczba_wystapien;
    double** liczba_wystapien = new double*[DlugoscHasla];
    for (size_t i = 0; i < DlugoscHasla; i++)
    {
        liczba_wystapien[i] = new double[ile];
    }

    for (size_t j = 0; j < DlugoscHasla; j++)
    {
        for (int i = 0; i < ile; i++)
        {
            liczba_wystapien[j][i] = 0; //zerowanie
        }
    }

    DlugoscHaslaI = 0;

    //kolejna dlugosc hasla
    while (!koniec_pliku)
    {
        zaszyfrowany >> std::noskipws >> tmp_char;
        if (zaszyfrowany.eof()) goto koniec;

        if (((int)tmp_char >= 48 && (int)tmp_char <= 57) || ((int)tmp_char >= 65 && (int)tmp_char <= 90))
        {

            //licznik_znakow[DlugoscHaslaI] += 1;
            tmp_double = licznik_znakow[DlugoscHaslaI];
            tmp_double++;
            licznik_znakow[DlugoscHaslaI] = tmp_double;

            for (size_t i = 0; i < ile; i++)
            {
                if (tmp_char == alph[i])
                {
                    liczba_wystapien[DlugoscHaslaI][i] += 1;
                }
            }

            DlugoscHaslaI++;
            if (DlugoscHaslaI == DlugoscHasla)
            {
                DlugoscHaslaI = 0;
            }
            /*else
            {
                DlugoscHaslaI++;
            }*/
        }
    }

koniec:
    for (size_t j = 0; j < DlugoscHasla; j++)
    {
        for (int i = 0; i < ile; i++)
        {
            IC[j] += liczba_wystapien[j][i] * (liczba_wystapien[j][i] - 1);
        }
        IC[j] = IC[j] / (licznik_znakow[j] * (licznik_znakow[j] - 1));
    }
    
    
    /*for (int i = 0; i < ile; i++)
    {
        IC += liczba_wystapien[i] * (liczba_wystapien[i] - 1);
    }
    IC = IC / (licznik_znakow * (licznik_znakow - 1));*/

    double srdIC = 0;
    for (size_t i = 0; i < DlugoscHasla; i++)
    {
        srdIC += IC[i];
    }
    srdIC = srdIC / DlugoscHasla;

    //std::cout << "\n\nDEBUG ONLY!!\n\n"; //DEBUG ONLY!!
    std::cout << "\nSredni index koincydencji wynosi: " << srdIC << "\n\n";
    //std::cout << "\n\nDEBUG ONLY!!\n\n"; //DEBUG ONLY!!

    delete[] IC;
    delete[] licznik_znakow;
    for (size_t j = 0; j < DlugoscHasla; j++)
    {
        delete[] liczba_wystapien[j];
    }
    delete[] liczba_wystapien;

    return 0;
}
