//Analiza Kasiskiego - odgadywanie dlugosci hasla

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

const int ile = 36;
const char alph[ile] = { '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U', 'V', 'W', 'X', 'Y', 'Z' };

int main()
{
    char tmp_char;
    string tmp_str = "";
    int tmp_int;

    ifstream zaszyfrowany;
    zaszyfrowany.open("zaszyfrowany.txt");

    std::vector<char> zaszyfrowany_tmp;
    //ofstream zaszyfrowany_tmp_out;
    //zaszyfrowany_tmp_out.open("zaszyfrowany_tmp.txt");

    //Pozbywanie sie nieszyfrowalnych znakow
    while (true)
    {
        zaszyfrowany >> std::noskipws >> tmp_char;
        if (zaszyfrowany.eof()) goto koniec1;

        if (((int)tmp_char >= 48 && (int)tmp_char <= 57) ||
            ((int)tmp_char >= 65 && (int)tmp_char <= 90) ||
            ((int)tmp_char >= 97 && (int)tmp_char <= 122))
        {
            //to mozna szyfrowac/deszyfrowac
            if ((int)tmp_char >= 97 && (int)tmp_char <= 122)
            {
                tmp_char = toupper((int)tmp_char);
            }

            //zaszyfrowany_tmp_out << tmp_char;
            zaszyfrowany_tmp.push_back(tmp_char);
        }
    }
koniec1:
    zaszyfrowany.close();
    //zaszyfrowany_tmp_out.close();


    //ifstream zaszyfrowany_tmp_in;
    //zaszyfrowany_tmp_in.open("zaszyfrowany_tmp.txt");

    
    const int M = 16;   //max dlugosc hasla
    int MTab[M];        //tab do wynikow
    int L = 3;          //dlugosc powtarzajacego kawalka
    int D = 0;          //odleglosc miedzy kawalkami

    int iledowczytania = 4;
    std::vector<char> TabWzor;   //tab do przechowania znakow wzorcowych
    std::vector<char> tabtmp;
    std::vector<char> wyciagniety;

    std::vector<char> tmpstring = { 'V','M','E' };

    for (size_t i = 0; i < M; i++) MTab[i] = 0; //zerowanie

    /* {
        //for (size_t q = 0; q < M; q++) //ile znakow ma byc pobierane do wzorca
        //{
            //petla 1 po tekscie
        for (size_t i = 0; i < zaszyfrowany_tmp.size() - L; i++)
        {
            //petla 2 po tekscie
            for (size_t j = L; j < zaszyfrowany_tmp.size(); j++)
            {
                wyciagniety.clear();
                wyciagniety.resize(0);

                for (size_t l = i; l < j - i; l++)
                {
                    wyciagniety.push_back(zaszyfrowany_tmp[l]);
                }

                //petla 3 po tekscie
                for (size_t k = i; k < j; k++)
                {
                    for (size_t l = 0; l < iledowczytania; l++)
                    {

                    }

                    //zliczanie powtorzen
                    if (j - i > M)
                    {
                        ////zerowanie
                        //for (size_t l = 0; l < M; l++)
                        //{
                        //    tabtmp[l] = '-';
                        //}
                        //
                        //for (size_t l = 0; l < M; l++)
                        //{
                        //    tabtmp[l] = zaszyfrowany_tmp[i+l];
                        //}


                    }
                }
            }
        }
        //}
    }*/

    bool sprawdzenie;
    string s1, s2;

    for (size_t l = 3; l < M; l++) //w kazdym przebiegu zasysana do testu inna ilosc liter
    {
        //std::cout << l << "\n"; //DEBUG ONLY
        for (size_t i = 0; i < zaszyfrowany_tmp.size()-M-l-1; i++)
        {
            //std::cout << "    " << l << " | " << (double)i / zaszyfrowany_tmp.size() << "\n"; //DEBUG ONLY
            for (size_t j = 0; j < l; j++)
            {
                TabWzor.push_back(zaszyfrowany_tmp[i + j]);//zaciaganie wzoru
                tabtmp.push_back(zaszyfrowany_tmp[i + l + j]); //zaciaganie do testu
            }

            for (size_t q = i+l+l+1; q < zaszyfrowany_tmp.size(); q++) //zaszyfrowany_tmp.size()-(i+l+1)
            {
                //std::cout << "        " << (float)l/M << " | " << (double)i / zaszyfrowany_tmp.size() << " -- " << (double)q / zaszyfrowany_tmp.size() << "\n"; //DEBUG ONLY

                tabtmp.erase(tabtmp.begin());
                tabtmp.push_back(zaszyfrowany_tmp[q]);

                if (TabWzor == tabtmp) 
                {
                    std::cout << "fgfdgsgdfg"; //DEBUG ONLY
                    //return 0;
                    MTab[l] += MTab[l] + 1;
                }
            }
        }
    }

    for (size_t i = L; i < M; i++)
    {
        std::cout << "M = " << i << " - " << MTab[i] << "\n";
    }

    //zaszyfrowany_tmp_in.close();
    return 0;
}