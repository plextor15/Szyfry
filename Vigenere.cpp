#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const int ile = 36;
const char alph[ile] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U', 'V', 'W', 'X', 'Y', 'Z'};

int main()
{
    ofstream zaszyfrowany;
	ofstream odszyfrowany;
	ifstream niezaszyfrowany;
	ifstream zaszyfrowany2;

	bool koniec_pliku = false;
	bool co_robic = true; //true-szyfrowanie, false-odszyfrowanie
	int przesuniecie = 0;
	string haslo;
	int *TabPrzesu;
	int zapetlenie = 0;
	char tmp_char;
	string tmp_str = "";
	int tmp_int;

	std::cout << "Szyfrowanie [s], czy deszyfrowanie [d]?: ";
	std::cin >> tmp_char;
	if (tmp_char == 's')
	{
		co_robic = true;
	}
	if (tmp_char == 'd')
	{
		co_robic = false;
	}

	std::cout << "Podaj haslo: ";
	std::cin >> haslo;
    TabPrzesu = new int(haslo.size());
    for (int i = 0; i < (int)haslo.size(); i++)
    {
        for (int j = 0; j < ile; j++)
        {
            if(haslo[i] == alph[j])
            {
                TabPrzesu[i] = j;
                //std::cout << j << "\n"; //DEBUG ONLY!!
                break;
            }
        }
    }

//std::cout << "\n\n\n\n\n"; //DEBUG ONLY!!
    if (co_robic)
    {
/*
*	SZYFROWANIE
*/
        zaszyfrowany.open("zaszyfrowany.txt");
        niezaszyfrowany.open("niezaszyfrowany.txt");

        while (!koniec_pliku)
        {
            niezaszyfrowany >> std::noskipws >> tmp_char;
            if (niezaszyfrowany.eof()) goto koniec;

            if ( ((int)tmp_char >= 48 && (int)tmp_char <= 57) ||
				((int)tmp_char >= 65 && (int)tmp_char <= 90) ||
				((int)tmp_char >= 97 && (int)tmp_char <= 122) )
			{
				//to mozna szyfrowac/deszyfrowac
				if ( (int)tmp_char >= 97 && (int)tmp_char <= 122 )
				{
					tmp_char = toupper( (int)tmp_char );
				}

				przesuniecie = TabPrzesu[zapetlenie];

				for (size_t i = 0; i < ile; i++)
				{
					if (tmp_char == alph[i])
					{
						i += przesuniecie;
						tmp_int = i % ile;

						zaszyfrowany << alph[tmp_int];
						break;
					}
				}
			zapetlenie++;
			zapetlenie = zapetlenie % haslo.size();
			//std::cout << zapetlenie << "\n"; //DEBUG ONLY!!
            }
            else
            {
                zaszyfrowany << std::noskipws << tmp_char;
				zaszyfrowany.flush();
            }
        }

        koniec:
        zaszyfrowany.close();
        niezaszyfrowany.close();
    }
/*
*	ODSZYFROWYWANIE
*/
    else
    {
        odszyfrowany.open("odszyfrowany.txt");
		zaszyfrowany2.open("zaszyfrowany.txt");

		while (!koniec_pliku)
		{
			zaszyfrowany2 >> std::noskipws >> tmp_char;
				if (zaszyfrowany2.eof()) goto koniec;

			if (((int)tmp_char >= 48 && (int)tmp_char <= 57) ||
				((int)tmp_char >= 65 && (int)tmp_char <= 90))
			{

                przesuniecie = TabPrzesu[zapetlenie];

				for (size_t i = 0; i < ile; i++)
				{
					if (tmp_char == alph[i])
					{
						i += ile - przesuniecie;
						tmp_int = i % ile;

						odszyfrowany << alph[tmp_int];

					}
				}
				zapetlenie++;
				//zapetlenie = 0 - zapetlenie;
                zapetlenie = zapetlenie % haslo.size();
                //std::cout << zapetlenie << "\n"; //DEBUG ONLY!!
			}
			else
			{
				//przechodzi jak w oryginale
				odszyfrowany << std::noskipws << tmp_char;

			}
		}
koniec2:
		odszyfrowany.close();
		zaszyfrowany2.close();
    }


    return 0;
}
